#!/usr/bin/env python3
"""close_read_check.py — 单章精读自查器（写作期自用，不替代门禁）

用法：
    python3 .memory/tools/close_read_check.py "<书目录>" "<章 md>"

检查项（全部按 text/ 逐字，弯直引号/破折号算排版差异）：
  1. 每块引语 ① 是否逐字命中本章 text（用 scripts/lib/text.norm 的口径归一化）
  2. 每块引语 ② 词数（目标 30–70）与句数（目标 1–3），>100 词单独报
  3. 词汇表三档：例句是否逐字命中、是否含词头、词头是否重复、例句是否混入中文
  4. 关键词：是否落在本块引语内、是否超过 8 词（整句照抄）
  5. 中文理解 / 为什么这样写的汉字数与中文占比（对齐 chapter.sh 的口径）

退出码 0 = 无问题；1 = 有问题（逐条打印）。
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "scripts"))
from lib.text import norm, cjk_count, cjk_ratio  # noqa: E402

SEP = r"[/、,;；]"
QUOTE_RE = re.compile(r"^> \*\*原句 (\d+):\*\*\s*(.*)$")
FIELD_RE = re.compile(r"^\*\*(中文理解|关键词|为什么这样写|读者视角提示)\*\*：\s*(.*)$")
TIER_RE = re.compile(r"^###\s*(⭐+)\s*(.*)$")


def text_path(book_dir, chapter_no):
    tdir = os.path.join(book_dir, "text")
    digits = f"{int(chapter_no):02d}"
    cands = [f for f in sorted(os.listdir(tdir))
             if re.match(rf"^ch{digits}([_. ].*)?\.txt$", f)]
    if not cands:
        cands = [f for f in sorted(os.listdir(tdir))
                 if re.match(rf"^ch\d+([_. ].*)?\.txt$", f)
                 and re.match(r"^ch(\d+)", f).group(1).lstrip("0") == digits.lstrip("0")]
    if not cands:
        sys.exit(f"❌ text/ 里找不到 ch{digits} 的提取件")
    return os.path.join(tdir, cands[0])


def main():
    book_dir, md_path = sys.argv[1], sys.argv[2]
    md = open(md_path, encoding="utf-8").read()
    m = re.search(r"^#\s*(\d+)\.", md, re.M)
    if not m:
        sys.exit("❌ H1 里找不到章号")
    tp = text_path(book_dir, m.group(1))
    raw = open(tp, encoding="utf-8").read()
    flat = norm(raw).lower()   # 契约：大小写、弯直引号不算差异
    problems = []
    warns = []

    # ── 1/2 引语块 ──
    blocks = []
    cur = None
    for line in md.splitlines():
        qm = QUOTE_RE.match(line.strip())
        if qm:
            cur = {"no": int(qm.group(1)), "quote": qm.group(2).strip(),
                   "fields": {}}
            blocks.append(cur)
            continue
        fm = FIELD_RE.match(line.strip())
        if fm and cur is not None:
            cur["fields"][fm.group(1)] = fm.group(2).strip()
            continue
    if not blocks:
        sys.exit("❌ 没找到引语块")

    last_no = 0
    for b in blocks:
        n = b["no"]
        if n != last_no + 1:
            problems.append(f"引语编号不连续：{last_no} → {n}")
        last_no = n
        q = norm(b["quote"]).lower()
        if q not in flat:
            problems.append(f"原句 {n}：text/ 逐字查无（{b['quote'][:60]}…）")
        words = len(b["quote"].split())
        # 句数口径：**整段引语（“…”）算一句**，引号外的旁白按句末标点计
        masked = re.sub(r"“[^”]*”", "Q", b["quote"])
        sents = len([s for s in re.split(r"(?<=[.!?])\s+", masked.strip())
                     if s.strip() and s.strip() != "Q"])
        if words > 100:
            problems.append(f"原句 {n}：{words} 词（>100，须按句界拆）")
        elif not (30 <= words <= 70):
            warns.append(f"原句 {n}：{words} 词（建议 30–70）")
        if not (1 <= sents <= 3):
            warns.append(f"原句 {n}：{sents} 句（建议 1–3）")
        for f in ("中文理解", "关键词", "为什么这样写", "读者视角提示"):
            if f not in b["fields"]:
                problems.append(f"原句 {n}：缺子项 {f}")
        zh = b["fields"].get("中文理解", "")
        if cjk_count(zh) < 6:
            problems.append(f"原句 {n}：中文理解汉字数 {cjk_count(zh)}（<6）")
        yy = b["fields"].get("为什么这样写", "")
        if cjk_count(yy) < 8:
            problems.append(f"原句 {n}：为什么这样写汉字数 {cjk_count(yy)}（<8）")
        if yy and cjk_ratio(yy) < 0.15:
            problems.append(f"原句 {n}：为什么这样写中文占比 {cjk_ratio(yy):.0%}（<15%）")
        zh_body = re.sub(r"[“\"][^”\"]*[”\"]", "", zh)
        lat = len(re.findall(r"[A-Za-z]", zh_body))
        han = cjk_count(zh)
        if lat + han:
            mix = lat / (lat + han)
            if mix > 0.35:
                problems.append(f"原句 {n}：中文理解英文字符占比 {mix:.0%}（>35%，判「夹杂理解」）")
            elif mix > 0.28:
                warns.append(f"原句 {n}：中文理解英文字符占比 {mix:.0%}（逼近 35% 红线）")
        kw = b["fields"].get("关键词", "")
        for k in [x.strip() for x in re.split(SEP, kw) if x.strip()]:
            if norm(k).lower() not in q:
                problems.append(f"原句 {n}：关键词「{k}」不在本块引语内")
            if len(k.split()) > 8:
                warns.append(f"原句 {n}：关键词「{k}」超过 8 词（整句照抄？）")

    # ── 3 词汇表 ──
    if "## 本章词汇" not in md:
        problems.append("缺 ## 本章词汇")
    else:
        sec = md.split("## 本章词汇")[1].split("## 一句话总结")[0]
        seen = {}
        tier = None
        for line in sec.splitlines():
            s = line.strip()
            tm = TIER_RE.match(s)
            if tm:
                tier = tm.group(2)
                continue
            if not s.startswith("|") or s.startswith("|---") or "词/短语" in s:
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 3:
                problems.append(f"词汇表列数异常：{cells}")
                continue
            head, meaning, ex = cells[0], cells[1], cells[2]
            if head in seen:
                problems.append(f"词条重复：「{head}」")
            seen[head] = tier
            if norm(ex).lower() not in flat:
                problems.append(f"词汇 {tier}「{head}」：例句在本章查无")
            if head.lower() not in ex.lower():
                problems.append(f"词汇 {tier}「{head}」：例句不含词头")
            if re.search(r"[一-鿿]", ex):
                problems.append(f"词汇 {tier}「{head}」：例句混入中文")

    if "## 一句话总结" not in md:
        problems.append("缺 ## 一句话总结")
    else:
        tail = md.split("## 一句话总结")[1].strip()
        if len(tail) < 10:
            problems.append("一句话总结为空")

    print(f"== {os.path.basename(md_path)} · 引语 {len(blocks)} 块 · 词条 {len(seen)} 条 ==")
    for w in warns:
        print("  ⚠️", w)
    for p in problems:
        print("  ❌", p)
    if not problems:
        print("  ✅ 自查无问题")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
