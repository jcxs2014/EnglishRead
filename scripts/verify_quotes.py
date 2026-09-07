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
    # NFKD 归一：组合变音符（如 Buzău = a+U+030C）拆解后丢弃，防组合字符假 MISS（Language City ch03 实证）
    import unicodedata
    s = unicodedata.normalize('NFKD', s)
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
    """按行提取候选引文，兼容多种书写顺序；同文本去重保序。

    口径：
      ① 圈数字行（①-㉕，裸字/粗体/引号包裹均可）
      ② "> **原句 N:**" 行
      ③ "> ### 第N处「...」" 标题口径不在本工具（check_chapter_quotes 管）
      ④ 言情无编号格式：`> "..."` blockquote 引号行（Up in Molten Lights 实证
         verify_quotes 对该格式抽到 0/0——2026-09-06 增补）
    短引语（<20 flat 字符）不参与校验但单独计数返回，提示人工 grep
    （Perfection/Forest of Scars/Rookie Season 三书互证的静默跳过盲区）。
    """
    quotes = []
    seen = set()
    short = 0
    for raw in txt.splitlines():
        s = raw.strip()
        m = (re.match(r'^[' + CIRCLED + r']\s+(.+)$', s)
             or re.match(r'^\*{1,2}[' + CIRCLED + r']\*{1,2}\s+["\'](.*)["\']', s)
             or re.match(r'^[' + CIRCLED + r']\s+["\'](.*)["\']', s)
             or re.match(r'^>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s+(.+)$', s)
             or re.match(r'^>\s*["\u201c](.+)$', s))   # 言情无编号 blockquote
        if not m:
            continue
        body = m.group(1).strip()
        # 言情行尾可能是 `" he said.` 叙述标签——剥掉引号外内容后校验引号内
        if body and not body.rstrip().endswith(('"', '”', "'", '’')):
            m2 = re.match(r'^["\u201c](.*?)[”"]\s*(?:[A-Za-z].{0,60})?$', body)
            if m2:
                body = m2.group(1)
        # 剥掉包裹性的粗体/斜体/引号字符（内容级引语完整性交给指纹比对判断）
        body = body.strip('*')
        body = body.strip('\'"“”‘’ ')
        fa = len(flat_alpha(body))
        if fa < 20:
            if fa >= 5:
                short += 1   # 有英文内容但太短——计数，提示人工核
            continue
        if body not in seen:
            seen.add(body)
            quotes.append(body)
    return quotes, short

def main(book_dir: str, epub_path: str):
    full = flat_alpha(epub_flat_text(epub_path))
    total_ok = total = clean = bad = 0
    short_total = 0
    for f in sorted(glob.glob(os.path.join(book_dir, "*.md"))):
        name = os.path.basename(f)
        txt = open(f, encoding="utf-8").read()
        quotes, short = extract_quotes(txt)
        short_total += short
        if not quotes:
            if short:
                print(f"{name}: ⚠️ 0 条长引语 + {short} 条短引语（<20字符，工具不校验，须人工 grep）")
            else:
                print(f"{name}: ⚠️ 未提取到编号引语（请人工核对格式）")
            continue
        ok = 0
        miss = []
        for q in quotes:
            qa = flat_alpha(q)
            frag = qa[:52]
            if frag in full:
                ok += 1
                continue
            # 引号分段回退：`"A" tag "B"` 跨标签行拆引号内各段独立验证
            # （对话体跨标签实证——flat 指纹跨标签必 MISS）
            qparts = re.findall(r'["\u201c]([^"\u201d]{12,})["\u201d]', q)
            if len(qparts) >= 2 and all(flat_alpha(p)[:40] in full for p in qparts):
                ok += 1
                continue
            # 省略号分段回退：每段均命中全书才算过
            segs = [p for p in re.split(r'…|\.\.\.', q)
                    if len(flat_alpha(p)) >= 15]
            if segs and all(flat_alpha(p)[:40] in full for p in segs):
                ok += 1
                continue
            miss.append(frag[:40])
        total_ok += ok
        total += len(quotes)
        note = f"（另有 {short} 条短引语未校验）" if short else ""
        if ok == len(quotes):
            clean += 1
            print(f"{name}: {ok}/{len(quotes)} ✅{note}")
        else:
            bad += 1
            print(f"{name}: {ok}/{len(quotes)} ❌{note}")
            for m in miss[:2]:
                print(f"    ✗ {m}...")
    if short_total:
        print(f"\n⚠️ 全书共 {short_total} 条短引语（<20 flat 字符）未被校验——按规则须人工 grep 兜底")
    print(f"\n=== 总计 {total_ok}/{total} 引文可核实（{round(total_ok/total*100) if total else 0}%）；完全干净文件 {clean}/{clean+bad} ===")
    sys.exit(0 if bad == 0 and total > 0 else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
