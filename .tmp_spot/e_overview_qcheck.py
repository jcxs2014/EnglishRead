#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""e 步专用：总览三篇里 verify_overview_quotes 未解析的引语（概述/情感节点的 `> ` 形态）逐字核验。

纪律（模板「审查过程自身四条纪律」第 1 条）：换实现。
本脚本不复用 verify_overview_quotes 的解析器（它对 `> ` 形态 0 提取），
改为独立解析 `^> ` 行；比对端**必须复用 verify_quotes 的 flat 口径**
（模板：`flat_alpha()` + `epub_flat_text()`），否则会自造口径出假红。

输出四档：
  ✅ 逐字命中全书        ✅ 同段命中
  ⚠️ 跨章命中（真在别章）  ← 阻断型候选
  ❌ 全书查无             ← 阻断型候选
"""
import io, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "vq", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "verify_quotes.py"))
vq = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vq)

BOOK = sys.argv[1] if len(sys.argv) > 1 else "notes/books/novels/only-a-monster-by-vanessa-len"
EPUB = os.path.join(BOOK, "library",
                    "Only a Monster -- Vanessa Len -- Only a Monster 01, 2021 -- "
                    "A&U Children’s -- 1761063669 -- 91e5fbe1ddeffa7d88a24a311d8dca36 -- "
                    "Anna’s Archive.epub")

LABEL = re.compile(r"（\s*ch\s*(\d{1,3})\s*）\s*$")
SEG = re.compile(r"\s*(?:…|\.\s\.\s\.)\s*")

NUM = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
# 形态 A（概述/情感节点）：`> {Q}（chNN）`
# 形态 B（金句精选）：`① {Q}（chNN）` 主条 + 呼应关系里的 `- {Q}（chNN）`
LINE_B = re.compile(r"^\s*(?:[-*]\s+|[%s]\s+)(.+?)$" % NUM)


def parse_quotes(md_path):
    """独立解析两种形态，去掉尾部（chNN）标签与行内 {Q:c:s} 标记。

    形态 B 只收**带（chNN）标签且正文像英文引语**的行——呼应关系里还有纯中文
    引导句（`- ch07 那条构成提问与反问——…`），那些不是引语。
    """
    is_jinju = os.path.basename(md_path) == "00_金句精选.md"
    out = []
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
            m = LABEL.search(body)
            if is_jinju and not m:
                continue          # 纯中文引导句，不是引语
            ch = int(m.group(1)) if m else None
            if m:
                body = body[:m.start()].strip()
            body = re.sub(r"\{[^}]*\}", "", body).strip()
            # 必须像英文引语（含拉丁字母，否则是中文行）
            if body and re.search(r"[A-Za-z]", body):
                out.append((ln, ch, body))
    return out

def segments(q):
    parts = [p.strip() for p in SEG.split(q) if p.strip()]
    return parts if len(parts) > 1 else [q]

def main():
    # ⚠️ epub_flat_text 返回带换行的原文本，必须再过一次 flat_alpha 才与 flat_alpha(引语) 同口径
    full = vq.flat_alpha(vq.epub_flat_text(EPUB))
    ch_flat = {}
    tdir = os.path.join(BOOK, "text")
    for fn in sorted(os.listdir(tdir)):
        m = re.match(r"ch(\d{2})_", fn)
        if not m:
            continue
        with io.open(os.path.join(tdir, fn), encoding="utf-8", errors="replace") as f:
            ch_flat[int(m.group(1))] = vq.flat_alpha(f.read())

    counts = {}
    problems = []
    for name in ("00_概述.md", "00_情感节点.md", "00_金句精选.md"):
        path = os.path.join(BOOK, name)
        items = parse_quotes(path)
        print("\n===== %s：%d 条引语 =====" % (name, len(items)))
        for ln, ch, q in items:
            segs = [vq.flat_alpha(s) for s in segments(q)]
            miss = [s for s in segs if len(s) >= 8 and s not in full]
            # 每段落在哪些章
            where = {}
            for s in segs:
                if len(s) < 8:
                    continue
                where[s] = sorted(c for c, t in ch_flat.items() if s in t)
            if miss:
                tag = "❌ 全书查无"
            elif ch is not None and all(ch in w for w in where.values()):
                tag = "✅ 标注章逐字"
            else:
                allc = sorted({c for w in where.values() for c in w})
                tag = "⚠️ 标注与实章不符（标注 ch%s，实章 %s）" % (
                    ch, ",".join("ch%02d" % c for c in allc))
            if not tag.startswith("✅"):
                problems.append((name, ln, ch, q, tag))
            counts[tag.split("（")[0].strip()] = counts.get(tag.split("（")[0].strip(), 0) + 1
            if tag.startswith(("⚠️", "❌")):
                print("  %s:%d  %s" % (name, ln, tag))
                print("      md: %s" % q[:110])
    print("\n----- 汇总 -----")
    for k in sorted(counts):
        print("  %s : %d" % (k, counts[k]))
    print("\n----- 待人判清单（%d 条）-----" % len(problems))
    for name, ln, ch, q, tag in problems:
        print("  %s:%d  标注ch%s  %s\n    %s" % (name, ln, ch, tag, q[:140]))
    return 0

if __name__ == "__main__":
    sys.exit(main())