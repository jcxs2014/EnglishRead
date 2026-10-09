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

# 印张页码锚点（epub 的 doc-pagebreak）。**必须在标签还完整时剥**：剥标签后
# 数字会与正文粘连（The Moon Papers 实证 `saw 12them` / `204and` / `281Then` 约百处）。
# 源形态（两种配对）：
#   <span aria-labelledby="pg12" epub:type="pagebreak" id="page_12" role="doc-pagebreak"/>
#   <span hidden="hidden" id="pg12">12</span>
# 页码不是正文，两侧（epub 参照集与 text/ 提取件）必须同口径，否则跨页引语必假 MISS。
PAGE_ANCHOR_RES = (
    re.compile(r'<(?:span|a|div|p)\b[^>]*(?:epub:type="pagebreak"|role="doc-pagebreak")[^>]*/?>'
               r'(?:[^<]{0,16}</(?:span|a|div|p)>)?', re.I),
    re.compile(r'<(\w+)\b[^>]*\bid="pg[a-z0-9]+"\b[^>]*>\s*[0-9]{1,4}\s*</\1>', re.I),
    re.compile(r'<(\w+)\b[^>]*\bhidden="hidden"[^>]*>\s*[0-9]{1,4}\s*</\1>', re.I),
)

def strip_page_anchors(t: str) -> str:
    for rx in PAGE_ANCHOR_RES:
        t = rx.sub('', t)
    return t

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
    t = strip_page_anchors(t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\u00a0', ' ')
    return t

def extract_quotes(txt: str, include_short: bool = False):
    """按行提取候选引文，兼容多种书写顺序；同文本去重保序。

    `include_short=True` 时把 <20 flat 字符的短引语也一并放进返回值（默认
    False，主门禁行为不变）。短引语平时只计数不返回，故**外部无从核对**——
    check_short_quotes.py 靠这个开关把它们捡回来。

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
    # ⚠️ 分支顺序 = HEAD 原序，**不要重排**（2026-09-30 五步审查教训，见下）
    # 逐分支试匹配只为记住命中的是哪一支，供 need_strip 判断
    _BR = ((r'^[' + CIRCLED + r']\s+(.+)$',                     'circ_bare'),
           (r'^\*{1,2}[' + CIRCLED + r']\*{1,2}\s+["\'](.*)["\']', 'circ_bold'),
           (r'^[' + CIRCLED + r']\s+["\'](.*)["\']',             'yuanku'),
           (r'^>\s*\*{0,2}原句\s+\d+[:：]?\s*\*{0,2}(?:\s+(.+))?$', 'yuanju'),
           (r'^>\s*[""](.+)$', 'yanqing'))   # 言情无编号 blockquote
    # 教训：审查期曾把「带引号的圈数字」两支提到 circ_bare 之前，想让剥离更准，
    # 结果 `yuanku` 的 `(.*)` 紧跟 `["\']` 时贪婪退化为**最短**匹配
    # （`⑥ "No." It would…` 只取到 `No.`）⇒ 全库 16 本书共丢引语。
    # 结论：修工具只改**必要的那一处**，分支顺序一动就要全库回归证明。
    lines = txt.splitlines()
    for idx, raw in enumerate(lines):
        s = raw.strip()
        m = br = None
        for pat, name in _BR:
            mm = re.match(pat, s)
            if mm:
                m, br = mm, name
                break
        if not m:
            continue
        body = (m.group(1) or '').strip()
        # ⚠️ **`yuanju`（`原句 N:`）分支不剥叙述标签**（2026-09-30 An Army like No Other 五步审查修）
        # 原实现对所有分支无差别剥壳，误伤了 `原句 N:` 行里**句中带引号对、末尾不带引号**的引语
        # —— 那是本库非虚构/论述格式的常态（An Army 实测 150 条里 9 条被截断）：
        #   实测 `Israel refers to wars as "operations," a practice that normalizes them…`
        #        被抽成 `Israel refers to wars as `（24 flat 字符 ≥20，照样「通过」）
        # ⇒ 门禁那 100% 里有一部分验的不是作者写的引语，而是它的截断版。
        # 纪律依据：新书启动模板「审查过程自身四条纪律」第 3 条（报告为 0/100% 时先怀疑脚本）。
        # ⚠️ 2026-10-08 修复：当 yuanju header 同行无内容时，合并下一行的 `> content` 行
        if br == "yuanju" and not body:
            # 找下一个非空且以 `> ` 开头的行，合并其内容
            for nxt_idx in range(idx + 1, len(lines)):
                nxt = lines[nxt_idx].strip()
                if not nxt:
                    continue
                if nxt.startswith('>'):
                    body = nxt.lstrip('> ').strip()
                break
        need_strip = br != 'yuanju' and not body.rstrip().endswith(('"', '"', "'", "'"))
        if need_strip:
            m2 = re.match(r'^["\u201c](.*?)["""]\s*(?:[A-Za-z\u2014].{0,60})?$', body)
            if not m2:
                m2 = re.match(r'^(.*?)["""]\s*(?:[A-Za-z\u2014].{0,60})?$', body)
            if m2:
                body = m2.group(1)
        # 剥掉包裹性的粗体/斜体/引号字符（内容级引语完整性交给指纹比对判断）
        # 2026-09-29 修正（The Last Lifeboat 总览批次实测）：先剥行尾的 `（chNN）`
        # 章号标注——`strip` 字符集不含括号，标注会留在引语体内；`① "'Pneumonia.'"
        # （ch52）` 曾被抽出 `Pneumonia.'"（ch52）`（带尾引号+标注）⇒ flat 查无
        # ⇒ check_short_quotes 报「全书查无」。**根因是剥壳顺序，不是引语有问题。**
        body = re.sub(r'[（(]\s*ch\d+\s*[）)]\s*$', '', body).strip()
        body = body.strip('*')
        body = body.strip('\'"""'' ')
        fa = len(flat_alpha(body))
        if fa < 20:
            if fa >= 5:
                short += 1   # 有英文内容但太短——计数，提示人工核
            # `include_short=True` 时把短引语也放进 quotes（check_short_quotes
            # 要逐条核对它们）。默认 False ⇒ 主门禁行为**逐字不变**。
            if include_short and body not in seen:
                seen.add(body)
                quotes.append(body)
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


