#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""总览层引语的两项核对：**逐字** + **（chNN）章号标注归属**。

补两个既有门禁的结构性盲区（2026-10-01 五步审查在 only-a-monster-by-vanessa-len 上实测）：

  1. `verify_overview_quotes.py` 的解析器只收裸 `> "…"`／`N "…"` 形态，
     对 `> {引语}（chNN）`（总览模板 gen_overview.py 的产出形态）**0 提取**。
     实测：该书概述 35 条 + 情感节点 27 条 = 62 条无人核。
  2. `check_overview_full.py` 的 B 项「章节标签核对」在本书报「对 0」＝**0 判定**；
     `verify_overview_quotes.py` 只验引语内容、**不验 `（chNN）` 章号标注**。
     实测：金句精选 25 条内容全 ✅，但把 ① 的 `（ch01）` 改成 `（ch05）` 它照样 25/25。
     ⚠️ 章号标错比凭空造词更常见也更危险——引语是真的，只是指错了出处。

用法：
  python3 scripts/check_overview_labels.py "<书目录>" ["<epub>"]
    epub 可省略——按 `library/*.epub` 自动取第一个；没有则退到 `text/` 逐章拼接
    （与 verify_overview_quotes 同一套降级优先级，见其 :125-140）。

比对端**必须复用 `verify_quotes.flat_alpha()` / `epub_flat_text()`**（NFKD + 先剥
`\\n`/`\\t`；剥标签 + `html.unescape`）。自写展平口径会出假红——本会话两次假红
分别来自漏 NFKD 与漏 `html.unescape`（见 .memory/reviews/ 同类教训）。

判据三档（每一段都单独查，按 `…` / `. . .` 切段）：
  ✅ 标注章逐字     —— 每一段都落在标注的那一章里
  ⚠️ 标注与实章不符 —— 段段都在书里，但不在标注章（阻断型候选）
  ❌ 全书查无       —— 至少一段查无（阻断型候选）

退出码：0 = 无 ⚠️/❌；1 = 有 ⚠️ 或 ❌；2 = 目录里没有 00*.md 或既无 epub 也无 text/（不是通过）。

⚠️ 已知边界（用前必读）：
  - 只核**引语行**。总览里的**中文散文断言**（人物身份/关系/结局/场景顺序）本工具
    完全看不见——那是 d/e 步人工核对的对象，本书已因此查出 15 条阻断型。
  - 中文引号里的**中文台词**不在任何英文引语门禁覆盖范围内（本工具同样不收）。
  - 章号归属只做「标注章 ∈ 实际命中章」的粗判；一条引语跨两章都命中时，会被判
    ⚠️，需人判是不是正常的跨章引语。
