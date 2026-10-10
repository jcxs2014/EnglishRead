#!/usr/bin/env python3
"""列出各章 ⭐⭐⭐ 档候选词：本章出现、词长 >=8、全章频次低、非专名。

供人工写释义后交给 vocab_to_table.py 建表。
用法：python3 scripts/list_advanced_candidates.py <书目录> <起始章> <结束章> [--top N]
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chapter_text_path import find_chapter_text

COMMON = set("""because another enough suddenly completely absolutely incredible
restaurant apartment something everything anything nothing anybody somebody
themselves yesterday afternoon morning tonight outside inside together
""" .split())


def main():
    book, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    top = 8
    if '--top' in sys.argv:
        top = int(sys.argv[sys.argv.index('--top') + 1])
    for ch in range(a, b + 1):
        p = find_chapter_text(book, str(ch))
        if not p:
            print(f'ch{ch:02d}: 无 text')
            continue
        t = Path(p).read_text(encoding='utf-8')
        words = re.findall(r"\b[a-z][a-z']{7,}\b", t)          # 只在正文小写处出现 ⇒ 排除专名
        cnt = Counter(w.strip("'’") for w in words)
        rare = [(w, n) for w, n in cnt.items() if w not in COMMON and n <= 2 and len(w) >= 8]
        rare.sort(key=lambda x: (-len(x[0]), x[0]))
        print(f'ch{ch:02d}: ' + ', '.join(f'{w}({n})' for w, n in rare[:top]))


if __name__ == '__main__':
    main()
