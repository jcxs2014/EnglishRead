# ch11 · R3 对账（漏 / 编 / 错）

- 章：ch11；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch11_chapter_eleven.txt`（370 行）
- R1 素读：`1-suread.json`（11 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句11 中文理解含引语外内容（“她裹着毛巾走出浴室”） | `text/ch11_chapter_eleven.txt:214` 原文 `draped a fluffy towel around her body` | 她裹着毛巾走出浴室，他削木刀的手停了 → 他削木刀的手停了 | 阻断 |
| 2 | 提示 | 原句5 读者提示把气味段说成“这段”，实际在下一段 | `text/ch11_chapter_eleven.txt:109` 原文 `clovers and embers caressed her senses` | clovers and embers 的气味在这段从叙事里冒头 → 紧接着的叙事里（她贴着他的胸口上楼时）…冒头 | 提示 |
| 3 | 提示 | 原句8 中文理解“一刻钟”为无据细化（原文 a moment） | `text/ch11_chapter_eleven.txt:175` 原文 `I’ll allow you a moment with your brother` | 就给你一刻钟见弟弟 → 就让你见弟弟一面 | 提示 |

## 结论

阻断 1 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
