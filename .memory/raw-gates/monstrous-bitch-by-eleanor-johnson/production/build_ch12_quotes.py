#!/usr/bin/env python3
"""Build ch12 quotes + vocab examples BY SLICING THE SOURCE (no hand transcription).

Sentence splitter is footnote-aware: a period followed by digits (e.g. "William.10")
is a sentence boundary; the digit run is dropped from the following chunk.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch12_10_monstrous_bitches_bite_back.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch12-quotes.json"
VOUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch12-vocab.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())


flattext = flat(text)
paras = re.split(r"\n\s*\n", text)


def split_sentences(p: str) -> list[str]:
    """Footnote-aware sentence split.  Returns sentences WITHOUT the footnote digits."""
    out, start, i, n = [], 0, 0, len(p)
    while i < n:
        c = p[i]
        if c in ".!?":
            j = i + 1
            while j < n and p[j] in "\u201d\u2019\"')]":
                j += 1
            if j < n and p[j].isdigit():
                # footnote marker: sentence ends here; digits are dropped
                out.append(p[start:i].strip())
                i = j
                while i < n and p[i].isdigit():
                    i += 1
                start = i
                continue
            if j >= n or p[j].isspace():
                out.append(p[start:j].strip())
                i = j
                start = i
                continue
        i += 1
    tail = p[start:].strip()
    if tail:
        out.append(tail)
    return [s for s in out if s]


# (para_index, start-sentence prefix, number of contiguous sentences)
SPECS = [
    (3,  "They are playing at vampirism", 3),
    (4,  "On the way home from their jaunt", 3),
    (10, "As in Werewolf Woman, so here", 3),
    (12, "They do this because they want their rock band", 2),
    (16, "Now this is interesting", 3),
    (16, "Jennifer and Needy are thus the Laura and Carmilla", 2),
    (21, "This is a film in which", 2),
    (23, "On the one hand, Monstrous Bitches in Raw", 3),
    (24, "But she’s also saying", 2),
    (30, "With no thought to the physical safety", 2),
    (33, "But this magnificent film is going to go out of its way", 1),
    (49, "Thomasin, in this film, goes from being a victim", 2),
    (51, "Guadagnino realizes", 2),
    (63, "It’s more one of waking up", 3),
    (64, "To varying degrees", 2),
]

errors: list[str] = []
records = []
last_pos = -1

for n, (pi, prefix, nsent) in enumerate(SPECS, 1):
    sents = split_sentences(paras[pi].strip())
    idx = next((i for i, s in enumerate(sents) if s.startswith(prefix)), None)
    if idx is None:
        errors.append(f"Q{n}: start sentence not found in para {pi}: {prefix!r}")
        continue
    span = " ".join(sents[idx:idx + nsent]).strip()
    # the span must be a verbatim run of the paragraph (footnote digits may sit at the seam)
    if span not in paras[pi].strip():
        errors.append(f"Q{n}: reconstruction NOT verbatim in para {pi}")
    words = len(span.split())
    if not (30 <= words <= 70):
        errors.append(f"Q{n}: word count {words} out of 30-70")
    if "…" in span or "..." in span:
        errors.append(f"Q{n}: ellipsis present")
    if re.search(r"[.!?]\d", span):
        errors.append(f"Q{n}: footnote marker inside span")
    if '"' in span:
        errors.append(f"Q{n}: ASCII double quote inside span")
    cnt = flattext.count(flat(span))
    if cnt != 1:
        errors.append(f"Q{n}: flat hit count {cnt} (need 1)")
    pos = text.find(span)
    if pos <= last_pos:
        errors.append(f"Q{n}: position {pos} not after {last_pos}")
    last_pos = pos
    records.append({"n": n, "pos": pos, "nwords": words, "count": cnt, "text": span})

if errors:
    for e in errors:
        print("ERROR:", e)
    raise SystemExit(1)

OUT.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
print("=== 15 QUOTES (md-ready lines) ===")
for r in records:
    print(f"> **原句 {r['n']}:** \"{r['text']}\"")
    print(f"      [pos={r['pos']} words={r['nwords']} hit={r['count']}] first6: {' '.join(r['text'].split()[:6])}")
print("OK: 15 quotes built from source, positions strictly increasing")

# ---------------- vocab ----------------
ALL_SENTS: list[str] = []
for pi, para in enumerate(paras):
    for s in split_sentences(para.strip()):
        if len(s.split()) >= 5:
            ALL_SENTS.append(s.strip())


def pick(head: str) -> str | None:
    pat = re.compile(r"\b" + re.escape(head).replace(r"\ ", r"\s+") + r"(s|es|ed|ing)?\b", re.I)
    hits = [s for s in ALL_SENTS if pat.search(s)]
    if not hits:
        return None
    hits.sort(key=lambda s: (len(s.split()), len(s)))
    best = hits[0]
    if flat(best) not in flattext:
        return None
    return best


TIERS = {
    "高级": ["mormolyke", "lycanthropy", "succubus", "matrilinear",
             "autosomal-dominant", "Erichtho", "Bacchanalian", "indomitability"],
    "进阶": ["patriarchal", "monstrosity", "transmissible", "sapphic",
             "forcible", "allegory", "dehumanizing", "seductive"],
    "基础": ["vampire", "cannibal", "monster", "sisters", "girl", "bite",
             "witch", "blood"],
}
vocab: dict[str, list] = {}
for tier, heads in TIERS.items():
    rows = []
    for h in heads:
        ex = pick(h)
        if ex is None:
            errors.append(f"VOCAB {tier}/{h}: no verbatim sentence found")
            continue
        rows.append({"head": h, "example": ex})
    vocab[tier] = rows

if errors:
    for e in errors:
        print("ERROR:", e)
    raise SystemExit(1)

VOUT.write_text(json.dumps(vocab, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n=== VOCAB ROWS ===")
for tier, rows in vocab.items():
    print(f"\n### {tier}")
    for r in rows:
        print(f"| {r['head']} | … | \"{r['example']}\" |")
print("\nchars without whitespace:", len(re.sub(r"\s", "", text)))
