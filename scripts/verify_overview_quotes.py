#!/usr/bin/env python3
"""
verify_overview_quotes.py — 总览文件引文真实性核对工具

用途：检查某本书 00*.md（概述/金句精选/情感节点）中的英文引文，
是否能在 epub 全书中逐字找到。
专门堵住 verify_quotes.py 的盲区——后者只扫 ch*.md，不覆盖总览层。

用法：
  python3 scripts/verify_overview_quotes.py "<书目录>" ["<epub>"]

  epub 可省略——无 epub 时退到 `text/` 逐章拼接（降级 lane），
  两者都没有则退出码 2「无法判定」，**不产出计数**。

输出：每个 00*.md 文件的 命中数/总数，失败文件列出未命中指纹；末尾给出总账。
原理：与 verify_quotes.py 完全一致（指纹比对逻辑共享），仅扫描目标不同。
"""
import re, sys, glob, html, zipfile, tempfile, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# 2026-09-29：拼接判定**从 check_overview_full 直接复用**，不另写一套。
# 该文件原注释已写死这条纪律——「两处口径必须一致，否则同一段文字在正文章节判 🔶、
# 在总览判 ❌，排查的人会怀疑工具而不是怀疑书」。构造上一致，而不是靠自觉保持一致。
from check_overview_full import halves, suffix_match, is_quoteish  # noqa: E402
from verify_quotes import strip_page_anchors  # noqa: E402  # 页码锚点口径须与 epub 参照集一致

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚'

def flat_alpha(s: str) -> str:
    s = re.sub(r'\\+\s*[nt]', '', s)
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
                out += _read_html(p)
    return out

