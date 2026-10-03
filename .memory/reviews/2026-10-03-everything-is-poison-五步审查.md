# Everything Is Poison（Joy McCullough）五步审查 · 缺陷清单与取证

- 审查触发：用户在本会话发起（AGENTS.md 第 10 条 ⇒ a–e 全跑，不得以「同会话局限」降档）。
- 对象：`notes/books/novels/everything-is-poison-by-joy-mccullough/`（66 件正文 md + 总览三篇）。
- 报警合计 **77**（d 步三路 65 ＋ e 步 12）⇒ 复核定档：**阻断型 65 已整改 / 提示型 7 只记不改 / 假红 5**。
- 整改 commit：b92a5bff9（批一、批二）＋ 23254673b（批三：章节 53 处 + 总览 12 处）。
- 复验：`gate.sh` EXIT=0（18 项，0 条阻断型）；`corruption_scan` FAIL 0；`check_struct_indep` 0；`check_analysis_indep` 2242 条全逐字（提示型 1：韵文公式 `There is a woman like X but not`）；`check_xref_indep` 英文证据 0 报警。
- 原始门禁输出：`.memory/raw-gates/everything-is-poison-by-joy-mccullough/`（a-gates / b-逐章归属 / c-gate全量 / d-gate整改后 / f-五步审查 a·b / g-整改批三后 ×2）。

## 一、阻断型 65 处（逐条：位置 → 缺陷 → 原文取证 → 处置）

### A 说话人 / 施动者（9）
1. ch15a:33 —「Antonio 被 Violetta 咽下半句念出」→ text/ch15:229 `"About Antonio," Carmela says`（Violetta 回应行未提该名）→ 改记 Carmela。
2. ch30:58 —「那时是 Violetta 说 "You did marry me first."」→ ch15:244-259 回合交替：Carmela 问 "Do you remember our wedding?"、Violetta 答 "What?" / "What are you talking about?"，随后叙述 `Carmela examines Violetta's face to see if she truly doesn't remember` ⇒ "You did marry me first." 与 "Never mind." **两句都是 Carmela 的**。**执行方此前判为假阳，本轮复核推翻自身旧判并改正。**
3. ch30a:72 —「San Giacomo 那句从药铺的人嘴里」→ ch34:106-118 该句由 **Sister Francesca** 说出（前句 "Of course not!" 属她，接话讽刺 "Ah. So you do sometimes meet…" 才是 Giulia）→ 改为隐修院的人，并标两位说话人。
4. ch36:13 — Carmela「在柜台上下单、收钱」→ ch36:139 报价句紧跟 `Carmela hands the very remedy to Violetta, who places it on the counter`，:142 `he digs the coins out of his pocket, sets them on the counter`＝钱由公证人自己撂下，无人收取；且与同文件 :11/:58/:60 自相矛盾 → 改为递药给 Violetta、钱由对方撂在柜台。
5. ch27:13/34/36 —「配方锁在后间、母亲才配得动」→ ch23:283 `Giulia takes hold of the locket she gave Carmela… withdraws a tiny scrap of parchment. She hands it to Carmela`；ch27:31 `Carmela pulls the key from the chain where it clinks against her mother's locket` ⇒ 配方 ch23 已交入 Carmela 手里并贴身 → 三处同改。
6. ch28:11/34 —「水果贩 Benicio」→ ch09 `Benicio the botanist… greenhouses where he grows his wares`、`Was your botanist not in?`、ch13 `the botanist has turned against them` → 改「植物贩 Benicio（原文 the botanist）」。
7. ch28:64 —「what we helped you do 全程不说破」→ 同章三行之上 `She tended the pennyroyal and rue in your abortive remedy—` 已当场点明 → 改为「明说在前，此处压成一句威胁」。
8. ch26:57 — 分析层行内英文 `"you pushed her out"` **全书查无**（push 仅 ch34 指 Giulia）→ 换原文 `she convinced Giulia to leave`。**该类字符串 check_analysis_indep 抽取不到，是工具盲区。**
9. ch09:54 —跨说话轮次拼接 `"four a week? …They'd burn all the women as witches"`（禁令 5）→ 拆回叙述并标原文无说话人标签。

### B 计数 / 形态断言（21）
ch23a:34 区名「随后八个」→ 实为七个（Campo Marzio + Regola/Colonna/Trevi/Testaccio/Sallustiano/Ludovisi/Parione）｜ch26a:53「前六行」→ 原句 2 共 10 行＝4+6｜ch26:35「Not Maria. 独立成段」→ 与后续叙述同段（ch26:7）；「四个 you will」→ 实得 3 次｜ch23:26「本章第一句台词是缺货清单」→ 第一句台词是 `"Sage?"`（:1），清单在 :22｜ch25:56「13 岁的 Giulia」→ 原文 `twelve or thirteen`（悬置点不许补死）｜ch37a:14「全诗现在时」→ `she shouldn't have seen / smacked / stole` 三处过去式｜ch32a:14「将来时后回到 even now is tugging」→ 该行在将来时段之前，收口句是 `and it occurs to her to worry`｜ch40:74「另起一段的只有三个词」→ 同段末句、四个词｜ch39:38「三对三／两次 insist／两次不答」→ tag 为 insists×1＋says×1，stalks away 与 busying 同句，第二回以 "I know." 作答｜ch39:50「回答被切成两段」→ 问句与 frowns 都在回答**之前**｜ch26a:98「三项全是过去将来时」→ `She was indispensable.` 无 would｜ch26a:115「the lady's maid 唯一一次从属称谓」→ 该词组早在第 3 块 `became lady's maid` 出现，仅带定指的 the 是首次｜ch14a:14/90「三次回环／Ponte Sisto 第三次」→ 全书仅两次｜ch19a:11/132「第一次转向男人」→ 前有 ch04a a man／ch13a a cat／ch15a a boy ⇒ 第三次非女性主体｜ch20a:13「未给出任何名字」→ `But whose? Surely not Giulia Tofana.` 三次具名｜ch22:13「两回都落在」→ 原文 `Unlike when Giulia had shown up` 恰是对照｜ch29:34「两句都以 never 起头」→ never 均在助动词之后｜ch37a:66「一行之内换两次介词」→ 两处独立诗行｜ch41:38「整段过去完成时（含 anointed）」→ anointed/led/grabbed 是一般过去时｜ch41:13「给糖杏仁」→ Carmela 只指了位置，孩子自取、Violetta 打包。

### C 跨章归属（8）
ch28:13「第 1 章往 Laura 身上泼垃圾」→ 实在 ch21 `body covered in refuse`｜ch18:24「上一章末尾」→ 该句在 ch16:293（ch19:139 复述）｜ch22:44「第一章登场时的 a single bag in hand」→ 该句在本章首行｜ch14a:58「上一章的阶级议论」→ 在本篇后段与 ch15:274｜ch18a:14「第 16 章的 The Women」→ 韵文是 16a｜ch20a:85 fighting → 原文 `as he fights for his final breaths`（分词连排兜底改限定动词）｜ch05a:34「呼应 ch04a 结尾那句」→ 在 ch04a 首节末尾｜ch13:82「黑猫第三次经过」→ 本章第四次现身（:16/:290/:314/:353）。

### D 分析层英文走形 / 省略号形态（12 项，含批一 8 处）
8 处 ASCII `...` → `…`（只动分析行，表格与原句行不动）｜ch32:12「Violetta … while giggling」→ 原文 `Carmela giggles`（词形＋归属双错）｜ch32:60 "That seems unlikely." 译成「这可不像话」＝命题反转 → 「那倒不太可能」｜ch32:34「说明她清楚刚才有观众」→ 原文随即否定 `Violetta isn't even watching her.`｜ch32:54/74 块号指针错（sheep-children 与 she startles 都不在所指块内）→ 改为按内容指｜ch27a:31 中文理解把 `but not` 的否定对象从身份挪到地点 → 改正｜ch26a:73「离开那张床」→ 离开的是 `her lady's side`｜ch26a:115「女仆亲手缝过的」→ 诗中无据，加限定｜ch37:11「喝令 Violetta」→ 受话人原文未标，不作裁决｜ch37:13「此后一直安静地做事」→ 后半章多次开口下指令｜ch40:44「同一口气」→ 两处相隔且顺序相反，夸女儿发生在错认中｜ch36:50 中文理解覆盖块外一句 → 把 `"Signora," he says with a mocking bow.` 并入原句 4。

### E 总览层事实（15）
00_概述:38「头伤不治**死于**修院」→ ch40 末句只到 `guides her through the archway`，ch41 全章无 Maria 之死（同库 00_情感节点:11 已列为留白）→ 改「未写咽气时刻」｜00_概述:37「第 23 章顶罪离铺入修院」→ ch23:232 `"I'm not going to the convent."`，收留许诺在 ch25:32、人在修院是 ch34 → 改「第 25/34 章入修院」｜00_概述:30「已判明脑内出血，无力回天」→ `I suspect…` ＋ `There's a chance it will stop on its own`｜00_概述:28「Sister Francesca 一言不发」→ 同章她有四句台词 → 改「进门一声不吭…开口也句句设墙」｜00_概述:22「把她推进火里」→ `shoved her out of his way` 后她撞入火鼎｜00_金句精选:50「一滴就够」→ ch08 量词是 `One barleycorn`，全书 drop 在 ch12｜00_金句精选:55「Giulia 念完（传单）」→ 全书无 Giulia 朗读；传单经 Carmela 细看、Maria 投火｜00_金句精选:117「全诗以问句收尾」→ 问句在 :103-127，末三行 `because this / other / has breathed her last.`｜00_金句精选:209「拿圣油」→ Flora Maria `grabbed the nearest bottle of oil`＝Melissa officinalis｜00_金句精选:48 时序（"I brought what we discussed" 在手腕一幕之前）｜00_金句精选:143「同街／同一段石板路」→ 13a 的猫是游荡于数个地点的类型｜00_金句精选:75「前一段」→ 中间隔三段｜另有批一已入库的 3 处（ch09 说话人、ch05a 指针、词表空档）。

