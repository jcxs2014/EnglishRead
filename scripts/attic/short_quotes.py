#!/usr/bin/env python3
"""
short_quotes.py — 短引语人工兜底核对（复刻 verify_quotes 的抽取逻辑，一次性脚本）

verify_quotes 对 <20 flat 字符的引语**静默跳过只计数**（本书 11 条）。
本脚本复刻其抽取与剥离逻辑，逐条列出并用**原文层正则**核对是否真在当章。
用法：python3 scripts/attic/short_quotes.py "<书目录>"
"""
import glob
import os
import re
import sys
import unicodedata

BOOK = sys.argv[1]
CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚'
flat_alpha = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())

corp = {}
for f in glob.glob(os.path.join(BOOK, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    t = open(f, encoding='utf-8').read()
    for a, b in {'\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"'}.items():
        t = t.replace(a, b)
    corp[nn] = t

TOKEN = re.compile(r"[A-Za-z0-9'\u00c0-\u024f]+(?:-[A-Za-z0-9'\u00c0-\u024f]+)*")
tot = ok = 0
# ch*.md + 总览三篇（工具统计短引语时同样扫 00_*.md）
files = sorted(glob.glob(os.path.join(BOOK, 'ch*.md')),
               key=lambda p: int(re.match(r'ch(\d+)', os.path.basename(p)).group(1)))
files += sorted(glob.glob(os.path.join(BOOK, '00_*.md')))
for path in files:
    m0 = re.match(r'ch(\d+)', os.path.basename(path))
    nn = int(m0.group(1)) if m0 else 0
    for raw in open(path, encoding='utf-8'):
        s = raw.strip()
        m = (re.match(r'^[' + CIRCLED + r']\s+(.+)$', s)
             or re.match(r'^\*{1,2}[' + CIRCLED + r']\*{1,2}\s+["\'](.*)["\']', s)
             or re.match(r'^[' + CIRCLED + r']\s+["\'](.*)["\']', s)
             or re.match(r'^>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s+(.+)$', s)
             or re.match(r'^>\s*["\u201c](.+)$', s))
        if not m:
            continue
        body = m.group(1).strip()
        if body and not body.rstrip().endswith(('"', '"', "'", "'")):
            m2 = re.match(r'^["\u201c](.*?)[""”]\s*(?:[A-Za-z—].{0,60})?$', body)
            if not m2:
                m2 = re.match(r'^(.*?)[""”]\s*(?:[A-Za-z—].{0,60})?$', body)
            if m2:
                body = m2.group(1)
        body = body.strip('*').strip('\'"“”‘’ ')
        fa = len(flat_alpha(body))
        if not (5 <= fa < 20):
            continue
        tot += 1
        toks = TOKEN.findall(body)
        rx = r'\W+'.join(re.escape(t) for t in toks) if len(toks) > 1 else None
        hay = corp.get(nn) or ''.join(corp.values())
        hit = bool(rx and re.search(rx, hay))
        ok += hit
        print(f"  {'✅' if hit else '❌'} {'ch%02d' % nn if nn else '00_*  '}  [{fa:2d} flat]  {body[:66]}")
print(f"\n工具口径短引语 {tot} 条，原文层核对命中 {ok} 条（{ok}/{tot}）")
print('SHORT_QUOTES ' + ('PASS' if ok == tot else 'FAIL'))
sys.exit(0 if ok == tot else 1)
