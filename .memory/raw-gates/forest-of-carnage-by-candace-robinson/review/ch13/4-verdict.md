# ch13 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句8 分析含引语之后的叙述（afoot / 恶毒游戏） | `text/ch13_chapter_thirteen.txt:157` | 引语扩至 He had to be coming up with another vindictive game of his own. | 阻断 |
| 原句1 “CFO 式的冷酷记性”为不明缩写 | `text/ch13_chapter_thirteen.txt:37` | 账房式的冷酷记性 | 提示 |
| 原句3 读者提示把 ch01 的 I don’t particularly care 记在 ch02 | `text/ch13_chapter_thirteen.txt:0` | 对照 ch01 他在绞刑场上那句 I don’t particularly care | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 纸鸽是母亲最爱的鸟：`text/ch13_chapter_thirteen.txt:40` 原文 `their mother’s favorite bird` —— 回原文核对成立，后续不得以“读着不对”改动
- 三楼私人房间：`text/ch13_chapter_thirteen.txt:91` 原文 `a private room on the third floor` —— 回原文核对成立，后续不得以“读着不对”改动
- 特例：`text/ch13_chapter_thirteen.txt:205` 原文 `you’re a rarity` —— 回原文核对成立，后续不得以“读着不对”改动
