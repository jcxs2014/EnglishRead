# -*- coding: utf-8 -*-
"""ch31 精读生成器：引语一律从 text/ch31_chapter_thirty.txt 切片，不手打。"""
import os, re

ROOT = "/Users/jcxs2014/Documents/Works/EnglishRead"
BOOK = os.path.join(ROOT, "notes/books/novels/love-you-to-death-by-jenna-levine")
TXT = os.path.join(BOOK, "text/ch31_chapter_thirty.txt")
OUT = os.path.join(BOOK, "ch31 the room.md")

raw = open(TXT, encoding="utf-8").read()
paras = [p for p in raw.split("\n") if p.strip()]


def seg(idx, start=None, end=None):
    """取 paras[idx] 的一段：从 start 起、到 end 止（含 end）。"""
    p = paras[idx]
    i = 0 if start is None else p.index(start)
    j = len(p) if end is None else p.index(end, i) + len(end)
    s = p[i:j]
    assert "\n" not in s and s in raw, repr(s[:60])
    return s


def wc(s):
    return len(s.split())


# ---------------- 引语块 ----------------
B1 = [seg(3), seg(4), seg(5)]
B2 = [seg(6), seg(7)]
B3 = [seg(13, None, "trying not to cry."), seg(13, "“I was an idiot", None), seg(14, "“You were brilliant. And so brave.", None)]
B4 = [seg(22), seg(26), seg(27)]

BLOCKS = [B1, B2, B3, B4]

for bi, b in enumerate(BLOCKS, 1):
    joined = " … ".join(b)
    n = wc(joined)
    assert 30 <= n <= 70, (bi, n)
    # 段间顺序递增：每段在原文中的起点必须递增
    pos = [raw.index(s) for s in b]
    assert pos == sorted(pos), (bi, pos)
    # 每段必须是原文连续的一段
    for s in b:
        assert s in raw
    print(f"块{bi}: 段数={len(b)} 词数={n}")

# ---------------- 词表 ----------------
VOCAB = [
    ("⭐⭐⭐ 高级", [
        ("brimming", "（情绪）满溢；藏不住", seg(3)),
        ("quip", "说俏皮话；打趣", seg(7, "“I’m trying", "trying to lighten the mood.")),
        ("mirthless", "毫无欢乐的；冷清的", seg(10, None, "mirthless space.")),
        ("utilitarian", "实用主义的；只讲功用的", seg(11, None, "utilitarian.")),
        ("luscious", "柔软华美的；诱人的", seg(11, "A far cry from", "every night.")),
        ("unshed", "未落下的；含在眼里的", seg(14, "Her eyes are glassy", "scalding.")),
    ]),
    ("⭐⭐ 进阶", [
        ("dismayed", "失望的；惊愕的", seg(3, "“This is your home?”", "but can’t.")),
        ("dreadful", "糟透了的；难过的", seg(6)),
        ("sniffling", "抽鼻子；忍着不哭", seg(13, "“That went terribly", "trying not to cry.")),
        ("perches", "（轻快地）坐定；栖身", seg(11, "Lucy crosses the room", "edge of my bed.")),
        ("revel", "尽情享受", seg(25, "I revel in", "of my own.")),
        ("draped", "垂落；搭着", seg(25, "We lie on our sides", "across her waist.")),
    ]),
    ("⭐ 常用", [
        ("room", "房间", seg(2)),
        ("home", "家", seg(3, "“This is your home?”", "“This is your home?”")),
        ("bed", "床", seg(11, "Lucy crosses the room", "edge of my bed.")),
        ("table", "桌子", seg(5, "“Only a bed", "where I stay.”")),
        ("chair", "椅子", seg(5, "“Only a bed", "where I stay.”")),
        ("sleep", "睡觉", seg(23)),
    ]),
]

for tier, rows in VOCAB:
    for head, gloss, ex in rows:
        assert head.lower() in ex.lower(), (head, ex)
        assert ex in raw, (head, ex)
    print(f"{tier}: {len(rows)} 条")

# ---------------- 正文 ----------------
Q = [" … ".join(b) for b in BLOCKS]

