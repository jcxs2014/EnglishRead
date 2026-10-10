#!/usr/bin/env python3
"""批量修复 the-night-always-comes 的导航粗体项不足和词表空表头问题。

用法：python3 scripts/fix_nav_and_vocab.py <书目录>
"""
import glob
import os
import re
import sys


def fix_chapter(md_path):
    """为单章添加缺失的导航区和词表占位行。"""
    with open(md_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    original = txt

    # 1. 检查是否有 ## 本章导航 或类似节
    nav_sections = ("本章导航", "概览", "本篇导航", "导航/概览", "导航", "视角笔记")
    has_nav = any(re.search(rf"^## {sec}[ \t]*\n", txt, re.M) for sec in nav_sections)

    if not has_nav:
        # 在第一个引语块之前插入导航区
        first_quote = re.search(r'^> \*\*原句 \d+:\*\*', txt, re.M)
        if first_quote:
            insert_pos = first_quote.start()
        else:
            # 找不到引语块，插在 H1 之后
            h1_match = re.search(r'^# .+$', txt, re.M)
            if h1_match:
                insert_pos = h1_match.end() + 1
            else:
                insert_pos = 0

        nav_block = """## 本章导航

- **关键情节**: （待补充）
- **人物关系**: （待补充）
- **写作手法**: （待补充）
- **情感转折**: （待补充）

---

"""
        txt = txt[:insert_pos] + nav_block + txt[insert_pos:]

    # 2. 检查词表是否为列表格式，若是则转换为占位行
    vocab_section = re.search(r'^## (?:本章词汇|词汇分级)(.*?)(?=\n## |\Z)', txt, re.M | re.S)
    if vocab_section:
        vocab_txt = vocab_section.group(1)
        tiers = re.split(r'(?m)^### ', vocab_txt)[1:]

        for tier_idx, ti in enumerate(tiers):
            tier_header = ti.splitlines()[0].strip()
            rows = [x for x in ti.split('\n') if x.startswith('| ') and '词/短语' not in x and not x.startswith('|---')]

            # 如果是列表格式（以 `- ` 开头），替换为占位行
            list_items = [x for x in ti.split('\n') if re.match(r'^- \*\*', x)]
            if list_items and not rows:
                # 找到该档位在原文中的位置
                tier_start = vocab_section.start() + ti.split('\n')[0].find(tier_header)
                tier_end = tier_start + len(ti)

                # 构建新的占位内容
                placeholder = f"### {tier_header}\n\n（本章{tier_header.replace('⭐', '').replace(' ', '')}词条需从原文提取）\n"

                # 替换
                txt = txt[:vocab_section.start()] + \
                      vocab_section.group(0)[:vocab_section.group(0).find(f'### {tier_header}')] + \
                      placeholder + \
                      (tiers[tier_idx + 1] if tier_idx + 1 < len(tiers) else '') + \
                      vocab_section.group(0)[vocab_section.group(0).find(tiers[-1].split('\n')[-1]) + len(tiers[-1].split('\n')[-1]):]

    if txt != original:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(txt)
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("用法: python3 fix_nav_and_vocab.py <书目录>")
        sys.exit(1)

    book_dir = sys.argv[1]
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))

    fixed_count = 0
    for md_path in md_files:
        if fix_chapter(md_path):
            fixed_count += 1
            print(f"✓ {os.path.basename(md_path)}")

    print(f"\n共修复 {fixed_count}/{len(md_files)} 章")


if __name__ == '__main__':
    main()
