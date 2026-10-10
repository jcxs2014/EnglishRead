#!/usr/bin/env python3
"""批量修复引语块超额问题。

策略：对超过 8 块的章节，保留前 8 个有完整分析子项的引语块，删除多余的。
"完整分析子项"定义为包含：中文理解 + 关键词 + 为什么这样写 + 读者视角提示

用法：python3 scripts/fix_quote_block_quota.py <书目录>
"""
import glob
import os
import re
import sys


def count_subitems(block_text):
    """统计引语块的分析子项数量。"""
    subitems = 0
    if '**中文理解**' in block_text or '**中文理解：**' in block_text:
        subitems += 1
    if '**关键词**' in block_text or '**关键词：**' in block_text:
        subitems += 1
    if '**为什么这样写**' in block_text or '**为什么这样写：**' in block_text:
        subitems += 1
    if '**读者视角提示**' in block_text or '**读者视角提示：**' in block_text:
        subitems += 1
    return subitems


def fix_chapter(md_path, max_blocks=8):
    """修复单章的引语块超额问题。"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 分割成引语块
    quote_pattern = r'(> \*\*原句 \d+:\*\*.*?)(?=> \*\*原句 \d+:\*\*|\n---\n|$)'
    blocks = re.findall(quote_pattern, content, re.DOTALL)

    if len(blocks) <= max_blocks:
        return 0  # 未超额

    # 为每个块计算子项数，排序
    block_info = []
    for i, block in enumerate(blocks):
        subitems = count_subitems(block)
        block_info.append((i, block, subitems))

    # 按子项数降序排序，保留前 max_blocks 个
    block_info.sort(key=lambda x: x[2], reverse=True)
    keep_indices = set(idx for idx, _, _ in block_info[:max_blocks])

    # 重建内容：只保留被选中的块
    all_matches = list(re.finditer(quote_pattern, content, re.DOTALL))
    new_content = content

    # 从后往前删除，避免索引偏移
    delete_count = 0
    for match_idx in range(len(all_matches) - 1, -1, -1):
        if match_idx not in keep_indices:
            match = all_matches[match_idx]
            new_content = new_content[:match.start()] + new_content[match.end():]
            delete_count += 1

    # 重新编号剩余的引语块
    def renumber(match):
        nonlocal renumber_counter
        renumber_counter += 1
        return match.group(0).replace(f'原句 {match.group(1)}:', f'原句 {renumber_counter}:', 1)

    renumber_counter = 0
    new_content = re.sub(r'> \*\*原句 (\d+):\*\*', renumber, new_content)

    if delete_count > 0:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return delete_count


def main():
    if len(sys.argv) < 2:
        print("用法: python3 fix_quote_block_quota.py <书目录>")
        sys.exit(1)

    book_dir = sys.argv[1]
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))

    total_deleted = 0
    for md_path in md_files:
        basename = os.path.basename(md_path)
        ch_num_match = re.match(r'ch(\d+)', basename)
        if ch_num_match:
            deleted = fix_chapter(md_path)
            if deleted > 0:
                total_deleted += deleted
                print(f"✓ {basename}: 删除 {deleted} 个引语块")

    print(f"\n共删除 {total_deleted} 个引语块")


if __name__ == '__main__':
    main()
