#!/usr/bin/env python3
"""取料器：把某章的每个引语块连同 text/ 原文上下文 + 现有四字段一起打印出来。

用途：为「把分析层改写成中文」提供**原文先行**的素材（AGENTS 第 1 条：
精读任何篇章前必须先把该章原文放入上下文，禁止凭记忆引用原句）。

用法：
    python3 dump_ctx.py "<书目录>" ch21
    python3 dump_ctx.py "<书目录>" ch21 --full     # 整章原文
"""
import glob
import os
import re
import sys

book = sys.argv[1]
target = sys.argv[2]
full = "--full" in sys.argv

md_path = None
for p in sorted(glob.glob(os.path.join(book, "ch*.md"))):
    if os.path.basename(p).startswith(target + " ") or os.path.basename(p).startswith(target):
        md_path = p
        break
if not md_path:
    sys.exit("找不到 md：" + target)

txt = open(md_path, encoding="utf-8").read()
print(f"########## {os.path.basename(md_path)} ##########")

# ---- 导航层 + 一句话总结原文 ----
def section(text, anchor):
    m = re.search(r"(?m)^#{2,4}[ \t]*" + anchor + r"[ \t]*$", text)
    if not m:
        return ""
    rest = text[m.end():].split("\n", 1)
    body = rest[1] if len(rest) > 1 else ""
    nxt = re.search(r"(?m)^(?:#{2,4}[ \t]+|\*\*[^*]+\*\*[ \t]*$)", body)
    return body[:nxt.start()] if nxt else body

print("===== [导航层] =====")
print(section(txt, "本章导航").strip())
print("===== [一句话总结] =====")
print(section(txt, "一句话总结").strip())

# ---- 对应 text/ 提取件 ----
cands = [p for p in sorted(glob.glob(os.path.join(book, "text", "ch*.txt")))
         if os.path.basename(p).startswith(target + "_")]
if not cands:
    cands = [p for p in sorted(glob.glob(os.path.join(book, "text", "ch*.txt")))
             if os.path.basename(p).startswith(target)]
corpus = "\n".join(open(p, encoding="utf-8").read() for p in cands)
print(f"===== [text 提取件] {' + '.join(os.path.basename(c) for c in cands)} "
      f"({len(corpus)} 字符) =====")
if full:
    print(corpus)

# ---- 引语块 + 原文上下文 ----
BLOCK = re.compile(r"^> \*\*原句 (\d+):\*\*\s*(.*)$", re.M)
ms = list(BLOCK.finditer(txt))
def _flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


corpus_flat = _flat(corpus)


def locate(q):
    """在原文里找引语首 40 个 flat 字符的位置（用于取上下文）。"""
    fq = _flat(q)
    if len(fq) < 8:
        return None
    return corpus_flat.find(fq[:40])


for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(txt)
    body = txt[m.end():end]
    print(f"\n----- 原句 {m.group(1)} -----")
    print(f"QUOTE: {m.group(2)}")
    for line in body.split("\n"):
        s = line.strip()
        if s.startswith("- **"):
            print("  " + s)
    if not full:
        pos = locate(m.group(2))
        if pos is None:
            print("  [原文定位失败——该引语可能在 text/ 中被截断或改写]")
        else:
            print("  ---- 原文上下文 ----")
            print("  " + corpus[max(0, pos - 400):pos + 900].replace("\n", "\n  "))
