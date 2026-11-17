# ch24 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（7 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句5 关键词：I’ll think about staying / staying / My mother would love him | 关键词与词头部分重叠 | 已修复 → I’ll think about staying / My mother would love him | 提示（已整改） |

## 已核实为正确
- 求缘献血 → text/ch24 'praying to Themis steadily this past year…I have shed a lot of my blood at his altar'
- MEAD 书来自西谷民兵 → text/ch24 'confiscated it from one of the militia members'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
