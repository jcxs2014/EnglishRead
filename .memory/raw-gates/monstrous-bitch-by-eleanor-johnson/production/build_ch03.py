#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建 ch03 精读 md：引语逐字从 text/ 抽取，避免转写误差。"""
import re, unicodedata, sys, pathlib

ROOT = pathlib.Path("/Users/jcxs2014/Documents/Works/EnglishRead")
BOOK = ROOT / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson"
TXT = BOOK / "text/ch03_1_monstrous_bitches_of_ancient_mesopotam.txt"
OUT = BOOK / "ch03 1 monstrous bitches of ancient mesopotamia demons and goddesses.md"

T = TXT.read_text(encoding="utf-8")

def flat(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())

TF = flat(T)

def span(start, end):
    i = T.find(start)
    assert i >= 0, ("START NOT FOUND", start[:60])
    j = T.find(end, i)
    assert j >= 0, ("END NOT FOUND", end[:60])
    s = T[i:j + len(end)]
    f = flat(s)
    cnt = TF.count(f)
    assert cnt == 1, ("NOT UNIQUE", cnt, start[:60])
    return s

Q = []
Q.append(span("Ancient Mesopotamia—in the Fertile Crescent", "about 100 CE."))
Q.append(span("Don’t get me wrong; Mesopotamian rulers", "power of women."))
Q.append(span("Lamashtu is a demoness, and she is the daughter", "She is an autonomous demon."))
Q.append(span("all this very real and very abject terror", "ravager of women."))
Q.append(span("First, we learn that Lamashtu is highborn", "banish her from heaven."))
Q.append(span("Let me slow this down for a moment", "across the human world."))
Q.append(span("It was her father who loosed Lamashtu on the world.",
              "children, babies, and fetuses."))
Q.append(span("This strange duality, wherein Lamashtu is both repulsively doglike",
              "both sexy and repulsive."))
Q.append(span("Fierce, wicked, sneaky, and unnatural, Lamashtu has the power",
              "as would her baby."))
Q.append(span("Over a thousand years after the earliest incantations to Lamashtu",
              "the creation of man."))
Q.append(span("Tiamat has a second power, one at least as frightening as her womb",
              "into silence and abject fear."))
Q.append(span("Symbolically, her swelling belly represents", "Marduk rapes Tiamat to death."))
Q.append(span("Tiamat was scary in theory, but Lamashtu was scary in practice.",
              "she could only temporarily be warded off."))
Q.append(span("But there is a crucial difference between them", "Tiamat had not been."))
Q.append(span("Sex, reproduction, and voice—not coincidentally",
              "for as long as the world has had writing."))
for i, q in enumerate(Q, 1):
    print(f"[{i:2d}] words={len(q.split()):3d} pos={TF.find(flat(q)):6d} :: {q[:58]}")

# 顺序必须严格递增
pos = [TF.find(flat(q)) for q in Q]
assert pos == sorted(pos) and len(set(pos)) == len(pos), "ORDER PROBLEM"

# ── 词表例句：逐字从原文取句 ──
def sentence_with(word, start=0):
    """取包含 word 的一句（按句末标点切分），返回逐字原文。"""
    # 先按句末标点切分全篇
    sents = re.split(r"(?<=[.!?])\s+", T)
    cands = []
    for s in sents:
        if word not in s:
            continue
        s = s.strip()
        if not (25 <= len(s) <= 400):
            continue
        cands.append(s)
    if cands:
        return min(cands, key=len)
    # 退路：取分号子句
    for s in sents:
        if word not in s:
            continue
        for cl in re.split(r";\s+", s):
            cl = cl.strip()
            if word in cl and 30 <= len(cl) <= 300:
                return cl
    raise AssertionError(("NO SENTENCE FOR", word))

VOCAB = [
    # (档, 词头, 释义, 取句用的关键词)
    ("3", "cuneiform", "楔形文字；古代美索不达米亚的书写系统", "cuneiform"),
    ("3", "proto-monotheistic", "原初一神教的；向一神信仰过渡的", "proto-monotheistic"),
    ("3", "iconography", "图像志；固定的神祇形象与标识系统", "iconography"),
    ("3", "autochthonous", "原生的；自发产生的", "autochthonous"),
    ("3", "talisman", "护身符；用于避邪的符物", "talisman"),
    ("3", "exorcist", "驱邪者；施法逐魔的祭司", "exorcist"),
    ("3", "succubus", "女魅魔；勾引男性的女妖", "succubus"),
    ("3", "larynx", "喉头；嗓音的发声器官", "larynx"),
    ("2", "incantation", "咒语；用于驱邪或治病的祷文", "incantations"),
    ("2", "amulet", "护身符片；贴身佩戴以避祸的小物", "amulets"),
    ("2", "demoness", "女魔；女性形态的恶灵", "demoness"),
    ("2", "spellcasting", "施法；施展巫术", "spellcasting"),
    ("2", "hypersexual", "极度性欲的；沉溺于性欲的", "hypersexual"),
    ("2", "paralyze", "使瘫痪；使失去回应能力", "paralyze"),
    ("2", "matriarch", "母系首领；女家长", "matriarch"),
    ("2", "reptilian", "爬行动物的；爬虫般的", "reptilian"),
    ("1", "newborn", "新生儿；刚出生的婴儿", "newborn"),
    ("1", "lair", "巢穴；野兽的藏身之处", "lair"),
    ("1", "scribes", "书记员；抄写与记录文字的人", "scribes"),
    ("1", "inheritance", "继承；遗产与继承权", "inheritance"),
    ("1", "goddess", "女神", "goddess"),
    ("1", "clay", "黏土；泥板", "clay"),
]

rows = []
for tier, head, gloss, key in VOCAB:
    ex = sentence_with(key)
    # 例句必须含词头（大小写不敏感）
    assert head.lower() in ex.lower(), ("HEAD NOT IN EXAMPLE", head, ex[:80])
    # 例句必须逐字命中本章
    f = flat(ex)
    assert f[:60] in TF, ("EXAMPLE NOT IN CORPUS", head, ex[:80])
    assert not re.search(r"[一-鿿]", ex), ("CHINESE IN EXAMPLE", head)
    rows.append((tier, head, gloss, ex))

print("\n=== 词表例句 ===")
for tier, head, gloss, ex in rows:
    print(f"[{tier}] {head:18s} | {ex[:110]}")

import json
(ROOT / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch03-quotes.json").write_text(
    json.dumps({"quotes": Q, "vocab": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nOK")
