# ch13 Coming Attractions · R3 对账

- 素读：`1-suread.json`（10 条，写定于打开 md 之前）
- 机器层：`2-machine.json`，rc=0，10 块 / 10 引语 / segment_miss=0 / 查无 0 / 空引号 0 / 字数 3947
- md：`ch13 coming attractions.md`（153 行）

## 一、漏（素读有、md 无）

### L1（阻断）Oliver 关于「信息不足」的警告与「我存在于他不知道的空间」——md 全章查无

素读第 8 条。原文两处（一处出自 Oliver，一处是 2025 年 Alba 心里复述同一句）：

```
text/ch13_coming_attractions.txt:478  “Most of the difficulties in Zach’s life will stem from a lack of information. You won’t tell him things he needs to know.”
text/ch13_coming_attractions.txt:486  “All this. Your life. Zach doesn’t know what goes on in half of your life.”
text/ch13_coming_attractions.txt:494  “Don’t worry, I’m not advocating telling Zach anything. I exist in the space he doesn’t know about.”
text/ch13_coming_attractions.txt:637  I exist in the space he doesn’t know about. What if I tell Zach everything, right now, before it happens?
```

md 侧：无。取证：

```
$ /usr/bin/grep -nE "space he doesn|lack of information|信息不足|Zach 一生|不知道的那" "ch13 coming attractions.md"
（无输出）rc=1
```

md 第 11 行导航只写到「他弹肖邦的《海洋》练习曲…然后他上楼睡觉」，第 13 行情感弧线、第 15 行 Tropes、第 17 行人物弧线均无此交锋；第 93-101 行（原句 8）讲的是 Alba 自己的「get my story straight」，不是 Oliver 这段话。

判定：这是本章把「隐瞒」从巧合变成定论的一场戏——Oliver 替读者说出了 Alba 婚姻的裂缝在哪，且第 637 行 Alba 在浴缸里原样复述这句话，是全章主题句。md 既未进块、也未进导航，且未写任何取舍理由 ⇒ **漏，阻断**。（修法建议：10 块已触本书上限，宜折进导航/人物弧线，不必新开块。）

### L2（提示）1964 年出租车队里的老年夫妇——只在词汇例句里留下一半

```
text/ch13_coming_attractions.txt:23  She has a blue fox stole; he is wearing a cashmere overcoat. They must be immensely old, they both have freakishly enormous ears.
```

md 侧：正文只以「皮草」（第 13 行）带过；`freakishly` 的例句（第 132 行）保留了 enormous ears，但「蓝狐披肩」只在第 19 行「年代靠物件写」的清单里出现，作为时代道具而非场景人物。

判定：非关键事件，且开篇镜头的主要功能（时代质感）已由「皮草/羊绒/Old Spice/肯尼迪徽章」承担 ⇒ **提示**。

## 二、编（md 有、原文无）

### N1（提示）md 第 99 行：「说明 Oliver 不是新出现的人，而是刚刚被她归了类」

```
md:99  suddenly become part of 说明 Oliver 不是新出现的人，而是刚刚被她归了类
text/ch13_coming_attractions.txt:93（同章前文）  “Really? This is it?” He laughs. “What a bizarre way to meet a girl. Wow.”
```

原文的 `has suddenly become part of the Yellow House`（`text/ch13:626`）说的是「他忽然成了黄房子的一部分」，即归属关系刚成立；md 把它读成「他不是新出现的人」，与本章开头他刚从街上跑来这一事实相抵。后半句「刚刚被她归了类」才是原意。

判定：属解读措辞失准，非情节虚构 ⇒ **提示**（改法：删「不是新出现的人」，留「刚刚被她归了类」）。

## 三、错（两边都有但不一致）

### E1（提示）md 第 11 行导航：弹琴与点曲的先后倒了

```
md:11  …他弹肖邦的《海洋》练习曲，问她想听什么，她点了这首；后来他让她也弹一段…
text/ch13_coming_attractions.txt:384  “Of course.” Oliver stands up and stretches, tries to loosen his neck and shoulders. He sits at the piano. “Anything in particular?”
text/ch13_coming_attractions.txt:388  “That étude. The Chopin.”
text/ch13_coming_attractions.txt:392  He laughs. “It’s been a while. I don’t know . . .” I stand at his side, slightly behind him. He rests his fingers on the keys.
text/ch13_coming_attractions.txt:393  Then he plays.
```

