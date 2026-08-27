import sys, zipfile, re, html
epub=sys.argv[1]; kw=sys.argv[2]; span=int(sys.argv[3]) if len(sys.argv)>3 else 200
z=zipfile.ZipFile(epub)
txt=''
for n in z.namelist():
    if n.lower().endswith(('.xhtml','.html','.htm')):
        d=z.read(n).decode('utf-8','ignore')
        d=re.sub(r'<[^>]+>',' ',d)
        d=html.unescape(d)
        txt+=' '+d
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
ft=norm(txt)
# try kw as-is
for cand in [kw, kw.replace("'","’"), kw.replace("'",'”')]:
    i=txt.find(cand)
    if i>=0:
        seg=txt[i-30:i+span].strip()
        print('EXACTHIT @',repr(cand),'->',repr(seg))
        print('FP', 'HIT' if norm(seg)[:60] in ft else 'CHECK')
        sys.exit(0)
print('rawNF for',repr(kw))
# fuzzy: use alphanumeric fingerprint of kw
fk=norm(kw)
if fk:
    pos=[m.start() for m in re.finditer(re.escape(fk),ft)]
    if pos:
        p=pos[0]
        print('FP-HIT',repr(fk),'pos',p)
        # get raw window from txt by scanning
        for off in range(len(txt)):
            if norm(txt[off:off+len(fk)])==fk:
                print('raw:',repr(txt[off-30:off+span].strip()))
                sys.exit(0)