## 二、提示型 7 处（只记不改）
ch18:66「递出小瓶」＝ch19 闪回的前指（时序可通）｜ch24:14 已在 D 类之外保留原推断｜ch23:72 第二处 "Hush, love." 原文未标说话人（已改为「按上下文当为 Giulia」）｜ch23:84 slip/exit 同词族（已改口径）｜ch26a:12 空间（已改）｜check_vocab WARN 1＝apothecary 词长≥9 启发式｜check_overview_full ⚠️ ㉑/㉔ 同句 ch6+ch15（经核为作者复述）。

## 三、假红 5 处 + 工具待办
1. `check_chapter_quotes.py` 单章模式 `nn = int(args[0])` 拒收 `chNNa` 后缀 ⇒ 后缀章只能走全目录口径。**待修工具。**
2. `check_analysis_indep.py` 抽取盲区：分析层紧跟中文的直引号英文串未被抽出 ⇒ ch26:57 凭空引语报 2223/2223 全绿。**待修工具（本轮已人判补上）。**
3. ch20a:85 threshold「第二次」、ch20a:107「will 四次」、ch23a:36「in 九行／八专名」三条报警经核 **md 正确**（子代理计数误判）。
4. ch30:58 一度被我判为假阳 ⇒ 见 A-2，反向订正。**教训：整改批里"这条像假阳"的判断，必须重读原文回合，不能沿用首轮结论。**
5. 禁令 2/5 对**分析层行内省略号形态**无机械覆盖 ⇒ 本轮靠 d 步人判，登记为工具缺口。
6. 其他实例文件（不在本任务范围，只报告）：`the-edge-of-water` 的 `ch27 iyanifa imole.md` 词表真空档位表头。

## 四、同会话审查局限（如实标注）
- 说话人层与总览中文事件断言**无机械门禁**，本轮覆盖度取决于 d/e 步人判，非全量证明；
- a/b/c 三侧重跑为机械层取证，未复核内容语义；d 步三路子代理各覆盖 20/16/12 文件，e 步覆盖总览三篇；
- 未被任何一路覆盖的文件：无（66 件按三路切分全覆盖，ch33/ch34/ch35/ch35a 三路均报 0 报警）。


---

## 批一（d 步 20 文件 / 108 引语块）

原始报告（子代理逐字输出，未改写）：

核对完毕（20/20 文件，全程只读，未改任何文件、未执行 git）。目录：`/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/everything-is-poison-by-joy-mccullough/`

---

**[档位建议: 阻断型] ch15a the groom.md:33**
md 侧：`**读者视角提示：**Antonio 在编号章第 15 章是对话里被 Violetta 咽下半句念出的名字；本篇先声明"但不是他"，合唱之声照例把"不是你认识的那个人"放在第三行。`
原文侧：`text/ch15_chapter_15.txt:229`「"About Antonio," **Carmela says.** "And your…" She waves vaguely in Violetta's direction as she retrieves the broom.」（第 15 章 Chapter 15；全章 Antonio 仅此一处；Violetta 的回应行 231 未提此名）
问题：第 2 类说话人归错——把 Carmela 的台词记成 Violetta"咽下半句念出"（反例 D 同型）。
建议改法：改为"第 15 章里是 Carmela 在对话中说出这个名字，Violetta 只回应未提"。
置信：高

**[档位建议: 阻断型] ch18 carmela starts a fire from scratch.md:24**
md 侧：`…而上一章末尾她说过"我们互相照应"，本章是这句话发酵之后的第一个安静夜晚。`
原文侧：`text/ch16_chapter_16.txt:293`（该章末行）「"Tonight," Carmela says, "I'm La Tofana. We take care of each other. It's what we're here for."」第 16 章 Chapter 16；第 17 章 Chapter 17 全章无此句（grep 全书仅 ch06:16、ch16:293、ch19:139 三处）
问题：第 6 类跨章指针错——"上一章"应为隔两章的第 16 章。
建议改法：把"上一章末尾"改为"第 16 章末尾（该句在第 19 章闪回中被复述）"。
置信：高

**[档位建议: 阻断型] ch19a the priest.md:11（同文件 :132 同错）**
md 侧：`- **一句话概括**：韵文插叙第一次离开女声合唱，转向一个男人：…` / `:132` `诗用与前两场《The Women》同一副"像……但不是"的骨架，第一次把镜头交给一个男人：…`
原文侧：`text/ch04a_the_widower.txt:1,4`「The Widower / There is a man / like Violetta's father」；`text/ch15a_the_groom.txt:1,4`「The Groom / There is a boy / like Antonio」（均早于 ch19a）
问题：第 5 类事实断言错——"第一次"被本篇之前两首男性主体韵文推翻。
建议改法：改为"第一次以男性神职者为主体"或"继 The Widower、The Groom 之后再次转向男人"。
置信：高

**[档位建议: 阻断型] ch20a the loiterer.md:85**
md 侧：`而死亡这一段被写成一串现在分词的连排（stumbling / crashing / retching and clutching / fighting），像把现场按帧放给读者看。`
原文侧：`text/ch20a_the_loiterer.txt:139`「as he **fights** for his final breaths.」（第 20a 章 The Loiterer；全诗无 "fighting"；同 md 关键词行 83 自己写作 `fights for his final breaths`）
问题：第 4 类分析层英文走形——原文是限定动词 fights，md 造出分词 fighting 以凑"现在分词连排"（正是反例 B 同型）。
建议改法：末项改为 "fights for his final breaths"，并说明此处由分词转为限定动词收束。
置信：高

**[档位建议: 阻断型] ch14 horror in the walls.md:24**
md 侧：`**为什么这样写：**开篇像一张户型图的沿革说明：同一间小公寓随年份轮住过 Maria 与丈夫、Maria 与 Giulia、Giulia 与新婚丈夫、Maria 与 Laura——`
原文侧：`text/ch14_chapter_14.txt:1,3,5`「The apartment Maria and Laura share is right around the corner from the apothecary. When Maria's husband died, she and Giulia lived there until Giulia married. **When Giulia and her new husband moved into the apartment above the apothecary**, Maria's niece Laura came to stay with her. … It is above the butcher shop」（第 14 章 Chapter 14）
问题：第 5 类事实断言错（两间不同公寓被并成"同一间"），且与同文件 :20 的正确译文"药铺上方的公寓"自相矛盾。
建议改法：删去"Giulia 与新婚丈夫"这一格，或注明他们住的是药铺上方、拐角外那间才是 Maria/Laura 的。
置信：高

**[档位建议: 阻断型] ch14a the traveler.md:90**
md 侧：`…桥名 Ponte Sisto 第三次出现，形成环形。`
原文侧：`text/ch14a_the_traveler.txt:13,16,184`「crossing the Tiber / at the Ponte Sisto / the Ponte Sisto」（第 14a 章 The Traveler；全书 grep "Ponte Sisto" 仅此两处）
问题：第 5 类计数断言错——本篇内（也是全书内）只有两次。
建议改法：改为"桥名首尾两次出现，形成环形"。
置信：高

**[档位建议: 阻断型] ch21 laura comes home covered in refuse.md:64**
md 侧：`under no obligation 是账簿与契约的语言，出自刚刚还喊着 You're family! 的那张嘴，这份温差就是本章的伤口。`
原文侧：`text/ch21_chapter_21.txt:128`「"Laura." Giulia takes her hands. "I hope you know you're under no obligation to keep working in the shop."」→ `:143`「"Of course," Giulia says, in her warmest voice. "You're family!"」（第 21 章 Chapter 21；全章 family 仅此一处，在 128 之后 15 行）
问题：第 5 类次序断言错——两句都出自 Giulia，但"You're family!"在后，不是"刚刚还喊过"。
建议改法：改为"说过 'under no obligation' 的那张嘴，十五行后才补上一句 'You're family!'"。
置信：高

**[档位建议: 阻断型] ch17a the infant.md:14**
md 侧：`- **叙事手法**：全诗用连续的现在时贴住产程；断行是收缩的刀口；中段三个 how 从句连排；末段以行首 and 的连缀堆到第一声啼哭，收在一个否定短句上。`
原文侧：`text/ch17a_the_infant.txt:46`「she was enveloped」、`:70`「turned on her」、`:133`「and then finally she emerged」（过去时）、`:121`「she will learn」（将来时）（第 17a 章 The Infant；md 自己在 :52、:72 就引用了 was enveloped / will learn）
问题：第 5 类技法断言与原文不符——产程关键处恰恰切到过去时。
建议改法：改为"以现在时为底，在'被裹住/转身/娩出'三处切进过去时"。
置信：中

**[档位建议: 提示型] ch14a the traveler.md:58**
md 侧：`transaction 用商业词称身体交易，冷度与上一章"她们叫卖、顾客买"的阶级议论同一口径。`
原文侧：该议论在本篇自身 `text/ch14a_the_traveler.txt:52,55,59-70`「from the ones they call courtesans / who flaunt their wares in church / The high-priced girls / offer charming conversation / … but that's not what the clients want, really.」；`text/ch14_chapter_14.txt`（第 14 章 Chapter 14，全章 35 行）无 courtesan/conversation/clients 任何一处；下一句同类议论在 `text/ch15_chapter_15.txt:274`「"Or the courtesans of Venice,"」
问题：第 6 类跨章指针错——所指内容不在"上一章"，而在本篇后半与下一章。
建议改法：把"上一章"改为"本篇后段（原句 X）"或"第 15 章 Carmela 的威尼斯妓女一句"。
置信：中

**[档位建议: 提示型] ch18a the women part 2.md:14**
md 侧：`- **叙事手法**：与第 16 章的《The Women》同用"There is a woman…but not"的开句模板（见第 16 章）；…`
原文侧：`text/ch16a_the_women.txt:1,4`「The Women / There is a woman」（第 16a 章 The Women）；`text/ch16_chapter_26…` 即 `text/ch16_chapter_16.txt`（第 16 章 Chapter 16）grep "There is a woman" 零命中
问题：第 6 类跨章指针错——a 类韵文与编号章混标（同文件 :14 后半"上一篇用一个'又一个'式短句"指的确实是 16a，标签却写 16）。
建议改法：两处"第 16 章"改为"第 16a 章《The Women》"。
置信：中

