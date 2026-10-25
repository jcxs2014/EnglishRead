#!/usr/bin/env python3
"""ch05 引语（连续、无省略号）核验：逐字 / 词数 / 句数 / 展平唯一命中 / 位置递增。"""
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TEXT = (REPO / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch05_3_roman_witch_bitches_the_persistence_of.txt").read_text(encoding="utf-8")
flat = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())

# (start_marker, end_marker) —— 连续引语，两端都是原文原词
BLOCKS = [
 (1,  "When I say “older women,” I mean women between about twenty and thirty:",
        "we see both a proliferation in the number of Monstrous Bitches and a diminution in their power."),
 (2,  "Indeed, the Roman Monstrous Bitch is even further humanized than the Greek Monstrous Bitches from the last chapter.",
        "who just happen to be able to bend nature and other human beings to their will through spellcraft."),
 (3,  "As will surprise no one who’s made it to this point in this book,",
        "but also because Horace is obsessed with her."),
 (4,  "Horace may vary the traits he assigns to Canidia in each of his works,",
        "to reanimate and recode the cultural DNA of Lamia and Medea for ancient Rome."),
 (5,  "The message of the opening of The Aeneid, then, is that women are disposable,",
        "Aeneas meets Queen Dido of Carthage, who is the most splendid literary ancient ruler I am aware of."),
 (6,  "Does that sound like an outtake from The Bacchae crossed with The Eumenides?",
        "another critically important and entirely human Monstrous Bitch: She is a human female version of Dionysus."),
 (7,  "So just as Tiamat was thrown down to form the ground we stand on,",
        "dispatched to the underworld, made abject once again. But not forever."),
 (8,  "But what Lucan seems to find most terrifying about Erichtho",
        "but they sure do follow Dionysus."),
 (9,  "Instead, much more like Medea, they’ve managed to weave themselves into the daily lives of regular people,",
        "Reproductive harm, sexual harm, spellcasting harm."),
 (10, "Older woman enslaves man with vagina.",
        "They are seductresses of formidable sexual power, notwithstanding their age."),
 (11, "By the end of the second century CE, then, when Apuleius is writing,",
        "attacks the blood and bodies of children and young men."),
 (12, "Obyzouth and Gello aren’t human, and they’re not comic relief.",
        "very much intact in the Greek eastern Mediterranean, from the first century CE through the Middle Ages."),
 (13, "Like Lamashtu, Lilith casts herself as the semidivine progenitrix of infanticide.",
        "invade people’s homes, seducing husbands, strangling babies, and sucking out the blood of children."),
 (14, "Their main function, in all the regions in which they appear, is to cause reproductive havoc.",
        "But they also destroy fetuses in the womb, prompting miscarriages."),
 (15, "So Romanitas didn’t tame and humanize Lamia everywhere.",
        "where the twin patriarchates of Western Christianity and Roman culture flowed together."),
]

KEYWORDS = {
 1: ["women between about twenty and thirty", "proliferation in the number", "diminution in their power", "ossified patriarchal social order"],
 2: ["even further humanized", "human women", "bend nature and other human beings", "through spellcraft"],
 3: ["Latin word for “dog,”", "literally a monstrous “bitch.”", "unleashes chaos wherever she goes", "Horace is obsessed with her"],
 4: ["Horace may vary the traits", "taken in the aggregate", "cultural DNA of Lamia and Medea", "reanimate and recode"],
 5: ["women are disposable", "men are essential", "protecting a new fatherland", "Queen Dido of Carthage"],
 6: ["The Bacchae crossed with The Eumenides", "Patriarchy cannot function", "raise their voices up together", "human female version of Dionysus"],
 7: ["Tiamat was thrown down", "Furies were banished from Athens", "must find her way under the earth", "But not forever"],
 8: ["most terrifying about Erichtho", "none of those other Monstrous Bitch incarnations", "She does not fear the gods", "sure do follow Dionysus"],
 9: ["weave themselves into the daily lives", "three core catastrophic powers", "eat their flesh and drink their blood", "Reproductive harm, sexual harm"],
 10: ["Older woman enslaves man with vagina", "what we might today call cougars", "seductresses of formidable sexual power", "notwithstanding their age"],
 11: ["had come to denote a Monstrous Bitch", "sexually predatory, baby-slaying, spellcasting", "Lamia has become lamiae", "she is an everywoman now"],
 12: ["not comic relief", "deadly and deadly serious demonesses", "baby-slaying, and woman-torturing", "very much intact in the Greek eastern Mediterranean"],
 13: ["semidivine progenitrix of infanticide", "an army of followers and helpers", "Lilith and her army of liliths", "sucking out the blood of children"],
 14: ["cause reproductive havoc", "eat their prey’s livers, lungs, and hearts", "destroy fetuses in the womb", "prompting miscarriages"],
 15: ["didn’t tame and humanize Lamia everywhere", "undergoes truly massive change", "in western Europe", "twin patriarchates of Western Christianity"],
}

ok = True
quotes = {}
positions = []
print("=== 引语核验（连续 / 无省略号）===")
for n, sm, em in BLOCKS:
    i = TEXT.index(sm)
    j = TEXT.index(em, i) + len(em)
    q = TEXT[i:j]
    quotes[n] = q
    words = len(q.split())
    sents = len(re.findall(r"[.!?][”\"']?(?=\s|$)", q))
    f = flat(q)
    cnt = flat(TEXT).count(f)
    first = flat(TEXT).find(f)
    positions.append((n, first))
    bad = []
    if "…" in q or "..." in q:
        bad.append("含省略号")
    if not (30 <= words <= 70):
        bad.append(f"词数{words}")
    if not (1 <= sents <= 3):
        bad.append(f"句数{sents}")
    if cnt != 1:
        bad.append(f"展平命中{cnt}次")
    if bad:
        ok = False
    print(f"block {n:2d} 词={words:3d} 句={sents} 展平命中={cnt} {'OK' if not bad else '!! ' + ' '.join(bad)}")

print()
print("=== 块序递增 ===")
prev = -1
for n, p in positions:
    if p <= prev:
        ok = False
        print(f"!! block {n} 位置 {p} 未递增")
    prev = p
if all(positions[i][1] < positions[i+1][1] for i in range(len(positions)-1)):
    print("OK 15 块位置严格递增")

print()
print("=== 关键词逐字命中（须在本块引语内）===")
for n in sorted(KEYWORDS):
    q = quotes[n]
    for kw in KEYWORDS[n]:
        hit = kw in q
        if not hit:
            ok = False
        print(f"{'OK ' if hit else '!! '}block {n:2d} {kw!r} 词数={len(kw.split())}")

out = REPO / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch05-quotes.json"
out.write_text(json.dumps(quotes, ensure_ascii=False, indent=1), encoding="utf-8")
print()
print("ALL OK" if ok else "HAS PROBLEMS")
print("written:", out)
