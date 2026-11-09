# ch08 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句2 中文理解含引语外内容（“而她都符合，只是人生比预期短”） | `text/ch08_chapter_eight.txt:37` | 删除该句 | 阻断 |
| 原句10 中文理解语病（“你我不可能放”） | `text/ch08_chapter_eight.txt:342` | 我不可能放你走，你懂的 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 10 条逐条比对

## 已核实为正确（防误修）

- gracious 回敬：`text/ch08_chapter_eight.txt:16` 原文 `rather gracious` —— 回原文核对成立，后续不得以“读着不对”改动
- 确认独居：`text/ch08_chapter_eight.txt:49` 原文 `he’d made sure of it` —— 回原文核对成立，后续不得以“读着不对”改动
- 三个月禁变身：`text/ch08_chapter_eight.txt:85` 原文 `for three months` —— 回原文核对成立，后续不得以“读着不对”改动
