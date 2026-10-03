#!/usr/bin/env bash
# 本批次全量门禁汇总（第 3 条提交门禁 + 逐章归属 + 写作侧兜底四件）。
# ⚠️ 原文件误用 python shebang + docstring，被 bash 当命令执行 ⇒ `line 4: 书目录: No such file`
#    （假红型：不影响任何门禁读数，但每次跑都刷一条错）。2026-09-29 已改为 bash 注释。
# 用法: bash scripts/gate.sh "<书目录>"
set -u
B="$1"
EPUB=$(ls "$B"/library/*.epub 2>/dev/null | head -1)
cd "$(git rev-parse --show-toplevel)"

# ⚠️ 2026-10-02 修正（Beach Read 第九轮）：**本脚本此前没有任何退出码聚合逻辑**——
#   退出码就是**最后一条管道**里 `tail` 的返回值，恒为 0。于是「bash gate.sh ⇒ exit 0」
#   这个信号**一直是空的**：⑱ 报出 28 章配额超限时，退出码照样是 0。
#   这与本项目已记录的「打印了成功」≠「文件改了」是同族：**量具报了失败，退出码说成功**。
#   ⇒ 落一份完整输出，末尾按「是否含 ❌」聚合退出码。
#   只认 ❌：⚠️（提示型）与 ❓（lane 降级不出结论）按 AGENTS 三档分类**不阻塞 commit**。
GATE_LOG="${TMPDIR:-/tmp}/englishread_gate_last.log"
exec > >(tee "$GATE_LOG")

echo "=== lane ==="
[ -n "$EPUB" ] && echo "完整 lane（有 epub）" || echo "降级 lane（无 epub）"

echo; echo "=== ① verify_quotes（引语逐字，对 epub；--full 关闭 52 字符指纹盲区）==="
# --full 只补一次整串/逐段 flat 比对并打印「--full 整串取证 N」计数；
# 它不参与退出码（verify_quotes.py:373 只看 bad/total/zero_fail），故不会让任何书误红。
if [ -n "$EPUB" ]; then python3 scripts/verify_quotes.py "$B" "$EPUB" --full 2>&1 | tail -4
else echo "❓ 无 epub，无法判定"; fi

echo; echo "=== ② check_vocab（词汇真实性/例句/分档）==="
python3 scripts/check_vocab.py "$B" 2>&1 | grep -E "词条行合计|FAIL \(|WARN \("

echo; echo "=== ③ check_entities（梗概实体一致性）==="
python3 scripts/check_entities.py "$B" 2>&1 | tail -1

echo; echo "=== ④ corruption_scan（编辑损坏，进门禁）==="
python3 scripts/corruption_scan.py "$B" 2>&1 | grep -E "FAIL|报告"

echo; echo "=== ⑤ sweep_full（引语整串 flat）==="
python3 scripts/sweep_full.py "$B" --quiet 2>&1 | grep -E "✅|❓"

echo; echo "=== ⑥ check_short_quotes（<20 字符短引语兜底）==="
python3 scripts/check_short_quotes.py "$B" 2>&1 | tail -2

echo; echo "=== ⑦ 逐章归属 check_chapter_quotes（不降级）==="
fail=0
for f in "$B"/ch*.md; do
  nn=$(basename "$f" | sed -E 's/^ch0*([0-9]+).*/\1/')
  out=$(python3 scripts/check_chapter_quotes.py "$nn" "$f" --out-dir "$B/text" 2>&1 | tail -1)
  case "$out" in *": "*) printf '%-46s %s\n' "$(basename "$f")" "$out";; *) fail=1; echo "❌ $f: $out";; esac
done
[ $fail -eq 0 ] && echo "（逐章归属：全部 X/X in 本章 text）"

echo; echo "=== ⑧ 块覆盖对账（每块都进 verify_quotes）==="
# ⚠️ 2026-09-29 修正：原写 `| tail -2` ⇒ **阻断型 ❌ 被藏掉**（ch37-39 批次实测：
# 实际有 ch39、ch45 两条 ❌ [被丢]，gate 只显示两条 ⚠️，exit 仍为 0）。
# 门禁汇总的唯一硬要求：**阻断型不许被任何截断隐藏**。
python3 scripts/check_block_coverage.py "$B" 2>&1 | grep -E "^(✅|❌|⚠️) |^❌ " | head -20
BLOCK8=$(python3 scripts/check_block_coverage.py "$B" 2>&1 | grep -c "^❌ " || true)
[ "$BLOCK8" -gt 0 ] && echo "⛔ 阻断型：$BLOCK8 个文件有块未进 verify_quotes 校验"

