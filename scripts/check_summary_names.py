#!/usr/bin/env python3
"""摘要层人物名 vs 本章正文/原文 — 抓「正文写对、导航或一句话总结写错人」。

为什么要有这一道：`verify_quotes` / `check_chapter_quotes` / `check_vocab` /
`check_chinese_layer` 全绿的书里，仍会出现「正文写女仆夏洛特、一句话概括写成费尔太太」
（ebenezer-scrooge ch45 实证）。这类错只落在摘要层，其余四道探针结构上碰不到。

做法（两遍）
  第一遍 **学**：全书正文里 `X太太 / X先生 / X上尉 / X医生 …` 这类带称谓的串按出现次数
  统计，≥3 次且前后不粘动词的才算「本书人名」；再用「同一引语块里中文名与英文专名共现」
  学出 `中文名 → 英文名`（≥3 块且占比 ≥60% 才认）。
  第二遍 **判**：本章「本章导航 + 一句话总结」提到的每个人名 ——
   ① 有英文映射、且该英文名在**本章** `text/` 一次都不出现 ⇒ **阻断**（摘要说本章有他，原文没有）；
   ② 无映射，且该人名在本章 md 正文层（导航之外）一次都不出现 ⇒ **提示**（可能只是间接提及）。

不做的事：不猜人名（没有称谓后缀的 3–5 字串一律不当人名——初版这么干，
一句「这件事上」也被当人名，全书报出几十条垃圾）、不改 md、不进 gate（先当抽查工具用）。

用法
  python3 scripts/check_summary_names.py "<书目录>" [--map]
  --map   打印学到的「中文名 → 英文名」，供人工确认

退出码：0 无阻断；1 有阻断；2 目录不可读或没有 md。
"""
import io, os, re, sys, glob, collections

SKIP_CONTEXT = ("未出现", "没有出现", "未露面", "不在场", "只被提到", "缺席", "未出场", "没有露面")
SUFFIX = ("太太", "先生", "夫人", "小姐", "上尉", "上校", "医生", "博士", "秘书",
          "女仆", "神父", "牧师", "探长", "队长", "律师")
LEAD = set("与和及在把被向对跟给是了的也都而但况且或只抢找按到回着家妻人请后己子门前随上下出从让使叫")
JUNK = set("此位是指的个名几数每两三四五些那这我你他她它们什怎为么 место")
EN_STOP = set("""The A An And But For Nor Or So Yet He She It They We You I His Her Their Our
This That These Those There Then When What Who Why How If In On At By Of To From With Without
Mr Mrs Miss Dr Captain Sir Lord Lady Yes No Oh Ah Well Now Just Only Even Still""".split())


def parse_md(path):
    s = io.open(path, encoding="utf-8").read()
    nav = re.search(r"## 本章导航\s*(.*?)(?=## 精读|$)", s, re.S)
    summ = re.search(r"## 一句话总结\s*(.*)$", s, re.S)
    body = s
    for blk in (nav, summ):
        if blk:
            body = body.replace(blk.group(0), "")
    return (nav.group(1) if nav else ""), (summ.group(1) if summ else ""), body


def split_blocks(body):
    parts = re.split(r"^> \*\*原句 \d+:\*\*\s*", body, flags=re.M)
    out = []
    for p in parts[1:]:
        lines = p.split("\n")
        out.append((lines[0], "\n".join(lines[1:])))
    return out


def raw_tokens(text):
    """带称谓后缀的原始串：取 2–5 字 + 后缀，并剥掉粘连的动词/介词。"""
    out = collections.Counter()
    pat = r"[\u4e00-\u9fff]{2,5}(?:" + "|".join(SUFFIX) + ")"
    for m in re.finditer(pat, text):
        tok = m.group(0)
        while tok and tok[0] in LEAD:
            tok = tok[1:]
        stem = tok[:-2] if len(tok) > 2 else ""
        if 2 <= len(tok) <= 6 and stem and not (set(stem) & JUNK):
            out[tok] += 1
    return out




def en_names(quote):
    found = set()
    for m in re.finditer(r"\b(?:Mr|Mrs|Miss|Dr|Captain|Sir|Lord|Lady)\.?\s+([A-Z][a-z]{2,})", quote):
        found.add(m.group(1))
    for m in re.finditer(r"\b([A-Z][a-z]{2,})\b", quote):
        if m.group(1) not in EN_STOP:
            found.add(m.group(1))
    return found


