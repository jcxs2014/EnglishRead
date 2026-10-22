# ch27 判定（R4）：`ch27 either mad or a murderer.md`

## 结论

**通过（无阻断，4 条提示）。** 五条「原句」与 24 条词汇例句全部逐字命中 `text/ch27_chapter_27.txt`，弯引号与破折号边界未自补、未跨段；章末「敲门」这个接口与 ch28 衔接正确。问题集中在**时序**与**两处口径不严**，不动事实层，属可改可不改的提示。

## 阻断

（无）

## 提示

1. **md:114 一句话总结｜「她在天亮之前就把自己判了」时序错**。text:8 是 `watching the dawn creep round the blue horizon`，text:26 明写 `the stillness of late morning`，到 text:62 才 `Either I was mad, or I was a murderer`。
   - 建议改为：「她在那个上午把自己判了：不是疯了，就是杀了人」。
2. **md:12 导航一句话｜「天刚亮她就给自己定了案」同上，提前了时间**。建议改为「上午她给自己定了案」或「查完传说她给自己定了案」。
3. **md:18 人物弧线｜「她这一章没有任何外在行动」与本条后半「章末她下楼开门」冲突，且「开门」不在本章**。text:95 止于 `headed downstairs`。建议拆成：「本章她几乎不向外动作（扔手机、查网页、穿衣下楼），真正的对外接触留给下一章」。
4. **md:70 为什么这样写｜「三个分词」实为四个**。text:83：`a creeping darkness, inching up…, climbing over…, clutching at my toes—`。建议改为「四个 -ing 分词」。

（附记，不必改）md:50「作者一个字没动」无法由 `text/` 核实——保留意思即可，别当作可验证事实。

## R4 三问

1. **谁做的**：本章无人被指认。她列的三件怪事——`The figure in the basement`（地下室里的人影）、`The phantom party next door`（隔壁没有人的聚会）、门前 `Knock-knock-knock` 的敲门者——文本都只给现象不给施动者：`There was someone at the door. I had no idea who`（text:92）。她唯一给出的"谁"是假设句 `Maybe it’s her ghost come to punish me for what I did`（text:56），即把施动者指向"她的鬼魂"，而"她"在本章未被点名。
2. **关系与谁欠谁**：本章只落实一条亲缘链——祖母→父亲→她：`she called my father to her house because she felt unwell`（text:71），`My father took her to the hospital that day`（text:74）。"欠"的雏形是她对自己旧事的一句自供 `for what I did`（text:56），但欠谁、欠什么，本章刻意不交底；md 写「第一次承认自己身上带着一件不能说的旧事」与此吻合，未越界编造。
3. **数字与死因**：死因逐字为 `combined liver and lung cancer`（肝癌合并肺癌，text:71）——不是意外、不是自杀，md:54 与 md:60 都照此写，正确。数字类：临终院在 `an hour away up north`（text:74）；敲门为三下（`Knock-knock-knock`，text:86）；祖母家 `Two cats sat in front of the fire`（text:71，md 未用，不算漏）。md 未出现与 text 冲突的数字。

## 已核实为正确（下一轮不要改坏）

- 五条原句的**逐字**与**边界**：text:8 / 29 / 47 / 71 / 83；特别是不给 `feared—`、`toes—`、`collect—stained` 补 `”`、不补空格。
- 词汇表 24 条例句全部可 grep 命中，含 `screed` 的两个弯引号成对（text:35）。
- 「开篇的光」与「结尾的黑」同一条上升路线（text:8 ↔ text:83）——这是本章最好的读法，勿删。
- 「第二人称'你'」的判断（text:23）成立，是本章叙述手法的一个真观察点。
- 章末只到 `headed downstairs`，不写开门——与 ch28 的分界守得对。
- 祖母死因写法 `combined liver and lung cancer` 与中文「肝癌与肺癌并发」对应无误。
