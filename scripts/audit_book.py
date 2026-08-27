#!/usr/bin/env python3
"""
audit_book.py — 一本书的一键总账（接任务定损 / 完工验收 / push 前巡检）

用法：
  python3 scripts/audit_book.py "<书目录>" [--save]

输出分四节：
  A. 库存对账 —— md 文件数 vs text/ 提取文件数（缺原文 = 精读在裸奔）
  B. 引文真实性 —— 复用 verify_quotes 的逐条指纹核对
  C. 格式门禁   —— frontmatter / 必备章节 / 五子项数量 / ■ 残留 / YAML 冒号炸弹
  D. 词汇与实体 —— check_vocab / check_entities 摘要
--save 时写入 docs/audits/<书名>-<日期>.md。
退出码：存在 fail 则非 0。
"""
import re, sys, glob, os, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import flat_alpha, epub_flat_text, extract_quotes
from check_vocab import load_corpus, check_book as vocab_check
from check_entities import check_book as entity_check

def find_epub(book_dir):
    epubs = glob.glob(os.path.join(book_dir, 'library', '*.epub'))
    return epubs[0] if epubs else None

def format_check(f, txt):
    issues = []
    if not txt.lstrip().startswith('---'):
        issues.append('缺 frontmatter')
    else:
        fm = txt.split('---', 2)[1] if '---' in txt[3:] else ''
        if '状态' not in fm: issues.append('frontmatter 缺 状态')
        if not re.search(r'modified\s*[:=]\s*"?20\d\d-\d\d-\d\d', fm): issues.append('frontmatter 缺 modified 日期')
    has_story = any(s in txt for s in ('## 故事梗概', '## 本章导航', '## 概览'))
    has_read  = ('## 逐句精读' in txt) or ('## 选择性精读' in txt) or ('## 精读' in txt)
    has_vocab = '## 词汇分级' in txt or '### ⭐' in txt
    has_summ  = '一句话总结' in txt
    for label, ok in [('梗概/概览节', has_story), ('精读节', has_read), ('词汇分级', has_vocab), ('总结', has_summ)]:
        if not ok: issues.append(f'缺「{label}」章节')
    n_quotes = len(extract_quotes(txt))
    n_five = len(re.findall(r'\*\*中文理解\*\*|- 中文理解|：中文理解', txt))
    if n_quotes and abs(n_five - min(n_quotes, 10)) > 1 and n_five < n_quotes:
        issues.append(f'五子项块数({n_five}) < 引语数({n_quotes})，疑有子项缺失')
    if '■' in txt: issues.append('含结束符 ■（规范禁止）')
    tm = re.search(r'^title\s*[:=]\s*(.+)$', txt, re.M)
    if tm and re.search(r"[:：?/'\"]", tm.group(1)) and not (tm.group(1).startswith('"') or tm.group(1).startswith("'")):
        issues.append('frontmatter title 含冒号/引号未加引号（YAML 炸弹）')
    return issues