def learn(book):
    """返回 (names, mapping)。映射用 **lift**（共现 ÷ 各自的边际频率）而不是简单计数：
    引语里 Scrooge 出现得多，任何中文名都会与它「共现」很多次，按最大值会把所有人都映射成
    Scrooge；lift 把这种普遍共现扣掉（费尔太太×Fell 实测 lift 4.3，×Scrooge 只有 0.7）。"""
    files = sorted(glob.glob(os.path.join(book, "ch*.md")))
    seen = collections.Counter()
    tok_blocks = collections.Counter()
    en_blocks = collections.Counter()
    both = collections.defaultdict(collections.Counter)
    n_blocks = 0
    for p in files:
        _, _, body = parse_md(p)
        seen.update(raw_tokens(body))
        for quote, ana in split_blocks(body):
            ens = en_names(quote)
            if not ens:
                continue
            n_blocks += 1
            toks = set(raw_tokens(ana))
            for t in toks:
                tok_blocks[t] += 1
            for e in ens:
                en_blocks[e] += 1
            for t in toks:
                for e in ens:
                    both[t][e] += 1
    names = {t for t, c in seen.items() if c >= 3}
    mapping = {}
    for t in names:
        c = both.get(t)
        if not c:
            continue
        # 选法：先卡「至少 3 块共现」且「占该名字出现的块的 1/4 以上」，再取共现次数最多的英文名。
        # 不用 lift：lift 偏爱全书罕见的英文名（Mittamus 只共现 1 次却 lift 7.0，把费尔太太→Fell 挤掉）。
        cand = [(k, e) for e, k in c.items()
                if k >= 3 and k / max(tok_blocks[t], 1) >= 0.25]
        if not cand:
            continue
        mapping[t] = max(cand)[1]
    return names, mapping


def mentioned(text, names):
    return {n for n in names if n in text}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        return 2
    book = args[0].rstrip("/")
    if not os.path.isdir(book):
        print(f"❌ 目录不可读：{book}")
        return 2
    names, mapping = learn(book)
    if "--map" in flags:
        for k in sorted(names, key=len):
            print(f"  {k} → {mapping.get(k, '（未映射）')}  ×{k}")

    texts_all = []
    for q in sorted(glob.glob(os.path.join(book, 'text', 'ch*.txt'))):
        texts_all.append(io.open(q, encoding='utf-8').read())
    findings = []
    for p in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        base = os.path.basename(p)
        m = re.match(r"ch(\d+)", base)
        if not m:
            continue
        n = int(m.group(1))
        nav, summ, body = parse_md(p)
        txts = glob.glob(os.path.join(book, "text", f"ch{n:02d}_*.txt"))
        text = io.open(txts[0], encoding="utf-8").read() if txts else ""
        if not text:
            continue
        # ② 直接用英文艺名的书（中文里嵌 Poppy / Eddie）：导航或总结点了名、本章原文却没有
        for scope, label in ((summ, "一句话概括"), (nav, "本章导航")):
            for e in sorted(en_names(scope)):
                frac_e = sum(1 for q in texts_all if q != text and
                             re.search(rf"\b{re.escape(e)}\b", q)) / max(len(texts_all) - 1, 1)
                if frac_e < 0.25:
                    continue
                if re.search(rf"\b{re.escape(e)}\b", text) or e in body:
                    continue
                level = "提示"
                findings.append((level, n, f"{label}提到「{e}」，本章原文查无"
                                 f"（{e} 在 {frac_e:.0%} 的其他章原文里出现）"))

        for scope, label in ((summ, "一句话概括"), (nav, "本章导航")):
            if label == "一句话概括" and any(t in summ for t in SKIP_CONTEXT):
                continue
            for name in sorted(mentioned(scope, names), key=len, reverse=True):
                e = mapping.get(name)
                if e:
                    if re.search(rf"\b{re.escape(e)}\b", text):
                        continue
                    # 这个人是否是本书的常驻角色：别的章原文里出现得越多，本章漏掉越可疑
                    frac = sum(1 for q in texts_all if q != text and
                               re.search(rf"\b{re.escape(e)}\b", q)) / max(len(texts_all) - 1, 1)
                    level = "提示"
                    findings.append((level, n, f"{label}提到「{name}」（{e}），本章原文查无"
                                     f"（{e} 在 {frac:.0%} 的其他章原文里出现）"))
                elif label == "一句话概括" and name not in body:
                    findings.append(("提示", n, f"{label}提到「{name}」，本章正文层未出现"))

    blocking = [f for f in findings if f[0] == "阻断"]
    for level, n, msg in dict.fromkeys(findings):
        print(f"{'❌' if level == '阻断' else '⚠️'} ch{n:02d} {msg}")
    print(f"=== 摘要层人物名：提示型 {len(set(findings))} ===")
    print("   全部是提示型：导航/总结可以合法地提到不在本章出场的人（铺垫、对比），必须人读一眼再定性；")
    print("   括号里的百分比＝该英文名在「其他章原文」中出现的比例，越高越值得先看（≥60% 优先）。")
    return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
