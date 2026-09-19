#!/usr/bin/env python3
"""Grim Tidings 独立五步审查检查器（换路径口径，非 check_* 工具复述）
- c 结构扫描：行首 `> **原句 N:**` 块——编号连续/四子项齐全/零孤儿/零重复
- b 独立归属：每条引语 flat 后必须命中本章 text/（独立 flat 实现，非 check_chapter_quotes）
- d 关键词锚定：块内关键词的英文词须命中该块引语（允许词形变化，剔除 stop words）
- d 词汇例句独立比对：词汇表每条例句 flat 后必须命中本章 text/（check_vocab 不做逐字校验的盲区补位）
- d 分析层英文片段 sweep：引语块外的英文片段（≥3 词）须命中本章 text/ 或全书 text/
- e 总览 flat 全量：00_金句精选/00_情感节点 的编号引语逐条命中全书 text/ 联合体，并列出来源章
"""
import re, sys, glob, unicodedata, os

BOOK = "notes/books/novels/grim-tidings-by-b-k-borison"
TEXT = os.path.join(BOOK, "text")

def flat(s):
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"[^a-z0-9]+", "", s.lower())
    return s

STOP = set("""a an the of to in on at for and or but is are was were be been it its this that these those i you he she we they me my our your his her their him them as with by from not no do does did done have has had will would can could should may might must than then there here what which who whom whose when where why how all any both each few more most other some such only own same so too very just also into over under out up down about against between through during before after above below again further once don't doesn't didn't won't can't isn't aren't wasn't weren't he'd she'd i've you've we've they've it's that's there's what's let's i'm you're we're they're he's she's""".split())

def words(s):
    return [w for w in re.findall(r"[a-zA-Z']+", s) if len(w) > 2 and w.lower() not in STOP and not w.isdigit()]

# ---------- 载入 ----------
ch_texts = {}
for p in sorted(glob.glob(os.path.join(TEXT, "ch*.txt"))):
    n = int(re.match(r"ch(\d+)_", os.path.basename(p)).group(1))
    ch_texts[n] = open(p, encoding="utf-8").read()
all_flat = {n: flat(t) for n, t in ch_texts.items()}
union_flat = "".join(all_flat.values())

def word_stem(w):
    w = w.lower().replace("'", "")
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w

def stems_hit(stem, textflat_stems):
    return stem in textflat_stems

# 预生成 stem 集合（对词形变化宽松匹配）
def stem_set(s):
    out = set()
    for w in re.findall(r"[a-zA-Z']+", s):
        out.add(word_stem(w))
        out.add(w.lower())
    return out

block_re = re.compile(r"^> \*\*原句 (\d+):\*\* (.+)$", re.M)
subitems = ["中文理解", "关键词", "为什么这样写", "读者视角提示"]
quote_line_re = re.compile(r"^> \*\*原句 (\d+):\*\*", re.M)

issues, stats = [], {"blocks": 0, "short": 0}

# ---------- 章节文件 ----------
mds = sorted(glob.glob(os.path.join(BOOK, "ch*.md")),
             key=lambda p: int(re.match(r".*ch(\d+) ", p).group(1)))
