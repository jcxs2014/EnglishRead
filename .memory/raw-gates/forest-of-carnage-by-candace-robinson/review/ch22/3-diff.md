# ch22 · R3 对账（漏 / 编 / 错）

- 章：ch22；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch22_chapter_twenty_two.txt`（205 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句10 中英夹杂（他’d meant it）与“两本书” | `text/ch22_chapter_twenty_two.txt:205` 原文 `he meant it down to his marrow` | ——他’d meant it down to his marrow。/两本书的开头与中段 → ——他把这句话刻进了骨髓。/本书的开头与中段 | 提示 |

## 结论

阻断 0 · 提示 1；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