echo; echo "=== ⑨ 导航/总结层英文核对（六道门禁盲区）==="
# ⚠️ 2026-10-03 修正：本项原先 `| tail -1` 只留汇总行，条目明细看不见；
#   且 check_nav_layer 的 ❌ **条目行顶格打印**，与退出码聚合的判据
#   `^[[:space:]]+❌`（要求至少一个前导空格）对不上 ⇒ 阻断型被静默漏网
#   （实证：ch08 导航层一条「I knew he had to allow it」全书查无，聚合仍报 0 条）。
#   修法：去掉 tail -1 显示明细，并用 sed 统一缩进使其进入既有聚合判据。
python3 scripts/check_nav_layer.py "$B" --per-chapter 2>&1 | sed 's/^/  /'

echo; echo "=== ⑩ sweep_analysis_inline（分析层行内英文）==="
python3 scripts/sweep_analysis_inline.py "$B" 2>&1 | grep "逐字"

echo; echo "=== ⑪ audit_structure（结构；子项检查是假阴性高发点，0 不等于齐）==="
python3 scripts/audit_structure.py "$B" --quiet 2>&1 | tail -2

echo; echo "=== ⑫ check_anchor（关键词锚定）==="
python3 scripts/check_anchor.py "$B" 2>&1 | grep -E "凭空造词|松散关键词"

echo; echo "=== ⑬ 空段扫描（必备章节标题在 ≠ 内容在）==="
python3 - "$B" <<'PY'
import glob, re, sys
book = sys.argv[1]
bad = 0
for f in sorted(glob.glob(f"{book}/ch*.md"), key=lambda x: int(re.search(r"ch(\d\d)", x).group(1))):
    txt = open(f, encoding="utf-8").read()
    n = f.split("/")[-1]
    # 每章必备三节：导航 5 项 / 四子项齐全 / 一句话总结有正文
    # 一句话总结：标题后必须紧跟非空正文（空行也算空）
    m = re.search(r"^## 一句话总结[ \t]*\n(.*?)(?=\n## |\Z)", txt, re.M | re.S)
    if not m or not m.group(1).strip():
        print(f"❌ {n}: ## 一句话总结 有标题无正文（所有门禁都不查这一项）")
        bad += 1
    # 本章词汇 / 词汇分级：三档表头下每档至少一条词条
    # ⚠️ 2026-09-30 修正（Ghost Tales of the UK 终验实测 20 章假红）：非虚构论述档的
    #    节名是 `## 词汇分级`（非虚构档）而非 `## 本章词汇`（言情/精简档），
    #    原式只认后者 ⇒ 分档检查整段跳过。**两档节名都认**，任一命中即查。
    for vsec in ("本章词汇", "词汇分级"):
        v = re.search(rf"^## {vsec}(.*?)(?=\n## |\Z)", txt, re.M | re.S)
        if not v:
            continue
        tiers = re.split(r"(?m)^### ", v.group(1))[1:]
        for ti in tiers:
            rows = [x for x in ti.split("\n") if x.startswith("| ") and "词/短语" not in x and not x.startswith("|---")]
            # ⚠️ 2026-10-02 修正（The Whispers 终验实测 ch41 假红）：空档的**既有先例**
            #    是写一行中文说明（`（本章无高级词条）` / `（本章过短，无基础词条）`），
            #    原判据只认表格行 ⇒ 合法空档被报「只有表头没有词条」。
            #    **只放行独立成行的中文括号说明**；表格占位行（`| （本章无X词） | | |`）
            #    仍判红——它会被 check_vocab 判 FAIL，不是合法写法。
            if not rows and not any(re.fullmatch(r"\s*（本章[^）]*）\s*", x) for x in ti.split("\n")):
                print(f"❌ {n}: 词表档位「{ti.splitlines()[0].strip()}」只有表头没有词条")
                bad += 1
        break
    # 导航必备 5 项：**只判「项数 ≥5 且每项有正文」，不锁死标签措辞**——
    # 言情档写「Tropes 兑现/反转」、双时间线档写「本节在双线中的位置」、
    # 非言情精简档写「母题/冲突兑现/反转」；枚举标签会把每种正当写法都判成假红
    # （AGENTS 8.3：格式自成一派的书是合法的；假红型先修工具）。
    # ⚠️ 2026-09-30 修正（Ghost Tales of the UK 终验实测 20 章假红）：非虚构论述档的
    #    对应节是 `## 概览`（出处/作者/章节定位/字符数/一句话主旨 5 项），
    #    原式只认 `## 本章导航` ⇒ nav 为 None ⇒ 恒 0 条 ⇒ **全量假红**。
    #    **两档节名都认**（`本章导航` 或 `概览`），与 ⑬b 的判据一致。
    nav = None
    for nsec in ("本章导航", "概览"):
        nav = re.search(rf"^## {nsec}[ \t]*\n(.*?)(?=\n## |\Z)", txt, re.M | re.S)
        if nav:
            break
    # ⚠️ 冒号后**允许前导空格**（2026-09-30 Broken Light 终验实测）：
    #    原式 `：(\S.*)$` 要求首字符非空白，于是写成「**： 内容」（带一个空格）的
    #    5 个导航项全被判 0 条 —— ch21–ch25 五章假红，内容本身完好。
    #    前导空格是正常排版，不是缺陷；判据只该管「有没有正文」。
    # 导航项数下限 **≥4**（2026-09-30 修正，原写死 5 ⇒ 精简格式全量假红）：
    #   5 项是**长篇言情档**的写法（一句话概括/情感弧线位置/Tropes 兑现反转/
    #   人物弧线/叙事手法）。**精简格式（四子项档）本库主流是 4 项**——
    #   一句话概括/情感弧线位置/人物弧线/叙事手法，**没有 Tropes 一栏**
    #   （Tropes 是言情专属，非言情书写它是硬填项，AGENTS 8.3）。
    #   实测（I Can't Save You 精读 12 章，2026-09-30 终验）：4 项规整、
    #   每项均有正文、内容完好，却被写死的 `5` 判成 12 处假红。
    #   **判据该管的是「有没有缺项/有没有正文」，不是「体裁规定的项数」**——
    #   与本段上方「不锁死标签措辞」同一原则：格式自成一派的书是合法的。
    #   取 4 为下限：两种体裁都过，且仍能抓住真正「导航写崩」的文件（0–3 项）。
    items = re.findall(r"(?m)^[-*]?\s*\*\*([^*]+)\*\*[：:]\s*(\S.*)$", nav.group(1)) if nav else []
    if len(items) < 4:
        print(f"❌ {n}: 导航/概览 粗体项 {len(items)} 条 < 4（缺项或写法不匹配 `**X**：`）")
        bad += 1
    for k, v in items:
        if not v.strip():
            print(f"❌ {n}: 导航项「{k}」有标题无正文")
            bad += 1
