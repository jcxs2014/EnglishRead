#!/usr/bin/env python3
"""裁决「英文短语 + N 个词」型散文断言。
判据：与断言就近配对的英文短语的词数，必须等于断言声称的 N；
      且该英文短语必须逐字出现在本章 text/（或该 md 的引语行）里。
退出码 0=无阻断；1=有阻断。"""
import os,re,sys,glob,unicodedata

CN2INT={"零":0,"一":1,"两":2,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10,
        "十一":11,"十二":12,"十三":13,"十四":14,"十五":15}
def cn2int(s):
    s=s.strip()
    if s.isdigit(): return int(s)
    return CN2INT.get(s)

CLAIM=re.compile(r'([零一两二三四五六七八九十]{1,3}|\d+)\s*(?:个)?\s*词')
# 英文片段：不含中文的最长串（允许内部空格与标点）
# 口径订正（2026-10-25）：原正则只排除了 CJK 标点区 U+3000–303F，
#   **漏掉全角 ASCII 变体**（U+FF00–FFEF，如全角逗号「，」）⇒ 候选短语被粘上中文标点，
#   词数与「在原文」双错（如 ch13 的「，sad little cardboard box」）。
def eng_spans(s):
    spans=[]
    for m in re.finditer(r'[^\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+', s):
        t=m.group(0)
        if re.search(r'[A-Za-z]',t):
            t=t.strip().strip('"“”\'‘’()（）')
            t=re.sub(r'\s+',' ',t).strip()
            if t: spans.append((m.start(),m.end(),t))
    return spans

# 断言前最近的一对引号内的英文内容 —— 「N 词」的**被计数对象**
# 口径订正（2026-10-25）：原实现用「就近英文串」配对 ⇒ 把「粗口只有两个词」错挂到
#   紧邻的 Because 句上（ch10 L54）、「末尾那句只剩四个词」错挂到 "bond" 上（ch20 L64）。
#   ⇒ 改为：**断言前最近的一对引号里的英文**才是被计数对象；没有引号对象 ⇒ 指代不明，判「需人判」。
QUOTED_BEFORE=re.compile(r'["“]([^"”]{1,120})["”][^"“”]{0,40}$')

def wc(t):
    t=unicodedata.normalize("NFKC",t)
    # 去掉引号内外的多余引号
    t=t.strip('"“”')
    return [w for w in re.split(r'\s+',t) if w]

def analyze(book):
    ch_text={}
    for p in glob.glob(os.path.join(book,"text","*.txt")):
        m=re.search(r'ch(\d+)',os.path.basename(p))
        if m: ch_text[f"ch{int(m.group(1)):02d}"]=open(p,encoding="utf-8").read()
    full="\n".join(ch_text.values())
    out=[]
    for f in sorted(glob.glob(os.path.join(book,"*.md"))):
        b=os.path.basename(f)
        mm=re.match(r'ch(\d+)',b); chk=f"ch{int(mm.group(1)):02d}" if mm else None
        content=open(f,encoding="utf-8").read()
        lines=content.split("\n")
        for i,l in enumerate(lines,1):
            s=l.strip()
            if not s or s.startswith(("|","#","> ")): continue
            if len(re.findall(r'[\u4e00-\u9fff]',s))<5: continue
            spans=eng_spans(s)
            if not spans: continue
            for cm in CLAIM.finditer(s):
                n=cn2int(cm.group(1))
                if n is None: continue
                corpus=ch_text.get(chk) or full
                if not corpus: corpus=full
                # ① 被计数对象 = 断言前最近一对引号内的英文内容
                head=s[:cm.start()]
                qm=QUOTED_BEFORE.search(head)
                obj=None
                if qm:
                    cand=qm.group(1).strip().strip('"“”\'‘’')
                    if re.search(r'[A-Za-z]',cand) and len(cand.split())<=12:
                        obj=cand
                if obj is not None:
                    out.append(dict(file=b,line=i,claim=n,actual=len(wc(obj)),
                                    phrase=obj, in_source=(obj in corpus),
                                    ambiguous=False, text=s[:230]))
                    continue
                # ② 无引号对象 ⇒ 指代不明；用行内英文候选做参考，只作「需人判」
                cands=[]
                for st,en,tx in spans:
                    if len(tx.split())>12: continue
                    d=min(abs(st-cm.end()),abs(cm.start()-en))
                    cands.append((d,tx))
                if not cands: continue
                cands.sort()
                hit=[c for c in cands if len(wc(c[1]))==n]
                if hit:
                    d,phrase=hit[0]
                    out.append(dict(file=b,line=i,claim=n,actual=len(wc(phrase)),
                                    phrase=phrase, in_source=(phrase in corpus),
                                    ambiguous=False, text=s[:230]))
                else:
                    d,phrase=cands[0]
                    out.append(dict(file=b,line=i,claim=n,actual=len(wc(phrase)),
                                    phrase=phrase, in_source=(phrase in corpus),
                                    ambiguous=True,
                                    text=s[:230]+"  ｜行内候选: "+" / ".join(f'"{c[1]}"({len(wc(c[1]))}词)' for c in cands[:4])))
    return out

if __name__=="__main__":
    book=sys.argv[1]
    bl=analyze(book)
    bad=[x for x in bl if x["actual"]!=x["claim"] and not x.get("ambiguous")]
    amb=[x for x in bl if x.get("ambiguous")]
    unver=[x for x in bl if not x["in_source"]]
    print(f"=== 「英文短语 + N 词」断言裁决：共 {len(bl)} 条 ===")
    print(f"· 计数与短语实际词数不符（阻断型）：{len(bad)}")
    for x in bad:
        print(f"  ❌ {x['file']} L{x['line']} 声称 {x['claim']} 词 / 实为 {x['actual']} 词 | \"{x['phrase']}\" | 在原文: {x['in_source']}")
        print(f"       {x['text'][:170]}")
    print(f"· 指代歧义（行内多候选，全不匹配）——需人判，不判阻断：{len(amb)}")
    for x in amb:
        print(f"  ❓ {x['file']} L{x['line']} 声称 {x['claim']} 词 ｜ 最近候选 \"{x['phrase']}\"（{x['actual']} 词）")
        print(f"       {x['text'][:210]}")
    print(f"· 短语在本章/全书原文查无（阻断型·需核实）：{len(unver)}")
    for x in unver:
        print(f"  ❓ {x['file']} L{x['line']} \"{x['phrase']}\" | {x['text'][:160]}")
    sys.exit(1 if (bad or unver) else 0)
