#!/usr/bin/env python3
"""lib.text — 文本归一化的**唯一实现**（2026-10-20）。

为什么要有它
------------
`norm()` / `strip_quotes()` / `split_segments()` 这套东西在库里有多个近似副本，
每份的引号处理、省略号切分都略有差异 —— 而**判定差异会直接变成假红或假绿**
（实测：md 用 `\u2018…\u2019`、原文用 `\u201c…\u201d`，只在一边去掉引号就会 6/6 全报"查无"）。

本模块只收**语义已确定**的四个原语，不涉任何判据：

- `norm()`          归一化到"只比字词"：弯/直引号统一去掉、空白压缩
- `strip_quotes()`  剥掉包在引语外面的一层引号（直/弯/直角都认）
- `split_segments()`按省略号拆段（`…` 与 `...`），保证中间段不丢
- `cjk_count()` / `cjk_ratio()` 中文字数与占比

先只有 `bookform.py` 一个消费者（**rule of three**：等到第二个真需要它的工具出现再迁，
不要为了"抽象"把口径不同的检查器硬并到一个 norm 上——那正是 93.5% 假红的来源）。
"""
from __future__ import annotations

import re

CJK = re.compile(r"[\u4e00-\u9fff]")

TRANS = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u00a0": " ",
    "\u2009": " ", "\u202f": " ", "\u200b": "",
})
ELLIPSIS = ("…", "...")

STOPWORDS = set("""
a an the and or but if of to in on at for with from by as is am are was were be been
being do does did done have has had having i me my we our you your he him his she her
it its they them their this that these those not no so than then there here what which
who whom whose when where why how all any both each few more most other some such only
own same too very can will just should now
""".split())


def norm(s: str) -> str:
    """归一化到「只比字词」：引号一律去掉（弯/直/单/双都是排版差异，不是文字差异）。"""
    s = s.translate(TRANS).replace("\n", " ")
    for ch in ('"', "'", "`"):
        s = s.replace(ch, "")
    return re.sub(r"\s+", " ", s).strip()


def cjk_count(s: str) -> int:
    return len(CJK.findall(s))


def cjk_ratio(s: str) -> float:
    body = re.sub(r"\s", "", s)
    return cjk_count(s) / len(body) if body else 0.0


def strip_quotes(s: str) -> str:
    s = s.strip()
    for lq, rq in (('"', '"'), ("'", "'"), ("「", "」"), ("『", "』")):
        if len(s) >= 2 and s.startswith(lq) and s.endswith(rq):
            return s[1:-1].strip()
    return s.strip('"“” ')


def split_segments(quote: str) -> list[str]:
    """按省略号拆段；返回原文顺序的片段（中间段不丢）。"""
    parts = [quote]
    for ell in ELLIPSIS:
        nxt = []
        for p in parts:
            nxt.extend(p.split(ell))
        parts = nxt
    out = []
    for p in parts:
        p = p.strip().strip(",;:.!?—- ")
        if p:
            out.append(p)
    return out

