#!/usr/bin/env python3
"""批5 结构复核：块数/四子项/导航/直撇/自标注释/空单元格。"""
import re
import os

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
FILES = [
    "ch14 part 2 danny is real.md",
    "ch15 part 2 top hat.md",
    "ch16 part 2 a murder of ravens.md",
]

for fn in FILES:
    p = os.path.join(BOOK, fn)
    s = open(p, encoding="utf-8").read()
    lines = s.split("\n")
    blocks = sum(1 for l in lines if l.startswith("> **原句"))
    subs = {k: sum(1 for l in lines if l.startswith(f"**{k}：**")) for k in
            ("中文理解", "关键词", "为什么这样写", "读者视角提示")}
    nav = sum(1 for l in lines if re.match(r"^- \*\*", l))
    straight = len(re.findall(r"[A-Za-z]'[A-Za-z]", s))
    ann = s.count("未出现在原文")
    rows = [l for l in lines if l.startswith("| ") and "词/短语" not in l
            and not set(l) <= set("|- ")]
    empty = [l[:40] for l in rows if len(l.split("|")) < 5 or not l.split("|")[3].strip()]
    fm = s.startswith("---\n")
    h1 = [l for l in lines if l.startswith("# ")]
    vocab = "## 本章词汇" in s
    one = "## 一句话总结" in s
    print(f"{fn}")
    print(f"  块={blocks} 中文理解={subs['中文理解']} 关键词={subs['关键词']} "
          f"为什么={subs['为什么这样写']} 提示={subs['读者视角提示']} 导航={nav}")
    print(f"  词条={len(rows)} 空单元格={len(empty)} 直撇={straight} 自标注释={ann}")
    print(f"  frontmatter={fm} H1={h1[0] if h1 else None} 本章词汇={vocab} 一句话总结={one}")
    leaks = []
    for l in lines:
        if l.startswith("**中文理解：**"):
            body = l[len("**中文理解：**"):]
            eng = re.findall(r"[A-Za-z]{2,}", body)
            if eng:
                leaks.append((eng, body[:60]))
    print(f"  中文理解英文泄漏={len(leaks)}")
    for eng, ctx in leaks:
        print("   LEAK:", eng, "::", ctx)
    if empty:
        for e in empty:
            print("   EMPTY:", e)
