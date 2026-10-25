#!/usr/bin/env python3
"""Print the 15 selected quote spans verbatim from ch11-candidates2.json."""
from __future__ import annotations

import json
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
CAND = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch11-candidates2.json"
cands = json.loads(CAND.read_text(encoding="utf-8"))

OPENINGS = [
    "Now part of what makes the vampiress so horrifying",
    "Put otherwise, we’re seeing the Monstrous Bitch tradition",
    "Early on, we meet the beautiful Marcilla Karnstein",
    "One night, Laura has a horrible nightmare",
    "In this reboot of Carmilla, we’re starting from an altered script",
    "The local doctor in Emma’s town says",
    "Just when we think that Carmilla will successfully convert Emma",
    "In each subsequent iteration, the films become more misogynist",
    "Embodying and voicing this understanding, a townsman, Anton",
    "From a feminist standpoint, this taming process is disappointing",
    "Bitch, notice: The dog-faced Monstrous Bitch creeps into this story",
    "Fran and Miriam do not undergo the ultimate punishment",
    "Western culture tends to view a woman’s aging process",
    "In the final scene, we are at a new location",
    "The Monstrous Bitch paradigm, then, isn’t only about",
]

for op in OPENINGS:
    hits = [c for c in cands if c["text"].startswith(op)]
    if not hits:
        print(f"!! NOT FOUND: {op}")
        continue
    # prefer the 2-3 sentence version with most words
    hits.sort(key=lambda c: -c["nwords"])
    best = hits[0]
    print(f"### pos={best['pos']} nwords={best['nwords']} para={best['para']} count={best['count']} nhits={len(hits)}")
    print(best["text"])
    print()