def main():
    book_dir = sys.argv[1]
    save = '--save' in sys.argv
    name_short = os.path.basename(book_dir.rstrip('/'))
    epub = find_epub(book_dir)
    mds = sorted(glob.glob(os.path.join(book_dir, '*.md')))
    texts = sorted(glob.glob(os.path.join(book_dir, 'text', '*.txt')))

    print(f"# 审计报告：{name_short}")
    print(f"生成时间：{datetime.date.today().isoformat()}   工具：scripts/audit_book.py\n")

    print("## A. 库存对账")
    print(f"- md 文件：{len(mds)} 个")
    print(f"- text/ 提取件：{len(texts)} 个")
    status_a = '✅' if texts else '⚠️'
    print(f"- {status_a} {'原文已提取' if texts else '**text/ 为空——先跑 extract_chapters.py**'}")

    full = flat_alpha(epub_flat_text(epub)) if epub else ''

    # A2. text/ 语料一致性抽检（防语料污染：逐章取多点指纹回查 epub）
    def probe_text_dir(texts, epub_flat, probes=6, frag=40):
        results = []
        for tp in texts:
            ta = flat_alpha(open(tp, encoding='utf-8', errors='ignore').read())
            if len(ta) < frag * (probes + 1):
                results.append((os.path.basename(tp), 0, 1)); continue
            start0 = int(len(ta) * 0.15)
            # 探针 1 号取文件头（抓标题截断/头部拼接污染），其余均匀取样于中后段
            span = max(1, (len(ta) - start0) // (probes - 1)) if len(ta) > start0 + frag * probes else len(ta) - frag
            positions = [0] + [start0 + k * span for k in range(probes - 1)]
            hits = sum(1 for pos in positions
                       if ta[pos:pos + frag] in epub_flat)
            results.append((os.path.basename(tp), hits, probes))
        return results

    text_bad = []
    if texts and epub:
        probes = probe_text_dir(texts, full)
        suspicious = [(n, h, p) for n, h, p in probes if h < p - 1]
        print(f"- text/ vs epub 一致性抽检：{len(probes)-len(suspicious)}/{len(probes)} 文件通过")
        for n, h, p in suspicious:
            text_bad.append(n)
            print(f"  ⚠️ {n}: 语料命中率 {h}/{p}——提取件与 epub 出入大（疑污染/截断/异版本），逐章严格校验慎用此件")
    elif texts and not epub:
        print("- ⚠️ 无 epub，无法做语料一致性抽检")

    quote_fails, q_ok, q_total = [], 0, 0
    print("\n## B. 引文真实性（verify_quotes）")
    if not epub:
        print("- ⚠️ 未找到 library/*.epub，跳过")
    for f in mds:
        nm = os.path.basename(f)
        quotes = extract_quotes(open(f, encoding='utf-8').read())
        if not quotes:
            print(f"- {nm}: ⚠️ 无编号引语")
            continue
        ok = sum(1 for q in quotes if flat_alpha(q)[:52] in full)
        q_ok += ok; q_total += len(quotes)
        mark = '✅' if ok == len(quotes) else f'❌ ({ok}/{len(quotes)})'
        if ok != len(quotes): quote_fails.append(nm)
        print(f"- {nm}: {mark}" + (f" ✗ {full}" and ''))

    print("\n## C. 格式门禁")
    fmt_issues = []
    for f in mds:
        iss = format_check(f, open(f, encoding='utf-8').read())
        if iss:
            fmt_issues.append((os.path.basename(f), iss))
    print(f"- {'✅ 全部通过' if not fmt_issues else str(len(fmt_issues))+' 个文件有格式问题：'}")
    for nm, iss in fmt_issues:
        print(f"  ❌ {nm}: {'; '.join(iss)}")

    print("\n## D. 词汇表与实体")
    vres = vocab_check(book_dir)
    eres = entity_check(book_dir)
    print(f"- 词条行合计 {vres['rows']}；词汇 FAIL {len(vres['fails'])} / WARN {len(vres['warns'])}")
    for x in vres['fails'][:8]:
        print(f"    ❌ {x[0]}: {x[2]} 「{x[3][:40]}」")
    e_files = [x[0] for x in eres['fails']]
    print(f"- 实体未知文件 {len(e_files)} 个" + (f": {e_files}" if e_files else ""))

    print("\n## 结论")
    total_fail = bool(quote_fails or fmt_issues or vres['fails'] or eres['fails'] or not texts or text_bad)
    print(f"- 引文：{q_ok}/{q_total} 可核实")
    verdict = "❌ 存在 fail——不可作为验收通过" if total_fail else "✅ 全部通过"
    print(f"- 总判定：{verdict}")

    if save:
        os.makedirs('docs/audits', exist_ok=True)
        fn = f"docs/audits/{re.sub(r'[^\w]+','_',name_short)[:50]}-{datetime.date.today().isoformat()}.md"
        print(f"\n（--save 模式请用重定向保存：audit_book.py … > {fn}）")
    sys.exit(1 if total_fail else 0)

if __name__ == "__main__":
    main()
