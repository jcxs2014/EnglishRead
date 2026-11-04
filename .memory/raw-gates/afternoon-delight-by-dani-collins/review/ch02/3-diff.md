# ch02 · R3 对账（漏 / 编 / 错）

- 对账基准：`1-suread.json`（R1 素读，审查会话独立只读 `text/`）+ 本章 md + `text/ch02_chapter_two_zak.txt`
- 逐字底稿：`2-machine.json`（R2 第二实现，verdict=ok，5 块）
- 章名：ch02 chapter two zak.md

## 单子一：漏（素读有、md 无）

| （无） | — | R1 抽读的 8 条关键事实均能在 md 的引语块或分析层找到落点 |

## 单子二：编（md 有、原文无）

| （无） | — | 分析层专名逐条回本章 text/ 核，未见凭空实体 |

## 单子三：错（两边都有但不一致）

| （无） | — | 施事/受事/数字/时序逐块核对，未见方向错误 |

## 引语起点/终点核对（引语截短类）

- **原句 4 引语起点截短（提示级）**：md 引语自 `“It's good to have you home, Zak. I like the company.”` 起，原文该话轮首句为 `“Let’s do that. It’s good to have you home, Zak. I like the company.”`——md 省略了同一话轮内的首句 `“Let’s do that.”`；分析层未涉及被省略内容（中文理解与「为什么这样写」讲的仍是拍肩与接球意象），故判提示级、不阻断。
- 该形态为全库通行（the-scarlet-ball 24 处、your-beloved-remains 114 处同类跨段归一化引语），verify_quotes 与 verify_fragments_indep 均判通过（MISS 0）。