**[档位建议: 提示型] ch20a the loiterer.md:13**
md 侧：`诗中还顺手完成了一次对药铺四个女人的点名——the older one / the quiet one / the young one——按年龄与性情标注，未给出任何名字。`
原文侧：`text/ch20a_the_loiterer.txt:151,154,175,178`「But whose? **Surely not Giulia Tofana.** / Perhaps it was the older one. / The quiet one, then. / Or even the young one.」（第 20a 章 The Loiterer；另有 :73「until Giulia Tofana's teas and tinctures」、:211「she met Giulia Tofana」）
问题：第 5 类事实断言错——点名实为"三个无名称谓 + 一个直接具名的 Giulia Tofana"，"未给出任何名字"与本篇三次具名冲突。
建议改法：改为"三个女人只按年龄性情标注、第四位则直接点名 Giulia Tofana"。
置信：中

**[档位建议: 提示型] ch22 laura shows up barefoot.md:13**
md 侧：`- **人物弧线**：Maria 这一章立起"收人的人"的谱系：Giulia 先来，Laura 后至，两回都落在一句 "no man of the house to consult" 的门风里；…`
原文侧：`text/ch22_chapter_22.txt:1`「**Unlike when Giulia had shown up**, there was no man of the house to consult.」（第 22 章 Laura Shows Up Barefoot；全书 grep "man of the house" 仅此一处）
问题：第 5/1 类——该句原文正是用 "Unlike" 把两回**对立**起来（Giulia 那回有男人可商量），md 说"两回都落在"同一门风里，且与同文件 :24 的正确解释自相矛盾。
建议改法：改为"两回被同一句标准对照着量：Giulia 那回有男人可问，Laura 这回没有"。
置信：中

**[档位建议: 提示型] ch22 laura shows up barefoot.md:44**
md 侧：`…她全部的财产一抱就起，与第一章登场时的 "a single bag in hand" 严丝合缝：几年过去，她添置的家当约等于零。`
原文侧：`text/ch22_chapter_22.txt:1`「Laura showed up on Maria's doorstep when she was fourteen, barefoot, **a single bag in hand** and not a word on her lips.」（第 22 章；全书 grep "single bag" 仅此一处，第 1 章 Chapter 1 无此句，ch01 的 Laura 只在 :10「silent Laura moves like a ghost」）
问题：第 6 类跨章指针错——所引句子在本章首块（原句 1），"第一章"应作"本章开场"。
建议改法：改为"与本章开场那句 'a single bag in hand' 严丝合缝"。
置信：中

**[档位建议: 提示型] ch13 carmela hides the arsenic.md:82**
md 侧：`作者只让 black tail 露一截——这是本章黑猫第三次经过，每次都在 Carmela 需要"别的路径"的时刻。`
原文侧：`text/ch13_chapter_13.txt:16`「nearly trips over a black cat darting across her path」、`:290`「A black cat crosses her path」、`:314`「The cat is underfoot again, strutting through the church grounds」、`:353`「"My cat!" … catching a glimpse of black tail rounding the corner.」（第 13 章 Chapter 13）
问题：第 5 类计数口径不稳——按同文件导航 :14 自列的四次（市集绊脚/街口穿路/院子领路/结尾"我的猫！"），结尾这次是第四次；只有把 :314 排除在"经过"外才成立。
建议改法：改为"第四次现身"，或明确"第三次擦身而过（院子那次是她跟着猫）"。
置信：低

**[档位建议: 提示型] ch18 carmela starts a fire from scratch.md:66**
md 侧：`seen and done and learned 三连用头韵式的节奏收拢她这几天的全部经历（接生、递出小瓶、听配方）。`
原文侧：`text/ch18_chapter_18.txt` 全章 32 行无 bottle/vial；递瓶场景首次落页在 `text/ch19_chapter_19.txt:199-211`「Carmela retrieved the vial. "You have to listen carefully," she said. …」（第 19 章 Chapter 19 闪回）；"听配方"有 `text/ch12_chapter_12.txt:130-154,280` 支撑；接生有第 17 章支撑
问题：第 5 类——"递出小瓶"在 ch18 及更早 text/ 中无文本支撑，属对后章闪回的前指（时序可通，故只作提示）。
建议改法：加注"此事要到第 19 章闪回才交代"。
置信：低

**[档位建议: 提示型] ch22 laura shows up barefoot.md:12**
md 侧：`让损失在读者手里自己称出重量。全章的现在时只属于最后一句。`
原文侧：`text/ch22_chapter_22.txt:55`「But now they **would have to learn** to go on without her.」（第 22 章；全章叙述动词逐一检过均为过去/过去完成，末句是 would+不定式，非现在时）
问题：第 5 类技法表述不准——末句的"现在"由 now 承担，动词形式仍是 would；把"现在时"当语法术语会误导学习者。
建议改法：改为"全章只有最后一句被 'now' 拉回当下"。
置信：低

---

按 brief 不报清单核实后**排除**的项（列此以证已查）：全部 108 个引语块逐字命中 text/，未发现反例 A（伪造/改写引语）、反例 C（主语替换）与反例 E（不相邻自然段拼接）；ch22 原句 6 的两段（text/ch22:52 与 :55）为相邻自然段，且 md:72 用「／」、md:76 用"同块的末段"明示分段；ch16a「and another 第 51 次才落句号」、ch18a「and still 三次」与方位 northwest/west/northeast、ch20a「教名 Claudio 仅见于本韵文」计数均实测正确；ch15:58「第 13 章它已在她的路上两次出现」按"擦身而过"口径（16、290）成立，与 ch13:82 一并不报；ch22:78 指向第 23 章的 `Without Laura, their supply of powdered blood will not be enough`（ch23:25）与 ch22:12"第 21 章 Laura 一身垃圾、夺门而逃"（ch21 末段 "she runs from the room"）均成立；ch21:76→第 22 章"十四岁赤脚出现在 Maria 门口"成立；ch22 词汇表 21 条例句全部逐字在 text/ch22 内；各文件"原文未写明/不作裁决"的悬置处一律未报。

核对文件数 20 / 引语块数 108 / 报警数 16（高 7 · 中 6 · 低 3）


---

## 批二（d 步 16 文件 / 88 引语块）

原始报告（子代理逐字输出，未改写）：

核对完成（16 文件 / 88 引语块）。以下为 d 步语义二审报告，未修改任何文件、未执行 git 命令。

---

**[阻断型] ch23a the women part 3.md:34**（23a. The Women, Part 3）
md 侧：「起头是药铺所在的 Campo Marzio（本书编号章与另两首插叙反复以此为原点），随后八个区名一路平铺，最后用 in every rione 把点名收尾」
原文侧：「in Campo Marzio / in Regola / in Colonna / in Trevi / in Testaccio / in Sallustiano / in Ludovisi / in Parione / in every rione」（23a. The Women, Part 3）——Campo Marzio 之后只有 7 个专名
问题：⑤「多少个」计数错，且与同文件 md:36「in 起头的行有九行，其中八个是专名」自相矛盾（引反例 A）
建议改法：「随后七个区名一路平铺」
置信：高

**[阻断型] ch26a the brokenhearted.md:53**（26a. The Brokenhearted）
md 侧：「前六行的"清算愿望"与后六行的"家庭供养"被诗放在同一块里」
原文侧：本块（md:36–45）＝「weeping so hard / with any luck / her tears will flood the Tiber / and carry them all away. / She has spent her life in service / and though the work is difficult / she is proud of the money she makes / that supports her grandmother / so the old woman no longer / has to clean up after others.」共 10 行＝4＋6（The Brokenhearted）
问题：⑤计数错；同文件 md:51 自己写「随后六行」，前半只可能是四行（引反例 A）
建议改法：「前四行的"清算愿望"与后六行的"家庭供养"」
置信：高

**[阻断型] ch26 carmela confronts maria.md:57**（26. Carmela Confronts Maria）
md 侧：「上一段 Maria 的 "I feel it too"（我懂）在这里被"you pushed her out"（你劝她走）抵消」
原文侧：「Maria cannot claim to know how she feels, because Maria encouraged Giulia to go. She agreed with Father Piero, she convinced Giulia to leave. She has no right.」；全书 push 仅 ch34「Giulia nods. She doesn't push her point.」（指 Giulia，非 Maria）
问题：④分析层行内英文为自造引语，原文无 "you pushed her out"（引反例 B）
建议改法：改用原文「she convinced Giulia to leave」
置信：高

**[阻断型] ch23 giulia leaves the shop forever.md:26**（23. Giulia Leaves the Shop Forever）
md 侧：「**为什么这样写：**本章的第一句台词是一份缺货清单：三个名词，没有动词……回看开场：草药盘点还是平稳的一问一答（"Sage?" "Fine."）」
原文侧：「“Sage?” Carmela says. / “Fine,” Maria reports. / “Chamomile?” / “Fine.”」，三样偏门货在第 22 行「“Mandrake, after the Fontina order. Spanish fly. Sanguis pulvis.”」
问题：⑤「第一句」ordinal 断言不成立（本章第一句台词是 "Sage?"），同块内部自相矛盾（引反例 A）
建议改法：「本章第一段偏门货报单」
置信：高

**[阻断型] ch23 giulia leaves the shop forever.md:13**（同上章）
md 侧：「她拒绝 Carmela 顶罪、设计让 Maria 作"定罪证人"、把配方缝在饰物里——每一步都是把"护住店与人"再往前推一寸」
原文侧：「"Yes, you do." Giulia takes hold of the locket she gave Carmela when she first began in the shop. She opens it and withdraws a tiny scrap of parchment. She hands it to Carmela」；同文件 md:84 作「护身坠饰里 "a tiny scrap of parchment"」
问题：⑤「缝在」无原文依据（羊皮纸是抽出、非缝入），并与同文件 md:84 冲突（引反例 A）
建议改法：「把配方（一小卷羊皮纸）收在坠饰里交给她」
置信：高

