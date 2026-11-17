# ch22 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（12 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句3 读者视角提示：对照 Darragh 的第一次准确称呼她的眼睛（ch19 栗色对 hazel 的镜像） | 编造断言：grep 'hazel' text/ch19_chapter_19.txt → 0 命中，Darragh 从未称呼她的眼色；信写 blue eyes 系原文（text/ch22），blue 是 Gabriel 自己的眼色 | 已修复 → 对照原文的眼色事实（她的 hazel 见 ch03，Gabriel 信里却写成 blue——blue 是他自己的眼色） | 阻断（已整改） |
| 原句6 读者视角提示：对照 ch03 她被 Acrion 甩门羞辱时的隐忍 | 取证：Acrion 仅存在于 ch13（ch03 为告别/穿越章）；且甩门受者是 Darragh 非「她」（text/ch13 'flung the door in Darragh's face'） | 已修复 → 对照 ch13 Acrion 甩门拒 Darragh 于门外时的敌意 | 阻断（已整改） |

## 已核实为正确
- Gabriel 信写 blue eyes → text/ch22 'gorgeous blue eyes'（她的眼为 hazel，反讽成立）
- 父母全名 → text/ch22 'Eliza and Fionn Alwine'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
