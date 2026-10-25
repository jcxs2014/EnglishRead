#!/usr/bin/env python3
"""Select + verify the 15 ch13 quotes (same 6 checks as select_ch12_quotes.py)."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch13_11_back_to_babylon.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch13-quotes.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())


flattext = flat(text)

# paragraphs as (start, end) absolute offsets
paras = []
pos = 0
for chunk in re.split(r"\n\s*\n", text):
    i = text.find(chunk, pos)
    if i < 0:
        i = pos
    paras.append((i, i + len(chunk), chunk))
    pos = i + len(chunk)

QUOTES = [
    # 1 para 3 — 生殖权利受威胁，拉玛什图回归
    "Reproductive rights are under profound threat, which will only bring back Lamashtu in her worst and most frightening forms: We must never forget that the core social fear Lamashtu embodies isn’t just harm to fetuses and babies but also the deaths of young women of reproductive age who weren’t able to receive lifesaving medical care but were instead left to the disastrous ministrations of Lamashtu.",
    # 2 para 3 — 从缺医少药到被剥夺医疗
    "Long ago, when Lamashtu killed women, fetuses, babies, and children, it was because medical care didn’t exist. Now, it’s because our governments are deciding that women don’t deserve access to that medical care.",
    # 3 para 5 — 父权把其他成因串起来
    "Is it wealth inequality? Is it the phenomenon by which women vote against their own rights and liberties, electing officials who want to restrict their reproductive rights, their sexual autonomy, and their public voice? Probably it’s all of them, but most of all, it’s Patriarchy, which strings all of those other things into the coercive puppet danse macabre we’re all living in.",
    # 4 para 6 — 两片同源
    "These two films—which seem miles apart within the capacious boundaries of horror about Monstrous Bitches—are intimately linked, and they give surprisingly similar answers to what is causing the feminist backslide we’re in right now. Both films, in the end, suggest that it is not just Patriarchy but also women’s own willingness to subordinate themselves to Patriarchy that we perhaps most need to fear and blame.",
    # 5 para 10 — 继承什么
    "What, the film asks, do we inherit simply by being women? The film’s answer, as we’ll see, is that we inherit Monstrous Bitchery, and in probably its gnarliest form. In this film, the Monstrous Bitch paradigm turns back to its most Lamashtean and Lamian roots: Lamashtu and Lamia are the ultimate evil, false mothers, sacrificing children rather than loving them and caring for them.",
    # 6 para 12 — 艾伦的干预
    "Annie’s mother, Ellen, was apparently hyperinvolved in Annie’s reproductive life. Annie talks about how her mother had been controlling and intrusive during her pregnancy with Peter, her first child. She did this even though Annie herself didn’t want a child, because she was too afraid, presumably, of passing along the horrific violence in her family.",
    # 7 para 13 — 历史即前史
    "So this history works exactly as the real history of Monstrous Bitchery works: Whether we are aware of it or not, the Monstrous Bitch has been calling the shots for real, human women and their horizons of possibility for a long, long time.",
    # 8 para 15 — 辱骂与咒术的千年传统
    "Annie fulfills the traditional invective-hurling, oath-swearing, curse-casting role of the Monstrous Bitch that goes back to Mesopotamia, cycles through Greece, roils through Rome, and carries through the medieval and early modern period.",
    # 9 para 17 — 母女相传
    "Like mother, like daughter: The women of this family are brutal, unstable, manipulative, cruel, dehumanizing spellcasters. Annie does it with invectives; Ellen with spells and reproductive control. Verbal violence and control are in their blood, in their psyches, and in their familial culture.",
    # 10 para 20 — 打破回咬趋势
    "This film, in a way, breaks the trend of the twenty-first century wherein the Monstrous Bitches bite back. Here, it seems more that the Monstrous Bitches are self-destructive, rather than biting back against a Patriarchy that has, for thousands of years, dehumanized and monsterized them.",
    # 11 para 22 — 回溯性产物
    "A film that seems to be about heritable Monstrous Bitchery in the female line winds up loudly confirming that Monstrous Bitchery—however autonomous it may seem—is a backformation of Patriarchy. Ari Aster, you are something else, and I salute you for your aesthetic commitment to reminding us all that, at its core, Monstrous Bitchery is best understood as an emergent property of Patriarchy itself.",
    # 12 para 25 — 药剂一分为二
    "Instead, it’s that Elisabeth splits into two selves—her true, older self and a new, younger self. At any one time, one of the selves has her intact consciousness, and the other self is a corporeal shell, paralyzed on the bathroom floor and receiving intravenous nutrition.",
    # 13 para 33 — 艾莉萨苏＝历代怪物母狗
    "This is, to my eye, the pinnacle of Fargeat’s brilliance in this film: Elisasue literally embodies the countless prior Monstrous Bitches throughout history—the Tiamats, the lamiae, the liliths, the Carmillas, the Canidias, the Furies—the other, prior women whom patriarchal culture chose to demonize and dehumanize as a way of keeping men and women alike in a state of terror about the nature of femaleness.",
    # 14 para 43 — 恩赫杜安娜与伊南娜
    "Indeed, throughout her tenure as priestess to the temples of An and Nanna, Enheduanna deepened her profound devotion to Inanna. In fact, she made quite clear that, in her view, Inanna outranked both An and Nanna in theological importance.",
    # 15 para 56 — 声音、性、生育
    "Instead, like you, I’ve grown up in a world in which women have been demonized for thousands of years, and in which they have been demonized in particular for three things: their voices, their sexuality, and their relationship to reproduction.",
]

ok = True
prev = -1
recs = []
for i, q in enumerate(QUOTES, 1):
    hits = [(s, e, c) for (s, e, c) in paras if q in c]
    f = flat(q)
    cnt = flattext.count(f)
    n = len(q.split())
    errs = []
    if len(hits) != 1:
        errs.append(f"段落命中数={len(hits)}")
        p = -1
    else:
        p = hits[0][0] + hits[0][2].index(q)
    if cnt != 1:
        errs.append(f"flat命中数={cnt}")
    if not (30 <= n <= 70):
        errs.append(f"词数={n}")
    if "…" in q or "..." in q:
        errs.append("含省略号")
    if re.search(r"[.!?]\d", q):
        errs.append("含脚注号")
    if p <= prev:
        errs.append(f"位置未递增({p}<={prev})")
    prev = p
    if errs:
        ok = False
    print(f"[{i:02d}] para={(hits[0][0] if len(hits)==1 else '?')} pos={p} words={n} flatcount={cnt} :: {'OK' if not errs else ' / '.join(errs)}")
    print("     first6:", " ".join(q.split()[:6]))
    recs.append({"no": i, "pos": p, "words": n, "text": q})

print("ALL OK" if ok else "PROBLEMS FOUND")
if ok:
    OUT.write_text(json.dumps(recs, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", OUT)
