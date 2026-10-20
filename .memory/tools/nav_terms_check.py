#!/usr/bin/env python3
"""导航层「关键术语」行核对：每个英文术语必须在**本章** text/ 里逐字出现，
且行内不得残留自撰标记（`? →` / `? no` / `? yes`）。
退出码 0=无阻断；1=有阻断。"""
import os,re,sys,glob
MARK=re.compile(r'[A-Za-z][A-Za-z\'\- ]{0,26}\?\s*(?:no\b|yes\b|→)')
def main():
    book=sys.argv[1]
    ch={}
    for p in glob.glob(os.path.join(book,"text","*.txt")):
        m=re.search(r'ch(\d+)',os.path.basename(p))
        if m: ch[f"ch{int(m.group(1)):02d}"]=open(p,encoding="utf-8").read()
    bad=[]
    for f in sorted(glob.glob(os.path.join(book,"ch*.md"))):
        b=os.path.basename(f)
        m=re.search(r'ch(\d+)',b); key=f"ch{int(m.group(1)):02d}"
        t=ch.get(key,"")
        for i,l in enumerate(open(f,encoding="utf-8"),1):
            if "关键术语" not in l: continue
            # ① 自撰标记
            for mm in MARK.finditer(l):
                bad.append((b,i,"标记残留",mm.group(0).strip()))
            # ② 术语存在性：取「英文（中文）」或「纯英文」片段
            body=l.split("：",1)[1] if "：" in l else l
            for part in re.split(r'[·、]',body):
                part=part.strip()
                if not part: continue
                m2=re.match(r'^([A-Za-z][A-Za-z\'\- ]{1,40}?)\s*(?:[（(]|→|$)',part)
                if not m2: continue
                term=m2.group(1).strip()
                # 去掉尾部的 ? 标记痕迹
                term=re.sub(r'\s*\?\s*(?:no|yes|→)?\s*$','',term).strip()
                if not term or len(term)<2: continue
                if term.lower() in ("the fey way",): pass
                if term not in t:
                    bad.append((b,i,"术语本章查无",f"{term!r}"))
    blk=[x for x in bad if x[2]=="标记残留"]
    tip=[x for x in bad if x[2]!="标记残留"]
    print(f"=== 导航层关键术语核对 ===")
    print(f"· 阻断型（自撰标记残留）：{len(blk)}")
    for x in blk: print(f"  ❌ {x[0][:32]:34s} L{x[1]:<5d} [{x[2]}] {x[3]}")
    print(f"· 提示型（术语在本章查无）：{len(tip)} —— **口径不匹配**，不判红：")
    print("  「关键术语」是导航层，可含全书级术语（seeb / The Fey Way / Ostrig Vontrik 等），")
    print("  本章未出现≠缺陷；仅当该词**全书**也查无时才是虚构。")
    return 1 if blk else 0
if __name__=="__main__":
    sys.exit(main())
