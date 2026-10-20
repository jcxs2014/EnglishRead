#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分析层**跨章指认**核对（gate.sh ⑯）：`chNN` 引用所附的英文是否真在被引的那一章。

**为什么要有这一项**（Beach Read 第四轮终验实测，11 处阻断型）：
`check_crossref` 只报「查无」，**不报「归错章」**——而这类错误的形态是
「片段真实存在，只是不在被引章」。它**不违反任何引语规则**，
所以 `verify_quotes` / `check_chapter_quotes` / `sweep_full` / `sweep_analysis_inline`
**全部放行**。实测那一类**系统性地往前偏 1–2 章**（把本章内容标成前一两章）。

**只认「紧邻同分句」形态**（两道限制都是踩过坑之后加的）：
1. 反引号必须出现在 `chNN` 引用**之后 20 个字符内**；
2. 二者之间**不得跨中文分句标点**（，。；、：）——
   否则「这一行里提了一句 ch04」会把该行的所有反引号片段都算成对 ch04 的指认
   （第一版没这条 ⇒ Beach Read 458 条假红）。

**分档**：
  ❌ 伪造  片段**全书 text 都没有**      → 阻断型，必须改
  ⚠️ 移章  片段在别的章、不在被引章      → **提示型，须人工读行**：可能是「回望前章」的正当
     写法，也可能是真错；**不分类就照单全改会把正当内容改坏**。
  ✅ 通过  片段在被引章
