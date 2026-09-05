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

# Pattern: ①/②… 圈数字 + optional quotes
CIRCLED_RE = re.compile(
    r'^(?:' + r'\*{0,2}[' + CIRCLED + r']' + r'\*{0,2})\s+["\u201c]?(.*?)["\u201d]?\s*$'
)
# Pattern: > **原句 N:** "..." or > **原句 N:** <text>
#   Handles any number of asterisks (0-3) around the label
YUAN_RE = re.compile(
    r'^>\s*(?:' + r'\*+' + r')?原句\s*(\d+)[:：]?\s*(?:' + r'\*+' + r')?\s+["\u201c]?(.*?)(?:["\u201d]?\s*)?$'
)
# Second口径: 标题「..."」引语
PLACE_RE = re.compile(r'^###\s+第(\d+)处[^「]*「([^」]+)」')

def extract_quotes(txt):
    """Return list of quote strings found in txt."""
    qs, seen = [], set()
    for raw in txt.splitlines():
        s = raw.rstrip()
        # Pattern 1: ①/②… 圈数字
        m = CIRCLED_RE.match(s)
        if m:
            b = m.group(1).strip().strip('*\'"\u201c\u201d\u2018\u2019').strip()
            if len(flat(b)) >= 20 and b not in seen:
                seen.add(b); qs.append(b)
            continue
        # Pattern 2: > **原句 N:** 裸文本或引号包裹
        m = YUAN_RE.match(s)
        if m:
            b = m.group(2).strip().strip('*\'"\u201c\u201d\u2018\u2019').strip()
            if len(flat(b)) >= 20 and b not in seen:
                seen.add(b); qs.append(b)
            continue
        # Pattern 3: ### 第N处：…「引语」
        pm = PLACE_RE.match(s)
        if pm:
            b = pm.group(2).strip()
            if len(flat(b)) >= 20 and b not in seen:
                seen.add(b); qs.append(b)
    return qs


def fragments(text):
    """Split text on …/.../... ; return list of non-trivial fragments."""
    return [p.strip() for p in re.split(r'…|\.\.\.', text)
            if len(re.findall(r'[A-Za-z0-9]', p)) >= 12]


def check_chapter(nn, md_path, text_dir):
    """Check one chapter. Returns (ok_count, total_count, miss_list)."""
    # Locate chapter text file
    cands = [os.path.join(text_dir, f'ch{nn:02d}.txt'),
             os.path.join(text_dir, f'ch{nn:02d}_')]
    tp = None
    for c in cands:
        if os.path.exists(c):
            tp = c; break
    if tp is None:
        matches = [f for f in os.listdir(text_dir)
                   if re.match(rf'^ch{nn:02d}_.*\.txt$', f)]
        if matches:
            tp = os.path.join(text_dir, matches[0])
    if tp is None:
        raise SystemExit(f'missing ch{nn:02d}*.txt in {text_dir}')

    chap_text = flat(open(tp, encoding='utf-8').read())
    qs = extract_quotes(open(md_path, encoding='utf-8').read())
    if not qs:
        return (0, 0, [], 'NO_QUOTES_EXTRACTED')

    ok, miss = 0, []
    for q in qs:
        fq = flat(q)
        frags = fragments(q)
        if fq[:60] in chap_text:
            ok += 1
        elif frags and all(flat(p)[:40] in chap_text for p in frags):
            # Each segment of a truncated quote must individually be found
            ok += 1
        else:
            miss.append(q[:80])
    return (ok, len(qs), miss, None)


def scan_book(book_dir, out_dir=None):
    """Scan all ch*.md files in book_dir."""
    text_dir = out_dir or os.path.join(book_dir, 'text')
    md_files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')))
    if not md_files:
        raise SystemExit(f'no ch*.md files found in {book_dir}')

    total_ok = total = 0
    failed_chapters = []
    for md in md_files:
        nn = int(re.match(r'ch(\d+)', os.path.basename(md)).group(1))
        ok, tot, miss, err = check_chapter(nn, md, text_dir)
        total_ok += ok; total += tot
        if err or miss:
            failed_chapters.append((nn, os.path.basename(md), ok, tot, miss, err))

    print(f'全章扫描: 解析引语块 {total}，命中本章 {total_ok}（{100*total_ok//max(1,total)}%）')
    if failed_chapters:
        print(f'\n--- 异常章节 ({len(failed_chapters)}) ---')
        for nn, name, ok, tot, miss, err in failed_chapters:
            if err:
                print(f'  ch{nn:02d} {name}: {err}')
            else:
                print(f'  ch{nn:02d} {name}: {ok}/{tot} ❌')
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
    ok, tot, miss, err = check_chapter(nn, md, text_dir)
    if err:
        print(f'NO_QUOTES_EXTRACTED')
        sys.exit(1)
    print(f'{os.path.basename(md)}: {ok}/{tot} in ch{nn:02d} text')
    for m in miss:
        print(f'  MISS: {m}')
    sys.exit(0 if ok == tot else 1)


if __name__ == '__main__':
    main()
