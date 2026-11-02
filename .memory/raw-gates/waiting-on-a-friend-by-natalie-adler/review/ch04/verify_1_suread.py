import json
import sys

TEXT = sys.argv[1]
OUT = sys.argv[2]
t = open(TEXT, encoding='utf-8').read()

CURLY = '\u2018\u2019\u201c\u201d'


def span_of(anchor):
    i = t.find(anchor)
    assert i >= 0, 'MISS: ' + anchor[:60]
    assert t.count(anchor) == 1, 'AMBIGUOUS: ' + anchor[:60]
    assert t[i:i + len(anchor)] == anchor
    assert anchor[0] not in CURLY and anchor[-1] not in CURLY, 'curly edge: ' + anchor[:40]
    return [i, i + len(anchor)]


FACTS = [
    ("Mark 自编 Norse 祖先的故事：那些人劫掠基督徒定居点，并嘲讽对方的神是会死的；他说自己的族人来自阳光更亮、更长也更可怕的地方，其实他来自 Bay Ridge。",
     "He liked to make up stories about his Norse ancestors who raided Christian settlements and taunted them that their god was mortal."),
    ("Mark 靠田径奖学金上大学，在校园里穿着作者见过的最短红短裤、不穿上衣地窜；作者一见就动心（Right off the bat, I was smitten with Mark）。",
     "He went to college on a track scholarship, so you\u2019d see him darting around campus in the shortest red shorts I\u2019d ever seen, and no shirt."),
    ("作者七岁那年：妈妈发现她与邻家小孩 Lisa 全裸，Lisa 被作者的鞋带绑在自家暖气片上，而作者穿着 Lisa 的套头衫；妈妈只叫她解开 Lisa、好好玩。",
     "Once, when I was seven, my mom found me with Lisa, a neighborhood kid, fully nude and tied to our radiator pipe with my shoelaces."),
    ("Mark 与作者一起离开大学：Mark 是被踢出来的（\u201cscholarship not renewed\u201d），作者则是自己选择离开。",
     "We got close because we left college together, only he got kicked out (\u201cscholarship not renewed\u201d) and I chose to leave."),
    ("Mark 与作者一起搬回城里，各带自己的 fag / dyke 圈子，但多半跟街区怪人混；作者最后成了 Mark 朋友的朋友，因为 Mark 总邀她出去（\u201cCome dancing with us\u201d）。",
     "When Mark and I moved back to the city together, we had our respective fag and dyke groups because our friends were the people we were sleeping with, and their friends, whom they had also slept with, but mostly we spent time with the neighborhood weirdos because they liked good music and hanging out and making stuff."),
    ("关于 Hank Henry 的谣言 vs 实情：谣言说 Spring Fling 后 Mark Johansen 勾搭了 Hank，Hank 只好把 \u201cfaggot\u201d 的头骨踢碎；实情是 Mark 在给 Hank 口交，这次 Hank 醉得射不出来、决定回报一次，吞下 Mark 的精液后却起身把他打昏。",
     "What actually happened was, Mark was blowing Hank, as he was often kind enough to do, but this time Hank was too drunk to get off and decided to return the favor for once, and when he swallowed Mark\u2019s load, instead of saying thank you, Hank got off his knees and coldcocked him."),
    ("Mark 生病前后在 Village 被 Hank 叫住：Mark 认不出这个形容枯槁的人，知道是 Hank 后没说出积压多年的话，而是接受了道歉（\u201cI\u2019m sorry for what I did, but hey, I\u2019m paying for it now\u201d）和握手。",
     "Instead, he accepted Hank\u2019s apology\u2014\u201cI\u2019m sorry for what I did, but hey, I\u2019m paying for it now\u201d\u2014and his bony handshake."),
    ("几周后 Mark 在《Times》上看到 Hank 的讣告：一个金融从业者死于 \u201ccancer\u201d，遗下慈爱的双亲、姐姐、姐夫和两个侄子；Mark 只说庆幸 Hank 做了弥补。",
     "And wouldn\u2019t you know it, a few weeks after that, Mark found Hank\u2019s obituary in the Times."),
]

