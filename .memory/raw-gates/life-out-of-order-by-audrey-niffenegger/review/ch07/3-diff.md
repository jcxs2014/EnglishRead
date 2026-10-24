# ch07 Mayday — 对账（R3）

素读：`1-suread.json`（8 条，锚点脚本核对 8/8 命中）
机器层：`2-machine.json`，rc=0，verdict=ok，10 块 / 3593 words / segments 11 / 查无 0 / 空引号 0 / 子项缺 0 / 关键词缺 0 / 形态偏离 0；`block_hint`：「块数 10 偏离本书常见区间 3–9」（仅提示，`issues.block_count` 为空）
精读：`ch07 mayday.md`（153 行，10 个引语块）

## 一、漏（素读有 / md 无）

| # | 素读条目 | 原文（text/ch07_mayday.txt） | md 对应 | 判 |
|---|---|---|---|---|
| L1 | 第 4 条：年长的 Alba 曾告诉 Caralora 她在等谁、何时出现、要吃哪些苦，原话是「去过你的日子，但 **2041 年**要空着」；Alba 算出那是十八年后，愤怒（「Beast in the Jungle」），Caralora 回「你救过我的命，你不是轻率地告诉我的」「到时候问未来的我」 | 109: “You basically said, go ahead and live your life, but be available in 2041.”　113: “That’s eighteen years from now.” I feel intense disapproval of my older self.　122: “That’s some serious Beast in the Jungle shit right there.”　127: “You saved my life; you didn’t tell me frivolously.” | **全篇零命中**（`grep -n "2041\|十八\|18 年" ch07 mayday.md` 退出码 1，无输出）。四个块（原句 1–10）无一覆盖；导航 :11 只写到「两人只是互相搭把手」就转场 | **阻断**：这是本章唯一的时间旅行揭示（Caralora 为什么「在等」），且它正是 Alba「不肯说未来」这条律法的反例；无块、无导航、未写取舍理由 |
| L2 | 第 1 条：今年派对临时顶上的原因——Charisse 的母亲摔断髋骨，Charisse、Max、Joe、Rosa 四人去了马尼拉 | 23: “But last week Charisse’s mom fell and broke her hip, and Charisse, Max, Joe and Rosa have gone to Manila to help her out, leaving the rest of us scrambling.” | 导航 :11 只写「第 50 选区的五月节派对散场」；`grep -n "马尼拉\|Manila\|髋"` 零命中 | 提示（解释 Rosa/Max/Joe 缺席，非本章转折；但缺了它「五个人」的构成无来处） |
| L3 | 第 2 条：Caralora 拒饭局的理由——今晚开回 Ann Arbor，周三搬新家、还没打包完；她是被「全员出动」叫来的 | 50: “I would love to, but I should hit the road. I’m driving back to Ann Arbor tonight.”　57: “but I’m moving to a new place on Wednesday. I haven’t finished packing.” | 零命中 | 提示（细节，人物弧线里只留了「愿意为 Bette 挪地方」） |
| L4 | 第 6 条：清单的由来——11 岁与 Rosa 争吵时说了「不可反驳因为是真的」的话，被 Gomez 听见后来追问，她就说了；她说此后立了更严的规矩（「你让我变得谨慎」）；以及「That list is just the answers, without the steps.」 | 275–295（“When I was eleven I was trying to win an argument with Rosa…”）　340: “That list is just the answers, without the steps.” | 「答案没有步骤」只出现在词汇表例句（:146），未进块；11 岁那段零命中 | 提示（解释 Alba 为何自责、为何拒给来源；无块但导航交代了「早年口述的清单」，因果未断） |

## 二、编（md 有 / 原文无）

| # | md 断言 | 原文 | 判 |
|---|---|---|---|
| — | 未发现凭空出现的情节、关系或数字 | — | 无 |

## 三、错（两边都有 / 不一致）

