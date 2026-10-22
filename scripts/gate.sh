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
# ⚠️ 2026-10-05 修正（The Edge of Water ch20 实测假红）：`exec > >(tee "$GATE_LOG")`
#   在受限沙箱里**静默失败**（`line 18: /dev/fd/62: Operation not permitted`，
#   既不写日志也不影响后续命令的 stdout），于是末尾聚合读到的是**上一次、别的书**
#   留下的旧日志 ⇒ 报出一条本次根本没跑出来的阻断型。
#   **根因与「量具报了失败，退出码说成功」同族，但方向相反：量具根本没量，读的是陈旧读数。**
#   ⇒ 改为「全量落盘 + 退出时回显」，且**必须先把原 stdout 存到 fd 3**：
#     `exec > "$GATE_LOG"` 之后 trap 里的 `cat` 若不重定向到 fd 3，
#     就会**把日志 cat 回日志自己**（`cat f > f`），得到一行空白 + 陈旧计数。
# ⚠️ 同日第二次修正（实测仍在假红）：`$GATE_LOG` 是**固定路径**，本工作区多 IDE 并行，
#   另一个 agent 的 gate.sh 会在我们 `cat` 的同时 `: > "$GATE_LOG"` 截断同一文件 ⇒
#   读到 5 行（一行正文 + 一整行空白），末尾聚合也读到**别人的** 101 行输出。
#   **教训（与 10-02 那次同族）：固定路径的共享临时文件 = 并行下的竞态源，
#     「量具读数」在多进程下根本不属于本次运行。** ⇒ 路径加 `$$`（每次运行唯一）。
GATE_LOG="${TMPDIR:-/tmp}/englishread_gate_last.$$.log"
exec 3>&1
: > "$GATE_LOG"
exec > "$GATE_LOG"
# shellcheck disable=SC2064
trap "cat '$GATE_LOG' >&3" EXIT
trap 'echo "gate.sh 中途中止（set -u 未定义变量等），以上为中止前的输出。" >&2' ERR

# 2026-10-20：**双轨聚合**。文本层数 ❌ 曾三次把真阻断洗成绿灯（见文件头 ①②③）。
# 现改为「退出码层 + 文本层」双轨：任一层报阻断即红；两层不一致时把不一致本身打出来
# ——那正是历次假绿的形态。
# ⚠️ rc 层目前只覆盖 5 个 lane（② check_vocab / ③ check_entities / ⑦ 逐章归属 /
#    ⑧ 块覆盖 / ⑲ 中文层），因为它们的退出码语义已明确（1=阻断，2=未判定）。
#    其余 14 个 lane 的 rc 语义尚未逐个核实（多个工具把 ⚠️ 提示也放进非零退出码），
#    **先不盲目扩大 rc 层**：把提示型判成阻断会在全库制造假红，比漏报更贵。
RC_BLOCK=0
RC_WHICH=""
_blk() { RC_BLOCK=$((RC_BLOCK+1)); RC_WHICH="$RC_WHICH $1"; }

echo "=== lane ==="
[ -n "$EPUB" ] && echo "完整 lane（有 epub）" || echo "降级 lane（无 epub）"

echo; echo "=== ① verify_quotes（引语逐字，对 epub；--full 关闭 52 字符指纹盲区）==="
# --full 只补一次整串/逐段 flat 比对并打印「--full 整串取证 N」计数；
# 它不参与退出码（verify_quotes.py:373 只看 bad/total/zero_fail），故不会让任何书误红。
if [ -n "$EPUB" ]; then python3 scripts/quotes.py verbatim "$B" "$EPUB" --full 2>&1 | tail -4
else echo "❓ 无 epub，无法判定"; fi

