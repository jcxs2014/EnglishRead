#!/usr/bin/env python3
"""批6 事实断言自检修正（幂等）。每条断言均已 grep 实证。"""

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"

FIXES = [
    # ---- ch17 ----
    ("ch17 part 2 the unkindness descends.md",
     "全书最锋利的一次**延迟反应**，也是全书第一次让叙述者**在恐怖升级的同时笑出声**。",
     "全书最锋利的一次**延迟反应**。注意这**不是**全书第一次笑出声——ch16 结尾叙述者已经写过\"I laugh in spite of myself, in spite of the obvious danger\"，本章的笑是**同一场笑的延续**，而它**跨越了章节边界**。"),
    ("ch17 part 2 the unkindness descends.md",
     "全书到这一句为止，叙述者**从未羡慕过一个活着的人**，因为羡慕活着的人等于**承认自己正在死去**",
     "全书第二次出现 jealousy 这个词（上一次是 ch04，叙述者嫉妒 Danny 与他前任的亲密），而这一次是全书第一次让**羡慕的对象变成无知本身**——不是羡慕某人的幸福，是羡慕某人的**不知情**，而\"不知情\"在这里等于**承认自己正在死去**"),
    ("ch17 part 2 the unkindness descends.md",
     "也是全书第一次让**沉默成为恐怖**。",
     "也是全书第一次让**沉默**成为恐怖的载体（ch15 的\"silent\"只是形容 Jace 的性格——\"Strong, silent type\"）。"),
    ("ch17 part 2 the unkindness descends.md",
     "注意每一句都比上一句**更短**：第一句 9 个词，第二句 7 个词，第三句 3 个词，第四句 4 个词，第五句 5 个词——作者在**句长上做了递减**，而句长的递减正是**声音的递减**在**语法上的等价物**。",
     "注意句长的轨迹：第一句 10 个词 → 第二句 7 个词 → 第三句 3 个词 → 第四句 4 个词 → 第五句 5 个词——呈 **V 形**（10 → 7 → 3 → 4 → 5）：先骤降到 3 个词，再微升到 5 个词，而**触底点是\"The music cuts.\"**——声音的塌缩在**最短的那一句**上触底，而句长正是**声音递减**在语法上的等价物。"),
    ("ch17 part 2 the unkindness descends.md",
     "而全书最恐怖的一句台词是**\"Your time is up\"**，而它总是**紧跟在滴答声之后**。",
     "而全书最锋利的一句台词是**\"Your time is up\"**——它全书只出现过**两次**（ch18 对 Danny、ch19 对叙述者），而两次都出现在怀表滴答声之后。"),
    # ---- ch18 ----
    ("ch18 part 2 mouth full of raven beaks.md",
     "——而\"先想到进来\"意味着**他的判断比她的更安全**，而这**是全书第一次 Ravi 的判断压过她的**。",
     "——而\"先想到进来\"意味着他比她**更早做出了判断**；全书到这里为止，Ravi 几乎从不主动做判断（他一直在回避她），而这一次他**先动了手**。"),
    ("ch18 part 2 mouth full of raven beaks.md",
     "而\"her name\"（她的名字）里的\"her\"值得单独看：这个代词**指代 Tanya**，而叙述者**从未用过\"her\"指代 Tanya**（她一直用\"Tanya\"或\"I\"），而\"her\"是一个**第三人称所有格**，等于让 Tanya **在这句话里被降格为一个代词**——而\"代词化\"正是 ch19 里 Tanya 被拆掉之前的**语法状态**。",
     "而\"her name\"（她的名字）里的\"her\"值得单独看：作者用**第三人称所有格代词**而不是名字本身，等于让 Tanya **在这句话里从一个人变成一个代词**——而\"代词化\"正是 ch19 里 Tanya 被拆掉之前的**语法状态**（ch19 里叙述者说\"her beautiful face is warping with rot\"，Tanya 已经只剩下一个\"her\"）。"),
    ("ch18 part 2 mouth full of raven beaks.md",
     "全书最长的一个**单句内心独白**，也是全书最锋利的一次**关系解剖**。",
     "全书第三长的一个**段落**（170 词，仅次于 ch15 的 202 词段与 ch01 的 175 词段），也是全书最锋利的一次**关系解剖**。"),
    ("ch18 part 2 mouth full of raven beaks.md",
     "而\"容器\"这个功能正是全书里**帽子**的功能（ch16 里那顶帽子是**空的**，现在它是**满的**）。",
     "而\"容器\"这个功能正是全书里**高礼帽**的功能——那顶帽子从 ch15（浮在空中、帽檐两侧折起、插着一根羽毛）到 ch16（帽檐压下来遮住他的脸）始终是**一个装着东西的容器**，而\"装着东西\"正是它成为恐怖来源的原因。"),
    # ---- ch19 ----
    ("ch19 part 2 my time is up.md",
     "是全章最锋利的一次**自白**，而五句**五句话的长度**在**递减**（5→6→2→3→5 词），作者用**句长**模拟**罪状清单**的**节奏**；",
     "是全章最锋利的一次**自白**，而五句话的长度呈**尖峰形**（2→6→2→3→4 词）——第二句最长，等于让**\"弃船\"**这个动作成为**罪状清单的峰值**；"),
    ("ch19 part 2 my time is up.md",
     "⑤**罪状清单的递减**（",
     "⑤**罪状清单的尖峰**（"),
    ("ch19 part 2 my time is up.md",
     "全段共五句，而**五句的长度**在**递减**：",
     "全段共五句，而**五句的长度**呈**尖峰形**："),
    ("ch19 part 2 my time is up.md",
     "——注意作者用**最短的句子**放在**开头和结尾**（两个词 / 四个词），而**最长的句子**放在**中间**（六个词），等于让**清单**形成一个**凹形**——而**凹形**正是全书的**节奏结构**（**中间最长、两头最短**）。",
     "——注意作者的排列是**最短 → 最长 → 最短 → 中 → 中**（2 → 6 → 2 → 3 → 4）：峰值在**第二句**，等于让**\"弃船\"**这个动作成为**罪状清单的峰值**，而结尾的\"I want too much\"（4 个词）比开头稍长，意味着**这份清单没有收敛，它还在增长**。"),
    # ch19 导航里 ch18 的 "out there" 归属（原文出自 ch17）
    ("ch19 part 2 my time is up.md",
     "ch18 的\"out there\"",
     "ch17 的\"out there\""),
]

for fn, old, new in FIXES:
    path = f"{BOOK}/{fn}"
    with open(path, encoding="utf-8") as f:
        s = f.read()
    if s.count(old) == 1:
        s = s.replace(old, new)
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        print(f"FIX OK  {fn[:12]} :: {old[:36]}")
    elif new in s:
        print(f"已应用（幂等跳过） {fn[:12]} :: {new[:36]}")
    else:
        raise SystemExit(f"FIX 目标未命中 {fn} :: {old[:60]}")

print("\n=== 残留断言复核 ===")
for fn in ("ch17 part 2 the unkindness descends.md",
           "ch18 part 2 mouth full of raven beaks.md",
           "ch19 part 2 my time is up.md"):
    s = open(f"{BOOK}/{fn}", encoding="utf-8").read()
    for bad in ("从未羡慕过一个活着的人", "全书第一次让叙述者**在恐怖升级的同时笑出声**",
                "全书最长的一个**单句内心独白**", "帽子是**空的**", "在**递减**", "凹形"):
        if bad in s:
            print(f"  残留 {fn[:12]} :: {bad}")
print("残留检查完成")
