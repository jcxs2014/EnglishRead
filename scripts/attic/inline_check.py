"""校验 md 分析层/总览层里的行内英文片段是否逐字存在于 text/。
只取「纯英文短语」（无 CJK、≥2 个英文词），逐条对全部 15 章 text/ 做 flat 断言。
跨章引用在报告中单列（提示型，不算缺陷）。"""
import re, glob, sys, os
nf = lambda s: re.sub(r'\s+', ' ', s).strip()
CJK = re.compile(r'[一-鿿　-〿＀-￯]')
WORD = re.compile(r'[A-Za-z][A-Za-z’\'-]*')

def texts(book):
    T = {}
    for p in glob.glob(f"{book}/text/ch*.txt"):
        c = int(re.match(r'ch(\d+)_', p.split('/')[-1]).group(1))
        T[c] = nf(open(p, encoding='utf-8').read())
    return T

def segments(md, min_words=2):
    """抽取所有连续英文词组（跨标点但不含 CJK），≥min_words 个词。"""
    out, buf = [], []
    for ch in md:
        if CJK.search(ch):
            if len(buf) >= min_words:
                out.append(nf("".join(buf)))
            buf = []
        elif WORD.match(ch):
            buf.append(ch)
        else:
            if len(buf) >= min_words:
                out.append(nf("".join(buf)))
            buf = []
    if len(buf) >= min_words:
        out.append(nf("".join(buf)))
    return out

def main():
    book = sys.argv[1]
    T = texts(book)
    allt = " ‖ ".join(T.values())
    files = sys.argv[2:] or sorted(glob.glob(f"{book}/*.md"))
    total = ok = 0
    report = []
    for f in files:
        md = open(f, encoding='utf-8').read()
        for s in segments(md):
            if s in allt:
                ok += 1
                continue
            total += 1
            where = [c for c, t in T.items() if s in t]
            report.append((os.path.basename(f), s, where))
    print(f"=== 行内英文逐字核查（{os.path.basename(book)}）===")
    print(f"  ✅ 逐字 {ok} ｜ ❌ 零命中 {total}")
    for f, s, where in report:
        tag = f"→ 实为 ch{','.join(map(str, where))}" if where else "→ 全书查无"
        print(f"  ❌ {f}: 「{s[:80]}」{tag}")
    return 0 if total == 0 else 1

sys.exit(main())
