import re,os,unicodedata
base='.'
def flat(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2014','-'),('\u2013','-')]:
        s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip().lower()
texts={n:flat(open(f"text/ch{n:02d}_chapter_{n}.txt",encoding='utf-8').read()) for n in range(1,13)}
targets=[
 (8,"ch08 his father had no friends.md",[
  "Colleagues in the army, drinking pals in the sergeants' and officers' mess—force of circumstance.",
  "What she said next revealed a side of her he had never known.",
  "A message from a harsher time. The form of words was unfamiliar too.",
  "Oh, that Susan.",
  "struggled to make the adjustment and her confabulation",
  "He had in mind his father's armchair by the window monotonously declaring his absence.",
  "It is what it is.",
  "Whereas Alissa—he saw the beauty of it.",
  "Except to leave school. No, that too was a reaction.",
  "That way the teeth of the cogs wear out evenly.",
  "medical","mahogany","open mouths","Jack Tate","confabulation",
 ]),
 (7,"ch07 the captain of the second fifteen.md",[
  "Remember, I'm always fond of you","I am almost sixteen","Roland is an intimate boy",
  "Ich weiss nicht, was soll es bedeuten","Fichtenknabe","Romanian","forty-five",
 ]),
]
for n,f,frs in targets:
    md=flat(open(f,encoding='utf-8').read())
    for fr in frs:
        infile = flat(fr) in md
        others=[k for k,v in texts.items() if flat(fr) in v]
        print(f"[md={'Y' if infile else 'N'}] ch{n:02d} {others} :: {fr[:70]}")