echo; echo "=== ② check_vocab（词汇真实性/例句/分档）==="
# ⚠️ 2026-10-19 修**假绿**（Maybe Next Time 批次实测）：
#   原写法 `| grep -E "词条行合计|FAIL \(|WARN \("` **只打印** `FAIL (147)` 这行文字，
#   **不把 FAIL 计入退出码** ⇒ gate.sh 报「0 条阻断型 · 退出码 0」而 check_vocab 实际 FAIL 147。
#   ⇒ 改为与 ③ lane 同一口径：**先取退出码，再按结论行判红**。
#   （判据仍是「结论/退出码」，不是 grep 匹配与否——记忆 #2048。）
# ⚠️ 2026-10-19 同步（与 ③ 同一处假警报）：check_vocab 在 FAIL>0 时退出码 1，
#   原式会让它触发 ERR trap 打印「中途中止」——脚本仍跑完，但读数误导。
#   同样改成 `&& A || B` 形式捕获退出码，判定逻辑不变。
_cv_out=$(python3 scripts/check_vocab.py "$B" 2>&1) && _cv_rc=0 || _cv_rc=$?
echo "$_cv_out" | grep -E "词条行合计|FAIL \(|WARN \("
# ⚠️ 2026-10-20 第三方复核指出：本 lane 原用 `-ne 0`，而 ③⑲ 用 `-eq 1`。
#   今天无害（check_vocab 从不返回 2），但 20-gate.md 的降级 lane 表若将来引入
#   exit 2（未判定），`-ne 0` 会把「未核」算成「阻断」——与「跳过型 ≠ 干净」直接冲突。
#   ⇒ 改成与 ③⑲ 同口径：rc==1 阻断、rc==2 明示「未核」、rc==0 通过。
if [ "$_cv_rc" -eq 2 ]; then
  echo "❓ check_vocab 无法判定（rc=2）——**未核不是通过**"
elif [ "$_cv_rc" -ne 0 ]; then
  echo "--- check_vocab 阻断明细（FAIL 非 0）---"
  echo "$_cv_out" | awk '/^--- FAIL/,/^--- WARN/' | grep -E "^  ch" -A1 | head -40
  echo "❌ check_vocab FAIL != 0（词表层缺陷：例句不命中本章 / 词条虚构 / 占位符）"
fi
[ "$_cv_rc" -eq 1 ] && _blk "②check_vocab"

echo; echo "=== ③ check_entities（梗概实体一致性）==="
# ⚠️ 2026-10-18：本 lane 原为 `| tail -1`，而 check_entities 修完真空绿后
# 0 段时输出**多行**（列出该书实际 H2 标题 + ❓ 无法判定），`tail -1` 只取到
# 标题行 ⇒ **「无法判定」这一句会被吞掉，板面/日志上看着像正常跑过**。
# ⇒ 改为 grep 出「❓ / ❌ / ⚠️」三类关键行；exit 2 是「未判定」，不进阻断聚合
#   （与 ① 无 epub 同口径，见文件头「只认 ❌」）。
# ⚠️ 2026-10-19 修正（captain-s-dinner 实测假警报）：原式
#   `_ce_out=$(python3 ... ); _ce_rc=$?`
# 会让**退出码 2（未判定，属合法结果）触发文件头的 ERR trap**，把
# 「gate.sh 中途中止」打到 stderr——**而脚本其实跑完了 19 lane**。
#   ⇒ 读日志的人会以为门禁没跑完，从而把「③ 实体层未核」误读成「干净」
#   （与文件头记的第 ①②③ 次「汇总层误导读数」同族）。
#   修法＝用 `&& A || B` 形式捕获退出码：失败命令不在 &&/|| 列表末尾 ⇒ 不触发 ERR trap，
#   而 `$?` 仍是 python 的退出码，判定逻辑一字未改。
_ce_out=$(python3 scripts/check_entities.py "$B" 2>&1) && _ce_rc=0 || _ce_rc=$?
if [ "$_ce_rc" -eq 2 ]; then
  echo "$_ce_out" | grep -E '❓|⚠️ 口径只认'
elif [ "$_ce_rc" -ne 0 ]; then
  echo "$_ce_out" | grep -E '❌|^===' | tail -8
else
  echo "$_ce_out" | tail -1
fi
[ "$_ce_rc" -eq 1 ] && _blk "③check_entities"

