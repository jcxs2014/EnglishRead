#!/usr/bin/env python3
"""章号指认机械裁决：散文行按 `chNN` 切段，段内专名/中文引语词必须出现在该章 text/。
退出码 0=无阻断；1=有阻断。"""
import os,re,sys,glob
STOP={"The","And","But","This","That","With","When","What","Then","They","There","Their","Chapter",
      "Gods","Well","Oh","Just","Like","Love","Hope","Help","Hear","Here","Hold","Home","Hate","How",
      "Why","Yes","No","Man","Miss","Dread","Death","Dark","Deep","One","Two","Three","Fey","Way"}
def load(book):
    ch={}
    for p in glob.glob(os.path.join(book,"text","*.txt")):
        m=re.search(r'ch(\d+)',os.path.basename(p))
        if m: ch[f"ch{int(m.group(1)):02d}"]=open(p,encoding="utf-8").read()
    return ch

def segs(s):
    """按 chNN 切段：返回 [(章号, 该章号之后到下一个章号之前的文本)]"""
    ms=list(re.finditer(r'\bch(\d{1,2})\b',s))
    out=[]
    for i,m in enumerate(ms):
        nn=int(m.group(1))
        end=ms[i+1].start() if i+1<len(ms) else len(s)
        out.append((nn,s[m.end():end]))
    return out

def run(book):
    ch=load(book)
    bad=[]
    for f in sorted(glob.glob(os.path.join(book,"*.md"))):
        b=os.path.basename(f)
        for i,l in enumerate(open(f,encoding="utf-8"),1):
            s=l.strip()
            if not s or s.startswith(("|","#","> ")): continue
            if len(re.findall(r'[\u4e00-\u9fff]',s))<5: continue
            for nn,seg in segs(s):
                key=f"ch{nn:02d}"
                if key not in ch: continue
                t=ch[key]
                # 中文引语词 「…」
                for q in re.findall(r'「([^」]{2,24})」',seg):
                    if q in t: continue
                    if any(c in q for c in "，。！？…—"): continue
                    bad.append((b,i,key,f"「{q}」","中文引语词",seg[:120]))
                # 英文专名
                for t0 in set(re.findall(r'\b[A-Z][A-Za-z]{2,}\b',seg)):
                    if t0 in STOP or t0 in ("Ben","Spidena","Obbie","Daffy","Wolf","Pesch","Paulav",
                                            "Earhav","Cross","Nasha","Celestra","Galev","Filif","Mervin","Hozel",
                                            "Daffodil","Kintel","Tall","Boots","Man","Chop","The","Fey","Way"):
                        continue
                    if t0 not in t:
                        bad.append((b,i,key,t0,"英文专名",seg[:120]))
    return bad

if __name__=="__main__":
    book=sys.argv[1]
    bad=run(book)
    print(f"=== 章号指认：{len(bad)} 条该章查无 ===")
    for x in bad: print(f"  ❌ {x[0][:30]:32s} L{x[1]:<5d} {x[2]} 中 {x[4]} 查无 {x[3]}\n       {x[5][:130]}")
    sys.exit(1 if bad else 0)
