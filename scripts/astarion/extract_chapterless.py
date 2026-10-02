#!/usr/bin/env python3
"""无章节标记 epub 的分段提取（PRH house style）。

背景：Astarion 这类 epub 把整本正文塞进**一个** XHTML，正文内没有任何
h1/h2/h3，也没有 "Chapter N" 字符串，NCX 的 toc 只有前后面��条目 + 一条
"Baldur's Gate 3: Astarion"（= 整本正文当一条）。唯一的结构信号是
`<hr class="transition"/>` 场景分隔符，它有两种形态：

  · ORN  —— 后面跟 `<div class="para-orn"><img class="height_3em">`（装饰花饰）
  · DASH —— 后面跟 `<div class="transition">—</div>`（破折号）

两种形态与段落 class 严格一一对应（实测 para-paft == ORN 数、para-sp +
para-paft-alt == DASH 数），故可当作出版方自己的两级结构信号。

本脚本按「ORN = 章节边界；章节内超过 --max-chars 时再用 DASH 补切」分段，
并把前后面页按 SKIP 规则另存为 xx_* （不占 ch 编号）。

用法:
  python3 extract_chapterless.py <book_dir> [--max-chars 25000] [--dry-run]
"""
import argparse
import html
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

OPF = "{http://www.idpf.org/2007/opf}"
HR = re.compile(r'<hr class="transition"/>')
ORN = re.compile(r'para-orn')
DASH = re.compile(r'class="transition">—</div>')
# 两种分隔符的整块标记（切片起点落在 hr 上时会残留，须整块剥掉）。
# ⚠️ 属性顺序是 `<div aria-hidden="true" class="transition">`，写成
# `<div class="transition">` 会一条都匹配不到（第一版即如此，静默失效）。
DASHMARK = re.compile(r'<div[^>]*class="transition"[^>]*>—</div>')
ORNBLOK = re.compile(r'<div aria-hidden="true">\s*<div class="para-orn">.*?</div>\s*</div>',
                     re.S)
PAGEBREAK = re.compile(r'<span epub:type="pagebreak"[^>]*/>')
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")

# 出版方 SKIP 表：这些不是正文
SKIP = (
    "acknowledg", "about", "contents", "copyright", "title", "dedication",
    "toc", "nav", "praise", "cover", "epigraph", "foreword", "intro",
    "also_by", "also-by", "next-reads", "dictionary", "promotional",
    "index_", "halftitle", "series", "testimonial", "warning", "map",
    "appendix",
)


def clean(fragment: str) -> str:
    """剥标签 + 归一空白。禁手打引语时以此为真值来源。

    ⚠️ **保留段落边界**（`</p>` → 空行），不把全文压成一行：
    AGENTS 8.4 要求「读原文一律 shell sed/grep」，单行文件既没法按段读、
    也没法用 grep -n 定位。压成一行是自己方便、门禁不方便。

    ⚠️ DASH 分隔符的 `—` 是**独立 div**（`class="transition">—</div>`），
    不属于任何段落。切片起点落在 hr 上时会把它带进正文，使首句变成
    "— It was a lovely evening..."。原文里那一句本身不以破折号开头
    （实测：`<div…>—</div><p class="para-sp">It was a lovely evening…`），
    故须剥掉，否则 text/ 与 epub 逐字比对时每章首句都对不上。
    """
    fragment = PAGEBREAK.sub("", fragment)
    fragment = DASHMARK.sub("", fragment)     # 独立破折号 div
    fragment = ORNBLOK.sub("", fragment)      # 装饰花饰 div（含 <img>）
    fragment = re.sub(r"</p>", "\n\n", fragment)
    # ⚠️ 实体解码必须在剥标签**之后**。剥之前不动，`&amp;` 会被 TAG 切碎
    # 成 "&" + "amp;" 两个孤立字符；剥之后再 unescape 才安全。
    # 不解码的后果实测：`Helm & Cloak` 落成 `Helm &amp; Cloak`，任何含 & 的
    # 引语在 verify_quotes（对 epub 比对，epub 里是真 `&`）必然 MISS。
    fragment = TAG.sub("", fragment)
    fragment = html.unescape(fragment)
    fragment = fragment.replace("\xa0", " ")
    # ⚠️ 只归一**横向**空白。`\s` 含 \n，用它会把上一步刚插入的段落边界
    # 全部压掉（第一版即如此：全文塌成一行）。
    fragment = re.sub(r"[^\S\n]+", " ", fragment)
    fragment = re.sub(r" *\n *", "\n", fragment)
    fragment = re.sub(r"\n{3,}", "\n\n", fragment)
    fragment = re.sub(r"^—\s*", "", fragment.strip())
    return fragment.strip()