echo; echo "=== ④ corruption_scan（编辑损坏，进门禁）==="
# ⚠️ 2026-10-05 五步审查修（I Am Not Jessica Chen 实证）：本项原写
#   `| grep -E "FAIL|报告"`，输出行是 `  FAIL 2 处（U+FFFD / 双句号）`——
#   **不含 ❌**，而正门结论的聚合判据是 `^[[:space:]]+❌` ⇒ **本项的 FAIL
#   完全不进「正门结论」**；同段那行 `报告 0 处（…）` 又含 ` 0 ` 被
#   `grep -v ' 0 '` 排除。后果：第 3 条明列的进门禁项报着 FAIL，
#   正门结论照样打「0 条阻断型 · 退出码 0」——**汇总层把真阻断洗成绿灯**
#   （实测：ch17:98 / ch19:28 两处 U+FFFD 在批次四与完工两轮 gate 里
#   都真实存在且被本项抓到，写作方却据正门结论宣布完工）。
#   与 2026-09-29「gate.sh 漏 verify_overview_quotes」同族复发。
#   修法：把 FAIL 行缩进并加 ❌ 标记，使其进入既有聚合判据；
#   **零计数时不得加标记**（否则每本书都会平白 +1）。
python3 scripts/corruption_scan.py "$B" 2>&1 | grep -E "FAIL|报告" \
  | sed -E 's/^  FAIL ([0-9]+) 处/  ❌ FAIL \1 处/'

echo; echo "=== ⑤ sweep_full（引语整串 flat）==="
python3 scripts/quotes.py full "$B" --quiet 2>&1 | grep -E "✅|❓"

echo; echo "=== ⑥ check_short_quotes（<20 字符短引语兜底）==="
python3 scripts/quotes.py short "$B" 2>&1 | tail -2

echo; echo "=== ⑦ 逐章归属 check_chapter_quotes（不降级）==="
fail=0
for f in "$B"/ch*.md; do
  nn=$(basename "$f" | sed -E 's/^ch0*([0-9]+).*/\1/')
  out=$(python3 scripts/quotes.py chapter "$nn" "$f" --out-dir "$B/text" 2>&1 | tail -1)
  # 2026-10-20 修假红：NO_LONG_QUOTES = 「本章没有 ≥阈值的引语，短引语未逐章校验」，
  # 那是**未核**不是缺陷——而且 ⑥ check_short_quotes 已在书级 + 跨章归属两层兜过短引语。
  # 原写法把它落进 `*)` 分支打成 ❌ 阻断（finding-darla ch12 实测：整本书因此 exit 1，
  # 而 ⑥ 报「命中 26 ｜ 在别的章 0 ｜ 查无 0」，引语层其实是干净的）。
  case "$out" in
    *": "*) printf '%-46s %s\n' "$(basename "$f")" "$out";;
    *NO_LONG_QUOTES*) echo "❓ $(basename "$f"): 短引语未逐章校验（由 ⑥ 兜底，不算阻断）";;
    *) fail=1; echo "❌ $f: $out";;
  esac
done
[ $fail -eq 0 ] && echo "（逐章归属：全部 X/X in 本章 text）"
[ $fail -ne 0 ] && _blk "⑦逐章归属"

echo; echo "=== ⑧ 块覆盖对账（每块都进 verify_quotes）==="
# ⚠️ 2026-09-29 修正：原写 `| tail -2` ⇒ **阻断型 ❌ 被藏掉**（ch37-39 批次实测：
# 实际有 ch39、ch45 两条 ❌ [被丢]，gate 只显示两条 ⚠️，exit 仍为 0）。
# 门禁汇总的唯一硬要求：**阻断型不许被任何截断隐藏**。
python3 scripts/quotes.py coverage "$B" 2>&1 | grep -E "^(✅|❌|⚠️) |^❌ " | head -20
BLOCK8=$(python3 scripts/quotes.py coverage "$B" 2>&1 | grep -c "^❌ " || true)
[ "$BLOCK8" -gt 0 ] && echo "⛔ 阻断型：$BLOCK8 个文件有块未进 verify_quotes 校验"
[ "$BLOCK8" -gt 0 ] && _blk "⑧块覆盖"

echo; echo "=== ⑨ 导航/总结层英文核对（六道门禁盲区）==="
# ⚠️ 2026-10-03 修正：本项原先 `| tail -1` 只留汇总行，条目明细看不见；
#   且 check_nav_layer 的 ❌ **条目行顶格打印**，与退出码聚合的判据
#   `^[[:space:]]+❌`（要求至少一个前导空格）对不上 ⇒ 阻断型被静默漏网
#   （实证：ch08 导航层一条「I knew he had to allow it」全书查无，聚合仍报 0 条）。
#   修法：去掉 tail -1 显示明细，并用 sed 统一缩进使其进入既有聚合判据。
python3 scripts/analysis.py nav "$B" --per-chapter 2>&1 | sed 's/^/  /'