**[阻断型] ch25 giulia remembers saving the novitiate.md:56**（25. Giulia Remembers Saving the Novitiate）
md 侧：「破折号前的"白色光环"（haloed in white）被破折号后的"血色覆盖"（covered in blood）拆穿；13 岁的 Giulia 从此知道」
原文侧：「She'd been twelve or thirteen, a year or so before her father's death—and her mother's—and she'd begun to help her mother in the apothecary after hours.」；同文件 md:14 作「十二三岁的初见」
问题：⑤替作者把悬置年龄点补死，且与同文件自述矛盾（brief 明令「不许替作者把悬置点补死」；引反例 A）
建议改法：「十二三岁的 Giulia 从此知道」
置信：高

**[阻断型] ch26 carmela confronts maria.md:35**（26. Carmela Confronts Maria）
md 侧：「一句 "Not Maria." 独立成段——上一段的对照（Laura 干活，Maria 不）在这里被压缩成**两个字的判决**」
原文侧：「Not Maria. She marches to Carmela's bed—her own bed—and says, “Tomorrow you will get up early…”」（同段句首，非独立段）
问题：⑤关于原文排句结构的断言不成立（引反例 A）
建议改法：「以 "Not Maria." 劈头（与后续叙述同段）」
置信：高

**[阻断型] ch26 carmela confronts maria.md:35**（同上章、同段）
md 侧：「四个 "you will" 的祈使句排在一起，把命令写成日程表：get up early / stoke the fire / boil water / prepare our breakfast / go to the shop and open it」
原文侧：「Tomorrow you will get up early, you will stoke the fire and boil water, and prepare our breakfast. Then you will go to the shop and open it while Laura and I take our time getting there.」（you will 实得 3 次，所列条目 5 项）
问题：⑤计数与所举条目两者皆不合（引反例 A）
建议改法：「三个 you will、五条日程」
置信：高

**[阻断型] ch27 tonight is for saving a life.md:36（并见 :34、:13）**（27. Tonight Is for Saving a Life）
md 侧：「注意这里的 key 开的是门；that recipe 不是同一物，而是留在后间、母亲才配得动的东西——第 1 章早写明她从没被允许绕过那道柜台。」／:34「那副出名的配方（母亲才碰、锁在后间的东西）今夜用不上」
原文侧：ch23「Giulia takes hold of the locket… She opens it and withdraws a tiny scrap of parchment. She hands it to Carmela」＋「There in a cramped script are the quantities required to make Acqua Tofana」；本块所引 ch27 原句自写「Carmela pulls the key from the chain where it clinks against her mother's locket」
问题：⑤＋⑥配方在第 23 章已交入 Carmela 手里、就在她颈间坠饰内，"留在后间、母亲才配得动"两处皆失（"第 1 章没被允许绕过柜台"一半成立，见 ch01「She has never ventured back behind the counter, to the workshop」）（引反例 A）
建议改法：改为「配方此刻就贴身在她母亲的坠饰里，她今夜不打开它」
置信：高

**[阻断型] ch27 tonight is for saving a life.md:56**（同上章）
md 侧：「留意 "as though this makes them the same" 里的 them——是"客人和卖身女"，还是"药铺主和码头人"？作者不替 Carmela 说破，只把她的不安藏进那两句 as though 的重复里。」
原文侧：「“How old are you?” she asks. … / “Fifteen,” she says, voice barely audible. / “I’m sixteen,” Carmela says, as though this makes them the same.」
问题：①指代被拆成两个皆错的选项，先行词就在紧邻两行（两个女孩），不属 brief 的"原文含糊"豁免（引反例 A）
建议改法：them＝十五岁的 Eleonora 与十六岁的 Carmela
置信：高

**[阻断型] ch28 carmela is not la tofana.md:34（另见 :11）**（28. Carmela Is Not La Tofana）
md 侧：「善举的触发点却是她们如今"有了可怪的主、不必再担心"；…先前避之不及的水果贩 Benicio 反而 come around」／:11「反倒让街坊（水果贩 Benicio）回过头来帮她们」
原文侧：ch09「Benicio the botanist has an extremely modest property on the eastern edge of Campo Marzio, with a few greenhouses where he grows his wares.」＋「“Was your botanist not in?”」＋ch13「as though it is her fault the botanist has turned against them」
问题：⑤＋⑥职业身份错（botanist／温室种苗人，非水果贩）（引反例 A）
建议改法：「草药师／植物贩 Benicio（the botanist）」
置信：高

**[阻断型] ch28 carmela is not la tofana.md:64**（同上章）
md 侧：「what we helped you do 全程不说破，把最重的信息留给读者自己去回填。」
原文侧：同章三行之上「“She tended the pennyroyal and rue in your abortive remedy—”」；另 ch04「“Do you want our help to end this pregnancy?”」
问题：⑤＋⑥"不说破"被同章同场台词直接推翻（引反例 A）
建议改法：「明说在前（pennyroyal and rue／abortive remedy），此处把它压成一句威胁」
置信：高

**[阻断型] ch28 carmela is not la tofana.md:54**（同上章）
md 侧：「用的全然是母亲那套动作语汇——glide 这个词在本书几乎专属于 Giulia（前文她应付 Stiatessi 时也"glides as her mother would have"）」
原文侧：全书 glide 普查：ch01「She glides up to the counter and engages Signora Tofana as though they are equals…」（Violetta）、ch22「Giulia glided out to the front」（唯一一次）、ch28「She glides as her mother would have…」「…hold her head high and glide through the apothecary」（Carmela×2）、ch33「She glides out to make her best effort」（Carmela）
问题：⑤唯一性断言反了（Giulia 1 次、Carmela 3 次），且所引证据句本身正是"Carmela 模仿母亲"（引反例 A）
建议改法：「glide 属于母亲的姿态；本书里用得最多的反而是 Carmela，且每次都带 as her mother would have」
置信：高

**[阻断型] ch28 carmela is not la tofana.md:13**（同上章）
md 侧：「Violetta 则从第 1 章那个自信地来买爱情药剂、又往 Laura 身上泼垃圾的姑娘，第一次显出恐惧、愧疚与求饶」
原文侧：泼垃圾在第 21 章：「But it's Laura. Or a shadow Laura, face agonized, body covered in refuse.」「“That's Violetta's apartment.”」；第 1 章只有「She glides up to the counter…」
问题：⑥跨章归属错（把 21 章事件记进 1 章）；同库 ch31 md:40 与 ch29 md 的写法才是对的（引反例 A）
建议改法：「第 1 章来买爱情药剂、第 21 章往 Laura 身上泼垃圾」
置信：高

**[阻断型] ch30 carmela makes violetta laugh.md:58**（30. Carmela Makes Violetta Laugh）
md 侧：「这块的锋利处在于**它把第 15 章一句玩笑原样收回**：那时是 Violetta 说 "You did marry me first."，Carmela 回答的是 "Never mind."」
原文侧：ch15「“Do you remember our wedding?” / “What?” / “I mean, if anyone should be upset, it's me. You did marry me first.” / “What are you talking about?” / Carmela examines Violetta's face to see if she truly doesn't remember… / “Never mind.” Carmela unclasps the hands of the carefree children in her memory.」
问题：②两句都出自 Carmela，md 把说话人对调（引反例 C）
建议改法：改为「那时 "You did marry me first." 与 "Never mind." 都是 Carmela 说的」
置信：高

**[阻断型] ch32 violetta grinds lemon balm.md:11**（32. Violetta Grinds Lemon Balm）
md 侧：「随后两人在后间一起研磨柠檬香蜂草，Carmela 第一次被 Violetta 的幽默逗笑，气氛由对抗转向松动。」
原文侧：「“You can't be back here.” / “Oh.” Violetta's brow wrinkles. … / “Come on.” Carmela hustles her out to the front.」；同研磨在前厅柜台：「Carmela pushes the mortar across the counter to Violetta. “Here, you try.”」后间里只有 Carmela 一人：「Carmela moves to the back and sits at Maria's worktable. …Carmela plucks the leaves from the stems and drops them into her mortar.」
问题：⑤空间事实错，且抹掉本章「后间门槛」这一关键节拍（幽默逗笑亦发生在被赶出后间之后）（引反例 A）
建议改法：「Carmela 独自在后间起手，把 Violetta 赶到前厅后两人在柜台旁一起研磨」
置信：高

**[提示型] ch23 giulia leaves the shop forever.md:72**（23. Giulia Leaves the Shop Forever）
md 侧：「这个短语本章出现两次，都是对 Carmela 的喝止…；第二处明写是 Giulia（紧接着 "I need to think."，前一句正是 Carmela 抓着她手臂求她别顶罪）」
原文侧：「Carmela rushes across the room and grabs Giulia's arm. “Mother, it was me. There's no reason for you to—” / “Hush, love. I need to think.” / Helpless, Carmela turns to Maria.」——两处 "Hush, love." 均无说话人标签
问题：②把按上下文的推断写成"明写"（引反例 D）
建议改法：「第二处原文未标说话人，按上下文当为 Giulia」
置信：中

**[提示型] ch23 giulia leaves the shop forever.md:84**（同上章）
md 侧：「后门在句尾才打开（slips out the back 的 slip 与前文神父 exits out the back door 同词族，全章"离开"一律走这扇门）」
原文侧：「Without another word, another glance, Father Piero pushes past them through the archway and exits out the back door.」／「…as her mother slips out the back」
问题：⑤语言事实错（slip 与 exit 不同词族，只共享 back）（引反例 B）
建议改法：「同一个 back，动词从 exit 换成 slip」
置信：中

**[提示型] ch24 carmela cannot muster the will.md:14**（24. Carmela Cannot Muster the Will）
md 侧：「关键信息全部经 Carmela **装睡偷听**而来（行刑日期、**母亲未死**）」
原文侧：「Which won't be much longer. Her execution date has been set, according to the hushed conversations Carmela has heard when she's lying in bed, pretending to be asleep.」（仅行刑日期挂在偷听）；「Maria begins to lose patience. …But Giulia isn't dead, at least.」（叙述／自由间接）
问题：⑤「全部」＋把叙述信息算作偷听（引反例 D）
建议改法：删去"母亲未死"或分标来源
置信：中

