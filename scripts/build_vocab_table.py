#!/usr/bin/env python3
"""Build a three-tier vocab table from vocab_candidates.py output, with glosses supplied
as a dict keyed by headword. No headword or example sentence is ever typed by hand —
both come from the generator, which reads text/chNN.txt.

Usage:  python3 scripts/build_vocab_table.py <book-dir> --ch NN --tiers '<json gloss map>'
        (gloss map: {"⭐⭐⭐": {"head": "释义", ...}, "⭐⭐": {...}, "⭐": {...}})
The example-sentence column is always the generator's verbatim sentence.
"""
import argparse
import json
import subprocess
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book_dir")
    ap.add_argument("--ch", required=True)
    ap.add_argument("--tiers", required=True, help="JSON gloss map")
    ap.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()

    gloss = json.loads(a.tiers)
    out = subprocess.run(
        [sys.executable, "scripts/vocab_candidates.py", a.book_dir,
         "--ch", a.ch, "--tiers", "--limit", str(a.limit)],
        capture_output=True, text=True, check=True,
    ).stdout

    # parse: "### ⭐⭐⭐ 高级" headings then table rows "| headword | (释义待填) | "example" |"
    cur, rows = None, []
    for line in out.splitlines():
        if line.startswith("### "):
            cur = line[4:].split()[0]
            rows.append((cur, []))
            continue
        if cur and line.startswith("| ") and "释义待填" in line:
            cells = [c.strip() for c in line.strip("|").split(" | ")]
            rows[-1][1].append((cells[0], cells[2]))

    print("| 词汇 | 释义 | 例句 |")
    print("|------|------|------|")
    filled = miss = 0
    for tier, items in rows:
        gm = gloss.get(tier, {})
        for head, sent in items:
            g = gm.get(head)
            if not g:
                print(f"MISSING GLOSS: [{tier}] {head}", file=sys.stderr)
                miss += 1
                continue
            print(f"| {head} | {g} | {sent} |")
            filled += 1
    print(f"<!-- filled {filled}, missing {miss} -->", file=sys.stderr)
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
