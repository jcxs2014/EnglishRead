# ch07 · R3 对账（漏 / 编 / 错）

- 章：ch07；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch07_chapter_seven.txt`（283 行）
- R1 素读：`1-suread.json`（10 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 提示 | 原句5 读者提示称 Bael 在 ch06“执行绑票”，原文只写他指认肉店位置 | `text/ch07_chapter_seven.txt`（锚点未定位） | ch06 执行绑票 → ch06 在肉店外盯梢定位 | 提示 |
| 2 | 提示 | 原句9 读者提示的英文非逐字（I let you go） | `text/ch07_chapter_seven.txt`（锚点未定位） | ch01 他亲口说“I let you go” → “If I let you go” | 提示 |
| 3 | 提示 | 原句10 读者提示“翻转两本书”（本书只有一本） | `text/ch07_chapter_seven.txt:256` 原文 `Your treacherous grandmother` | 这一句同时翻转两本书 → 这一句同时翻转两代人的账 | 提示 |

## 结论

阻断 0 · 提示 3；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
