# ch45 oliver practices piano — 判定表（R5）

- 原文：`text/ch45_oliver_practices_piano.txt`（464 行）
- 精读：`ch45 oliver practices piano.md`（153 行）
- 机器层：`2-machine.json` rc=0（verdict=ok，10 块，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5）
- 结论：**阻断 1**；漏 8（1 阻断 + 7 提示）· 编 0 · 错 0（2 条假红）· 跳过 0

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 10 块引语逐字、均属本章 | `2-machine.json` segments=10, segment_miss=0；回捞 `:23` `:66` `:75` `:102` `:147` `:157` `:176` `:338` `:347` `:464` 全命中 | 引语层干净 | 假红 |
| 2 | 块数 10 偏离本书常见区间 3–9 | `2-machine.json` form.block_hint「块数 10 偏离本书常见区间 3–9」；block_target [8,15] 仍达标 | 未超硬上限，只报不判红 | 假红 |
| 3 | 1975 段把奥利弗写成「少年」 | `/usr/bin/grep -c "少年" "ch45 oliver practices piano.md"` → 0，rc=1；`:18` “Alba is 24, Oliver is 38” | 未写少年；1975 段的他是 38 岁 | 已核实为正确 |
| 4 | 亲属称谓混用「舅舅/叔父」 | `grep -c "叔叔"` → 1（`:153`）；`grep -c "舅舅"` → 0；原文 `:214` “You must call him Uncle Stephen.”、`:362` “Your Uncle Stephen sent me.” | 统一「叔叔」，指向父系的 Stephen | 已核实为正确 |
| 5 | **父母的核心叮嘱「别告诉他时间旅行的事」整条未进 md** | `:245` ““Don’t tell him anything,” my mother said with surprising force.”；`:253` ““Don’t tell him about the time traveling,” my father clarified.”；`:261` ““Just don’t—travel. Be very strict with yourself.” … “For me. For us. Try very hard, okay?””；`/usr/bin/grep -c "时间旅行"` → 0，rc=1；后续章节正以此为前提（`text/ch46_the_drowned_hotel.txt:77`、`:252`） | **漏 = 阻断**：2041 段唯一的行动约束，既未进任何一块，也未在任何导航条里说明取舍；导航 `md:11/12/13/14/15` 全部无 | **阻断** |
| 6 | 两部手机与「叔叔抱着婴儿时的你」全息影像未进正文 | `:208` “one the fancy Xiaomi I had been begging for, the other a cheap-looking, battered one.”；`:226` ““This one is hacked—you can use it without anyone tracking it.””；`:214` “You must call him Uncle Stephen. He doesn’t use his Chinese name now. He will call you Oliver.”；`grep -c "手机"`→1（仅 `md:15` 「衣服、手机、证件、扫描、书」的清单词） | **漏**：改名换姓与「两部手机」的来处被抽空 | 提示 |
| 7 | 扫描时调动的「林黛玉」记忆未进 md | `:327` “I summon the same memory I always use for scans: … We called her Lin Daiyu, but that was not her name. Her face had been scarred in an acid attack.”；`:328` “Daiyu made me ginger tea and sang to me.”；`grep -c "林黛玉"`→0 | **漏**：「用同一段记忆过关」是他此后每次过安检的办法 | 提示 |
| 8 | 书店四本书（含 Watership Down「兔子找新家」）未进 md | `:393` ““this one is about rabbits who must find a new home, you’ll like this.” … Watership Down.”；`grep -c "兔子"`→0 | **漏**：「找新家」是本章主题回声 | 提示 |
| 9 | 「你叔叔人好吗？」→「不。」这一问答未进 md | `:447` “I don’t remember my uncle. Is he kind?”；`:451` “Isadora consults the Interstices. “No,” she says.”；`:459` “All is for the best in the best of all possible worlds.”” | **漏**：来投奔的人「不善」，且说者当场收回——全章最重的伏笔 | 提示 |
| 10 | 「当你我都到了中年…可以彼此安静」未进 md | `:124` “When you and I are both middle-aged we sometimes spend days talking intermittently, with long gaps between; we’ve already said so much that we can be quiet with each other.”；`grep -c "中年"`→0 | **漏**：把两人关系钉在「中年伴侣」的硬证据 | 提示 |
| 11 | 1975 段的年龄（Alba 24 / Oliver 38）未写 | `:18` “Monday, February 24, 1975 (Alba is 24, Oliver is 38)”；`grep -c "三十八"`→0、`grep -c "二十四"`→0；2041 段的 13 岁写对（`md:11` `:14` `:153`） | **漏**：全书年龄表最易错处，1975 段只写「十几小时」不写年龄 | 提示 |
| 12 | 上海童年的餐桌/书堆/Zǐ Yì 未进 md | `:142` “In the middle of the table were piles of books, like a mountain range dividing the table”；`:156` “I had a friend in my building, Zǐ Yì, my best friend. … I still miss him.” | **漏**：软禁线已由块 5 覆盖，此处属取舍；仍建议留一句「最好的朋友」 | 提示 |
| 13 | `md:11` 的「他十三岁被父母…送进皇家学院」会不会被读成 1975 年的他十三岁 | `:66` “we sent someone else’s audition video. I had never touched a piano. I was thirteen”；`:18` Oliver is 38（1975） | 句子主语指 2041 的当年，且 `md:14`「十三岁的奥利弗在机场」分工清楚，不与 1975 混 | 假红 |
| 14 | `md:15`「中间隔着几十年与一次跨时旅行」 | `ch44:121` “I will be born this coming August.”（2028 年 8 月出生）⇒ 1975 年他尚未出生，1975 段必为回溯 | 措辞笼统但不构成事实错 | 假红 |
| 15 | 块 7 的「明白父母不指望我回来」归属 | `:176` “I understood for the first time that my parents didn’t expect me to return.” | 判断者是 Oliver 本人，非母亲说出口；md `:81` 写法正确 | 已核实为正确 |
| 16 | 「叔叔雇了伊莎多拉」的归属 | `:362` ““Your Uncle Stephen sent me,” Isadora says.”；`:455` “Wasn’t it my uncle who hired Isadora to be my minder?” | md `:153`「被叔叔派来的伊莎多拉」方向正确 | 已核实为正确 |
| 17 | 试奏弹砸的曲目与「即兴救场」 | `:84` “made a complete mess of Mozart’s ‘Ah, vous dirai-je, Maman.’”；`:102` “Nothing; I was improvising. … I started moving through the circle of fifths” | md `:11` 与块 4 均正确 | 已核实为正确 |
| 18 | 词汇 16 条例句逐字 | 例：`:125` “I’ve got tendinitis in my upper back.”；`:119` “I think my uncle explained that my parents were in danger of imprisonment and I could not go back, and I think he bribed them.”；`:232` “The holopassport rotated slowly, my new name encircling my head and shoulders, everything except my eye color and height quite untrue.” | 全命中，无改写 | 已核实为正确 |

