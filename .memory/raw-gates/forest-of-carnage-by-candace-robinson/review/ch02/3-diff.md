# ch02 · R3 对账（漏 / 编 / 错）

- 章：ch02；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch02_chap2.txt`（217 行）
- R1 素读：`1-suread.json`（10 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句4 中文理解含引语外内容（花园守卫、爬常春藤、两小时前） | `text/ch02_chap2.txt:145` 原文 `They killed the guards in the garden and climbed up the ivy` | 中文理解写“杀了花园守卫、顺着常春藤爬进国王房间” → 删去引语外细节，只保留引语内的伤情清单 | 阻断 |

## 结论

阻断 1 · 提示 0；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
