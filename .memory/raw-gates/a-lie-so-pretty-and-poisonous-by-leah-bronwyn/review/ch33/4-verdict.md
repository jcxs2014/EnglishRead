# ch33 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（12 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句5 为什么这样写：`elixir` 与 ch20 的 tincture 假说并轨 | tincture 假说在 ch16（We drank tinctures…）；同章 ch33:64 已正确写 ch16，本条为同章内自相矛盾 | 已修复 → `elixir` 与 ch16 的 tincture 假说并轨 | 阻断（已整改） |

## 已核实为正确
- compeller → text/ch33 'I'm a compeller. I can make anyone do anything I want.'
- Alec=药水+撞穿屏障 → text/ch33 'I was able to knock both her and the youngling off and through the barrier'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