for mp in mds:
    base = os.path.basename(mp)
    n = int(re.match(r"ch(\d+) ", base).group(1))
    raw = open(mp, encoding="utf-8").read()
    tflat = all_flat[n]
    tstems = stem_set(ch_texts[n])

    # 引语块
    quotes = block_re.findall(raw)
    nums = [int(x) for x, _ in quotes]
    stats["blocks"] += len(nums)
    if nums != list(range(1, len(nums) + 1)):
        issues.append(f"{base}: 编号不连续 {nums[:5]}...{nums[-3:] if len(nums)>8 else ''}")
    if len(set(nums)) != len(nums):
        issues.append(f"{base}: 重复编号")

    # 孤儿块/四子项：按块切片
    pos = [(m.start(), m.end(), int(m.group(1))) for m in quote_line_re.finditer(raw)]
    for idx, (s, e, num) in enumerate(pos):
        end = pos[idx + 1][0] if idx + 1 < len(pos) else len(raw)
        seg = raw[e:end]
        missing = [si for si in subitems if f"**{si}：**" not in seg]
        if missing:
            issues.append(f"{base} 原句{num}: 缺子项 {missing}")
        # 引语本体命中本章
        q = quotes[[x for x, _ in quotes].index(str(num))][1] if False else None
    # 引语 flat 比对（独立实现）
    for qnum, qtext in quotes:
        q = qtext
        # 拆省略号
        segs = [s for s in re.split(r"…|\.\.\.", q) if flat(s)]
        for seg in segs:
            fs = flat(seg)
            if len(fs) < 20:
                stats["short"] += 1
                continue
            if fs not in tflat:
                issues.append(f"{base} 原句{qnum}: 引语片段未命中本章 text（独立 flat）:: {seg[:60]}")
    blocks = re.split(r"(?=^> \*\*原句 \d+:\*\*)", raw, flags=re.M)
    for blk in blocks:
        m = re.match(r"^> \*\*原句 (\d+):\*\* (.+)$", blk, re.M)
        if not m:
            continue
        qnum, qtext = int(m.group(1)), m.group(2)
        km = re.search(r"\*\*关键词：\*\* (.+)", blk)
        if not km:
            continue
        kws = [k.strip() for k in km.group(1).split(",")]
        qstems = stem_set(qtext)
        qflat = flat(qtext)
        for kw in kws:
            kw = kw.strip()
            if not kw or kw.startswith("（"):
                continue
            for w in re.findall(r"[a-zA-Z']+", kw):
                if len(w) <= 2 or w.lower() in STOP:
                    continue
                st = word_stem(w)
                if st not in qstems and w.lower() not in qflat:
                    issues.append(f"{base} 原句{qnum}: 关键词词未命中引语 :: {kw}（词 {w}）")

    # 词汇例句独立 flat 比对
    for m in re.finditer(r"^\| ([^|\n]+) \| ([^|\n]+) \| ([^|\n]+) \|$", raw, re.M):
        ex = m.group(3).strip()
        fex = flat(ex)
        if len(fex) < 8:
            continue
        if fex not in tflat:
            issues.append(f"{base}: 词汇例句未命中本章（独立 flat）:: {ex[:60]}")

    # 分析层英文片段 sweep（引语行/词汇行/代码外，含 ≥3 个英文词的引号片段）
    analysis = re.sub(r"^> \*\*原句 \d+:\*\* .*$", "", raw, flags=re.M)
    analysis = re.sub(r"^\|.*\|$", "", analysis, flags=re.M)
    for frag in re.findall(r'"([^"\n]{25,})"', analysis):
        ffrag = flat(frag)
        wcount = len(re.findall(r"[a-zA-Z]+", frag))
        if wcount >= 3 and ffrag not in tflat and ffrag not in union_flat:
            issues.append(f"{base}: 分析层英文片段全书未命中 :: {frag[:70]}")

# ---------- 总览 flat 全量（金句/情感节点）----------
def parse_numbered(path):
    out = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\s*[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚]\s*[\"“](.+)[\"”]", line.strip() and line or line)
        mm = re.match(r"^\s*([①-⑳㉑-㉚])\s+(.+)$", line.rstrip("\n"))
        if mm:
            out.append((mm.group(1), mm.group(2).strip()))
    return out

for fname in ["00_金句精选.md", "00_情感节点.md"]:
    path = os.path.join(BOOK, fname)
    for circ, line in parse_numbered(path):
        # 提取英文部分（首个英文引号内容或整行英文）
        m = re.search(r'"([^"]+)"', line)
        q = m.group(1) if m else line
        segs = [s for s in re.split(r"…|\.\.\.", q) if flat(s)]
        srcs = set()
        ok = True
        for seg in segs:
            fs = flat(seg)
            if len(fs) < 20:
                stats["short"] += 1
                continue
            hit = [n for n, f in all_flat.items() if fs in f]
            if not hit:
                ok = False
                issues.append(f"{fname} {circ}: 未命中任何章 text :: {seg[:60]}")
            else:
                srcs |= set(hit)
        if ok and srcs:
            pass  # 来源章打印由汇总输出

print(f"== 独立审查器 ==")
print(f"章节引语块 {stats['blocks']}；短引语(<20 flat) {stats['short']}")
print(f"问题 {len(issues)} 条：")
for i in issues:
    print("  ❌", i)
if not issues:
    print("  （零问题）")
