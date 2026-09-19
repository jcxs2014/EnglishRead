import re, glob, sys, zipfile, html as htmlmod

# FMW（Find My Way Down to You）独立审查检查器（2026-09-19 五步审查用）。
# 四项换路径检查：① 总览圈数字行全量 flat 扫描（对 epub 展平+text） ② 章节结构扫描
# ③ 关键词锚定（块感知版） ④ 短引语清单 + 文件名/H1 交叉。
# 参考 kw_anchor_ksr.py 的块感知逻辑；不占用 verify_/check_ 系列命名。

BOOK = "notes/books/novels/find-my-way-down-to-you-by-julian-winters"
EPUB = BOOK + "/library/Find My Way Down to You (Julian Winters) (z-library.sk, 1lib.sk, z-lib.sk).epub"
CIRCLED = {chr(0x2460 + i): i + 1 for i in range(30)}  # ①-㉚
STOP = {"the","and","but","not","all","his","her","its","you","don","didn","was","were","has",
        "had","can","that","this","with","from","for","they","she","him","our","their","who",
        "what","how","why","when","where","been","being","would","could","should","just","like",
        "about","after","before","over","under","into","onto","every","some","then","there",
        "here","very","also","than","too","only","have","are","it","he","did","does","say",
        "says","get","got","out","off","one","two","make","made","do","be","am","is","so","up"}

def flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

# ---- epub 展平 ----
z = zipfile.ZipFile(EPUB)
epub_text = ""
for n in sorted(z.namelist()):
    if n.endswith((".xhtml", ".html", ".htm")):
        raw = z.read(n).decode("utf-8", "ignore")
        raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<[^>]+>", " ", raw)
        epub_text += " " + htmlmod.unescape(raw)
EPUB_FLAT = flat(epub_text)

# ---- ① 总览圈数字行全量扫描 ----
print("=" * 20, "① 总览圈数字行全量 flat 扫描", "=" * 20)
for fname in ["00_金句精选.md", "00_情感节点.md"]:
    f = BOOK + "/" + fname
    lines = open(f).read().split("\n")
    total, miss, short = 0, [], []
    for ln in lines:
        s = ln.strip()
        if s and s[0] in CIRCLED:
            quote = s[1:].strip()
            qf = flat(quote)
            if len(qf) < 20:
                short.append((CIRCLED[s[0]], quote[:60]))
                continue
            total += 1
            # 拆省略号/引号分段逐段验
            segs = [p for p in re.split(r"…|\.\.\.|—|“|”|\"", quote)
                    if len(flat(p)) >= 12]
            ok = (qf[:60] in EPUB_FLAT) or (not segs and False)
            if segs:
                ok = all(flat(p)[:60] in EPUB_FLAT for p in segs)
            if not ok:
                # 逐段放宽：任一失败列出
                bad = [p[:40] for p in segs if flat(p)[:60] not in EPUB_FLAT]
                miss.append((CIRCLED[s[0]], bad))
    print(f"{fname}: 全量 {total} 条（另有短行 {len(short)} 条）", "MISS:", miss if miss else 0)
    for n, q in short:
        qf2 = flat(q)
        segs2 = [p for p in re.split(r"…|“|”", q) if flat(p)]
        hit = any(flat(p) in EPUB_FLAT for p in segs2) if segs2 else qf2 in EPUB_FLAT
        print(f"   短行 {n}: flat={len(qf2)} 命中epub={hit} | {q}")

# ---- ② 结构扫描 ----
print("=" * 20, "② 结构扫描（行首引语块口径）", "=" * 20)
tot_blocks, problems = 0, []
for md in sorted(glob.glob(BOOK + "/ch*.md")):
    base = md.split("/")[-1]
    m = re.match(r"ch(\d+)", base)
    if not m:
        continue
    lines = open(md).read().split("\n")
    blocks, cur = [], None
    for i, ln in enumerate(lines):
        if ln.startswith("> **原句"):
            if cur:
                blocks.append(cur)
            num = re.match(r"> \*\*原句 (\d+):\*\*", ln)
            cur = {"num": int(num.group(1)) if num else -1, "line": i + 1,
                   "quote": ln, "subs": []}
        elif cur is not None and ln.startswith("> ") and "**原句" not in ln:
            cur["quote"] += " " + ln[2:]
        elif cur is not None and re.match(r"\*\*.+\*\*", ln.strip()) and not ln.startswith(">"):
            cur["subs"].append(ln.strip().split(":")[0].strip("*"))
        elif cur is not None and ln.strip() == "---":
            blocks.append(cur)
            cur = None
    if cur:
        blocks.append(cur)
    tot_blocks += len(blocks)
    nums = [b["num"] for b in blocks]
    if nums != list(range(1, len(nums) + 1)):
        problems.append(f"{base}: 编号不连续 {nums}")
    for b in blocks:
        if len(b["subs"]) != 4:
            problems.append(f"{base}:L{b['line']} 原句{b['num']} 子项{len(b['subs'])}个{b['subs']}")
