#!/usr/bin/env python3
"""Pick verbatim example sentences from ch09 text for vocab rows.
Each headword -> find a sentence in the text containing it verbatim; print markdown row.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch09_7_crazy_bitches_of_the_1940s_and_1950s.txt"
text = TXT.read_text(encoding="utf-8")

# sentence split (with abbreviation guard), paragraph-aware
ABBREV = ("Dr.", "Mr.", "Mrs.", "Ms.", "No.", "St.", "Jr.", "Sr.", "etc.", "vs.", "U.S.")
SENT_END = re.compile(r'(?<=[.!?…])["”\')\]]*\s+(?=[A-Z“"\'(])')

sents = []
for para in re.split(r"\n\s*\n", text):
    last = 0
    for m in SENT_END.finditer(para):
        head = para[last:m.end()]
        if any(head.rstrip().endswith(a) for a in ABBREV):
            continue
        s = para[last:m.end()].strip()
        if s:
            sents.append(s)
        last = m.end()
    tail = para[last:].strip()
    if tail:
        sents.append(tail)

seen = set()
uniq = []
for s in sents:
    k = re.sub(r"\s+", " ", s)
    if k not in seen:
        seen.add(k)
        uniq.append(k)

WORDS = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
for w in WORDS:
    hits = [s for s in uniq if w in s]
    # prefer the shortest sentence containing the word
    hits.sort(key=lambda s: len(s.split()))
    if not hits:
        print(f"!! NOT FOUND: {w}")
        continue
    best = hits[0]
    # verify verbatim in text
    assert best in text, (w, best[:60])
    print(f"HEAD: {w}\nEX: {best}\n")
