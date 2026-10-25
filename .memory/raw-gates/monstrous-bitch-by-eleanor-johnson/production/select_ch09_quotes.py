#!/usr/bin/env python3
"""Select the final 15 quotes for ch09 from candidates, validate hard constraints, emit ch09-quotes.json."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch09_7_crazy_bitches_of_the_1940s_and_1950s.txt"
CAND = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch09-candidates.json"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch09-quotes.json"

text = TXT.read_text(encoding="utf-8")
cands = json.loads(CAND.read_text(encoding="utf-8"))


def flat(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


flattext = flat(text)

# target positions: one candidate per chapter beat, strictly increasing
TARGETS = [2612, 5132, 5292, 7932, 8335, 9377, 10835, 12491, 16312, 21625, 30950, 41537, 43756, 55241, 56477]

by_pos = {}
for c in cands:
    by_pos.setdefault(c["pos"], []).append(c)

chosen = []
last = -1
for t in TARGETS:
    opts = by_pos[t]
    # prefer the longest option (most content) that is still <=70 words
    opts = sorted(opts, key=lambda c: -c["nwords"])
    pick = None
    for o in opts:
        if o["pos"] > last:
            pick = o
            break
    assert pick is not None, t
    last = pick["pos"]
    chosen.append(pick)

# validate
prev = -1
for i, c in enumerate(chosen, 1):
    span = c["text"]
    n = len(span.split())
    fs = flat(span)
    cnt = flattext.count(fs)
    assert 30 <= n <= 70, (i, n)
    assert "…" not in span and "..." not in span, (i, "ellipsis")
    assert cnt == 1, (i, cnt, span[:60])
    assert c["pos"] > prev, (i, "order")
    prev = c["pos"]
    # same-paragraph check: paragraph boundaries are blank lines; ensure no double newline inside
    assert "\n\n" not in span, (i, "cross-paragraph")
    # no footnote digits
    assert not re.search(r"\d", span), (i, "digit in span")
    print(f"--- block {i}: pos={c['pos']} words={n}")
    print(span)
    print()

OUT.write_text(json.dumps([c["text"] for c in chosen], ensure_ascii=False, indent=1), encoding="utf-8")
print("ALL CONSTRAINTS OK ->", OUT)
