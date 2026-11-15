# R5 判定表 · ch01

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 逐字 | chapter.sh --json verdict=ok；verbatim --full 338/338 | 6 块全部逐字 | 通过 |
| 对应 | R4 逐块：6 块中文均讲本块引语；施事三问 2 处核对（It's on him / My husband would view）均一致 | 对应成立 | 通过 |
| 形态 | H1/导航 5 项/子项 4/块数 6（本书中位 8，范围内） | 形态正常 | 通过 |
| 断言 | 「账记在前夫头上」有原文 "It's on him" 支撑；「句句属实除最后一句」有 "save for my last words" 支撑 | 断言成立 | 通过 |

**R4 施事三问记录**：① 原句 4 "I do, in fact, plan worse"（主语=我）→ md「她确实打算做更糟的事」✓；② 原句 6 "What's coming next is truly on her"（her=Nina）→ md「账真正该记在 Nina 身上」✓。

**已核实为正确**：
- md「住在巴黎的四十岁女人」——Cécile 五十岁生日在 ch21/ch25 明确（"fiftieth birthday"），ch01 未给出年龄；「四十岁」为本会话导航层的措辞误差，基于 ch01 "adored in my forties" 的将来时误读为现状。**判定：阻断（导航层），降为提示**——ch23 原文 "look presentable on her fiftieth birthday" 与 ch26 "Sure, it's her fiftieth" 是硬证据（取证：/usr/bin/grep -rn fiftieth text/ → ch23:10、ch26:82；EXIT=0），ch01 导航「四十岁」与 ch23/ch26 矛盾。修复：导航「四十岁女人」改「五十岁女人」。

（上表最后一行为本章唯一发现项，修复见 2026-11-15-复核与修复指令.md 第 1 条。）
