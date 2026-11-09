# ch08 · R3 对账（漏 / 编 / 错）

- 章：ch08；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch08_chapter_eight.txt`（348 行）
- R1 素读：`1-suread.json`（10 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句2 中文理解含引语外内容（“而她都符合，只是人生比预期短”） | `text/ch08_chapter_eight.txt:37` 原文 `She was all of those things. Her lifetime was simply shorter` | 附在“天生的猎手”之后 → 删除该句 | 阻断 |
| 2 | 提示 | 原句10 中文理解语病（“你我不可能放”） | `text/ch08_chapter_eight.txt:342` 原文 `I can’t let you go` | 你我不可能放，你懂的 → 我不可能放你走，你懂的 | 提示 |

## 结论

阻断 1 · 提示 1；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