原文顺序是：问「想听什么」→ 她点这首 → 他才弹。md 写成「先弹、再问、她点」，把因果与礼貌关系都倒了（她点的正是他刚讲过的那首，这是有意的呼应，倒叙后呼应消失）。

判定：**提示**（导航一句话的语序，不影响块内分析；第 73-81 行原句 6 的解读顺序是对的）。

## 四、R4 逐块对应（10 块）

| 块 | 引语（首句） | 这段中文是不是在讲这句引语 | 三问（主语 / 受事 / 归属） |
|---|---|---|---|
| 1 | `I turn and there’s a naked man running down Wacker Drive…` | 是。「她替一个还没跑到的人把着门」「心跳」都对得上 | 主语：Alba（转身/看见/扶门）；受事：车门、跑来的男人；归属：她误认他是父亲——`text:28` `I haven’t seen my dad in years.` 在她心跳之后，md 第 31 行「紧接着的一句」定位正确 |
| 2 | `A dresser appeared in that bedroom in 1960…` | 是。清单性质、婚戒与 JFK 徽章的年代功能都讲了 | 主语：无人称（物自己出现）；受事：清单物件；归属：婚戒「说明这人有妻子」——`text:54` 只列物，未点明妻子，属合理推断（同段后文他确实戴着婚戒） |
| 3 | `He’s freshly shaved, and I can smell Old Spice…` | 是。`The kiss says` 的宣告语气讲透了 | 主语：Oliver（吻）；受事：Alba；归属：吻的「说话人」是 Oliver 这一方，md 未错置；「她问 Who are you? 在吻之后」核对 `text:81-89` 正确 |
| 4 | `It was kind of a mess, actually, my playing that day…` | 是。a mess / possessed / installed 三层换说法准确 | 主语：Oliver（弹）；受事：那天的演奏；归属：`the player I was going to become` 指他自己，md 第 61 行「他还没走到的自己」方向正确 |
| 5 | `I had an uncle who lived in Bristol, but he was and is insane…` | 是。「一句比一句短」「家还在，回不去」对得上 | 主语：Oliver 的叔叔/Oliver；受事：家；归属：`my parents were in prison` 是他的父母，md 第 71 行「十八岁那年」引 `text:266` 正确 |
| 6 | `His hands move together in waves…` | 是。潮汐/建筑术语/`familiar and not` 都落在引语上 | 主语：Oliver 的手；受事：琴键、旋律结构；归属：`I have not heard…` 的「我」是 Alba，md 未误置 |
| 7 | `Alba: It’s almost dawn when I get home…` | 是。「门没锁比一句他在等更说明问题」是对引语末句的解读 | 主语：Alba（回家）、Zach（没锁门）；受事：雪、草地；归属：`Zach left the back door unlocked` 施动者是 Zach，md 第 89 行未错 |
| 8 | `I need to get my story straight…` | 是。三个问句语气与「黄房子不进外人」的原则都讲了 | 主语：Alba；受事：说辞、Zach；归属：`I do not tell people about the Yellow House` 的「我」= Alba，md 第 99 行「她的辖区」正确 |
| 9 | `My dad always said no, you can’t change anything…` | 是。`or, rather` 的自我修正讲得准 | 主语：她父亲（说）、Alba（没能推翻）；受事：已发生的事；归属：规矩的出处是父亲，md 第 111 行明确 |
| 10 | `“Look, Alba, it’s a pair of cardinals,” Zach says…` | 是。「被人指给她看」「全是些不体面的细节」都贴着引语 | 主语：Zach（说/做吐司前）、Alba（看）；受事：鸟、喂食器、Zach 的样子；归属：`our kitchen window` 是两人共有的窗，md 第 121 行「桌边的两个人」与此一致 |

R4 结论：10 块中文均与所贴引语同层，无「讲引语之外的上下文」、无「讲全书主旨」、无「只复述字面」。**对应 0 缺陷。**
