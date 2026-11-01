# ch01 Introduction 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，6 块 / 引语 9 片段查无 0；`quotes.py verbatim --full` 与 `verify_fragments_indep` 均 0 MISS。

## 逐块对应（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

| 块 | 引语落位 | 中文是否讲这句引语 | 关键词是否在引语/本章 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 原句 1 | :15 | 是：really 连用＝口头加重，不迟疑 | better / really ✅ | 说话人＝作者本人 ✅ | 提示：`really` 连用的“郑重滑稽”属解读，可接受 |
| 原句 2 | :18 | 是：研究背书→把人连起来 | endless / immune / unites ✅ | 动作主语＝研究/幽默 ✅ | 通过 |
| 原句 3 | :21 | 是：独木舟＝工具 | useful / canoe / functional ✅ | 受事＝好笑话 ✅ | 通过 |
| 原句 4 | :24 | 是：库存与三类坏法 | corny / predictable / contrived / wilfully ✅ | 主语＝本书/讲述者（wilfully）✅ | 通过 |
| 原句 5 | :27 | 是：额外一层与“勉强好笑” | extra / slightly / situation ✅ | 主语＝坏笑话；场面由讲述者造 ✅ | 通过 |
| 原句 6 | :36+:39 | 是：自证式坏双关 | kayak / heat ✅ | 主语＝读者（you can have）✅ | 通过 |

## 断言核对

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 字符数约 1,727 | text/ch01_introduction.txt 全文 1,727 字符（末条 char_range 止于 1726） | 正确 | 通过 |
| 700-ish jokes | text/ch01_introduction.txt:24 | 正确（作者自述约数，md 未越级断言） | 通过 |
| 三类坏法 | text/ch01_introduction.txt:24 | 正确 | 通过 |
| 免疫系统等研究背书 | text/ch01_introduction.txt:18 | 正确 | 通过 |
| 结尾 kayak/heat 改写 have your cake and eat it too | text/ch01_introduction.txt:39；原习语未在原文出现，md 写明“改写” | 正确（已用“改写”而非“原文”） | 通过 |

## 已核实为正确

- 「热水袋加在独木舟上」：`text/ch01_introduction.txt:33` 原文 “if a joke is a canoe, the badness of a bad joke is a luxurious hot water bottle that makes your canoeing journey warmer and more pleasant.” —— md 复述一致，不是杜撰。
- 「groan / moan 同源」：`:30` “People groan in agony, sure, but they also moan in ecstasy.” —— md 未写成“作者说两者同词”，只写“同一条生活法则”，成立。
- 「作者简介在书末」：本章 text 无此内容，md 放在「作者」栏而非正文分析，按元数据处理，不算编。

## 结论

阻断 0 / 提示 1（已补证据行）/ 假红 1。修后 `chapter.sh` rc=0。
