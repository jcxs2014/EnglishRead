#!/usr/bin/env python3
"""Strict per-chapter quote attribution checker.

Unlike verify_quotes.py (which searches the WHOLE epub and could pass a quote
lifted from a DIFFERENT chapter), this checks each quote block against THAT
chapter's own extracted text/chNN.txt only. This prevents cross-chapter
misattribution.

Supported quote formats:
  ① "..."               ①②③④⑤⑥⑦⑧⑨⑩ 圈数字 + 引号包裹
  > **原句 N:** "..."   引号包裹（任何格式）
  > **原句 N:** <text>  无引号裸文本（Ligotti 短篇合集格式）
  ### 第N处：标题「...」引语（第二个口径，不单独计 PASS/FAIL）

省略号/…分段容忍：引语含省略号时，每段都必须命中本章才算 PASS。

用法：
  python3 scripts/check_chapter_quotes.py <NN> "<md_file_path>" [--out-dir <text_dir>]
  python3 scripts/check_chapter_quotes.py --book-dir <book_dir>  # 全书逐章扫描

Exit 0 = all quotes found in their own chapter text.
Exit 1 = at least one MISS.
"""
import re, sys, os, glob

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'
flat = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())


# ── P0-5 首/尾词吞词检测（2026-09-26，方案 §3.2）────────────────────────
# 病根：flat 删掉所有非字母数字后做**子串**判定，于是
#     md   : "Hate it here. Will you take me away with you"
#     原文 : "I hate it here. Will you take me away with you"
# flat 后前者是后者的子串 → verify_quotes 与本工具**双双 1/1 ✅ 放行**，
# 而真实缺陷是引语首词 "I" 被吞。§3.2 实证：Forgotten Sisters 批次。
#
# 修法：判定加**词边界**。注意两条约束——
#   ① 边界必须在**原文**上判，不能在 flat 串上判（flat 串每字符皆字母数字，
#      边界恒假——与 verify_corpus 第一版 has_token 同一个坑）；
#   ② **破折号不并词**：`word—word` flat 后成 `wordword`，若按 flat 串
#      判边界会把破折号处误判成"词中间"，须把非字母数字一律视为词边界。
def flat_with_bounds(s):
    """返回 (flat串, 边界数组, 原文字引数组)。

    - 边界数组[i] 为 True 表示 flat 串第 i 字符在**原文**里是一个新词的
      开头（前一个非字母数字字符，或位于串首）
    - 原文字引数组[i] 给出该 flat 字符在原文中的下标，用于报告时打印
      原文上下文——因为「md 首词被吞」与「text/ 把两个词粘连」在 flat 串上
      **表现完全相同**（实测 living-on-paper ch21 的 `IPlease forgive`：
      md 引语是对的，是 text/ 提取件把 I 与 Please 粘住了），只有原文能分辨。
    """
    out, bnd, orig = [], [], []
    prev_alnum = False
    for idx, ch in enumerate(s.lower()):
        if 'a' <= ch <= 'z' or '0' <= ch <= '9':
            out.append(ch)
            bnd.append(not prev_alnum)
            orig.append(idx)
            prev_alnum = True
        else:
            # 任何非字母数字都断词——含破折号/连字符（破折号不并词）
            prev_alnum = False
    return ''.join(out), bnd, orig


def boundary_clean_positions(chap_flat, chap_bnd, needle):
    """needle 在 chap_flat 中所有出现位置里，返回「词边界干净」的那些位置。

    - 首端：位置 >0 时要求 chap_bnd[pos] 为 True（否则首词被吞）
    - 尾端：仅当整条引语（而非 60 字符前缀）被匹配时才检查，
            因为前缀截断必然停在词中间，据此判「尾词被截断」必然假红
    """
    if not needle:
        return []
    hits, i = [], chap_flat.find(needle)
    while i != -1:
        ok = (i == 0) or chap_bnd[i]
        if ok:
            hits.append(i)
        i = chap_flat.find(needle, i + 1)
    return hits


def tail_boundary_ok(chap_flat, chap_bnd, start, length):
    """整条引语匹配后，尾端是否落在词边界上。"""
    end = start + length
    if end >= len(chap_flat):
        return True                      # 匹配到文末，尾端天然完整
    return chap_bnd[end]

