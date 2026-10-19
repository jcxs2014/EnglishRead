#!/usr/bin/env python3
"""词汇表修复器（取证驱动）：

对「## 本章词汇」里例句不命中的行，到该章 text/ 里找**含该词头的整行原文**，
替换例句；词头本身本章查无的行，按指定替换表整行替换（词头+释义+例句）。

硬约束（AGENTS 第 5 条 / 记忆 #2187）：
  · 例句必须是**本章 text/ 的整行逐字**（不得跨行拼接、不得加省略号）
  · 词头必须在本章 text/ 里真实出现（A 类虚构 ⇒ 换词）

用法：
    python3 vocab_repair.py "<书目录>" <补丁.py>
补丁.py 里：REPLACE = { "<md 文件名>": { "<旧词头>": ("<新词头>", "<新释义>", "<新例句>") } }
未在 REPLACE 里出现的行，只换例句（自动取候选行）。
"""
import glob
import os
import re
import sys
import tempfile

BOOK = sys.argv[1]
PATCH = sys.argv[2]
ns = {}
with open(PATCH, encoding="utf-8") as f:
    exec(compile(f.read(), PATCH, "exec"), ns)
REPLACE = ns.get("REPLACE", {})

RE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")
PLACEHOLDER = re.compile(r"^\s*[-—]\s*$|^no$|not in text|未出现|未在原文", re.I)


def flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def chapter_lines(book, fname):
    cnum = re.match(r"ch(\d+)", fname).group(1)
    out = []
    for tp in sorted(glob.glob(os.path.join(book, "text", "ch*.txt"))):
        if os.path.basename(tp).startswith("ch" + cnum + "_"):
            out += [l.strip() for l in open(tp, encoding="utf-8").read().split("\n") if l.strip()]
    return out


def pick_example(lines, head, old_ex):
    """从本章 text/ 里挑一段**含该词头、单行内连续**的逐字原文片段。"""
    hf = flat(head)
    cands = []
    for l in lines:
        if not (hf and hf in flat(l)):
            continue
        ws = l.split()
        low = [w.lower().strip(".,;:!?\"'()[]—–") for w in ws]
        for i, w in enumerate(low):
            if hf in flat(w) or flat(w) in hf and flat(w):
                frag = " ".join(ws[max(0, i - 4):i + 8])
                if len(frag.split()) >= 3:
                    cands.append(frag)
                break
    if not cands:
        return None
    # 优先与旧例句首词相近（保留作者本意），其次片段较短
    old_words = [w for w in re.findall(r"[A-Za-z']+", old_ex or "") if len(w) > 3]
    def score(l):
        lw = set(w.lower() for w in re.findall(r"[A-Za-z']+", l))
        overlap = len(lw & {w.lower() for w in old_words})
        return (-overlap, abs(len(l) - 90))
    cands.sort(key=score)
    return cands[0]


total_fixed = 0
for md in sorted(glob.glob(os.path.join(BOOK, "ch*.md")),
                 key=lambda x: int(re.search(r"ch(\d+)", x).group(1))):
    fname = os.path.basename(md)
    lines = chapter_lines(BOOK, fname)
    body = open(md, encoding="utf-8").read().split("\n")
    repl = REPLACE.get(fname, {})
    changed = False
    in_vocab = False
    for i, ln in enumerate(body):
        if re.match(r"^##\s*本章词汇", ln):
            in_vocab = True
            continue
        if in_vocab and re.match(r"^##\s", ln):
            in_vocab = False
        if not in_vocab:
            continue
        m = RE_ROW.match(ln)
        if not m:
            continue
        head, gloss, ex = m.group(1), m.group(2), m.group(3)
        if head in ("词/短语", "词", "词汇") or set(head) <= set("- "):
            continue
        head_in = flat(head) in flat("\n".join(lines))
        ex_ok = (not PLACEHOLDER.match(ex.strip())) and flat(ex) and \
            flat(ex) in flat("\n".join(lines))
        if ex_ok and head_in:
            continue
        if head in repl:
            nh, ng, nex = repl[head]
            body[i] = f"| {nh} | {ng} | {nex} |"
            changed = True
            total_fixed += 1
            continue
        if head_in:
            ne = pick_example(lines, head, ex)
            if ne:
                body[i] = f"| {head} | {gloss} | {ne} |"
                changed = True
                total_fixed += 1
            else:
                print(f"⚠️ {fname}:{i+1} {head} —— 本章找不到含该词的整行，需人工指定")
        else:
            print(f"⚠️ {fname}:{i+1} {head} —— 词头本章查无且未在替换表中，需人工指定")
    if changed:
        out = "\n".join(body)
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(md), suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        os.replace(tmp, md)
        print(f"✓ {fname} 已更新")
print(f"—— 共修复 {total_fixed} 行 ——")
