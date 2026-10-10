#!/usr/bin/env python3
"""批量修复 ch10-ch22 缺失的 ## 词汇分级 标题。

用法：python3 scripts/fix_missing_vocab_header.py <书目录>
"""
import glob
import os
import re
import sys


def fix_chapter(md_path):
    """为单章添加缺失的 ## 词汇分级 标题。"""
    with open(md_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    original = txt

    # 检查是否有 ### ⭐ 档位但无 ## 词汇分级 或 ## 本章词汇 标题
    has_tier = re.search(r'^### ⭐', txt, re.M)
    has_vocab_header = re.search(r'^## (?:本章词汇|词汇分级)', txt, re.M)

    if has_tier and not has_vocab_header:
        # 在第一个 ### ⭐ 之前插入 ## 词汇分级
        first_tier = re.search(r'^### ⭐', txt, re.M)
        if first_tier:
            insert_pos = first_tier.start()
            # 找到前面的 --- 分隔线
            prev_sep = txt.rfind('---', 0, insert_pos)
            if prev_sep != -1:
                # 在 --- 之后、第一个档位之前插入
                after_sep = txt.find('\n', prev_sep) + 1
                txt = txt[:after_sep] + '\n## 词汇分级\n' + txt[after_sep:]

    if txt != original:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(txt)
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("用法: python3 fix_missing_vocab_header.py <书目录>")
        sys.exit(1)

    book_dir = sys.argv[1]
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))

    fixed_count = 0
    for md_path in md_files:
        basename = os.path.basename(md_path)
        ch_num_match = re.match(r'ch(\d+)', basename)
        if ch_num_match:
            ch_num = int(ch_num_match.group(1))
            if 10 <= ch_num <= 22:
                if fix_chapter(md_path):
                    fixed_count += 1
                    print(f"✓ {basename}")

    print(f"\n共修复 {fixed_count} 章")


if __name__ == '__main__':
    main()
