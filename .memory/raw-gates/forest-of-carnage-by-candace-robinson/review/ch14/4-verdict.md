# ch14 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句6 夹生英文（椅 lap） | `text/ch14_chapter_fourteen.txt:25` | 笼子、大腿、谈判做框架 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（10 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 14 条逐条比对

## 已核实为正确（防误修）

- 两支箭：`text/ch14_chapter_fourteen.txt:52` 原文 `left her two arrows` —— 回原文核对成立，后续不得以“读着不对”改动
- 四队出局：`text/ch14_chapter_fourteen.txt:88` 原文 `Four teams were out` —— 回原文核对成立，后续不得以“读着不对”改动
- 拧断 Micah：`text/ch14_chapter_fourteen.txt:189` 原文 `snapped his neck` —— 回原文核对成立，后续不得以“读着不对”改动
