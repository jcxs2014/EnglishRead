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
from urllib.parse import unquote

# 出版商 dropcap 修连：**必须在标签还完整时做**（剥标签后无法再判断大写到哪结束）。
# 排版形态：<span class="dropcap-rw">I</span><span class="smallcaps-rw">T WAS UNSPOKEN</span>
# 产出：首字母 + 逐词首字母大写 + 单空格（"IT WAS UNSPOKEN"，即正常句子形态）。
#
# 为什么不用纯文本启发式（`\b([A-Z])\s+([A-Z]{2,})\b`）：两种失败都实测到
#   ① U+200B 零宽空格在 dropcap 与小体大写之间，对 `\s` 不匹配、对 `\b` 是词边界
#      ⇒ "I|ZSP|T WAS" → "I|ZSP|TWas"（吞空格）；
#   ② 贪婪吞整段大写、只 capitalize() 留首词 ⇒ "A MAN CAME TO" → "AMan"，
#      既吞空格又丢词。
# 34 章里 ① 命中 9 章、② 命中 6 章。标签层是唯一可靠口径。
DROP_RE = re.compile(
    r'<span class="dropcap-rw">([^<]*)</span>( ?)<span class="smallcaps-rw">([^<]*)</span>')

def _fix_dropcap_markup(t: str) -> str:
    def rep(m):
        head, gap, small = m.group(1).strip(), m.group(2), m.group(3).replace('\u200b', ' ')
        small = small.strip()
        if not small:
            return head
        # 排版有两种形态，本书两种都有（B 形态 8 章：A MAN / I AWOKE / A MONTH…）：
        #   A 形态（首个词被 dropcap 拆开）：gap 为空
        #        "<span>T</span><span>HE LAST DAY" ⇒ "THE LAST DAY"（T+HE=THE）
        #   B 形态（dropcap 是独立单字母词）：gap 为一个空格
        #        "<span>A</span> <span>MAN CAME TO" ⇒ "A MAN CAME TO"
        # **判据只能是这个空格本身**：dropcap 与 smallcaps 都是全大写，
        # 纯文本层分不出 "T"+"HE"（同词）与 "A"+"MAN"（异词）——
        # "AN"/"IN"/"TH" 全都是合法的已拼好词。原始 HTML 的间隔是唯一可靠信号。
        joined = (head + small) if gap == '' else (head + ' ' + small)
        # 末词后原文有空格要补回（"I FOUND " + "a letter" ⇒ 不能拼成 "FOUNDa"）
        tail = ' ' if m.group(3).replace('\u200b', '').endswith(' ') else ''
        return re.sub(r'\s+', ' ', joined).strip() + tail
    return DROP_RE.sub(rep, t)