echo; echo "=== ⑩ sweep_analysis_inline（分析层行内英文）==="
python3 scripts/analysis.py inline "$B" 2>&1 | grep "逐字"

echo; echo "=== ⑪ structure.py audit（结构；子项检查是假阴性高发点，0 不等于齐）==="
python3 scripts/structure.py audit "$B" --quiet 2>&1 | tail -2

echo; echo "=== ⑫ structure.py anchor（关键词锚定）==="
# ⚠️ 2026-10-13 修正（Some Other Time 实测）：本行原为裸 `| grep -E "凭空造词|松散关键词"`，
#   而 grep **无匹配时退出码 1** ⇒ 触发文件头的 ERR trap，把
#   「gate.sh 中途中止（set -u 未定义变量等）」打到 stderr——**而脚本其实跑完了**。
#   本次实测的触发场景：`check_anchor.py` 对「关键词标签独占行 + 逐条 `- **词**：释义`」
#   这种格式收不到关键词（报 ❓ 无法判定、退出码 2），于是两行汇总都不打印 ⇒ grep 落空。
#   后果与文件头记载的前三次同族：**汇总层误导读数**——看日志的人会以为本次门禁没跑完，
#   从而忽略「⑫ 这一层根本没检查」这个真事实。⇒ 加 `|| true`（与下方 ⑱ 同一写法）。
python3 scripts/structure.py anchor "$B" 2>&1 | grep -E "凭空造词|松散关键词|无法判定" || true

echo; echo "=== ⑬ 空段扫描（必备章节标题在 ≠ 内容在）==="
python3 - "$B" <<'PY'
import glob, re, sys
book = sys.argv[1]
bad = 0
for f in sorted(glob.glob(f"{book}/ch*.md"), key=lambda x: int(re.search(r"ch(\d\d)", x).group(1))):
    txt = open(f, encoding="utf-8").read()
    n = f.split("/")[-1]
    # 每章必备三节：导航 5 项 / 四子项齐全 / 一句话总结有正文
    # 一句话总结：支持 ## 一句话总结（书籍格式）和 ### 一句话总结（言情精简格式）
    m = re.search(r"^#{2,3} 一句话总结[ \t]*\n(.*?)(?=\n## |\Z)", txt, re.M | re.S)
    if not m or not m.group(1).strip():
        print(f"❌ {n}: 一句话总结 有标题无正文（所有门禁都不查这一项）")
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
            # ⚠️ 2026-10-10 修正（The Man ch02/ch71/ch79 实测假红）：
            #    原判据只认表格行（`| ` 前缀），但本书使用 bullet 列表格式
            #    （`- **word** ⭐⭐⭐ — 释义`）=> rows 恒为空，合法词表被误判。
            #    **同时认表格行和 bullet 行**作为有效词条。
            rows = [x for x in ti.split("\n")
                    if (x.startswith("| ") and "词/短语" not in x and not x.startswith("|---"))
                    or x.startswith("- **")]
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
    # ⚠️ 2026-10-06 修正（The Language of Knives 批1 实测 4 章假红）：
    #    短篇合集用 `## 本篇导航`（体裁表逐篇精读格式；权威样本
    #    the-passing-of-the-dragon-by-ken-liu/ch01），而 check_entities 早在
    #    2026-09-27 就补过这一档，**gate.sh 这一处漏了** ⇒ nav 恒 None ⇒ 0 条 ⇒ 全量假红。
    #    修法与本段上方「两档节名都认」同一原则：**三档节名都认**。
    for nsec in ("本章导航", "概览", "本篇导航", "导航/概览", "导航", "视角笔记"):
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
    # ⚠️ 2026-10-06 修正（The Language of Knives 批2 实测 1 章假红）：原式**锁死冒号**，
    #   而本库推荐的导航层分隔符是 `·`（check_vocab 明确建议「概述/导航层避免用 | ，改用 ·」）
    #   ⇒ 用 ` · ` 分隔且内容完好的导航被判「粗体项 2 条 < 4」。
    #   这与本段上方「只判项数与正文、不锁死标签措辞」同一原则：**分隔符也不该锁**。
    # ⚠️ 2026-10-08 新增（The Man ch07/ch73 等实测）：
    #   本库同时存在两种导航项格式：
    #   Format A: **key**：value —— 分隔符（：）在 bold 外；ch05 等多数章节
    #   Format B: **key：** value —— 分隔符在 bold 内；ch07 等
    #   原模式只匹配 Format A，Format B 恒 0 条 ⇒ 53 章假红。
    #   新代码跑四个 pattern 并合并结果。
    if nav:
        txt = nav.group(1)
        # Format A: **key**：value (separator outside bold) / **key**（value）（中文括号分隔）
        items = re.findall(r"(?m)^[-*]?\s*\*\*([^*：]+)\*\*\s*(?:[：:]|\u00b7|\u2014|\u2013|（)\s*(.+)$", txt)
        # Format B: **key：** value (separator inside bold)
        items += re.findall(r"(?m)^[-*]?\s*\*\*([^*：：]+[：:])\*\*\s+(\S.+)$", txt)
        # Format C: 【**key**】value 或 **key**（单行括号包裹的标签，纯标签行也计数）
        items += re.findall(r"(?m)^【?\s*\*\*([^*]+)\*\*\s*】?\s*[:：]?\s*(.*)$", txt)
        items += [(k, v) for k, v in re.findall(r"(?m)^\s*\*\*([^*]+)\*\*\s*$/", txt)]
        # Format D: Markdown link list navigation（[ch07...](#ch07...)）—— 每条链接计 1 项
        link_items = re.findall(r"\[([^\]]+)\]\([^\)]+\)", txt)
        items += [(link, '') for link in link_items]
        # 去重（Format A 和 Format C 会重复匹配同一行）
        seen = set()
        unique_items = []
        for k, v in items:
            if k not in seen:
                seen.add(k)
                unique_items.append((k, v))
        items = unique_items
        # ⚠️ 2026-10-09 修正（Maybe Once, Maybe Twice ch08–ch31 实测）：
        #   言情精简格式用 Markdown 链接列表做导航（如 `[ch07...](#ch07...)`），
        #   每条链接计 1 项。link-list 格式天然有 3 项（上一章/本章/下一章），
        #   而 bold-key-value 格式用 4 项结构——两种都是合法写法，不应因格式不同而判不同的档。
        #   下限取 3：link-list 3 项全通过，bold-key-value 4 项也通过。
        min_items = 3
    else:
        items = []
        min_items = 4
    if len(items) < min_items:
        print(f"❌ {n}: 导航/概览 粗体项 {len(items)} 条 < {min_items}（缺项或格式不匹配）")
        bad += 1
    for k, v in items:
        # Markdown link list items have empty value by design; skip the "无正文" check for them
        if not v.strip() and not re.match(r'^ch\d+', k):
            print(f"❌ {n}: 导航项「{k}」有标题无正文")
            bad += 1
