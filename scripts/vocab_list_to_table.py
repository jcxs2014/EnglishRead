#!/usr/bin/env python3
"""把 chNN 的词表从列表格式转为门禁认可的表格格式，例句一律从**本章 text/** 逐字抽取。

它替代的动作是「手写词表」——词条先在本章语料里验存在，例句由程序从命中句截取，
因此例句不可能来自他章、也不可能自造。

用法：python3 scripts/vocab_list_to_table.py <书目录> <起始章> <结束章> [--dry]
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chapter_text_path import find_chapter_text

HEAD = re.compile(r'^- \*\*(.+?)\*\*\s*(?:/[^/]*/\s*)?(?:\*[a-zA-Z.]+\*)?\s*(.*)$')
TIERS = ('⭐⭐⭐', '⭐⭐', '⭐')


def gloss_from(raw):
    """从旧行的释义段取中文释义（剥掉词性标注与破折号后的注释）。"""
    g = re.sub(r'^\([a-z.]+\)\s*', '', raw.strip())
    g = re.split(r'\s+[—–-]\s+', g)[0]
    g = re.sub(r'\s*—\s*$', '', g).strip()
    return g


def example(sentences, headword):
    """返回第一个包含该词（词边界、忽略大小写）的原文句子，逐字。"""
    pat = re.compile(r"(?<![A-Za-z])" + re.escape(headword).replace(r"\ ", r"[\s-]+") + r"(?![A-Za-z])", re.I)
    for s in sentences:
        if pat.search(s):
            return s.strip()
    return None


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    book, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    dry = '--dry' in sys.argv

    # 空档补词：{ch: {tier_key: {headword: 释义}}}
    fills = {}
    fp = Path(__file__).with_name('vocab_fill_advanced.json')
    if fp.exists():
        fills = json.loads(fp.read_text(encoding='utf-8'))

    for ch in range(a, b + 1):
        mds = sorted(Path(book).glob(f'ch{ch:02d}*.md'))
        if not mds:
            continue
        md = mds[0]
        tp = find_chapter_text(book, str(ch))
        if not tp:
            print(f'⚠ ch{ch:02d}: 无 text，跳过')
            continue
        txt = Path(tp).read_text(encoding='utf-8')
        sents = re.split(r'(?<=[.!?])\s+', txt)

        s = md.read_text(encoding='utf-8')
        m = re.search(r'^## (?:本章词汇|词汇分级)\n(.*?)(?=\n## |\Z)', s, re.M | re.S)
        if not m:
            print(f'⚠ ch{ch:02d}: 无词汇节，跳过')
            continue

        body = m.group(1)
        parts = re.split(r'(?m)^### (.*?)\n', body)
        tier_heads = parts[1::2]
        tier_bodies = parts[2::2]

        new_blocks = []
        report = []
        for head, tb in zip(tier_heads, tier_bodies):
            rows = []
            for line in tb.split('\n'):
                hm = HEAD.match(line.strip())
                if hm:
                    w, g = hm.group(1).strip(), gloss_from(hm.group(2))
                    if g:
                        rows.append((w, g))
                    continue
                tm = re.match(r'^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
                if tm and tm.group(1).strip() not in ('词/短语',) \
                        and set(tm.group(1).strip()) - set('-: ') \
                        and '—' not in tm.group(2):
                    rows.append((tm.group(1).strip(), tm.group(2).strip()))
            key = 'advanced' if '⭐⭐⭐' in head else ('inter' if '⭐⭐' in head else 'basic')
            if not rows:
                for w, g in (fills.get(str(ch), {}) or {}).get(key, {}).items():
                    rows.append((w, g))
            kept = []
            for w, g in rows:
                ex = example(sents, w)
                if ex:
                    kept.append((w, g, ex))
                else:
                    report.append(f'    ✗ 本章语料查无，弃用词条「{w}」')
            # 档位偏薄时按 topup 表补足（候选同样先过本章语料）
            for w, g in (fills.get(str(ch), {}) or {}).get(key + '_topup', {}).items():
                if len(kept) >= 3:
                    break
                if any(k[0].lower() == w.lower() for k in kept):
                    continue
                ex = example(sents, w)
                if ex:
                    kept.append((w, g, ex))
                    report.append(f'    + 补词条「{w}」')
            table = f'### {head}\n\n| 词/短语 | 释义 | 原文例句 |\n|---------|------|----------|\n'
            for w, g, ex in kept:
                table += f'| {w} | {g} | {ex} |\n'
            if not kept:
                table += '\n（本章无该档词条）\n'
            new_blocks.append(table)

        new_body = '\n' + '\n'.join(new_blocks) + '\n'
        new_s = s[:m.start(1)] + new_body + s[m.end(1):]
        if new_s != s:
            if not dry:
                md.write_text(new_s, encoding='utf-8')
            print(f'✓ ch{ch:02d}' + ''.join(report))


if __name__ == '__main__':
    main()
