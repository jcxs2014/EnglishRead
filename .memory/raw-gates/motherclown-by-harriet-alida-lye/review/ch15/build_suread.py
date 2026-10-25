# -*- coding: utf-8 -*-
import json, os, io

SRC = "notes/books/novels/motherclown-by-harriet-alida-lye/text/ch15_chapter_fourteen.txt"
OUT = ".memory/raw-gates/motherclown-by-harriet-alida-lye/review/ch15/1-suread.json"

with io.open(SRC, "r", encoding="utf-8") as f:
    text = f.read()

items = [
    ("Two days later, the bleeding becomes spotting. Three days later, it is manageable.",
     "出血两天后转为点滴状，再过三天变得可控，她认为自己能应付。"),
    ("On Friday, the fourth day, Elise returns to class.",
     "到第四天星期五，Elise 回到课堂上课。"),
    ("\u201cToday everyone is performing their autocours. You have something to share?\u201d",
     "Tomas 在课堂上问 Elise：今天每个人都要演 autocours，问她有没有东西可以分享。"),
    ("\u201cYou will not develop in this class unless you unlock that and let it out.",
     "Tomas 在课后对 Elise 说：除非她打开并释放心里那部分，否则在这门课上不会有进展。"),
    ("\u201cI can book my return flight now,\u201d she says, nodding to the credit card.",
     "Catherine 对 Elise 说，她下周某个时候大概会离开，现在就可以订回程机票，并朝信用卡点头。"),
    ("\u201cWell, it\u2019s not finished, but it\u2019ll be about me,\u201d Elise says. \u201cMy life.\u201d",
     "Elise 告诉母亲，自己要写的场景还没写完，但会写她自己、写她的生活。"),
    ("\u201cAya is not my friend. Well, not just my friend.\u201d",
     "Elise 在餐桌上对母亲 Catherine 说，Aya 不是她的朋友，或者说不仅是朋友。"),
    ("\u201cI want to tell you the story of how I met your dad.\u201d",
     "Catherine 深吸一口气，对 Elise 说她想讲自己当年如何遇见她父亲的故事。"),
]

facts = []
for anchor, fact in items:
    assert text.count(anchor) == 1, ("anchor not unique", anchor, text.count(anchor))
    start = text.index(anchor)
    end = start + len(anchor)
    assert text[start:end] == anchor
    facts.append({"anchor": anchor, "start": start, "end": end, "fact": fact})

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with io.open(OUT, "w", encoding="utf-8") as f:
    json.dump({"chapter": "ch15", "facts": facts}, f, ensure_ascii=False, indent=2)

# self-check from written file
with io.open(OUT, "r", encoding="utf-8") as f:
    data = json.load(f)
assert len(data["facts"]) == 8
for it in data["facts"]:
    assert text.count(it["anchor"]) == 1, it["anchor"]
    assert text[it["start"]:it["end"]] == it["anchor"], it["anchor"]

print("OK 8 facts")
for it in data["facts"]:
    print(it["start"], it["end"], " ".join(it["anchor"].split()[:5]))