print(f"=== 空段扫描：{bad} 处 ===")
sys.exit(2 if bad else 0)
PY

# ⑭⑮ 2026-09-29 增补：原 13 项**漏了总览三篇**，而 AGENTS 第 3 条明写「总览文件
# 不在 verify_quotes 主口径内，须单独加跑 verify_overview_quotes」⇒ 一本有总览的书
# 跑完原 gate.sh 全绿，**总览引语从未被校验**（同型实测：概述 5 条 0 命中而门禁全绿）。
echo; echo "=== ⑭ verify_overview_quotes（总览三篇引语；有 00_* 才跑）==="
# 2026-10-15 兼容空格型总览命名（these-vengeful-wishes 五步审查实证）：
# 本库总览既有 `00_概述.md`（192 个）也有 `00 概述.md`（21 个）两种形态，
# 只认 `00_*` 会让空格型整本判「无总览三篇」⇒ ⑭⑮ 双双空跑，
# 总览引语与章节标签从未进门禁（同型：概述 5 条 0 命中而门禁全绿）。
# 2026-10-17 再修：加空格仍不够——裸 `概述.md`/`金句精选.md`/`情感节点.md`
# （无编号）、`00概述.md`（无分隔）、`01_金句精选.md`/`02_情感节点.md`、`00_全书概述.md`
# 全在口径外 ⇒ 实测 **22 本书目录**被 ⑭⑮ 判「本项不适用」而**整本总览从未进门禁**，
# 比空格型那批更大（静默跳过型假绿，第四档）。
# 处置：与 `check_overview_full.py` / `verify_overview_quotes.py` / `check_overview_labels.py`
# 四处统一改**语义关键词**判据（`概述|金句|情感节点`），不再依赖编号前缀。
# 全库章级文件（`chNN` 开头）含该三词的 0 个，故不会把章节文件当总览。
# 2026-10-22 三修（三处漏洞一次补齐，用户拍板 1+2+3）：
#   ① **英文命名漏收**：中文语义关键词之外，本库还有 `00_overview.md` / `01_quotes.md` /
#      `02_emotional_nodes.md` / `00 golden quotes.md` / `00 emotional moments.md` 等英文命名，
#      实测 **7 本书**（a-sea-of-unspoken-things / the-last-thing / forest-of-scars / lost /
#      the-girl-from-the-war-room / wolf-hour / books-that-saved-my-life）因此被 ⑭⑮ 判
#      「本项不适用」⇒ 总览引语与章节标签从未进门禁。文件名识别统一到
#      `scripts/overviewcheck/names.py`（三处工具 + gate 同一实现）。
#   ② **「口径外」不判红**：`overview.py quotes` 在整篇口径外时**退出码 1**，但原式
#      `… | tail -6` 把退出码吃掉了，而 rc 层只覆盖 ②③⑦⑧⑲⑳、口径外那行又是 ⚠️ ⇒
#      **一整篇总览零核验而 gate EXIT=0**（habits 概述 11 条行内引语实证）。现接住退出码。
#   ③ **没有总览也算「不适用」**：全库 23 本小说/悬疑/非虚构没有任何总览文件，
#      而 profile 要求 3 篇 ⇒ 现打一行提示（不判红：书可能在写）。
OV=$(python3 scripts/overview.py names "$B" 2>/dev/null | wc -l | tr -d ' ')
NEED=$(python3 scripts/overview.py need "$B" 2>/dev/null || echo "?")
if [ "$OV" -gt 0 ]; then
  # 2026-10-22 补：无 epub 也要跑（工具本身有降级 lane，用 `text/` 兜底）。
  # 原式 `[ -n "$EPUB" ]` 直接跳过 ⇒ 7 本英文总览书**全部无 epub**，
  # 即使文件名识别修好了，⑭ 仍会打印「❓ 无 epub，无法判定」= 跳过型假绿。
  OVLOG=$(mktemp)
  if [ -n "$EPUB" ]; then
    # 签名是「书目录 + epub」两参，它自己扫该目录下的总览件——不是单文件
    python3 scripts/overview.py quotes "$B" "$EPUB" >"$OVLOG" 2>&1
  else
    python3 scripts/overview.py quotes "$B" >"$OVLOG" 2>&1
  fi
  OVRC=$?
  tail -6 "$OVLOG"
  rm -f "$OVLOG"
  if [ "$OVRC" -eq 2 ]; then
    echo "❓ 降级 lane 参照集不足 ⇒ 未核（不是通过）"
  elif [ "$OVRC" -ne 0 ]; then
    _blk ⑭     # 口径外 / 覆盖缺口 / 查无 = 阻断型（2026-10-22 起接住退出码）
  fi
