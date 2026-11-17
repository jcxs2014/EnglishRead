# ch03 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（12 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句6 关键词：parallel to the barrier / parallel to the barrier | 批修残留重复词；新词均在本块首段 | 已修复 → parallel to the barrier / small, worn path / broke the heavy silence | 提示（已整改） |
| 原句8 关键词：Horses / Horses / turned to me | 同上；首段仅两句，收敛为两词 | 已修复 → Alec turned to me / Horses | 提示（已整改） |
| 原句9 读者视角提示：对照 ch00 的跳车心境 | 取证：/usr/bin/grep -l 'finish our story' text/*.txt → 仅 text/ch03_chapter_3.txt 命中；ch00 无跳车 | 已修复 → 对照本章坠落段的自我说服 | 阻断（已整改） |
| 原句12 为什么这样写：与 ch01 那双 cold, grey eyes | 取证：/usr/bin/grep -lc 'Cold, grey eyes' text/*.txt → 仅 text/ch00_prologue.txt:1 | 已修复 → 与 ch00 开篇那双 cold, grey eyes | 阻断（已整改） |

## 已核实为正确
- 'finish our story' 自我说服在本章 → grep 仅 text/ch03
- hazel eyes 母女同色 → text/ch03 'glassy hazel eyes that matched mine'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