## 已核实为正确（防下一轮误修）

1. **1975 段的奥利弗是 38 岁，不是少年**：`:18` “Monday, February 24, 1975 (Alba is 24, Oliver is 38)”。他讲的是**十三岁那年的往事**（`:66` “I was thirteen”），讲故事的此刻已 38。**勿按「他十三岁」把 1975 段改写成少年场景。**
2. **2041 段的他才是 13 岁**：`:166` “Wednesday, October 30, 2041 (Oliver is 13)”，`:319` ““Thirteen.””。两段的年龄分工勿对调。
3. **叔叔＝父系的 Stephen，全书统一「叔叔」**：`:214` “You must call him Uncle Stephen.”、`:362` “Your Uncle Stephen sent me.” **勿写成「舅舅」或「叔父」。**
4. **「别告诉他时间旅行的事」是母亲先起头、父亲补明确的**：`:245` 母亲 “Don’t tell him anything.”，`:253` 父亲 “Don’t tell him about the time traveling.”。若要补写，**别把顺序倒过来**（不是父亲先说）。
5. **改名是父母的安排，不是他自己选的**：`:214` 父亲 “He will call you Oliver.”；`:347` “Oliver, I remember, is my name now.”。**勿写成「他给自己取名奥利弗」。**
6. **「护照上除了瞳色与身高都不真」是原文**：`:232` “everything except my eye color and height quite untrue”。**勿改成「除了姓名都不真」。**
7. **试奏弹砸的是莫扎特《妈妈请听我说》**：`:84` “Mozart’s ‘Ah, vous dirai-je, Maman.’”——不是随便一首。**勿换成《小星星》以外的曲名**（该曲即《小星星变奏曲》主题，原文用的法文题名，保留法文名更稳）。
8. **老师叫 Madeline Baxter，后来成为他导师的是 Garcia 教授**：`:74` “Madeline Baxter was her name.”；`:110` “Professor Garcia, who became my tutor”。**两个名字勿混。**
9. **「被录取」是叔叔转述的，且叔叔显得意外**：`:110` “my uncle said to me, ‘They say that you are accepted.’ He seemed surprised.”。**勿写成「教授当场宣布录取」。**
10. **伊莎多拉＝「你的陪同」（minder），不是保姆/家教**：`:352` “I’m Isadora… I’m your minder.”；`:362` “I’m going to fly with you to London”。**勿写成「管家」或「监护人」。**
11. **「他先查间隙才说『不』」这一层不能省**：`:451` “Isadora consults the Interstices. “No,” she says.”——先查后答，再当场收回（`:459`）。**若补写，勿写成她脱口而出。**
12. **飞机是「开始向后倒退」，不是起飞**：`:464` “I watch through the windows as the plane begins to move backward.”。**勿改成「飞机起飞」。**