# Pattern: ①/②… 圈数字 + optional quotes
CIRCLED_RE = re.compile(
    r'^(?:>\s*)?(?:\*{0,2}[' + CIRCLED + r']\*{0,2})\s+["\u201c]?(.*?)["\u201d]?\s*$'
)
# Pattern: > **原句 N:** "..." or > **原句 N:** <text>
#   Handles any number of asterisks (0-3) around the label
YUAN_RE = re.compile(
    r'^>\s*(?:' + r'\*+' + r')?原句\s*(\d+)[:：]?\s*(?:' + r'\*+' + r')?\s+["\u201c]?(.*?)(?:["\u201d]?\s*)?$'
)
# Second口径: 标题「..."」引语
PLACE_RE = re.compile(r'^###\s+第(\d+)处[^「]*「([^」]+)」')

ROMAN_RE = re.compile(r'^>\s*(.+)$')  # 言情无编号 blockquote（引号行或裸叙述行；Up in Molten Lights 实证 0/0 盲区）

def extract_quotes(txt):
    """Return (quotes, short_count)."""
    qs, seen = [], set()
    short = 0
    for raw in txt.splitlines():
        s = raw.rstrip()
        b = None
        # Pattern 1: ①/②… 圈数字
        m = CIRCLED_RE.match(s)
        if m:
            b = m.group(1)
        else:
            # Pattern 2: > **原句 N:** 裸文本或引号包裹
            m = YUAN_RE.match(s)
            if m:
                b = m.group(2)
            else:
                # Pattern 4: 言情无编号 blockquote（2026-09-06 增补）
                m = ROMAN_RE.match(s)
                if m:
                    b = m.group(1)
                    # 引号行：剥掉引号外的叙述标签 `"..." he said.`
                    if b.lstrip().startswith(('"', '\u201c')) and not b.rstrip().endswith(('"', '\u201d', "'", '\u2019')):
                        m2 = re.match(r'^["\u201c](.*?)[\u201d"]\s*(?:[A-Za-z].{0,60})?$', b)
                        if m2:
                            b = m2.group(1)
        if b is None:
            # Pattern 3: ### 第N处：…「引语」
            pm = PLACE_RE.match(s)
            if pm:
                b = pm.group(2)
            else:
                continue
        b = b.strip().strip('*\'"\u201c\u201d\u2018\u2019 ').strip()
        fb = len(flat(b))
        if fb < 20:
            if fb >= 5:
                short += 1   # 短引语：计数，提示人工 grep
            continue
        if b not in seen:
            seen.add(b); qs.append(b)
    return qs, short


def fragments(text):
    """Split text on …/.../... ; return list of non-trivial fragments."""
    return [p.strip() for p in re.split(r'…|\.\.\.', text)
            if len(re.findall(r'[A-Za-z0-9]', p)) >= 12]


