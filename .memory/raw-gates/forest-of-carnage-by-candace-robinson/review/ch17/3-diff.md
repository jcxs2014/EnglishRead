# ch17 · R3 对账（漏 / 编 / 错）

- 章：ch17；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch17_chapter_seventeen.txt`（196 行）
- R1 素读：`1-suread.json`（14 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句2 关键词 carnival 不在本块引语内（在上一段叙事） | `text/ch17_chapter_seventeen.txt:34` 原文 `like a carnival performance` | 关键词：carnival / expect → 关键词：expect / servant；并在分析中标明“上文那句” | 提示 |
| 2 | 提示 | 原句6 残句（“露出地 下面”） | `text/ch17_chapter_seventeen.txt:145` 原文 `Even though that’s all I will fucking think about` | 在语言层露出地 下面 → 在语言层露出地表 | 提示 |

## 结论

阻断 0 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
