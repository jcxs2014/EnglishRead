#!/usr/bin/env python3
"""批量验收：books batch checker（只读，不改任何文件）

用法：python3 scripts/batch_check.py "<书目录>" ch01 ch02 ch03 ...

对每章输出（不依赖 scripts/ 源码，只按创建卡 + 契约的判据自查）：
  ① 引语逐段逐字命中本章 text/（按 `…` 切段，每段须连续命中）
  ② 块序：各块在 text/ 中的偏移必须递增
  ③ 词条例句：每条例句须逐字命中本章 text/，且**例句必须含词头本身**
  ④ 块数是否在 3–10（ novels profile）
  ⑤ 引语块词数（>100 提示；<30 提示）
  ⑥ 子项齐全 / 导航 5 项 / 必备节 / H1 形态
  ⑦ 可疑模板套话 / 写作期自述残留

退出码：0 = 全部通过；1 = 有阻断（逐字查无 / 块序错 / 例句查无 / 缺子项）
"""
import os
import re
import sys

PROFILE_MIN_BLOCKS = 3
PROFILE_MAX_BLOCKS = 10
WARN_MAX_WORDS = 100
WARN_MIN_WORDS = 30

NAV_ITEMS = ["一句话概括", "情感弧线位置", "Tropes", "人物弧线", "叙事手法"]
SUBITEMS = ["中文理解", "关键词", "为什么这样写", "读者视角提示"]
TEMPLATE_PHRASES = [
    "本句描写了场景与人物的反应",
    "重新定义 as",
    "此句通过修辞与节奏把人物的",
    "为后续情节的转折埋下伏笔",
]
SELFWRITE = [
    "写作期自查", "写作期备注", "不作为独立引语块计", "待补充",
    "Let me fix", "end anchor", "K flag", "anchor = ",
]


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def find_text(book, ch):
    tdir = os.path.join(book, "text")
    for f in sorted(os.listdir(tdir)):
        if re.match(rf"^{ch}[_. ]", f) and f.endswith(".txt"):
            return os.path.join(tdir, f)
    return None


def check(book, ch):
    problems, warns = [], []
    md = None
    for f in sorted(os.listdir(book)):
        if f.startswith(ch + " ") and f.endswith(".md"):
            md = os.path.join(book, f)
            break
    if not md:
        return [f"{ch}: 找不到 md 文件"], []
    body = open(md, encoding="utf-8").read()
    tp = find_text(book, ch)
    if not tp:
        return [f"{ch}: 找不到 text/{ch}_*.txt"], []
    raw = open(tp, encoding="utf-8").read()
    tf = flat(raw)

    # ① 引语逐字 + ② 块序
    quotes = re.findall(r"^> \*\*原句 \d+:\*\* (.+)$", body, re.M)
    if not quotes:
        problems.append(f"{ch}: 没有引语块")
    offsets = []
    for i, q in enumerate(quotes, 1):
        qq = q.strip()
        if qq and qq[0] in '"“' and qq[-1] in '"”':
            qq = qq[1:-1]
        segs = [s.strip().rstrip(" .") for s in qq.split("…") if s.strip()]
        if not segs:
            problems.append(f"{ch} 块{i}: 引语为空")
            continue
        for s in segs:
            if s not in tf:
                problems.append(f"{ch} 块{i}: 片段查无 → {s[:70]}")
        w = len(qq.split())
        if w > WARN_MAX_WORDS:
            warns.append(f"{ch} 块{i}: 引语 {w} 词（>100 提示）")
        elif w < WARN_MIN_WORDS:
            warns.append(f"{ch} 块{i}: 引语 {w} 词（<30 提示）")
        # 偏移：取第一段在原文中的位置（查无则跳过该块，不中断序列比较）
        off = tf.find(segs[0])
        if off >= 0:
            offsets.append((i, off))
    # 块序：只在**都能定位**的块之间比较；定位不到的块单独提示
    if len(offsets) < len(quotes):
        missing = len(quotes) - len(offsets)
        warns.append(f"{ch}: {missing} 块无法定位偏移（片段查无），块序仅在可定位块间比较")
    for k in range(len(offsets) - 1):
        if offsets[k][1] >= offsets[k + 1][1]:
            problems.append(
                f"{ch}: 块序倒置（块{offsets[k][0]} off={offsets[k][1]} "
                f">= 块{offsets[k+1][0]} off={offsets[k+1][1]}）"
            )

    # 块数
    n = len(quotes)
    if n < PROFILE_MIN_BLOCKS or n > PROFILE_MAX_BLOCKS:
        problems.append(f"{ch}: 块数 {n} 越出 profile {PROFILE_MIN_BLOCKS}–{PROFILE_MAX_BLOCKS}")

    # ③ 词条例句
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|$", body, re.M):
        w, _, ex = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        if set(w) <= set("-: ") or w == "词/短语":
            continue
        if ex.rstrip(" .") not in tf:
            problems.append(f"{ch}: 词条「{w}」例句查无 → {ex[:60]}")
            continue
        if w.lower() not in ex.lower():
            warns.append(f"{ch}: 词条「{w}」例句未含词头")

    # ⑥ 结构
    for item in NAV_ITEMS:
        if item not in body:
            problems.append(f"{ch}: 导航缺「{item}」")
    for item in SUBITEMS:
        if item not in body:
            problems.append(f"{ch}: 缺子项「{item}」")
    for sec in ["## 本章导航", "## 精读", "## 本章词汇", "## 一句话总结"]:
        if sec not in body:
            problems.append(f"{ch}: 缺必备节「{sec}」")
    if not re.search(r"^# \d{2}\. ", body, re.M):
        problems.append(f"{ch}: H1 形态不符（应 `# NN. 标题`）")
    for tier in ["⭐⭐⭐", "⭐⭐", "⭐"]:
        if tier not in body:
            problems.append(f"{ch}: 词汇缺档位 {tier}")
    # 一句话总结必须有正文
    m = re.search(r"^## 一句话总结\s*\n+(.+)$", body, re.M)
    if not m or len(m.group(1).strip()) < 10:
        problems.append(f"{ch}: 一句话总结缺正文")

    # ⑦ 套话与自述
    for p in TEMPLATE_PHRASES:
        if p in body:
            problems.append(f"{ch}: 模板套话「{p}」")
    for p in SELFWRITE:
        if p in body:
            problems.append(f"{ch}: 写作期自述残留「{p}」")
    return problems, warns


def main():
    book = sys.argv[1]
    chapters = sys.argv[2:]
    allp, allw = [], []
    for ch in chapters:
        p, w = check(book, ch)
        allp += p
        allw += w
        print(f"── {ch} ── {'✅ 无阻断' if not p else f'❌ {len(p)} 阻断'}")
        for x in p:
            print("   ❌", x)
        for x in w:
            print("   ⚠️ ", x)
    print(f"\n{'='*50}")
    print(f"阻断 {len(allp)} ｜ 提示 {len(allw)}")
    return 1 if allp else 0


if __name__ == "__main__":
    sys.exit(main())
