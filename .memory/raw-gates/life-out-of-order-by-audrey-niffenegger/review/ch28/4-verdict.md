# ch28 判定表

机器层 rc=0，8 块（block_target=[5,8]）。人判结论：**漏 7 · 编 0 · 错 3 · 提示 10**；**零阻断**——所有漏都属细节/母题层，本章的关键事件（午饭、握手虚惊、死人问题、浴室记笔记、婚事提问、举杯）全部落在 8 块之内。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 座位/客人位的母题整段没进任何块 | `text/ch28_a_muse_in_the_machine.txt:120`「Which of the seats at this table was his?」`:121`「Probably the one Kimy’s sitting in; mine is the farthest from the kitchen, the one reserved for guests.」；md `/usr/bin/grep -c -F "座位"` → `0`、`"客人"` → `0`、`"guest"` → `0`（rc=1） | 漏：Beck 在这家的位置唯一被写成实物坐标的一句 | 提示 |
| Alba 的「Older Alba 早就告诉我了」与「我不能记得自己不该知道什么」被删 | 原文 `:43`「I guess I thought it would be like we already know each other because Older Alba has been telling me about Beck」；`:44`「I can’t remember what I’m not supposed to know.」；md `"Older Alba"` → `0` | 漏：孩子「早知道结局」的文本依据，缺了它「反转」像作者旁白 | 提示 |
| 数字猫只回答了「在网站里晃」这半句没进 md | 原文 `:109`「She’s not warm and soft, like my cat was. It’s nice to see her wandering around inside my website, though.」；`:105`「So you have a cat zombie?」；md `"zombie"` → `0`、`"website"` → `0` | 漏：提问在、回答缺 | 提示 |
| 九种蓝 / Cerulean Blue /「You keep it」整段不入块 | 原文 `:151`「Soon there are nine different blues. “That one,” I say, handing her Cerulean Blue.」；`:165`「Cerulean Blue next to my spoon」；`:159`「The only thing I’ve painted recently is the walls of my studio」；md `"Cerulean"` → `0`、`"九种"` → `0`、`"颜料"` → `0` | 漏：Beck 重拾画画这条暗线全无 | 提示 |
| 溜冰是「谈得顺利」的奖励（条件句），md 无 | 原文 `:29`「“If things go well with Beck,” she says, “you and Nadia and Colin might be able to go roller-skating later this afternoon.”」；md `"溜冰"` → `0`、`"roller"` → `0` | 漏：孩子视角的紧张从这句开始 | 提示 |
| 马蹄莲、巧克力、pinot grigio、Alba 的 7-Up、冷汤笑话全缺 | 原文 `:70`「Clare puts the calla lilies I brought into a vase…pours herself, Kimy and me each a glass of pinot grigio. Alba has 7-Up, with ice, in a wineglass.」`:72`「we laugh because the soup is vichyssoise」；md `"马蹄莲"`/`"calla"`/`"pinot"`/`"7-Up"` 均 `0` | 漏：宴席只剩炸丸子一道，「这是正式的一顿」的信号消失 | 提示 |
| 导航称「Alba 不追问死亡，也不打听婚事」 | 原文 `:89`「“Can you do that with people? After they’re dead?”」、`:220`「“So, are you going to move in with us and get married now?”」；md 导航 `:13` 原文「反转「孩子不懂事」：Alba 不追问死亡，也不打听婚事，她早已知道结局，不确定的只是时间。」；而同篇总结 `:132` 写「饭桌上 Alba 一路追问」 | 错：**导航与自家总结打架**，且两头都与原文对撞 | 提示 |
| 导航称那句提问「问得满桌安静」 | 原文 `:76`「We eat in silence for what seems like eons.」（沉默在提问**之前**，是等菜时的）；`:89` 提问后接的是 Clare「Did you have someone in mind, sweetie?」 | 错：因果反向——沉默不是被问出来的 | 提示 |
| 原句 4 中文称双手是「她一整晚的骄傲」 | md `:57`「孩子的双手是她一整晚的骄傲」；原文抹甜菜发生在当天上午 `:23`「I got to put the carrots and beets through the food processor…I rubbed the beets all over my hands」 | 错：时间词无据 | 提示 |

**报数（四组）**

- 逐字：8 块 / 8 段引语全部在 `text/ch28_a_muse_in_the_machine.txt` 命中（机器 `segment_miss=0`；手核 `:23`、`:50`、`:211`、`:216`、`:220`、`:285` 起止一致）→ **0 缺陷**
- 对应：8 块全部在讲自己的引语，无一讲引语之外的上下文（详见 `3-diff.md` 第四节）→ **0 缺陷**；块 6 密度稍欠（省掉「在浴缸边偷偷记」这个动作）
- 形态：H1 `28. A Muse in the Machine` ✓、导航 5 ✓、子项 4 齐 ✓、8 块在 [5,8] ✓、块序单调 ✓ → **0 缺陷**
- 断言：编 0；3 条表述与原文/自身不符（上表后三行）→ **错 3（全提示）**

## 已核实为正确（防下一轮误修）

| 看着可疑的写法 | 原文 | 核实结果 |
|---|---|---|
| 「八岁孩子问『你要不要搬进来跟我妈妈结婚』」 | `:220`「“So, are you going to move in with us and get married now?”」 | 原文无「跟我妈妈」，但 Alba 是对 Beck 说话、婚配对象只能是 Clare ⇒ **合理补足，不算编，不必改** |
| 原句 3 中文「不是她那一晚在俄式餐厅见到的成年女子」 | `:50`「who of course is a young girl, not the woman I met that night at the Russian restaurant」 | **正确**：那位成年女子是未来的 Alba（Older Alba），不是 Clare。别改成「Clare 年轻时」 |
| 全章用「她」指 Beck，包括「探出头看她」「把手放进她掌心」 | `:50`「Alba steps forward and places hers in mine…I recoil」 | **正确**：本章 Beck 视角、全书统一写「她」；「她掌心」＝Beck 的手，受事方向对，别改成「Alba 的掌心」 |
| 「Kimy 与 Clare 退到旁边，只在她失言时递一个眼神」 | `:222`「“Alba,” Kimy says, warningly.」`:224`「Clare regards her daughter with horrified appreciation」 | **正确**：警告确由 Kimy 发出，Clare 是「又惊又佩地看」 |
| 「灵感来时 Beck 躲进浴室记笔记」 | `:216`「I grab my handbag on my way to the bathroom. I sit on the side of the tub, take out my phone and start making notes」 | **正确**：地点是浴室浴缸边，工具是手机 |
| 「最后三个人举杯」 | `:285`「Kimy expresses…three red-purple drinks on a tray」 | **正确**：Kimy/Clare/Beck 三人 |
| 「Alba 这一章几乎不变，始终是知道太多、必须装作不知道的孩子」 | `:44`「I can’t remember what I’m not supposed to know.」 | **方向正确**：原文确有「装作不知道」的依据（只是那句本身没进 md，见漏 L1 组） |
