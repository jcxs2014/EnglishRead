#!/usr/bin/env python3
"""
verify_quotes.py — 书籍精读引文真实性核对工具

用途：检查某本书所有精读 md 文件中 ①-⑩ 编号引语块里的英文引文，
是否能在对应 epub 全书中逐字找到。抓不到的即视为"凭记忆转写或虚构"。

用法：
  python3 scripts/verify_quotes.py "<书目录绝对路径>" "<epub绝对路径>"

输出：每个文件的 命中数/总数，失败文件列出未命中指纹；末尾给出总账。
原理：把 epub 所有 html 展平为纯文本，与引文同时做"仅保留字母数字、
      大小写不敏感、去全部空白"处理后再比对，规避首字母下沉(dropcap)
      与弯直引号差异造成的误报。
"""
import re, sys, glob, html, zipfile, tempfile, os

def flat_alpha(s: str) -> str:
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
                out += read_html(p)
    return out

def read_html(p: str) -> str:
    t = open(p, encoding="utf-8", errors="ignore").read()
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\u00a0', ' ')
    return t

def main(book_dir: str, epub_path: str):
    full = flat_alpha(epub_flat_text(epub_path))
    total_ok = total = clean = bad = 0
    for f in sorted(glob.glob(os.path.join(book_dir, "*.md"))):
        name = os.path.basename(f)
        txt = open(f, encoding="utf-8").read()
        quotes = re.findall(r'^[①②③④⑤⑥⑦⑧⑨⑩]\s+\*\*"(.+?)"\*\*', txt, re.M)
        quotes += re.findall(r'>\s*\*\*原句\s*\d+[:：]\*\*\s*"?(.+?)"?\s*\*\*', txt, re.M)
        if not quotes:
            print(f"{name}: ⚠️ 未提取到编号引语（请人工核对格式）")
            continue
        ok = 0
        miss = []
        for q in quotes:
            qa = flat_alpha(q)
            if len(qa) < 20:
                continue
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
            for m in miss[:2]:
                print(f"    ✗ {m}...")
    print(f"\n=== 总计 {total_ok}/{total} 引文可核实（{round(total_ok/total*100) if total else 0}%）；完全干净文件 {clean}/{clean+bad} ===")
    sys.exit(0 if bad == 0 and total > 0 else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