用法: python3 scripts/check_xref_chapter.py "<书目录>"
"""
import glob
import importlib.util
import io
import os
import re
import sys

_CLAUSE = "，。；、：？！,;"


def _load_sai():
    here = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(here, "sweep_analysis_inline.py")  # 同包内，改名会断
    if not os.path.exists(p):
        p = os.path.join(os.getcwd(), "scripts", "sweep_analysis_inline.py")
    spec = importlib.util.spec_from_file_location("sai", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit('用法: check_xref_chapter.py "<书目录>"')
    book = args[0]
    sai = _load_sai()
    ref, ref_src, epub_flat = sai.load_ref(book)
    if ref is None:
        print("=== 分析层跨章指认核对（%s）===" % os.path.basename(book.rstrip("/")))
        print("  ❓ **无法判定**：无 text/ 且无 epub —— 参照集缺失，不等于通过。")
        return 2
    # ⚠️ 2026-10-20 修死代码：`load_ref` 返回的 num 是**零填充字符串**（'01'…'43'，
    #   插叙件还可能带字母后缀 '01b'），而下面用 `tgt = int(...)` 得到**整数**，
    #   ⇒ `tgt not in by_chap` 恒为真 ⇒ **本项对所有书 100% 跳过**，永远只报 0/0/0
    #   （2026-10-20 阴性对照实测：在 ch01 注入 `ch05 \`Zxqvblorp qqqzzz\`` 仍报 0 条）。
    #   修法：按 int 建索引，一个章号对应多个提取件（ch01 / ch01b 插叙）。
    by_int = {}
    for num, f, _t in ref:
        m0 = re.match(r'(\d+)', str(num))
        if m0:
            by_int.setdefault(int(m0.group(1)), []).append((num, f))
    all_flat = " ".join(f for _n, f, _t in ref)

    EN = re.compile(r"`([^`]{3,})`")
    NEAR = re.compile(r"(?:ch(\d{1,2})\b|第\s*(\d{1,2})\s*章)([^`]{0,20})$")

    fake, moved, bmiss, unknown, nonquote, ok = [], [], [], [], [], 0
    for md in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        name = os.path.basename(md)
        mo = re.search(r"ch(\d+)", name)
        if not mo:
            continue
        own = int(mo.group(1))
        for i, line in enumerate(io.open(md, encoding="utf-8", errors="ignore").read().split("\n"), 1):
            if line.startswith("> "):          # 引语行由六道引语门禁覆盖
                continue
            for m in EN.finditer(line):
                frag = m.group(1)
                # ⚠️ 2026-10-20 修正（真实假阳性）：**补字标注**（`y[ou]` / `vide[o]`，
                #   英文原句里被改写者补回的那个字母用方括号标出）会让 flat 比对必失配
                #   ——`y[ou]` → "y ou"，原文是 "you"。修法＝比对前先去掉方括号、保留其内容。
                frag_cmp = re.sub(r"\[([^\]]*)\]", r"\1", frag)
                f = sai.flat(frag_cmp)
                if len(f) < 6:
                    continue
                nm = NEAR.search(line[:m.start()])
                if not nm:
                    continue
                gap = nm.group(3)
                if any(c in _CLAUSE for c in gap):     # 跨分句 ⇒ 不是紧邻指认
                    continue
                tgt = int(nm.group(1) or nm.group(2))
                if tgt == own or tgt not in by_int:
                    continue
                # ⚠️ 2026-10-20 新增「非引语片段」档：反引号里装的**不是引语**
                #   （分析式表达 `bafflement → fascination`、章号/文件名标签 `chap41`）
                #   ⇒ 不参与「伪造」判定，但**计数并列出**，让扫描集规模可审计。
                if "→" in frag or re.fullmatch(r"ch\d{1,3}[a-z]?", frag.strip()):
                    nonquote.append((name, i, tgt, frag))
                    continue
                tgt_hits = by_int[tgt]
                if any(f in cf for _n, cf in tgt_hits):
                    ok += 1
                    continue
                others = []
                for c, clist in by_int.items():
                    if c == own or c == tgt:
                        continue
                    if any(f in cf for _n, cf in clist):
                        others.append(c)
                if f in all_flat:
                    moved.append((name, i, tgt, frag, others[:4]))
                elif epub_flat and f in epub_flat:
                    # B 类语料缺失：text/ 提取件没覆盖到，但 epub 里有 ⇒ 不是伪造
                    bmiss.append((name, i, tgt, frag))
                elif epub_flat:
                    fake.append((name, i, tgt, frag))
                else:
                    # ⚠️ 2026-10-20：无 epub ⇒ 参照集不完整，「text/ 查无」**不能判伪造**
                    #   （AGENTS 第 3 条降级 lane 表：引语是否逐字在全书，权威依据是 epub；
                    #     无 epub 即「❓ 无法判定」，不是「❌ 伪造」）。
                    #   实证：全库 8 本无 epub 的书（stet / notes-on-grief / some-desperate-glory 等）
                    #   在本项判「伪造」共 76 条，逐条回原文看**多为其它的口径问题**
                    #   （分析式表达 `bafflement → fascination`、把改述写成反引号引语），
                    #   无 epub 即无法 A/B 裁决 ⇒ 不出结论、不判红。
                    unknown.append((name, i, tgt, frag))

    print("=== 分析层跨章指认核对（%s）===" % os.path.basename(book.rstrip("/")))
    print("  参照集：%s ；只认「chNN 后 20 字符内、且不跨中文分句标点」的反引号片段"
          % ref_src)
    print("  ✅ 归章正确 %d ｜ ❌ 伪造（全书查无）%d ｜ ⚠️ 移章（不在被引章）%d"
          % (ok, len(fake), len(moved)))
    if nonquote:
        print("  📎 非引语片段（分析式表达／章号标签，不参与判定）：%d" % len(nonquote))
        for name, ln, tgt, frag in nonquote:
            print("     📎 %s:%d 声称 ch%02d ｜ %s" % (name, ln, tgt, frag[:80]))
    if bmiss:
        print("  🔧 B 类语料缺失（text/ 查无但 epub 命中，非伪造）：%d" % len(bmiss))
        for name, ln, tgt, frag in bmiss:
            print("     🔧 %s:%d 声称 ch%02d ｜ %s" % (name, ln, tgt, frag[:88]))
    if unknown:
        print("  ❓ **无法判定**（无 epub ⇒ 参照集不完整，text/ 查无 ≠ 伪造）：%d" % len(unknown))
        print("     ⛔ 不判红、不出结论；须人工回原文裁决或补 epub 后重跑")
        for name, ln, tgt, frag in unknown:
            print("     ❓ %s:%d 声称 ch%02d ｜ %s" % (name, ln, tgt, frag[:88]))
    if fake:
        print("  ⛔ 阻断型：伪造英文必须改")
        for name, ln, tgt, frag in fake:
            print("     ❌ %s:%d 声称 ch%02d ｜ %s" % (name, ln, tgt, frag[:88]))
    if moved:
        print("  ⚠️ 移章**只记不改**：须人工读行——「回望前章」是正当写法，真错与正当在这里同形")
        for name, ln, tgt, frag, others in moved:
            where = "/".join("ch%02d" % c for c in others) if others else "别章亦无"
            print("     ⚠️ %s:%d 声称 ch%02d ｜ 实际在 %s ｜ %s"
                  % (name, ln, tgt, where, frag[:70]))
    return 2 if fake else 0


if __name__ == "__main__":
    sys.exit(main())
