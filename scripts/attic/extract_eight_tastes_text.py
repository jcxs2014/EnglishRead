#!/usr/bin/env python3
"""Eight Tastes of Treachery 专用提取器（一次性，attic）

与通用 extract_chapters.py 的差异：
  1. **关闭 dropcap 修连正则**。通用版规则 `\\b([A-Z])\\s+([A-Z][a-z]+|[A-Z]{2,})\\b`
     会把正文小体大写首行 `A TRAIN THIRTY wagons deep` 误改成 `ATrain Th...
     wagons deep`（Pictures of You / Preaching to the Choir 同类实证）。
     本书小体大写一律写作 `<small>A TRAIN THIRTY</small>`，无真 dropcap 结构，
     关掉该正则即可。
  2. **显式 skip 清单**：praise（通用版的 'praise ?for' 匹配不到 01_Praise.xhtml）、
     timeline（背景附录，非正文）、yenne's notes / acknowledgments / about the author。
  3. 输出仍为 ch<NN>_<slug>.txt，NN 按 spine 顺序连续编号，与 md 文件 1:1。
"""
import re, sys, html, os, zipfile, argparse, posixpath
from urllib.parse import unquote

SKIP = re.compile(
    r'(cover|praise|also|title[_ ]?page|review|copyright|\bcontents\b|\btoc\b|dedication|'
    r'\bmap\b|yenne|acknowledg|about ?the ?author|timeline|bibliograph|\bindex\b)', re.I)


def clean(raw: str) -> str:
    t = re.sub(r'<(p|div|h[1-6]|li|br)\b[^>]*>', '\n', raw)
    t = re.sub(r'</(p|div|h[1-6])>', '\n', t)
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', '', t)          # 行内标签删除，不引入空格
    t = html.unescape(t)
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
    ap.add_argument("epub")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--prefix", default="ch")
    a = ap.parse_args()

    z = zipfile.ZipFile(a.epub)
    container = z.read('META-INF/container.xml').decode('utf-8', 'ignore')
    opf_file = re.search(r'full-path="([^"]+)"', container).group(1)
    opf_path = posixpath.dirname(opf_file)
    opf = z.read(opf_file).decode('utf-8', 'ignore')

    manifest = {}
    for it in re.findall(r'<item\b[^>]*/?>', opf):
        idm = re.search(r'id="([^"]+)"', it); hm = re.search(r'href="([^"]+)"', it)
        tm = re.search(r'media-type="([^"]+)"', it)
        if idm and hm:
            manifest[idm.group(1)] = (posixpath.normpath(posixpath.join(opf_path, unquote(hm.group(1)))),
                                      (tm.group(1) if tm else ''))

    labels = {}
    for n in z.namelist():
        if n.lower().endswith('.ncx'):
            ncx = z.read(n).decode('utf-8', 'ignore')
            for blk in ncx.split('<navPoint ')[1:]:
                lm = re.search(r'<text>(.*?)</text>', blk)
                sm = re.search(r'<content\s+src="([^"]+)"', blk)
                if lm and sm:
                    labels[posixpath.normpath(posixpath.join(opf_path,
                          unquote(html.unescape(sm.group(1)).split('#')[0])))] = html.unescape(lm.group(1))

    os.makedirs(a.out_dir, exist_ok=True)
    written, skipped = [], []
    n = a.start
    for idref in re.findall(r'<itemref\b[^>]*idref="([^"]+)"', opf):
        if idref not in manifest:
            continue
        path, mtype = manifest[idref]
        if 'html' not in mtype and not path.lower().endswith(('.html', '.htm', '.xhtml')):
            continue
        raw = z.read(path).decode('utf-8', errors='ignore')
        body = clean(raw)
        fname = path.split('/')[-1]
        title = labels.get(posixpath.normpath(path), '')
        if SKIP.search(fname) or SKIP.search(title) or len(re.sub(r'\s+', '', body)) < 300:
            skipped.append((fname, title or '(no label)', len(re.sub(r'\s+', '', body))))
            continue
        slug = slugify(title, f'chap{n}')
        target = f"{a.prefix}{n:02d}_{slug}.txt"
        open(os.path.join(a.out_dir, target), 'w').write(body + "\n")
        written.append((n, target, len(re.sub(r'\s+', '', body)), title or target))
        n += 1

    print(f"写入 {len(written)} 篇 → {a.out_dir}")
    for w in written:
        print(f"  {w[0]:>3}  {w[1]:<50s} {w[2]:>7} 字符   {w[3]}")
    print(f"\n跳过 {len(skipped)} 页（非正文）：")
    for s in skipped:
        print(f"  ~ {s[0]:<44s} {str(s[2]):>7}   {s[1]}")


if __name__ == "__main__":
    main()
