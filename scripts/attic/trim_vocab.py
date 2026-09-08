#!/usr/bin/env python3
"""Trim vocabulary tables in Wolf Hour chapters to ~25 entries per chapter."""
import re
import sys
from pathlib import Path

BOOK_DIR = Path("notes/books/mystery-thriller/wolf-hour-by-jo-nesbo")
TARGETS = {
    1: (8, 10, 7),   # ch01: 25 total
    2: (8, 10, 7),   # ch02: 25 total
    3: (8, 10, 7),   # ch03: 25 total
    4: (8, 10, 7),   # ch04: 25 total
    5: (8, 10, 7),   # ch05: 25 total
    6: (8, 10, 7),   # ch06: 25 total
    7: (8, 10, 7),   # ch07: 25 total
    8: (8, 10, 7),   # ch08: 25 total
    9: (8, 10, 7),   # ch09: 25 total
    10: (8, 10, 7),  # ch10: 25 total
    11: (8, 10, 7),  # ch11: 25 total
    12: (8, 10, 7),  # ch12: 25 total
    13: (8, 10, 7),  # ch13: 25 total
    14: (8, 10, 7),  # ch14: 25 total
    15: (8, 10, 7),  # ch15: 25 total
    16: (8, 10, 7),  # ch16: 25 total
    17: (8, 10, 7),  # ch17: 25 total
    18: (8, 10, 7),  # ch18: 25 total
    19: (8, 10, 7),  # ch19: 25 total
    20: (8, 10, 7),  # ch20: 25 total
    21: (8, 10, 7),  # ch21: 25 total
    22: (8, 10, 7),  # ch22: 25 total
    23: (8, 10, 7),  # ch23: 25 total
    24: (8, 10, 7),  # ch24: 25 total
    25: (8, 10, 7),  # ch25: 25 total
    26: (8, 10, 7),  # ch26: 25 total
    27: (8, 10, 7),  # ch27: 25 total
    28: (8, 10, 7),  # ch28: 25 total
    29: (8, 10, 7),  # ch29: 25 total
    30: (8, 10, 7),  # ch30: 25 total
}

def trim_file(ch_num, star3_max, star2_max, star1_max):
    fpath = BOOK_DIR / f"ch{ch_num:02d} *.md"
    files = list(BOOK_DIR.glob(f"ch{ch_num:02d} *.md"))
    if not files:
        print(f"  ch{ch_num:02d}: NOT FOUND")
        return
    
    fpath = files[0]
    content = fpath.read_text(encoding='utf-8')
    
    # Find vocab section
    lines = content.split('\n')
    vocab_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('## 本章词汇'):
            vocab_start = i
            break
    
    if vocab_start is None:
        print(f"  ch{ch_num:02d}: NO VOCAB SECTION")
        return
    
    # Find section boundaries
    sections = {}
    current_section = None
    for i in range(vocab_start, len(lines)):
        line = lines[i].strip()
        if line.startswith('### ⭐⭐⭐'):
            current_section = 'star3'
            sections[current_section] = {'start': i, 'lines': []}
        elif line.startswith('### ⭐⭐'):
            current_section = 'star2'
            sections[current_section] = {'start': i, 'lines': []}
        elif line.startswith('### ⭐'):
            current_section = 'star1'
            sections[current_section] = {'start': i, 'lines': []}
        elif line.startswith('## ') and current_section:
            break
        elif current_section and line.startswith('|') and not line.startswith('|---'):
            sections[current_section]['lines'].append(i)
    
    # Build new vocab section
    new_lines = lines[:vocab_start]
    new_lines.append('')
    new_lines.append('## 本章词汇')
    new_lines.append('')
    
    maxes = {'star3': star3_max, 'star2': star2_max, 'star1': star1_max}
    
    for section in ['star3', 'star2', 'star1']:
        if section not in sections:
            continue
        new_lines.append(f'### {"⭐" * (3 if section == "star3" else 2 if section == "star2" else 1)} {"高级" if section == "star3" else "进阶" if section == "star2" else "基础"}')
        new_lines.append('')
        new_lines.append('| 词/短语 | 释义 | 例句 |')
        new_lines.append('|---------|------|------|')
        for idx in sections[section]['lines'][:maxes[section]]:
            new_lines.append(lines[idx])
        new_lines.append('')
    
    # Append everything after the vocab section
    # Find where vocab section ends
    vocab_end = len(lines)
    for i in range(vocab_start + 1, len(lines)):
        if lines[i].strip().startswith('## ') and '本章词汇' not in lines[i]:
            vocab_end = i
            break
    
    new_lines.extend(lines[vocab_end:])
    
    new_content = '\n'.join(new_lines)
    fpath.write_text(new_content, encoding='utf-8')
    print(f"  ch{ch_num:02d}: trimmed to ~{star3_max+star2_max+star1_max} entries")

def main():
    for ch_num, (s3, s2, s1) in sorted(TARGETS.items()):
        trim_file(ch_num, s3, s2, s1)

if __name__ == '__main__':
    main()
