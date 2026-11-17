# ch21 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（10 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句4 读者视角提示：对照 ch01 的粉裙（母亲的颜色） | 取证：/usr/bin/grep -l 'my mother’s chosen color' text/*.txt → 仅 text/ch09_chapter_9.txt；ch01 无粉裙 | 已修复 → 对照 ch09 的粉裙（母亲的颜色） | 阻断（已整改） |
| 原句9 关键词：mare spooks so easily, find her | 逗号会被关键词切分器拆开，收敛为单词组 | 已修复 → mare spooks so easily | 提示（已整改） |

## 已核实为正确
- enchant 从未看错 → text/ch21 'And my enchant has never been wrong.'
- 血裙入火 → text/ch21 'tossed it into the lit fireplace'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
