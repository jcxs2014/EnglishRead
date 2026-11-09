# ch24 · R3 对账（漏 / 编 / 错）

- 章：ch24；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch24_chapter_twenty_four.txt`（178 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句4 英文引用截断（which was why he'd planned to use surprise） | `text/ch24_chapter_twenty_four.txt:160` 原文 `he’d planned to use the element of surprise` | “which was why he'd planned to use surprise” → “he’d planned to use the element of surprise” | 提示 |
| 2 | 提示 | 原句10 为什么这样写误加“拖着调子”（原文该句无此标记） | `text/ch24_chapter_twenty_four.txt:178` 原文 `I solved our problem` | 语气却是他惯常的拖着调子 → 语气却轻描淡写 | 提示 |

## 结论

阻断 0 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
