# -*- coding: utf-8 -*-
"""Build 1-suread.json for Mother Clown ch16 (chapter fifteen). Read-only over the source text."""
import json
import os

SRC = (
    "notes/books/novels/motherclown-by-harriet-alida-lye/text/"
    "ch16_chapter_fifteen.txt"
)
OUT = (
    ".memory/raw-gates/motherclown-by-harriet-alida-lye/review/ch16/"
    "1-suread.json"
)

with open(SRC, "r", encoding="utf-8") as f:
    text = f.read()

facts = [
    # 开头
    ("It had been a terrible night. A terrible string of nights.",
     "Catherine 连续过了好几个糟糕的夜晚，婴儿 Elisabeth 整夜吃奶，两人都没睡。"),
    ("Catherine had just turned twenty but she didn\u2019t have time to celebrate.",
     "Catherine 刚满二十岁，没有时间庆祝。"),
    ("she told Catherine to call the local priest to perform an exorcism.",
     "母亲 Patricia 在一次散步中听到 Elisabeth 尖叫后，让 Catherine 去请当地神父来做驱魔。"),
    # 关键关系：谁是生父
    ("he is the man who raised you. He\u2019s your dad. But he\u2019s not\u2014",
     "Catherine 对女儿说：Seb 是把她养大的人、是她的爸爸，但不是（她的生父）。"),
    # 转折
    ("She ran to the stroller, but Elisabeth wasn\u2019t there. She wasn\u2019t there.",
     "Catherine 冲回婴儿车，发现 Elisabeth 不在车里。"),
    ("beside her stroller, a man she didn\u2019t know, and he was holding a baby.",
     "Catherine 在婴儿车旁看见一个她不认识的男人，他正抱着一个婴儿。"),
    # 数字
    ("He proposed four months after they met and she said yes",
     "Seb 在两人相识四个月后求婚，Catherine 答应了。"),
    # 结尾
    ("With that, her daughter leaves, just as Catherine had predicted.",
     "说完这些，女儿 Elise 起身离开，正如 Catherine 预料的那样。"),
]

out_facts = []
for anchor, fact in facts:
    n = text.count(anchor)
    assert n == 1, (n, anchor)
    start = text.index(anchor)
    end = start + len(anchor)
    assert text[start:end] == anchor
    out_facts.append({"anchor": anchor, "start": start, "end": end, "fact": fact})

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"chapter": "ch16", "facts": out_facts}, f, ensure_ascii=False, indent=2)

# ---- self-check ----
with open(OUT, "r", encoding="utf-8") as f:
    data = json.load(f)
assert data["chapter"] == "ch16"
assert len(data["facts"]) == 8
for it in data["facts"]:
    a, s, e = it["anchor"], it["start"], it["end"]
    assert isinstance(s, int) and isinstance(e, int)
    assert text[s:e] == a, ("slice mismatch", a)
    assert text.count(a) == 1, ("not unique", a)
    wc = len(a.split())
    assert 8 <= wc <= 15, (wc, a)

print("SELF-CHECK: ALL PASS (8 facts, each count==1, text[start:end]==anchor)")
for i, it in enumerate(data["facts"], 1):
    print(i, it["start"], it["end"], len(it["anchor"].split()), "|", " ".join(it["anchor"].split()[:5]))
