#!/usr/bin/env bash
# a-labyrinth-of-honeybees-by-fawcett-heather · T3 深审第三方复核（按序重跑）
# 用法：从 repo 根执行  bash .memory/raw-gates/a-labyrinth-of-honeybees-by-fawcett-heather/review/run.sh
set -u
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
cd "$ROOT" || exit 1
B="notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather"
R=".memory/raw-gates/a-labyrinth-of-honeybees-by-fawcett-heather/review"

echo "== 0. 语料 =="
python3 scripts/verify_corpus.py "$B" --expect 6 --edges

echo "== 1. R2 机器层：逐章 chapter.sh（rc 必须 0）=="
for f in "$B"/ch0*.md; do
  bash scripts/chapter.sh "$f" || echo "!! rc!=0: $f"
done

echo "== 2. 整书门禁 =="
bash scripts/gate.sh "$B" | tail -5

echo "== 3. 损坏扫描 =="
python3 scripts/corruption_scan.py "$B" | tail -3

echo "== 4. R1 素读锚点自证（每条 text[start:end]==anchor）=="
python3 - "$B" "$R" <<'PY'
import json, sys, pathlib
book, rev = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
bad = 0
for n in ["01","02","03","04","05","06"]:
    p = rev / f"ch{n}" / "1-suread.json"
    d = json.loads(p.read_text())
    src = book / "text" / d["source"].split("text/")[-1]
    t = src.read_text()
    for f in d["facts"]:
        got = t[f["start"]:f["end"]]
        if got != f["anchor"]:
            bad += 1; print(f"  MISS ch{n}: {f['anchor'][:50]!r}")
    print(f"  ch{n}: {len(d['facts'])} facts, source={src.name}")
print(f"锚点异常 {bad}")
PY

echo "== 5. 2-machine.json 哈希（与审查时比对）=="
for n in 01 02 03 04 05 06; do
  shasum -a 256 "$R/ch$n/2-machine.json"
done

echo "== 6. 抽验 3 行判定表（回原文核）=="
grep -n "溺死\|九个词\|He is not my God" "$R"/ch0*/3-diff.md "$R"/ch0*/4-verdict.md | head -6
