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
python3 scripts/check_block_coverage.py "$B" 2>&1 | grep -E "✅|❌|⚠️" | tail -2

echo; echo "=== ⑨ 导航/总结层英文核对（六道门禁盲区）==="
python3 scripts/check_nav_layer.py "$B" --per-chapter 2>&1 | tail -1

echo; echo "=== ⑩ sweep_analysis_inline（分析层行内英文）==="
python3 scripts/sweep_analysis_inline.py "$B" 2>&1 | grep "逐字"

echo; echo "=== ⑪ audit_structure（结构；子项检查是假阴性高发点，0 不等于齐）==="
python3 scripts/audit_structure.py "$B" --quiet 2>&1 | tail -2

echo; echo "=== ⑫ check_anchor（关键词锚定）==="
python3 scripts/check_anchor.py "$B" 2>&1 | grep -E "凭空造词|松散关键词"