def check_chapter(nn, md_path, text_dir):
    """Check one chapter.

    Returns (ok_count, total_count, miss_list, err, short, swallowed)。
    `swallowed` 是 P0-5 新增：引语 flat 后能在本章命中、但命中位置落在原文
    **词中间**（首词被吞）或尾端停在词中间（尾词被截断）者。§3.2 实证这类
    缺陷过去被两个工具双双 1/1 ✅ 放行。
    """
    # Resolve chapter number from frontmatter source_text if present
    # 2026-09-28 修正 `ch18a` 类编号冲突：原代码把字母后缀丢掉，
    # `ch18a the cop…md` 被拿去比对 `ch18_oh_whistle….txt` ⇒ 10/10 真实引语
    # 全判 MISS（假红型）。改为整段携带后缀。
    actual_nn = nn
    suffix = ''
    try:
        with open(md_path, encoding='utf-8') as f:
            content = f.read()
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                fm_text = content[3:end]
                # Simple regex parse for source_text: chNN[字母后缀]
                m_st = re.search(r'source_text:\s*[\'"]?(ch\d+[a-z]?)', fm_text)
                if m_st:
                    m_num = re.match(r'(\d+)([a-z]?)', m_st.group(1))
                    if m_num:
                        actual_nn = int(m_num.group(1))
                        suffix = m_num.group(2)
        if not suffix:
            # 文件名里的后缀同样有效（md 名与 text 名都带 ch18a）
            m_fn = re.match(r'ch(\d+)([a-z]?)', os.path.basename(md_path))
            if m_fn and int(m_fn.group(1)) == actual_nn:
                suffix = m_fn.group(2)
    except Exception:
        pass

    # Locate chapter text file
    # ⚠️ 位数不能写死为 2：111 章的书用 ch001–ch111 三位号，写死 `f'{nn:02d}'`
    # 会让 tag 与文件名系统性错位（ch009 → '09'，而磁盘上是 'ch009_'），
    # 结果是**每一章都 SystemExit**——逐章归属这道门禁直接失效且不报错。
    # 做法：依次试 2/3/4 位，取第一个能在 text/ 命中的；命中即用。
    for width in (2, 3, 4):
        tag = f'{actual_nn:0{width}d}{suffix}'
        cands = [os.path.join(text_dir, f'ch{tag}.txt'),
                 os.path.join(text_dir, f'ch{tag}_')]
        tp = None
        for c in cands:
            if os.path.exists(c):
                tp = c; break
        if tp is None:
            matches = [f for f in os.listdir(text_dir)
                       if re.match(rf'^ch{tag}_.*\.txt$', f)]
            if matches:
                tp = os.path.join(text_dir, matches[0])
        if tp is not None:
            break
    if tp is None:
        raise SystemExit(f'missing ch{tag}*.txt in {text_dir} (source_text from ch{nn:02d}{suffix})')

    raw_chap = open(tp, encoding='utf-8').read()
    chap_text, chap_bnd, chap_orig = flat_with_bounds(raw_chap)
    qs, short = extract_quotes(open(md_path, encoding='utf-8').read())
    if not qs:
        if short:
            return (0, 0, [], f'NO_LONG_QUOTES ({short} 短引语未校验，须人工 grep)', short, [])
        return (0, 0, [], 'NO_QUOTES_EXTRACTED', short, [])

    ok, miss, swallowed = 0, [], []
    for q in qs:
        fq = flat(q)
        frags = fragments(q)
        head = fq[:60]
        hits = boundary_clean_positions(chap_text, chap_bnd, head)
        if hits:
            # P0-5：整条引语（未被 60 字符前缀截断）才检查尾端边界
            if len(head) < len(fq) or tail_boundary_ok(
                    chap_text, chap_bnd, hits[0], len(head)):
                ok += 1
            else:
                p0 = hits[0]
                ej = p0 + len(head)
                oi = chap_orig[ej] if ej < len(chap_orig) else len(raw_chap)
                ctx = re.sub(r'\s+', ' ', raw_chap[max(0, oi - 18):oi + 24]).strip()
                swallowed.append((q[:80], '尾词被截断', f'原文：…{ctx}…'))
            continue
        # 前缀匹配上了但**所有出现位置都在词中间**（§3.2）
        if head and head in chap_text:
            p0 = chap_text.find(head)
            oi = chap_orig[p0] if p0 < len(chap_orig) else 0
            ctx = re.sub(r'\s+', ' ', raw_chap[max(0, oi - 24):oi + 18]).strip()
            swallowed.append((
                q[:80],
                '首词被吞或 text/ 粘连（flat 命中落在原文词中间）',
                f'原文：…{ctx}…'))
            continue
        # ── 截短引语（真含省略号）才走片段通道 ──
        # ⚠️ 2026-09-28 The Paris Deception ch01 实证假绿：`fragments()` 只按 …/... 切，
        # 于是**无省略号的引语也被切成一整个 fragment**（`frags == [整条]`），
        # 本分支遂退化为「前 40 flat 字符命中即算通过」——只要引语开头约八个词对得上，
        # 后面改成什么（甚至把 grime 拼成 grimo 这种非逐字形）都照样报 OK。
        # 实测：投毒 `in the grime where` → `in the grimo where`，
        # 本工具报 7/7、verify_quotes 也报 7/7（52 指纹在错误点之前就截断了），
        # 只有 sweep_full 整串比对抓到。**`len(frags) > 1` 是「真截短」的必要条件**，
        # 不是可选优化——它把「片段前缀检查」这道兜底闸门还给省略号引语专用。
        if len(frags) > 1 and all(flat(p)[:40] in chap_text for p in frags):
            # Each segment of a truncated quote must individually be found
            ok += 1
        else:
            miss.append(q[:80])
    return (ok, len(qs), miss, None, short, swallowed)