elif [ "$NEED" != "0" ] && [ "$NEED" != "?" ] && [ -n "$NEED" ]; then
  echo "⚠️ 本书体裁 profile 要求 ${NEED} 篇总览，实有 0（提示型：书可能尚未写完，不判红）"
else echo "（无总览三篇，本项不适用）"; fi

echo; echo "=== ⑮ check_overview_full（章节标签对账 + H1 语义；条件性）==="
if [ "$OV" -gt 0 ]; then
  [ -n "$EPUB" ] && python3 scripts/overview.py full "$B" "$EPUB" 2>&1 | tail -1 \
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
python3 scripts/analysis.py xref "$B" 2>&1 | sed -n '1,40p'


# ⑰ 2026-10-02 新增（Beach Read 第八轮，验证器指出）：**引语块结构对账**。
#   起因：ch21 出现**引语行丢失 `> ` 前缀**（`**原句 10:**` 不带 `>`）＋**原句 9/10 倒序且撞车**
#   ＋**写作期自查记录泄漏到成品**；ch18 出现**孤儿分析**（四个子项齐全、上方无引语行）。
#   **这类损坏对六道引语门禁全部不可见**——它们只解析带 `> ` 的引语行，丢了前缀的行在它们
#   眼里根本不是引语；而「孤儿分析」是少了一行，多出来的东西没有任何检查会报。
#   五种判据：缺前缀 / 编号倒序 / 编号撞车 / 孤儿分析 / 自查泄漏。
echo; echo "=== ⑰ check_quote_blocks（引语块结构：前缀/编号/孤儿/泄漏）==="
python3 scripts/quotes.py blocks "$B" 2>&1 | head -40


