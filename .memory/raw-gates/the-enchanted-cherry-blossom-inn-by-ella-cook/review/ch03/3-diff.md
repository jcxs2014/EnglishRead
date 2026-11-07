# ch03 对账（R3）

- 素读：`1-suread.json`（8 条，锚点全中）
- md：14 块

## 漏
| 素读条目 | md 覆盖 | 判定 |
|---|---|---|
| 雾中进镇、导航失灵 | 块 1、2 | 覆盖 |
| Rayenne 指路（Lunar 在肩） | 块 3、4 | 覆盖 |
| 重新开始 + 改坡道 | 块 5、6、8 | 覆盖 |
| 她划图点亮魔法 | 块 7 | 覆盖 |
| 小精灵捣乱（含咖啡被动手脚） | 块 10 | 原 md 只写桌面下的嘟囔，未写咖啡；已补一句 | 提示（已修） |
| 外卖晚餐 + 文化差异 + 差点接吻 | 块 11–13 | 覆盖 |
| 拉绳 vs 穿戴设备 | 块 14 | 覆盖 |
| 结论 | 关键事件无遗漏 | 无阻断 |

## 编
- 无。

## 错
| 位置 | md | 原文 | 判定 |
|---|---|---|---|
| 块 8 读者视角 | 「它（她的话）被 Jamie 抄在图纸角落」 | `:280` 他写的是自己的转述 "Unapologetic access makes life better all round." | 提示（已修：改「这层意思」） |

## 取证
- `grep -n "didn’t taste the difference in his coffee" text/ch03_chapter_3.txt` → `:385`；退出码 0。
- `grep -n "scribbled the words across the corner" …` → `:280`；退出码 0。
