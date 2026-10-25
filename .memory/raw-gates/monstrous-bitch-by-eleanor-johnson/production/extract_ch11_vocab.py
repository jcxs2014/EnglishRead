#!/usr/bin/env python3
"""Extract exact example sentences (verbatim) containing a given term, for ch11 vocab tables."""
from __future__ import annotations

import re
import sys
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch11_9_sexy_vampire_bitches_of_the_1970s_and_.txt"
text = TXT.read_text(encoding="utf-8")

# paragraph-local sentences
paras = []
pos = 0
for chunk in re.split(r"\n\s*\n", text):
    idx = text.find(chunk, pos)
    if idx < 0:
        idx = pos
    paras.append((idx, chunk))
    pos = idx + len(chunk)

sentences = []
for off, chunk in paras:
    for s in re.findall(r"[^.!?]*[.!?]+(?:[”’\"']?)(?:\s+|$)|[^.!?]+$", chunk):
        s = re.sub(r"\s+", " ", s).strip()
        if s:
            sentences.append((off + chunk.find(s), s))

TERMS = sys.argv[1:]
for t in TERMS:
    pat = re.compile(re.escape(t), re.IGNORECASE)
    print("=" * 8, t)
    n = 0
    for off, s in sentences:
        if pat.search(s) and len(s.split()) >= 8:
            print(f"  [{off}] {s}")
            n += 1
            if n >= 4:
                break
