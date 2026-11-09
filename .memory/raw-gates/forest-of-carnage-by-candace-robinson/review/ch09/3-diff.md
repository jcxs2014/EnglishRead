# ch09 · R3 对账（漏 / 编 / 错）

- 章：ch09；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch09_chapter_nine.txt`（262 行）
- R1 素读：`1-suread.json`（11 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句6 中文层夹生英文（whatever） | `text/ch09_chapter_nine.txt:145` 原文 `hidden in the depths of his eyes` | 眼底的 whatever 深藏不露 → 眼底的情绪深藏不露 | 提示 |
| 2 | 提示 | 原句7 读者提示“昨日撞墙”与原文不符（ch08 只回了一个 No） | `text/ch09_chapter_nine.txt`（锚点未定位） | 昨日撞墙、今日獠牙 → 前一次一个“不”字、这一次直接摔墙 | 提示 |

## 结论

阻断 0 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
