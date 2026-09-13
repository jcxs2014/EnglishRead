"""One-off independent-review helper for The Chosen Queen (ZCode-Mac 2026-09-13).

Two sweeps over ch*.md 精读 blocks (format: `> **原句 N:**` + **关键词：** + **为什么这样写：**):
  1. flat-continuity: the whole quote (punctuation stripped) must be a contiguous
     substring of the chapter's flat text (catches cross-label splices that
     segment-wise verify passes).
  2. keyword anchoring: every English keyword word (minus stopwords, inflection
     tolerant) must occur in the quote or the why-write bullet.
Usage: python3 scripts/attic/review_chosen_queen.py <book-dir>
"""
import glob, os, re, sys, unicodedata

STOP = set(
    "a an the and or but of to in on at for with from by as is are was were "
    "be been being it its this that these those he him his she her hers they "
    "them their theirs we us our ours you your yours i me my mine not no nor "
    "so such than then there here what when where which who whom whose how why "
    "if else will would can could shall should may might must do does did done "
    "doing have has had having too very just only also even still more most own "
    "same out up down over under again once all any both each few many other "
    "some don t ll re ve m s d".split()
)


def norm(t):
    t = unicodedata.normalize("NFKD", t)
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def words(t):
    t = unicodedata.normalize("NFKD", t)
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    out = []
    for w in re.findall(r"[a-z]+(?:'[a-z]+)?", t.lower()):
        out.append(w.replace("'", ""))
    return out


def stems(w):
    yield w
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            yield w[: -len(suf)]


def main(book_dir):
    texts = {}
    tdir = os.path.join(book_dir, "text")
    for f in sorted(glob.glob(os.path.join(tdir, "ch*.txt"))):
        key = os.path.basename(f).split("_")[0]
        texts[key] = norm(open(f, encoding="utf-8").read())

    cont_bad = []
    anchor_bad = []
    total_blocks = 0
    total_kw = 0
    for f in sorted(glob.glob(os.path.join(book_dir, "ch*.md"))):
        base = os.path.basename(f)
        key = base.split(" ")[0]
        if key not in texts:
            print("!! no text file for", base)
            continue
        hay_chapter = texts[key]
        lines = open(f, encoding="utf-8").read().splitlines()
        heads = [
            (i, re.sub(r"^>\s*\*\*原句\s*\d+:\*\*\s*", "", l.strip()))
            for i, l in enumerate(lines)
            if re.match(r"^>\s*\*\*原句\s*\d+:\*\*", l.strip())
        ]
        bounds = [i for i, _ in heads] + [len(lines)]
        for k, (start, qtext) in enumerate(heads):
            total_blocks += 1
            seg = lines[bounds[k] : bounds[k + 1]]
            fq = norm(qtext)
            # 1. continuity sweep
            if fq and fq not in hay_chapter:
                cont_bad.append((base, f"原句{k+1}", qtext[:70]))
            # 2. keyword anchoring
            kw = " ".join(
                l for l in seg if l.strip().startswith("**关键词")
            )
            why = " ".join(
                l for l in seg if l.strip().startswith("**为什么这样写")
            )
            hay = norm(qtext) + " " + norm(why)
            for w in words(kw):
                if w in STOP or len(w) < 3:
                    continue
                total_kw += 1
                if not any(s in hay for s in stems(w)):
                    anchor_bad.append((base, f"原句{k+1}", w))
    print(f"blocks={total_blocks} kw_tokens={total_kw}")
    print(f"-- continuity violations: {len(cont_bad)}")
    for v in cont_bad:
        print("   ", v)
    print(f"-- anchor violations: {len(anchor_bad)}")
    for v in anchor_bad:
        print("   ", v)


if __name__ == "__main__":
    main(sys.argv[1])
