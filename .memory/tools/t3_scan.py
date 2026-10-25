#!/usr/bin/env python3
"""t3_scan.py — T3 深审的 R4 辅助筛查器（人判前置，**不替代 R4 人判**）

用法：
    python3 .memory/tools/t3_scan.py "<书目录>" [ch01 ch02 …]

扫三类「机器门禁结构上查不到」的东西，全部只报**候选**，定性由人判：

  ① §0.2 专名 ∉ 本块引语
     判据原文（审查表 §0.2）：「分析里出现的每个人名/动作/关系，都必须在这段引语里；
     不在，就是引语选短了。」
     ⇒ 抽分析层（中文理解/关键词/为什么这样写/读者视角提示）里的拉丁专名，
       逐个查它是否在本块引语里。不在 ⇒ 候选。
     分档：**阻断型候选**＝该名在本章原文里根本查无（凭空生词）；
           **提示型候选**＝该名在本章原文里有（职衔/前向引用/别处出场），
           但不在本块引语内。

  ② 章内/跨章相对指认（「上一章」「下一章」「前文」「后面会……」）
     跨章相对指认在成品里是缺陷（读者看不到别的章）；
     章内相对指认是提示层职能（引导读者章内前后对照）⇒ 分两档。

  ③ 块词数软区间（<30 词 / >100 词）与句数

退出码：0 = 无候选（不是「查过且通过」）；1 = 有候选。
注意：本脚本**只做候选提取**，报告必须写「判了多少 / 跳了多少」。
"""
import os
import re
import sys

QUOTE_RE = re.compile(r"^> \*\*原句 (\d+):\*\*\s*(.*)$")
FIELD_RE = re.compile(r"^\*\*(中文理解|关键词|为什么这样写|读者视角提示)\*\*：\s*(.*)$")

# 相对指认：跨章 vs 章内 vs 待人判
# ⚠️ 口径（2026-10-25 首版跑偏后订正）：
#   「这一章/本章/章首/章末/开篇」= **章内**（指正在读的这一章），不是跨章；
#   「后文/下文/前文/上文」= **待人判**——既可能指本章后续段落，也可能是全书后续；
#   「上一章/下一章/第N章」= 跨章（在成品里是缺陷：读者看不到别的章）。
REL_CROSS = re.compile(
    r"(上一章|下一章|前一章|后一章|上章|下章|前章|后章|第[0-9一二三四五六七八九十百]+章|"
    r"前面(?:提|说|写|讲)过|上一节|下一节|前一节|后一节)")
REL_INCHAP = re.compile(
    r"(这一章|这一节|本章|本节|章首|章末|章内|开篇|全章|"
    r"前面(?:那|这|几)|后面(?:那|这|几)|上面(?:那|这)|下面(?:那|这)|"
    r"后面(?:会|将|还)|前面(?:一|两|几)块|后面(?:一|两|几)块|"
    r"本(?:段|块|节|章|书))")
REL_AMBIG = re.compile(r"(后文|下文|前文|上文)")

# 拉丁专名候选：首字母大写的词（排除句首常见虚词与普通词）
STOP = {
    "I", "A", "An", "The", "But", "And", "Or", "So", "If", "It", "He", "She", "They",
    "We", "You", "This", "That", "There", "Here", "When", "What", "Why", "How", "Who",
    "Then", "Now", "Not", "No", "Yes", "Do", "Does", "Did", "Was", "Were", "Will",
    "Would", "Can", "Could", "Should", "Has", "Have", "Had", "My", "Your", "His", "Her",
    "Their", "Our", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
    "Nine", "Ten", "After", "Before", "Between", "Without", "Because", "While", "For",
    "From", "With", "Into", "Out", "Up", "Down", "Over", "Under", "About", "Like",
    "As", "At", "By", "In", "On", "To", "Of", "Is", "Are", "Was", "Been", "Have",
    "Chapter", "Prologue", "Epilogue", "Part", "MR", "MRS", "MS", "DR", "OK",
    "Theres", "Im", "Id", "Ive", "Dont", "Cant", "Wont", "Youre", "Youll", "Thats",
    "Its", "Lets", "Ill", "Hes", "Shes", "Theyre", "Weve", "Youve", "Havent",
}
NAME_RE = re.compile(r"\b([A-Z][a-zA-Z]{1,}(?:\s+[A-Z][a-zA-Z]+)?)\b")


def text_path(book_dir, chno):
    tdir = os.path.join(book_dir, "text")
    digits = f"{int(chno):02d}"
    for f in sorted(os.listdir(tdir)):
        if re.match(rf"^ch{digits}([_. ].*)?\.txt$", f):
            return os.path.join(tdir, f)
    return None