def clean(raw: str) -> str:
    t = _fix_dropcap_markup(raw)
    t = re.sub(r'<(p|div|h[1-6]|li|br)\b[^>]*>', '\n', t)
    t = re.sub(r'</(p|div|h[1-6])>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)          # 行内标签删除，不引入空格
    t = html.unescape(t)
    t = t.replace('\u200b', '')            # 排版零宽残留（非原文字符）
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
    ap.add_argument("--min-len", type=int, default=600, help="最小正文字符数（默认 600；短篇插叙章节书可降到 200）")
    a = ap.parse_args()

    z = zipfile.ZipFile(a.epub)
    container = z.read('META-INF/container.xml').decode('utf-8', 'ignore')
    opf_path = posixpath.dirname(re.search(r'full-path="([^"]+)"', container).group(1))
    opf_file = re.search(r'full-path="([^"]+)"', container).group(1)
    opf = z.read(opf_file).decode('utf-8', 'ignore')
    # 书名（用于剥书眉）：dc:title 首个
    _mt = re.search(r'<dc:title[^>]*>(.*?)</dc:title>', opf, re.S)
    book_title = html.unescape(re.sub(r'\s+', ' ', _mt.group(1))).strip() if _mt else ''

    manifest = {}
    for it in re.findall(r'<item\b[^>]*/?>', opf):
        idm = re.search(r'id="([^"]+)"', it); hm = re.search(r'href="([^"]+)"', it)
        tm = re.search(r'media-type="([^"]+)"', it)
        if idm and hm: manifest[idm.group(1)] = (posixpath.normpath(posixpath.join(opf_path, unquote(hm.group(1)))), (tm.group(1) if tm else ''))

    # TOC 标签映射 href -> title
    labels = {}
    for n in z.namelist():
        if n.lower().endswith('.ncx'):
            ncx = z.read(n).decode('utf-8', 'ignore')
            for blk in ncx.split('<navPoint ')[1:]:
                lm = re.search(r'<text>(.*?)</text>', blk); sm = re.search(r'<content\s+src="([^"]+)"', blk)
                if lm and sm:
                    labels[posixpath.normpath(posixpath.join(opf_path, unquote(html.unescape(sm.group(1)).split('#')[0])))] = html.unescape(lm.group(1))

    # ── 装置页（非正文）判定：2026-09-26 重写 ──
    # **原实现是子串搜索，而被搜的是章节标题（可能是散文性文字），23 个探针里 6 个
    # 误判**，其中 3 个方向最危险——**静默丢掉真实章节**：
    #   `Today You Will Rediscover…`  被 `cover` 命中（discover ⊃ cover）——整章丢失
    #   `Protocol` / `Stockholm`      被 `toc` 命中（toc ⊂ protocol / stockholm）
    #   `The Cover Letter`           被 `Cover` 命中
    # 另有 2 个反向漏进：`Resources` / `Reading Group Guide` 不在任何分支里。
    # 改为**标签精确匹配**（出版商 nav 标签是干净短标签）+ **词边界路径判据**。
    BOILER_LABEL = {
        'cover', 'cover image', 'front cover', 'back cover', 'cover page',
        'title page', 'half title', 'copyright', 'colophon', 'imprint',
        'contents', 'table of contents', 'toc', 'dedication',
        'acknowledgment', 'acknowledgments', 'acknowledgement', 'acknowledgements',
        'about the author', 'about the artist', 'also by', 'also by the author',
        'epigraph', 'index', 'resources', 'reading group guide', 'reader guide',
        'excerpt', 'newsletter', 'sign up', 'other titles', 'other books',
        'works by', 'selected bibliography', 'bibliography', 'notes', 'endnotes',
        'footnotes', 'praise for', 'about the publisher',
    }
    # 出版商固定文件名 + 导航文档 + 促销页
    BOILER_PATH = re.compile(
        r'_(cov|tp|cop|ctc|toc|ded|ack|ata|rsc|excerpt|newsletter|promo|ssd|bmn|cue|int|nav|ncx)\d*_'
        r'|(^|[/_-])(nav|ncx|toc|next-?reads?|promo|advert|ads?)\.xhtml$', re.I)

    def _label_key(s):
        return re.sub(r'[^a-z0-9 ]+', ' ', (s or '').lower()).strip()

    def is_boilerplate(title, path, text_head):
        # ⚠️ nav 标签缺失时用**正文首行兜底**——否则装置页没有标签可测，
        # 只能靠长度放行（实测出版社促销页 "Discover your next great read!"
        # 无 nav 标签，1187 字符 > min_len，于是被当正文收进来）。
        lab = _label_key(title) or _label_key(text_head[:60])
        return lab in BOILER_LABEL or bool(BOILER_PATH.search(path))
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
        is_story = len(text) > a.min_len and not is_boilerplate(
            title, path.split('/')[-1], text)
        if not is_story:
            skipped.append((path.split('/')[-1], title or '(no label)', len(text)))
            continue
        body = text
        # ── 去掉文件头部的书眉/书名横幅行 ──
        # 原实现只认 `the stories of` / `stories of`，是**为某一本书写死的补丁**。
        # 改为通用规则：首行等于书名、或以「, 书名」结尾（出版商 running head 惯例，
        # 实测 `Continued, The Glass Girl` / `Friday, The Glass Girl`），一律删掉。
        # 不删的后果：① 提取件首行不是正文首句，`verify_corpus` 首末句抽印与
        # AGENTS 第 8 条 8.1「先摘录」都会取到书眉；② slug 回落到文件名
        # （`ch02_chap2.txt`），章节名丢失。
        blines = body.split('\n')
        nz = [i for i, l in enumerate(blines) if l.strip()]
        if nz and len(nz) > 1:
            first = blines[nz[0]].strip()
            hit = False
            if book_title:
                bt = re.sub(r'\s+', ' ', book_title).strip().lower()
                fl = re.sub(r'\s+', ' ', first).strip().lower()
                hit = (fl == bt) or fl.endswith(', ' + bt) or fl.endswith(' ' + bt)
            if not hit and first.lower().startswith(('the stories of', 'stories of')):
                hit = True
            if hit:
                del blines[nz[0]]
                body = '\n'.join(blines).strip()
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
