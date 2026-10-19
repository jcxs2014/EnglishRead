#!/usr/bin/env python3
"""Maybe Next Time 情感节点归属逐条核验（一次性工具）。

对每个节点：检查其描述里提到的**全部事件指纹**在标注章与候选章的 text/ 里各命中几次。
判定：标注章应当命中**全部**指纹；候选章若命中更多 ⇒ 标注可能有误。
"""
import os
import re

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "novels", "maybe-next-time-by-cesca-major")
T = os.path.join(B, "text")

texts = {}
for x in os.listdir(T):
    m = re.match(r"ch(\d+)_", x)
    if m:
        texts[int(m.group(1))] = open(os.path.join(T, x), encoding="utf-8").read().lower()

# 节点 → (标注章, [事件指纹, ...])
NODES = [
    ("节点一", 2, ["hattie", "anniversary"]),
    ("节点二", 46, ["binge", "brighton", "nobu", "wanted to die"]),
    ("节点三", 48, ["ernestina", "jas", "gus", "audiobook", "quit"]),
    ("节点四", 49, ["today you are happy", "poppy", "school"]),
    ("节点五", 50, ["tiktok", "holly", "whatsapp", "gee"]),
    ("节点六", 55, ["you did this"]),
    ("节点七", 56, ["accepted wholeheartedly", "not hattie's fault"]),
    ("节点八", 57, ["you die", "tonight", "perfect"]),
    ("节点九", 58, ["i've loved my life"]),
    ("节点十", 59, ["alarm", "curtains", "turn over"]),
]
CAND = {
    "节点一": [1, 2, 3, 4],
    "节点二": [45, 46, 47],
    "节点三": [47, 48, 49],
    "节点四": [48, 49, 50],
    "节点五": [50, 51, 52, 53, 54],
    "节点六": [54, 55, 56],
    "节点七": [55, 56, 57],
    "节点八": [56, 57, 58],
    "节点九": [57, 58, 59],
    "节点十": [58, 59],
}

for name, ch, fps in NODES:
    cands = CAND[name]
    print(f"\n{name}（标注 ch{ch}）指纹 {fps}")
    for c in cands:
        t = texts.get(c, "")
        hits = [f for f in fps if f in t]
        mark = "  ← 标注章" if c == ch else ""
        print(f"   ch{c:02d}: {len(hits)}/{len(fps)} {hits}{mark}")