print(f"=== 空段扫描：{bad} 处 ===")
sys.exit(2 if bad else 0)
PY

# ⑭⑮ 2026-09-29 增补：原 13 项**漏了总览三篇**，而 AGENTS 第 3 条明写「总览文件
# 不在 verify_quotes 主口径内，须单独加跑 verify_overview_quotes」⇒ 一本有总览的书
# 跑完原 gate.sh 全绿，**总览引语从未被校验**（同型实测：概述 5 条 0 命中而门禁全绿）。
echo; echo "=== ⑭ verify_overview_quotes（总览三篇引语；有 00_* 才跑）==="
OV=$(ls "$B"/00_*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$OV" -gt 0 ]; then
  if [ -n "$EPUB" ]; then
    # 签名是「书目录 + epub」两参，它自己扫该目录下的 00*.md——不是单文件
    python3 scripts/verify_overview_quotes.py "$B" "$EPUB" 2>&1 | tail -6
  else echo "❓ 无 epub，无法判定（总览 ${OV} 篇）"; fi
else echo "（无总览三篇，本项不适用）"; fi

echo; echo "=== ⑮ check_overview_full（章节标签对账 + H1 语义；条件性）==="
if [ "$OV" -gt 0 ]; then
  [ -n "$EPUB" ] && python3 scripts/check_overview_full.py "$B" "$EPUB" 2>&1 | tail -1 \
                || echo "❓ 需 epub，本项不判定"
else echo "（无总览三篇，本项不适用）"; fi

# ⑯ 2026-10-02 新增（Beach Read 第四轮终验）：分析层**跨章指认**核对。
#   起因：`check_crossref` 只报「查无」，**不报「归错章」**——而 Beach Read 实测
#   11 处阻断型全是后者（片段真实存在，只是不在被引章），且**系统性往前偏 1–2 章**。
#   它不违反任何引语规则 ⇒ 前 15 项**全部放行**。本项分两档：
#     ❌ 伪造（全书查无）  阻断型，必须改；脚本对这一档返回 2
#     ⚠️ 移章（不在被引章）**只记不改**——「回望前章」是正当写法，真错与正当在这里同形，
#        机械阻断会把正当内容改坏；**必须人工读行并把处置写进报告**（Beach Read 11 处即如此查出）
echo; echo "=== ⑯ check_xref_chapter（分析层跨章指认；❌阻断 / ⚠️须人工读行）==="
python3 scripts/check_xref_chapter.py "$B" 2>&1 | sed -n '1,40p'


# ⑰ 2026-10-02 新增（Beach Read 第八轮，验证器指出）：**引语块结构对账**。
#   起因：ch21 出现**引语行丢失 `> ` 前缀**（`**原句 10:**` 不带 `>`）＋**原句 9/10 倒序且撞车**
#   ＋**写作期自查记录泄漏到成品**；ch18 出现**孤儿分析**（四个子项齐全、上方无引语行）。
#   **这类损坏对六道引语门禁全部不可见**——它们只解析带 `> ` 的引语行，丢了前缀的行在它们
#   眼里根本不是引语；而「孤儿分析」是少了一行，多出来的东西没有任何检查会报。
#   五种判据：缺前缀 / 编号倒序 / 编号撞车 / 孤儿分析 / 自查泄漏。
echo; echo "=== ⑰ check_quote_blocks（引语块结构：前缀/编号/孤儿/泄漏）==="
python3 scripts/check_quote_blocks.py "$B" 2>&1 | head -40


# ⑱ 2026-10-02 新增（Beach Read 第九轮）：**引语块配额 + 关键词锚定 + 拼接红线**。
#   起因（本项目第 4 次同形态失误）：`check_block_keywords` **从未接进正门**，
#   于是前 17 项全绿的情况下——① 28 章**每章 12–23 块、全部超出体裁表 3–8 处配额**，
#   ② 17 处关键词越界／删词（not to→not、plural "books,"→plural "books"）全部漏网。
#   教训同前三次：**「以为跑了 gate.sh 就够」**——正门本身也有覆盖缺口，
#   接进门禁的检查器集合**必须对着 `ls scripts/` 清点过**。
#   本项同时兜住两个此前无人负责的层：块数配额（体裁表）与关键词逐字锚定。
echo; echo "=== ⑱ check_block_keywords（块数配额 3–8 处 / 关键词锚定 / 拼接红线）==="
python3 scripts/check_block_keywords.py "$B" 2>&1 | tail -32


# ---- 退出码聚合（2026-10-02 新增，见文件头说明）----
# ⚠️ 上一版用 `exec >/dev/tty` 把汇总行打回终端，在 stdout 被重定向到文件/管道的
#   场景下 /dev/tty 不存在 ⇒ exec 失败把 stdout 置坏，汇总行根本没打出来，退出码仍 0。
#   ⇒ 不做任何 fd  gymnastics：直接读 tee 落下的日志。sleep 只是等 tee 刷缓冲。
sleep 0.3
# ⚠️ 2026-10-02 第二次修正：不能简单 `grep -c "❌"`——各工具的**汇总行本身就含 ❌ 字形**
#   却报 0（`❌ 结构缺陷 0 ｜ ⚠️ 提示 1`、`❌ 凭空造词 0 处`），第一版把 28 条真阻断
#   数成 36。判据：缩进 ❌ **条目行**（工具逐条打印的问题），排除
#   ① 含 `｜` 的汇总行  ② 含 ` 0 ` 的零计数行。
_gfail=$(grep -E '^[[:space:]]+❌' "$GATE_LOG" 2>/dev/null | grep -v '｜' | grep -v ' 0 ' | wc -l | tr -d ' ')
_gfail=${_gfail:-0}
if [ "$_gfail" -gt 0 ]; then
  echo "══ 正门结论：❌ ${_gfail} 条阻断型（见上；退出码 1）══"
  exit 1
fi
echo "══ 正门结论：0 条阻断型（⚠️/❓ 不阻塞；退出码 0）══"
exit 0