def read_epub(path: str):
    z = zipfile.ZipFile(path)
    opf_name = next(n for n in z.namelist() if n.endswith(".opf"))
    opf = ET.fromstring(z.read(opf_name).decode("utf-8", "replace"))
    base = os.path.dirname(opf_name)
    manifest = {i.get("id"): i.get("href") for i in opf.iter(OPF + "item")}
    spine = [manifest[it.get("idref")] for it in
             opf.find(".//" + OPF + "spine").findall(OPF + "itemref")]
    return z, base, spine


def pick_body(z, base, spine):
    """正文 = spine 里最长的非 boilerplate 件（不按文件名猜，见坑字典）。"""
    best = None
    for href in spine:
        low = href.lower()
        if any(k in low for k in SKIP):
            continue
        raw = z.read(os.path.join(base, href)).decode("utf-8", "replace")
        size = len(clean(raw))
        if best is None or size > best[0]:
            best = (size, href, raw)
    if best is None:
        sys.exit("正文件未找到：spine 全部命中 SKIP")
    return best[1], best[2]


def body_start(raw: str) -> int:
    """正文起点。正文首个 <p 带 dropcap class；兜底取第一个 <p。

    ⚠️ 必须用同一处起点做「整本 vs 拼接」对账——`clean(raw)` 若从文件头算起，
    会把 <head> 里的 <title>（"Baldur's Gate 3: Astarion, Baldur's Gate 3:
    Astarion"，53 字符）算进整本，两边天然不等，判据自身出错。
    """
    start = raw.find('<p class="para-pf-supb-pg')
    return start if start >= 0 else raw.find("<p")


def slice_body(raw: str, max_chars: int):
    """返回 [(起点, 终点, 分级)]，分级 ∈ {start, ORN, DASH}。"""
    start = body_start(raw)
    marks = []
    for m in HR.finditer(raw):
        tail = raw[m.start():m.start() + 260]
        marks.append((m.start(), "ORN" if ORN.search(tail) else "DASH"))

    cuts = [(start, "start")]
    cursor = start
    for pos, kind in marks:
        if kind == "ORN":
            cuts.append((pos, kind))
            cursor = pos
        elif len(clean(raw[cursor:pos])) >= max_chars:
            cuts.append((pos, kind))
            cursor = pos
    cuts.append((len(raw), "end"))
    return [(cuts[i][0], cuts[i + 1][0], cuts[i][1])
            for i in range(len(cuts) - 1)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_dir")
    ap.add_argument("--max-chars", type=int, default=25000)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    lib = os.path.join(args.book_dir, "library")
    epubs = [f for f in os.listdir(lib) if f.lower().endswith(".epub")]
    if not epubs:
        sys.exit("library/ 下没有 epub")
    z, base, spine = read_epub(os.path.join(lib, epubs[0]))
    href, raw = pick_body(z, base, spine)
    print(f"正文件: {href}  ({len(raw)} B raw)")

    segs = slice_body(raw, args.max_chars)
    print(f"章节数: {len(segs)}  (max-chars={args.max_chars})")
    for i, (a, b, kind) in enumerate(segs, 1):
        head = clean(raw[a:b])[:70]
        print(f"  ch{i:02d} {len(clean(raw[a:b])):6d} [{kind:5s}] {head}")

    if args.dry_run:
        return

    out = os.path.join(args.book_dir, "text")
    os.makedirs(out, exist_ok=True)
    for i, (a, b, _kind) in enumerate(segs, 1):
        head = clean(raw[a:b]).split(". ")[0][:40].rstrip(".")
        # text/ 用**下划线**分词（AGENTS：`_` 只在精读 md 里禁用，text/ 提取件
        # 恰恰规定用 `_`）。生产工具 build_vocab_table / build_vocab_section 的
        # glob 是 `ch<NN>_*.txt`，写成空格会命中 0 件、静默 SystemExit。
        slug = re.sub(r"[^a-z0-9]+", "_", head.lower()).strip("_")[:38]
        name = f"ch{i:02d}_{slug}.txt"
        with open(os.path.join(out, name), "w", encoding="utf-8") as fh:
            fh.write(clean(raw[a:b]) + "\n")
    print(f"text/ 落盘完成：{len(segs)} 件（前后面页按用户指令不保留）")


if __name__ == "__main__":
    main()