**[提示型] ch26a the brokenhearted.md:12**（26a. The Brokenhearted）
md 侧：「紧接第 26 章 Carmela 扑在母亲的床上抽泣之后——同一栋建筑东北方几扇门内，另一个女子在另一张床上哭。」
原文侧：「sprawled on her bed / in the servants' quarters / of the finest home / in Campo Marzio, / to the northeast of the apothecary / just a few doors down from the notary's」；同文件 md:11 作「离药铺几段路、离公证人几扇门」、md:28 作「就在药铺东北边、离公证人那处只差几扇门」
问题：⑤空间错（仆人间在另一座宅子里，非"同一栋建筑"），与同文件两处自述冲突（引反例 A）
建议改法：「药铺东北边、公证人宅子旁几扇门的另一座大宅里」
置信：中

**[提示型] ch26a the brokenhearted.md:73**（同上章）
md 侧：「末两行 "each night / reluctantly." 把副词 reluctantly（不舍地）单独抽出来，让整块收束在**回家**这个动作上——**她每天夜里都不情愿地离开那张床**。」
原文侧：「to cherish laughter so delicate / she replayed it over and over in her mind / long after she'd left her lady's side / each night / reluctantly.」
问题：①离开的是"小姐身边"，不是床；诗里未写她回家（引反例 A）
建议改法：「每天夜里离开小姐身边时都不情愿」
置信：中

**[提示型] ch26a the brokenhearted.md:98**（同上章）
md 侧：「请留意这一块的**时态**——She was indispensable / would never know / would not need 全部是**过去将来时**（would）」
原文侧：「She was indispensable.」（一般过去时，无 would）；「for her lady's husband would never / know her the way she did.」「Her lady would not need him」
问题：⑤三项并列的首项不含 would（引反例 A）
建议改法：把 She was indispensable 单列为过去时
置信：中

**[提示型] ch26a the brokenhearted.md:115**（同上章）
md 侧：「而它选的意象是**丝袜上崩开的缝**：这不是抽象的破裂，是**这位女仆亲手缝过的、这位小姐的、最贵的那一双**上的一次崩线」
原文侧：「But then it all came apart / like the seam on her lady's finest stockings」；诗内唯一手艺依据是「to fasten and unfasten buttons on creamy skin」
问题：⑤"亲手缝过"无原文依据，被写成明写（引反例 A）
建议改法：加"诗中未写明，只写她日夜扣解她的纽扣"限定
置信：中

**[提示型] ch27a the mother.md:31**（27a. The Mother）
md 侧（中文理解，所引块为「There is a woman / like Eleonora's mother / but not / in her home by the docks / to the northwest of the apothecary…」）：「有一个女人，像 Eleonora 的母亲，却又不完全是；不在码头边她的那个家里——药铺西北方向…」
原文侧：「in her home by the docks / to the northwest of the apothecary」＋全诗发生在此处：「until she hears her key in the lock.」「So far / her children have returned / like her daughter does now / key in the lock」；同文件 md:35 的解释正确（「用 but not 把身份撤回」）
问题：①＋⑤把 but not 的否定对象从身份挪到地点，得出与本诗相反的结论（引反例 A）
建议改法：「像 Eleonora 的母亲，可又不是她——她就在码头边自己的家里」
置信：中

**[提示型] ch29 violetta saves carmela at the docks.md:34**（29. Violetta Saves Carmela at the Docks）
md 侧：「两句都以 never 起头，其中 With any man 是只有三个词的独立短句」
原文侧：「She has never walked like this, side by side, with a young man down a city street. With any man. Another person has never shielded her from harm, except Giulia, in her way.」
问题：⑤形式断言不成立（两句的 never 都在助动词之后，非句首）（引反例 A）
建议改法：「两句都以 never 为轴」
置信：中

**[提示型] ch29 violetta saves carmela at the docks.md:46**（同上章）
md 侧（本节＝原句 3，md:38 引「He boxes her in against the wall, muscled arms caging her, making her the wild animal.」）：「这一句她自己成了被"方式"对待的物件：caging、making、pressing 全施加在她身上，她没有动词，只承受。」
原文侧：本块只有 caging / making；pressing 在下一段：「He presses the length of his body against hers…」
问题：④行内英文把未引的下一段词形并入本块清单（引反例 E）
建议改法：注明 pressing 出自下一段
置信：中

**[提示型] ch30a the laughing girl.md:72**（30a. The Laughing Girl）
md 侧：「这座医院在后文再次被提到，而且是从**药铺的人**嘴里（第 34 章 "We have a ward of pox patients we care for, those whose cases even San Giacomo of the Incurables will not take."）」
原文侧：引语逐字在 ch34 L109，但说话人是 Sister Francesca（上文 L106「Sister Francesca drops her spatula with a clatter. “Of course not!”」，下文 L112「“Ah. So you do sometimes meet the needs of your community.”」＝Giulia，L115「“Sometimes? Always.”」，L118「Giulia nods. She doesn't push her point.」）；全书 San Giacomo 仅两处（30a L13、ch34 L109）
问题：②＋⑥说话人归属错（引反例 C）
建议改法：「从隐修院药草间的 Sister Francesca 嘴里；接话讽刺的是 Giulia」
置信：中

**[提示型] ch32 violetta grinds lemon balm.md:12**（32. Violetta Grinds Lemon Balm）
md 侧：「后段因 Violetta 一句关于继母的玩笑 while giggling、又因她把手凑到鼻下端详香蜂草的气味，Carmela 出现了本章唯一的柔软」
原文侧：「“Oh, she'd immediately succumb to the vapors.”（无笑的动作标签）／Carmela giggles, then berates herself for rewarding Violetta's attempt at humor.」；本章无 giggling，"while giggling" 全书无
问题：④行内英文词形走形（原形是 giggles），且就近修饰语把笑记到 Violetta 名下（引反例 B／C）
建议改法：删 while giggling 或写「Carmela giggles」
置信：中

**[提示型] ch32 violetta grinds lemon balm.md:60（原句 5 中文理解；引语见 md:58）**（同上章）
md 侧：「Carmela 咯咯笑了一声…可她仍忍不住接话："这可不像话。所谓『子宫游荡之气』是源于忧郁的子宫。可你继母成天怀着孕。"」（所引原句含 "That seems unlikely."）
原文侧：「Still, she can't help but respond, “That seems unlikely. Vapors arise from a melancholy uterus. But your stepmother is constantly pregnant.”」
问题：①该句的命题是"不可能"，中译成"不像话"（道德谴责）后与紧随的理由句及同块 md:64 的解释相互抵消（非译风选择，属命题反转）（引反例 A）
建议改法：「那倒不太可能」
置信：中

**[提示型] ch32 violetta grinds lemon balm.md:34（原句 2 为什么这样写）**（同上章）
md 侧：「末句 without an audience（没有观众）反过来说明她清楚刚才有观众——擦泪要背过身，正是她不肯在人前示弱。」
原文侧：「Violetta isn't even watching her. Or at least, she isn't being obvious about it.」（紧随"without an audience"之后的一段）
问题：①／⑤分析断言"刚才有观众"，原文当场予以否定（引反例 A）
建议改法：改写成"她以为有观众，原文偏说没有"这层错位
置信：中

**[提示型] ch32 violetta grinds lemon balm.md:54 与 :74（块间指针）**（同上章）
md 侧：:54「这句和第一块呼应：当年孩子们「doing whatever Violetta declared」（第 2 章里发号施令的是她）」；:74「That's lovely 极短，却正是对上一块 she startles 那种受惊的温柔回应」
原文侧：「Carmela remembers all the sheep-children doing whatever Violetta declared, while Carmela's suggestions got ignored.」在 text L58（原句 4 与原句 5 之间）；「She startles at Violetta's appearance in the back room.」在 text L70（亦不在原句 5＝text L97 之内）；原句 1＝text L1（Acqua Tofana 一段）不含上述二者
问题：①分析指向错误的引语块（两处块号标签与实际位置不合；引语逐字均在本章）（引反例 A）
建议改法：:54 改指"本章稍后的 sheep-children 一句"；:74 改指"两块之前"
置信：中

**[提示型·低置信] ch26a the brokenhearted.md:115**（26a. The Brokenhearted）
md 侧：「"And so the lady's maid sobs" 里 "the lady's maid" 是全诗唯一一次以**从属称谓**指她（此前一直是 "this young woman" / "she" / "this maid"）」
原文侧：「The day this young woman / became lady's maid / to the daughter of the house」（同词组早于崩溃处出现）；「this maid accompanied her,」「this maid celebrated.」
问题：⑤"唯一一次／此前一直是…"的分布断言不严（带定指的 the lady's maid 确为一次，但同词组已先用过）（引反例 A）
建议改法：限定为"唯一一次以 the lady's maid 这一带定指称谓指她"
置信：低

---

汇总：`核对文件数 16 / 引语块数 88 / 报警数 32（高 16·中 15·低 1）`

补充说明（不构成报警）：
- 88 个引语块的英文原文全部逐字命中配对 `text/` 件（唯一例外即第 3 条自造引语 "you pushed her out"）。全部缺陷集中在分析层与导航层，无一处是引语抄错。
- ch22a / ch29a 两文件 0 报警；ch29a 的计数类断言（三个句号、"He has earned it." 四词）、ch21a 方位引用、ch30a 的病名/词频计数、ch23a「九行 in、八个专名」、ch31 全部跨章引用（ch07「Violetta's mother had died.」及其次句、ch08 的 Mass 句、ch21 的 refuse 句、ch28「She is La Tofana now.」、ch30「Your mother wouldn't—」、ch32 首段）、ch32 词汇表 21 条例句，均逐条复核通过。
- 已按 brief 排除的候选（避免假阳）：ch27「没向 Violetta 收钱」与 ch01 的书内矛盾、韵文 `like X but not` 的"唯一明喻"计数、`Not since…` 大小写、`box her in` 原形引用、ch29a/ch26a 语气标签类描述。


---

## 批三（d 步 12 文件 / 66 引语块）

原始报告（子代理逐字输出，未改写）：