# ⑱ 2026-10-02 新增（Beach Read 第九轮）：**引语块配额 + 关键词锚定 + 拼接红线**。
#   起因（本项目第 4 次同形态失误）：`check_block_keywords` **从未接进正门**，
#   于是前 17 项全绿的情况下——① 28 章**每章 12–23 块、全部超出体裁表 3–8 处配额**，
#   ② 17 处关键词越界／删词（not to→not、plural "books,"→plural "books"）全部漏网。
#   教训同前三次：**「以为跑了 gate.sh 就够」**——正门本身也有覆盖缺口，
#   接进门禁的检查器集合**必须对着 `ls scripts/` 清点过**。
#   本项同时兜住两个此前无人负责的层：块数配额（体裁表）与关键词逐字锚定。
echo; echo "=== ⑱ structure.py keywords（块覆盖度 / 关键词锚定 / 拼接红线）==="
#   ⚠️ 2026-10-05 修正（Heirs 五步审查 a 步）：本项原写 `| tail -32`，而**块数配额是
#   按章逐条打印的**——Heirs 39 章超配额共 39 条 ❌，单跑 39 条，`tail -32` 只留下 14 条，
#   **25 条阻断型被截断隐藏**（退出码仍靠剩下那 14 条判成 1，没翻车，但报告是残缺的）。
#   这与文件头「阻断型不许被任何截断隐藏」是同一条纪律（⑧ 曾因 `| tail -2` 藏掉两条 ❌）。
#   修法：**不再截断条目行**——先落临时文件，再打全部 ❌ 条目 + 末行汇总。
_KW_OUT="$(mktemp)"
python3 scripts/structure.py keywords "$B" > "$_KW_OUT" 2>&1
grep -E '^[[:space:]]+❌' "$_KW_OUT" || true
tail -1 "$_KW_OUT"
rm -f "$_KW_OUT"


# ⑲ 2026-10-19 新增：**中文层体检**——分析字段（中文理解 / 句子结构 / 为什么这样写）
#   必须是中文、不能是空话。
#   起因（2026-10-19 全库扫描）：10 本 2026-10-17~19 完工的书**全部通过前 18 lane**
#   （引语逐字 100%、vocab FAIL=0、空段扫描 0 处），但「中文理解」有 12%–100% 写成英文、
#   「为什么这样写」有 80%–100% 写成英文或中英夹杂。根因：**前 18 lane 没有一个查分析层**——
#   verify_quotes / check_chapter_quotes / sweep_full 只验引语行；check_vocab 只看词汇表；
#   ⑱ 块覆盖对账只查「每块进没进校验」，**不查块里有没有内容**。
#   ⚠️ 本项进正门后，**已有 150 本书的 gate 会变红**（其中 16 本阻断型 ≥50）——
#   那是真实状态，不是误报；按 AGENTS「🚦 新规则的适用范围」节，
#   **判据变更只对新增书籍生效**，存量书不自动回溯整改，但**新写的书必须过这一关**。
echo; echo "=== ⑲ check_chinese_layer（中文层：分析字段必须是中文、不能是空话）==="
_CCL_OUT="$(mktemp)"
python3 scripts/check_chinese_layer.py "$B" > "$_CCL_OUT" 2>&1
_CCL_RC=$?
grep -E '^[[:space:]]*❌' "$_CCL_OUT" | grep -v '：0 处' || true
grep -E '^=== 汇总|^=== 结论|^❓|^⚠️ 本书' "$_CCL_OUT" || true
rm -f "$_CCL_OUT"
if [ "$_CCL_RC" -eq 2 ]; then
  echo "⚠️ check_chinese_layer 退出码 2 = 无法判定（未解析出引语块）——**该层未核**，不是「干净」"
fi
[ "$_CCL_RC" -eq 1 ] && _blk "⑲中文层"


