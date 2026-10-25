#!/usr/bin/env bash
# monstrous-bitch-by-eleanor-johnson · T3 机器层一键复跑
# 用法：bash .memory/raw-gates/monstrous-bitch-by-eleanor-johnson/review/run.sh
set -u
cd "$(git rev-parse --show-toplevel)" || exit 1
B="notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson"
R=".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/review"
T="/tmp/t3mb"; mkdir -p "$T"
mkdir -p "$R"

echo "== 1) 整书门禁 =="
bash scripts/gate.sh "$B" > "$T/gate.txt" 2>&1; echo "gate rc=$?"

echo "== 2) 总览门禁 =="
E=$(ls "$B"/library/*.epub 2>/dev/null | head -1)
python3 scripts/overview.py quotes "$B" "$E" > "$T/ov-quotes.txt" 2>&1; echo "quotes rc=$?"
python3 scripts/overview.py full   "$B" "$E" > "$T/ov-full.txt"   2>&1; echo "full rc=$?"
python3 scripts/overview.py labels "$B" "$E" > "$T/ov-labels.txt" 2>&1; echo "labels rc=$?"

echo "== 3) 引语逐字（全量 + 整串） =="
python3 scripts/quotes.py verbatim "$B" "$E" --full > "$T/quotes-verbatim.txt" 2>&1; echo "verbatim rc=$?"

echo "== 4) 结构顺序 =="
python3 scripts/structure.py order "$B" > "$T/structure-order.txt" 2>&1; echo "order rc=$?"

echo "== 5) 语料 =="
python3 scripts/verify_corpus.py "$B" --expect 13 \
  --expect-source "epub 目录页：Preface + Introduction + ch.1–11（13 件）" --quiet-edges \
  > "$T/corpus.txt" 2>&1; echo "corpus rc=$?"

echo "== 6) 每章机器层 JSON（R2 复跑） =="
for f in "$B"/ch*.md; do
  nn=$(basename "$f" | sed -n 's/^ch\([0-9][0-9]\) .*/\1/p')
  [ -n "$nn" ] || continue
  mkdir -p "$R/ch$nn"
  bash scripts/chapter.sh "$f" --json > "$R/ch$nn/2-machine.json" 2>"$R/ch$nn/2-machine.err"
  echo "ch$nn rc=$?"
done

echo "== 7) 省略号块普查（应 0） =="
/usr/bin/grep -c '^> \*\*原句.*…' "$B"/*.md 2>/dev/null | awk -F: '{s+=$2} END{print "ellipsis_blocks:", s+0}'

echo "== 全部输出在 $T/ =="
