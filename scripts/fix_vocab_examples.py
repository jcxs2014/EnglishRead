#!/usr/bin/env python3
"""校验每章词表例句是否逐字取自本章 text/；不命中则从本章原文替换（或删该行）。

用法: python3 scripts/fix_vocab_examples.py "<书目录>"
（写作期修复件；对应门禁 lane ② check_vocab 的「例句不命中本章」）
"""
import os, re, sys
if len(sys.argv) < 2:
    print('usage: fix_vocab_examples.py "<书目录>"'); sys.exit(2)
md_dir=sys.argv[1]
d=md_dir
def chapters():
    out={}
    for f in sorted(os.listdir(f'{d}/text')):
        m=re.match(r'ch(\d+)_', f)
        if m:
            out[int(m.group(1))]=open(f'{d}/text/{f}',encoding='utf-8').read()
    return out
CH=chapters()
def chap_of_md(fn):
    m=re.match(r'ch(\d+) ', fn)
    return int(m.group(1)) if m else None
report=[]
for fn in sorted(os.listdir(md_dir)):
    if not fn.endswith('.md'): continue
    n=chap_of_md(fn)
    if n is None or n not in CH: continue
    src=CH[n]
    p=os.path.join(md_dir,fn)
    t=open(p,encoding='utf-8').read()
    lines=t.split('\n')
    out=[]; changed=0
    for l in lines:
        if l.startswith('| ') and l.count('|')>=4:
            cells=[c.strip() for c in l.split('|')[1:-1]]
            if len(cells)==3 and cells[0] not in ('词/短语',''):
                word, gloss, ex = cells
                if word.endswith('?') or gloss.strip() in ('——','-'):
                    changed+=1
                    continue
                if ex and ex not in src and ex!='——':
                    # find a sentence in this chapter containing the word (case-insensitive)
                    sents=re.split(r'(?<=[.!?])\s+', src.replace('\n',' '))
                    cand=None
                    for s in sents:
                        if re.search(r'\b'+re.escape(word)+r'\b', s, re.I) and 20<len(s)<220:
                            cand=s.strip(); break
                    if cand:
                        cells[2]=cand; changed+=1
                    else:
                        # drop the row
                        changed+=1
                        continue
                    l='| '+' | '.join(cells)+' |'
        out.append(l)
    if changed:
        open(p,'w',encoding='utf-8').write('\n'.join(out))
        report.append((fn,changed))
for r in report: print(r)
