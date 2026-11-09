# ch13 · R3 对账（漏 / 编 / 错）

- 章：ch13；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch13_chapter_thirteen.txt`（358 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句8 分析含引语之后的叙述（afoot / 恶毒游戏） | `text/ch13_chapter_thirteen.txt:157` 原文 `Something was afoot` | 引语止于 After I taste your cunt. → 引语扩至 He had to be coming up with another vindictive game of his own. | 阻断 |
| 2 | 提示 | 原句1 “CFO 式的冷酷记性”为不明缩写 | `text/ch13_chapter_thirteen.txt:37` 原文 `pressed it into her palm` | CFO 式的冷酷记性 → 账房式的冷酷记性 | 提示 |
| 3 | 提示 | 原句3 读者提示把 ch01 的 I don’t particularly care 记在 ch02 | `text/ch13_chapter_thirteen.txt`（锚点未定位） | 对照 ch02 他对 Caston 的“我不在乎她说什么” → 对照 ch01 他在绞刑场上那句 I don’t particularly care | 提示 |

## 结论

阻断 1 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
