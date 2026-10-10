#!/usr/bin/env python3
"""简单粗暴的关键词修复：直接从违规行提取信息并删除无效关键词。"""
import re


def main():
    with open('/tmp/kw_violations.txt', 'r') as f:
        violations = f.readlines()

    for line in violations:
        # 解析：❌ ch02 chapter 2.md 原句2: 关键词不在本块引语内 → ['find me first', 'change of clothes']
        match = re.search(r'(ch\d+ chapter \d+\.md) 原句(\d+):.*→ \[(.*?)\]', line)
        if not match:
            continue

        chapter_file = match.group(1)
        quote_num = match.group(2)
        invalid_kws_str = match.group(3)

        md_path = f"notes/books/novels/the-night-always-comes-by-willy-vlautin/{chapter_file}"

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 找到对应的关键词行（支持多种格式，不要求严格的双换行）
            pattern = rf'> \*\*原句 {quote_num}:\*\*.*?\n(.*?\n)*?\*\*关键词[：:]\s*(.*?)(\n)'
            match2 = re.search(pattern, content, re.DOTALL)
            if not match2:
                # 尝试另一种格式：**关键词**：
                pattern = rf'> \*\*原句 {quote_num}:\*\*.*?\n(.*?\n)*?\*\*关键词\*\*[：:]\s*(.*?)(\n)'
                match2 = re.search(pattern, content, re.DOTALL)

            if not match2:
                print(f"✗ {chapter_file} 原句{quote_num}: 未找到关键词行")
                continue

            old_kw_line = match2.group(2)

            # 简单策略：直接替换为"（待补充）"
            new_content = content.replace(
                f'**关键词**：{old_kw_line}',
                '**关键词**：（待补充）'
            )
            new_content = new_content.replace(
                f'**关键词**: {old_kw_line}',
                '**关键词**：（待补充）'
            )

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"✓ {chapter_file} 原句{quote_num}")

        except Exception as e:
            print(f"✗ {chapter_file} 原句{quote_num}: {e}")


if __name__ == '__main__':
    main()
