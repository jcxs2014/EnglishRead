#!/usr/bin/env python3
"""00_情感节点.md 行内引语外移（AGENTS 第 9 条 d2）。

d2：三篇总览中任何英文原句**一律**写成独立成行的 `> "…"（chNN）` 引用块，
**禁止嵌在中文正文里**。本节 7 处的英文原句**下方已有独立引用块**，
故此处只是「段落里的行内重复」⇒ 直接从中文段落中移除（不动引用块）。

行级替换，原子落盘。
"""
import os
import tempfile

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
P = os.path.join(_ROOT, "notes", "books", "novels", "maybe-next-time-by-cesca-major",
                 "00_情感节点.md")

REPL = [
    # (原文行, 新行)
    ('**情感**：Emma binge watching、漫无目的的购物、Brighton 海边、Nobu 独酌、街头闹事被捕、闭门不出。'
     'Dan 每晚死在不同地点。Emma 产生自杀念头："I couldn\'t do this anymore."',
     '**情感**：Emma binge watching、漫无目的的购物、Brighton 海边、Nobu 独酌、街头闹事被捕、闭门不出。'
     'Dan 每晚死在不同地点。Emma 产生自杀念头（见下方引用）。'),
    ('**情感**：Emma 与 Dan 做爱（重新发现亲密）、送孩子上学（重新连接孩子）、警告 Poppy（防止霸凌）、'
     '读 Ernestina 的书稿（职业目的）、给 Jurek 妈妈送有声书（善良）。"Today you are happy."',
     '**情感**：Emma 与 Dan 做爱（重新发现亲密）、送孩子上学（重新连接孩子）、警告 Poppy（防止霸凌）、'
     '读 Ernestina 的书稿（职业目的）、给 Jurek 妈妈送有声书（善良）。'),
    ('**情感**：Emma 每晚回到事故现场， confrontation Hattie。Hattie 恳求 Emma 带她回家，Emma 拒绝："You did this."',
     '**情感**：Emma 每晚回到事故现场，confrontation Hattie。Hattie 恳求 Emma 带她回家，Emma 拒绝了。'),
    ('**情感**：Hattie 揭露 Ed 的情感虐待与流产。Emma 接纳 Hattie 住进家中，原谅了她。'
     '"And in that second I accepted wholeheartedly that it was not Hattie\'s fault. He always died."',
     '**情感**：Hattie 揭露 Ed 的情感虐待与流产。Emma 接纳 Hattie 住进家中，原谅了她。'),
    ('**情感**：Emma 告诉 Dan 循环真相："You die. Tonight. And there\'s nothing I can do to stop it." '
     'Dan 安静倾听，最终相信了 Emma。两人相拥而眠。"Today was perfect."',
     '**情感**：Emma 告诉 Dan 循环真相（见下方引用）。Dan 安静倾听，最终相信了 Emma。两人相拥而眠。'),
    ('**情感**：Dan 向 Emma、Poppy、Miles 告别，表达对生命的感激："I\'ve loved my life. I love my life." '
     'Dan 的信是他的 farewell，也是 Emma 循环的"意义"。',
     '**情感**：Dan 向 Emma、Poppy、Miles 告别，表达对生命的感激（见下方引用）。'
     'Dan 的信是他的 farewell，也是 Emma 循环的「意义」。'),
]

text = open(P, encoding="utf-8").read()
orig_lines = text.count("\n")
for old, new in REPL:
    n = text.count(old)
    if n != 1:
        print(f"❌ 命中 {n} 次（应为 1）：{old[:60]}")
        raise SystemExit(1)
    text = text.replace(old, new)
assert text.count("\n") == orig_lines, "行数变化"
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    f.write(text)
os.replace(tmp, P)
print(f"✅ 已外移 {len(REPL)} 处行内引语（引用块未动）")