| # | md 断言 | 原文逐字 | 判 |
|---|---|---|---|
| E1 | :11「两人**只是**互相搭把手」；:13「门口那句『我要跟人住了』**不是恋情公布**」 | 85: ““I thought you meant you were in a relationship,” I say, disappointed.”　89: ““Oh, we are, kind of,” Caralora says.” | **阻断**：原文明确「算是（kind of）在一起」，md 导航用「只是」抹掉这半句，且与本书自己的原句 3 中文理解（:41「Caralora 承认两人『算是』在一起」）自相矛盾。改法：「两人算搭伙，也算在一起（kind of）」 |
| E2 | 原句 2 中文理解 :31「到了 Gomolinskis 家的**后门**，Lucinda 一溜烟穿过**院门**、蹦上台阶」 | 69: “We’ve arrived at the Gomolinskis’ **back gate**. Zach unlatches it… Lucinda sails through and skips to the **back door**.” | 提示：到达处是后院**院门**（back gate），穿过院门才到后门；md 把到达点写成后门，顺序颠倒。不影响情节 |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句 | 三问 | 判 |
|---|---|---|---|---|
| 1 | 24–26 行 干活清单→五个人走小巷 | 是 | 主语＝Alba 与四人＋工作人员；受事＝椅子/饮食/垃圾；「五个人」的成员 md 未列，但名单在引语里 | 通过 |
| 2 | 69 行 Lucinda 穿门→Caralora 收口说「我要跟人住了」 | 是（地点小错见 E2） | 主语＝Lucinda（穿门）／Caralora（改口）；受事＝那句没说完的回嘴；「他」＝Zach（Ladies first），md 写「对方」，未错挂 | 通过 |
| 3 | 89 行 “Oh, we are, kind of… I guess I’m lonely.” | 是 | 主语＝Caralora；受事＝Bette（被说成 drowning）与「我自己」（lonely）；quietly, to me 的**听者＝Alba**，md 未把听者写成 Zach | 通过 |
| 4 | 214–216 行 牙套／未来已到／智齿袋 | 是 | 主语＝Lucinda（笑）＋Alba（看、想起）；受事＝牙、袋子；「她给**我**、为 Isadora」方向正确（Lucinda → Alba） | 通过 |
| 5 | 299 行 “Climate change… That is a list of dates and events…” | 是 | 主语＝Alba；受事＝文件夹（被挥手赶）；md「先挥手再说话」与原文语序一致 | 通过 |
| 6 | 358 行 “Gomez, you want to feel important…” | 是 | 主语＝Alba（说）／Gomez（被说）；受事＝Gomez 的动机与那张单子；md 未把指责方向搞反 | 通过 |
| 7 | 362–363 行 Zach 想走→「没人把我绑在椅子上」 | 是 | 主语＝Zach；受事＝椅子/自己；「Alba 和 Gomez 忘了我」是 Zach 的猜测，md 用「疑心」保留了这个不确定 | 通过 |
| 8 | 438–439 行 母亲多次濒死→十六岁结扎 | 是 | 主语＝Gomez（转述）／Alba 的母亲（濒死）／Alba（结扎）；受事＝Alba 的身体；「She and Alba decided」＝母女二人共同决定，md「母女俩因此认定」正确 | 通过 |
| 9 | 544–545 行 母亲不敢留她与父亲独处→当不了家长 | 是 | 主语＝Alba 的母亲（看管）／Alba（判断）；受事＝Alba；could never ≠ didn't，md 特别点出，正确 | 通过 |
| 10 | 562 行 “Because I am a coward…” | 是 | 主语＝Alba；受事＝她自己（定罪）、Zach（被她想象成提出分手的人）；md「抢在对方开口前给自己定罪」是解读，可回溯到 might have decided differently | 通过 |

> 密度：10 块均非字面复述，且未越到全书主旨；块 6/7 把「动机之争」与「退场」分工清楚。

## 五、已核实为正确（防下一轮误修）

1. **抬头 `Alba is 22, Zach is 23`（2024 年）**：`text/ch07_mayday.txt:18` 原文如此；md :11 照抄，未据此推算全书年龄线（与 ch06 的 `Alba is 42` 并存，属原书自相矛盾，不计缺陷）。
2. **「十七岁」Lucinda**：`:196` “I thought you were seventeen now?”；md :14 写十七岁，成立。Lucinda 说「只差五岁」与 Caralora 22 岁对得上。
3. **「Zach 第一人称」切换**：`:230` “Zach: I can feel Alba watching me.” 起至章末均为 Zach 叙述；md :15 的「前半是 Alba 的第一人称」成立（切换点描述略含糊，见提示 P5，非错）。
4. **15 条词汇例句**：脚本逐条在 `text/ch07_mayday.txt` 内整串命中（`rows=15 miss=0`），无跨章搬句、无改写。
5. **「All of it has happened」**：`:312` 原文；md :11 译「清单上的事全都已经发生」，未加码成「不可改变历史」之类原文没有的断言。
6. **「Bette 是 premed、有孩子、又怀一个、丈夫走了」**：`:79` 原文四要素齐全，md 未添「离婚」「寡妇」等原文没有的措辞。
