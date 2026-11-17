# ch26 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（10 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句8 关键词：Why wouldn’t I believe you / preconceived beliefs / hysterics and blasphemy | 块续段缺 > 前缀致 lane ⑱ 仅见首段；keyword3 收敛。 hysterics and blasphemy 确在 text/ch26（grep=1）与引语续段，属工具口径而非内容缺陷 | 已修复 → Why wouldn’t I believe you / preconceived beliefs | 提示（已整改） |

## 已核实为正确
- 鹿衔叶家纹与 ch01 火漆一致 → text/ch01 'a stag with a leaf between its horns' 与 text/ch26 'a crest…of a stag with a leaf'
- 父亲失踪十一年 → text/ch26 'Eleven years this past spring'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
