# ch46 the drowned hotel — 对账单（R3）

- 原文：`text/ch46_the_drowned_hotel.txt`（255 行；两段：2041-10-30/31 抵达伦敦；2041-10-31 / 2041-10-29 / 2055-07-02 夜间穿越，Oliver 13 与 26）
- 精读：`ch46 the drowned hotel.md`（133 行）
- 机器层：`2-machine.json` rc=0，verdict=ok，8 块 / 8 段引语全逐字，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5 条，H1 `46. The Drowned Hotel`，words 2410，block_target [4,8] 达标、无 hint

## 〇、作业单相关点

- 亲属称谓：`grep -c "舅舅\|叔父"` → 0（ch46/ch47 均 0），全篇「叔叔」（含 `md:11` 「叔叔斯蒂芬」）。原文 `:63` “my Uncle Stephen” / `:69` “Uncle Stephen”。**统一「叔叔」成立。**
- 年龄：`md:11` 「十三岁的奥利弗」与 `:18` “Oliver is 13” 对齐；2055 段「26 岁」未写（见 L6）。

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | Isadora 的**两条**交代：①别让人看见你跟我在一起（他们会问太多问题）；②**最好也别跟你叔叔提起我**。block 1 只截后半句「你一直在我的保护之下」+ 催他走 | `:28` “It will be better for you if no one sees you with me. They will ask too many questions. **It might be best if you don’t mention me to your uncle, either.**” | block 1 引语自 “Don’t worry, Oliver.” 起，把前两句略去；`md:11`/`md:133` 导航提到「要他不许向叔叔提起自己」，块内无 | 提示（块内引语选短，R4 对应问题） |
| L2 | 「深睡 delta 脑波会降低时间旅行的可能」→ 他此刻才明白 Isadora 为什么想让他昏睡 | `:77` “This talk of jet lag and circadian rhythms alarms me. Now I understand why Isadora wanted me unconscious: the delta brainwaves of deep sleep decrease the likelihood of time travel.” | `grep -c "脑波"`→0、`grep -c "昏睡"`→0；导航只写「一路用时间差、速成与自己的身世给他立规矩」 | 提示（本章唯一解释「她为什么让他睡」的因果，全无） |
| L3 | 叔叔泼冷水：连他也弄不进皇家学院，得苦读六个月再试奏，「进不去我再给你想别的」 | `:85` ““Even I cannot get you into the Royal Academy with no skills whatsoever. You are going to have to cram for six months, and then audition. If you don’t get in, I’ll think of something else for you to do.”” | `grep -c "皇家学院"`→0；导航只有「六个月速成和试音」（无「皇家学院」这个目标，也无「进不去就另想法子」的威胁） | 提示（下一章的赌注全靠这句） |
| L4 | 本章的题眼句「这是最低点，会好起来」未进任何块 | `:200` ““It’s going to be all right,” he says. “This is the low point. It will get better.”” | 只在 `md:12`（情感弧线）与 `md:133`（一句话总结）出现；8 块里没有 | 提示（题眼句只在导航，引语层缺席） |
| L5 | 2055 年院子里那层伏笔：屋里有个「你现在还不该见的人」，且该在**真实时间**里见（不是他猜的女友/妻子）；以及「他不想你在身边，你也很少会见到他」「有人爱你」 | `:217` “This is London, in 2055. I wish I could invite you in, but someone is here that you shouldn’t meet yet.”；`:225` “You should meet this person in real time. Not now.”；`:242` “But he doesn’t want you around any more than you want to be near him. You will rarely see him.”；`:251` “You have people who love you.” | `grep -c "真实时间"`→0；块 7 只到拥抱与「你看上去很糟」 | 提示（「谁在这个屋里」是全书重要悬置） |
| L6 | 真名：年长的自己用普通话喊他「Yang Qing」（Oliver 是新名字的对照）；2055 年他 26 岁 | `:184` ““Yang Qing, come here,” he says, in Mandarin.”；`:229` “In 2055 I will be twenty-six.” | `grep -c "杨清"`→0、`grep -c "Yang"`→0、`grep -c "二十六"`→0（`26` 仅 frontmatter 日期） | 提示（`md:39` 只说「真名」不落地；年龄锚点 26 缺） |
| L7 | 中间那两次落地：河边裸土呕吐、有人喊「Oi!」、砖房后院草丛 | `:180` “I vomit the spaghetti onto bare dirt. I am outdoors, at night, near the river. … a man sees me and shouts Oi! … Then I time travel again—… an overgrown garden in back of an unfamiliar brick house.” | `md:11`「他在惊惧中穿到二〇五五年的伦敦」——一跳直达，中间两跳全无 | 提示（`ch46` 标题「淹水的旅馆」与水线的呼应，一大部分在这段夜里） |
| L8 | 到达大厅：几百人、举牌、铝膜气球；他在人群里找不到叔叔 | `:47` “There are hundreds of people waiting on the other side. They have signs, and mylar balloons, and they are all talking at once.” | 无 | 跳过（氛围） |
| L9 | 电梯楼层、镜子里的憔悴、叔叔在床上喝啤酒看电视 | `:148` `:162` `:163` | 无 | 跳过（`md:89` 结尾块已覆盖「他自己那半边」） |

