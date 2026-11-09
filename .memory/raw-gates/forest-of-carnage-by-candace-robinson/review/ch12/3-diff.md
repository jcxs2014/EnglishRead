# ch12 · R3 对账（漏 / 编 / 错）

- 章：ch12；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch12_chapter_twelve.txt`（256 行）
- R1 素读：`1-suread.json`（10 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句8 中文理解含引语外内容（纸作品清单） | `text/ch12_chapter_twelve.txt:208` 原文 `Flowers, tea cups, a house, wolves, Sterling` | 地牢里 Cyan 盘腿坐在一堆纸作品中间：花、茶杯、房子、狼、Sterling。 → 删去清单，只留问话 | 阻断 |
| 2 | 提示 | 原句3 “乱伦式的宫廷腐坏”措辞失准（原文无乱伦） | `text/ch12_chapter_twelve.txt:85` 原文 `slithered between countless women’s legs` | 乱伦式的宫廷腐坏 → 宫廷的腐坏 | 提示 |
| 3 | 提示 | 原句7 夹生英文（say liar） | `text/ch12_chapter_twelve.txt:184` 原文 `as if to say liar` | 狼歪头 say liar → 狼歪头说“骗子” | 提示 |
| 4 | 提示 | 原句9 读者提示把“被捏碎的纸花”记在 ch08（实为 ch04） | `text/ch12_chapter_twelve.txt`（锚点未定位） | ch08 被捏碎的纸花 → ch04 被捏碎的纸花 | 提示 |

## 结论

阻断 1 · 提示 3；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