print(f"总块数 {tot_blocks}；文件 {len(glob.glob(BOOK + '/ch*.md'))} 个")
print("问题:", problems if problems else 0)

# ---- ③ 关键词锚定 ----
print("=" * 20, "③ 关键词锚定（块感知）", "=" * 20)
tot_kw, viol = 0, []
for md in sorted(glob.glob(BOOK + "/ch*.md")):
    base = md.split("/")[-1]
    m = re.match(r"ch(\d+)", base)
    tfile = BOOK + f"/text/ch{int(m.group(1)):02d}_"
    import os
    tfiles = [f for f in glob.glob(BOOK + "/text/ch" + f"{int(m.group(1)):02d}_" + "*.txt")]
    if not tfiles:
        continue
    tflat = flat(open(tfiles[0]).read())
    lines = open(md).read().split("\n")
    i = 0
    while i < len(lines):
        if lines[i].startswith("> **原句"):
            block = [lines[i]]
            j = i + 1
            while j < len(lines) and not lines[j].startswith("> **原句") and not lines[j].startswith("## "):
                block.append(lines[j])
                j += 1
            kw_line = next((l for l in block if l.strip().startswith("**关键词**")), None)
            if kw_line:
                kws = [k.strip() for k in kw_line.split("**：**")[-1].split("/")]
                for k in kws:
                    words = [w for w in re.findall(r"[A-Za-z']+", k)
                             if w.lower() not in STOP and len(w) >= 3]
                    for w in words:
                        tot_kw += 1
                        qflat = flat(" ".join(block))
                        stems = {w.lower(), flat(w), w.lower().rstrip("e"), w.lower() + "e",
                                 w.lower() + "s", w.lower()[:-1] if w.endswith("s") else w.lower() + "s"}
                        if not any(s and s in qflat for s in stems):
                            viol.append(f"{base}:L{i+1} 关键词[{w}]未命中本块")
            i = j
        else:
            i += 1
print(f"关键词词数 {tot_kw}；违规 {len(viol)}")
for v in viol[:20]:
    print("  ", v)

# ---- ④ 短引语清单 + 文件名/H1 交叉 ----
print("=" * 20, "④ 短引语清单（<20 flat）", "=" * 20)
for md in sorted(glob.glob(BOOK + "/ch*.md")) + [BOOK + "/00_金句精选.md", BOOK + "/00_情感节点.md"]:
    base = md.split("/")[-1]
    for ln in open(md).read().split("\n"):
        s = ln.strip()
        qm = re.match(r"> \*\*原句 \d+:\*\* (.+)", ln)
        if qm:
            q = qm.group(1)
        elif s and s[0] in CIRCLED:
            q = s[1:].strip()
        else:
            continue
        if 0 < len(flat(q)) < 20:
            segs = [p for p in re.split(r"“|”", q) if flat(p)]
            for p in segs:
                if len(flat(p)) < 20:
                    print(f"  {base}: [{p}] flat={len(flat(p))}")
print("=" * 20, "④b 文件名-H1 交叉", "=" * 20)
for md in sorted(glob.glob(BOOK + "/ch*.md")):
    base = md.split("/")[-1]
    fn = int(re.match(r"ch(\d+)", base).group(1))
    h1 = open(md).readline().strip()
    h1m = re.match(r"# (\d+)\.", h1)
    if not h1m or int(h1m.group(1)) != fn:
        print(f"  {base}: H1={h1[:40]}")
print("交叉完成")
