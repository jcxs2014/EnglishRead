# ch32 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（10 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句1 读者视角提示：对照 Cora 在 ch27 的强制观礼 | 强制观礼鞭刑在 ch31（捂住 Cora 耳眼）；ch27 为舞会 | 已修复 → 对照 Cora 在 ch31 的强制观礼 | 阻断（已整改） |
| 原句9 读者视角提示：对照 Gabriel 的白光三次出场（ch09/22/32） | 取证：/usr/bin/grep -l 'white light' text/*.txt → ch05/09/26/32；其中 ch26 是 Rosalyn 的白光非 Gabriel；ch22 无 | 已修复 → 对照 Gabriel 的白光三次出场（ch05/09/32） | 阻断（已整改） |

## 已核实为正确
- covenant 三天无痕死 → text/ch32 'a painful, unseen death that lasts for three days' time'
- audioperceptive → text/ch32 'I am audioperceptive'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
