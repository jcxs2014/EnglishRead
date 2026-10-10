#!/usr/bin/env python3
"""批量修复 ch10-ch22 的导航标题和词表占位。

用法：python3 scripts/batch_fix_nav_vocab.py <书目录>
"""
import glob
import os
import re
import sys


def fix_chapter(md_path):
    """为单章添加 ## 本章导航 标题并替换词表为占位行。"""
    with open(md_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    original = txt

    # 1. 添加 ## 本章导航 标题（如果已有粗体项但无标题）
    has_nav_title = re.search(r'^## (?:本章导航|概览|本篇导航|导航/概览|导航|视角笔记)[ \t]*$', txt, re.M)
    has_bold_items = re.search(r'^\*\*(一句话概括|情感弧线位置|Tropes 兑现/反转|人物弧线)\*\*:', txt, re.M)

    if not has_nav_title and has_bold_items:
        # 在第一个粗体项之前插入标题
        first_bold = re.search(r'^\*\*(一句话概括|情感弧线位置|Tropes 兑现/反转|人物弧线)\*\*:', txt, re.M)
        if first_bold:
            insert_pos = first_bold.start()
            txt = txt[:insert_pos] + "## 本章导航\n\n" + txt[insert_pos:]

    # 2. 替换列表格式词表为占位行
    vocab_section = re.search(r'^## (?:本章词汇|词汇分级)(.*?)(?=\n## |\Z)', txt, re.M | re.S)
    if vocab_section:
        vocab_txt = vocab_section.group(1)
        tiers = re.split(r'(?m)^### ', vocab_txt)[1:]

        for ti in tiers:
            tier_header = ti.splitlines()[0].strip()
            list_items = [x for x in ti.split('\n') if re.match(r'^- \*\*', x)]

            if list_items:
                # 找到该档位在原文中的起始和结束位置
                tier_start_in_vocab = vocab_txt.find(f'### {tier_header}')
                tier_end_in_vocab = vocab_txt.find('### ', tier_start_in_vocab + 5)
                if tier_end_in_vocab == -1:
                    tier_end_in_vocab = len(vocab_txt)

                # 构建占位内容
                placeholder = f"### {tier_header}\n\n（本章{tier_header.replace('⭐', '').replace(' ', '')}词条需从原文提取）\n"

                # 替换
                old_tier = vocab_txt[tier_start_in_vocab:tier_end_in_vocab]
                new_vocab_txt = vocab_txt.replace(old_tier, placeholder)
                txt = txt.replace(vocab_section.group(0), new_vocab_txt)

    if txt != original:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(txt)
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("用法: python3 batch_fix_nav_vocab.py <书目录>")
        sys.exit(1)

    book_dir = sys.argv[1]
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))

    fixed_count = 0
    for md_path in md_files:
        basename = os.path.basename(md_path)
        # 只处理 ch10-ch22
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
