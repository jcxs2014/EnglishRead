#!/usr/bin/env python3
"""批6 (ch17-ch19) 撇号弯化 + 例句 flat 比对 + 分档统计 + 词条实词比对。"""
import re
import sys

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
FILES = [
    "ch17 part 2 the unkindness descends.md",
    "ch18 part 2 mouth full of raven beaks.md",
    "ch19 part 2 my time is up.md",
]
TEXT = {
    "ch17 part 2 the unkindness descends.md": "text/ch17_chapter_7.txt",
    "ch18 part 2 mouth full of raven beaks.md": "text/ch18_chapter_8.txt",
    "ch19 part 2 my time is up.md": "text/ch19_chapter_9.txt",
}


def conv(s):
    return re.sub(r"(?<=[A-Za-z])'(?=[A-Za-z])", "\u2019", s)


def flat(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


for fn in FILES:
    path = f"{BOOK}/{fn}"
    with open(path, encoding="utf-8") as f:
        s = f.read()
    straight = len(re.findall(r"[A-Za-z]'[A-Za-z]", s))
    s2 = conv(s)
    straight_after = len(re.findall(r"[A-Za-z]'[A-Za-z]", s2))
    if s != s2:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s2)
        print(f"撇号转换 {fn}: 直撇 {straight} -> {straight_after}")

    # 例句 flat 比对
    with open(f"{BOOK}/{TEXT[fn]}", encoding="utf-8") as f:
        cf = flat(f.read())
    lines = s2.split("\n")
    miss_ex = []
    rows = []
    cur = ""
    for l in lines:
        if l.startswith("### "):
            cur = l.strip()
            continue
        if l.startswith("| ") and "词/短语" not in l and not set(l) <= set("|- "):
            cols = [c.strip() for c in l.split("|")]
            if len(cols) >= 5:
                rows.append((cur, cols[1], cols[3]))
    for cur, term, example in rows:
        ex = flat(example)
        if len(ex) >= 8 and ex not in cf:
            miss_ex.append((cur, term, example))
    # 词条实词比对
    miss_term = []
    for cur, term, example in rows:
        for w in re.findall(r"[A-Za-z']+", term):
            if len(w) < 4:
                continue
            if flat(w) not in cf:
                miss_term.append((cur, term, w))
    # 分档统计
    counts = {}
    for cur, term, example in rows:
        counts[cur] = counts.get(cur, 0) + 1
    print(f"--- {fn} ---")
    print(f"  直撇(转换后)={straight_after}  例句MISS={len(miss_ex)}  词条MISS={len(miss_term)}")
    for cur, term, example in miss_ex:
        print(f"  EX MISS: {cur[:6]} | {term} | {example[:60]}")
    for cur, term, w in miss_term:
        print(f"  TERM MISS: {cur[:6]} | {term} | {w}")
    print(f"  分档: " + "  ".join(f"{k}={v}" for k, v in counts.items()))
