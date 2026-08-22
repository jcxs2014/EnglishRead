import re, os, sys
from datetime import date

# 用法: python3 scan.py [source]
#   source: parisreview(默认) | granta | brainpickings | lithub | economist
SRC = sys.argv[1] if len(sys.argv) > 1 else "parisreview"

if SRC == "economist":
    # economist 按期刊日期分目录，无统一"今日"目录；扫描最新一个
    base = f"/Users/jcxs2014/Documents/Works/EnglishRead/economist"
    sub = sorted(os.listdir(base))[-1]
    OUT = os.path.join(base, sub)
else:
    OUT = f"/Users/jcxs2014/Documents/Works/EnglishRead/{SRC}/{date.today():%Y-%m-%d_%A}"

# 各源题材/敏感度（idx -> 说明）；未知 idx 显示 '?'
flags = {
    "parisreview": {
        "01": {"topic":"history/religion book review (Jonestown, cult)", "sensitive":"medium — Jonestown mass suicide, handled academically"},
        "02": {"topic":"NYC racetrack demolition / urban essay", "sensitive":"none"},
        "03": {"topic":"personal essay (testing + arbitration)", "sensitive":"none"},
        "04": {"topic":"Shen Yun performance review", "sensitive":"HIGH — Shen Yun linked to banned org; SKIP"},
        "05": {"topic":"sports memoir review (boxing)", "sensitive":"none"},
        "06": {"topic":"family essay (father + film)", "sensitive":"none"},
        "07": {"topic":"science (interstitium, human body)", "sensitive":"none"},
        "08": {"topic":"personal/reading reflection", "sensitive":"none"},
        "09": {"topic":"literary history (Charles brockden Brown)", "sensitive":"none"},
        "10": {"topic":"travel essay", "sensitive":"none"},
    },
    "granta": {
        "01": {"topic":"literary fiction / memoir (Granta)", "sensitive":"none"},
        "02": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "03": {"topic":"reportage / essay (Granta)", "sensitive":"none"},
        "04": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "05": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "06": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "07": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "08": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "09": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
        "10": {"topic":"literary non-fiction (Granta)", "sensitive":"none"},
    },
    "brainpickings": {
        "01": {"topic":"idea/science essay (The Marginalian)", "sensitive":"none"},
        "02": {"topic":"idea/ science essay (The Marginalian)", "sensitive":"none"},
        "03": {"topic":"idea essay (The Marginalian)", "sensitive":"none"},
        "04": {"topic":"idea essay (The Marginalian)", "sensitive":"none"},
        "05": {"topic":"idea essay (The Marginalian)", "sensitive":"none"},
    },
    "lithub": {
        "01": {"topic":"lit essay / book review (Lit Hub)", "sensitive":"none"},
        "02": {"topic":"lit essay / book review (Lit Hub)", "sensitive":"none"},
        "03": {"topic":"lit essay / book review (Lit Hub)", "sensitive":"none"},
        "04": {"topic":"lit essay / book review (Lit Hub)", "sensitive":"none"},
        "05": {"topic":"lit essay / book review (Lit Hub)", "sensitive":"none"},
    },
    "economist": {},  # economist 文章按标题命名，无 idx 前缀体系
}

fl = flags.get(SRC, {})
print(f"### scanning source=[{SRC}]  out={OUT}\n")

if not os.path.isdir(OUT):
    print(f"  (目录不存在: {OUT})")
    sys.exit()

for f in sorted(os.listdir(OUT)):
    if not f.endswith(".txt"):
        continue
    idx = f.split("_")[0]
    path = os.path.join(OUT, f)
    txt = open(path, encoding="utf-8").read()
    paras = [p for p in re.split(r'\n\s*\n', txt) if len(p) > 60]
    sents = re.findall(r'[.!?]["\'\)]?\s', txt)
    print(f"\n### {idx} | {f[:45]}...")
    print(f"   topic:  {fl.get(idx,{}).get('topic','?')}")
    print(f"   risk:   {fl.get(idx,{}).get('sensitive','?')}")
    print(f"   ~{len(paras)} blocks, ~{len(sents)} sentences, {len(txt)} chars")
    lines = [l.strip() for l in txt.split('\n') if l.strip() and not l.startswith('#') and 'Source:' not in l and 'URL:' not in l and 'Published' not in l and '---' not in l]
    for l in lines:
        if len(l) > 40:
            print(f"   opener: {l[:140]}")
            break