# ── P0-6 --full：全串 flat 比对 + fragment 分段取证（2026-09-26，方案 §三.1）──
# 病根：常规判定只取 flat_alpha(q)[:52] 作指纹——**前 52 个字符之后的内容
# 从未被比对**。引语若在第 53 字符之后被改写/拼接/张冠李戴，指纹仍命中放行。
# §三.1 实测：4 本书 11 处。--full 打开后补一次整串比对；整串不命中时按
# fragment 分段取证，把「哪一段对不上」落到具体位置而非一句 MISS。
# 尾部编辑性标注（金句/节点类常写 `⑥ "…"（ch04）`）。这类标注是**出处标记**、
# 本就不该出现在 epub 里；若不剥掉，--full 整串比对会把它当成"对不上"——
# 实测 why-we-die 35 条取证里绝大多数是 `（ch04）` 造成的假取证。默认 52 字符
# 口径因标注位于尾部、超出指纹长度而一直没能暴露它。
RE_TRAIL_ANNOT = re.compile(
    r'[\(（\[【]\s*(?:ch\d+|第[一二三四五六七八九十百\d]+[章节]|[^)\s]{0,12}章)\s*'
    r'[\)）\]】]\s*$'
    r'|\s*[—–\-]{1,2}\s*(?:ch\d+|p{1,2}\.?\s*\d+)\s*$', re.I)


def _strip_trailing_annot(q):
    """剥掉引语尾部的章节/页码标注，返回 (清理后文本, 是否被剥)。"""
    t = q.rstrip()
    m = RE_TRAIL_ANNOT.search(t)
    if not m:
        return q, False
    return t[:m.start()].rstrip(), True


