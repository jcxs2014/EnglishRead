#!/usr/bin/env python3
"""章号指认机械裁决（**lane ⑯ 的补充**：lane ⑯ 只认「chNN 后 20 字符内的反引号片段」，
本书 257 处 chNN 指认**无一用反引号** ⇒ lane ⑯ 对本书是**跳过型**（扫描集为空），
本脚本按「chNN 切段 → 段内专名须在该章 text/」补做同一维度。

**分档（2026-10-20 修正）**：
  · **英文专名**（大写开头、长度 ≥3、不在停用表）——该章 text/ 查无 ⇒ 可判定，报**阻断型**。
  · **中文引语词**（`「…」`）——中文译文对英文语料**结构性不可判定** ⇒ 报 **❓ 无法判定**，
    **不判红、不算缺陷**（导航/分析层的中文引语是译文，英文原文里当然查无）。
  ⇒ 报数时必须**同时给扫描集规模**（切了几段、检出了几个专名），不能只写「0 条」。

退出码 0=无阻断型；1=有阻断型（英文专名在该章查无）。
"""
import os
import re
import sys
import glob

# 通用专名/书内标识：不参与「专名是否在该章」判定
STOP = set("""The And But This That With When What Then They There Their Chapter
Gods Well Oh Just Like Love Hope Help Hear Here Hold Home Hate How Why Yes No
Man Miss Dread Death Dark Deep One Two Three Fey Way Goldbry Sweeney Kettle Callex
Lord Commander Captain Major General King Queen Prince Princess God Goddess Gods
Chapter Part Book Note Page Mr Mrs Ms Sir Lady I Me My We Our You Your His Her Its""".split())


def load(book):
    ch = {}
    for p in glob.glob(os.path.join(book, "text", "*.txt")):
        m = re.search(r"ch(\d+)", os.path.basename(p))
        if m:
            ch[f"ch{int(m.group(1)):02d}"] = open(p, encoding="utf-8").read()
    return ch


def segs(s):
    """按 chNN 切段：返回 [(章号, 该章号之后到下一个章号之前的文本)]

    ⚠️ 2026-10-20 修正：`ch41–ch43` 这类**章号区间**（标题里的「第七段（ch41–ch43）」）
    不是「对某章的指认」，原实现把它切成两段 ⇒ 区间名与正文之间的内容被**错误归属**
    给区间末端的章号 ⇒ 概述 L36「Galev」假阳性的根因。
    ⇒ 区间的两个端点**都不产生分段**。
    """
    rng = [(m.start(), m.end()) for m in
           re.finditer(r"ch\d{1,2}\s*[-–—~]\s*ch\d{1,2}", s)]
    ms = list(re.finditer(r"\bch(\d{1,2})\b", s))
    out = []
    for i, m in enumerate(ms):
        if any(a <= m.start() < b for a, b in rng):
            continue                      # 区间端点：不产生分段
        end = ms[i + 1].start() if i + 1 < len(ms) else len(s)
        out.append((int(m.group(1)), s[m.end():end]))
    return out


def run(book):
    ch = load(book)
    eng_bad, cjk_unknown = [], []
    n_seg = n_tok = 0
    for f in sorted(glob.glob(os.path.join(book, "*.md"))):
        b = os.path.basename(f)
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            s = line.strip()
            if not s or s.startswith(("|", "#", "> ")):
                continue
            if len(re.findall(r"[\u4e00-\u9fff]", s)) < 5:
                continue
            for nn, seg in segs(s):
                key = f"ch{nn:02d}"
                if key not in ch:
                    continue
                n_seg += 1
                t = ch[key]
                for q in re.findall(r"「([^」]{2,24})」", seg):
                    if q in t:
                        continue
                    if any(c in q for c in "，。！？…—"):
                        continue
                    cjk_unknown.append((b, i, key, f"「{q}」", seg[:110]))
                for tok in set(re.findall(r"\b[A-Z][A-Za-z]{2,}\b", seg)):
                    if tok in STOP:
                        continue
                    n_tok += 1
                    if tok not in t:
                        eng_bad.append((b, i, key, tok, seg[:110]))
    return n_seg, n_tok, eng_bad, cjk_unknown


if __name__ == "__main__":
    book = sys.argv[1]
    n_seg, n_tok, eng_bad, cjk_unknown = run(book)
    print("=== 章号指认补充核对（lane ⑯ 跳过型的替代扫描）===")
    print("· 扫描集：%d 个 chNN 分段（md 行内），其中检出 %d 个英文专名" % (n_seg, n_tok))
    print("· **阻断型**（英文专名在该章 text/ 查无）：%d" % len(eng_bad))
    for x in eng_bad:
        print("  ❌ %s:%d  %s 查无 %r" % (x[0][:32], x[1], x[2], x[3]))
        print("       %s" % x[4][:120])
    print("· **❓ 无法判定**（中文引语词：中文译文对英文语料结构性不可判定）：%d"
          % len(cjk_unknown))
    print("  ⛔ 不判红、不算缺陷（导航/分析层的中文引语是译文，英文原文里本就查无）")
    for x in cjk_unknown[:5]:
        print("  ❓ %s:%d  %s %s" % (x[0][:32], x[1], x[2], x[3]))
    if len(cjk_unknown) > 5:
        print("  ❓ …其余 %d 条同型，略" % (len(cjk_unknown) - 5))
    sys.exit(1 if eng_bad else 0)
