#!/usr/bin/env python3
"""
extract_preaching_to_the_choir_text.py — 本书专用原文提取（关闭通用脚本的 dropcap 修连正则）

背景：
  scripts/extract_chapters.py 的 dropcap 修连正则
    \\b([A-Z])\\s+([A-Z][a-z]+|[A-Z]{2,})\\b
  会把正文中任何「单字母大写 + 空格 + 首字母大写单词」误拼成一个词：
    "A Kirk" → "AKirk"（ch05）、"T Bank" → "TBank"（ch03）。
  本书正文无真实首字母下沉（章节开头的 smallcaps span 覆盖整段开头短语，非单字母），
  因此关闭该正则。

另外通用脚本保留 <title> 正文（head 内），本书每个正文分册 <title> 一律是 "Chapter 1"
（元数据错误），会污染每章首行，故一并剥离 <head>。

正文结构：spine 中 01-01 … 01-08 = 书内 1. … 8.（TOC 标 Chapter 1–8）
输出：ch01_chapter_1.txt … ch08_chapter_8.txt
"""
import re, sys, html, os, zipfile, posixpath
from urllib.parse import unquote

SRC = "/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/preaching-to-the-choir-by-adrian-tchaikovsky/library/Preaching to the Choir (Adrian Tchaikovsky) (z-library.sk, 1lib.sk, z-lib.sk).epub"
OUT = "/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/preaching-to-the-choir-by-adrian-tchaikovsky/text"

BODY = [f"OEBPS/01-0{i}.xhtml" for i in range(1, 9)]


def clean(raw: str) -> str:
    raw = re.sub(r"<head\b.*?</head>", "", raw, flags=re.S | re.I)
    t = re.sub(r"<(p|div|h[1-6]|li|br)\b[^>]*>", "\n", raw)
    t = re.sub(r"</(p|div|h[1-6])>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = t.replace("\u00a0", " ")
    lines = []
    for l in t.split("\n"):
        l = l.strip()
        if not l:
            lines.append("")
        elif lines and lines[-1] and not l[0].isupper() and not re.match(r"^[\u201c\u201d'\"(\\-—*\\d]", l):
            lines[-1] += " " + l
        else:
            lines.append(l)
    return "\n".join(lines).strip()


def main():
    z = zipfile.ZipFile(SRC)
    os.makedirs(OUT, exist_ok=True)
    for i, path in enumerate(BODY, start=1):
        text = clean(z.read(path).decode("utf-8", "ignore"))
        target = f"{OUT}/ch{i:02d}_chapter_{i}.txt"
        open(target, "w").write(text + "\n")
        print(f"ch{i:02d}_chapter_{i}.txt  {len(re.sub(r'[ \t\n]', '', text))} 字符  {path}")


if __name__ == "__main__":
    main()
