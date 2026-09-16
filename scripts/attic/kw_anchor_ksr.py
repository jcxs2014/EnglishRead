import re, glob, sys

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
STOP = {"the", "and", "but", "not", "all", "his", "her", "its", "you", "don", "didn",
        "was", "were", "has", "had", "can", "cant", "that", "this", "with", "from",
        "for", "they", "she", "him", "our", "their", "who", "what", "how", "why",
        "when", "where", "been", "being", "would", "could", "should", "just", "like",
        "about", "after", "before", "over", "under", "into", "onto", "every", "some",
        "been", "then", "there", "here", "very", "been", "also", "than", "too", "only"}

def flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

tot = 0
bad = 0
files = sorted(glob.glob(BOOK + "/ch*.md"))
for f in files:
    L = open(f, encoding="utf-8").read().split("\n")
    for i, l in enumerate(L):
        m = re.match(r"^> \*\*原句 (\d+):\*\* (.*)", l)
        if not m:
            continue
        kf = None
        for j in range(i + 1, min(i + 8, len(L))):
            if L[j].startswith("**关键词：**"):
                kf = L[j].replace("**关键词：**", "").strip()
                break
        if kf is None:
            print("MISSING 关键词", f, "原句", m.group(1))
            continue
        qf = flat(m.group(2))
        for kw in re.split(r"[,，、;；]", kf):
            for t in re.findall(r"[A-Za-z’']+", kw):
                tf = flat(t)
                if len(tf) < 3 or tf in STOP:
                    continue
                tot += 1
                if tf not in qf:
                    print("VIOLATION", f.split("/")[-1], "原句", m.group(1), t)
                    bad += 1

print(f"关键词锚定检查：共 {tot} 个英文词，违规 {bad} 处")
