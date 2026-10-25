#!/usr/bin/env python3
"""Pick verbatim example sentences for the ch13 vocabulary table."""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch13_11_back_to_babylon.txt"
text = TXT.read_text(encoding="utf-8")

SENT = re.compile(r"[^.!?]*[.!?]+[”’\"')\]]*(?:\s+|$)|[^.!?]+$")
sents = []
for chunk in re.split(r"\n\s*\n", text):
    for s in SENT.findall(chunk):
        s = re.sub(r"\s+", " ", s).strip()
        if s:
            sents.append(s)

HEADS = [
    "backformation", "emergent property", "gnarliest", "Lamashtean", "disastrous ministrations",
    "decrepitude", "chimeric", "ambivalent", "hyperinvolved", "backslide", "atrophy",
    "subordination", "Mesopotamia", "priestess", "succubus", "neuro", "theological",
    "hereditary", "hormone", "depredation", "surveillance", "epidemic", "invective",
    "corporeal", "decrepit", "spore", "throes", "menace", "harrowing", "savage",
    "extremity", "obsession", "predatory", "poison", "defilement", "ravage", "slaughter",
    "decapitate", "suffocate", "reverence", "conflagration", "paradox", "duality",
    "ecstatic", "mutilation", "maimed", "flesh", "gynecological", "uterus", "womb",
]

for h in HEADS:
    hits = [s for s in sents if h.lower() in s.lower()]
    if not hits:
        print(f"--- {h}: NOT FOUND")
        continue
    s = hits[0]
    print(f"--- {h}  ({len(hits)} hits)")
    print(s)
    print()
