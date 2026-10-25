#!/usr/bin/env python3
"""Verify the 15 chosen quotes against the SAME flat() used by scripts/chapter_contiguity.py
(the ruler used by scripts/structurecheck/order.py). Must be: unique match, strictly increasing."""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch09_7_crazy_bitches_of_the_1940s_and_1950s.txt"
QUOTES = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch09-quotes.json"


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())


T = flat(TXT.read_text(encoding="utf-8"))
qs = json.loads(QUOTES.read_text(encoding="utf-8"))
prev = -1
ok = True
for i, q in enumerate(qs, 1):
    f = flat(q).strip().rstrip(".,;")
    p = T.find(f)
    cnt = T.count(f)
    words = len(q.split())
    flags = []
    if p < 0:
        flags.append("NOT FOUND")
    if cnt != 1:
        flags.append(f"count={cnt}")
    if p <= prev:
        flags.append("ORDER")
    if not (30 <= words <= 70):
        flags.append(f"words={words}")
    if "…" in q or "..." in q:
        flags.append("ELLIPSIS")
    if re.search(r"[A-Za-z)\"”]\d+", q):
        flags.append("FOOTNOTE-DIGIT")
    if flags:
        ok = False
    print(f"{i:2d} pos={p:6d} w={words:2d} {'OK' if not flags else '!! ' + ','.join(flags)}  {' '.join(q.split()[:6])}")
    prev = p if p >= 0 else prev
print("ALL OK" if ok else "PROBLEMS FOUND")
sys.exit(0 if ok else 1)
