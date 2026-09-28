import re, os, unicodedata
base = os.path.dirname(os.path.abspath(__file__))
def flat(s):
    s = unicodedata.normalize('NFKC', s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2014','-'),('\u2013','-')]:
        s = s.replace(a,b)
    return re.sub(r'\s+',' ', s).strip().lower()
texts = {n: flat(open(f"{base}/text/ch{n:02d}_chapter_{n}.txt", encoding='utf-8').read()) for n in range(1,13)}
mdf = {5:"ch05 the boundless life elsewhere.md",6:"ch06 the world was growing smaller.md",
       7:"ch07 the captain of the second fifteen.md",8:"ch08 his father had no friends.md"}
def variants(q):
    cur={q}
    for _ in range(6):
        new=set(cur)
        for x in cur:
            if x[:1] in '"“‘\'' and len(x)>20: new.add(x[1:])
            if x[-1:] in '"“’\'.' and len(x)>20: new.add(x[:-1])
        cur=new
    return {x for x in cur if len(x)>20}
for n,f in mdf.items():
    for i,ln in enumerate(open(os.path.join(base,f),encoding='utf-8').read().split('\n'),1):
        m=re.match(r'^> \*\*原句 (\d+)：\*\*\s*(.+)$', ln)
        if not m: continue
        q=flat(m.group(2))
        if not any(v in texts[n] for v in variants(q)):
            print(f"MISS {f} L{i} q#{m.group(1)}: {m.group(2)[:100]}")
print("done")
