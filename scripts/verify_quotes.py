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

def flat_alpha(s) -> str:
    # 先剥掉引文里手写的段落转义符（\n/\t 会被指纹误读为字母 nn/tt）
    if not isinstance(s, str):
        return ''
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
        if body and not body.rstrip().endswith(('"', '"', "'", "'")):
            m2 = re.match(r'^["\u201c](.*?)[""”]\s*(?:[A-Za-z\u2014].{0,60})?$', body)
            if not m2:
                m2 = re.match(r'^(.*?)[""”]\s*(?:[A-Za-z\u2014].{0,60})?$', body)
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

# ── P0-1 「0 提取」按文件角色四类分派（2026-09-26，方案 §3.6）──────────────
# 原实现对「0 提取」只有一句 ⚠️ 后 continue，既不计入 bad 也不说明该不该管，
# 于是 168 个正文章节文件（涉 22 本书）长期静默跳过。§3.6 全库盘点实测：
#   非内容 6 / 概述类 209 / 金句·节点类 213（涉 160 本）/ 正文章节 168（涉 22 本）
# 四者性质不同，不能一律判失败。判定顺序不可颠倒。
RE_NONCONTENT = re.compile(
    r'审查报告|审查|review|handoff|index|索引|collab|协作|readme|'
    r'summary_log|gate_log|报告', re.I)
RE_OVERVIEW = re.compile(r'概述|综述|overview|全书概览|梗概', re.I)
RE_QUOTES = re.compile(r'金句|quotes?|情感节点|节点|emotional', re.I)
# 正文章节里的非章节文件（参考文献 / 贡献者名单 / 人物表等）——同样不该有引语
RE_BACKMATTER = re.compile(
    r'contributor|reference|bibliograph|^人物|角色|目录|contents|about|'
    r'acknow|appendix|glossar|list of books|works mentioned|index', re.I)

ROLE_SKIP, ROLE_ALLOW, ROLE_DEFER, ROLE_FAIL = 'skip', 'allow', 'defer', 'fail'


def classify_md(name: str) -> str:
    """按文件名角色返回 ROLE_* 之一。顺序即优先级（§3.6 判定链）。

    总览三篇（金句/节点/概述）判 ROLE_DEFER 而非 ROLE_FAIL——**这是对方案
    §3.6 表格「金句/节点类 0 = FAIL」的一处有意偏离**，依据：
      AGENTS 已知盲区表明写「verify_quotes 不覆盖 00_*.md 总览（须另跑
      verify_overview_quotes）」，即总览引语的主管门禁是 verify_overview_quotes。
      实测 chinas-world-view 的 `00_情感节点.md` 被 verify_overview_quotes
      以 22/22 ✅ 覆盖——若 verify_quotes 仍判它红，就是与另一门禁自相矛盾
      的假红。verify_quotes 无法知道姊妹门禁是否已覆盖，故只提示不判红。
    """
    if RE_NONCONTENT.search(name):
        return ROLE_SKIP
    if RE_OVERVIEW.search(name):
        return ROLE_ALLOW
    if RE_QUOTES.search(name):
        return ROLE_DEFER
    if RE_BACKMATTER.search(name):
        return ROLE_SKIP          # 正文章节里的 back-matter，同样排除
    return ROLE_FAIL


def main(book_dir: str, epub_path: str):
    full = flat_alpha(epub_flat_text(epub_path))
    total_ok = total = clean = bad = 0
    short_total = 0
    zero_fail = []               # (name, role) —— 0 提取且该角色应为 FAIL
    zero_allow = 0
    zero_defer = []              # 总览三篇：0 提取但不判红（转交 verify_overview_quotes）
    for f in sorted(glob.glob(os.path.join(book_dir, "*.md"))):
        name = os.path.basename(f)
        txt = open(f, encoding="utf-8").read()
        quotes, short = extract_quotes(txt)
        short_total += short
        if not quotes:
            role = classify_md(name)
            if short:
                print(f"{name}: ⚠️ 0 条长引语 + {short} 条短引语（<20字符，工具不校验，须人工 grep）")
            elif role == ROLE_SKIP:
                continue           # 非内容 / back-matter：本就不该有引语
            elif role == ROLE_ALLOW:
                zero_allow += 1
                print(f"{name}: ○ 0 提取（概述类，允许——散文体无编号引语块）")
            elif role == ROLE_DEFER:
                zero_defer.append(name)
            else:
                zero_fail.append((name, role))
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
    # ── P0-1 0 提取的角色分派结论 ──────────────────────────────────
    if zero_allow:
        print(f"\n○ 概述类 {zero_allow} 个文件 0 提取——按设计允许（散文体，无编号引语块）")
    if zero_defer:
        print(f"\n○ 总览三篇 {len(zero_defer)} 个文件 0 提取——**本工具不判红**"
              f"（总览引语主管门禁是 verify_overview_quotes）")
        for nm in zero_defer:
            print(f"    · {nm}  → 须由 verify_overview_quotes 覆盖；"
                  f"若它也 0 提取则该文件引语确实无人核实")
    if zero_fail:
        print(f"\n❌ P0-1：{len(zero_fail)} 个正文章节 0 提取（引语完全未被任何门禁核实）")
        for nm, role in zero_fail:
            print(f"    · {nm}")
        print("   注：0 提取也可能源于**解析器盲区**——本工具只认 ①-㉕ / "
              "「> **原句 N:**」/「> \"...\"」三种格式；")
        print("       裸 `> English` 整段式与 `- \"English\"` bullet 式抽不到"
              "（全库实测 75 个正文章节文件属此类，其引语从未被核实）。")
    print(f"\n=== 总计 {total_ok}/{total} 引文可核实（{round(total_ok/total*100) if total else 0}%）；完全干净文件 {clean}/{clean+bad}；正文章节 0 提取 {len(zero_fail)}；总览 0 提取转交 {len(zero_defer)} ===")
    sys.exit(0 if bad == 0 and total > 0 and not zero_fail else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