核对完成（只读，未改动任何文件，未执行 git）。66 个引语块逐字比对全部命中所属章的 `text/`，且多段引语块都是**相邻自然段**（无反例 E 跨段拼接）；下列报警全部落在导航/分析层。ch33、ch34、ch35、ch35a 未发现可报问题（其跨章引用逐条核过：ch01/ch08/ch17/ch21a/ch28 等均属实）。

```
[阻断型] ch36 violetta sells the notary a remedy.md:13
md 侧：「Carmela 的两处变化更细：她替 Violetta 挡公证人（Her stepmother sent her），也在 Violetta 面前承认自己不知道（I don’t.），最后在柜台上下单、收钱。」（同文件 11 行概括作「Violetta 反手把"治月事剧痛的神药"卖给他，柜台上报出五十 baiocchi」；58 行引语块与 60 行中文理解作「Carmela 把那剂药递过去，Violetta 把它放上柜台……"一次一大勺，早晚各一次。五十 baiocchi。"」）
原文侧：「Carmela hands the very remedy to Violetta, who places it on the counter before her stepmother’s brother. “A hefty spoonful, morning and evening. That’ll be fifty baiocchi.”」(text/ch36_chapter_36.txt:139)；「Finally, he digs the coins out of his pocket, sets them on the counter, then whisks the bottle away and very nearly runs from the shop.」(同章:142)〔第 36 章 Violetta Sells the Notary a Remedy〕
问题：第 2+5 类——柜台报价那句话的说话人是 Violetta，被记到 Carmela 名下；"收钱"全章无据（硬币由 Nicolò 自己撂在柜台上，无人收取），并与同一 md 的 11/58/60 行自相矛盾（反例 D：台词归错人 + 无据动作）。
建议改法：改成「最后把药递给 Violetta，由 Violetta 在柜台前报价五十 baiocchi，公证人自己摸出硬币撂在柜台上、抓瓶几乎逃走」。
置信：高
```

```
[阻断型] ch40 carmela brings maria to the convent.md:74
md 侧：「而这个设想推翻的是本章更早的那句自认：She cannot rebuild and sustain the mission of the apothecary, not without her mother.——紧跟在它后面，另起一段的只有三个词：Not as it was. 落点就在第二个的限定上」
原文侧：「She cannot rebuild and sustain the mission of the apothecary, not without her mother. Not as it was.」(text/ch40_chapter_40.txt:619)〔第 40 章 Carmela Brings Maria to the Convent〕
问题：第 5 类——两句在**同一个自然段**里，不是"另起一段"；"Not as it was." 是四个词，不是三个。
建议改法：改为「同段末尾只补了四个词的限定：Not as it was.」
置信：高
```

```
[阻断型] ch37a the witness.md:33
md 侧：「这一位与本书其他站在店门口的人同一类（第 20a 首那个闲荡者、第 21a 首那个修鞋匠）——都在这条街上，都靠"不看"过日子。」
原文侧：「loitering at the costermonger」(text/ch20a_the_loiterer.txt:13)、「on the north end of the Ortaccio,」(:16)、「but always with an eye」(:22)、「on the apothecary’s door.」(:25)；「along Via del Corso」(text/ch21a_the_cobbler.txt:13)、「Which is why he doesn’t.」(:100)〔第 20a 首 The Loiterer／第 21a 首 The Cobbler〕
问题：第 6+5 类——第 20a 那位闲荡者恰恰是以"一直盯着药铺门"定义的人，不是"靠不看过日子"；三首的街也各不同（Ortaccio 北端／Via del Corso／药铺隔一条街），"都在这条街上"无据。
建议改法：只保留修鞋匠那一例，删去"同一条街"与把闲荡者算进"不看"的说法。
置信：高
```

```
[阻断型] ch37a the witness.md:14
md 侧：「全诗现在时，末尾停在一个名词上而不是一个事件上。」（同文件 42 行中文理解自己译成过去：「所以嘛，那个男人打了他老婆，那个男孩偷了那只钱袋」）
原文侧：「she shouldn’t have seen」(text/ch37a_the_witness.txt:25)、「So that man smacked his wife」(:37)、「so that boy stole that purse」(:40)〔第 37a 首 The Witness〕
问题：第 1+5 类——诗中有三处过去式，"全诗现在时"与同块引语（md 38-39 行）和 42 行译文直接冲突（反例 A 型：分析与引语说的不是一回事）。
建议改法：改为「她的推辞用现在时，转述街面三事时两次落到过去式（smacked / stole），这也正是"听来的"标记」。
置信：高
```

```
[阻断型] ch39 maria mistakes carmela for giulia.md:50
md 侧：「Laura 的回答被切成两段，中间隔着一个 frowns 与一个问句，于是"她的小妹妹"这个信息到达 Carmela（也到达读者）时是迟到一步的」（同块 43-44 行引语：「“Who’s Bettina?” Carmela asks Laura at the door.」/「She frowns. “Her little sister. She died of the plague when Maria was ten.”」；46 行中文理解为「'Bettina 是谁？'Carmela 在门口问 Laura。Laura 皱起眉：'她的小妹妹。Maria 十岁那年，瘟疫把她带走了。'」）
原文侧：同章三段顺序为 :117「“Who’s Bettina?” Carmela asks Laura at the door.」→ :120「She frowns. “Her little sister. She died of the plague when Maria was ten.”」，两句回答紧邻〔第 39 章 Maria Mistakes Carmela for Giulia〕
问题：第 5+1 类——问句与 frowns 都在回答**之前**，Laura 的回答没有被切成两段；且与同块 46 行译文自相矛盾。
建议改法：改为「回答前先垫一个问句和一个 frowns，两个信息句本身是连着说出的」。
置信：高
```

```
[阻断型] ch32a the friends.md:14
md 侧：「末段整段落入将来时（There will be… / She will… / They will…），再回到一个 present 的进行（even now is tugging）。」
原文侧：「who even now is tugging too hard」(text/ch32a_the_friends.txt:112) 在「There will be relief」(:118) **之前**；将来时整段（118-181）之后回到现在时的是「and it occurs to her to worry」(:184)〔第 32a 首 The Friends〕
问题：第 5 类——顺序倒置：even now is tugging 属第 4 块末行、位于将来时段之前，不是"再回到"的那个现在时（md 自己 81 行的引语块也把它放在 92 行「and it occurs to her to worry」那块之前）。
建议改法：改为「将来时整段之后回到现在时的 and it occurs to her to worry；even now is tugging 在那段之前」。
置信：高
```

```
[阻断型] ch38 your mother is well.md:13
md 侧：「全章她唯一一次把私心说出口，就是那句被打断的 "Carmela wants to be happy for him, but her mother is still on the run and—"」
原文侧：「Carmela wants to be happy for him, but her mother is still on the run and—」(text/ch38_chapter_38.txt:22)，下一段是「“Your mother is well.”」(:25)——22 行无引号、无 said 标签，是叙述句〔第 38 章 Your Mother Is Well〕
问题：第 2 类——叙述语记成台词（反例 D）；同文件 11 行的处理是对的（「把 Carmela 没说完的心事截在半路」），13 行却说"说出口"。
建议改法：改为「全章她唯一一次把私心提到嘴边就被截断（那是叙述句，不是台词）」。
置信：中
```

```
[阻断型] ch39 maria mistakes carmela for giulia.md:38
md 侧：「随后是一段三对三的短兵相接：Carmela 两次 insist（She’s not well / Ignoring it isn’t helping her），Laura 两次不答（stalks away / busying herself）」（同块 40 行读者视角提示自己列的是「这一块的三个动词（insists / stalks / says）」）
原文侧：「“She’s not well,” Carmela insists.」(text/ch39_chapter_39.txt:40)、「Laura stalks away from her, busying herself with an unimportant task.」(:43)、「“Ignoring it isn’t helping her,” Carmela says.」(:46)、「When Laura turns around, her eyes are full of tears. “I know.”」(:49)〔第 39 章 Maria Mistakes Carmela for Giulia〕
问题：第 5 类——块内 insist 这个 tag 只出现一次（第二次是 says）；"两次不答"实际只有一次（stalks away 与 busying herself 是同一句里的两个动词），第二次 Laura 以 "I know." 正面答了；"三对三"也无从数起。
建议改法：改为「Carmela 连着两句（insists / says），Laura 先走开不答，第二次只答了两个词的 I know.」
置信：中
```

```
[提示型] ch36 violetta sells the notary a remedy.md:50
md 侧：**中文理解：** "“夫人，”他说着行了一个带嘲讽的躬。他转回身朝 Violetta——她已经一动不动站了好一会儿了。……"（48 行引语块起自 "He turns back to Violetta, who has been standing very still."）
原文侧：「“Signora,” he says with a mocking bow. He turns back to Violetta, who has been standing very still. “I’d heard rumors, Violetta. …”」(text/ch36_chapter_36.txt:106)〔第 36 章〕
问题：第 3 类——译文覆盖了引语块外的前一句（该句与块首同段相连，无跨段拼接，故只是引语短于支撑它的分析）。
建议改法：把 "Signora," he says with a mocking bow. 并入 48 行引语块，或从 50 行译文删去该句。
置信：中
```

```
[提示型] ch37 carla brings the violence inside.md:13
md 侧：「Laura 在本章始终没失控：动手的是她（gathering a poultice、ministers to the wound），定策的是她（We’re inviting them to open every drawer and bottle），末句也是她。……Laura 在本章开头只问了一句 Are you feeling well?，此后一直安静地做事。」
原文侧：「“It’s normal,” Laura murmurs, gathering a poultice. “Head wounds bleed excessively.”」(text/ch37_chapter_37.txt:95)、「“No, keep her upright.” Laura hurries over with the materials she’s gathered. “She needs to stay alert.”」(:107)、「“It looks worse than it is,” Laura says, dabbing away the blood.」(:110)、「“And if we start hurling accusations…?” Laura goes on.」(:140)〔第 37 章 Carla Brings the Violence Inside〕
问题：第 5 类——Laura 后半章多次开口下指令，"此后一直安静地做事"不成立，且与同一行"定策的是她"及 md 74 行「同一章里 Laura 刚说过 "It’s normal" 与 "It looks worse than it is"」冲突。
建议改法：改为「开头只问了一句 Are you feeling well?，随后先动手、到救治受阻时才出声定策」。
置信：中
```

