# ch38 an horizon is nothing save the limit of our sight — 判定表（R5）

- 原文 265 行 / 精读 132 行；机器层 `2-machine.json` **rc=0**（verdict=ok，8 块 / 8 段全逐字，counts 八类全零，words 2857）
- 报数四组：**逐字 8/8 通 · 对应 8/8 通 · 形态 通（H1 `38. An Horizon is Nothing Save the Limit of Our Sight`／导航 5 条／子项四件齐／块数 8 在 block_target [5,9] 内）· 断言 漏 7（提示 6·跳过 1）· 编 1 提示 · 错 0**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| **L1** 贝克·查尔斯当面向亨利自我介绍（全名／「久闻大名」／握手／「金美英的事我很遗憾」），以及「亨利不认识她」「她与克莱尔、阿尔芭之间那场无声对话」「克莱尔盯着她的古怪强度」「克莱尔身上的桂皮味」——整组未进 md | `:194` ““I’m Beck Charles. I’ve heard so much about you.” Her voice is low-pitched and soft. Her palm is warm but her fingers are cold.”；`:200` “Beck’s eyes dart away from me toward Alba and then Clare.”；`:201` “Clare… staring at her friend with an odd intensity.”；`:185` “she smells of cinnamon.”；`:218` “this woman I don’t know.”；取证 `grep -nE "Beck Charles|查尔斯|肉桂|cinnamon|听说过|不认识"` 于 md → 无输出 rc=1 | 事件进了 md（`人物弧线:14`「克莱尔带着朋友赶来」、导航「贝克赶到」），故不判阻断；但本章对全书的功能（亨利在临终床前与日后取代他的人握手）只剩一个「贝克」，**建议补「久闻大名」一句＋「他不认识她」** | 提示（优先级最高） |
| **L2** 浴袍女主人闹场整场（护士通报「她认为你拿了她父亲的浴袍」→ 亨利当场脱袍被缠住 → 四人一起帮 → 走廊脏话 → 阿尔芭拿金美英的浴袍）未进 md | `:247` “there’s a lady who’s raising a fuss because she thinks you have her father’s bathrobe.”；`:253` “it entangles me like a straitjacket”；`:254` “What the fuck are they doing in there?”；`:255` “Alba brings a bathrobe that I recognize as Kimy’s” | 全章唯一滑稽拍、也是「屈辱」线的落点；删掉不伤主线 | 提示 |
| **L3** 「她不会再说话了，但她也许还听得见你」／「还能多久」「Not long, now」／他报出姓名与家里电话求护士打给克莱尔 | `:147` ““She won’t speak again. But she may still be able to hear you.””；`:156` “He says, “Not long, now.” I ask him again to call Clare. He says he already has.” | 缺「还听得见」这一句，中段他不停说话、唱歌就没有动机 | 提示 |
| **L4** 金美英的旧伤与恩情（女儿 Min 七岁死于白血病；她怎样安慰童年的他；她看透他父亲仍是好友；她当年欢喜地接纳克莱尔） | `:101` “Her daughter, Min, lost to leukemia at seven… I think of how we all love her, unreservedly.” | 这段是守夜的全部内容，也是末句「我们全都毫无保留地爱她」的依据；md 只留 `unreservedly` 一个词条与例句 | 提示 |
| **L5** 他对自身死亡的预感与对穿越的新解释（死会像龙卷风追上他；这些日子更随机也更有目的；「现在我在我该在的地方」） | `:164` “I won’t die of old age; my death will catch me up like a tornado and leave me broken and bleeding.”；`:164-165` “in these last days my time traveling feels both more random and more purposeful… But now I am where I’m supposed to be.” | 原句 7 只留「也靠近我自己的尽头」，把「怎么死」「为什么被送来」都收掉了 | 提示 |
| **L6** 她是夜猫子／失眠（半夜两三点摆接龙或床上看书，收音机九点自动响）；七点十五分的斜光像假血色；他唱她小时候唱过的圣歌 | `:160` “Kimy was always a night owl, an insomniac… It’s seven fifteen now and the indirect sunrise falls across Kimy’s face and arms, giving her a warm complexion that seems like a flush of false health.” | 侧写与光线，不承载事件（但日后对「七点十五／七点半」的时序要记得原文给了两个时刻） | 跳过 |
| **L7** 抬头四人年龄（Henry 43／Clare 43／Alba 13／**Beck 38**） | `:18` “Sunday, December 14, 2014 (Henry is 43, Clare is 43, Alba is 13, Beck is 38)” | 日期对；年龄零命中。**Beck 38 是全书唯一给出她年龄处**，且说明她与克莱尔同龄 | 提示 |
| **F1** 块 2 读者视角「他坐在**偷来的**轮椅上」 | `:58-59` “Fortunately the wheelchairs are only across the corridor… Finally I manage it.”（坐上去，未言偷）；被偷的只有浴袍（`:53`） | 行文顺手加码，与浴袍形成两笔「赃物」 | 提示 |
| 8 块引语逐字（8/8 段 ok，pos 145/3698/3929/4388/8641/12350/12676/14696） | 例：`:19` 块 1 起 “I wake up in the future again…”；`:69` 块 6 起 “What thou gavest thou takest not away, O Lover of souls…” | 逐字命中，无一段查无、无空引号 | 已核实 |
| 六块姓名板逐字（Rasmussen / Hartford / Chopra / Abramovitz / Kim Ji-woo / Kim Mi-young）与中文译名一一对应 | `:64` “Rasmussen . . . Hartford . . . Chopra . . . Abramovitz . . . Kim Ji-woo . . . Kim Mi-young.” | 六个名字，md 块 2 中文理解六个译名，顺序一致，`金美英` 对应 `Kim Mi-young` 正确 | 已核实 |
| 祷文归属与内容 | `:233` “Beck bows her head and reads: “‘We give them back to thee, dear Lord…’”” | 念者是贝克；md 引语虽从 “What thou gavest…” 起（省了开头两句），但读者视角（`:77`）交代了克莱尔先征求许可、贝克从大衣口袋掏出小本子，引语选段未失上下文 | 已核实 |
| 「Kimy was sweet」的过去时判定 | `:170` “tells me that she’s sorry, that Kimy was sweet. She turns off the machines.” | md 块 5「用的是过去时——死亡先由语法确认」（`:65`）——原文确为 was，判断成立 | 已核实 |
| 词汇表 14 条例句逐字 | `:23` insubstantial／`:34` undignified、disguise、diaper／`:39` humiliations／`:69` bluish-gray／`:101` unreservedly／`:43` orderlies／`:64` amputated／`:53` hesitate、curtains／`:58` bathrobe／`:116` son／`:170` bedding | 全部回原文命中，含标点，无一改写 | 已核实 |

