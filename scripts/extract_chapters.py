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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# 页码锚点剥离与 epub 参照集**共用同一实现**（verify_quotes）。提取侧剥、参照侧不剥
# 会造成「跨页引语两侧都不认识」的假 MISS，故口径只能有一份。
from verify_quotes import strip_page_anchors  # noqa: E402

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


def head_title_of(raw: str) -> str:
    """取 `<head>` 里的 `<title>` 文本（出版商 running head / 章标题的来源）。

    ⚠️ 2026-10-20（Ebenezer Scrooge 实测）：`<title>` 的内容会**原样进入正文**
    （`clean()` 只删标签、不删 title 里的文字）⇒ 它就是 text/ 首行。
    两种角色：
      ① **章标题行**（"Chapter 1" / "Prologue" / "1. Clem: January 3, 1883"…）
         ——本库既有惯例（500 个 text/ 目录里 259 个首行如此），**必须保留**；
      ② **书眉**（"Ebenezer Scrooge Ghost Hunter"——含书名且长于 dc:title）
         ——必须删，否则每章首行都是它。
    ⇒ 调用方用「与 dc:title 的关系」区分，见 main() 里的判定。
    """
    m = re.search(r'<head\b.*?</head>', raw, re.S | re.I)
    if not m:
        return ''
    tm = re.search(r'<title[^>]*>(.*?)</title>', m.group(0), re.S | re.I)
    if not tm:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', tm.group(1))).strip()


