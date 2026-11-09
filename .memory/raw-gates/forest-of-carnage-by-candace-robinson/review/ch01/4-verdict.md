# ch01 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句3 的分析指涉引语外内容（“她还爱着你，可话没说完就断了”“句末的 but—”） | `text/ch01_chapter_one.txt:37` | 引语扩至 but—（原文续句） | 阻断 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 10 条逐条比对

## 已核实为正确（防误修）

- 十四岁 / 无父 / 母亲收钱陪床：`text/ch01_chapter_one.txt:34` 原文 `she was only fourteen years old` —— 回原文核对成立，后续不得以“读着不对”改动
- 外婆被撕碎：`text/ch01_chapter_one.txt:0` 原文 `her arm and leg were torn clean off` —— 回原文核对成立，后续不得以“读着不对”改动
- 结尾立誓包括王子：`text/ch01_chapter_one.txt:306` 原文 `Including the prince` —— 回原文核对成立，后续不得以“读着不对”改动
