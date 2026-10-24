#!/usr/bin/env bash
# T3 深审复现脚本 — Life Out of Order (Audrey Niffenegger)
# 用途：按序复跑本次深审的全部机器层命令，结果写入 /tmp/t3-repro/
# 说明：R1 素读（review/chNN/1-suread.json）与 R4 逐块三问（3-diff.md / 4-verdict.md）
#       属人判，无法脚本化；本脚本只覆盖可机读部分。
set -u
BOOK="notes/books/novels/life-out-of-order-by-audrey-niffenegger"
OUT="/tmp/t3-repro"
mkdir -p "$OUT"

ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"; cd "$ROOT" || exit 1

echo "== 0. 语料与计数"
python3 scripts/verify_corpus.py "$BOOK" > "$OUT/00-corpus.txt" 2>&1
printf "ch*.md=%s  blocks=%s  00_*.md=%s\n" \
  "$(ls "$BOOK"/ch*.md | wc -l | tr -d ' ')" \
  "$(grep -c '^> \*\*原句' "$BOOK"/ch*.md | awk -F: '{s+=$2} END{print s}')" \
  "$(ls "$BOOK"/00_*.md | wc -l | tr -d ' ')"

echo "== 1. 每章 chapter.sh --json（72 章）"
: > "$OUT/01-chapters.txt"
for f in "$BOOK"/ch*.md; do
  n=$(basename "$f" | sed -E 's/^ch([0-9]+) .*/\1/')
  bash scripts/chapter.sh "$f" --json > "$OUT/ch$n.json" 2> "$OUT/ch$n.err"
  echo "ch$n rc=$? bytes=$(wc -c < "$OUT/ch$n.json" | tr -d ' ')" >> "$OUT/01-chapters.txt"
done
echo "-- rc!=0 的章："; grep -v "rc=0" "$OUT/01-chapters.txt" || echo "（无）"

echo "== 2. 全书门禁 gate.sh"
bash scripts/gate.sh "$BOOK" > "$OUT/02-gate.txt" 2>&1
echo "gate exit=$? → 末 3 行："; tail -3 "$OUT/02-gate.txt"

echo "== 3. 总览三篇"
python3 scripts/overview.py quotes "$BOOK" > "$OUT/03-overview-quotes.txt" 2>&1
python3 scripts/overview.py full   "$BOOK" > "$OUT/03-overview-full.txt" 2>&1
tail -2 "$OUT/03-overview-quotes.txt"; tail -3 "$OUT/03-overview-full.txt"

echo "== 4. 损坏扫描"
python3 scripts/corruption_scan.py "$BOOK" > "$OUT/04-corruption.txt" 2>&1
tail -2 "$OUT/04-corruption.txt"

echo
echo "全部输出在 $OUT/。交叉验证建议："
echo "  1) 比对 2-machine.json 哈希：shasum \"$OUT\"/ch*.json 与 review/chNN/2-machine.json"
echo "  2) 从任一 review/chNN/4-verdict.md 抽 3 行，按 text/文件:行 回原文逐字核"
