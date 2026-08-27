#!/usr/bin/env python3
"""
extract_chapters.py — 把书籍 epub 拆分为逐章纯文本（精读前的"原文先行"第一步）

用法：
  python3 scripts/extract_chapters.py "<epub路径>" [--out-dir <text目录>] [--start 1] [--prefix ch]

行为：
  - 按 OPF spine 顺序读入各 html 分册，跳过封面/版权/目录等非正文页（打印明细供人工确认）；
  - 清洗 HTML：段落保留换行、修复首字母下沉（dropcap "S OME"→"Some"）；
  - 输出 <out-dir>/ch<NN>_<slug>.txt，打印每章字数与推断标题。
"""
import re, sys, html, os, zipfile, argparse, glob, posixpath

def clean(raw: str) -> str:
    t = re.sub(r'<(p|div|h[1-6]|li|br)\b[^>]*>', '\n', raw)
    t = re.sub(r'</(p|div|h[1-6])>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)          # 行内标签删除，不引入空格（保住 dropcap 相邻拼合）
    t = html.unescape(t)
    # dropcap 修连："S" + 小体大写 "OME" → Some
    t = re.sub(r'\b([A-Z])\s+([A-Z][a-z]+|[A-Z]{2,})\b',
               lambda m: m.group(1) + m.group(2).capitalize(), t)
    t = t.replace('\u00a0', ' ')
    lines = []
    for l in t.split('\n'):
        l = l.strip()
        if not l:
            lines.append('')
        elif lines and lines[-1] and not l[0].isupper() and not re.match(r'^[\u201c\u201d\'"(\-—*\d]', l):
            lines[-1] += ' ' + l
        else:
            lines.append(l)
    return '\n'.join(lines).strip()

def slugify(title: str, fallback: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip('_')
    return (s or fallback)[:40]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("epub"); ap.add_argument("--out-dir"); ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--prefix", default="ch")
    a = ap.parse_args()

    z = zipfile.ZipFile(a.epub)
    container = z.read('META-INF/container.xml').decode('utf-8', 'ignore')
    opf_path = posixpath.dirname(re.search(r'full-path="([^"]+)"', container).group(1))
    opf_file = re.search(r'full-path="([^"]+)"', container).group(1)
    opf = z.read(opf_file).decode('utf-8', 'ignore')

    manifest = {}
    for it in re.findall(r'<item\b[^>]*/?>', opf):
        idm = re.search(r'id="([^"]+)"', it); hm = re.search(r'href="([^"]+)"', it)
        tm = re.search(r'media-type="([^"]+)"', it)
        if idm and hm: manifest[idm.group(1)] = (posixpath.normpath(posixpath.join(opf_path, hm.group(1))), (tm.group(1) if tm else ''))

    # TOC 标签映射 href -> title
    labels = {}
    for n in z.namelist():
        if n.lower().endswith('.ncx'):
            ncx = z.read(n).decode('utf-8', 'ignore')
            for blk in ncx.split('<navPoint ')[1:]:
                lm = re.search(r'<text>(.*?)</text>', blk); sm = re.search(r'<content\s+src="([^"]+)"', blk)
                if lm and sm:
                    labels[posixpath.normpath(posixpath.join(opf_path, html.unescape(sm.group(1)).split('#')[0]))] = html.unescape(lm.group(1))

    skip_pat = re.compile(r'(cover|copyright|colophon|\bcontents\b|\btoc\b|title[_ ]?page|other ?books|dedication|acknowledg|\bnotes\b|appendix|translator|bibliograph|\bindex\b|epigraph|about ?the ?author|praise ?for|excerpt)', re.I)
    out_dir = a.out_dir or '.'
    os.makedirs(out_dir, exist_ok=True)
    written, skipped = [], []

    n = a.start
    for idref in re.findall(r'<itemref\b[^>]*idref="([^"]+)"', opf):
        if idref not in manifest: continue
        path, mtype = manifest[idref]
        if 'html' not in mtype and not path.lower().endswith(('.html','.htm','.xhtml')): continue
        raw = z.read(path).decode('utf-8', errors='ignore')
        text = clean(raw)
        title = labels.get(posixpath.normpath(path), '')
        is_story = len(text) > 600 and not (skip_pat.search(title) or skip_pat.search(path.split('/')[-1]))
        if not is_story:
            skipped.append((path.split('/')[-1], title or '(no label)', len(text)))
            continue
        body = text
        # 去掉文件头部的书名横幅行（如 "The Stories of Vladimir Nabokov"）
        first_lines = [l for l in body.split('\n') if l][:3]
        for fl in first_lines:
            if fl.strip().lower().startswith(('the stories of', 'stories of')) and len(body.split('\n')) > 2:
                body = '\n'.join(l for l in body.split('\n')[1:] if True).strip()
                break
        slug = slugify(title, f'chap{n}')
        target = f"{a.prefix}{n:02d}_{slug}.txt"
        open(f"{out_dir}/{target}", 'w').write(body + "\n")
        written.append((n, target, len(alpha_safe(body)), title or target))
        n += 1

    print(f"写入 {len(written)} 章 → {out_dir or '.'}")
    for w in written:
        print(f"  {w[0]:>3}  {w[1]:<48s} {w[2]:>7} 字符   {w[3]}")
    print(f"\n跳过 {len(skipped)} 页（非正文）：")
    for s in skipped:
        print(f"  ~ {s[0]:<44s} {str(s[2]):>7}   {s[1]}")

def alpha_safe(s): return re.sub(r'\s+', '', s)

if __name__ == "__main__":
    main()
