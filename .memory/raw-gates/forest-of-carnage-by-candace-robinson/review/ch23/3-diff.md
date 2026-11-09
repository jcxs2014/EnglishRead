# ch23 · R3 对账（漏 / 编 / 错）

- 章：ch23；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch23_chapter_twenty_three.txt`（262 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句10 为什么这样写误加“drawl”（原文该句无此标记） | `text/ch23_chapter_twenty_three.txt:172` 原文 `Wicked princes don’t get happy endings` | drawl 与关门的动作让告白与告别同时完成 → 关门的动作让告白与告别同时完成 | 提示 |

## 结论

阻断 0 · 提示 1；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
