#!/usr/bin/env python3
"""批5 (ch14-16)：撇号弯化 + ch15 bathroom 例句修正 + 词汇例句逐条 grep 验证。"""
import re
import os

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
FILES = [
    "ch14 part 2 danny is real.md",
    "ch15 part 2 top hat.md",
    "ch16 part 2 a murder of ravens.md",
]
TEXT = {
    "ch14 part 2 danny is real.md": "text/ch14_chapter_4.txt",
    "ch15 part 2 top hat.md": "text/ch15_chapter_5.txt",
    "ch16 part 2 a murder of ravens.md": "text/ch16_chapter_6.txt",
}

FIXES = [
    ("ch15 part 2 top hat.md",
     "| bathroom | 浴室，洗手间 | be forced to make small talk in the bathroom |",
     "| bathroom | 浴室，洗手间 | run into Tanya in the bathroom |"),
]

def conv(s):
    return re.sub(r"(?<=[A-Za-z])'(?=[A-Za-z])", "\u2019", s)

for fn in FILES:
    p = os.path.join(BOOK, fn)
    s = open(p, encoding="utf-8").read()
    n0 = len(re.findall(r"[A-Za-z]'[A-Za-z]", s))
    for ffn, old, new in FIXES:
        if fn == ffn:
            if s.count(old) == 1:
                s = s.replace(old, new)
            elif s.count(new) == 1:
                pass  # 已修过，幂等
            else:
                raise SystemExit(f"FIX 目标未命中 {fn} :: {old[:40]}")
    s = conv(s)
    open(p, "w", encoding="utf-8").write(s)
    n1 = len(re.findall(r"[A-Za-z]'[A-Za-z]", s))
    print(f"{fn}: 直撇 {n0} -> {n1}")

print()
# 词汇例句逐条 flat 比对（ch14/ch15 有 text/；ch16 待写）
for fn, tfn in TEXT.items():
    p = os.path.join(BOOK, fn)
    s = open(p, encoding="utf-8").read()
    corpus = open(os.path.join(BOOK, tfn), encoding="utf-8").read()
    cf = re.sub(r"[^a-z0-9]", "", corpus.lower())
    rows = [l for l in s.split("\n") if l.startswith("| ") and "词/短语" not in l
            and not set(l) <= set("|- ")]
    bad = 0
    miss_w = 0
    for l in rows:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        entry, meaning, example = (cells + ["", "", ""])[:3]
        ex = re.sub(r"[^a-z0-9]", "", example.lower())
        if len(ex) >= 8 and ex not in cf:
            bad += 1
            print(f"  MISS {fn} [{entry}] :: {example[:70]}")
        for w in re.findall(r"[a-z]+", entry):
            if len(w) >= 4 and w not in cf:
                miss_w += 1
                print(f"  MISS-WORD {fn} [{w}]")
    print(f"{fn}: 词条 {len(rows)} 条，例句 MISS {bad} 条，词条实词 MISS {miss_w} 条")
    tiers = {}
    cur = None
    for l in s.split("\n"):
        if l.startswith("### "):
            cur = l.strip()
        elif cur and l.startswith("| ") and "词/短语" not in l and not set(l) <= set("|- "):
            tiers[cur] = tiers.get(cur, 0) + 1
    print("  分档:", {k.split()[-1] if k else k: v for k, v in tiers.items()})
