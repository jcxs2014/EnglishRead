#!/usr/bin/env python3
"""Maybe Next Time 总览章号归属交叉核对（一次性工具）。

问题：建书简报（scripts/make_zh_briefs.py）的章节规划与实际 epub 章节序号**错位**
（简报 ch50「the tiktok day」= TikTok 章，但实际 TikTok 在 ch53）⇒
文件名 slug 与总览的 chNN 标注沿用了错位的规划。

本脚本对每个总览节点：
  ① 取该节点描述里的英文实词（专名/关键词）作指纹；
  ② 逐章统计指纹命中数；
  ③ 报告**标注章**与**命中最高的章**是否一致。
"""
import os
import re
from collections import Counter

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "novels", "maybe-next-time-by-cesca-major")

# 英文实词（专名/专有物）作指纹
FINGER = {
    "节点一": ["loop", "Abilene"],
    "节点二": ["despair", "overcast", "Nobu"],
    "节点三": ["gift", "Ealing", "Gumtree"],
    "节点四": ["gift", "anniversary", "ring"],
    "节点五": ["TikTok", "Holly", "WhatsApp", "Gee"],
    "节点六": ["Hattie", "revelation"],
    "节点七": ["forgiveness", "Dover"],
    "节点八": ["perfect", "creperie"],
    "节点九": ["last letter", "revelation"],
    "节点十": ["loop", "curtains"],
}

# 章 → text
texts = {}
tdir = os.path.join(B, "text")
for x in os.listdir(tdir):
    m = re.match(r"ch(\d+)_", x)
    if m:
        texts[int(m.group(1))] = open(os.path.join(tdir, x), encoding="utf-8").read()

# 情感节点 → 标注章
node_ch = {}
for line in open(os.path.join(B, "00_情感节点.md"), encoding="utf-8"):
    m = re.match(r"^###\s*(节点[一二三四五六七八九十]+)[：:].*?（ch(\d+)）", line)
    if m:
        node_ch[m.group(1)] = int(m.group(2))

print(f"{'节点':<8}{'标注章':<8}{'指纹命中分布（章:次数）':<46}判定")
print("-" * 100)
for node, ch in node_ch.items():
    fps = FINGER.get(node, [])
    cnt = Counter()
    for cn, t in texts.items():
        n = sum(1 for f in fps if f.lower() in t.lower())
        if n:
            cnt[cn] = n
    top = cnt.most_common(3)
    best = top[0][0] if top else -1
    bestn = top[0][1] if top else 0
    mark = "✅" if best == ch else ("⚠️ 不符" if best > 0 else "❓ 无命中")
    print(f"{node:<8}ch{ch:<6}{str(top):<46}{mark} (最高 ch{best} 命中 {bestn}/{len(fps)})")
