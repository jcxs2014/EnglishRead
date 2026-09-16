#!/usr/bin/env python3
"""
verify_strange_overview.py — 总览三篇全量英文片段 flat 比对（含工具口径外的行内引语与 blockquote）

背景：verify_overview_quotes.py 只吃「① 引语」等编号行；概述行内英文片段与
情感节点的 `> 引语` blockquote 不在其口径内（AGENTS.md 已列为盲区）。
本脚本把 00_*.md 里所有 >=20 flat 字符的英文连续片段抽出来，逐条对 epub
展平全文做 flat 比对，MISS 一律打印供人工复核。

用法：
  python3 scripts/attic/verify_strange_overview.py "<书目录>" "<epub>"
"""
import re, sys, os, glob, html, zipfile, tempfile, unicodedata

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚'


def flat(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())


def epub_flat(path):
    out = []
    with zipfile.ZipFile(path) as z, tempfile.TemporaryDirectory() as td:
        for n in z.namelist():
            if n.lower().endswith(('.html', '.htm', '.xhtml')):
                p = os.path.join(td, re.sub(r'[\\/]', '_', n))
                open(p, 'wb').write(z.read(n))
        for p in glob.glob(os.path.join(td, '*')):
            t = open(p, encoding='utf-8', errors='ignore').read()
            t = re.sub(r'<[^>]+>', ' ', t)
            out.append(html.unescape(t).replace('\u00a0', ' '))
    return flat(' '.join(out))


# 英文片段：连续英文/引号/破折号/撇号，且分词数 >= 3
FRAG = re.compile(r"[A-Za-z][A-Za-z0-9''\u2019\-,\u2014\.;:!\?\"\u201c\u201d ]{15,}")


def fragments(text):
    frags = []
    for raw in text.split('\n'):
        s = raw.strip()
        if s.startswith('#'):
            continue
        # 去掉粗体/斜体标记与行首引用符
        s = re.sub(r'^\s*>\s*', '', s)
        s = s.replace('**', '')
        for m in FRAG.finditer(s):
            f = m.group(0).strip(' -,;:')
            if len(flat(f)) >= 20 and len(f.split()) >= 3:
                frags.append(f)
    return frags


def main():
    book_dir, epub = sys.argv[1], sys.argv[2]
    full = epub_flat(epub)
    tot = miss = 0
    for f in sorted(glob.glob(os.path.join(book_dir, '00_*.md'))):
        name = os.path.basename(f)
        frags = fragments(open(f, encoding='utf-8').read())
        bad = []
        for q in frags:
            tot += 1
            if flat(q) not in full:
                bad.append(q)
        miss += len(bad)
        mark = '✅' if not bad else '❌'
        print(f'{name}: {len(frags) - len(bad)}/{len(frags)} 英文片段 flat 命中 {mark}')
        for b in bad:
            print(f'    ✗ {b[:96]}')
    print(f'\n=== 合计 {tot - miss}/{tot} 命中（MISS={miss}）===')
    sys.exit(1 if miss else 0)


if __name__ == '__main__':
    main()