RELATIONS = [
    ("Mark（Mark Johansen）", "作者 / 叙述者", "一起离开大学又一起搬回城里的密友；作者从小对他动心，但坚称自己一直只喜欢女孩。",
     "We got close because we left college together"),
    ("Hank Henry", "Mark", "毕业舞会（Spring Fling）后那件事的施暴者：把 Mark 打昏、踢碎他头骨的传言对象；后来病弱，向 Mark 道歉。",
     "Mark Johansen had come on to Hank Henry after the Spring Fling"),
    ("作者的母亲", "作者 / 叙述者", "爱女儿、也爱海洛因的母亲；作者七岁时发现她与 Lisa 后，只叫她解开 Lisa 并好好玩。",
     "My mother just told me to untie Lisa and to play nice."),
    ("Lisa", "作者 / 叙述者", "邻家小孩（a neighborhood kid）；七岁时与作者一起裸体，被作者的母亲撞见。",
     "my mom found me with Lisa, a neighborhood kid, fully nude and tied to our radiator pipe with my shoelaces"),
    ("Mark 的父母（一个 longshoreman 和一个 homemaker）", "Mark", "冷冰冰的父母，把 Mark 养大；与作者有母亲陪伴的童年形成对照。",
     "He was raised by cold parents, a longshoreman and a homemaker"),
    ("Mark 的三个姐姐", "Mark", "年年赢 Miss Norway 冠军；对照作者在华盛顿广场公园喷泉里玩水的童年。",
     "Mark\u2019s three sisters were winning the Miss Norway crown year after year"),
    ("Hank 的家属（loving parents 与 sister、brother-in-law、two nephews）", "Hank Henry", "讣告中列出的遗属。",
     "survived by his loving parents and sister and brother-in-law and two nephews"),
]

NUMBERS = [
    ("seven", None, "Once, when I was seven"),
    ("three", "Mark 的三个姐姐拿 Miss Norway 冠军", "Mark\u2019s three sisters"),
    ("a couple of times", "两人年轻时睡过几次", "We slept together a couple of times"),
    ("year after year", "作者童年与 Mark 姐姐们的对照", "year after year"),
    ("One day", "在 Village 遇见 Hank 的那天", "One day, in the Village"),
    ("a few weeks after that", "遇见 Hank 与读到讣告之间的间隔", "a few weeks after that"),
    ("two nephews", "Hank 讣告中的遗属", "and two nephews"),
]

facts = []
for fact, anchor in FACTS:
    facts.append({"fact": fact, "anchor": anchor, "span": span_of(anchor)})

relations = []
for a, b, rel, anchor in RELATIONS:
    relations.append({"a": a, "b": b, "relation": rel, "anchor": anchor, "span": span_of(anchor)})

numbers = []
for val, note, anchor in NUMBERS:
    entry = {"value": val, "anchor": anchor, "span": span_of(anchor)}
    if note is not None:
        entry["note"] = note
    numbers.append(entry)

total = len(facts) + len(relations) + len(numbers)
anchors_hit = "%d/%d" % (total, total)

doc = {
    "chapter": "ch04",
    "text_file": TEXT,
    "chars": len(t),
    "facts": facts,
    "relations": relations,
    "numbers": numbers,
    "turning_point": "Mark 生病前后，当年在毕业舞会后把他打昏的 Hank 在 Village 叫住他；Mark 没有报复，接受了道歉与握手——几周后 Hank 的讣告出现在《Times》上，而 Mark 只说他庆幸 Hank 做了弥补。",
    "numbers_note": "本章正文无阿拉伯数字（0-9 零匹配），也无 ’78 类缩写年份；所有数量/时间均为拼写形式，逐字见 numbers 各条 anchor。",
    "anchors_hit": anchors_hit,
    "verify_cmd": "python3 -I /Users/jcxs2014/Documents/Works/EnglishRead/.memory/raw-gates/waiting-on-a-friend-by-natalie-adler/review/ch04/verify_1_suread.py /Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/waiting-on-a-friend-by-natalie-adler/text/ch04_everyone_was_hot_for_mark.txt /Users/jcxs2014/Documents/Works/EnglishRead/.memory/raw-gates/waiting-on-a-friend-by-natalie-adler/review/ch04/1-suread.json",
}

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
    f.write('\n')

print('OK', anchors_hit, 'chars', len(t))