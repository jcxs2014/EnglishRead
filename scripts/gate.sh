#!/usr/bin/env bash
# 本批次全量门禁汇总（第 3 条提交门禁 + 逐章归属 + 写作侧兜底四件）。
# ⚠️ 原文件误用 python shebang + docstring，被 bash 当命令执行 ⇒ `line 4: 书目录: No such file`
#    （假红型：不影响任何门禁读数，但每次跑都刷一条错）。2026-09-29 已改为 bash 注释。
# 用法: bash scripts/gate.sh "<书目录>"
set -u
B="$1"
EPUB=$(ls "$B"/library/*.epub 2>/dev/null | head -1)
cd "$(git rev-parse --show-toplevel)"

echo "=== lane ==="
[ -n "$EPUB" ] && echo "完整 lane（有 epub）" || echo "降级 lane（无 epub）"

echo; echo "=== ① verify_quotes（引语逐字，对 epub）==="
if [ -n "$EPUB" ]; then python3 scripts/verify_quotes.py "$B" "$EPUB" 2>&1 | tail -3
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
python3 scripts/check_nav_layer.py "$B" --per-chapter 2>&1 | tail -1

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
    # 本章词汇：三档表头下每档至少一条词条
    v = re.search(r"^## 本章词汇(.*?)(?=\n## |\Z)", txt, re.M | re.S)
    if v:
        tiers = re.split(r"(?m)^### ", v.group(1))[1:]
        for ti in tiers:
            rows = [x for x in ti.split("\n") if x.startswith("| ") and "词/短语" not in x and not x.startswith("|---")]
            if not rows:
                print(f"❌ {n}: 词表档位「{ti.splitlines()[0].strip()}」只有表头没有词条")
                bad += 1
    # 导航必备 5 项：**只判「项数 ≥5 且每项有正文」，不锁死标签措辞**——
    # 言情档写「Tropes 兑现/反转」、双时间线档写「本节在双线中的位置」、
    # 非言情精简档写「母题/冲突兑现/反转」；枚举标签会把每种正当写法都判成假红
    # （AGENTS 8.3：格式自成一派的书是合法的；假红型先修工具）。
    nav = re.search(r"^## 本章导航[ \t]*\n(.*?)(?=\n## |\Z)", txt, re.M | re.S)
    # ⚠️ 冒号后**允许前导空格**（2026-09-30 Broken Light 终验实测）：
    #    原式 `：(\S.*)$` 要求首字符非空白，于是写成「**： 内容」（带一个空格）的
    #    5 个导航项全被判 0 条 —— ch21–ch25 五章假红，内容本身完好。
    #    前导空格是正常排版，不是缺陷；判据只该管「有没有正文」。
    items = re.findall(r"(?m)^[-*]?\s*\*\*([^*]+)\*\*：\s*(\S.*)$", nav.group(1)) if nav else []
    if len(items) < 5:
        print(f"❌ {n}: 导航粗体项 {len(items)} 条 < 5（缺项或写法不匹配 `**X**：`）")
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
