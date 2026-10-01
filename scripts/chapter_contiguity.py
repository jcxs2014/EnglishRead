#!/usr/bin/env python3
"""b 步专用：引语「分段连续性」独立实现（换检查路径用）。

**为什么需要它**：`verify_quotes` / `check_chapter_quotes` / `sweep_full`
都走 52 字符指纹或 flat 口径。指纹有个已知盲区——**恰好跨过接缝**：
引语里悄悄跳过中间一整句而不加省略号，指纹仍能在原文里匹配到前后两段，
于是六道门禁同时放过（Lottery of Secrets ch38 即此型，2026-10-01 实证）。

**判据**：把每条引语按句末标点切成片段。合法形态只有两种——
  ① 整串连续命中本章 text；
  ② 含 `…` 或 `...` ⇒ 每一段各自连续命中（AGENTS 禁令 5：省略号两侧都必须是原词）。
**没有省略号却缺片段** = 静默漏句 ⇒ 报。

用法：python3 scripts/chapter_contiguity.py <书目录>
退出码：0 = 无静默漏句；2 = 有
"""
import glob
import os
import re
import sys
import unicodedata


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFC", s).lower())


def main() -> int:
    book = sys.argv[1]
    files = sorted(
        p for p in glob.glob(os.path.join(book, "ch*.md"))
        if not os.path.basename(p).startswith("00_")
    )
    total = cont = omitted = bad = 0
    for md in files:
        ch = os.path.basename(md)[:4]
        hits = sorted(glob.glob(os.path.join(book, "text", f"{ch}*.txt")))
        if not hits:
            continue
        tf = flat(open(hits[0], encoding="utf-8").read())
        body = open(md, encoding="utf-8").read()
        for q in re.findall(r"^> \*\*原句 \d+:\*\* (.+)$", body, re.M):
            q = q.strip()
            if len(q) >= 2 and q[0] in "\"“" and q[-1] in "\"”":
                q = q[1:-1]
            total += 1
            if flat(q) in tf:
                cont += 1
                continue
            if "…" in q or "..." in q:
                omitted += 1
                frags = [flat(p) for p in re.split(r"…|\.\.\.", q)]
                miss = [p for p in frags if p and p not in tf]
                if miss:
                    bad += 1
                    print(f"❌ {os.path.basename(md)} 省略片段查无: {miss[0][:70]}")
                continue
            # 无省略号却整串不命中 → 按句末切，找缺哪几段
            frags = [flat(p) for p in re.split(r"(?<=[.!?])\s+", q) if flat(p)]
            miss = [p for p in frags if p not in tf]
            if miss:
                bad += 1
                print(f"❌ {os.path.basename(md)} 无省略号却缺 {len(miss)}/{len(frags)} 段")
                print(f"   首缺: {miss[0][:80]}")
            else:
                bad += 1
                print(f"❌ {os.path.basename(md)} 整串不命中但分段全在（疑跨标签拼接）")

    print(f"=== 分段连续性：整串连续 {cont} ｜ 含省略号 {omitted} ｜ 合计 {total} ｜"
          f" 静默漏句/拼接 {bad} ===")
    if bad:
        print("⚠️ 逐条人工判：真漏句 / 跨标签拼接 / 假红")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())