def scan_book(book_dir, out_dir=None):
    """Scan all ch*.md files in book_dir."""
    text_dir = out_dir or os.path.join(book_dir, 'text')
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))
    if not md_files:
        raise SystemExit(f'no ch*.md files found in {book_dir}')

    total_ok = total = 0
    short_total = 0
    failed_chapters = []
    all_swallowed = []
    for md in md_files:
        m_nn = re.match(r'ch(\d+)([a-z]?)', os.path.basename(md))
        nn = int(m_nn.group(1))
        ok, tot, miss, err, short, swallowed = check_chapter(nn, md, text_dir)
        total_ok += ok; total += tot; short_total += short
        for it in swallowed:
            all_swallowed.append((nn, os.path.basename(md)) + it)
        # P0-5 的吞词**不计入 failed_chapters**（不翻转退出码）：命中位置在
        # 词中间有两种成因——md 引语真的吞了词，或 text/ 提取件把两个词粘连。
        # 二者在 flat 串上表现完全相同，工具无法分辨。实测 living-on-paper
        # ch21 属后者（原文 `IPlease forgive`，md 引语是对的），若据此判红
        # 就是「md 没毛病却门禁变红」的假红。故只报不改退出码，由人裁决；
        # 语料成因走 verify_corpus（P0-0），引语成因改 md。
        if err or miss:
            failed_chapters.append(
                (nn, os.path.basename(md), ok, tot, miss, err, swallowed))
    if short_total:
        print(f'\u26a0\ufe0f  全书共 {short_total} 条短引语（<20 flat 字符）未被校验\u2014\u2014按规则须人工 grep 兜底')

    print(f'全章扫描: 解析引语块 {total}，命中本章 {total_ok}（{100*total_ok//max(1,total)}%）')
    if all_swallowed:
        print(f'\n--- P0-5 首/尾词吞词 ({len(all_swallowed)}) ---')
        print('    flat 子串能在本章命中，但命中位置落在原文**词中间**。这类缺陷过去被')
        print('    verify_quotes 与本工具双双 1/1 ✅ 放行（方案 §3.2）。破折号不并词，')
        print('    故 em-dash 处的 flat 连续不算吞词。')
        print('    ⚠️ **不翻转退出码**：成因有二且工具无法分辨——')
        print('       ① md 引语首词被吞 → 改 md；② text/ 提取件把两词粘连 → 走')
        print('          verify_corpus（P0-0）。实测 living-on-paper ch21 属②，')
        print('       md 引语无误；据此判红即假红。请对照下方「原文」一行裁决。')
        for nn, name, q, why, ctx in all_swallowed[:20]:
            print(f'  ch{nn:02d} {name}: {why}')
            print(f'      md  ：「{q}」')
            print(f'      {ctx}')
    if failed_chapters:
        print(f'\n--- 异常章节 ({len(failed_chapters)}) ---')
        for nn, name, ok, tot, miss, err, swallowed in failed_chapters:
            if err:
                print(f'  ch{nn:02d} {name}: {err}')
            else:
                tag = '❌' if miss else '⚠️'
                print(f'  ch{nn:02d} {name}: {ok}/{tot} {tag}')
                for m in miss[:3]:
                    print(f'      MISS: {m}')
        return 1
    print('✅ 全部引语均归属正确章节')
    return 0


def main():
    args = sys.argv[1:]
    out_dir = None
    if '--out-dir' in args:
        i = args.index('--out-dir')
        out_dir = args[i + 1]
        del args[i:i + 2]

    # --book-dir mode: scan whole book
    if '--book-dir' in args:
        i = args.index('--book-dir')
        book_dir = args[i + 1]
        del args[i:i + 2]
        sys.exit(scan_book(book_dir, out_dir))

    if len(args) < 2:
        raise SystemExit(f'Usage: {sys.argv[0]} <NN> "<md_file>" [--out-dir <dir>] [--book-dir <book_dir>]')

    nn = int(args[0])
    md = args[1]
    text_dir = out_dir or os.path.join(os.path.dirname(os.path.abspath(md)), 'text')
    ok, tot, miss, err, short, swallowed = check_chapter(nn, md, text_dir)
    if err:
        print(err)
        sys.exit(1)
    note = f'（另有 {short} 条短引语未校验）' if short else ''
    print(f'{os.path.basename(md)}: {ok}/{tot} in ch{nn:02d} text{note}')
    for m in miss:
        print(f'  MISS: {m}')
    for it in swallowed:
        q, why = it[0], it[1]
        print(f'  P0-5 {why}：「{q}」')
        if len(it) > 2:
            print(f'      {it[2]}')
    sys.exit(0 if ok == tot else 1)   # P0-5 不翻转退出码（见 scan_book 注释）


if __name__ == '__main__':
    main()
