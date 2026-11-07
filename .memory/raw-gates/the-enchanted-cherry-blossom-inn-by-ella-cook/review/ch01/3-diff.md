# ch01 对账（R3）

- 素读来源：`review/ch01/1-suread.json`（8 条事实，锚点全部命中 `text/ch01_chapter_1.txt`）
- 比对对象：`ch01 the physio and the architect.md`（13 块）

## 漏（素读有、md 无）
| 素读条目 | md 是否覆盖 | 判定 |
|---|---|---|
| Amrita 训练 Sylvie、以 samosas 换加练 | 块 1–3 | 覆盖 |
| Jamie 受 Mia 之托出图、被 Sylvie 当场雇下 | 导航「被 Sylvie 当场拍板雇下」+ 块 4 上下文 | 覆盖 |
| 握手触发魔法（魔法只在手作/铅笔上生效） | 块 5、6、12 | 覆盖 |
| Amrita 指出设计未做长远考虑、提前离场 | 块 7–10 | 覆盖 |
| 一周后 Jamie 借 Mist 提示要来号码并道歉 | 块 11–13 | 覆盖 |
| 结论 | 关键事件无遗漏 | 无阻断 |

## 编（md 有、原文无）
- 无。逐块引语均在本章 `text/` 命中（`quotes.py verbatim --full` 13/13）。

## 错（两边都有但不一致）
| 位置 | md 写法 | 原文 | 判定 |
|---|---|---|---|
| 块 10 读者视角 | 「后文凡是涉及她家庭与成长的段落，都和雨有关」 | ch07/ch08 婚礼、ch12 客厅均无雨/季风；季风只在本章出现一次 | 阻断（已修） |

## 取证
- `/usr/bin/grep -n "monsoon" text/ch01_chapter_1.txt` → 1 命中（本章唯一）；退出码 0。
- `quotes.py verbatim --full` 本章 13/13、MISS 0。
