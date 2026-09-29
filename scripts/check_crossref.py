#!/usr/bin/env python3
"""
check_crossref.py — 分析层交叉引用校验器

背景：verify_quotes/check_chapter_quotes/check_vocab 三道门禁都不管
"分析文字里 chNN '引语'" 是否指对章。Forest of Scars 审查 21 处缺陷中
16 处源于此（分析层 cross-ref 章号错/说话人错），Life and Death and
Giants 亦有 10 处同类——凭印象写 cross-ref = 凭记忆引语。

用法：
  python3 scripts/check_crossref.py "<书目录>" [--verbose]

原理：
  1. 扫描所有 ch*.md 的非引语行（分析/导航/总结层）；
  2. 正则抓 `chNN "quoted"` / `chNN "…quoted…"` 对（兼容中文引导的引用）；
  3. flat 比对引语片段是否存在于所指章的 text/chNN*.txt；
  4. 未命中 → 报警（附文件/行号/上下文，供人工读行复核——同行多引用
     会误配，报警不等于缺陷）。

局限（须人工复核的原因）：
  - 同一行多个 chNN 引用会与最近的引语错误配对；
  - 章内跨章叙事（如 "ch54 讲的手术" 无引语）不覆盖；
  - 中文理解/关键词子项内的合法引用同源，需人工判断。

Exit 0 = 零报警；Exit 1 = 有待人工复核的报警。
"""
import re, sys, os, glob, unicodedata

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())

# chNN + 引语（中英文引号均可，允许省略号）
XREF_RE = re.compile(
    # ⚠️ 2026-09-29 修正（Carmen and Grace 实测）：原式为 `chNN\s*[「"“]`，两处漏检
    #  ①`\s*` 只容许空白，**容不下中文引导词**——本库极常见的写法是
    #    「chNN 那句/那段/里的『…』」「与 chNN 成对阅读」，引号与 chNN 之间隔着
    #    2–8 个汉字。Carmen and Grace 31 条精确断言里 **29 条是这种写法**，
    #    原式对它们 0 命中，而作者据此以为"本层已覆盖" ⇒ 侥幸心理比没工具更危险。
    #  ②`{12,200}` 是**字符数**下限，把短引语整批滤掉：该书 11/31 条断言是
    #    6–11 字符的短句（"she was not home" / "Until you don't."）。
    #    阈值应按 flat 后的**字母数**给，且下限要低到能覆盖短句。
    # 间隔上限取 12 字是**实测定的**：再宽（如 30）会把「本章自己的引语 + 邻章编号」
    # 配成对，实测假阳性从 26/54 涨到不可用。
    r'ch(\d{1,3})[^，。；：\n]{0,12}?[「"“]([^」"”]{4,200})[」"”]'
)

def load_corpora(book_dir):
    corpora = {}
    for f in glob.glob(os.path.join(book_dir, 'text', 'ch*.txt')):
        m = re.match(r'ch(\d+)', os.path.basename(f))
        if m:
            corpora.setdefault(int(m.group(1)), []).append(flat(open(f, encoding='utf-8', errors='ignore').read()))
    return corpora

def main(book_dir, verbose=False):
    corpora = load_corpora(book_dir)
    if not corpora:
        raise SystemExit(f'no text/ch*.txt under {book_dir}/text')
    alerts = []
    checked = 0
    for f in sorted(glob.glob(os.path.join(book_dir, 'ch*.md'))):
        name = os.path.basename(f)
        if name.startswith('00_'):
            continue
        for lineno, line in enumerate(open(f, encoding='utf-8'), 1):
            s = line.strip()
            if s.startswith('> '):          # 引语行本身不在分析层口径
                continue
            for m in XREF_RE.finditer(s):
                nn = int(m.group(1))
                quoted = m.group(2)
                # ⚠️ 2026-09-29（两轮修正）：放宽间隔后正则会吃进**非英文**的「…」。
                # 第一轮只加「含 ≥2 连续字母」，仍漏中英混排；第二轮试「字母占比
                # > 0.34」也失败——实测反例：真引语 `Until you don't.` 占比 0.86，
                # 而 `在 Crater 之前，我们还有 Lumpling 和 Dumpling` 占比 **0.71**，
                # **占比根本区分不开**（专名多的中文串占比可以很高）。
                # 正判据是**引号内不得含中日韩字符**：本门禁比对的是英文小说的
                # 原文引语，凡含 CJK 即不是引语（多半是中文摘要/复述被引号包住）。
                if re.search(r'[\u3400-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]', quoted):
                    continue
                if not re.search(r'[A-Za-z]{2,}', quoted):
                    continue
                fp = flat(quoted)
                # 省略号分段：两侧都须命中所指章。
                # ⚠️ 2026-09-29：`len(flat(p)) >= 15` 把 <15 字母的短段整段丢弃，
                # 于是「省略号两侧」只要有一侧是短句就等于没校验。改按 8 字母起。
                segs = [p for p in re.split(r'…|\.\.\.', quoted)
                        if len(flat(p)) >= 8]
                pieces = segs if segs else [quoted]
                checked += 1
                corp_list = corpora.get(nn, [])
                ok = any(all(fp[:40] in c or flat(p)[:40] in c for p in pieces) for c in corp_list)
                if not ok:
                    alerts.append((name, lineno, nn, quoted[:70], s[:110]))
    print(f'交叉引用核对：{checked} 对，报警 {len(alerts)}')
    for name, lineno, nn, quoted, ctx in alerts:
        print(f'  ⚠️ {name}:{lineno} → ch{nn:02d} 查无「{quoted}…」')
        if verbose:
            print(f'      行：{ctx}')
    if alerts:
        print(f'\n⚠️ 报警须人工读行复核（同行多引用会误配）；确认后再判缺陷')
    sys.exit(1 if alerts else 0)

if __name__ == '__main__':
    main(sys.argv[1], '--verbose' in sys.argv)
