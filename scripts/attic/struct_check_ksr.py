import re, sys

files = sys.argv[1:]
for f in files:
    lines = open(f, encoding="utf-8").read().split("\n")
    rows = [l for l in lines if l.startswith("| ") and "\u8bcd/\u77ed\u8bed" not in l and not set(l) <= set("|- ")]
    bad = [l for l in rows if len(l.split("|")) < 5 or not l.split("|")[3].strip()]
    print(f, "rows:", len(rows), "empty:", len(bad))
    for l in bad:
        print("   ", l)
    s = open(f, encoding="utf-8").read().split("## \u672c\u7ae0\u8bcd\u6c47")[1]
    for m in re.finditer(r"^### (.+)", s, re.M):
        nxt = s.find("\n###", m.end())
        if nxt == -1:
            nxt = s.find("\n## ", m.end())
        r = [l for l in s[m.end():nxt].split("\n") if l.startswith("| ") and "\u8bcd/\u77ed\u8bed" not in l]
        print("   ", m.group(1), len(r))
