# ch04 · R3 对账（漏 / 编 / 错）

- 章：ch04；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch04_chapter_four.txt`
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句3 中文理解含引语外内容（“不到二十岁”） | `text/ch04_chapter_four.txt:79` 原文 `the youngest, perhaps not even twenty years` | 引语自 Please 起 → 引语前扩至 The wolf nearest him—the youngest… | 阻断 |
| 2 | 提示 | 原句2 读者提示的英文非逐字（like theirs） | `text/ch04_chapter_four.txt:0` 原文 `like hers, like their mother` | like theirs, like their mother's → like hers, like their mother’s | 提示 |
| 3 | 提示 | 原句6 中文层夹生英文（releasing） | `text/ch04_chapter_four.txt:133` 原文 `the maggots turn to flies` | 尸体变成持续 releasing 的教育装置 → 尸体变成持续投放的教育装置 | 提示 |
| 4 | 提示 | 原句9 中文理解语病（“一整袋箭的弓上方”） | `text/ch04_chapter_four.txt:229` 原文 `a bow and quiver full of arrows` | 床架上、一整袋箭的弓上方 → 床架横杆上、弓与满袋箭的上方 | 提示 |

## 结论

阻断 1 · 提示 3；均已当场整改，整改后 `chapter.sh` rc=0。
