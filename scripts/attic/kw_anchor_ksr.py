import re, glob, sys

# KSR（Kiss Slay Replay）关键词锚定检查器 —— 自建门禁工具，不占用 verify_/check_ 系列命名。
# 规则 9b：块内"关键词"的英文词必须命中该块引语（允许词形变化，剔除 stop words）。
# 块感知版（2026-09-15 修）：旧版只取 `> **原句 N:**` 首行、关键词搜索窗口 8 行——
#   对 ch21/ch22 的多行引语块产生两类假报警：
#   ① 续行把 `**关键词：**` 顶出 8 行窗口 → 假 MISSING；
#   ② 关键词取自续行 → qf 只含首行 → 假 VIOLATION（实证 ch22 原句 2：life/death/parse/out/actual/stakes 6 处）。
#   修法：按块边界（下一 `> **原句` 或下一个 `## `）切片，引语 = 块内所有非结构行。

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
STOP = {"the", "and", "but", "not", "all", "his", "her", "its", "you", "don", "didn",
        "was", "were", "has", "had", "can", "cant", "that", "this", "with", "from",
        "for", "they", "she", "him", "our", "their", "who", "what", "how", "why",
        "when", "where", "been", "being", "would", "could", "should", "just", "like",
        "about", "after", "before", "over", "under", "into", "onto", "every", "some",
        "then", "there", "here", "very", "also", "than", "too", "only"}

# 结构性行前缀：引语续行不会以这些开头
STRUCT = ("**", "## ", "> ", "|", "---", "### ", "# ")


def flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


tot = 0
bad = 0
blocks = 0
for f in sorted(glob.glob(BOOK + "/ch*.md")):
    L = open(f, encoding="utf-8").read().split("\n")
    # 定位所有 `> **原句 N:**` 行号
    starts = []
    for i, l in enumerate(L):
        if re.match(r"^> \*\*原句 (\d+):\*\*", l):
            starts.append(i)
    if not starts:
        continue
    for k, i in enumerate(starts):
        end = starts[k + 1] if k + 1 < len(starts) else len(L)
        # 块遇到下一个章节标题即止
        for j in range(i + 1, end):
            if L[j].startswith("## "):
                end = j
                break
        blocks += 1
        # 块内引语 = 原句行正文 + 续行（非结构行）
        quote_parts = [re.match(r"^> \*\*原句 (\d+):\*\* (.*)", L[i]).group(2)]
        for j in range(i + 1, end):
            lj = L[j].strip()
            if not lj or lj.startswith(STRUCT):
                continue
            quote_parts.append(lj)
        kf = None
        for j in range(i + 1, end):
            if L[j].startswith("**关键词：**"):
                kf = L[j].replace("**关键词：**", "").strip()
                break
        if kf is None:
            print("MISSING 关键词", f.split("/")[-1], "原句",
                  re.match(r"^> \*\*原句 (\d+):\*\*", L[i]).group(1))
            continue
        qf = flat(" ".join(quote_parts))
        for kw in re.split(r"[,，、;；]", kf):
            for t in re.findall(r"[A-Za-z’']+", kw):
                tf = flat(t)
                if len(tf) < 3 or tf in STOP:
                    continue
                tot += 1
                if tf not in qf:
                    print("VIOLATION", f.split("/")[-1], "原句",
                          re.match(r"^> \*\*原句 (\d+):\*\*", L[i]).group(1), t)
                    bad += 1

print(f"关键词锚定检查：{blocks} 个引语块，共 {tot} 个英文词，违规 {bad} 处")
