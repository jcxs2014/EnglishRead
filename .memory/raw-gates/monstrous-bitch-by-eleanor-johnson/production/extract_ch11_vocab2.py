#!/usr/bin/env python3
"""Final vocab example sentences for ch11 — flag footnote markers, dedupe."""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch11_9_sexy_vampire_bitches_of_the_1970s_and_.txt"
text = TXT.read_text(encoding="utf-8")

paras = []
pos = 0
for chunk in re.split(r"\n\s*\n", text):
    idx = text.find(chunk, pos)
    if idx < 0:
        idx = pos
    paras.append((idx, chunk))
    pos = idx + len(chunk)

sents = []
for off, chunk in paras:
    for s in re.findall(r"[^.!?]*[.!?]+(?:[”’\"']?)(?:\s+|$)|[^.!?]+$", chunk):
        s = re.sub(r"\s+", " ", s).strip()
        if s:
            sents.append((off + chunk.find(s), s))

TERMS = ["bloodthirstiness", "rapacious", "phallicized", "sempiternal", "erotic epicenter",
         "heteronormativity", "sapphism", "Satanist", "subversion", "witchcraft", "wanes",
         "tamed", "Botox", "crucifixes", "governess", "Bacchae", "epicentral", "subdued",
         "occult", "slash", "scream", "sunlight", "hysteria", "preying on", "sapphic",
         "undead", "vampiress", "suck out", "coffin", "sarcophagus", "thirst", "thirsty",
         "seduce", "seduced", "conspiracy", "sacrifice", "torture", "decay", "monstrosity",
         "hatred", "gun", "bodies", "survive", "slaughter", "preach", "Bible", "Christian",
         "mass hysteria", "movie", "film", "audience", "viewer", "villain", "monster"]

used = set()
for t in TERMS:
    pat = re.compile(re.escape(t), re.IGNORECASE)
    print("=" * 10, t)
    n = 0
    for off, s in sents:
        if not pat.search(s):
            continue
        if len(s.split()) < 8:
            continue
        if re.search(r"[a-zA-Z]\.\d", s):        # footnote marker inside
            continue
        if re.match(r"^\d", s):                   # leading footnote number
            continue
        if "Dr. " in s or "Mr. " in s or "St. " in s:
            continue
        if s in used:
            continue
        used.add(s)
        print(f"  [{off}] {s}")
        n += 1
        if n >= 3:
            break