## 已核实为正确（防下一轮误修）

1. 日期别改：**2014 年 12 月 14 日星期日**（`:18`），不是 12 月 4 日；「凌晨」对应钟面 **3:20**（`:83`），不是三点整。
2. 「金美英」＝**Kim Mi-young**（`:64`），不是 Kim Ji-woo（金智友，同行另一位病人）。两位 Kim 不可互换。
3. 「我是她的儿子」是**亨利**说的（`:116`），且原文紧跟一句「感到这话是真的」——md 词汇表 `son` 例句保留了这一句，勿删。
4. 「因为我已经死了」是**亨利**对护士说的（`:124`），护士的回话是 ““Very funny,” … “Seriously, I’m going to have to ask you to leave.””——**不是**护士先讽刺他死。修导航那句时别把说话人挪走。
5. 关机器的是**另一位（女）护士**（`:170`），不是男护士、不是克莱尔；男护士（`:110`）只做检查、打电话、说「她不会再说话了」。
6. 祷文作者是 **William Penn**（`:222` “It’s by William Penn, you know, who founded Pennsylvania?”）——md 写「威廉·佩恩」正确，**不是** George Fox、不是贵格会无名氏。
7. 金美英的宗教自述是原文的玩笑：「**a Catholic Buddhist, or a Buddhist Catholic** as the mood took her」（`:228`）——md 译「天主教佛教徒，或者佛教天主教徒，看心情」，两个顺序都保留，正确，勿「改正」成一个。
8. 「借出时间」（`:265` “lend my time to Kimy”）是**亨利**对自己这次穿越的定性，不是克莱尔的安慰话；末句主语别换成克莱尔。
9. 阿尔芭最后那声「爸——？」（`:265` “Alba says, “Dad—?””）是**唤醒**，不是惊呼；原文没有感叹号，md 用破折号，贴合。
10. 本章是**亨利第一人称**（`:23` “Henry: I wake up…”），克莱尔与阿尔芭在本章没有内心视角；块 8 中文理解把「他心里想」写清楚是对的，勿改成全知。
11. 块数 8、H1 带 `38.` 编号、导航 5 条——均符合本书主流形态（机器层 form 已核），块数 8 在 block_target [5,9] 内，不是缺陷。
