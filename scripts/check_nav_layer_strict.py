#!/usr/bin/env python3
"""导航层/总结层引语逐章归属核对——check_nav_layer 的补强实现。

**为什么需要它**：`check_nav_layer` 只报「导航/总结层有没有英文」，
`sweep_analysis_inline` / `sweep_full` / `strict_quote_check` 都不扫这两层。
于是「导航层写了别章的句子」或「凭空写出两句像引语的英文」全都能溜过去——
**实测抓到 ch17 两句虚构引语**（`Shifting from a different angle` /
`Masking my surprise`，epub 全文 0 命中），四道门禁同时放过。

本脚本抽出 `## 本章导航` 与 `## 一句话总结` 两节里的**反引号片段**，
逐条到本章 `text/` 做 flat 比对（去标点、大小写、变音符）。

用法：python3 check_nav_layer_strict.py <书目录>
退出码：0 = 全部命中本章；2 = 有片段不属本章（或查无）
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
    total = 0
    bad = []
    for md in files:
        ch = os.path.basename(md)[:4]
        texts = glob.glob(os.path.join(book, "text", f"{ch}*.txt"))
        if not texts:
            continue
        tf = flat(open(texts[0], encoding="utf-8").read())
        body = open(md, encoding="utf-8").read()
        for sec in ("本章导航", "一句话总结"):
            m = re.search(r"## " + sec + r"(.*?)(?=\n## |\Z)", body, re.S)
            if not m:
                continue
            for seg in re.findall(r"`([^`]+)`", m.group(1)):
                total += 1
                sf = flat(seg)
                if sf not in tf:
                    bad.append((os.path.basename(md), sec, seg))

    for name, sec, seg in bad:
        print(f"❌ {name} [{sec}] 「{seg[:110]}」")
    print(f"=== 导航/总结层反引号片段: {total - len(bad)}/{total} 命中本章 text ===")
    if bad:
        print("⚠️ 有片段不属本章——逐条人工判：跨章搬句 / 虚构 / 合法省略")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())