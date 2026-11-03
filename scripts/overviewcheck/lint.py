#!/usr/bin/env python3
"""总览三篇的**轻量体检**——补 19 lane 结构上查不到的三件事。

为什么要有这一层
----------------
2026-11-03 核 23 本完工书时，机器层 23/23 全绿，人读仍看见两类问题：

1. `00_概述.md` 写成「几天后，几天后，畅销作家…」——重复短语，语义没变但句子坏了；
2. `00_金句精选.md` 有 30 条引语、**一条「为什么重要 / 呼应关系」子项都没有**——
   它不是引语错，是**条目格式整个缺**，`verify_overview_quotes` 只核引语，看不见。

这两类都不进任何 lane：⑭ 只核引语逐字、⑮ 只核整串与章号标签、⑲ 只管章节文件。
⇒ 总览的中文散文与条目结构是「零门禁区」。

判据（三条，全部可机判）
------------------------
A. 金句子项：条目数 ≥5 时，含「为什么/呼应/上下文/中文理解」的条目占比
   = 0 → **阻断**（整篇没有子项，读者拿不到任何解释）；< 0.8 → 提示。
B. 重复短语：`X，X` / `X、X` 且 X 为 2–6 个汉字 → 提示（修辞性重复有白名单）。
C. 行内引语：不以 `>` 开头的行里出现 `"…"` 且含 ≥25 个字母 → 提示
   （按 `d2` 硬规定，总览英文原句必须独立成行引用块，行内等于放弃门禁）。

退出码：0 无阻断；1 有阻断；2 无法判定（没有总览文件且体裁要求有）。
"""
from __future__ import annotations

import re
import sys

from .names import find_overviews, required_count

RHETORIC = {"更多", "很多", "我们", "噪声", "一切", "一下", "慢慢", "渐渐", "真的", "已经"}
DUP_RE = re.compile(r"([\u4e00-\u9fa5]{2,6})[，、]\1")
SUB_KEYS = ("为什么", "呼应", "上下文", "中文理解", "为什么重要", "上下文与出处")
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
INLINE_RE = re.compile(r'[""“‘][^""“”\n]{20,}[""”’]')


def _entries(text: str) -> list[str]:
    """按圈码行首 / `### ` 标题切条目。"""
    lines = text.split("\n")
    idx = []
    for i, ln in enumerate(lines):
        core = ln.lstrip("#").strip()
        if core and core[0] in CIRC:
            idx.append(i)
    if not idx:
        return []
    out = []
    for k, i in enumerate(idx):
        end = idx[k + 1] if k + 1 < len(idx) else len(lines)
        out.append("\n".join(lines[i:end]))
    return out


def lint_file(path: str) -> tuple[list[str], list[str]]:
    text = open(path, encoding="utf-8").read()
    blocked: list[str] = []
    warns: list[str] = []
    name = path.split("/")[-1]

    if "金句" in name or "quote" in name.lower():
        ents = _entries(text)
        if len(ents) >= 5:
            hit = sum(1 for e in ents if any(k in e for k in SUB_KEYS))
            ratio = hit / len(ents)
            if ratio == 0:
                blocked.append(f"{name}：{len(ents)} 条金句，**一条解释子项都没有**（为什么重要/呼应关系/中文理解全缺）")
            elif ratio < 0.8:
                warns.append(f"{name}：{len(ents)} 条金句里只有 {hit} 条带子项（{ratio:.0%}）")

    for m in DUP_RE.finditer(text):
        if m.group(1) in RHETORIC:
            continue
        s = max(0, m.start() - 20)
        warns.append(f"{name}：重复短语「{m.group(0)}」… {text[s:m.end() + 15].replace(chr(10), ' ')}")

    inline = []
    for ln in text.split("\n"):
        if ln.lstrip().startswith(">"):
            continue
        for m in INLINE_RE.finditer(ln):
            if sum(ch.isascii() and ch.isalpha() for ch in m.group(0)) >= 25:
                inline.append(ln)
                break
    if inline:
        warns.append(f"{name}：{len(inline)} 行带行内英文引语（按 d2 须独立成引用块），例：{inline[0][:60]}")
    return blocked, warns


def main(book: str) -> int:
    files = find_overviews(book)
    if not files:
        need = required_count(book)
        print(f"❓ 无总览文件；体裁要求 {need if need is not None else '?'} 篇")
        return 0 if need in (0, None) else 2
    blocked: list[str] = []
    warns: list[str] = []
    for p in files:
        b, w = lint_file(p)
        blocked += b
        warns += w
    for x in blocked:
        print(f"❌ {x}")
    for x in warns:
        print(f"⚠️  {x}")
    print(f"总览轻量体检：{len(files)} 篇 · 阻断 {len(blocked)} · 提示 {len(warns)}")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ""))