def _p06_probe(q, full, frag_evidence, name):
    """P0-6 深检：指纹（前 52 字符）已命中，补一次真正的内容比对。

    两种情形必须分开，否则全是假取证：
      ① 引语**无省略号** → 整串 flat 比对（尾部出处标注先剥掉）
      ② 引语**有省略号** → AGENTS 允许 `…` 跳过中间文字，故整串比对无意义；
         改为**逐段整串比对**（默认口径只比每段前 40 字符，同样有盲区）。
         实测 all-our-yesterdays ch18、one-way-back ch21/ch30 均属此类。
    """
    q_clean, stripped = _strip_trailing_annot(q)
    # 复合引语（对话与叙述交织、多段引号）：整串比对无意义。默认口径有
    # 「引号分段回退」，但只比每段**前 40 字符**，同样有盲区——故 --full
    # 对复合引语改为**逐段整串比对**。实测 that-first-flight 6 条取证全是
    # 此类（ch04 把 "And my name is Oliver." 与 "Macey." 两段对白中间的
    # 叙述省略后直接相接），不是造假。
    qsegs = [x for x in re.findall(r'[""]([^""]{12,})[""]', q_clean)]
    if len(qsegs) >= 2:
        for seg in qsegs:
            fs = flat_alpha(seg)
            if len(fs) >= 15 and fs not in full:
                bad = _first_bad_fragment(seg, full)
                frag_evidence.append(
                    (q[:70], bad if bad else (0, fs[:40]), stripped))
                return
        return
    if '…' in q_clean or '...' in q_clean:
        for seg in re.split(r'…|\.\.\.', q_clean):
            fs = flat_alpha(seg)
            if len(fs) < 15:
                continue
            if fs not in full:
                bad = _first_bad_fragment(seg, full)
                frag_evidence.append(
                    (q[:70], bad if bad else (0, fs[:40]), stripped))
                return
        return
    fa = flat_alpha(q_clean)
    if fa and fa not in full:
        frag_evidence.append((q[:70], _first_bad_fragment(q_clean, full), stripped))


def _first_bad_fragment(q, full, win=40, step=15):
    """返回首个不命中的 fragment 及其在引语中的字符偏移；全命中返回 None。"""
    fa = flat_alpha(q)
    if not fa:
        return None
    off = 0
    while off < len(fa):
        piece = fa[off:off + win]
        if len(piece) >= 12 and piece not in full:
            return (off, piece)
        off += step
    return None



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