"""
import argparse
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import flat_alpha, epub_flat_text  # noqa: E402
from chapter_text_path import find_chapter_text  # noqa: E402

LABEL = re.compile(r"（\s*ch\s*(\d{1,3})\s*）\s*$")
SEG = re.compile(r"\s*(?:…|\.\s\.\s\.)\s*")
NUM = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚"
# 行首序号：①…㉚ 全部圈码，或 `12.` / `12)` / `12、`（NFKD 会把圈码归一成数字
# 留在指纹头部，**每条必然查无**——ticket-to-mars 全红、the-coral-bones 5 条即此因）
# ⚠️ 2026-10-01 修正（The Death of Us 批实测，全库假红）：本行原为
# `r"^(?:\s*(?:%s|\d+\s*[.、)])\s*)+"`，**圈码没有字符类方括号**——于是
# `(?:①②③…㉚|\d+…)` 被编译成「**三个字的字面串**」而不是「任一圈码」，
# 行首序号**永远剥不掉**；随后 flat_alpha 的 NFKD 把 `①` 归一成 `1` 留在
# 指纹头部 ⇒ 每一条都必然「全书查无」。
# 实测全库 292 本：修复前 ❌1429 / ✅45；修复后 ❌0 / ✅1400+。
# 对照：同文件 `LINE_B`（下一行）本就写了 `[%s]`，本行是漏写。
# 判据（#2012）：正则形态一动就跑全库逐条行为对照，不只比总数。
LEAD_NUM = re.compile(r"^(?:\s*(?:[%s]|\d+\s*[.、)])\s*)+" % NUM)
CJK = re.compile(r"[一-鿿]")
# 形态 A（概述/情感节点）：`> {Q}（chNN）`
# 形态 B（金句精选）：`① {Q}（chNN）` 主条 + 呼应关系里的 `- {Q}（chNN）`
LINE_B = re.compile(r"^\s*(?:[-*]\s+|[%s]\s+)(.+?)$" % NUM)
OVERVIEWS = ("00_概述.md", "00_情感节点.md", "00_金句精选.md")
MIN_SEG = 8  # 短于此的片段不做 flat 查找（否则单字母/短词必然误报）


def parse_quotes(md_path):
    """解析带 `（chNN）` 标签的引语行，去掉尾部标签、行内 `{Q:c:s}` 标记与行首序号。

    **只收带标签的行**，这是本工具的职责边界（核 chNN 标注归属）。不带标签的裸引语
    由 `verify_overview_quotes.py` 负责——两层不重叠。

    ⚠️ 序言：行首的 `①`/`1.` 必须在 flat 之前剥掉，否则 `flat_alpha` 的 NFKD 会把
    `①` 归一成 `1` 留在指纹头部，**每一条都必然查无**（ticket-to-mars 全红实证）。
    """
    is_jinju = os.path.basename(md_path) == "00_金句精选.md"
    out = []
    skipped = 0
    with io.open(md_path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            body = None
            if not is_jinju:
                if not line.startswith("> "):
                    continue
                body = line[2:].strip()
            else:
                m = LINE_B.match(line.rstrip("\n"))
                if not m:
                    continue
                body = m.group(1).strip()
            body = LEAD_NUM.sub("", body)
            m = LABEL.search(body)
            if not m:
                # 金句精选的呼应关系里还有纯中文引导句（`- ch07 那条构成提问与反问——…`）；
                # 其他篇目的无标签行属于别的总览模板，不归本工具管。
                skipped += 1
                continue
            body = body[:m.start()].strip()
            body = re.sub(r"\{[^}]*\}", "", body).strip()
            if not body or not re.search(r"[A-Za-z]", body):
                continue
            if CJK.search(body):
                # 形如 `「…」是同一个论证的两次投放；与 “…” , said Kyr, （ch1）`——
                # 这是**中文分析 bullet 恰好以（chNN）收尾**，不是引语行。
                # （some-desperate-glory 00_金句精选.md:119 实证：误判成 ❌ 查无）
                skipped += 1
                continue
            out.append((ln, int(m.group(1)), body))
    return out, skipped


def segments(q):
    parts = [p.strip() for p in SEG.split(q) if p.strip()]
    return parts if len(parts) > 1 else [q]


def build_refs(book_dir, epub_path):
    """返回 (参照集 flat, {章号: 章 flat}, lane 名)。优先 epub，退 text/。"""
    if epub_path and os.path.exists(epub_path):
        # ⚠️ epub_flat_text 返回带换行的原文本，必须再过一次 flat_alpha 才同口径
        return flat_alpha(epub_flat_text(epub_path)), "完整 lane（epub）"
    parts = [io.open(f, encoding="utf-8", errors="replace").read()
             for f in sorted(glob.glob(os.path.join(book_dir, "text", "*.txt")))]
    if not parts:
        return None, ""
    return flat_alpha("\n".join(parts)), "降级 lane（text/ 逐章拼接）"


def chapter_flats(book_dir):
    out = {}
    tdir = os.path.join(book_dir, "text")
    if not os.path.isdir(tdir):
        return out
    # ⚠️ 2026-10-02 修正（Beach Read 五步审查 e 步实测）：原实现用
    # `re.match(r"ch(\d{2,3})_", fn)` 定位章文件，**只认下划线命名**；
    # 而根 AGENTS.md「文件命名约定」规定精读 md 的唯一分隔符是**单空格**
    # （`ch01 1 the house.txt`）⇒ 空格命名的书章号表**恒为空**，
    # 于是总览每条引语都报「标注与实章不符（标注 ch25，实章 *空*）」＝
    # **整类假红**，且报数看着像「标签全错」而不是「工具没跑」。
    # 收口为 chapter_text_path.find_chapter_text（分隔符已兼容 _ / . / 空格），
    # 与 check_block_keywords / check_quote_blocks 用同一实现。
    for fn in sorted(os.listdir(tdir)):
        m = re.match(r"^ch(\d+)", fn)
        if not m or not fn.endswith(".txt"):
            continue
        p = find_chapter_text(book_dir, int(m.group(1)))
        if p is None:
            continue
        with io.open(p, encoding="utf-8", errors="replace") as f:
            out[int(m.group(1))] = flat_alpha(f.read())
    return out


def main():
    ap = argparse.ArgumentParser(description="总览层引语逐字 + （chNN）章号标注核对")
    ap.add_argument("book_dir")
    ap.add_argument("epub", nargs="?", default="")
    a = ap.parse_args()

    book = a.book_dir
    ovs = [os.path.join(book, n) for n in OVERVIEWS]
    ovs = [p for p in ovs if os.path.exists(p)]
    if not ovs:
        print(f"⚠️ 未找到 {OVERVIEWS[0]} 等总览文件（{book}），跳过")
        return 0

    epub = a.epub
    if not epub:
        eps = sorted(glob.glob(os.path.join(book, "library", "*.epub")))
        epub = eps[0] if eps else ""
    full, lane = build_refs(book, epub)
    if full is None:
        print(f"❓ {book} 无 epub 且无 text/ ⇒ 无法判定（不是通过）")
        return 2
    ch_flat = chapter_flats(book)

    print("=== 总览引语标注核对（逐字 + chNN 归属）：%s ===" % book)
    print("参照集：%s" % lane)

    counts, problems, outside, total, skipped_total = {}, [], [], 0, 0
    for path in ovs:
        name = os.path.basename(path)
        items, skipped = parse_quotes(path)
        total += len(items)
        skipped_total += skipped
        print("\n===== %s：%d 条带标签引语（跳过无标签行 %d）=====" % (name, len(items), skipped))
        for ln, ch, q in items:
            # 口径外：`"A" / "B"` 这种用 / 拼两条引语的形态，整体 flat 必然查无，
            # 但不是缺陷（what-grows-in-the-dark 00_情感节点.md:104 实证）。
            # 单独列出来等人判，不计入失败——**别把它算成查无**。
            if " / " in q and q.count("\"") + q.count("‘") >= 4:
                outside.append((name, ln, ch, q))
                continue
            segs = [flat_alpha(s) for s in segments(q) if len(s) >= MIN_SEG]
            miss = [s for s in segs if s not in full]
            where = {s: sorted(c for c, t in ch_flat.items() if s in t) for s in segs}
            if miss:
                tag = "❌ 全书查无"
            elif ch is not None and all(ch in w for w in where.values()):
                tag = "✅ 标注章逐字"
            else:
                allc = sorted({c for w in where.values() for c in w})
                tag = "⚠️ 标注与实章不符（标注 ch%s，实章 %s）" % (
                    ch, ",".join("ch%02d" % c for c in allc))
            key = tag.split("（")[0].strip()
            counts[key] = counts.get(key, 0) + 1
            if not tag.startswith("✅"):
                problems.append((name, ln, ch, q, tag))
                print("  %s:%d  %s" % (name, ln, tag))
                print("      md: %s" % q[:110])

    if total == 0:
        print("\n该书总览无（chNN）标注引语（跳过 %d 行）——本工具只核标注层，"
              "裸引语归 verify_overview_quotes.py。不是通过。" % skipped_total)
        return 0

    print("\n----- 汇总（共 %d 条带标签引语，跳过无标签行 %d）-----" % (total, skipped_total))
    for k in sorted(counts):
        print("  %s : %d" % (k, counts[k]))
    print("\n----- 口径外（%d 条，不计入失败，需人判）-----" % len(outside))
    for name, ln, ch, q in outside:
        print("  %s:%d  标注ch%s  含 / 分隔的复合引语\n    %s" % (name, ln, ch, q[:140]))
    print("\n----- 待人判清单（%d 条）-----" % len(problems))
    for name, ln, ch, q, tag in problems:
        print("  %s:%d  标注ch%s  %s\n    %s" % (name, ln, ch, tag, q[:140]))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())