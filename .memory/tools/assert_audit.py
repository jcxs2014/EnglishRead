#!/usr/bin/env python3
"""散文断言的两类机械裁决：
  P) 标点/符号计数类：断言「N 个省略号/破折号/问号…」→ 回本章原文取所在句，数该符号。
  A) 绝对化断言类：断言「全书唯一/第一次/从未/总是/每次」+ 就近英文词 → 全书计数。
退出码 0=无阻断；1=有阻断。"""
import os,re,sys,glob,unicodedata

SYM={
 "省略号":("…","..."),
 "破折号":("—","——"),
 "引号":("“","”","\"","'"),
 "感叹号":("!",),
 "问号":("?",),
 "逗号":(",",),
 "句号":(".",),
 "破折":("—","——"),
}
NORM={"零":0,"一":1,"两":2,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
def cn(s):
    s=s.strip()
    if s.isdigit(): return int(s)
    return NORM.get(s)

def load(book):
    ch={}
    for p in glob.glob(os.path.join(book,"text","*.txt")):
        m=re.search(r'ch(\d+)',os.path.basename(p))
        if m: ch[f"ch{int(m.group(1)):02d}"]=open(p,encoding="utf-8").read()
    return ch,"\n".join(ch.values())

def eng_spans(s):
    out=[]
    for m in re.finditer(r'[^\u4e00-\u9fff\u3000-\u303f]+',s):
        t=re.sub(r'\s+',' ',m.group(0)).strip().strip('"“”\'‘’()（）')
        if re.search(r'[A-Za-z]',t): out.append((m.start(),m.end(),t))
    return out

def nearest(span_list,pos):
    best=None
    for st,en,t in span_list:
        d=min(abs(st-pos),abs(pos-en))
        if best is None or d<best[0]: best=(d,t)
    return best[1] if best else None

def run(book):
    ch,full=load(book)
    blocks=[]
    for f in sorted(glob.glob(os.path.join(book,"*.md"))):
        b=os.path.basename(f)
        m=re.match(r'ch(\d+)',b); key=f"ch{int(m.group(1)):02d}" if m else None
        for i,l in enumerate(open(f,encoding="utf-8"),1):
            s=l.strip()
            if not s or s.startswith(("|","#","> ")): continue
            if len(re.findall(r'[\u4e00-\u9fff]',s))<5: continue
            spans=eng_spans(s)
            # ---- P) 符号计数
            for cm in re.finditer(r'([零一两二三四五六七八九十]|\d+)\s*个?\s*(省略号|破折号|引号|感叹号|问号|逗号|句号)',s):
                n=cn(cm.group(1)); sym=cm.group(2)
                if n is None: continue
                phrase=nearest(spans,cm.start())
                if not phrase: continue
                corpus=ch.get(key) or full
                if phrase not in corpus: continue
                # 取包含该短语的句子
                seg=None
                for part in re.split(r'(?<=[.!?])\s+',corpus):
                    if phrase in part: seg=part; break
                if seg is None: continue
                cnt=0
                seen=set()
                for t in SYM[sym]:
                    if t in seen: continue
                    seen.add(t)
                    cnt+=seg.count(t)
                blocks.append(("P",b,i,sym,n,cnt,phrase[:50],s[:170]))
            # ---- A) 绝对化断言
            for cm in re.finditer(r'(全书唯一|唯一一次|唯一一处|全书第一次|全书唯一一次|第一次|首次|从未|再没|再也没有|总是|每次|每逢|最后一次)',s):
                kind=cm.group(1)
                phrase=nearest(spans,cm.end())
                if not phrase or len(phrase.split())>6: continue
                key2=phrase.split()[0] if phrase.split() else phrase
                if len(key2)<4: continue
                cnt=len(re.findall(re.escape(key2),full,re.I))
                blocks.append(("A",b,i,kind,None,cnt,key2,s[:170]))
    return blocks

if __name__=="__main__":
    book=sys.argv[1]
    bl=run(book)
    P=[x for x in bl if x[0]=="P"]; A=[x for x in bl if x[0]=="A"]
    badP=[x for x in P if x[4]!=x[5]]
    print(f"=== 标点/符号计数断言：{len(P)} 条，计数不符 {len(badP)} 条 ===")
    for x in badP:
        print(f"  ❌ {x[1]} L{x[2]} 声称 {x[4]} 个{x[3]} / 实为 {x[5]} | 短语 \"{x[6]}\"")
        print(f"       {x[7][:160]}")
    print(f"\n=== 绝对化断言：{len(A)} 条 ===")
    for x in A:
        flag=""
        k=x[3]; c=x[5]
        if k in("全书唯一","唯一一次","唯一一处","全书唯一一次") and c!=1: flag="  ← 唯一性可计数证伪"
        if k in("第一次","全书第一次","首次","最后一次") and c!=1: flag="  ← 首次/末次可计数证伪"
        if k in("从未","再没","再也没有") and c>0: flag="  ← 「从未」被证伪"
        if k in("总是","每次","每逢") and c<2: flag="  ← 全称量词可证伪"
        print(f"  {'❌' if flag else '·'} {x[1][:30]:32s} L{x[2]:<5d} [{k}] 词\"{x[6]}\" 全书出现 {c} 次{flag}")
        print(f"       {x[7][:150]}")
    sys.exit(1 if badP else 0)
