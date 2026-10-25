#!/usr/bin/env python3
"""Dump canonical quote lines + vocab example sentences verbatim from ch13 text."""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch13_11_back_to_babylon.txt"
text = TXT.read_text(encoding="utf-8")

# ---------- quotes from the validated JSON ----------
quotes = json.loads((BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch13-quotes.json").read_text(encoding="utf-8"))
print("=== QUOTE LINES ===")
for q in quotes:
    assert q["text"] in text, q["no"]
    print(f'> **原句 {q["no"]}:** "{q["text"]}"')
print()

# ---------- vocab: headword -> anchor (verbatim substring used to locate the sentence) ----------
PAIRS = [
    ("backformation", "is a backformation of Patriarchy"),
    ("emergent property", "is best understood as an emergent property of Patriarchy itself"),
    ("Lamashtean", "turns back to its most Lamashtean and Lamian roots"),
    ("decrepitude", "Through the increasing decrepitude of Elisabeth"),
    ("chimeric", "a disgusting chimeric body"),
    ("subordination", "participant in her own subordination to Paimon"),
    ("talisman", "clay tablets or talismans"),
    ("hyperinvolved", "was apparently hyperinvolved in Annie"),
    ("ambivalent", "are almost always ambivalent"),
    ("backslide", "the feminist backslide we"),
    # 进阶
    ("occult", "and the occult, by dint of their femaleness"),
    ("monstrosity", "the same monstrosity we"),
    ("succubus", "the succubus-like Sue slaughters"),
    ("theological", "in theological importance"),
    ("invectives", "slingers of invectives, curses, and spells"),
    ("spellcasters", "dehumanizing spellcasters"),
    ("coven", "a coven (of both men and women)"),
    ("neural pathways", "work new neural pathways into our cultural brain"),
    ("self-mutilation", "a ritual dagger of suicide and self-mutilation"),
    ("dirge", "as a dirge, an elegy"),
    # 基础
    ("womb", "kill him in the womb"),
    ("goddess", "worshiper of the goddess Inanna"),
    ("prayer", "prayer for restitution and justice"),
    ("ancient", "an ancient, demonic Patriarch named Paimon"),
    ("monster", "This monster, whom the film names Elisasue"),
    ("film", "Coralie Fargeat"),
    ("history", "the real history of Monstrous Bitchery works"),
    ("mother", "Like mother, like daughter"),
    ("violence", "a larger system of violence, mental illness, trauma"),
    ("priestess", "a sacred priestess, socially respected"),
]


def expand(anchor: str) -> str:
    """Return the full sentence (verbatim) containing anchor, using sentence offsets."""
    i = text.find(anchor)
    if i < 0:
        raise SystemExit(f"anchor not found: {anchor!r}")
    best = None
    for m in SENT.finditer(text):
        s, e = m.span()
        if s <= i < e:
            cand = text[s:e]
            # prefer the longest sentence covering the anchor
            if best is None or len(cand) > len(best):
                best = cand
    if best is None:
        raise SystemExit(f"sentence not found: {anchor!r}")
    return re.sub(r"\s+", " ", best).strip()


print("=== VOCAB ROWS ===")
rows = []
for head, anchor in PAIRS:
    ex = expand(anchor)
    assert ex in text, head
    assert head.lower() in ex.lower(), (head, ex)
    rows.append((head, ex))
    print(f"{head}\t{ex}")
print()
print("count:", len(rows))