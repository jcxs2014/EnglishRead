import re, sys

CAND = {
    "text/ch14_chapter_4.txt": [
        "decapitated", "hovering", "mortified", "platitudes", "affliction", "raucous", "manic", "tiptoe",
        "scarlet letter", "flask", "dimples", "pivot", "wobbly", "discretion", "vantage", "dahlia",
        "mood-killer", "prodigious",
        "bar", "purse", "couch", "arch", "window", "door", "closet", "heels",
    ],
    "text/ch15_chapter_5.txt": [
        "jumpsuit", "cheekbones", "veneers", "kitschy", "anticipating", "abject", "tattered", "cartoonishly",
        "strategic", "boxed in", "neurosis", "psychotic", "imperfections", "faint of heart",
        "vulnerability", "hors d'oeuvres", "finger whistle", "command of the space",
        "window", "menu", "chair", "glass", "toast", "key", "bathroom", "cabin",
    ],
    "text/ch16_chapter_6.txt": [
        "reprieve", "ethereal", "majesty", "choreography", "trauma bonded", "iridescent", "tendrils", "delusion",
        "backslid", "swig", "follow-ups", "paranoia", "postcoital", "misjudgment", "placate", "ominous",
        "balaclava", "unkindness",
        "porch", "swing", "bag", "key", "door", "bed", "window", "suit",
    ],
}

for path, words in CAND.items():
    s = open(path, encoding="utf-8").read().replace("\u2019", "'")
    print("==", path)
    for w in words:
        n = len(re.findall(re.escape(w), s, flags=re.I))
        print(f"   {'OK ' if n else 'MISS'} {w:24s} x{n}")
