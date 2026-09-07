import re, os
BASE="notes/books/a-most-angelic-death"
# replacements: (chapter_file, block_number, new_quoted_string)
REPS=[
 ("ch04 alex ghost arrives.md",4,'“I don’t know anything else…but I am certain of that.”'),
 ("ch04 alex ghost arrives.md",6,'“We love you. But the thought of putting up with him doesn’t fill me with joy.”'),
 ("ch07 five suspects assemble.md",3,"“I’ll explain later,” she said quietly. “He’ll disappear in a moment.”"),
 ("ch11 soul tea clue.md",1,"“I can move things!” she whispered, her face lighting up. “I bashed Sam’s popcorn all over the place.”"),
 ("ch11 soul tea clue.md",5,"“I bet they did that with my bacon roll as well,” Giles declared, his face red with indignation."),
 ("ch11 soul tea clue.md",6,"“BlackWall Security is a registered business, one that I established many years ago.”"),
 ("ch13 alexs watch.md",4,"“Ash could be on to something. I bloody loved that watch. I’m pretty sure that’s what I’m connected to.”"),
 ("ch15 alex first outing.md",3,"“Can we try it now? Please Lily? I really need to.”"),
 ("ch15 alex first outing.md",6,"“Lily, where’s Alex? Shouldn’t he be here as well?”"),
 ("ch17 petrov beats sam.md",1,"“Oi, knobhead. Come here.”"),
 ("ch17 petrov beats sam.md",3,"“A Russian ghost,” he explained. “My mum loves all that kind of stuff,” he continued."),
 ("ch18 annas confession.md",1,"“The results came back surprisingly quickly.”"),
 ("ch18 annas confession.md",6,"“I had already decided I wasn’t going to prison because of him.”"),
]
num2sym={1:'①',2:'②',3:'③',4:'④',5:'⑤',6:'⑥',7:'⑦',8:'⑧',9:'⑨',10:'⑩'}
for fn,n,newq in REPS:
    path=os.path.join(BASE,fn)
    md=open(path).read()
    sym=num2sym[n]
    m=re.search(r'\*\*'+sym+r'\*\*\s+".*?"', md, re.S)
    if not m:
        print('NO MATCH',fn,n); continue
    old=m.group(0)
    repl='**'+sym+'** '+newq
    md=md.replace(old,repl,1)
    open(path,'w').write(md)
    print('OK',fn,'#',n)
