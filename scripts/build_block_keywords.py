#!/usr/bin/env python3
"""为引语块生成关键词：只从**该块自己的引语**里取词，逐字命中由构造保证。

它替代的动作是「凭印象挑关键词」——占位符「（待补充）」不是答案，抽词才是。

用法：python3 scripts/build_block_keywords.py <书目录> [--dry]
"""
import glob
import os
import re
import sys

STOP = set("""the a an and or but if is are was were been being have has had do does did
not so too very can will just about after again all any because be both few more most
other our own same she him his her they them their this that these those to of in on at
for from with without within into onto over under above below up down out off then there
here when where why how what which who whom whose as than while during before since
would could should may might must shall i me my mine you your yours he it its we us
said says say saying tell told ask asked thought know knew wanted needed got get
""".split())


def tokens(s):
    return [w for w in re.findall(r"[A-Za-z][A-Za-z'’]*", s)]


def pick(quote):
    """从引语里取 2 个关键词：先取含长词的二字短语，再取最有内容的单词。"""
    words = tokens(quote)
    if not words:
        return []
    low = [w.lower() for w in words]
    # 候选：长度 >=5 且非停用词
    cand = [(w, len(w)) for w in words if len(w) >= 5 and w.lower() not in STOP]
    if not cand:
        cand = [(w, len(w)) for w in words if w.lower() not in STOP]
    if not cand:
        cand = [(w, len(w)) for w in words]

    seen, out = set(), []
    # 1) 含最长词的相邻 bigram（逐字短语，信息量高于单词）
    by_len = sorted(cand, key=lambda x: -x[1])
    for w, _ in by_len[:4]:
        i = next((k for k, x in enumerate(words) if x == w), None)
        if i is None:
            continue
        for j in (i - 1, i + 1):
            if 0 <= j < len(words) and words[j].lower() not in STOP and len(words[j]) >= 4:
                pair = f"{words[min(i, j)].lower()} {words[max(i, j)].lower()}"
                if pair.lower() in quote.lower() and pair not in seen:
                    seen.add(pair)
                    out.append(pair)
                    break
        if len(out) >= 2:
            break
    # 2) 补齐：按长度降序取未出现过的单词
    for w, _ in by_len:
        lw = w.lower()
        if lw not in seen:
            seen.add(lw)
            out.append(lw)
        if len(out) >= 2:
            break
    return out[:2]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    book = sys.argv[1]
    dry = '--dry' in sys.argv

    total = 0
    for md in sorted(glob.glob(os.path.join(book, 'ch*.md'))):
        s = open(md, encoding='utf-8').read()
        changed = 0
        out_lines = []
        blocks = re.split(r'(?=> \*\*原句 \d+:)', s)
        rebuilt = []
        for b in blocks:
            m = re.search(r'> \*\*原句 (\d+):\*\* ["“](.+?)["”]\s*$', b, re.M)
            if not m:
                rebuilt.append(b)
                continue
            quote = m.group(2)
            kws = pick(quote)
            if not kws:
                rebuilt.append(b)
                continue
            new_line = '**关键词**：' + ' / '.join(kws)
            ph = re.compile(r'\*\*关键词\*\*[：:]\s*（待补充）')
            if ph.search(b):
                b = ph.sub(new_line, b, count=1)
                changed += 1
            rebuilt.append(b)
        new_s = ''.join(rebuilt)
        if changed and not dry:
            open(md, 'w', encoding='utf-8').write(new_s)
        if changed:
            print(f"{'(dry) ' if dry else ''}{os.path.basename(md)}: {changed} 块")
        total += changed

    print(f"\n共生成关键词 {total} 块")


if __name__ == '__main__':
    main()
