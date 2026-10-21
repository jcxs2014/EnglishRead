#!/usr/bin/env python3
"""块内英文覆盖检查（独立实现，用于 d 步语义二审）。

判据（与写作期分析路径不同：按「引语块」作用域切分，逐字段取英文片段）：
  对每个引语块的每个分析字段，取其中的英文片段，判定它落在哪一层：
    BLOCK   该片段在本块引语内（逐字）        → 合规
    PARTIAL 该片段不在本块引语内，但逐词都在  → 引语截短（弱）：分析依赖引语外原文
    CHAPTER 整段不在本块引语内，但在本章 text/ 里 → 引语截短（强）：分析引用了本章另一处原文
    CROSSCH 整段不在本章，但在全书 text/ 里   → 跨章引用（合法，需人工确认指向）
    NONE    全书都查无                        → 分析层走形/虚构
  只做「同一块内」判定：片段必须来自与引语同块的相邻字段行。

用法：python3 scripts/block_scope_check.py <书目录> [--json]
"""
import argparse, glob, json, os, re, sys

HAN = re.compile(r"[一-鿿]")
ENW = re.compile(r"[A-Za-z][A-Za-z'’-]*")
QUOTE_LINE = re.compile(r"^>\s*\*\*原句\s+(\d+):\*\*\s*(.*)$")
LABEL = re.compile(r"^\*\*([^*]+)\*\*[：:]\s*(.*)$")
# 分析字段
FIELDS = ("中文理解", "关键词", "句子结构", "为什么这样写", "读者视角提示", "表达方式")
# 字段里引用的英文：优先取引号内的整体，其次取裸的英文词组
INLINE_QUOTED = re.compile(r'[“"]([^“”"]+)[”"]|「([^「」]+)」|`([^`]+)`')

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def frag_words(s):
    return [w.lower() for w in ENW.findall(s)]

def in_flat(frag, flat):
    """整段连续出现（flat 口径：只保留字母数字小写）。"""
    f = re.sub(r"[^a-z0-9]+", "", frag.lower())
    return bool(f) and f in flat

def in_words(frag, words):
    ws = set(w.lower() for w in words)
    return all(w.lower() in ws for w in frag_words(frag))

def load_texts(book):
    out = {}
    for p in sorted(glob.glob(os.path.join(book, "text", "*.txt"))):
        out[os.path.basename(p)] = open(p, encoding="utf-8", errors="replace").read()
    return out

def book_flat(texts):
    return re.sub(r"[^a-z0-9]+", "", "".join(texts.values()).lower())

def chapter_of(fname):
    m = re.search(r"ch(\d+)", fname)
    return int(m.group(1)) if m else None

def parse_blocks(path):
    """返回 [(章号, 原句号, 引语文本, [(字段, 内容), ...])]"""
    lines = open(path, encoding="utf-8").read().split("\n")
    ch = chapter_of(os.path.basename(path))
    blocks, cur = [], None
    for ln in lines:
        m = QUOTE_LINE.match(ln)
        if m:
            if cur: blocks.append(cur)
            cur = {"ch": ch, "n": int(m.group(1)), "quote": m.group(2), "fields": []}
            continue
        if cur is None: continue
        mm = LABEL.match(ln)
        if mm and mm.group(1) in FIELDS:
            cur["fields"].append((mm.group(1), mm.group(2)))
        elif ln.startswith("## ") or ln.startswith("> **原句"):
            if cur: blocks.append(cur); cur = None
    if cur: blocks.append(cur)
    return blocks

def extract_frags(field, content):
    """取该字段里的英文片段。"""
    out = []
    for mm in INLINE_QUOTED.finditer(content):
        s = next(g for g in mm.groups() if g is not None)
        if ENW.search(s): out.append(s.strip())
    # 去掉引号整体后的剩余裸英文词组（≥3 词）
    rest = INLINE_QUOTED.sub(" ", content)
    for mm in re.finditer(r"[A-Za-z][A-Za-z'’\-]*(?:[ ,]+[A-Za-z][A-Za-z'’\-]*){2,}", rest):
        s = mm.group(0).strip()
        if len(s.split()) >= 3: out.append(s)
    seen, uniq = set(), []
    for s in out:
        k = norm(s)
        if k and k not in seen:
            seen.add(k); uniq.append(s)
    return uniq

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--min-words", type=int, default=3)
    a = ap.parse_args()
    book = a.book
    texts = load_texts(book)
    if not texts:
        print("❓ 无法判定：本书没有 text/ 提取件（未进扫描集，不是「干净」）"); sys.exit(2)
    allflat = book_flat(texts)
    chap_flat = {}
    for name, t in texts.items():
        chap_flat.setdefault(chapter_of(name), re.sub(r"[^a-z0-9]+", "", t.lower()))
    rows = []
    for p in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        for b in parse_blocks(p):
            qflat = re.sub(r"[^a-z0-9]+", "", b["quote"].lower())
            qwords = frag_words(b["quote"])
            for fname, content in b["fields"]:
                for frag in extract_frags(fname, content):
                    if len(frag_words(frag)) < a.min_words: continue
                    if in_flat(frag, qflat): continue
                    if in_words(frag, qwords):
                        verdict = "PARTIAL"
                    elif b["ch"] in chap_flat and in_flat(frag, chap_flat[b["ch"]]):
                        verdict = "CHAPTER"
                    elif in_flat(frag, allflat):
                        verdict = "CROSSCH"
                    else:
                        verdict = "NONE"
                    rows.append({
                        "file": os.path.basename(p), "line": 0, "ch": b["ch"], "n": b["n"],
                        "field": fname, "verdict": verdict, "frag": frag[:160],
                    })
    cnt = {}
    for r in rows: cnt[r["verdict"]] = cnt.get(r["verdict"], 0) + 1
    print(f"=== 块内英文覆盖检查：{os.path.basename(book.rstrip('/'))} ===")
    print(f"分析层英文片段（≥{a.min_words} 词）总数：{len(rows)}")
    for k in ("PARTIAL", "CHAPTER", "CROSSCH", "NONE"):
        print(f"  {k:8} {cnt.get(k,0)}")
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
    else:
        for r in rows:
            if r["verdict"] in ("CHAPTER", "NONE", "CROSSCH"):
                print(f"  [{r['verdict']}] {r['file']} 原句{r['n']} [{r['field']}] {r['frag']!r}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
