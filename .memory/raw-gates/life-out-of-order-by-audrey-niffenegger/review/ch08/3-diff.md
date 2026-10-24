# ch08 Election Day 2024 — 对账（R3）

素读：`1-suread.json`（8 条，锚点脚本核对 8/8 命中）
机器层：`2-machine.json`，rc=0，verdict=ok，3 块 / 602 words / segments 4 / 查无 0 / 空引号 0 / 子项缺 0 / 关键词缺 0 / 形态偏离 0；`issues` 全空，无 `block_hint`
精读：`ch08 election day 2024.md`（82 行，3 个引语块）

> 结构提示：112 行原文、8 条素读，只有 3 块（开头投票 / Celia 与 Lucinda / 结尾出门）。**中段（观票派对缺席→门口痛哭→寿司之夜→天亮列清单→烧纸）整段无块**，只活在本章导航与一句话总结里——这是本章最大的形态偏轻处，见 P1。

## 一、漏（素读有 / md 无）

| # | 素读条目 | 原文（text/ch08_election_day_2024.txt） | md 对应 | 判 |
|---|---|---|---|---|
| L1 | 第 5 条后半：Zach 的「任何事」有两条边界，「不吃人、不牵扯孩子」；她问「你想保留多少选择的幻觉」，他答「一点也不要——我不想提前感到悔恨」 | 62: “Well. Not cannibalism. Nothing involving kids.”　66: “Understood. How much illusion of choice would you like to preserve?”　70: “None,” he says decisively. “I don’t want to feel the remorse in advance.” | 三块全无；导航 :11 只写「让她吩咐他做任何事」；`cannibalism` 仅作词汇表词条（:56）出现 | 提示：这段是本章的道德核心（他自愿交出选择权、拒绝预先悔恨），无块、导航亦无一字；建议至少并入导航。`grep -n "illusion\|remorse\|cannibalism" "ch08 election day 2024.md"` → 仅 :56 命中词汇行 |
| L2 | 第 3 条：观票派对的**地点**是 Celia 与 Lucinda 家 | 35: “Tonight there’s a watch party for the returns **at their place**. Mama and Beck are going.” | 导航 :11「晚上有一场为开票办的 watch party，Mama 和 Beck 都去」——未交代在哪、也未交代是 Lucinda 家的场子 | 提示：这正是她整晚回避的场合，也是「安慰 Lucinda」的兑现现场；归属一缺，:11 的「她对他们说自己去陪 Zach」就失去了对象（他们是去 Lucinda 家） |
| L3 | 第 6 条：清单的两类来源——「有些是你和 Gomez 自己做的、我只知道日期」 | 74: “There are some that you and Gomez did on your own, all I know is the dates.” | 导航 :11「写下确定知道的那些和只有日期的那些」——保留「只有日期」，丢掉「你和 Gomez 做的」 | 提示：无块，导航略去主语，不构成事实错误 |
| L4 | 第 7 条末：她说「这会是一段狂野的旅程」，他答「好」 | 104: “It’s going to be a wild ride.”　108: “Okay.” | 零命中 | 提示（收束句，可有可无） |

## 二、编（md 有 / 原文无）

| # | md 断言 | 原文 | 判 |
|---|---|---|---|
| E1 | :13「烧清单的仪式发生在水槽里，**火很小，烟要用水冲走**」 | 95: “I… burn the paper in the sink. “Don’t mention this to anyone,” I insist.” | 提示：原文只有「在水槽里烧掉」；「火很小」「烟要用水冲走」是加出来的物理细节，不可逐字回溯。不影响情节，但属演绎（同 ch06 甜筒条的处理口径） |
| — | 其余未见凭空出现的情节、关系、数字 | — | 无 |

## 三、错（两边都有 / 不一致）