```
[提示型] ch40 carmela brings maria to the convent.md:44
md 侧：「名字错位在本章不是道具：后面 Maria 会在清醒时喊出 Carmela 的名字（Carmela, not Giulia or Costanza.），也会在同一口气里把女儿夸成"你的女儿是个奇迹"（your daughter is a wonder）。」
原文侧：「“You know, Costanza”—Carmela stops short at the sound of Maria’s voice, stronger than it’s been in days—“your daughter is a wonder.”」(text/ch40_chapter_40.txt:272)；「Carmela jumps to attention at the sound of her name in Maria’s voice. Carmela, not Giulia or Costanza.」(:418)〔第 40 章〕
问题：第 5 类——两处相隔 146 行、顺序与行文相反（夸女儿在前、喊对名字在后），而且夸女儿那一句发生在 Maria 仍把人认成 Costanza 的场景里，不是"同一口气"。
建议改法：拆成两个时间点是非分明的例子，并注明 272 行那句是在错认中说出的。
置信：中
```

```
[提示型] ch41 there is a child.md:13
md 侧：「Carmela 在本章是招呼客人、给糖杏仁、给孩子划额头祝福的那一个」
原文侧：「“I see you over there,” Carmela calls when the door shuts behind the customer. “There’s a fresh batch of sugared almonds in the back.”」(text/ch41_epilogue.txt:55)、「Flora Maria spots the candied almonds and there are no distractions more enticing…She hurries to the tray.」(:70)、「Violetta slips Flora Maria a little package of candied almonds to take home.」(:109)〔第 41 章（尾声）There Is a Child〕
问题：第 5 类——Carmela 只告知有一批新的，杏仁由孩子自取、由 Violetta 打包递给她；与本文件 54-55 行引语块一致，冲突只在导航行。
建议改法："给糖杏仁"改为"一句话把糖杏仁指给她"。
置信：中
```

```
[提示型] ch41 there is a child.md:38
md 侧：「技术上，作者把整段放在过去完成时（had watched / had ducked / anointed），主叙述仍是现在时」
原文侧：「Flora Maria had watched, jealous, as the priest anointed first Matteo and then Giada with holy oil…Flora Maria led the other younger children in their own sacred ritual.」(text/ch41_epilogue.txt:19)、「She had ducked into the shop—that back door never was secured—and grabbed the nearest bottle of oil her fingers found.…With it, Flora Maria anointed each small child, while droning the best Latin she knew」(:22)〔第 41 章（尾声）〕
问题：第 4 类——三个举例里只有 had watched / had ducked 是过去完成时，anointed（以及 led、grabbed）是一般过去时；同文件 15 行只列 had watched / had ducked，是对的。
建议改法：删去括号里的 anointed，或补一句「从句与后续动作落回一般过去时」。
置信：中
```

```
[提示型] ch37a the witness.md:66
md 侧：「meddles 在一行之内被换了两次介词：先 in every trouble（摊子太多），后 with others（关系危险）」
原文侧：「if she meddles in every trouble」(text/ch37a_the_witness.txt:46) 与「if she meddles with others」(:58)，两个独立诗行，中间隔着「she’d have no time, no coin,/nothing left for all that’s wrong/in her own life and besides」(:49-55)〔第 37a 首 The Witness〕
问题：第 5 类——"一行之内"不成立（md 自己的关键词行也把它们列为两个条目）。
建议改法：改为「同一个 meddles 在两个诗行里换了介词，中间隔着她那套"没时间没钱"的算账」。
置信：中
```

```
[提示型] ch37 carla brings the violence inside.md:11
md 侧：「进来的妇人叫 Carla，是 Violetta 的继母，当着三个女人的面喝令 Violetta "shut your whore mouth"，还要她离自家远点」
原文侧：「“Violetta?”」(text/ch37_chapter_37.txt:48)…「“Signora,” Carmela says, wishing all over again that her mother were here. “Violetta isn’t—”」(:55)、「“You shut your whore mouth,” she snaps. “And I’ll thank you to stay away from my family!”」(:58)〔第 37 章〕
问题：第 5 类（把悬置点补死）——紧邻的前一句是 Carmela 被打断的话，"she snaps" 的受话人原文不确定（骂 Violetta、骂 Carmela 都读得通），导航行直接坐实为"喝令 Violetta"。
建议改法：改为「一句 "You shut your whore mouth" 截断 Carmela 的话，受话人原文没有标明」，不作裁决。
置信：中
```

```
[提示型] ch32a the friends.md:11
md 侧：「她们晾衣绳横在两家窗户之间，绳那头就在药铺北边的 Ortaccio 上方」
原文侧：「bringing in the laundry」(text/ch32a_the_friends.txt:13)、「that hangs between their windows」(:16)、「over the north end of the Ortaccio」(:19)、「so close to the apothecary」(:22)；另参「The nearest public fountain is a short walk from the apothecary—through a couple of alleys in the jumbled warren of streets known as the Ortaccio」(text/ch07_chapter_7.txt:64)〔第 32a 首 The Friends〕
问题：第 5 类——"north" 说的是 Ortaccio 这条街自己的北端，不是"药铺北边"；全书未写 Ortaccio 在药铺哪一侧，同文件 31 行译文（「那窗就在 Ortaccio 北端上方，离药铺近」）才是对的。
建议改法：与 31 行统一为「Ortaccio 北端的上方，离药铺近得走出门就能听见」。
置信：中
```

```
[提示型] ch38 your mother is well.md:13
md 侧：「Maria 的那句"Maria is fine, mostly."从第一行就开始漏（forgetful or confused、less talkative、扶着碗站起身时绊了一下）」
原文侧：「Maria is fine, mostly. If she’s forgetful or confused sometimes, it’s hard to tell if it’s new or how she’s always been, at least as long as Carmela has known her.」(text/ch38_chapter_38.txt:1)〔第 38 章〕
问题：第 2 类残余风险（反例 D）——本章第一句是叙述句、不是 Maria 的话，"Maria 的那句"易被读成她的自陈；后半句"从第一行"显示作者本意是章首句，故仅提请注意。
建议改法：改为「关于 Maria 的章首那句」。
置信：低
```

已排除的疑似项（核过为原文属实或 md 自身已作悬置处理，未列入）：ch32a→ch21a "like the chandler / but not"、ch32 "aromatic with lemon balm"；ch33→ch32 三处台词与 ch02 的"女巫/蛤蟆"传闻出处（第 2 章那句确实出自 Violetta，md 未误记给 Serafina）；ch34→ch01 "brazen Maria cackles…"；ch35→ch01/ch08/ch17/ch28 各处；ch35a "There is a vendor" / "He’ll wake me before dawn" / "about his roaming hands"；ch36→ch01 "Violetta pays for her potion"；ch37 "名字 Carla 落在打人的那句里"（md 44 行已明确限定"在叙述层"，并自己列出门口那声 "Carla, what are you—"）；ch38 mostly 两次、ch39 开篇、ch40→ch10/ch23、ch41 全部计数断言（magistrate/raid/convent/poison/Acqua 各 0、Flora Maria 26、Maria 26、Giulia 0、La Tofana 1、Tofana 2、Auntie Carmela 3 且全书他处无 Auntie、officinalis 3、blasphemous 1、scolding 3、forehead 2、back door 1、secured 1、in one piece 全书仅 1 处、25 首韵文插叙）。

核对文件数 12 / 引语块数 66 / 报警数 17（高 6·中 10·低 1）


---

## 批四（e 步 总览三篇）

原始报告（子代理逐字输出，未改写）：

核对完成（只读，未改任何文件）。按 brief 格式输出 12 条，按确定性从高到低。

---

```
[档位建议: 阻断型] 00_金句精选.md:117（⑭ 上下文）
md 侧：「第二章后的韵文插叙 The Witch（出处 ch02a）；全诗以问句收尾，不作答。」
原文侧：ch02a_the_witch.txt —— 问句在诗中段的 :103–:127「Is she moments from death … on seeing her / as other?」，其后仍有 :130「Someone shouts.」…直到全诗末三行 :244–:250「because this / other / has breathed her last.」
问题：计数与结构断言（诗的实际收束不是问句）＋ 反例 C（前提性错误）
建议改法：改为「问句悬在全诗中段（处决进行中），末尾仍以女子断气收束，问题不作答也不收尾」。
置信：高
```

```
[档位建议: 阻断型] 00_金句精选.md:209（㉔ 为什么重要）
md 侧：「而祝福落点正是额头：本章先前是孩子拿圣油在更小的孩子额头上留下亮痕，现在是大人把祝词按在同一个位置。」
原文侧：ch41_epilogue.txt :19「the priest anointed first Matteo and then Giada with holy oil」（圣油属于神父、对象是受坚信礼的两名较大孩子）；:22「She had ducked into the shop … and grabbed the nearest bottle of oil her fingers found. A bright, happy scent confirmed it to be Melissa officinalis. … With it, Flora Maria anointed each small child」——给更小的孩子抹的是药铺里的香蜂辣油，:25 的「glistening smudge on his forehead」由此而来
问题：说话人/施动者（器物属性错配）＋ 反例 D（把甲处修饰语「holy」安到乙处的油上）
建议改法：「拿圣油」改「拿药铺的一瓶香蜂草油冒充圣油」。
置信：高
```

```
[档位建议: 阻断型] 00_概述.md:38（人物表 Maria 行）
md 侧：「ch40 头伤不治死于修院，被 Carmela『领过拱门』」
原文侧：ch40_chapter_40.txt :649 全章末句「Now another door has opened. Carmela squeezes Maria’s hand in hers and guides her through the archway.」（通章无一句写她咽气；ch41 全章亦无一处提及 Maria 之死）；本书自己的 00_情感节点.md:199 写明「原文就此收章，Maria 是否在那一刻咽气，原文未写」，:11 更把「Maria 咽气时刻」列为已按规则留白处
问题：结局断言（替作者把悬置点补死）＋ 跨文件自相矛盾 ＋ 反例 C
建议改法：改为「ch40 头伤不治、被送进修院，章末由 Carmela『领过拱门』——原文未写咽气」。
置信：高
```

