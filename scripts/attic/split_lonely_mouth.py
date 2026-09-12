#!/usr/bin/env python3
"""一次性脚本：Lonely Mouth (Jacqueline Maley) epub 拆分提取。

epub 物理上只有 3 个正章 XHTML（出版方把整书装进 3 个文件）：
  Chapter01 = Barbara: Goulburn, 2002（9.7K 字符）
  Chapter02 = Matilda: Sydney, 2019（544K 字符，内部 118 个 `* * *` 场景分隔）
  Chapter03 = Matilda: Paris, 2022（4.4K 字符）

处理策略（Butcher of the Forest 先例：无章节号按 `* * *` 场景分隔分章）：
  ch01 = Part 1 全部；ch02-ch20 = Part 2 的 119 个场景按 ~26-38K 字符
  机械分组（贪心：累积到 ≥26K 即切单元）；ch21 = Part 3 全部。
"""
import html
import os
import re
import sys

EPUB_XHTML_DIR = sys.argv[1]  # 解压后的 OEBPS/text 目录
OUT_DIR = sys.argv[2]         # 输出 text/ 目录

os.makedirs(OUT_DIR, exist_ok=True)


def html_to_paragraphs(path):
    raw = open(path).read()
    paras = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.S)
    out = []
    for p in paras:
        t = html.unescape(re.sub(r'<[^>]+>', '', p)).strip()
        if t:
            out.append(t)
    return out


def write_unit(nn, slug, paras):
    assert paras and paras[0], f'ch{nn} empty'
    text = '\n\n'.join(paras)
    dest = os.path.join(OUT_DIR, f'ch{nn:02d}_{slug}.txt')
    with open(dest, 'w') as f:
        f.write(text)
    print(f'ch{nn:02d}_{slug}.txt  {len(text):>7d} 字符  首段: {paras[0][:60]!r}')


# Part 1: Barbara（ch01，整部件）
write_unit(1, 'barbara_goulburn_2002',
           html_to_paragraphs(os.path.join(EPUB_XHTML_DIR, '9781460712917_Chapter01.xhtml')))

# Part 2: Sydney（ch02-ch20，119 场景按贪心 26K 阈值分组）
paras = html_to_paragraphs(os.path.join(EPUB_XHTML_DIR, '9781460712917_Chapter02.xhtml'))
scenes, cur = [], []
for t in paras:
    if re.fullmatch(r'[\*\s]+', t):  # `* * *` 场景分隔（原文形态 *\xa0*\xa0*）
        if cur:
            scenes.append(cur)
            cur = []
    else:
        cur.append(t)
if cur:
    scenes.append(cur)
assert len(scenes) == 119, f'场景数异常: {len(scenes)}'

ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
         'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix']
nn = 2
unit, ucum = [], 0
for i, sc in enumerate(scenes):
    unit.append(sc)
    ucum += sum(len(t) for t in sc)
    if ucum >= 26000 or i == len(scenes) - 1:
        idx = ROMAN[nn - 2]
        write_unit(nn, f'matilda_sydney_2019_{idx}', [t for sc in unit for t in sc])
        nn += 1
        unit, ucum = [], 0
assert nn - 2 == 19, f'Sydney 单元数异常: {nn - 2}'

# Part 3: Paris（ch21，整部件）
write_unit(21, 'matilda_paris_2022',
           html_to_paragraphs(os.path.join(EPUB_XHTML_DIR, '9781460712917_Chapter03.xhtml')))
print(f'\n共 ch01-ch21 21 件')
