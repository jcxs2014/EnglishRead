"""One-off independent-review helper: keyword anchoring (AGENTS.md rule 8e).

For each numbered quote block in ch*.md, every English word in the
keyword bullet (minus stopwords, allowing inflections) must occur in
the block quote or in the why-write-this-way bullet.
Usage: python3 scripts/attic/kw_anchor_review.py <book-dir>
"""
import glob
import os
import re
import sys
import unicodedata

CIRC = "123456789:;<=>?"  # placeholder replaced below
CIRC = "\u2460\u2461\u2462\u2463\u2464\u2465\u2466\u2467\u2468\u2469"
STOP = set(
    "a an the and or but of to in on at for with from by as is are was were "
    "be been being it its this that these those he him his she her hers they "
    "them their theirs we us our ours you your yours i me my mine not no nor "
    "so such than then there here what when where which who whom whose how why "
    "if else will would can could shall should may might must do does did done "
    "doing have has had having too very just only also even still more most own "
    "same out up down over under again once all any both each few many other "
    "some such will just don t ll re ve m s d".split()
)


def norm(t):
    t = unicodedata.normalize("NFKD", t)
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    return t.lower()


def stems(w):
    yield w
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            yield w[: -len(suf)]


def main(book_dir):
    viol = []
    total = 0
    files = sorted(glob.glob(os.path.join(book_dir, "ch*.md")))
    for f in files:
        base = os.path.basename(f)
        lines = open(f, encoding="utf-8").read().splitlines()
        heads = [
            (i, l.strip())
            for i, l in enumerate(lines)
            if re.match(r"\*\*[" + CIRC + r"]\*\*\s+\"", l.strip())
        ]
        bounds = [i for i, _ in heads] + [len(lines)]
        for k in range(min(10, len(heads))):
            seg = lines[bounds[k] : bounds[k + 1]]
            quote = norm(heads[k][1])
            why = " ".join(
                l for l in seg if l.strip().startswith("- \u4e3a\u4ec0\u4e48\u8fd9\u6837\u5199")
            )
            hay = quote + " " + norm(why)
            kw_text = " ".join(
                l for l in seg if l.strip().startswith("- \u5173\u952e\u8bcd")
            )
            words = re.findall(r"[a-z]+(?:'[a-z]+)?", norm(kw_text))
            for w in words:
                if w in STOP or len(w) < 3:
                    continue
                total += 1
                if not any(s in hay for s in stems(w)):
                    viol.append((base, "b" + str(k + 1), w))
    print("checked %d keyword tokens; violations: %d" % (total, len(viol)))
    for v in viol:
        print(v)


if __name__ == "__main__":
    main(sys.argv[1])