def clean(raw: str) -> str:
    t = strip_page_anchors(raw)          # 页码锚点须在标签还在时剥，否则数字粘进正文
    t = _fix_dropcap_markup(t)
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
    ap.add_argument("--strip-running-head", action="store_true",
                    help="剥掉 text 首行的出版商书眉（`<head><title>` = 书名+副标题，与 dc:title 不一致）。"
                         "⚠️ 默认关闭：全库 20 本书有恒定书名 title，开启会改变它们的 text/ 首行。")
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
    # ⚠️ 2026-10-01 修正：OPF 允许**带命名空间前缀**的 `<opf:item>` / `<opf:itemref>`
    # （epubcheck 合法形态；实测 Only a Monster 即为此形态）。
    # 原 `<item\b` / `<itemref\b` 不含前缀 ⇒ manifest 为空 ⇒ spine 全部 `continue`
    # ⇒ **静默「写入 0 章」**——工具不报错、不退出非零，最危险的 fail-open。
    for it in re.findall(r'<(?:[\w.-]+:)?item\b[^>]*/?>', opf):
        idm = re.search(r'id="([^"]+)"', it); hm = re.search(r'href="([^"]+)"', it)
        tm = re.search(r'media-type="([^"]+)"', it)
        if idm and hm: manifest[idm.group(1)] = (posixpath.normpath(posixpath.join(opf_path, unquote(hm.group(1)))), (tm.group(1) if tm else ''))

    # TOC 标签映射 href -> title
    #
    # ⚠️ 2026-09-30 修正：`labels[path] = ...` 是**无条件覆盖**，而一个 xhtml 常有多个
    # navPoint 指向它——章级一个 + 每个小节锚点一个（`<content src="09_Two.xhtml#_idParaDest-12"/>`）。
    # 覆盖 ⇒ 留下**最后一个**，即章内最后一节的小节标题，章标题被彻底顶掉。
    # 实测（I Can't Save You / Anthony Chin-Quee）12 件里 **4 件 slug 取自小节**：
    # 「two: A-Side—Success*」→ `ch04_track_3_plumbing`、「three: B-Side—The Fall」
    # → `ch05_track_7_falls_end`、「seven: Y'ain't (k)no(w)」→ `ch09_you_want_your_favorite_negro_dead`、
    # 「eight: Fatherhood」→ `ch10_lorisa`——**章名与文件名全错，且正文本身是对的**，
    # 不核对首行就发现不了（首行仍是正确的 "two / A-Side—Success*"）。
    # 修法：**章级 navPoint（src 无 `#` 锚点）优先**，锚点 navPoint 只在该文件没有任何章级项时兜底。
    labels, anchor_labels = {}, {}
    for n in z.namelist():
        if n.lower().endswith('.ncx'):
            ncx = z.read(n).decode('utf-8', 'ignore')
            # ⚠️ 2026-10-01：NCX 的 `navPoint` 也可能带命名空间前缀（实测本库已有此形态），
            # 原 `<navPoint ` 硬编码前缀 ⇒ 该文件**一个标签都取不到** ⇒ slug 回落到文件名。
            for blk in re.split(r'<[\w.-]*:?navPoint\b', ncx)[1:]:
                lm = re.search(r'<text>(.*?)</text>', blk); sm = re.search(r'<content\s+src="([^"]+)"', blk)
                if lm and sm:
                    href = html.unescape(sm.group(1))
                    key = posixpath.normpath(posixpath.join(opf_path, unquote(href.split('#')[0])))
                    (anchor_labels if '#' in href else labels)[key] = html.unescape(lm.group(1))
    for k, v in anchor_labels.items():
        labels.setdefault(k, v)

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
        'title page', 'half title', 'half title page',
        'copyright', 'copyright page', 'copyright-page', 'colophon', 'imprint',
        'contents', 'table of contents', 'toc', 'dedication',
        'acknowledgment', 'acknowledgments', 'acknowledgement', 'acknowledgements',
        'about the author', 'about the artist', 'also by', 'also by the author',
        'epigraph', 'index', 'resources', 'reading group guide', 'reader guide',
        'excerpt', 'newsletter', 'sign up', 'other titles', 'other books',
        'works by', 'selected bibliography', 'bibliography', 'notes', 'endnotes',
        'footnotes', 'praise for', 'about the publisher',
        # 同上实测补：尾注书目页标签就是裸 `Sources`（Their Shadows Deep ch76，
        # 14147 字符）。与 `notes` / `bibliography` 同类，非正文。
        'sources', 'source notes',
        # ⚠️ 2026-10-20 补（Ebenezer Scrooge 实测）：`Frontmatter` 页是**前置资料页**
        # （本书 = 1844–1853 年《Illustrated London News》的 WANTED 广告），
        # **不在出版商目录里**（toc.ncx 80 项无此条；Contents 页也不列），
        # 但出版商给了 `<section title="Frontmatter">` ⇒ 772 字符 > min_len 600
        # ⇒ 被当正文收成 ch01。`frontmatter` 是前置页的通用词，入名单。
        # ⚠️ **只收 frontmatter 两词，不收 prologue/foreword/preface**——
        #   本库至少 20 本书的 Prologue 是**正式正文章**（sweet-fury ch01、
        #   book-lovers ch02、dominion ch01、armor-for-liars ch01…），
        #   把 `prologue` 放进名单会让这些书**整章丢失**
        #   （回归实测：capture-by-amanda-lohrey 原 36 件，新版仍 36 件但
        #   ch35 整体错位一章 ⇒ 该页是正文不是装置页）。
        #   **前置页与正文章同名时，靠目录/章节标记区分，不靠名字区分。**
        # ⚠️ 2026-10-20：`characters` **不能进这张表**——回归实测 a-fatal-legacy-by-charlotte-vassell
        #   的**导航标签**就叫 `Characters`（页 = `s006-Foreword-01.xhtml`，
        #   `<section epub:type="frontmatter foreword">`，内容是人物表），
        #   进了本表 ⇒ 该页被整页丢掉（55 件 → 54 件）⇒ **存量书行为被改变**。
        #   ⇒ 改用**专用的 section title 名单**（见 DEVICE_SECTION）。
        'frontmatter', 'front matter',
    }
    # ⚠️ 2026-10-20：`<section title="...">` 专用的装置页名单。
    #   与 BOILER_LABEL 分开的原因：**同名的页在不同书里角色不同**——
    #   · ebenezer-scrooge 的 `<section title="Characters">`（07_Characters.xhtml）是
    #     纯人物表，**导航里没有条目** ⇒ 只能靠 section title 拦；
    #   · a-fatal-legacy 的 `Characters`（s006-Foreword-01.xhtml）**有导航条目**，
    #     且该页在存量 text/ 里是 ch01 ⇒ 拦掉会改变存量书。
    #   ⇒ 判据必须限定在「**section title** 命中」这一条，不碰导航标签路径。
    #   全库实测：section title 命中这两个词的**只有 ebenezer-scrooge 一本**。
    DEVICE_SECTION = {'characters', 'frontmatter', 'front matter'}
    # ⚠️ 2026-10-14 补「词族前缀」判据（Their Shadows Deep 实测）：
    # 精确匹配那次重写（2026-09-26）修掉了子串误判（`discover` ⊃ `cover` 静默丢章），
    # 却在另一侧留下反向漏网——名单里写的是**词族**（`praise for` / `also by` /
    # `about the`），而出版方 nav 标签带作者名／限定语：
    #   `Praise for Peter Golden` / `A Note on Sources` / `Sources`
    # 三件装置页全部精确匹配落空 ⇒ 被当正文收成 ch01 / ch77 / ch78（该书 78 件 vs
    # 目录页实测 Chapter 1–75 = 75 件），且**件数为偶数**的假账最难发现。
    # 只对下列**词族**放宽为前缀匹配，绝不退回全文子串搜索（那是 09-26 修掉的坑）：
    # 判据形如 `<族首词> …`（前缀 + 至少一个词），故 `Protocol` / `Stockholm`
    # 这类与族首词无边界关系的标题仍然不会被误判。
    BOILER_PREFIX = (
        'praise for', 'also by', 'about the', 'works by', 'a note on',
    )
    # 出版商固定文件名 + 导航文档 + 促销页 + 脚注/尾注页
    #
    # ⚠️ 2026-09-30 补 `foot-?notes?`：脚注页**不在 nav 里**（NCX 只列 33 项，脚注 25 页全无），
    # 于是 `labels` 取不到标签 → `is_boilerplate` 回退到正文首行兜底，首行是
    # 「* Stenosis is a medical word for…」，不在 BOILER_LABEL ⇒ **只能靠长度放行**。
    # 实测（I Can't Save You）25 个脚注页里 `34_Footnote.xhtml` 恰好 608 字符 > 600 min_len
    # ⇒ **一个脚注被当成 ch13 章**，而 `ch13_chap13.txt` 这个 slug 还会反过来掩盖它。
    # 脚注按库内既有约定属非正文（`xx_` 前缀，不占 ch 编号），须在路径层拦住。
    BOILER_PATH = re.compile(
        r'_(cov|tp|cop|ctc|toc|ded|ack|ata|rsc|excerpt|newsletter|promo|ssd|bmn|cue|int|nav|ncx)\d*_'
        r'|(^|[/_-])(nav|ncx|toc|next-?reads?|promo|advert|ads?|foot-?notes?|end-?notes?'
        r'|copyright-?page|title-?page|half-?title-?page|dedication)\.xhtml$', re.I)

    def _label_key(s):
        return re.sub(r'[^a-z0-9 ]+', ' ', (s or '').lower()).strip()

    def is_boilerplate(title, path, text_head):
        # ⚠️ nav 标签缺失时用**正文首行兜底**——否则装置页没有标签可测，
        # 只能靠长度放行（实测出版社促销页 "Discover your next great read!"
        # 无 nav 标签，1187 字符 > min_len，于是被当正文收进来）。
        lab = _label_key(title) or _label_key(text_head[:60])
        if lab in BOILER_LABEL or bool(BOILER_PATH.search(path)):
            return True
        return any(lab.startswith(fam + ' ') for fam in BOILER_PREFIX)

    def section_title(raw):
        """EPUB3 常见：`<section epub:type="chapter" title="Characters">`——
        出版商给每个分册的**结构性标题**。它比 nav 标签可靠（nav 常漏列前置页），
        且与正文内容无关（`title` 是元数据，不是正文里的字）。
        ⚠️ 只取**第一个** section 的 title：正文分册里后续 section 可能是节标题。
        """
        m = re.search(r'<section\b[^>]*\btitle="([^"]*)"', raw, re.I)
        return html.unescape(m.group(1)).strip() if m else ''

    # ⚠️ 2026-10-20：section title 的**装置页判据必须精确匹配**，不能走
    #   `is_boilerplate` 的「词族前缀」分支——前缀族里有 `a note on`，
    #   而 `A Note on Terminology`（a-wall-is-also-a-road 的尾页，3000 字符）
    #   是**正文级内容**（作者自述术语用法），不是装置页。
    #   回归实测：走 is_boilerplate 会把它整页丢掉（50 章 → 49 章）。
    #   ⇒ 装置页只认**精确标签**（与 BOILER_LABEL 同表）。
    def _is_device_title(stitle):
        if not stitle:
            return False
        return _label_key(stitle) in DEVICE_SECTION
    out_dir = a.out_dir or '.'
    os.makedirs(out_dir, exist_ok=True)
    written, skipped = [], []

    n = a.start
    for idref in re.findall(r'<(?:[\w.-]+:)?itemref\b[^>]*idref="([^"]+)"', opf):
        if idref not in manifest: continue
        path, mtype = manifest[idref]
        if 'html' not in mtype and not path.lower().endswith(('.html','.htm','.xhtml')): continue
        raw = z.read(path).decode('utf-8', errors='ignore')
        text = clean(raw)
        title = labels.get(posixpath.normpath(path), '')
        stitle = section_title(raw)
        head_title = head_title_of(raw)
        # ⚠️ 2026-10-20：装置页判据＝「nav 标签」或「section title」**精确命中**
        #   BOILER_LABEL（Characters / Frontmatter / Acknowledgements / About…）。
        #   ⚠️ **不用出版商的 h1 class 判定**——2026-10-20 回归实测否决：
        #     · `class="chapnuma"`（本想标"非正文章节页"）在 monstera-by-delilah-s-dawson
        #       里标的是 `38_Bloom.xhtml`——**那是一篇真故事**（987 字符，Romney/Ash 情节），
        #       按 class 判会把整篇丢掉（33 章 → 32 章）。
        #     · `class="chapnum"` 只说明"出版商认为是章"，不区分真章与版权页。
        #   ⇒ **只认"标签在装置页名单里"这一条**，其余按既有 nav + 长度判据。
        is_story = (len(text) > a.min_len
                    and not is_boilerplate(title, path.split('/')[-1], text)
                    and not _is_device_title(stitle))
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
            # ⚠️ 2026-10-20（Ebenezer Scrooge 实测）：**出版商把 running head 写进
            #   `<head><title>`**，且 `<title>` 与 dc:title **不一致**（本书
            #   `<title>Ebenezer Scrooge Ghost Hunter</title>` vs dc:title `Ebenezer Scrooge`），
            #   ⇒ 上面按 dc:title 的比对**不命中** ⇒ 每章 text 首行都是这条书眉。
            #   ⚠️ **该判据是 opt-in 的**（`--strip-running-head`），因为全库实测：
            #   **20 本书**的 `<title>` 是全书恒定的书名/副标题（sweet-spot / raising-ai /
            #   why-nothing-works / a-snake-among-swans / bruja-s-nest / capture /
            #   ebenezer-scrooge / fabulous-bodies / finding-darla / maybe-next-time /
            #   monstera / our-wives-under-the-sea / quaint-folk / the-splintered-sun /
            #   the-thrice-bound-fool / we-will-see-you-bleed / what-feeds-below /
            #   you-between-the-lines / red-ants / a-scholar-s-guide…），
            #   其中 why-nothing-works 的**仓库存好的 text/ 首行就是那条书名**
            #   ⇒ 默认开启会让 20 本书的 text/ 首行整体变化 ⇒ **改变存量书行为**，
            #   违反「工具改动不得影响其他书」的纪律。
            #   ⇒ 处置：**默认关闭**，需要时按书显式传 `--strip-running-head`。
            if not hit and a.strip_running_head and head_title:
                ht = re.sub(r'\s+', ' ', head_title).strip().lower()
                fl2 = re.sub(r'\s+', ' ', first).strip().lower()
                bt2 = re.sub(r'\s+', ' ', book_title).strip().lower() if book_title else ''
                # `<title>` 以 dc:title 开头（说明它是"书名 + 副标题"的书眉）
                # 且与 dc:title 不相等（否则是书名本身，走上面的判据）
                # 且 text 首行正是它 ⇒ 删
                if ht and fl2 == ht and bt2 and bt2 != ht and ht.startswith(bt2):
                    hit = True
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
