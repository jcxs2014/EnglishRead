# ch04 判定表（R5）

章：`ch04 in spring a young mans fancy lightly turns to thoughts of climate change.md`（155 行，10 块）
原文：`text/ch04_in_spring_a_young_man_s_fancy_lightly_tu.txt`（419 行 / 3132 词）
机器：`2-machine.json` rc=0；块数 10；引语 10 段全 ok；`segment_miss` 0；空引号 0；子项缺 0；`keyword_bad` 0；`cjk_low` 0；`block_hint` 仅提示块数（并列本书最高）。
素读：`1-suread.json` 13 条，`quote in line` 校验 13/13（首版两条行号写错，已改 18 / 128 并复验）。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| Lucinda 与 Isadora 的身份应进块或导航 | `:361`「**Lucinda is my mom’s friend Celia Attley’s daughter. Foster daughter.**」；`:370`「**She’s our darling**」；`:378`「**Isadora is the anti-darling. We’re all terrified of her.**」；`:386`「**She’s Beck’s daughter**…She had a serious fixation on Caralora.」；`:397`「They spend every Saturday afternoon together, at our place.」；md `grep -nE "Isadora\|Lucinda"` 仅命中 md:151 词汇表的 `anti-darling` 例句，叙事层 0 | 本章唯一的新人物登记处整段缺失，无取舍说明 | **阻断**（漏） |
| Zach 的新车 | `:413`「It’s a very ordinary, not-attention-attracting **2012 silver Jetta**, and every time I see it I think of my lost Nash and feel bereft.」；md `grep -nE "Jetta\|银色"` = 0 | 承接上一章烧车，属实质细节 | 提示（漏） |
| Clare 的第一次正面出场应有外貌 | `:34`「a heart-shaped, Pre-Raphaelite face, **waist-length red hair, coppery and streaked with white**, and her enormous eyes are **pale gray, like Alba’s**…mint-green knit dress…Her skin is surprisingly rough」；md `grep -nE "红发\|灰眼\|Pre-Raphaelite"` = 0 | 整段未落 | 提示（漏） |
| 抬头年龄 23 / 22 / 51 | `:18`「Saturday, April 15, 2023 (**Alba is 23, Zach is 22, Clare is 51**)」；md:11 只有日期。Alba 的 23 是替班伏笔（2023 年正主应 21） | 伏笔已靠对白讲清，年龄行未抄 | 提示（漏） |
| md:11「Clare 先关掉手机才起身」是否把「收起」写成「关机」 | `:34`「a middle-aged woman hurriedly **shuts off** her phone and rises to greet us」 | 原文确为关机，md 还专门点出「不是收起」 | **假红** |
| md:11「二十岁才在 Newberry 图书馆正式「第一次」见他」 | `:108`「By then I was twenty, and he was twenty-eight. That was when Henry met me for the first time. He was a librarian at the Newberry Library」 | 年龄、地点、方向全对 | **假红** |
| md:13「六岁的她在草地上见一个成年男人，二十岁的她在图书馆才见到那个「第一次」见她的人」 | 同上 `:108`；另 `:117`「I don’t tell that story to many people, it **squicks them out**」 | 「两次初遇」的镜像关系写对，未颠倒 | **假红** |
| md:15「Easter Parade 到底指游行还是指行动，都没有被解释」 | `:76`「But Easter Parade is also the code name of an effort to expose a bunch of white supremacists’ links to an Illinois congressman.」＋`:80` Clare 答「Maybe next year you could get some extra dogs…」 | md 把它列为「限知视角的有意留白」，与原文一致 | **跳过**（md 已交代取舍） |

计数（只数阻断档）：漏 1 · 编 0 · 错 0；提示 3；假红 3；跳过 1。

## 已核实为正确

1. 日期：md:11「2023 年 4 月 15 日」= `:18`；天气「连日八十度」= `:23`「80 degrees day after day is eerie here in mid-April」。
2. 地点：`:29`「Café Selmarie」＋「Your mom’s already here」；广场干喷泉/空演奏台 = `:28`。
3. Beck 缺席原因：`:60`「She was, but she had to go to Detroit… it’s got to do with Jasper. Someone told Beck they’d seen him, and he wasn’t doing too well… She couldn’t find him.」；`:65`「Beck is Alba’s stepmother」——md:45 只写「去了底特律找人」，成立（未写 Jasper 名字属可接受的压缩）。
4. 「Alba 父亲最爱吃的」：`:65`「“That was Alba’s dad’s favorite,” Clare says, nodding at my plate」。
5. 王尔德引语：`:225`「‘In matters of grave importance, style, not sincerity is the vital thing.’」；md:13 引作「要紧的是风格，不是真诚」，逐字对。
6. 号码是事先写好的：`:199`「She passes me a slip of paper, **written out beforehand**」；「需要解释很久的那种」= `:207` 前后「especially one that takes a lot of explaining」。
7. 决定论那组对白：`:123`「If your life is a huge causal loop, you don’t have freedom of choice…you were always locked together in a great big deterministic circle.」＋`:128`「we did choose each other, moment by moment, day by day」——md 块 6 取的是 Clare 后半，前半由 md:11 概述，未错。
8. 丧失观：`:147`「I think loss just mutates. You can’t have the person you lost, so you rebuild yourself around that emptiness.」
9. Montrose Beach 那段：`:181`「Alba was four. We were at Montrose Beach with Charisse and the kids…we found her with her older self. You must have been in your sixties…like seeing Henry’s doppelgänger」；md:15 提「她一直念叨水」= 同段 `:189` 前后，Alba 摇头制止也确有其事。
10. 替班揭底：`:328`「She’s back in the 1980s, with my dad. I’m coming from July 2025. We sometimes manage to fill in for each other like this.」
11. 回程：`:413` 起点「I turn the ignition and head east」＋`:418`「roll the windows down and crank up the stereo…David Bowie sings “Heroes”…potentially glorious despite the abnormal weather」；「just for one day」重复两次 = `:419` 末句。
12. 机器层块序与原文顺序一致（`:23`→`:28`→`:34`→`:108`→`:108`→`:128`→`:199`→`:287`→`:328`→`:418`），第 4、5 块同出一段长文但各取一处、不重叠。
