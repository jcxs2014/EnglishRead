# ch23 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句10 为什么这样写误加“drawl”（原文该句无此标记） | `text/ch23_chapter_twenty_three.txt:172` | 关门的动作让告白与告别同时完成 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 抽脊令：`text/ch23_chapter_twenty_three.txt:25` 原文 `tear the wolf’s spine out` —— 回原文核对成立，后续不得以“读着不对”改动
- 杀母真相：`text/ch23_chapter_twenty_three.txt:64` 原文 `your grandmother murder my mother` —— 回原文核对成立，后续不得以“读着不对”改动
- 无圆满结局：`text/ch23_chapter_twenty_three.txt:172` 原文 `don’t get happy endings` —— 回原文核对成立，后续不得以“读着不对”改动
