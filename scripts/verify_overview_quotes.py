#!/usr/bin/env python3
"""
verify_overview_quotes.py — 总览文件引文真实性核对工具

用途：检查某本书 00*.md（概述/金句精选/情感节点）中的英文引文，
是否能在 epub 全书中逐字找到。
专门堵住 verify_quotes.py 的盲区——后者只扫 ch*.md，不覆盖总览层。

用法：
  python3 scripts/verify_overview_quotes.py "<书目录绝对路径>" "<epub绝对路径>"

输出：每个 00*.md 文件的 命中数/总数，失败文件列出未命中指纹；末尾给出总账。
原理：与 verify_quotes.py 完全一致（指纹比对逻辑共享），仅扫描目标不同。
"""
import re, sys, glob, html, zipfile, tempfile, os

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'

def flat_alpha(s: str) -> str:
    s = re.sub(r'\\+\s*[nt]', '', s)
    return re.sub(r'[^a-z0-9]', '', s.lower())

def epub_flat_text(epub_path: str) -> str:
    out = ""
    if zipfile.is_zipfile(epub_path):
        with zipfile.ZipFile(epub_path) as z, tempfile.TemporaryDirectory() as td:
            for n in z.namelist():
                if n.lower().endswith((".html", ".htm", ".xhtml")):
                    p = os.path.join(td, re.sub(r'[\\/]', '_', n))
                    open(p, "wb").write(z.read(n))
            for p in glob.glob(os.path.join(td, "*")):
                out += _read_html(p)
    return out

def _read_html(p: str) -> str:
    t = open(p, encoding="utf-8", errors="ignore").read()
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\u00a0', ' ')
    return t

def extract_quotes(txt: str):
    """按行提取候选引文，兼容多种书写顺序；同文本去重保序。"""
    quotes = []
    seen = set()
    for raw in txt.splitlines():
        s = raw.strip()
        # 剥掉 markdown 引用块前缀 "> "（若有）
        s = re.sub(r'^>\s*', '', s)
        # 匹配 ①-⑩ 编号引语块（粗体/裸字/带引号均可）
        m = (re.match(r'^[' + CIRCLED + r']\s+(.+)$', s)
             or re.match(r'^\*{1,2}[' + CIRCLED + r']\*{1,2}\s+["\'](.*)["\']', s)
             or re.match(r'^[' + CIRCLED + r']\s+["\'](.*)["\']', s)
             # 兼容 "> **原句 N:**" 格式
             or re.match(r'^>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s+(.+)$', s))
        if not m:
            continue
        body = m.group(1).strip()
        body = body.strip('*\'"""\' ')
        if len(flat_alpha(body)) >= 20 and body not in seen:
            seen.add(body)
            quotes.append(body)
    return quotes

def main(book_dir: str, epub_path: str):
    if not glob.glob(os.path.join(book_dir, "00*.md")):
        print(f"⚠️ 未找到 00*.md 总览文件（{book_dir}），跳过")
        sys.exit(0)

    full = flat_alpha(epub_flat_text(epub_path))
    total_ok = total = clean = bad = 0
    for f in sorted(glob.glob(os.path.join(book_dir, "00*.md"))):
        name = os.path.basename(f)
        txt = open(f, encoding="utf-8").read()
        quotes = extract_quotes(txt)
        if not quotes:
            print(f"{name}: ⚠️ 未提取到编号引语（请人工核对格式）")
            continue
        ok = 0
        miss = []
        for q in quotes:
            qa = flat_alpha(q)
            frag = qa[:52]
            if frag in full:
                ok += 1
            else:
                miss.append(frag[:40])
        total_ok += ok
        total += len(quotes)
        if ok == len(quotes):
            clean += 1
            print(f"{name}: {ok}/{len(quotes)} ✅")
        else:
            bad += 1
            print(f"{name}: {ok}/{len(quotes)} ❌")
            for m in miss[:3]:
                print(f"    ✗ {m}...")
    print(f"\n=== 总览引文 {total_ok}/{total} 可核实（{round(total_ok/total*100) if total else 0}%）；完全干净文件 {clean}/{clean+bad} ===")
    sys.exit(0 if bad == 0 and total > 0 else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
