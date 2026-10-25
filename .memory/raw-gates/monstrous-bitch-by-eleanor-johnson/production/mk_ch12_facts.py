#!/usr/bin/env python3
"""Verify candidate anchors for ch12 facts.txt against the verbatim source text."""
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch12_10_monstrous_bitches_bite_back.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch12-facts.txt"

text = TXT.read_text(encoding="utf-8")

FACTS = [
    (
        "Ginger’s snap is a snap into actual bitchdom",
        "《姜汁 snaps》：那一咬触发四件事——狼人化、极端性欲、食人、攻击性，作者称金杰是「真刀真枪地咬进了母狗的身份」。",
    ),
    (
        "You can’t kill the Monstrous Bitch within, even if you kill one particular instantiation of her.",
        "《姜汁 snaps》全系列的结论：杀不掉她体内的怪物母狗，哪怕杀掉了她的某一次具体化身——她还会一次次回来。",
    ),
    (
        "Jennifer is made a Monstrous Bitch by a patriarchal order that wants to use her body for its own gain; she is not born as one.",
        "《詹妮弗的身体》：杰妮弗是被一个想用她身体抬自己身价的父权秩序「做」成怪物母狗的，不是天生如此。",
    ),
    (
        "Needy’s Monstrous Bitch origin isn’t about rape or demonic possession—it’s about monstrous contagion between women.",
        "《詹妮弗的身体》：妮迪的怪物母狗来历不是强奸也不是附体，而是女性之间的怪物传染，因此落在酒神／吸血鬼／狼人传统而非附体传统。",
    ),
    (
        "cannibalism is a sex-linked, autosomal-dominant trait in female children",
        "《生肉》：贾斯汀一家女性只要肉进了嘴就必然成为食人者——食人在这部电影里是伴性、常染色体显性遗传的女性特征。",
    ),
    (
        "She is a colonial American Erichtho",
        "《女巫》：林中老巫被作者写成一位「殖民地美洲的埃里克托」，同时是猎巫时代厌女症的范本。",
    ),
    (
        "The new world order may be feminist as all hell, but that doesn’t mean it’s going to be cozy.",
        "《Suspiria》结尾的保留：新的世界秩序可以女性主义到极点，但绝不等于舒适。",
    ),
    (
        "But something really has shifted, because, in all of these films, the Monstrous Bitch is the protagonist and, increasingly, the heroine.",
        "全章落点：确实有什么东西变了——在这些影片里怪物母狗成了主角，而且越来越是女主角。",
    ),
]

lines = []
bad = []
for anchor, fact in FACTS:
    if text.count(anchor) == 1:
        lines.append(f"{anchor} || {fact}")
    else:
        bad.append((anchor, text.count(anchor)))

if bad:
    for a, c in bad:
        print("MISS:", repr(a), "count=", c)
    raise SystemExit(1)

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("facts written:", len(lines))