# ---- 退出码聚合（2026-10-02 新增，见文件头说明）----
# ⚠️ 上一版用 `exec >/dev/tty` 把汇总行打回终端，在 stdout 被重定向到文件/管道的
#   场景下 /dev/tty 不存在 ⇒ exec 失败把 stdout 置坏，汇总行根本没打出来，退出码仍 0。
#   ⇒ 不做任何 fd  gymnastics：直接读 tee 落下的日志。sleep 只是等 tee 刷缓冲。
sleep 0.3
# ⚠️ 2026-10-02 第二次修正：不能简单 `grep -c "❌"`——各工具的**汇总行本身就含 ❌ 字形**
#   却报 0（`❌ 结构缺陷 0 ｜ ⚠️ 提示 1`、`❌ 凭空造词 0 处`），第一版把 28 条真阻断
#   数成 36。判据：缩进 ❌ **条目行**（工具逐条打印的问题），排除
#   ① 含 `｜` 的汇总行  ② 含 ` 0 ` 的零计数行。
# ⚠️ 2026-10-06 第三次同型复发（The Language of Knives 批2 实测）：本判据要求
#   **行首有空白**（`^[[:space:]]+❌`），而 ⑬ 空段扫描的 ❌ 是**顶格**打印的
#   ⇒ ch07 导航只有 2 项这一条真阻断**不进聚合**，正门照样打「0 条 · 退出码 0」。
#   这是「汇总层把真阻断洗成绿灯」的**第三次**（前两次：④ corruption_scan 的 FAIL
#   无 ❌ 标记、⑱ 被 tail 截断）。⇒ 判据改为**行首可有可无空白**，只认 ❌ 本身。
echo; echo "=== ⑳ 整书体检（bookform --all，判据与 chapter.sh 相同）==="
# ⚠️ 2026-10-20 新增（用户要求「gate 调 chapter.sh」）：单章入口 chapter.sh 与整书入口
#   gate.sh 原本是两套判据——同一章，单章查得出的缺陷整书可能查不出，反之亦然。
#   ⇒ 整书复用 bookform 的同一实现（`--all`），**只报其他 lane 不查的维度**
#   （分析层残留空引号 / H1 形态 / 导航项数 / 块数越界），引语、子项、关键词、
#   中文密度仍由 ①⑤⑦⑩⑪⑫⑬⑲ 负责——否则同一处缺陷数两遍，正门计数虚高。
_bf_out=$(python3 scripts/bookform.py "$B" --all 2>&1) && _bf_rc=0 || _bf_rc=$?
echo "$_bf_out"
[ "$_bf_rc" -eq 1 ] && _blk "⑳整书体检"

_gfail=$(grep -E '^[[:space:]]*❌' "$GATE_LOG" 2>/dev/null | grep -v '｜' | grep -v ' 0 ' | wc -l | tr -d ' ')
_gfail=${_gfail:-0}
if [ "$RC_BLOCK" -gt 0 ] || [ "$_gfail" -gt 0 ]; then
  [ "$RC_BLOCK" -gt 0 ] && echo "══ 退出码层：${RC_BLOCK} 个 lane 报阻断 →${RC_WHICH} ══"
  if [ "$RC_BLOCK" -gt 0 ] && [ "$_gfail" -eq 0 ]; then
    echo "⚠️ **文本层没数到 ❌，但退出码层报阻断**——以退出码为准。"
    echo "   （这正是 2026-10-02/10-05/10-06 三次「汇总层把真阻断洗成绿灯」的形态）"
  fi
  if [ "$_gfail" -gt 0 ] && [ "$RC_BLOCK" -eq 0 ]; then
    echo "⚠️ **文本层数到 ${_gfail} 条 ❌，但退出码层全绿**——请读上面的行确认是真缺陷还是显示层问题。"
  fi
  echo "══ 正门结论：阻断型（文本层 ❌ ${_gfail} 条 ｜ 退出码层 ${RC_BLOCK} 个 lane）——退出码 1 ══"
  exit 1
fi
echo "   （rc 层覆盖 ②③⑦⑧⑲⑳ 六个 lane；其余 14 个仍由文本层 ❌ 计数兜底）"
echo "══ 正门结论：0 条阻断型（⚠️/❓ 不阻塞；退出码 0）══"
exit 0
