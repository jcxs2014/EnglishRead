# ch10 · R3 对账（漏 / 编 / 错）

- 章：ch10；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch10_chapter_ten.txt`（219 行）
- R1 素读：`1-suread.json`（10 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句8 读者提示称 ch01 Winter 以狼形扑击 Sterling，原文扑击者是狼群（非 Winter） | `text/ch10_chapter_ten.txt`（锚点未定位） | ch01 Winter 的第一形态也是扑击（扑向 Sterling 被外婆救） → ch01 外婆家那一夜的扑杀（Sterling 被大狼按在地上） | 提示 |
| 2 | 提示 | 原句9 夹生英文（ annoyed ex） | `text/ch10_chapter_ten.txt:138` 原文 `She was the one other wolf he loathed` | 从“ annoying ex”升级 → 从“烦人的前任”升级 | 提示 |

## 结论

阻断 0 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
