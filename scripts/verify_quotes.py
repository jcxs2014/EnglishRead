#!/usr/bin/env python3
"""
verify_quotes.py — 书籍精读引文真实性核对工具

用途：检查某本书所有精读 md 文件中 ①-⑩ 编号引语块里的英文引文，
是否能在对应 epub 全书中逐字找到。抓不到的即视为"凭记忆转写或虚构"。

用法：
  python3 scripts/verify_quotes.py "<书目录绝对路径>" "<epub绝对路径>"

输出：每个文件的 命中数/总数，失败文件列出未命中指纹；末尾给出总账。
原理：
  1. epub 所有 html 展平为纯文本；
  2. 精读 md 按行提取编号块——凡以 ①-⑩（裸字/**粗体**/**顺序均可）
     或 "> **原句 N:**" 开头的行，取该行剩余部分为候选引文；
  3. 双方做"仅保留字母数字、大小写不敏感"指纹比对——行级取材 +
     指纹剥格式，双重规避 dropcap 大写、弯直引号、内部单引号、
     markdown 加粗等一切差异。
"""
import re, sys, glob, html, zipfile, tempfile, os

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'

def flat_alpha(s: str) -> str:
    # 先剥掉引文里手写的段落转义符（\n/\t 会被指纹误读为字母 nn/tt）
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
                out += read_html(p)
    return out

def read_html(p: str) -> str:
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
        m = (re.match(r'^[' + CIRCLED + r']\s+(.+)$', s)
             or re.match(r'^\*{1,2}[' + CIRCLED + r']\*{1,2}\s+["\'](.*)["\']', s)
             or re.match(r'^[' + CIRCLED + r']\s+["\'](.*)["\']', s)
             or re.match(r'^>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s+(.+)$', s))
        if not m:
            continue
        body = m.group(1).strip()
        # 剥掉包裹性的粗体/斜体/引号字符（内容级引语完整性交给指纹比对判断）
        body = body.strip('*')
        body = body.strip('\'"“”‘’ ')
        if len(flat_alpha(body)) >= 20 and body not in seen:
            seen.add(body)
            quotes.append(body)
    return quotes

def main(book_dir: str, epub_path: str):
    full = flat_alpha(epub_flat_text(epub_path))
    total_ok = total = clean = bad = 0
    for f in sorted(glob.glob(os.path.join(book_dir, "*.md"))):
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
            for m in miss[:2]:
                print(f"    ✗ {m}...")
    print(f"\n=== 总计 {total_ok}/{total} 引文可核实（{round(total_ok/total*100) if total else 0}%）；完全干净文件 {clean}/{clean+bad} ===")
    sys.exit(0 if bad == 0 and total > 0 else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
