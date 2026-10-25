#!/usr/bin/env python3
"""Validate the 15 planned ch12 quotes against the verbatim source text.

Checks per quote:
  1. contiguous substring of ONE natural paragraph (no cross-paragraph splice)
  2. 30-70 words
  3. unique flat() hit in the whole chapter text
  4. strictly increasing source positions
  5. no footnote marker ([.!?] followed by a digit)
  6. no ellipsis
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch12_10_monstrous_bitches_bite_back.txt"
OUT = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production/ch12-quotes.json"

text = TXT.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())


flattext = flat(text)

# paragraph spans: split on blank lines, keep offsets
paras = []
pos = 0
for chunk in re.split(r"\n\s*\n", text):
    idx = text.find(chunk, pos)
    if idx < 0:
        idx = pos
    paras.append((idx, idx + len(chunk), chunk))
    pos = idx + len(chunk)

QUOTES = [
    # 1 Ginger Snaps — the girls playing
    "They are playing at vampirism, playing at murder, playing at being creatures of the night, playing at being witches. They are playing at being the Monstrous Bitches who populate their cultural history. But pretty soon, it won’t be a game anymore.",
    # 2 Ginger Snaps — the bite
    "On the way home from their jaunt, a massive doglike creature starts pursuing them. They almost get away, but Ginger gets bitten by the thing, whatever it is. This is a bummer, because Ginger has also just started her first period, and the combination of menstruation and crazy dog bite is bad news.",
    # 3 Ginger Snaps — mormolyke / canis lineage
    "And remember that Lamia is described by Philostratus as a mormolyke, or werewolf. And our old friend Canidia, of course, has a name derived from canis, Latin for “dog.” Now a werewolf woman, Ginger has transitioned from girlhood into young womanhood by stepping into a long, long lineage of Monstrous Bitchery, her teething snapping back at the patriarchal world around her.",
    # 4 Ginger Snaps — eternal return
    "You can’t kill the Monstrous Bitch within, even if you kill one particular instantiation of her. She’ll come back again and again, throughout time, to seduce, rape, drink blood, kill young people, voice her salacious and rapacious views, and leave corpses in her wake. Patriarchy will never be safe from her.",
    # 5 Jennifer’s Body — the possession ritual as gang rape
    "They do this because they want their rock band to become internationally famous, and they believe that by offering Jennifer up to be possessed by demonic forces, they will get their wish. The possession ritual is a barely veiled allegory for gang rape; the result of this rape-possession, for Jennifer, is that she is turned into a demonically sexy vampiress cannibal wolf-woman.",
    # 6 Jennifer’s Body — two origins
    "Now this is interesting. Jennifer’s origin story as a Monstrous Bitch is one of gang rape framed as demonic possession. Needy’s Monstrous Bitch origin isn’t about rape or demonic possession—it’s about monstrous contagion between women.",
    # 7 Jennifer’s Body — Laura and Carmilla
    "Jennifer and Needy are thus the Laura and Carmilla of the twenty-first century, bound by blood and forbidden love. But whereas Laura, in Carmilla, escapes conversion to vampirism and is “saved” by the men in her life, this little bit of saliva that gets into Needy from Jennifer is enough to change Needy forever.",
    # 8 Raw — cannibalism as a heritable trait
    "This is a film in which—to use modern terminology—cannibalism is a sex-linked, autosomal-dominant trait in female children, which only has to be triggered by a mild environmental injury in order to awaken the pathological process. It is inherited and environmental.",
    # 9 Raw — born bad
    "Monstrous Bitches in Raw come by their monstrosity through a matrilinear process of inheritance; monstrosity is understood to be innate, baked into a woman’s nature, her essential character as it descends to her from her mother. This reflects the theory of Monstrous Bitchery advocated by dominant patriarchies, going back to Tiamat and Lilith and Lamia. These bitches are born bad, because their mommies are bad.",
    # 10 Raw — the dual argument
    "But she’s also saying, Monstrous Bitchery is also caused by the forcible violation of women’s bodies by a patriarchal order that wants to put things in her—penises, babies, food—that she doesn’t want. And Julia Ducournau, through her flesh-eating heroine Justine, isn’t having it anymore. Justine is going to bite back hard.",
    # 11 The Witch — William calls his wife like a dog
    "With no thought to the physical safety or wishes of his wife and four children, he says, “Katherine,” beckoning his wife to his side like a dog. He doesn’t address the children at all, nor does he reassure them that he has any kind of a plan, or vision, or even basic resources for their survival.",
    # 12 The Witch — power by adjacency
    "But this magnificent film is going to go out of its way to show how she—the wicked witch of the woods—is given power and authority directly by her adjacency to a predatory, abusive, controlling patriarch, William. On top of that, the film will show how her Monstrous Bitchery offers Thomasin a way out of that predatory, abusive, controlling Patriarchy, once and for all.",
    # 13 The Witch — victim to opponent
    "Thomasin, in this film, goes from being a victim of Patriarchy to being its opponent. Even in the moment of her transcendent transformation into a Monstrous Bitch, she is nevertheless cast by the film as our hero.",
    # 14 Suspiria — not cozy
    "It’s more one of waking up, coming to a new consciousness, but it’s not one of mirth, laughter, or any kind of facile peace. Guadagnino doesn’t retreat into the realm of consolation in his film. The new world order may be feminist as all hell, but that doesn’t mean it’s going to be cozy.",
    # 15 Closing — protagonist and heroine
    "To varying degrees, that’s true in Ginger Snaps, Raw, Suspiria, The Witch, and Jennifer’s Body. But something really has shifted, because, in all of these films, the Monstrous Bitch is the protagonist and, increasingly, the heroine.",
]

errors = []
records = []
last_pos = -1
for i, q in enumerate(QUOTES, 1):
    n = len(q.split())
    # paragraph containment
    hits = [(s, e) for (s, e, c) in paras if q in c]
    if len(hits) != 1:
        errors.append(f"Q{i}: contained in {len(hits)} paragraphs (need exactly 1)")
        continue
    s, e = hits[0]
    abs_pos = text.find(q, s)
    cnt = flattext.count(flat(q))
    if cnt != 1:
        errors.append(f"Q{i}: flat hit count = {cnt} (need 1)")
    if not (30 <= n <= 70):
        errors.append(f"Q{i}: word count {n} out of 30-70")
    if re.search(r"[.!?]\d", q):
        errors.append(f"Q{i}: contains footnote-like digit after punctuation")
    if "…" in q or "..." in q:
        errors.append(f"Q{i}: contains ellipsis")
    if abs_pos <= last_pos:
        errors.append(f"Q{i}: position {abs_pos} not strictly after {last_pos}")
    last_pos = abs_pos
    records.append({"n": i, "pos": abs_pos, "nwords": n, "count": cnt, "text": q})

if errors:
    for e in errors:
        print("ERROR:", e)
    raise SystemExit(1)

OUT.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
for r in records:
    first6 = " ".join(r["text"].split()[:6])
    print(f"Q{r['n']:2d}  pos={r['pos']:6d}  w={r['nwords']:3d}  hit={r['count']}  | {first6}")
print("OK: 15 quotes validated, positions strictly increasing")
