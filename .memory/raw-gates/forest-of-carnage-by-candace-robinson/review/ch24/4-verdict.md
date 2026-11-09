# ch24 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句4 英文引用截断（which was why he'd planned to use surprise） | `text/ch24_chapter_twenty_four.txt:160` | “he’d planned to use the element of surprise” | 提示 |
| 原句10 为什么这样写误加“拖着调子”（原文该句无此标记） | `text/ch24_chapter_twenty_four.txt:178` | 语气却轻描淡写 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（10 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- patricide 顾虑：`text/ch24_chapter_twenty_four.txt:34` 原文 `couldn’t look like patricide` —— 回原文核对成立，后续不得以“读着不对”改动
- 红线：`text/ch24_chapter_twenty_four.txt:61` 原文 `the red line trailing` —— 回原文核对成立，后续不得以“读着不对”改动
- 按水为止：`text/ch24_chapter_twenty_four.txt:163` 原文 `held it there` —— 回原文核对成立，后续不得以“读着不对”改动
