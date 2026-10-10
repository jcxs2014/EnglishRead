#!/usr/bin/env python3
"""把「关键词行」重排回它所描述的引语块，并复用门禁自己的判据。

它替代的动作是「按块序号回填关键词」——序号在删块重编后会整体错位一格，
于是关键词行说的全是**上一块**的内容（占全库本类阻断型的大多数）。

用法：python3 scripts/realign_block_keywords.py <书目录> [--dry]
"""
import itertools
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_block_keywords as cbk  # noqa: E402
from build_block_keywords import pick  # noqa: E402

HEAD = re.compile(r'^> \*\*原句\s*(\d+)[：:]\*\*\s*(.*)$', re.M)
KW = re.compile(r'^\*\*关键词\*\*[：:][ \t]*(.*)$', re.M)
KW2 = re.compile(r'^\*\*关键词[：:]\*\*[ \t]*(.*)$', re.M)


def anchors(kwval, quote):
    qflat = cbk._flat(cbk.norm(quote))
    parts = cbk._split_kw(kwval)
    if not parts:
        return False
    return all(cbk._kw_in_quote(k, qflat) or
               cbk._kw_in_quote(cbk._BRACKET.sub("", k), qflat) for k in parts)


def parse(s):
    heads = list(HEAD.finditer(s))
    blocks = []
    for i, m in enumerate(heads):
        end = s.find("\n", m.start()) + 1          # 引语行末
        nxt = heads[i + 1].start() if i + 1 < len(heads) else len(s)
        quote = m.group(2).strip().strip('"“‘”’').strip()
        blocks.append({"num": m.group(1), "quote": quote,
                       "qend": end, "body": s[end:nxt]})
    kws = [(m.start(1), m.end(1), m.group(1)) for m in KW.finditer(s)]
    return blocks, kws


def realign(path, dry):
    s = path.read_text(encoding="utf-8")
    blocks, kws = parse(s)
    n = min(len(blocks), len(kws))
    if len(blocks) != len(kws):
        print(f"  ⚠️ {path.name}: 引语块 {len(blocks)} ≠ 关键词行 {len(kws)}，跳过")
        return 0
    bad = []
    for i, b in enumerate(blocks):
        miss = [k for k in cbk._split_kw(kws[i][2])
                if not anchors(k, b["quote"]) and not cbk._echoed(k, b["body"])]
        if miss:
            bad.append(i)
    if not bad:
        return 0
    # 候选：坏块之间互相重排（好块保持自己的行不动）。
    # 观测到的错位形态是「关键词行整体下移一格」⇒ 本块应取**下一块**的行。
    used, assign = set(), {}
    for i in bad:
        cand = [j for j in bad if j != i and j not in used
                and anchors(kws[j][2], blocks[i]["quote"])]
        cand.sort(key=lambda j: (abs(j - i - 1), abs(j - i)))
        if cand:
            assign[i] = cand[0]
            used.add(cand[0])
    edits = []
    for i in bad:
        j = assign.get(i)
        new = kws[j][2] if j is not None else " / ".join(pick(blocks[i]["quote"]))
        if new and new != kws[i][2]:
            edits.append((kws[i][0], kws[i][1], new))
            print(f"  {path.name} 原句{blocks[i]['num']}: "
                  f"{'移自原句' + blocks[j]['num'] if j is not None else '由本块引语生成'} "
                  f"→ {new}")
    for st, en, new in sorted(edits, reverse=True):
        s = s[:st] + new + s[en:]
    if edits and not dry:
        path.write_text(s, encoding="utf-8")
    return len(edits)


def main():
    book = Path(sys.argv[1])
    dry = "--dry" in sys.argv
    total = 0
    for md in sorted(book.glob("ch*.md")):
        total += realign(md, dry)
    print(f"\n共改写关键词行 {total} 条{'（dry-run，未落盘）' if dry else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
