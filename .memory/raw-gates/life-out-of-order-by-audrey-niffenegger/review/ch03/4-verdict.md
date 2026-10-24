# ch03 判定表（R5）

章：`ch03 fallout.md`（153 行，10 块）
原文：`text/ch03_fallout.txt`（1106 行 / 8934 词）
机器：`2-machine.json` rc=0；块数 10；引语 10 段全 ok；`segment_miss` 0；空引号 0；子项缺 0；`keyword_bad` 0；`cjk_low` 0；`block_hint` 仅提示块数（本书中位 6、最高 10，本章并列最高）。
素读：`1-suread.json` 14 条，`quote in line` 校验 14/14。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 他们为什么半夜出逃（有人在外面等）应进块或导航 | `text/ch03_fallout.txt:101`「Zach’s car is pretty conspicuous. It was noticed, and **there are some guys waiting for you out there**」＋`:109`「**Large guys. Friends of Junior’s**」；md 全章 `grep -nE "Junior\|朋友"` = 0（exit 1），md:11 只写「Caralora 拉响火警」 | 起因全缺，从「拉火警」直接跳到「钻隧道」 | **阻断**（漏） |
| 敌手的分量（死了七个人）应至少一句 | `:1042`「**Junior and his friends killed seven people** that I know about, and they had allies in the police」；md `grep -n "七"` = 0 | 同上，读者无从知道这一夜有多险 | **阻断**（与上行同一处，合并计数） |
| 进门暗号「jellyfish paradox」 | `:34`「Zach gives the password, jellyfish paradox, and we’re in.」；md `grep -n "jellyfish"` = 0 | 细节未落 | 提示（漏） |
| 「另一个 Alba」登场方式与当面消失 | `:242`「It’s me. Of course.」`:244`「I brought a ladder」`:247`「The floor is rotted out」；`:375`「She steps back inside, but I see her vanish before the door closes.」；md 仅 md:27 出现「梯子」一词，`:375` 无块无导航 | 两个关键动作未落 | 提示（漏） |
| Caralora 为什么敢离开 Alba | `:983`「the other you told me I would start again. **She knew my real name**」；md:14 只写「她厌倦了当那套支撑系统」 | 丢了「年长 Alba 促成」这一层 | 提示（漏） |
| md:11/md:15「元旦早上…同一个早上被写了两遍」 | `:412`「fireworks to the east, along the lakefront」＋`:401`「Come back tomorrow and pick it up」＋`:638`「**We fall asleep in the New Year**」＋`:641`「**Zach: I wake up happy.** The light around the edges of the blinds is white.」 | 喝茶在 1 月 1 日凌晨，Zach 段在睡醒后的上午；日期对、时段错并 | 提示（错） |
| md:11「她当面指出他改过名字」是否把话说反 | `:507`「“**You’ve changed your name**,” I say. “Was any of the other stuff you told me true?”」 | 确是她先开口，写法成立 | **假红** |
| md:105「后备箱里装着他十二岁那年祖母给他缝的被子、书、母亲扔进垃圾桶的相册」 | `:861`「A quilt my grandmother made for me **when I was twelve**. My books. **Photo albums that my mom had thrown in the trash**.」 | 三项逐字对得上 | **假红** |
| md:11「派对主题要迎接的是 1923 年，不是 2023 年」 | `:23`「The theme is “The Beautiful and Damned” (we are supposed to be welcoming **1923, not 2023**)」 | 括号里的更正已进导航，属正确抓取 | **假红** |
| md:12「2023 年元旦的消失始终没有下文，填空题留到 2029 年」 | 原文 `:766` 之后直接切 `:838` Caralora 来接；`:1079` 才是她回到 2029 | 这是 md 明写的取舍，不是漏 | **跳过** |

计数（只数阻断档）：漏 1 · 编 0 · 错 0；提示 4；假红 3；跳过 1。

## 已核实为正确

1. 抬头：md:11「2022 年 12 月 31 日」= `:18`「Saturday, December 31, 2022, and Sunday, January 1, 2023 (Alba is 21 and 21, Zach is 22)」；md:11「2029 年 7 月 28 日：27 岁的 Alba」= `:1074`「Saturday, July 28, 2029 (Alba is 27, Zach is 28)」＋块 10 中文的「27 岁和 28 岁」。
2. 父亲忌日＝跨年夜：`:24`「New Year’s Eve because that’s the anniversary of my dad’s death」。
3. 借裙：`:23`「I’ve borrowed a beaded dress and some vaguely appropriate low-heeled shoes from Mama’s closet」——是借，非买；md:11 写「借」正确。
4. Green Mill 隧道史：`:158` 前后（Capone、运煤、赌局、藏酒）与 md:11「钻过 Green Mill 底下的隧道」一致；Uptown 1981 年关闭＝`:200`「has been closed since 1981」。
5. 停车位：`:34`「next to St. Boniface Cemetery」；md:33 读者视角提示据此预告「下一段故事要在光天化日里回到这里」——该预告是否兑现属 ch04 的事，本条只核「停在哪」：正确。
6. 午夜台词：`:330`「You make me want the future.」；md:11 引用逐字无误。
7. 地下室钢门与谎话：`:471`「It’s kind of a family secret.」＋`:475`「There’s a lot of computer equipment down there…」；md:57 读者视角提示「一边把童年摊开给他看，一边把地下室锁上」对应准确。
8. 换声部位置：`:641`「Zach: I wake up happy.」；md 块 8 起改由 Zach 叙述，读者视角提示明说。
9. 洗澡：`:766`「I realize that I’ve been listening to bathwater for a long time」；`:769`「I open the door and find water overflowing and—no Alba.」
10. 车与家当：`:838` 三段烧毁细节（windows shattered / tires melted / charred gray-and-white hulk）＋`:861` 后备箱清单＋`:871`「I don’t have a home…The Nash was all that was left of home.」
11. 2029 结尾：`:1101`「‘It’s all for the best in the best of all possible worlds.’」；`:1093`「Belated thanks, darling. Good work.」；md:121 读者视角提示「幸好只是她」对应 `:1096` 前后 Zach 抓毛巾松口气的动作，块 10 中文「27 岁和 28 岁」对应 `:1074` 抬头。
12. 机器层逐字：`2-machine.json` 10/10 segments ok，块序与原文顺序一致（`:23`→`:34`→`:273`→`:297`→`:456`→`:527`→`:710`→`:766`→`:838`→`:1079`），无倒置。
