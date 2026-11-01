# ch05 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch05 two ships peel away from the silklands.md`
- 原文：`text/ch05_chapter_five.txt`（`char_total` = 13340）
- 素读底稿：`review/ch05/1-suread.json`（events 8 / relations 5 / numbers 4，17/17 命中）
- 机器层：`review/ch05/2-machine.json`（verdict ok，块数 7，本章 2308 词、建议 4–7）

## R2 对账

7 块、30–70 词、逐字查无 0、形态全绿、块数 7；`check_para_span.py` 通过。

## R3 三张单子

### 漏

无。素读 8 条事件（分道扬镳 → 贼鸥送信 → 她伸手被打断 → 无徽记蛾形小艇围杀运俘船 → 强拽进舱、七人阵亡 → 命令绑人、与三名幸存者迎战 → 拯救号降下清场 → 只想让一切燃烧）在 md 中原句 1–7 一一对应。

### 编

无。块 3「他以太术几乎耗尽」对应 `his aethermancy was running perilously low`；块 4「巫拉纳石崩口」对应 `chipped at the edge`。

### 错

| # | 位置 | 修前 | 判定 | 取证 |
|---|---|---|---|---|
| C1 | 原句 6 中文理解 | 「砸穿了**永海**的表面」 | 阻断（术语漂移） | 术语表 `Eversea → 越海`；已改 |
| C2 | 原句 1 中文理解 | 「这位**女海军上将**」 | 阻断（术语漂移） | 术语表 `Amirante → 阿米兰特`（ch45 4 处、ch51 2 处均用「阿米兰特」，本章 0 处）；已改为「这位阿米兰特」 |

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 素读 numbers 的 `fifteen`（约十五艘蛾形小艇）未进 md | 记一行不改：md 写「成群」，属概述层；数目不构成事件 |
| T2 | 关键词行长度（`⚠️ 关键词整句 7 处`） | 已收紧（`26e3efd2b`），复跑 0 ⚠️ |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️；`gate.sh` rc=0。