| # | md 断言 | 原文逐字 | 判 |
|---|---|---|---|
| E2 | :12「哭不是为结果，是「poker face」**终于不必维持**」 | 35: “I ring the doorbell, Zach answers, I burst into tears, he pulls me into the house and embraces me. **So much for keeping a poker face.**” | 提示：原文是「本想端着，结果当场破功」——poker face 是**失败**了，不是「不必维持」；md 把「破功」读成「解脱/不必再演」，因果方向偏了半格。可辩护（在 Zach 面前确实不用演），故不判阻断，但措辞宜改「没能端住」 |
| E3 | 原句 3 中文理解 :41「外面一个人也没有」 | 112: “The sun is barely up… We dress in silence, let ourselves out. **There’s no one in sight**, the streets are empty.” | 通过（范围限街道，md 未扩成全市空无一人） |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句 | 三问 | 判 |
|---|---|---|---|---|
| 1 | 23 行 世界翻页／邮寄投票／亲友不问却觉出绝望 | 是 | 主语＝世界（翻页）／Alba（投票、推断）；受事＝她自己（躲开「见任何人」）；`they sense` 的主语是亲友，md「亲友…确信」写成「她确信他们感觉得到」——归属正确（原文 `I'm sure they sense`） | 通过 |
| 2 | 28–30 行 只告诉 Celia／Lucinda 十八岁首次投票／美国辜负我们 | 是（省略号跳过 DNC 与「在她们家」的场合，中文亦未补，与引语等长） | 主语＝Alba（告诉）／Celia（被交付任务）／Lucinda（期待）；受事＝那个「结果」与 Lucinda 的兴头；`the first Black female major party presidential candidate` 是**候选人**，md「这一届有第一位…候选人」未误挂成 Lucinda 本人 | 通过 |
| 3 | 112 行 空街／无鸟鸣／牵手进未来 | 是 | 主语＝we（两人）；受事＝城市与未来（被走进去）；md「他们没有解释也没有安慰」是解读，未越到作者生平/全书主旨 | 通过 |

> 密度：3 块都不止复述字面，块 2 把「交给第三方保管」讲透，块 3 抓住「写没有」的句法。

## 五、已核实为正确（防下一轮误修）

1. **抬头年龄**：`:18` “Tuesday, November 5, 2024 (**Alba is 23, Zach is 23**)”——两人同为 23 岁，md :11/:82 均写「二十三岁」，未与 ch07（22/23）冲突（跨年正常）。**注意**：本章不与 ch06 的 `Alba is 42` 相涉，md 未据此推算任何年龄。
2. **`Alba:` 声部标签**：`:23` 句子以 “Alba:” 起，md :15 写「日期抬头加『Alba:』声部标签」，成立。
3. **Lucinda 的年龄与「第一次投票」**：`:29` “she’d just turned eighteen, this is the first election she can vote in”；md 未把「刚满十八」扩写成「十八岁生日就在这几天」。
4. **14 条词汇例句**：脚本逐条整串命中 `text/ch08_election_day_2024.txt`（`rows=14 miss=0`），含 `embraces`（:68 用原句 “embraces me”）、`decisively`（:58）、`rhapsodizing`（:55），无跨章搬句、无改写。
5. **结果始终不被说出**：md 全篇未写谁赢（`/usr/bin/grep -niE "won\|win \|trump\|harris\|当选\|赢了|民主党的候选人赢了" "ch08 election day 2024.md"` 退出码 1、零输出），与原文一致——这是本章的写作机关，md 没有破它。
6. **午夜脚步声的主语**：`:40` “I hear Charisse and Gomez come home around midnight.”；md :11 写「午夜听见 Charisse 和 Gomez 回家」，未误写成 Celia 或 Lucinda。
7. **「买枪」是她添的、不是 Zach 提的**：`:83` ““This is all defense. What about offense?””（Zach 问）→ `:87` “I add a few things to the list. “Buy a gun and learn to use it,” I tell him.”；md :11「又添了一条『买枪、学会用』」——主体与方向正确。
