#!/usr/bin/env python3
"""
chapref_check.py — 总览里「呼应第 N 章…那句 "X"」型跨章引用的落地核对
  只在同一行内、且**章号出现在引语之前**时才判定（这才是"引用"的语法）
  判定：被引句 flat 必须命中**书内第 N 章**的 text/
用法：python3 scripts/attic/chapref_check.py "<书目录>"
"""
import re, os, sys, glob, unicodedata

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
book = sys.argv[1]

text_of = {}
for f in glob.glob(os.path.join(book, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    text_of[nn - 1] = flat(open(f, encoding='utf-8').read())

REF = re.compile(r'第\s*(\d+)\s*章')
Q = re.compile(r'[""“]([^""”\n]{20,})[""”]')

bad = total = 0
for fn in ('00_概述.md', '00_金句精选.md', '00_情感节点.md'):
    p = os.path.join(book, fn)
    if not os.path.exists(p):
        continue
    for i, line in enumerate(open(p, encoding='utf-8'), 1):
        for qm in Q.finditer(line):
            q = qm.group(1)
            if sum(1 for c in q if 'a' <= c.lower() <= 'z') < 25:
                continue
            # 该引语之前最近的章号引用
            refs = list(REF.finditer(line[:qm.start()]))
            if not refs:
                continue
            ref_ch = int(refs[-1].group(1))
            total += 1
            fq = flat(q)
            if fq not in text_of.get(ref_ch, ''):
                hits = sorted(n for n, c in text_of.items() if fq in c)
                print(f"  ✗ {fn}:L{i}  引用 第 {ref_ch} 章 与引语不符；实际命中书内章 {hits}")
                print(f"      引语: {q[:72]}")
                bad += 1
print(f"\n跨章引用共 {total} 处，不符 {bad} 处")
print('CHAPREF_CHECK ' + ('PASS' if bad == 0 else 'FAIL'))
sys.exit(1 if bad else 0)
