#!/usr/bin/env python3
"""Check which ①-⑩ quotes of given files hit the epub (like verify_quotes but per-file detail)."""
import re, zipfile, html, sys
EPUB = 'notes/books/short-story-anthologies/100 Great Short Stories by James Daley/library/100 Great Short Stories - James Daley.epub'
CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩'
def flat(s): return re.sub(r'[^a-z0-9]', '', s.lower())
def epub_flat():
    out = ''
    with zipfile.ZipFile(EPUB) as z:
        for n in z.namelist():
            if n.lower().endswith(('.html','.htm','.xhtml')):
                t = z.read(n).decode('utf-8','ignore')
                t = re.sub(r'<[^>]+>', ' ', t)
                t = html.unescape(t).replace('\u00a0',' ')
                out += t
    return flat(out)
def extract(txt):
    qs=[]; seen=set()
    for raw in txt.splitlines():
        s=raw.strip()
        m=(re.match(r'^['+CIRCLED+r']\s+(.+)$', s)
           or re.match(r'^\*{1,2}['+CIRCLED+r']\*{1,2}\s+[\"\'](.*)[\"\']', s)
           or re.match(r'^['+CIRCLED+r']\s+[\"\'](.*)[\"\']', s))
        if not m: continue
        b=m.group(1).strip().strip('*').strip('\'"“”‘’ ')
        if len(flat(b))>=20 and b not in seen:
            seen.add(b); qs.append(b)
    return qs
full=epub_flat()
for fn in sys.argv[1:]:
    txt=open(fn,encoding='utf-8').read()
    qs=extract(txt)
    print(f'\n=== {fn.split("/")[-1]} ({len(qs)} quotes) ===')
    for i,q in enumerate(qs,1):
        f=flat(q)[:52]
        print(f'  {"OK " if f in full else "MISS"} #{i}: {q[:72]}')
