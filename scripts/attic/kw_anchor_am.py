#!/usr/bin/env python3
"""Adam, Mine 关键词锚定自查（AGENTS.md 第8e/9b条，独立审查 d 步标准件）。

region 口径：每个 `> **原句 N:**` 区域 = 引语行到下一引语块/`## 本章词汇` 之前。
锚定规则：
  A) 关键词英文词命中本块引语行 → OK；
  B) 未命中引语但命中本块「为什么这样写」段落 → 语境延伸词，OK；
  C) 两者皆未命中 → 违规。
另查：四子项齐全（**中文理解**： 等格式，冒号在粗体外）、编号连续、重复引语块。

用法: python3 scripts/attic/kw_anchor_am.py "<书目录>"
"""
import re
import sys
from pathlib import Path

STOP = {"the","a","an","of","to","in","for","and","or","is","are","was","were","be","been",
        "it","its","i","you","we","they","he","she","my","your","our","their","his","her",
        "that","this","with","on","at","not","no","as","by","so","do","did","done"}

def norm(s):
    s = s.replace("\u2019","'").replace("\u2018","'").replace("\u201c",'"').replace("\u201d",'"')
    return re.sub(r"\s+"," ",s).strip().lower()

def tok(s):
    return [w for w in re.findall(r"[a-z']+", norm(s)) if w not in STOP and len(w) > 2]

def word_in(word, text_norm):
    if word in text_norm: return True
    for suf in ("ing","ed","es","s","d"):
        if word.endswith(suf) and word[:-len(suf)] and word[:-len(suf)] in text_norm: return True
        if (word+suf) in text_norm: return True
    return False

def main(book_dir):
    problems=[]; total_kw=total_blocks=0; ext_ok=0
    for f in sorted(Path(book_dir).glob("ch*.md"), key=lambda p:int(re.match(r'ch0*(\d+)',p.name).group(1))):
        t=f.read_text(encoding="utf-8")
        starts=[m.start() for m in re.finditer(r'^> \*\*原句 \d+:\*\*', t, re.M)]
        endmark=t.find('## 本章词汇')
        regions=[]
        for i,s in enumerate(starts):
            e=starts[i+1] if i+1<len(starts) else (endmark if endmark>s else len(t))
            regions.append(t[s:e])
        nums=[int(re.match(r'^> \*\*原句 (\d+):',r).group(1)) for r in regions]
        if nums!=list(range(1,len(nums)+1)):
            problems.append(f"{f.name}: 编号不连续 {nums}")
        seen=set()
        for num,r in zip(nums,regions):
            total_blocks+=1
            lines=r.split("\n")
            quote=lines[0][len('> **原句 %d:** ' % num):]
            qnorm=norm(quote)
            for item in ("中文理解","关键词","为什么这样写","读者视角提示"):
                if f"**{item}**：" not in r and f"**{item}：**" not in r:
                    problems.append(f"{f.name} 原句{num}: 缺子项 {item}")
            key=qnorm[:60]
            if key in seen: problems.append(f"{f.name} 原句{num}: 重复引语块")
            seen.add(key)
            m=re.search(r'\*\*关键词\*\*：(.+)', r)
            if not m:
                continue
            total_kw+=1
            # 为什么这样写 段落
            wm=re.search(r'\*\*为什么这样写\*\*：(.+?)(?=\n\n\*\*读者视角提示|\n\n## |\Z)', r, re.S)
            wnorm=norm(wm.group(1)) if wm else ""
            for phrase in re.split(r' / |，|,', m.group(1)):
                phrase=phrase.strip()
                if not phrase or not re.search(r'[a-zA-Z]', phrase): continue
                words=tok(phrase)
                if not words: continue
                missing=[w for w in words if not word_in(w,qnorm)]
                if not missing: continue
                if wnorm and all(word_in(w,wnorm) for w in missing):
                    ext_ok+=1; continue
                problems.append(f"{f.name} 原句{num}: 关键词未锚定 -> '{phrase}' (缺 {missing})")
    print(f"扫描 {len(list(Path(book_dir).glob('ch*.md')))} 文件 / {total_blocks} 引语块 / {total_kw} 关键词行 / 语境延伸词放行 {ext_ok}")
    if problems:
        print(f"发现 {len(problems)} 处问题：")
        for p in problems: print("  -", p)
        sys.exit(1)
    print("锚定自查全绿：关键词全部命中本块引语（或'为什么这样写'语境延伸），无缺子项/编号断裂/重复块")

if __name__=="__main__":
    main(sys.argv[1])
