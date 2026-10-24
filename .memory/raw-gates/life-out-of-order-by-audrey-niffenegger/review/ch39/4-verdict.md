# ch39 making music — 判定表（R5）

原文 `text/ch39_making_music.txt` 435 行／精读 `ch39 making music.md` 130 行；机器层 **rc=0**（verdict=ok，块 8／引语 8／段 8 全 ok，查无 0／空引号 0／子项缺 0／关键词 0／结构 0／密度低 0／模板 0／洞 0，words 2761，H1 `39. Making Music`，导航 5，block_target [5,9]）。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 抬头「2015 年 6 月 6 日／阿尔芭 13 岁、克莱尔 44 岁、贝克 39 岁」与原文一致 | `text/ch39_making_music.txt:18` “Saturday, June 6, 2015 (Alba is 13, Clare is 44, Beck is 39)” | md 正文未抄年龄，只写「二〇一五年六月六日」（`:130`）；数字本身未出错——**未抄 ≠ 抄错** | 跳过 |
| 两日两视角的归属正确（6/6 阿尔芭、6/7 克莱尔） | `:23` “Alba: I wake up in my own bed”；`:174` “Clare: These days our lives are conducted around the dining room table.” | md 叙事手法（`:15`）「六月六日由阿尔芭以第一人称讲，六月七日换成克莱尔」；块 5 读者视角（`:67`）「这一段由克莱尔叙述」——两处都对 | 已核实 |
| 「贝克雇侦探查贾斯珀」的施动者与对象都没错挂 | `:47` ““I’m off to hire a detective,” Beck says.”；`:55` ““She wants to know what happened to Jasper.”” | 导航（`:11`）「她得知贝克雇侦探去查失踪的贾斯珀」；人物弧线（`:14`）「贝克以雇侦探……」——施动者＝贝克、对象＝贾斯珀，正确 | 已核实 |
| 「她说漏教堂枪击，母亲才明白她已知未发生的事」时序与因果成立 | `:108-110` ““It was in the news, there was a shooting at a church…”… “What church?” Mama puts down her fork.”；`:104` “We both know we can’t stop it. It’s already happened.” | 导航（`:11`）与块 3 中文理解（`:41`）「她说漏了教堂枪击，母亲追问」——与原文同序，正确 | 已核实 |
| 「母亲说快乐本身就有用」是克莱尔的话，不是阿尔芭的反问 | `:137` ““Music gives people joy, and joy is very good for a person,” Mama says.” | 总结（`:130`）「阿尔芭反问音乐有什么用，母亲说快乐本身就有用」——问答两头都对上了 | 已核实 |
| 「都没要她上卡内基音乐厅」保留了否定的**双方**（父亲、外公），不是只说一个人 | `:150-156` ““Your dad wanted you to learn music because he loved it… My father saw that you had a gift and he wanted you to use it… But neither of them needed you to play Carnegie Hall… Art isn’t something you owe to anyone.”” | md 块 4 中文理解（`:51`）「父亲……外公……但两个人都没要求她登上卡内基音乐厅」——两人都保留，正确 | 已核实 |
| 「D 调、两个升号、三张纸、小提琴」这四个参数一个不错 | `:240` ““How about D major? Two sharps.””；`:244` ““Three pieces of paper.””；`:252` “Go get your violin.” | 块 6 中文理解（`:71`）四项齐全；词汇表 `improvise` 例句亦为原句 | 已核实 |
| 「阿尔芭和母亲几乎同时说『不行』」是两人，不是母亲一个人 | `:395` ““No—” Alba and I say at the same time.” | 块 7 中文理解（`:81`）「阿尔芭和母亲几乎同时说『不行』」——人数正确 | 已核实 |
| 打电话的限制属于阿尔芭自己（她不能往出生前、买房前打） | `:390` ““I can’t call here before Mama and Daddy bought this house in 1994. And I don’t call before 2001, when I was born.”” | 块 7 中文理解（`:81`）主语保留为阿尔芭，未错挂成「父母不接」 | 已核实 |
| 「艺术家得闲荡」出自贝克；克莱尔说的是命令句「去……闲荡」 | `:324` ““Artists have to noodle, that’s how we get ideas,” Beck says.”；`:435` “Go on, find your violin, noodle.” | md 人物弧线（`:14`）与总结（`:130`）均挂给贝克；块 8 读者视角（`:97`）「上一段克莱尔把女儿赶走：「去，找到你的小提琴，闲荡。」贝克也说过艺术家必须闲荡」——两人分工清楚 | 已核实 |
| 做纸浆的是克莱尔、训练伊莎多拉的是贝克 | `:435` “I collect all the bits of linen into a bag… I head to my studio to beat the linen into paper pulp.” | 块 8 中文理解（`:91`）「贝克下楼去训练伊莎多拉，她自己到工作室把亚麻打成纸浆」——正确 | 已核实 |
| 结尾「不写成功，只写琴声从零碎变得有目的」的概括与原文同构 | `:435` “random nothings that slowly become purposeful, music assembled from thinking out loud.” | 叙事手法（`:15`）与块 8 为什么这样写（`:95`）「从 random nothings 到 purposeful，中间是『慢慢』」——逐字对应 | 已核实 |
| **她已知的未来清单**（明年选举结果／仇恨犯罪／大流行病／内战／气候变化）在 md 中零命中 | `:123` “I agree, but I already know more than I want to: next year’s presidential election results, all the crazy hate crimes, the pandemic, the civil war, climate change . . . but I can’t tell Mama.”；取证：`/usr/bin/grep -nE "选举|疫情|大流行|内战|气候|仇恨" "ch39 making music.md"` → 无输出 **rc=1** | 缺口成立。「知道未来帮不上忙」的判断还在（`:130`），但**支撑这个判断的五样具体事物全丢了**——本章的题眼因此只剩一句抽象话 | 提示 |
| 「服务器」这条物证方向在 md 中零命中 | `:64` ““She just wants to know he’s safe and find out if he’s the one who messed with her servers.””；取证：`grep -nE "服务器"` → 无输出 rc=1 | 缺口成立。贝克雇侦探的**目的**被压成「查失踪」，丢掉了「他有没有动过我的服务器」这层（与后文 Jasper 的专利/IP 旧账同一根线） | 提示 |
| 「空着的第四副餐具」在 md 中零命中 | `:174` “We’d eat with her art projects and violin homework pushed over to the empty, fourth place at the table”；取证：`grep -nE "第四|餐具"` → 无输出 rc=1 | 缺口成立。这是全书对「亨利不在了」最克制的一笔，md 只在读者视角（`:67`）交代了报纸与碎布，漏掉了这张桌子的历史 | 提示 |
| 「专注就不穿越」这条机制在 md 中零命中 | `:137` “Your dad always said that music helped him stay in the present, and I think it does that for you, too; it helps you concentrate, and when you concentrate you don’t time travel so much.”；取证：`grep -nE "专注"` → 无输出 rc=1（md 只有「快乐本身就有用」） | 缺口成立。音乐与时间病的接线在这一句上，缺它母亲的劝导就退化成泛泛的育儿安慰 | 提示 |
| 「如果你不想做音乐，你就不必做。它是你的」在 md 中零命中 | `:156` “But if you don’t want to make music, you don’t have to. It’s yours”；取证：`/usr/bin/grep -nE "它是你的" "ch39 making music.md"` → 无输出 **rc=1**（注：若把 `不必` 并入模式会命中 `:21`「不必去任何地方」，那是另一句，与本条无关） | 缺口成立（轻）。md 用「从没要她上卡内基音乐厅」承担了大部分同义功能，故只记提示 | 提示 |
| 实操清单（洗车／吸尘／洗澡／洗地板／「有真科学，你该谷歌一下」）与家务玩笑在 md 中零命中 | `:324` “Or, you can do some boring thing, like washing the car, or vacuuming.”；`:334` “Anything involving water is good,”；`:351` “There’s real science behind this. You should google it.”；取证：`grep -nE "吸尘|洗车|谷歌|家务"` → 无输出 rc=1 | 缺口成立。「闲荡」抽象地收了，具体办法与那记玩笑全丢 | 提示 |
| 求子那些年＋「Kids」在 md 中零命中 | `:409` “I think of those years when we were trying so hard to have a baby and Alba was there on the other end of the telephone line, breathing and then hanging up gently. Kids, Henry used to say whenever it happened.”；取证：`grep -nE "求子|怀孩子"` → 无输出 rc=1 | 缺口成立。md 读者视角（`:87`）停在「她只是想听听我们的声音」，没接到「那时她已经在电话那头了」这层回溯 | 提示 |
| 开头那幅把四个人都画进去的漫画在 md 中零命中 | `:28` “I draw a little cartoon Alba… my mother flying around like one of her bird sculptures and my dad reading a book. I don’t want Beck to feel left out, so I draw her with Isadora curled up on her lap.”；取证：`grep -nE "漫画|派对帽"` → 无输出 rc=1 | 快写过场，但「不想让贝克被落下」是这个重组家庭的一条底色；删之不伤主线 | 跳过 |
| 读纸质报纸的仪式（「死掉的树」）与「这听着像约会」在 md 中零命中 | `:189` “Neither Beck nor Alba have any interest in The New York Times in physical form. Dead trees, they both say.”；`:419` ““That sounds like dating,” I say. Beck and I exchange smiles.”；取证：`grep -nE "死掉的树|约会"` → 无输出 rc=1 | 生活质感与一句玩笑，不承载事件 | 跳过 |
| 「让马洛跑腿」译错：give sb the runaround＝把人耍得团团转，「跑腿」是 run errands | md `:37`「贝克说要去找侦探，还自比侦探小说里让马洛跑腿的女人」／原文 `:47` ““I’m going to be that dame giving Philip Marlowe the runaround.”” | 方向与词义双偏（「跑腿」把施受关系理解为「替马洛办事」，原文恰是「让马洛白转圈」）；md 词汇表 `runaround` 释义「推诿、拖延」本身正确，说明是行文时的手滑 | 提示 |
| 「本章最没把握的一处」＝L1 未来清单该不该升级为阻断 | 见上表 L1 行（`text/ch39_making_music.txt:123` + rc=1 取证） | 判提示：**判断在、证据亡**，读者仍能懂「她知道未来的事且无能为力」，只是不知道是哪五件；若后有修订轮次，优先补这一句 | 提示 |

