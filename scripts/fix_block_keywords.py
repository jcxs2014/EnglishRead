#!/usr/bin/env python3
"""把每块的「关键词」对齐到本块引语内：不在块内的词项换成引语中的连续短语。

用法: python3 scripts/fix_block_keywords.py "<章 md>" [...]
（写作期修复件；不改动引语正文，只改 **关键词** 行）
"""
import re, sys

def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’',"'").replace('“','"').replace('”','"')).strip().lower()

def pick_from_quote(q, n=3):
    """pick a contiguous phrase from the quote: 3-6 words, starting at a word boundary"""
    # remove outer quotes and leading dialogue quote
    s = q.strip().strip('"')
    s = re.sub(r'^[“"]', '', s)
    words = s.split()
    best = None
    for start in range(0, min(len(words), 14)):
        for size in (5, 4, 6, 3):
            if start+size <= len(words):
                cand = ' '.join(words[start:start+size])
                cand = cand.strip(' ,.;:!?"“”')
                if len(cand.split()) >= 3 and not cand[0].islower():
                    best = cand
                    break
        if best: break
    return best

def fix(path):
    t = open(path, encoding='utf-8').read()
    # split into blocks
    parts = re.split(r'(> \*\*原句 \d+:\*\* )', t)
    head = parts[0]
    chunks = [parts[i]+parts[i+1] for i in range(1, len(parts), 2)]
    changed = 0
    for ci,c in enumerate(chunks):
        mq = re.search(r'> \*\*原句 \d+:\*\* "(.*?)"', c, re.S)
        mk = re.search(r'\*\*关键词\*\*：(.*?)\n', c, re.S)
        if not (mq and mk): continue
        quote = mq.group(1)
        nq = norm(quote)
        items = [x.strip() for x in mk.group(1).split('/')]
        new_items = []
        for it in items:
            if norm(it) in nq:
                new_items.append(it)
            else:
                repl = pick_from_quote(quote)
                if repl and norm(repl) in nq:
                    new_items.append(repl); changed += 1
                else:
                    new_items.append(it)
        if new_items != items:
            c = c.replace('**关键词**：'+mk.group(1), '**关键词**：'+' / '.join(new_items))
            chunks[ci] = c
    out = head + ''.join(chunks)
    open(path,'w',encoding='utf-8').write(out)
    return changed

if len(sys.argv) < 2:
    print('usage: fix_block_keywords.py "<章 md>" [...]'); sys.exit(2)
for p in sys.argv[1:]:
    print(p, 'replaced', fix(p))