def _read_html(p: str) -> str:
    t = open(p, encoding="utf-8", errors="ignore").read()
    t = strip_page_anchors(t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\u00a0', ' ')
    return t

def extract_quotes(txt: str):
    """按行提取候选引文，兼容多种书写顺序；同文本去重保序。

    2026-09-06 增补（实证盲区）：
    - CIRCLED 扩展到 ㉚（Black River 金句 ㉖-㉚ 曾静默漏检）
    - `**①**` 行中粗体圈数字格式（Up in Molten Lights 30 句仅抽到 1 条）
    - 省略号/… 分段：每段均命中才算过（与其他工具口径一致）
    - 2026-09-29：**裸 `> "…"` 格式**（总览情感节点的主力写法）。此前 60 个
      总览文件因此被报「口径外」——全库 1015 条引语**从未被任何工具核验过**，
      而汇总行只显示「已核覆盖 1/3 篇」，是典型的假绿。
    """
    quotes = []
    seen = set()
    circ = '[' + CIRCLED + r']'
    for raw in txt.splitlines():
        s = raw.strip()
        # 剥掉 markdown 引用块前缀 "> "（若有）
        # 裸 `> "…"` 须在剥 `> ` 之前判，否则丢掉「这是引用块」这个信号
        # 裸 `> "…"` —— 含「引号后还接叙述」的写法（the-glass-girl 情感节点：
        # `> "Oh god," my mother says. She covers her mouth with her hands.`）
        # 收**整行内容**而非只收到第一个引号：短引语（`Oh god,` 7 flat 字符）单独
        # 达不到 20 字符阈值，只收引号内会把整个文件判成「无引语」。
        # 整行收进来后由 🔶 拼接档如实报告「这行不是一条干净引语」。
        # ⚠️ 必须排除带标签的行：`**原句 1:** "…"` / `> **①** "…"` 由后面那些
        # 分支处理。第一版没排除 ⇒ 裸分支抢在前面把 `**原句 1:**` 当成引语本体，
        # 指纹变成 `原句1thisroad…` ⇒ 永远查无（实测 the-green-road 0/25）。
        if (raw.strip().startswith('>') and ('"' in raw or '\u201c' in raw)
                and not re.match(r'^>\s*\**\s*(?:原句\s*\d+|[' + CIRCLED + r'])',
                                 raw.strip())):
            b = re.sub(r'^>\s*', '', raw.strip())
            b = re.sub(r'[（(]\s*ch\d+\s*[）)]\s*$', '', b)
            b = b.strip("*' \"\u201c\u201d")
            # ⚠️ 必须过 is_quoteish——否则中文说明行也会被当引语。实测
            # jane-eyre 概述:8 `> 本概述只依据本 EPUB 的正文（text/ch01–ch38）。
            # …例如第二十八章开头的"阁楼夜"不在本版…Rochester…` 含 `"` 且 ASCII
            # 字符够 20，被抽成引语 ⇒ 指纹带 `epubtextch01ch38` 永远查无。
            # is_quoteish 直接拒含中文、含 `text/`/`chNN`/`.md` 的行。
            if not is_quoteish(b):
                continue
            if len(flat_alpha(b)) >= 20 and b not in seen:
                seen.add(b)
                quotes.append(b)
            continue
        s = re.sub(r'^>\s*', '', s)
        # ⚠️ 2026-10-05（Heirs of the Cursed 总览三篇实测）：原口径每个分支都是
        # `编号 + \s+ + 引语`，于是**接不住最常见的中文标注式样**
        # ——`**①**（ch01）"Love could conquer…"`（编号与章号之间没有空格）。
        # 结果该文件被整篇判成「无引语行」⇒ 退出码 1，**零引语被校验**，
        # 而 `check_overview_full` 的 `label_near` 却认得同一种形态 ⇒
        # **两把尺口径漂移**（正是本仓库反复警告的那类）。
        # 处置：加一条**纯增量**分支（带可选章号标注），不改原有分支行为。
        m = (re.match(r'^\*{0,2}' + circ + r'\*{0,2}[（(]\s*ch\d+\s*[）)]\s*(.+)$', s)
             or re.match(r'^' + circ + r'\s+(.+)$', s)
             or re.match(r'^\*{1,2}' + circ + r'\*{1,2}\s+(.+)$', s)      # **①** "..."
             or re.match(r'^\*{1,2}' + circ + r'\*{1,2}\s*["\'](.*)["\']', s)
             or re.match(r'^' + circ + r'\s+["\'](.*)["\']', s)
             or re.match(r'^\*\*原句\s*\d+(?:\s*\([^)]+\)\s*)?[:：]?\*\*\s+(.+)$', s)
             or re.match(r'^>\s*\*{0,2}原句\s*\d+(?:\s*\([^)]+\)\s*)?[:：]?\*{0,2}\s+(.+)$', s))
        if not m:
            continue
        body = m.group(1).strip()
        body = body.strip("*' ")
        # 章节标注（chNN）不属引文本体，**出现在任何位置都要剥**：
        # 旧口径只剥行尾，实测 i-have-some-questions-for-you 金句:19
        # `**④** **I think the wrong guy is in prison.**（ch07）——这是全书第二次…`
        # 标签后面跟着中文点评 ⇒ 没剥 ⇒ 指纹成 `…inprisonch07` 永远查无。
        body = re.sub(r'[（(]\s*ch\d+\s*[）)]', ' ', body)
        # 引语本体切到第一个中文字符：其后是 md 自己的点评/译文，不参与校验
        # （`…in prison.`（我认为关错人了。）**（ch07）** 就是中英混行）
        m_cjk = re.search(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', body)
        if m_cjk and m_cjk.start() > 0:
            body = body[:m_cjk.start()]
        body = re.sub(r'\s*[—–-]{1,2}\s*$', '', body).strip("'\"*—–- ")
        if len(flat_alpha(body)) >= 20 and body not in seen:
            seen.add(body)
            quotes.append(body)
    return quotes

def main(book_dir: str, epub_path: str = ""):
    if not glob.glob(os.path.join(book_dir, "00*.md")):
        print(f"⚠️ 未找到 00*.md 总览文件（{book_dir}），跳过")
        sys.exit(0)

    # 参照集优先级（与 sweep_full 一致）：有 epub 用 epub，否则退到逐章 text/。
    # 2026-09-29 新增 text/ 兜底的动因：全库 64 个含裸 `> "…"` 引语的总览里
    # **多数没有 epub**，而裸格式正是本工具原先收不到的那一类——不兜底的话
    # 「口径外」虽然消除了，那些书仍然一条都验不了。
    lane = ""
    if epub_path and os.path.exists(epub_path):
        full = flat_alpha(epub_flat_text(epub_path))
        lane = "完整 lane（epub）"
    else:
        parts = []
        for f in sorted(glob.glob(os.path.join(book_dir, "text", "*.txt"))):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        if not parts:
            print(f"❓ {book_dir} 无 epub 且无 text/ ⇒ 无法判定（不是通过）")
            sys.exit(2)
        full = flat_alpha("\n".join(parts))
        lane = "降级 lane（text/ 兜底，非 epub 全书）"
    print(f"=== lane：{lane} ===")
    total_ok = total = clean = bad = splice = 0
    nfiles = 0
    splice_list = []
    gap = []   # 口径外：有像引语的 > 行却提取到 0 条
    bare = []  # 无引语：确实没有可核的引语行（正常）
    for f in sorted(glob.glob(os.path.join(book_dir, "00*.md"))):
        name = os.path.basename(f)
        nfiles += 1
        txt = open(f, encoding="utf-8").read()
        quotes = extract_quotes(txt)
        if not quotes:
            # 2026-09-29 修正：原先一律「⚠️ 未提取到编号引语」后 `continue`，
            # 而文件既不计入 clean 也不计入 bad ⇒ 汇总行照样打
            # 「完全干净文件 1/1」——**3 篇总览只核了 1 篇却显示 100%**（假绿，
            # 正是 8.5c「死代码报 0」形态）。现在按「> 行里有没有像引语的东西」分两类：
            #   · 有 ⇒ 工具口径外（裸 `> "…"` 格式不被 extract_quotes 收）⇒ 计入覆盖缺口
            #   · 无 ⇒ 该文件本就没有引语（如 00_概述 的作者/体裁元数据行）⇒ 正常跳过
            looks = [ln for ln in txt.splitlines()
                     if ln.lstrip().startswith(">") and '"' in ln
                     and len(flat_alpha(ln)) >= 15]
            if looks:
                gap.append((name, looks[0].strip()[:90]))
                print(f"{name}: ❌ 覆盖缺口——{len(looks)} 条引语样 > 行，"
                      f"但 extract_quotes 提取到 0 条（口径外，须人判）")
            else:
                bare.append(name)
                print(f"{name}: ➖ 无引语行（正常，非门禁项）")
            continue
        ok = 0
        miss = []
        for q in quotes:
            qa = flat_alpha(q)
            frag = qa[:52]
            if frag in full:
                ok += 1
                continue
            # 省略号分段：每段（≥15 flat 字符）均命中才算过
            segs = [p for p in re.split(r'…|\.\.\.', q)
                    if len(flat_alpha(p)) >= 15]
            if segs and all(flat_alpha(p)[:40] in full for p in segs):
                ok += 1
                continue
            # 2026-09-29：**跨缝隙拼接**档（🔶 提示，不判红）。
            # 整串查无但按句切开后每段都在 ⇒ 两半逐字真实、中间叙述/对话标签
            # 被去掉后接上了。flat 整串口径对拼接天然假阴为「查无」，
            # 直接判 ❌ 会误杀真引语（本库 She Haunts 批次 9 条 flat 查无里
            # 7 条正是这一类）。口径复用 check_overview_full 的 halves +
            # suffix_match，**不另立一套**。
            pieces = halves(q)
            if len(pieces) > 1:
                allin = True
                for pc in pieces:
                    if not pc.strip():
                        continue
                    fpc = flat_alpha(pc)
                    if len(fpc) < 15:
                        continue
                    if fpc[:52] in full or fpc[:40] in full:
                        continue
                    if suffix_match(pc, full):
                        continue
                    allin = False
                    break
                if allin:
                    splice += 1
                    splice_list.append((name, q[:80]))
                    continue
            miss.append(frag[:40])
        total_ok += ok
        total += len(quotes)
        if ok == len(quotes):
            clean += 1
            print(f"{name}: {ok}/{len(quotes)} ✅")
        else:
            if miss:
                bad += 1
                print(f"{name}: {ok}/{len(quotes)} ❌")
                for m in miss[:3]:
                    print(f"    ✗ {m}...")
            else:
                clean += 1
                print(f"{name}: {ok}/{len(quotes)} ✅（含 🔶 跨缝隙拼接 {len([x for x in splice_list if x[0]==name])}，不判红）")
    print(f"\n=== 总览引文 {total_ok}/{total} 可核实（{round(total_ok/total*100) if total else 0}%）；"
          f"完全干净文件 {clean}/{clean+bad}；已核覆盖 {clean+bad}/{nfiles} 篇"
          f"（无引语 {len(bare)} · 口径外 {len(gap)}）；"
          f"🔶 跨缝隙拼接 {splice} 条（提示，不判红）===")
    for n, q in splice_list[:10]:
        print(f"    🔶 {n}: {q}")
    for n, ex in gap:
        print(f"    ⚠️ 口径外 {n}: {ex}")
    if gap:
        print("⚠️ 「口径外」= 工具收不到该文件的引语格式 ⇒ 这些引语**未经任何核验**，"
              "不是「已核且干净」。按 8.5c 先怀疑工具：确认格式后扩展 extract_quotes，"
              "或人工逐条核。")
    if splice:
        print("⚠️ 「跨缝隙拼接」= 整串查无但按句切开每段逐字都在 ⇒ 引语本体是真的，"
              "**拼接处丢了原文里的叙述/对话标签**。本库 She Haunts 批次 9 条 flat 查无里 "
              "7 条正是这一类，判 ❌ 会误杀真引语。按提示型处理：查拼接处是否该补回标签。")
    # 退出码：内容 ❌（bad）或覆盖缺口（gap）都算不通过；拼接不算
    sys.exit(0 if bad == 0 and total > 0 and not gap else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