## 二、编（md 有、原文无）

无。逐条回查：`md:13`「替人开门的司机」有 `:53` “He motions for me to follow him”；`md:14`「背熟客套」有 `:106` “My mother made me rehearse this speech with her.”；`md:13`「只在自己身世那一段露出一点真」有 `:115-120`；`md:67`「水线留在墙上没人铲掉，工人只是往上刷漆」有 `:143` “two men are repainting a wall in the lobby that has a knee-high flood line”。

## 三、错（两边都有但不一致）

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `md:14` 人物弧线 | 「他学会不露慌、背熟客套、**把疑问咽回去**」 | `:255` “I am about to ask him who Isadora is, and what she meant when she said that I am under her protection?—but I am gone, back to the hotel bathroom” | **错（提示）**：疑问不是他咽下的，是**话没出口就被拽走**；这一篇的收束正在「没问成」，写成「咽回去」把被动改成主动 |
| E2 | `md:51` 中文理解 | 「叔叔说自己是那个「黑孩子」…**父母**交不出二胎的罚款，知道他不会有户口」 | `:115` “I was the black child, the extra. **Our parents** knew that I wouldn’t have a hukou because they were never able to pay the fines for having two children.” | **错（提示）**：此处的「父母」是**叔叔与奥利弗父亲的父母**（即奥利弗的祖父母），不是奥利弗的父母；且「black child」在此语境＝**黑户**（无户口），`md:51` 保留「黑孩子」但不注明，易被读成肤色 |
| E3 | `md:11` 一句话概括 | 「夜里两人**同住**河畔旅馆」 | `:148` “The hotel room is small; the bed takes up most of the room.”；`:158` “I tell him I don’t mind sharing a bed with him.” | 假红（「同住」不假；同床这层由块 6 的「叔叔的手…在我们的床上」承担） |
| E4 | `md:15` 叙事手法 | 「两个日期栏把一章劈成两半」 | `:18` 一个日期栏（10-30 与 10-31）、`:171` 一个日期栏（10-31 / 10-29 / 2055-07-02）——版式确是两栏 | 假红（栏内日期数不影响「两栏」的判断） |

## 四、归属方向复核（R4 三问）

- 块 1 “You are always under my protection” ⇄ `:37`：说话人＝**Isadora**；受事＝Oliver；md `:21`「她叫他别担心」——正确。但被承诺的「保护」从何而来（`:255` 他正要问）在本块无着落。
- 块 2 “they are giving me hard looks” ⇄ `:43`：施事＝**入境官员**；受事＝他；md `:31` 未写成「他打量官员」。
- 块 3 “He calls me by my real name” ⇄ `:63`：叫名字的人＝**叔叔**；「他不会说普通话」是叔叔**对 Oliver 说**（不是对司机说）；md `:41`「叔叔说没关系，司机不会说普通话」——方向正确。
- 块 4 “I was the black child, the extra” ⇄ `:115`：说话人＝**叔叔自述**；「Our parents」＝**祖父母**（见 E2）；「made sure I was born here」的施事＝祖父母，受事＝叔叔本人；md `:51`「就设法让他生在英国」——施受方向对，指代需修。
- 块 5 “two men are repainting a wall” ⇄ `:143`：施事＝**两名工人**；受事＝带水线的墙；md `:61` 正确。
- 块 6 “My uncle’s hand is on my thigh—not moving” ⇄ `:180`：施事＝**叔叔**（睡着与否未知，原文故意不给）；受事＝Oliver；md `:71`「叔叔的手搭在他的大腿上，一动不动」——保留了两义，未擅自判「醒着」。
- 块 7 “he puts his hands on my shoulders” ⇄ `:195`：施事＝**年长的自己**；受事＝13 岁的他；md `:81`「对方让他意外：伸手搭住他的两肩」——正确（未写成叔叔）。
- 块 8 “My uncle is sleeping on his own side” ⇄ `:255`：施事＝叔叔；md `:91`「叔叔睡在自己那半边床上」——正确。
