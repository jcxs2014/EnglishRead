# ch43 the last evening of the old normal — 判定表（R5）

- 原文：`text/ch43_the_last_evening_of_the_old_normal.txt`
- 精读：`ch43 the last evening of the old normal.md`
- 机器层：`2-machine.json` rc=0（verdict=ok，8 块，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5）
- 结论：**无阻断**；漏 7（提示）· 编 0 · 错 2（提示）· 跳过 3

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 8 块引语全部逐字、且全部属本章 | `2-machine.json` counts.segments=8, segment_miss=0；逐块回捞 ch43 文本均命中（`:23` `:47` `:56` `:112` `:134` `:211` `:235` `:342`） | 引语层干净 | 假红（机器已过，人工复核同意） |
| 2 | 四个子项（中文理解/关键词/为什么这样写/读者视角提示）8 块齐全，块内 3–10 行，中位 6 | `2-machine.json` form.subitems_modal；block_range [3,10] | 形态合规 | 假红 |
| 3 | 「二〇二〇年二月七日，星期五」的日期锚点写对 | `:18` “Friday, February 7, 2020 (Alba is 18, Clare is 48, Beck is 43)”；md:132 同 | 正确 | 已核实为正确 |
| 4 | md 把「要囤粮、卖股、居家两年」的受话人写成「母亲与贝克」（块 4） | `:112` “she wants **you** to go out and buy tons of groceries and stuff and sell some of your stock… Like, about two years. She called it self-quarantining.” | 正确（you＝在场的克莱尔与贝克；Alba 对他俩说话） | 已核实为正确 |
| 5 | md:132 一句话总结写「年长的自己让她转告母亲」 | 同上 `:112`；另 `:117` “We're going to New York for Clare's show next week.” 贝克当场接话 | **错**：受话人由「母亲与贝克」缩成母亲一人，与前文块 4 中文理解自相矛盾 | 提示 |
| 6 | md:11 一句话概括：「两个大人只当是电影，**直到**她说出戴口罩、抢厕纸与死者的名字」 | 原文实际次序：`:95` 李文亮名字 → `:112` 疫情/两年 → `:117-121` 纽约 → `:211` 口罩/厕纸 → `:230` “it sounds more like a zombie movie than real life” → `:234` Floyd | **错**：时序倒置（电影类比在口罩之后、名字在最前） | 提示 |
| 7 | 李文亮的名字与「年长的自己提过却没给名字」这层传话机制未进 md | `:95` ““Li Wenliang,” Alba says. “I never knew his name.””；`:104` “My older self mentioned him a while ago. She didn't say his name, though.”；`/usr/bin/grep -c "李文亮" ch43*.md` → 0，rc=1 | **漏**：本章对「预告如何残缺」的唯一实证 | 提示 |
| 8 | 纽约之行与 Drawing Center 画展（2/17 开幕）整段未进 md | `:117` / `:121` / `:127` “My show at the Drawing Center opens on the 17th.” / `:128` “if you don't want us to go, we won't go.”；`/usr/bin/grep -c "纽约"` → 0；`/usr/bin/grep -ln "Drawing Center" text/*.txt` 仅命中本章（rc=0） | **漏**：预言撞上的唯一具体计划；因全书仅此一处提及，按一次性布景处理 | 提示 |
| 9 | 双胞胎 Nick / 密歇根大一 / Nadia 在西北 未进 md | `:86` “Nick is Carl's twin. They're both freshmen at the University of Michigan. He is Nadia's boyfriend, and since Nadia is at Northwestern with Alba…”；`grep -c "尼克"`→0 | **漏**：关系网背景 | 提示 |
| 10 | 「他是同性恋，我们早知道」未进 md | `:161` “We exchange confirmative looks: He's gay, we knew it.”；`grep -c "同性恋"`→0 | **漏**：对 Carl 分手理由的解释性伏笔 | 提示 |
| 11 | 卧室里伊莎多拉那段（「要在没有母亲的情况下长大」/「我更担心阿尔芭」）未进 md | `:307` “I felt bad for Isadora, that she would have to grow up without a mother.”；`:325` “I can't bear to think of her down there, waiting.”；`:329` “I'm more worried about Alba”；`grep -c "伊莎多拉"`→0 | **漏**：伊莎多拉线在本章的收束；与后文她的处境直接相关 | 提示 |
| 12 | 「明天列清单」的行动决定未进 md | `:249` ““Tomorrow,” Alba says. “We'll make a list and start on it tomorrow. Tonight I'm too sad.””；`grep -c "清单"`→0 | **漏**：承接下一章的唯一钩子 | 提示 |
| 13 | 贝克高中恋人赴斯坦福前一天甩了她 | `:171` “she had a high school sweetheart who dumped her the day before he left for Stanford” | 未收；细节性回照，不影响本章因果 | 跳过 |
| 14 | 年龄锚点 18 / 48 / 43 | `:18` 同上 | 未收；同 ch30 口径 | 跳过 |
| 15 | 「先笑、再问、最后沉默」的反应序列 | `:117` nervous laugh；`:196` “We all fall silent”（发生在卡尔分手段末）；`:244` “So what do we have to do?” | 顺序被压平，但三个锚点都在原文，不作事实断言判 | 跳过 |
| 16 | 块 5 中文理解：「卡尔今天和她分手」（主动方） | `:134` “Carl broke up with me today and I sort of knew he was going to” | 方向正确，未写成「她与卡尔分手」 | 已核实为正确 |
| 17 | md:132「贝克问要是他们中有一个死了怎么办，两人说好不死」 | `:290` “What if one of us dies?”（贝克）→ `:295` “Let's not.” → `:303` “Deal?” / “Deal.” | 说话人、次序、结果全对 | 已核实为正确 |
| 18 | md:91/132「克莱尔最后祈祷」「愿阿尔芭见过的一切放过他们」 | `:342` “I had wanted to be free… but now I pray that whatever Alba has already seen, whatever she knows must happen, that it might spare us.” | 祈祷者＝克莱尔、对象空着（“though I don't know to whom, or what”）均对 | 已核实为正确 |
| 19 | md:15 叙事手法「以克莱尔第一人称、现在时推进」 | `:23` “Beck and I are eating dinner”；`:47` “I call to her again”；结尾转 past perfect `:342` “I had wanted to be free” | 主体成立（末段时态切换属有意收束），不作为错 | 已核实为正确 |
| 20 | 词汇 14 条例句逐字 | 例：`:105` “I like to yell at the screen and suggest possible afterlives for each miscreant.”；`:118` “Alba lets out a long wavering breath.”；`:290` “Her profile is silhouetted against the curtained bedroom window.”；`:127` “My show at the Drawing Center…” | 逐条回捞均命中，无改写 | 已核实为正确 |

