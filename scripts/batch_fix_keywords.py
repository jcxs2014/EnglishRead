#!/usr/bin/env python3
"""批量修复关键词不在引语内的问题。

用法：从 gate.sh 输出解析违规数据，自动删除无效关键词。
python3 scripts/batch_fix_keywords.py <书目录>
"""
import glob
import os
import re
import subprocess
import sys


def get_violations(book_dir):
    """从 gate.sh 输出提取关键词违规数据。"""
    result = subprocess.run(
        ['bash', 'scripts/gate.sh', book_dir],
        capture_output=True, text=True, cwd='/Users/jcxs2014/Documents/Works/EnglishRead'
    )

    violations = []
    for line in result.stdout.split('\n'):
        match = re.search(r'(ch\d+ chapter \d+\.md) 原句(\d+): 关键词不在本块引语内 → \[(.*?)\]', line)
        if match:
            chapter = match.group(1)
            quote_num = int(match.group(2))
            keywords = [k.strip().strip("'") for k in match.group(3).split(',')]
            violations.append((chapter, quote_num, keywords))

    return violations


def fix_keywords(md_path, quote_num, invalid_keywords):
    """删除指定引语块中的无效关键词。"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 找到对应的引语块
    pattern = rf'(> \*\*原句 {quote_num}:\*\*.*?)(?=> \*\*原句 \d+:\*\*|\n---\n|$)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return False

    block = match.group(1)

    # 找到关键词行
    kw_match = re.search(r'(\*\*关键词[：:]\*\*[：:]?\s*)(.*)', block)
    if not kw_match:
        return False

    kw_line = kw_match.group(2)
    original_kw = kw_line

    # 分割关键词（支持 / · 、 等分隔符）
    separators = r'[／/·、]'
    keywords = [k.strip() for k in re.split(separators, kw_line)]

    # 获取引语文本
    quote_match = re.search(r'> \*\*原句 \d+:\*\* "(.*?)"', block)
    if not quote_match:
        return False

    quote_text = quote_match.group(1).lower()

    # 过滤掉不在引语内的关键词
    valid_keywords = []
    removed_keywords = []
    for kw in keywords:
        if kw.lower() in quote_text:
            valid_keywords.append(kw)
        else:
            removed_keywords.append(kw)

    if not removed_keywords:
        return False  # 没有需要删除的

    # 重建关键词行
    new_kw_line = ' / '.join(valid_keywords) if valid_keywords else '（待补充）'
    new_block = block.replace(original_kw, new_kw_line)
    new_content = content.replace(block, new_block)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    if len(sys.argv) < 2:
        print("用法: python3 batch_fix_keywords.py <书目录>")
        sys.exit(1)

    book_dir = sys.argv[1]
    violations = get_violations(book_dir)

    if not violations:
        print("未发现关键词违规")
        return

    fixed_count = 0
    for chapter, quote_num, invalid_kws in violations:
        md_path = os.path.join(book_dir, chapter)
        if os.path.exists(md_path):
            if fix_keywords(md_path, quote_num, invalid_kws):
                fixed_count += 1
                print(f"✓ {chapter} 原句{quote_num}: 删除 {invalid_kws}")

    print(f"\n共修复 {fixed_count}/{len(violations)} 处")


if __name__ == '__main__':
    main()