MD = """---
状态: 未读
modified: "2026-10-24"
---

# 31. Chapter Thirty

## 本章导航

- **一句话概括**：她走进他住的地方，看着一张床、一张桌子和一把椅子，问「这是你的家？」；他嘴上说这里只是他落脚的地方，她却嫌它糟糕又空荡。两人挤在他那张单薄的床垫上过了一夜，他闭着眼假装这几个偷来的片刻可以永远不结束。
- **情感弧线位置**：从「她站在屋里藏不住的失望」走到「两人独处时的短暂安宁」。中间他用一句玩笑挡住被刺到的痛，又把她自责的话一句句顶回去；落点是那个「假装」——明知时间有限，仍要先把这一刻演成没有尽头。
- **Tropes 兑现/反转**：言情里常见的「带恋人回自己的住处」在这里反转成一次失败的家访：他准备不足（书架几个月没擦，碗堆在水槽里该昨天洗），她一句「糟透了」就把这间屋子的全部问题摊在两人面前。浪漫的「给她一个家」没有出现，出现的是他亲口否认——「这不是我的家」。
- **人物弧线**：Daniel 在这一章露出老习惯——先把感觉按下去（「我正拼命不让自己受伤」），再用动作代替解释；Lucy 相反，她的失望当场就说了出口，而她的眼泪被他一句「你做了能做的一切」接住。
- **叙事手法**：第一人称当下时。房间用**物件**而不是形容词来写：一张床、一张桌子、一把椅子、薄而窄的床垫；叙述者对自己的窘迫有一份自嘲的清点。结尾用三段递进收束——先是决心让这个时刻延长，再是安排她醒来后回家，最后才是那个「假装」。

## 精读

> **原句 1:** "{Q0}"

**中文理解**：「这是你的家？」她的失望藏不住——她不想让我看见，可我一眼就知道；就算没有我们之间的联结也一样，她满身都是这种情绪。我想告诉她的是：你才是我的家。……「这不是我的家，」我却说。「只有一张床、一张桌子、一把椅子，不过是我落脚的地方。」

**关键词**：She’s brimming with it / wants to hide it from me / even without our bond / It’s just where I stay（藏不住的失望、不想让我看见、就算没有联结也清楚、只是落脚的地方）

**为什么这样写**：这一块让「家」这个字在两个人之间来回弹了一次：她用疑问句把球递过来，他心里那句真话刚冒头，就被他自己咽回去，出口的却是一句「这不是我的家」。接着「Only a bed, a table, a chair」用三个并列的名词把一个家压缩成一张清单——清单上的东西越少，房间就越空；而他给这个空间的身份是「just where I stay」，落脚处，不是家。

**读者视角提示**：她问的是「这是你的家？」，他答的是「这不是我的家」——两个人谈的是同一个字，答案却相反；她想听的是承认，他递过来的是一张清单。

> **原句 2:** "{Q1}"

**中文理解**：「这地方糟透了。」她打了个寒颤。「真不敢相信你住在这么难过又空荡的地方。」……「我正拼命不让自己受伤，」我打趣道，想把气氛转轻一点。可这没用。我们都知道我们失去了什么。

**关键词**：can’t believe you live somewhere / so sad and empty / trying to lighten the mood / We both know what we’ve lost（不敢相信他住在这种地方、难过又空荡、想把气氛转轻、我们都知道失去了什么）

**为什么这样写**：她一句「糟透了」正好落在他最没准备好的地方，于是他把受伤改写成一句玩笑，还给自己挂上「trying to lighten the mood」这个动作说明，像在宣布「气氛维护中」。但下一句自我评估就拆了台：「It’s pointless, though.」玩笑没救得回来，因为紧接着的「We both know what we’ve lost」把这份心照不宣交给两个人共同承担——作者没有解释各自失去了什么，只用一个「we」把账并在一起。

**读者视角提示**：她的评价落在房子上，他的痛点落在「我居然住在让你难受的地方」；「trying to lighten the mood」失败之后，两人谁也没再往这个话题上走。

> **原句 3:** "{Q2}"

**中文理解**：「刚才糟透了，是吧。」她抽着鼻子，说明她在忍着不哭。……「我真是个傻瓜，居然以为这事能成。」……「你很出色，也非常勇敢。你做了你能做的一切。」

**关键词**：That went terribly / trying not to cry / I was an idiot / You did all you could（刚才糟透了、忍着不哭、我是傻瓜、你做了能做的一切）

**为什么这样写**：她的两句台词是层层加码的自我指控：先把场面判为「糟透了」，再把责任整个揽到自己身上——「我是个傻瓜，居然以为这事能成」；中间的 sniffling 把话堵在半路，她不肯在他面前哭出声。他的回答只有三个短句，把「我搞砸了」整个换掉：不是「你尽力了」，而是「你很出色、很勇敢、你做了能做的一切」——夸赞落在动词（did）上，因此比落在形容词上更硬。

**读者视角提示**：两个人其实在说同一件事：她认为这场尝试从一开始就错了，他认为她已经做到了能做的一切。他没有解释，也没有一句安慰的套话，只是连着说了三个短句，把她的道歉顶了回去。

> **原句 4:** "{Q3}"

**中文理解**：如果这一刻是我们最后的时刻之一，那我决心让它延续下去。……等她醒来，我会送她回家，让她在最后几天里和姐姐待在一起。……不过现在，我闭上眼睛，假装我们可以永远留在这几个偷来的片刻里。

**关键词**：determined to make it last / take her home / spend her final days / pretend we can stay forever（决心让它延续、送她回家、度过最后几天、假装可以永远停留）

**为什么这样写**：结尾用三段递进把「时间有限」压成一次演出：先是一个宣告（决心让这个时刻延长），接着是一份具体安排（醒来就送她回去，让她和姐姐度过最后几天），最后才是那个「假装」。一句动人的话被安排句垫在下面，温柔因此始终压着期限——他能做的只有把时间尽量用满。

**读者视角提示**：最后那句先用一个「For now, though」把时间挪开：不是「他们会永远在一起」，而是「现在先这样」——他知道这份延长是有尽头的，只是这一刻先不算。

## 本章词汇

### ⭐⭐⭐ 高级
| 词/短语 | 释义 | 例句 |
|---|---|---|
| brimming | （情绪）满溢；藏不住 | {E0} |
| quip | 说俏皮话；打趣 | {E1} |
| mirthless | 毫无欢乐的；冷清的 | {E2} |
| utilitarian | 实用主义的；只讲功用的 | {E3} |
| luscious | 柔软华美的；诱人的 | {E4} |
| unshed | 未落下的；含在眼里的 | {E5} |

### ⭐⭐ 进阶
| 词/短语 | 释义 | 例句 |
|---|---|---|
| dismayed | 失望的；惊愕的 | {E6} |
| dreadful | 糟透了的；难过的 | {E7} |
| sniffling | 抽鼻子；忍着不哭 | {E8} |
| perches | （轻快地）坐定；栖身 | {E9} |
| revel | 尽情享受 | {E10} |
| draped | 垂落；搭着 | {E11} |

### ⭐ 常用
| 词/短语 | 释义 | 例句 |
|---|---|---|
| room | 房间 | {E12} |
| home | 家 | {E13} |
| bed | 床 | {E14} |
| table | 桌子 | {E15} |
| chair | 椅子 | {E16} |
| sleep | 睡觉 | {E17} |

## 一句话总结

她走进他住的地方，他嘴上说这里只有一张床、一张桌子和一把椅子，却把她的失望一句句接下来；两人挤在他那张单薄的床垫上过了一夜，他闭着眼假装这几个偷来的片刻可以永远不结束。
"""

subs = {f"Q{i}": Q[i] for i in range(4)}
_k = 0
for _tier, _rows in VOCAB:
    for _head, _gloss, _ex in _rows:
        subs[f"E{_k}"] = _ex
        _k += 1
assert _k == 18, _k
MD = MD.format(**subs)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(MD)
print("written:", OUT, len(MD), "chars")
