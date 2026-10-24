# ch46 the drowned hotel — 判定表（R5）

- 原文：`text/ch46_the_drowned_hotel.txt`（255 行）
- 精读：`ch46 the drowned hotel.md`（133 行）
- 机器层：`2-machine.json` rc=0（verdict=ok，8 块，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5）
- 结论：**无阻断**；漏 7（提示）· 编 0 · 错 2（提示）· 跳过 2

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 8 块引语逐字、均属本章 | `2-machine.json` segments=8, segment_miss=0；回捞 `:37` `:43` `:63` `:115` `:143` `:180` `:195` `:255` 全命中 | 引语层干净 | 假红 |
| 2 | 亲属称谓是否混用 | `grep -c "舅舅\|叔父"` → 0（ch46/ch47 均 0）；全篇「叔叔斯蒂芬」；原文 `:63` “my Uncle Stephen”、`:69` “Uncle Stephen” | 统一「叔叔」 | 已核实为正确 |
| 3 | 年龄与日期 | `:18` “Wednesday, October 30, 2041, and Thursday, October 31, 2041 (Oliver is 13)”；md:11「二〇四一年十月三十日，十三岁的奥利弗」 | 正确 | 已核实为正确 |
| 4 | block 1 引语截短，漏掉「最好也别跟你叔叔提起我」这条命令 | `:28` “It will be better for you if no one sees you with me. They will ask too many questions. It might be best if you don’t mention me to your uncle, either.”；块内引语自 “Don’t worry, Oliver.” 起 | **漏（块内）**：命令本身在导航（`md:11`/`md:133`）里有，块内无 | 提示 |
| 5 | 「深睡 delta 脑波降低时间旅行可能」这条因果全无 | `:77` “Now I understand why Isadora wanted me unconscious: the delta brainwaves of deep sleep decrease the likelihood of time travel.”；`grep -c "脑波"`→0、`grep -c "昏睡"`→0 | **漏**：本章唯一解释「她为何让他睡」的句子 | 提示 |
| 6 | 皇家学院与「六个月苦读再试奏、进不去另想办法」全无 | `:85` “Even I cannot get you into the Royal Academy with no skills whatsoever. … If you don’t get in, I’ll think of something else for you to do.”；`grep -c "皇家学院"`→0 | **漏**：下一章的赌注，导航只留「六个月速成和试音」 | 提示 |
| 7 | 题眼句「这是最低点，会好起来」只在导航，未进块 | `:200` ““It’s going to be all right,” he says. “This is the low point. It will get better.””；`grep -n "最低点"` → `md:12`、`md:133`（两条都是导航） | **漏（引语层缺席）**：本章的立意句 | 提示 |
| 8 | 2055 院子里「有个你现在还不该见的人」「该在真实时间里见」这层悬置全无 | `:217` “someone is here that you shouldn’t meet yet.”；`:225` “You should meet this person in real time. Not now.”；`:242` “he doesn’t want you around any more than you want to be near him.”；`:251` “You have people who love you.”；`grep -c "真实时间"`→0 | **漏**：全书重要伏笔 | 提示 |
| 9 | 真名与 2055 年的 26 岁全无 | `:184` ““Yang Qing, come here,” he says, in Mandarin.”；`:229` “In 2055 I will be twenty-six.”；`grep -c "杨清"`→0、`grep -c "Yang"`→0、`grep -c "二十六"`→0 | **漏**：`md:39` 只说「真名」不落地（原文只有拉丁转写，**勿臆造汉字**） | 提示 |
| 10 | 中间两次落地（河边裸土呕吐 / 「Oi!」/ 砖房后院）全无 | `:180` “I vomit the spaghetti onto bare dirt. … a man sees me and shouts Oi! … an overgrown garden in back of an unfamiliar brick house.” | **漏**：「淹水」这一半意象在夜里 | 提示 |
| 11 | 到达大厅的几百人与铝膜气球 | `:47` “There are hundreds of people waiting on the other side. They have signs, and mylar balloons” | 未收 | 跳过 |
| 12 | 电梯楼层 / 镜中憔悴 / 叔叔喝啤酒看电视 | `:148` `:162` `:163` | 未收（块 8 已收到「他自己那半边」） | 跳过 |
| 13 | `md:14`「把疑问咽回去」 | `:255` “I am about to ask him who Isadora is… —but I am gone, back to the hotel bathroom” | **错（提示）**：疑问是**没问出口就被拽走**，不是他主动咽下；被动写成主动 | 提示 |
| 14 | `md:51` 的「父母」指代与「黑孩子」 | `:115` “I was the black child, the extra. **Our parents** knew that I wouldn’t have a hukou because they were never able to pay the fines for having two children.” | **错（提示）**：「父母」＝祖父母（叔叔与奥利弗父亲的父母）；「black child」此处＝**黑户**，不注明易读成肤色 | 提示 |
| 15 | `md:11`「两人同住河畔旅馆」 | `:148` “The hotel room is small; the bed takes up most of the room.”；`:158` “I don’t mind sharing a bed with him.” | 假红（同床这层由块 6 承担） | 假红 |
| 16 | `md:15`「两个日期栏」 | `:18` 与 `:171` 各一个日期栏 | 假红（版式判断成立） | 假红 |
| 17 | 「手没有动」的两义未被擅自判定 | `:180` “My uncle’s hand is on my thigh—not moving” + “He seems to be asleep. Is he asleep?” | md `:71` 保留「一动不动」，未写成「叔叔醒着」或「叔叔睡着」 | 已核实为正确 |
| 18 | 「叔叔叫他真名、司机听不懂普通话」的方向 | `:63` “He calls me by my real name… “It’s all right,” my uncle says to me. “He doesn’t speak Mandarin.”” | 叔叔对 Oliver 说，非对司机说；md `:41` 正确 | 已核实为正确 |
| 19 | 「伊莎多拉推他一把后消失」 | `:37` “Isadora gives me a little push… I look back, but Isadora has disappeared.” | md `:21`「接着又催他走」+ 通道口退场，与原文一致 | 已核实为正确 |
| 20 | 词汇 15 条例句逐字 | 例：`:105` “so gray and uninviting”；`:109` “Our parents knew that I wouldn’t have a hukou…”；`:120` “kneeling on the cold tile floor, dry heaving”；`:115` “It helps to look at sunlight, it will reset your circadian rhythms.” | 全命中，无改写 | 已核实为正确 |