## 已核实为正确（防下一轮误修）

1. **「要母亲与贝克去囤粮」不是错**：原文 `:112` 的 “you” 指在场的克莱尔与贝克两人（Alba 正对二人说话，`:117` 贝克立刻接话）。**勿改成「要她自己囤」。**
2. **「卡尔今天和她分手」方向正确**：`:134` “Carl broke up with me today”——主动方是卡尔。**勿改成「她与卡尔分手」。**
3. **「乔治·弗洛伊德被警察杀害、大桥升起拦抗议者」方向正确**：`:234-235` “will be murdered by police… all the bridges over the Chicago River raised to keep the protesters from crossing”。**勿改成「抗议者升起大桥」。**
4. **「克莱尔最后开口祈祷」不是贝克**：本章第一人称是克莱尔，`:342` “I find myself praying”。**勿改主语。**
5. **「两人说好不死」有原文三段支撑**（`:290` / `:295` / `:303`），不是 md 编的。**勿删。**
6. **祈祷发生在床上睡前，不是梦醒之后**：`:342` 同段先写 “We lie still together”，最后才是 “I dream of monstrous black wings”。**勿把祈祷挪到梦后。**
7. **「像哭过或吐过」照抄原文**：`:47` “she looks as though she's been crying or vomiting”。**勿改成单指哭。**
8. **「not quite in the doorway」被译成「站在门口却没有完全进来」是对的**：`:47` 原句含 “stand not quite in the doorway”，既非进门也非离开。**勿改成「站在门里」。**
9. **「两个大人没有打断她」有据**：`:240` 前后 “We sit and stare at Alba… a Cassandra daring us to disbelieve her.”，且 `:244` 之后才发问。**勿改成「他们不停插话」。**
10. **「冰淇淋在汽水里化着」可写**：`:122` “Her ice cream sits half eaten, melting into the ginger soda.” md 未写，但若补写不算编。
11. **「病毒如风、效果才可见」是原文比喻**：`:342` “The virus moves like a wind, an invisible force that can be known only by its effects.” **勿改成「病毒如雾/如水」。**
