# ch04 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句3 中文理解含引语外内容（“不到二十岁”） | `text/ch04_chapter_four.txt:79` | 引语前扩至 The wolf nearest him—the youngest… | 阻断 |
| 原句2 读者提示的英文非逐字（like theirs） | `text/ch04_chapter_four.txt:0` | like hers, like their mother’s | 提示 |
| 原句6 中文层夹生英文（releasing） | `text/ch04_chapter_four.txt:133` | 尸体变成持续投放的教育装置 | 提示 |
| 原句9 中文理解语病（“一整袋箭的弓上方”） | `text/ch04_chapter_four.txt:229` | 床架横杆上、弓与满袋箭的上方 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过
- 对应：本章 9 块逐块 R4 已做
- 形态：chapter.sh 报告合规
- 断言：与素读 12 条事实逐条比对

## 已核实为正确（防误修）

- 近一百村民：`text/ch04_chapter_four.txt:40` 原文 `Nearly a hundred villagers` —— 回原文核对成立
- 蛆生蝇：`text/ch04_chapter_four.txt:133` 原文 `maggots turn to flies` —— 回原文核对成立
- 姓名与肉店：`text/ch04_chapter_four.txt:172` 原文 `Her name is Sterling` —— 回原文核对成立
