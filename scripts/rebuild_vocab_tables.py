#!/usr/bin/env python3
"""按「词条先验、例句抽取」重建 chNN 词表三档表格。

候选顺序：词表原词条（须在本章语料命中）→ 补词表 fills → 补档 topup。
例句从**本章 text/** 逐字取，取包含该词的**最短一句**，内部空白折成单空格，
因此不会出现跨自然段的例句（那会破坏 markdown 表格）。

用法：python3 scripts/rebuild_vocab_tables.py <书目录> <起始章> <结束章> [--dry]
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chapter_text_path import find_chapter_text

TIER_KEY = (('⭐⭐⭐', 'advanced'), ('⭐⭐', 'inter'), ('⭐', 'basic'))


def tier_key(head):
    for mark, key in TIER_KEY:
        if head.strip().startswith(mark):
            return key
    return 'basic'


def sentences(text):
    out = []
    for para in re.split(r'\n\s*\n', text):
        for s in re.split(r'(?<=[.!?])\s+', para):
            s = re.sub(r'\s+', ' ', s).strip()
            if len(s) > 20:
                out.append(s)
    return out


def example(sents, headword):
    pat = re.compile(r"(?<![A-Za-z])" + re.escape(headword).replace(r'\ ', r'[\s\-‑]+') + r"(?![A-Za-z])", re.I)
    hit = [s for s in sents if pat.search(s)]
    if not hit:
        return None
    return min(hit, key=len)


def main():
    book, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    dry = '--dry' in sys.argv
    base = json.loads(Path(__file__).with_name('vocab_base.json').read_text(encoding='utf-8'))
    fills = json.loads(Path(__file__).with_name('vocab_fill_advanced.json').read_text(encoding='utf-8'))

    for ch in range(a, b + 1):
        mds = sorted(Path(book).glob(f'ch{ch:02d}*.md'))
        if not mds:
            continue
        md, txt_p = mds[0], find_chapter_text(book, str(ch))
        sents = sentences(Path(txt_p).read_text(encoding='utf-8'))
        s = md.read_text(encoding='utf-8')
        m = re.search(r'^## (?:本章词汇|词汇分级)\n(.*?)(?=\n## |\Z)', s, re.M | re.S)
        if not m:
            print(f'⚠ ch{ch:02d}: 无词汇节')
            continue

        heads = re.findall(r'(?m)^### (.*)$', m.group(1))
        parts = re.split(r'(?m)^### .*?\n', m.group(1))
        old_bodies = parts[1:]

        blocks, notes = [], []
        for i, head in enumerate(heads):
            key = tier_key(head)
            order = {}
            order.update(base.get(str(ch), {}).get(key, {}))
            order.update(fills.get(str(ch), {}).get(key, {}))
            rows = []
            for w, g in order.items():
                ex = example(sents, w)
                if ex:
                    rows.append((w, g, ex))
                else:
                    notes.append(f'✗「{w}」本章查无')
            if len(rows) < 3:
                for w, g in fills.get(str(ch), {}).get(key + '_topup', {}).items():
                    if len(rows) >= 3:
                        break
                    if w in [r[0] for r in rows]:
                        continue
                    ex = example(sents, w)
                    if ex:
                        rows.append((w, g, ex))
                        notes.append(f'+补「{w}」')
            rows = rows[:3]
            # 已有的中文说明档保持不覆盖
            if not rows and old_bodies[i] and '（本章' in old_bodies[i]:
                rows = []
            table = f'### {head}\n\n| 词/短语 | 释义 | 原文例句 |\n|---------|------|----------|\n'
            table += ''.join(f'| {w} | {g} | {ex} |\n' for w, g, ex in rows)
            if not rows:
                table += '\n（本章无该档词条）\n'
            blocks.append(table)

        new_body = '\n' + '\n'.join(blocks) + '\n'
        new_s = s[:m.start(1)] + new_body + s[m.end(1):]
        if new_s != s and not dry:
            md.write_text(new_s, encoding='utf-8')
        print(f'✓ ch{ch:02d} ' + ' '.join(notes))


if __name__ == '__main__':
    main()
