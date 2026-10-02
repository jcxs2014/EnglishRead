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
    p = os.path.join(here, "sweep_analysis_inline.py")
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
    ref, ref_src, _ep = sai.load_ref(book)
    if ref is None:
        print("=== 分析层跨章指认核对（%s）===" % os.path.basename(book.rstrip("/")))
        print("  ❓ **无法判定**：无 text/ 且无 epub —— 参照集缺失，不等于通过。")
        return 2
    by_chap = dict((num, f) for num, f, _t in ref)
    all_flat = " ".join(f for _n, f, _t in ref)

    EN = re.compile(r"`([^`]{3,})`")
    NEAR = re.compile(r"(?:ch(\d{1,2})\b|第\s*(\d{1,2})\s*章)([^`]{0,20})$")

    fake, moved, ok = [], [], 0
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
                f = sai.flat(frag)
                if len(f) < 6:
                    continue
                nm = NEAR.search(line[:m.start()])
                if not nm:
                    continue
                gap = nm.group(3)
                if any(c in _CLAUSE for c in gap):     # 跨分句 ⇒ 不是紧邻指认
                    continue
                tgt = int(nm.group(1) or nm.group(2))
                if tgt == own or tgt not in by_chap:
                    continue
                if f in by_chap[tgt]:
                    ok += 1
                    continue
                others = [c for c, cf in by_chap.items()
                          if c != own and c != tgt and f in cf]
                if f in all_flat:
                    moved.append((name, i, tgt, frag, others[:4]))
                else:
                    fake.append((name, i, tgt, frag))

    print("=== 分析层跨章指认核对（%s）===" % os.path.basename(book.rstrip("/")))
    print("  参照集：%s ；只认「chNN 后 20 字符内、且不跨中文分句标点」的反引号片段"
          % ref_src)
    print("  ✅ 归章正确 %d ｜ ❌ 伪造（全书查无）%d ｜ ⚠️ 移章（不在被引章）%d"
          % (ok, len(fake), len(moved)))
    if fake:
        print("  ⛔ 阻断型：伪造英文必须改")
        for name, ln, tgt, frag in fake:
            print("     ❌ %s:%d 声称 ch%02d ｜ %s" % (name[:30], ln, tgt, frag[:88]))
    if moved:
        print("  ⚠️ 移章**只记不改**：须人工读行——「回望前章」是正当写法，真错与正当在这里同形")
        for name, ln, tgt, frag, others in moved:
            where = "/".join("ch%02d" % c for c in others) if others else "别章亦无"
            print("     ⚠️ %s:%d 声称 ch%02d ｜ 实际在 %s ｜ %s"
                  % (name[:30], ln, tgt, where, frag[:70]))
    return 2 if fake else 0


if __name__ == "__main__":
    sys.exit(main())
