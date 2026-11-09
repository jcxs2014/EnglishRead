# ch20 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句4 读者提示“十九天”为无据数字 | `text/ch20_chapter_twenty.txt:0` | 中间隔着一整段从笼子到婚床的距离 | 阻断 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 13 条逐条比对

## 已核实为正确（防误修）

- virginity：`text/ch20_chapter_twenty.txt:22` 原文 `lost his virginity` —— 回原文核对成立，后续不得以“读着不对”改动
- before he could stop himself：`text/ch20_chapter_twenty.txt:37` 原文 `before he could stop himself` —— 回原文核对成立，后续不得以“读着不对”改动
- 摘钥匙：`text/ch20_chapter_twenty.txt:190` 原文 `plucked the dangling key` —— 回原文核对成立，后续不得以“读着不对”改动
