# ch02 对账（R3）

- 素读：`1-suread.json`（8 条，锚点全中）
- md：13 块

## 漏
| 素读条目 | md 覆盖 | 判定 |
|---|---|---|
| Aiden 闭眼引路、室内复刻初次约会 | 块 2 | 覆盖 |
| 求婚（配套戒指、她先求的婚） | 块 4、5 | 覆盖 |
| 两天后向 Katie/Ophelia 公布 | 块 7、8 | 覆盖 |
| Katie 误以为怀孕 → 八个月 | 块 8 | 覆盖 |
| 撞窗 → 鸟复活 → 自报 Lunar | 块 9–13 | 覆盖 |
| 结论 | 无关键遗漏 | 无阻断 |

## 编
- 无。13 块引语全部 `verbatim --full` 命中。

## 错
| 位置 | md | 原文 | 判定 |
|---|---|---|---|
| 导航「情感弧线」 | 「交往三个月的公开说法（实际八个月）」 | `:510` "you’ve only been dating three months!"；`:531` "Eight months?" | 一致，已改为「公开说法」表述 |
| 块 8 中文理解 | Katie「误以为 Mia 怀孕」 | `:501` "Plenty of women bring up babies by themselves" | 一致 |

## 取证
- `grep -n "Eight months" text/ch02_chapter_2.txt` → `:531`；退出码 0。
