#!/usr/bin/env python3
"""check_candidate.py — 校验候选引文 fingerprint 是否命中 epub。
用法:
  python3 check_candidate.py <epub_path> <candidates_file>
candidates_file 每行一句候选英文引文；脚本输出 编号 + OK/X + 长度。
"""
import re, sys, html, zipfile, tempfile, os, glob

def flat_alpha(s): return re.sub(r'[^a-z0-9]','',s.lower())

def epub_flat(epub):
    z=zipfile.ZipFile(epub); out=""
    with tempfile.TemporaryDirectory() as td:
        for n in z.namelist():
            if n.lower().endswith(('.html','.htm','.xhtml')):
                p=os.path.join(td,re.sub(r'[\\/]','_',n))
                open(p,'wb').write(z.read(n))
        for p in sorted(glob.glob(os.path.join(td,'*'))):
            t=open(p,encoding='utf-8',errors='ignore').read()
            t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t).replace('\u00a0',' ')
            out+=t
    return out

def main():
    epub=sys.argv[1]; cands=sys.argv[2]
    full=flat_alpha(epub_flat(epub))
    lines=[l.strip() for l in open(cands,encoding='utf-8') if l.strip()]
    for i,l in enumerate(lines,1):
        qa=flat_alpha(l)
        ok= qa[:52] in full if len(qa)>=52 else (qa in full if len(qa)>=20 else 'SKIP')
        print(f"{i:03d} {'OK' if ok is True else ('X' if ok is False else 'SKIP')}: len={len(qa)} | {l[:90]}")

if __name__=='__main__': main()