## 报数（四组）

- **逐字**：8 条引语块全部逐字命中原文（机器层 8/8 段 ok，查无 0）；无一处引语被改写或拼接。
- **对应**：8 块逐块人判全部「这段中文在讲这句引语」；无一块跑题到全书主旨或作者生平。
- **形态**：H1／导航 5 条／子项 4 项（小说档）／块数 8 在 [5,9] 内；块序列与原文时序一致（6/6 → 6/7 结尾琴声）。
- **断言**：可核验断言 9 条（未来清单／服务器／第四副餐具／专注机制／它是你的／实操清单／求子／漫画／报纸），全部附 `grep` 命令与 rc，判「零命中」的 9 条 rc 均为 1。
  ⇒ **阻断 0 · 提示 7 · 跳过 2 · 已核实 13**

## 已核实为正确（防下一轮误修）

1. `ch39 making music.md:11` 导航「早餐时她得知贝克雇侦探去查失踪的贾斯珀」——原文 `:47`/`:55` 的施动者与对象都对；**不要**改成「克莱尔雇侦探」。
2. `ch39 making music.md:14` 「贝克以雇侦探、随口玩笑和『艺术得闲荡』推进另外两条线」——`:324` “Artists have to noodle,” **Beck** says；勿挂给克莱尔。
3. `ch39 making music.md:15` 「六月六日由阿尔芭……六月七日换成克莱尔」——`:23` “Alba: …”／`:174` “Clare: …”；视角没串。
4. `ch39 making music.md:41` 「她说漏了教堂枪击，母亲追问『什么人？什么教堂』」——`:108-110` 逐句对应；勿改成「母亲先说」。
5. `ch39 making music.md:51` 「父亲……外公……两个人都没要求她登上卡内基音乐厅」——`:150-156` 确实是**两人**，勿简化为一人。
6. `ch39 making music.md:71` 「D 调、两个升号、三张纸、小提琴」——`:240`/`:244`/`:252` 四项全对，勿改数字。
7. `ch39 making music.md:81` 「阿尔芭和母亲几乎同时说『不行』」——`:395` ““No—” Alba and I say at the same time.”；勿写成母亲单方面制止。
8. `ch39 making music.md:87` 「阿尔芭承认她只是想听听他们的声音」——`:405` ““Yeah, I just wanted to hear your voices,” she says”；主语是阿尔芭，勿挂给克莱尔。
9. `ch39 making music.md:91` 「贝克下楼去训练伊莎多拉，她自己到工作室把亚麻打成纸浆」——`:435` 分工正确，勿对调。
10. `ch39 making music.md:97` 「上一段克莱尔把女儿赶走：「去，找到你的小提琴，闲荡。」贝克也说过艺术家必须闲荡」——`:435`/`:324` 两人两处，勿合并成一句。
11. `ch39 making music.md:117-118` 词汇表 `inventive`/`improvise` 例句 `Terryl says you are very inventive, that he enjoys listening to you improvise.`——原文逐字，Terryl 拼写正确，勿改。
12. `ch39 making music.md:130` 总结「次日，她在餐桌铺开五线谱纸」——材料 `:216` “staff paper”、地点餐桌、时间次日（`:169` “Sunday, June 7, 2015”），三者皆对。
13. `ch39 making music.md:37` 里 `runaround` 的**结构**没错（贝克自比侦探小说里的女人、阿尔芭只当好玩、说了「玩得开心」——`:47`/`:53` 皆有原文），只有「跑腿」这一处译词要改；修订时**不要连带重写整段**。
