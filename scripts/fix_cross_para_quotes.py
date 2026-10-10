#!/usr/bin/env python3
"""批量修复引语跨自然段拼接问题。

策略：对含 … 的引语块，只保留第一个片段（删除 … 及之后的所有内容）。
这样既符合"单自然段"规则，又保留核心内容。

用法：python3 scripts/fix_cross_para_quotes.py <书目录>
"""
import glob
import os
import re
import sys


def fix_chapter(md_path):
    """修复单章中所有跨段拼接的引语块。"""
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_lines = lines[:]
    fixed_count = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        # 匹配引语行：> **原句 N:** "..."
        quote_match = re.match(r'^> \*\*原句 (\d+):\*\* "(.*)"$', line.strip())
        if quote_match:
            quote_num = quote_match.group(1)
            quote_text = quote_match.group(2)

            # 检查是否含 …
            if '…' in quote_text:
                # 只保留第一个片段
                parts = quote_text.split('…')
                first_part = parts[0].strip()

                # 确保第一个片段以句号结尾（如果不是完整句子则保持原样）
                if not first_part.endswith(('.', '!', '?', '"')):
                    # 找到最后一个完整的句子
                    last_period = first_part.rfind('.')
                    if last_period != -1:
                        first_part = first_part[:last_period + 1]

                # 重建引语行
                new_quote_line = f'> **原句 {quote_num}:** "{first_part}"\n'
                lines[i] = new_quote_line
                fixed_count += 1

        i += 1

    if fixed_count > 0:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    return fixed_count


def main():
    if len(sys.argv) < 2:
        print("用法: python3 fix_cross_para_quotes.py <书目录>")
        sys.exit(1)

    book_dir = sys.argv[1]
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))

    total_fixed = 0
    for md_path in md_files:
        basename = os.path.basename(md_path)
        ch_num_match = re.match(r'ch(\d+)', basename)
        if ch_num_match:
            fixed = fix_chapter(md_path)
            if fixed > 0:
                total_fixed += fixed
                print(f"✓ {basename}: 修复 {fixed} 处")

    print(f"\n共修复 {total_fixed} 处跨段拼接")


if __name__ == '__main__':
    main()
