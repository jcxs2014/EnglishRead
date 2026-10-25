#!/bin/bash
# T3 深审 · motherclown-by-harriet-alida-lye · 2026-10-25
# 全部命令按序执行；R1 由独立子代理产出 1-suread.json（只读 text/）
set -u
cd /Users/jcxs2014/Documents/Works/EnglishRead
B="notes/books/novels/motherclown-by-harriet-alida-lye"
R=".memory/raw-gates/motherclown-by-harriet-alida-lye/review"

# R2 机器层（第二实现，不读 md 结构）：每章一份 2-machine.json
for f in "$B"/ch*.md; do
  n=$(basename "$f" | cut -c1-4)
  mkdir -p "$R/$n"
  bash scripts/chapter.sh "$f" --json > "$R/$n/2-machine.json" 2>/dev/null
  echo "$n rc=$?"
done

# 整书门禁与块序（审查基线）
bash scripts/gate.sh "$B" > /tmp/t3-gate.log 2>&1; echo "GATE_RC=$?"
python3 scripts/structure.py order "$B" | tail -1
python3 scripts/corruption_scan.py "$B" | grep -E "FAIL|报告"

# 第三方复核：2-machine.json 哈希
shasum -a 256 "$R"/ch*/2-machine.json > "$R/2-machine.sha256"
