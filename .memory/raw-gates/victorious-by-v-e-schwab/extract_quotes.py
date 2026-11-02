#!/usr/bin/env python3
"""从已过门禁的章节块程序化抽取引语（供总览三篇选材用）。

输出 JSON 行：{"ch": "ch05", "n": 1, "file": "...", "quote": "...", "words": N}
用法：python3 extract_quotes.py <书目录> > quotes.jsonl
"""
import json
import re
import sys
from pathlib import Path

BOOK = Path(sys.argv[1])
pat = re.compile(r'^> \*\*原句 (\d+):\*\* "(.+)"\s*$')

rows = []
for md in sorted(BOOK.glob("ch[0-9]* *.md")):
    ch = md.name.split(" ")[0]
    for line in md.read_text(encoding="utf-8").splitlines():
        m = pat.match(line)
        if not m:
            continue
        q = m.group(2)
        rows.append({
            "ch": ch,
            "n": int(m.group(1)),
            "file": md.name,
            "quote": q,
            "words": len(q.split()),
        })

for r in rows:
    print(json.dumps(r, ensure_ascii=False))
print(f"# total {len(rows)} quotes from {len({r['ch'] for r in rows})} chapters", file=sys.stderr)