def main(book_dir: str, epub_path: str, full_mode: bool = False):
    # ⚠️ 2026-09-27 加 epub 缺失守卫（对齐 check_anchor 的「❓ 无法判定」惯例）
    # 原行为：epub 路径不存在 → epub_flat_text 返回 ""→ 每条引语都判「查无」
    # → 输出「0/N 引文可核实（0%）」，读起来像「全部伪造」，而这其实是「根本没查」。
    # 与 audit 无关，属脚本假阴性；修法：缺参照集即退出码 2 且不产出任何计数。
    if not epub_path or not os.path.isfile(epub_path):
        print("❓ 无法判定：epub 不存在 — %s" % (epub_path or "(空)"))
        print("   本书无参照集 ⇒ 引语逐字这一层**未检查**，不是「引语有问题」。")
        print("   处置：按 AGENTS 第 3 条 lane 表记「降级 lane」；逐章归属改跑 check_chapter_quotes.py。")
        sys.exit(2)
    full = flat_alpha(epub_flat_text(epub_path))
    total_ok = total = clean = bad = 0
    short_total = 0
    zero_fail = []               # (name, role) —— 0 提取且该角色应为 FAIL
    zero_allow = 0
    zero_defer = []              # 总览三篇：0 提取但不判红（转交 verify_overview_quotes）
    all_frag_evidence = []       # P0-6：--full 下「指纹过但整串对不上」的引语
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
        frag_evidence = []      # P0-6 取证：指纹过但整串对不上的引语
        for q in quotes:
            # 尾部出处标注（`（ch12）` / `[chNN]` / `——ch04` / `p.12`）是**编辑性
            # 标记**，永不属于引语内容。原实现只在 --full 路径剥离，默认 52 字符
            # 路径不剥 → 短引语（>20 flat 字符会被校验）带着标注就判红。
            # 实测 what-grows-in-the-dark `00_情感节点.md` 两条：`（ch12）`、
            # `（ch30）` 剥离后均命中，原样均查无。标签层归 verify_overview_quotes
            # 管（它同样不剥，见其盲区），但引语层必须剥——否则是假红。
            q_body, _stripped = _strip_trailing_annot(q)
            qa = flat_alpha(q_body)
            frag = qa[:52]
            if frag in full:
                ok += 1
                if full_mode and len(qa) > 52:
                    _p06_probe(q, full, frag_evidence, name)
                continue
            # 引号分段回退：`"A" tag "B"` 跨标签行拆引号内各段独立验证
            # （对话体跨标签实证——flat 指纹跨标签必 MISS）
            qparts = re.findall(r'["\u201c]([^"\u201d]{12,})["\u201d]', q_body)
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
        if frag_evidence:
            all_frag_evidence.extend((name,) + t for t in frag_evidence)
        total_ok += ok
        total += len(quotes)
        note = f"（另有 {short} 条短引语未校验）" if short else ""
        if ok == len(quotes):
            clean += 1
            print(f"{name}: {ok}/{len(quotes)} ✅{note}")
        else:
            bad += 1
            print(f"{name}: {ok}/{len(quotes)} ❌{note}")
            for m in miss[:5]:
                print(f"    ✗ {m}...")
            if len(miss) > 5:
                # ⚠️ 2026-09-26 修**工单漏数根因**：原实现只打前 2 条且**不报
                # 剩余数**，于是「10/13 ❌」看上去只有 2 条问题——据此写工单时
                # 把 10 条缺陷记成 1 条（that-first-flight 总览层，情感节点 3 +
                # 金句精选 7）。**显示条数少不是问题，不报剩余数才是问题。**
                print(f"    …另有 {len(miss) - 5} 条未列出（**全部 {len(miss)} 条均已计入 "
                      f"本文件 FAIL**）")
    if short_total:
        print(f"\n⚠️ 全书共 {short_total} 条短引语（<20 flat 字符）未被校验——按规则须人工 grep 兜底")
    # ── P0-1 0 提取的角色分派结论 ──────────────────────────────────
    if all_frag_evidence:
        print(f"\n🔬 P0-6 --full 取证：{len(all_frag_evidence)} 条引语**前 52 字符命中"
              f"但整串对不上**——常规口径看不见这一段")
        for nm, q, badfrag, stripped in all_frag_evidence[:25]:
            if badfrag:
                off, piece = badfrag
                note = '（已剥尾部出处标注后仍对不上）' if stripped else ''
                print(f"    · {nm}{note}")
                print(f"      md：「{q}」")
                print(f"      首个不命中片段：flat 偏移 {off}  「{piece}」")
            else:
                print(f"    · {nm}：「{q}」分段均命中（疑跨标签/连写，非虚构）")
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
              "（全库实测 81 个正文章节文件属此类）。")
        print("       ⚠️ 更正：这些文件的引语**并非未核实**——check_chapter_quotes 的"
              "言情无编号口径 `^>\\s*(.+)$` 81/81 全部抽得到，")
        print("          已按 text/ 逐章口径核实过。真实缺口只是**未经 epub 全书口径**"
              "交叉核对（跨章搬句查不出）。")
    print(f"\n=== 总计 {total_ok}/{total} 引文可核实（{round(total_ok/total*100) if total else 0}%）；完全干净文件 {clean}/{clean+bad}；正文章节 0 提取 {len(zero_fail)}；总览 0 提取转交 {len(zero_defer)}{'；--full 整串取证 ' + str(len(all_frag_evidence)) if full_mode else ''} ===")
    sys.exit(0 if bad == 0 and total > 0 and not zero_fail else 1)

if __name__ == "__main__":
    _a = sys.argv[1:]
    _full = '--full' in _a
    if _full:
        _a.remove('--full')
    if len(_a) < 2:
        raise SystemExit(
            'Usage: verify_quotes.py "<书目录>" "<epub>" [--full]\n'
            '  --full  关闭 52 字符指纹盲区：指纹命中后再补一次**整串** flat 比对，'
            '整串不命中则按 fragment 分段取证（方案 P0-6 / §三.1）')
    main(_a[0], _a[1], _full)
