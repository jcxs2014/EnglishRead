# ch15 · R3 对账（漏 / 编 / 错）

- 章：ch15；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch15_chapter_fifteen.txt`（319 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句12 读者提示伪造 ch12 引语（his eyes glowed with their own cruelty 只在 ch15 出现） | `text/ch15_chapter_fifteen.txt:295` 原文 `glowed with their own cruelty` | 对照 ch12 “his eyes glowed with their own cruelty”的 Winter 版本 → 删去伪造引语与章号，只保留父子同源的判断 | 阻断 |
| 2 | 提示 | 原句1 读者提示悬空分号 | `text/ch15_chapter_fifteen.txt:16` 原文 `striking the shifter between its golden eyes` | 她的枪法曲线在这场游戏里被拉到顶； → …拉到顶。 | 提示 |
| 3 | 提示 | 原句11 夹生英文（her words hit something） | `text/ch15_chapter_fifteen.txt:271` 原文 `Silence. You’ll speak only when I tell you to speak` | her words hit something——他失控的前兆被动词出卖 → 她那句话扎到了他——失控的前兆被动词出卖 | 提示 |

## 结论

阻断 1 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