def parse_blocks(md):
    blocks, cur = [], None
    for line in md.splitlines():
        s = line.strip()
        qm = QUOTE_RE.match(s)
        if qm:
            cur = {"no": int(qm.group(1)), "quote": qm.group(2).strip(), "fields": {}}
            blocks.append(cur)
            continue
        fm = FIELD_RE.match(s)
        if fm and cur is not None:
            cur["fields"][fm.group(1)] = fm.group(2).strip()
    return blocks


def names_in(text):
    out = set()
    for m in NAME_RE.finditer(text):
        tok = m.group(1)
        if tok in STOP:
            continue
        parts = tok.split()
        if all(p in STOP for p in parts):
            continue
        # 单个词：必须是「不在句首」或本身像专名（小写开头不行）
        out.add(tok)
    return out


def main():
    book_dir = sys.argv[1]
    want = set(sys.argv[2:])
    files = sorted(f for f in os.listdir(book_dir)
                   if f.startswith("ch") and f.endswith(".md")
                   and re.match(r"^ch\d\d ", f))
    if want:
        files = [f for f in files if f[:4] in want]
    total = {"name_block": 0, "name_hint": 0, "rel_cross": 0, "rel_ambig": 0,
             "wordlen": 0, "blocks": 0, "chapters": 0}
    # 全书语料（专名「凭空生词」的判据口径＝**全书**查无，不是本章查无：
    # 该名在本章没有、但全书有 ⇒ 前向引用/职衔 ⇒ 提示型，不是阻断）
    book_raw = ""
    tdir = os.path.join(book_dir, "text")
    for f in sorted(os.listdir(tdir)):
        if f.startswith("ch") and f.endswith(".txt"):
            book_raw += open(os.path.join(tdir, f), encoding="utf-8").read() + "\n"
    book_low = book_raw.lower()
    for fn in files:
        md = open(os.path.join(book_dir, fn), encoding="utf-8").read()
        m = re.search(r"^#\s*(\d+)\.", md, re.M)
        if not m:
            continue
        chno = m.group(1)
        tp = text_path(book_dir, chno)
        raw = open(tp, encoding="utf-8").read() if tp else ""
        blocks = parse_blocks(md)
        total["chapters"] += 1
        total["blocks"] += len(blocks)
        lines = []
        for b in blocks:
            q = b["quote"]
            ql = q.lower()
            for fname, fval in b["fields"].items():
                if fname == "关键词":
                    continue
                for nm in sorted(names_in(fval)):
                    if nm.lower() in ql:
                        continue
                    if nm.lower() in book_low:
                        lines.append(f"    [提示候选] 原句 {b['no']} · {fname}：专名「{nm}」不在本块引语内（全书有此名）")
                        total["name_hint"] += 1
                    else:
                        lines.append(f"    [阻断候选] 原句 {b['no']} · {fname}：专名「{nm}」不在本块引语内，且**全书原文查无**")
                        total["name_block"] += 1
                for rm in REL_CROSS.finditer(fval):
                    seg = fval[max(0, rm.start() - 12):rm.end() + 12]
                    lines.append(f"    [跨章相对] 原句 {b['no']} · {fname}：「{rm.group(0)}」（…{seg}…）")
                    total["rel_cross"] += 1
                for rm in REL_AMBIG.finditer(fval):
                    seg = fval[max(0, rm.start() - 14):rm.end() + 14]
                    lines.append(f"    [待人判] 原句 {b['no']} · {fname}：「{rm.group(0)}」（…{seg}…）")
                    total["rel_ambig"] += 1
            w = len(q.split())
            if w < 30 or w > 100:
                lines.append(f"    [块词数] 原句 {b['no']}：{w} 词")
                total["wordlen"] += 1
        if lines:
            print(f"── {fn} ──")
            print("\n".join(lines))
    print("=" * 50)
    print(f"章 {total['chapters']} ｜ 块 {total['blocks']} ｜ "
          f"专名∉块内：阻断候选 {total['name_block']} · 提示候选 {total['name_hint']} ｜ "
          f"相对指认：跨章 {total['rel_cross']} · 待人判 {total['rel_ambig']} ｜ 块词数越界 {total['wordlen']}")
    return 1 if (total["name_block"] or total["name_hint"] or total["rel_cross"]
                 or total["rel_ambig"] or total["wordlen"]) else 0


if __name__ == "__main__":
    sys.exit(main())
