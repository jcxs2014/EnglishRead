#!/usr/bin/env python3
"""ch18 STAR tier: 3 examples rewritten as verbatim source (idempotent)."""
import re

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
FN = "ch18 part 2 mouth full of raven beaks.md"
TEXT = "text/ch18_chapter_8.txt"

OLD_NEW = [
    ("| door | ", "Ravi holds the door open for us. |"),
    ("| water | ", "A bottle of water out of the mini fridge that I somehow failed to notice. |"),
    ("| arm | ", "propping himself on his functioning arm |"),
]


def flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


path = f"{BOOK}/{FN}"
with open(path, encoding="utf-8") as f:
    s = f.read()
with open(f"{BOOK}/{TEXT}", encoding="utf-8") as f:
    cf = flat(f.read())

lines = s.split("\n")
changed = 0
for i, l in enumerate(lines):
    for prefix, new_tail in OLD_NEW:
        if l.startswith(prefix) and not l.endswith(new_tail):
            # rebuild: | term | 释义 | new example |
            cols = l.split("|")
            lines[i] = "| " + cols[1] + " | " + cols[2] + " | " + new_tail
            changed += 1
            break

if changed:
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"FIX 应用 {changed} 行")
else:
    print("FIX 已应用（幂等跳过）")

# 复核
miss = []
for l in lines:
    if l.startswith("| ") and "词/短语" not in l and not set(l) <= set("|- "):
        cols = [c.strip() for c in l.split("|")]
        if len(cols) >= 5 and cols[3].strip():
            ex = flat(cols[3])
            if len(ex) >= 8 and ex not in cf:
                miss.append((cols[1], cols[3]))
print(f"ch18 example MISS={len(miss)}")
for t, e in miss:
    print(f"  MISS: {t} | {e}")