```
[档位建议: 阻断型] 00_金句精选.md:55（⑥ 上下文）
md 侧：「……说洗衣妇 Geneviève Laurent 成了 "Lady of Death"；Giulia 念完接着讲男人们为什么怕它。」
原文侧：ch09_chapter_9.txt :91「She hands Giulia a leaflet.」→ :117「“But this is ridiculous.” Giulia tosses the leaflet onto the counter.」→ :120「Carmela picks it up and studies it.」→ :162「Maria takes the leaflet and tosses it in the fire on her way back to her worktable.」→ 其后 :183 才是 ⑥ 的引语「“But men like Benicio,” Giulia goes on」
问题：施动者错配（全文无一处 Giulia 朗读传单；到手后被 Carmela 细看、被 Maria 投火， Giulia 的议论距阅读已过数段）＋ 反例 A/B
建议改法：改为「传单在几家手里传过（Carmela 细看、Maria 一把丢进火里），Giulia 随后把话头转到男人们为什么怕它」。
置信：高
```

```
[档位建议: 阻断型] 00_金句精选.md:50（⑤ 呼应关系）
md 侧：「与 ⑧ 的书名句同属"剂量"这一层：一处讲一滴就够，一处讲一切皆看量。」
原文侧：ch08_chapter_8.txt :163「The smallest amount will kill a man.」＋ :172「“One barleycorn should do it, you understand?”」——本章的量词是一粒 barleycorn，全章无 drop；按"滴"给药的是 ch12_chapter_12.txt :130「A woman is to give her husband one drop the first night.」/ :280「Six drops to kill a man without a trace.」
问题：计数与数字（跨章计量嫁接：把 ch12 的滴剂单位安到 ch08 的砷上）＋ 反例 D
建议改法：改为「一处讲一粒就够致命，一处讲一切皆看量」。
置信：中
```

```
[档位建议: 提示型] 00_概述.md:28
md 侧：「管事的 Sister Francesca 对她一言不发、处处守着她。」
原文侧：ch34_chapter_34.txt :1「a humorless sister who looks up when Giulia enters the room but does not say a word」（仅进门那一刻）；同章 Francesca 有多句台词：:22「“I am used to working alone.”」、:46「“We have no use for rue or pennyroyal.”」、:85「“You know the holy wood cure?”」、:103「“Of course not!”」；「处处守着她」有支撑（:9–:17「there the sister is」三叠＋「everywhere Giulia moves, it seems she is underfoot」）
问题：事实断言过强（把「进门时不语」扩写成整章「一言不发」）
建议改法：「一言不发」改「开口也句句设墙」（或「进门一声不吭，处处守着她」）。
置信：中
```

```
[档位建议: 提示型] 00_概述.md:37（人物表 Giulia 行）
md 侧：「第 23 章顶罪离铺入修院，第 40 章明言不归，尾声未再出场」
原文侧：ch23_chapter_23.txt :232「“I’m not going to the convent. You know what the Church did to my mother.”」（:220 Maria 只是假设“If she goes to the convent”）；修院收留的许诺出现在 ch25_chapter_25.txt :32「“I am the Mother Superior at Santa Maria of the Angels. You are welcome with us anytime.”」，人在修院是 ch34_chapter_34.txt :4「The Mother Superior told Giulia when she arrived that she would be welcome」；本文件 :28 自己也把「修道院里的 Giulia」标在 ch34
问题：计数与数字（第 X 章标签贴错章，且与同文件 :28 的 ch34 标注相互别扭）＋ 反例 C
建议改法：改为「第 23 章顶罪离铺，第 25/34 章入修院」。
置信：中
```

```
[档位建议: 提示型] 00_概述.md:30
md 侧：「Giulia 赶到时已判明脑内出血，无力回天」
原文侧：ch40_chapter_40.txt :311「I suspect that her brain is bleeding, from when she hit her head.」（suspect 而非判明）＋ :317「“There’s nothing we can do to stop it.”」＋ :323「“There’s a chance it will stop on its own,” Giulia says.」
问题：结局断言（把「怀疑＋尚有一线」写成确诊与绝境）
建议改法：「已判明」改「疑为」，并保留 Giulia「仍有自行止住的可能」这一层。
置信：中
```

```
[档位建议: 提示型] 00_金句精选.md:48（⑤ 上下文）
md 侧：「……抓着她手腕说出这四句，随后把一只棕色纸包推过柜台——"I brought what we discussed"。」
原文侧：ch08_chapter_8.txt :118「But then he leans in, inches from Carmela’s face and says, “I brought what we discussed.”」（在手腕那段 :163「The priest grabs Carmela’s wrist. …」之前，纸包 :169「He draws a small packet wrapped in brown paper … pushes it across the counter」在其后）
问题：场景时序（破折号把早于手腕一幕的台词挂到了推包动作上；说话人本身无误）
建议改法：把该句移到「醉得把 Carmela 当成 Giulia」之后、四句台词之前。
置信：中
```

```
[档位建议: 提示型] 00_金句精选.md:143（⑯ 呼应关系）
md 侧：「与 ⑪（第十三章正文）同街：那里一只黑猫穿过她的去路，这里它成了这条街的拥有者；两句写的同一段石板路。」
原文侧：ch13a_the_cat.txt :4–:7「There is a cat / that wanders / from the Piazza Monte d’Oro / to the Church of San Girolamo, / and around the Palazzo Borghese.」——是类型化的“a cat”与一片活动范围（多处地名），并非 ch13 集市/教堂院里的同一只猫、同一条街；本库 00_概述.md:59 自设规则即「原文刻意用 but not 与编号章人物保持距离，阅读时不应把任何一首指认给某个具体角色」
问题：跨章身份坐实（把插叙的类型声记成正文里的个体）＋ 反例 D
建议改法：「同街／同一段石板路」降为「同题（教堂院里的黑猫）；诗里的猫是游荡于数个地点的类型」，去掉「它」的同一性。
置信：中
```

```
[档位建议: 提示型] 00_金句精选.md:75（⑨ 上下文）
md 侧：「第二章末段，说话的是 Violetta：前一段刚写明"Violetta said to Nina"，这一段是"she repeated, louder this time"。」
原文侧：ch02_chapter_2.txt :142「“Didn’t you know?” Violetta said to Nina … “Carmela’s mother is a witch.”」与 :154 的重复喊话之间还隔着 :145、:148、:151 三个自然段（「Some of the children laughed…」/「Nina glanced at Carmela…」/「Violetta wasn’t content only to have said it, though.」）
问题：场景定位措辞（说话人判定正确，「前一段」的位置描述不成立）
建议改法：「前一段」改「上文数段前」。
置信：低
```

```
[档位建议: 提示型] 00_概述.md:22（身世与配方段）
md 侧：「第 10 章跌进 Giulia 的往事：父亲是把她推进火里的怪物」
原文侧：ch10_chapter_10.txt :169「He stood up from the table and shoved her out of his way.」→ :172「Giulia fell, crashing into the cauldron. The iron blazed and the flames licked her skin before she could change her momentum and collapse away from the fire.」——是推搡后跌进火里，不是「推进火里」
问题：施动方式（把推搡写成蓄意投火）
建议改法：改「一把推得她跌进火里」。
置信：低
```

---

**对本篇自带自检声明的审查结论**（00_金句精选.md:11–13）

- :11「凡『某人对某人说』式归因……一律回所属章 text/ 开窗口核对」——**说话人层成立**：25 条里所有带归因的引语（② Giulia、③ Giulia、④ Giulia、⑤ 神父、⑥ Giulia、⑨ Violetta、⑩ Tassi、⑬ Violetta、⑳ Carmela 与 Moretti、㉑ 母亲信、㉔ Carmela）逐条开窗核对无误，含最易错的 ②「before she finally speaks」与 ⑳「You're a child」。
- :12「归因与场景另开原文窗口……核对 20 处，据此改写了 5 条的上下文表述」——**「场景」这半未落实**：上述 ⑥（朗读主体）、⑭（诗体收束）、㉔（圣油）、⑤（计量与时序）四条都属于「归因与场景」口径内、且一次 `grep -n -B10 -A5` 即可发现的问题仍在文内；该声明的数字应视为**未达成**，不宜作为「场景层已清」的依据。
- 同段可机检的数字经复核为真：25 条／五组（4+4+5+6+6）／韵文 6 条＋正文 19 条=25／25 段插叙首行一律 There is a|There are／⑲ 的病名确为 11 行／⑱ 的 ch21a 全篇确仅 1 处 you／节点数 16／引语块 29／节点十六 的 raid·poison·magistrate·search 在 ch41 各 0 次／全书正文仅 1 处四位年份（ch09:98 February 1651）。

**汇总**：`00_金句精选.md 核对 25 条（另核头部 5 项自检声明）/ 报警 7 条（高 3：⑭ ⑥ ㉔；中 3：⑤ 剂量、⑤ 时序、⑯；低 1：⑨）；00_概述.md 核对约 40 条断言（设定 3＋脉络 7 段＋人物表 11 行＋主题 4＋形式 6＋附注引文 6）/ 报警 5 条（高 1：Maria 死于修院；中 3：Francesca 一言不发、ch23 入修院、已判明脑出血；低 1：推进火里）；00_情感节点.md 核对 16 节点 29 条引语的归因与叙述 / 报警 0 条。合计 12 条（高 4 · 中 5 · 低 3）。已确认为悬置/留白而不报 10 处：Maria 咽气、Moretti 行刑场面、Moretti 案结局、Laura 婚礼、Carmela 与 Violetta 名分、Father Piero 结局、Tassi 结局、㉕ 店铺名下、㉔ 挂坠盒不开、Eleonora 下落。另按指派跳过两条已定性的提示型（00_概述.md:28 chNN 范围标签；㉔/③ "We take care…" ch06 与 ch15 各现一次）。`