import sys, os, re
mdpath=sys.argv[1]
name=os.path.basename(mdpath)[:-3]
txtpath=os.path.join(os.path.dirname(mdpath), "text", name + ".txt")
md=open(mdpath).read()
text=open(txtpath).read() if os.path.exists(txtpath) else ""
def fp(s): return re.sub(r'[^a-z0-9]','',s.lower())
ft=fp(text)
blocks=re.findall(r'\*\*[①②③④⑤⑥⑦⑧⑨⑩]\*\*\s+"(.+?)"', md, re.S)
print(f"### {name}  ({len(blocks)} blocks)")
fails=[]
for i,q in enumerate(blocks,1):
    qq=q.replace('\n',' ').strip()
    f=fp(qq)[:60]
    hit='HIT' if f in ft else 'FAIL'
    print(f"  [{i}] {hit} :: {qq[:120]}")
    if hit=='FAIL': fails.append((i,qq))
if fails:
    print(f"  => {len(fails)} FAIL(s) to fix")