## 已核实为正确（防下一轮误修）

1. **「叔叔」不是「舅舅」**：`:63` “my Uncle Stephen”；全书统一「叔叔」（`grep -c "舅舅"`→0）。**勿改。**
2. **2041 年他是 13 岁**：`:18` “(Oliver is 13)”；`:319`（ch45）““Thirteen.””。**勿因 1975 段（ch45，38 岁）把他整体改成成年人。**
3. **真名只有拉丁转写 “Yang Qing”**：`:184`。**勿臆造汉字姓名**（原文未给汉字）。
4. **2055 年的他是 26 岁**：`:229` “In 2055 I will be twenty-six.”——与「13 岁」不冲突，是同一夜的穿越。
5. **「手没有动」不能判成猥亵已遂或未遂**：`:180` 原文只给 “not moving” + “He seems to be asleep. Is he asleep?”，**故意不给答案**。md `:71` 保留两义是对的，**勿在正文替作者定性**（若要加一句，只能写「她不确定他是否醒着」之类，不能写「叔叔装睡」）。
6. **「黑孩子」是黑户（无户口），不是肤色**：`:115` 同句紧接 “I wouldn’t have a hukou because they were never able to pay the fines for having two children”。**勿译作「黑人孩子」。**
7. **「Our father was British」是叔叔说祖父**：`:115` “I came here because I could. Our father was British.”——这句解释的是**兄弟二人为何能有英国身份**，不是叔叔一人的父亲。**勿写成「奥利弗的父亲是英国人」**（奥利弗父亲只能「claim English citizenship」，`:115`）。
8. **叔叔 33 岁来英国，那年奥利弗 8 个月大**：`:106` “I was thirty-three. You were eight months old.”。**两个数字勿对调。**
9. **旅馆在河边、水线齐膝、正在重刷**：`:143` “The river is near the top of its banks… a knee-high flood line.”——这是书名「淹水的旅馆」的落点。**勿改成「地下室进水」。**
10. **结尾他等到天亮，没告状也没叫醒叔叔**：`:255` “I dress and wait by the window to see what the day will bring.”。**勿补写「他决定告诉叔叔」之类。**
11. **车是真人驾驶，他第一次坐人开的车**：`:63-64` “the freckled man is actually driving… I’ve never been in a car driven by a human before.”。**勿写成自动驾驶。**
