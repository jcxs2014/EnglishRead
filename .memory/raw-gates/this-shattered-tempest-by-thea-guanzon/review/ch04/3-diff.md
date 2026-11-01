# ch04 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch04 the shadowgate on the red mountain.md`
- 原文：`text/ch04_chapter_four.txt`（`char_total` = 15434）
- 素读底稿：`review/ch04/1-suread.json`（events 8 / relations 5 / numbers 4，17/17 命中）
- 机器层：`review/ch04/2-machine.json`（verdict ok，块数 8，本章 2672 词、建议 5–8）

## R2 对账

引语 8 块、30–70 词、逐字查无 0、形态全绿、块数 8 —— 与人工对账一致；`check_para_span.py`（`…` 同段检测）通过。

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | 塔拉辛下令「维持原样、去找幸存者、通知龙女王我们正在回去」 | **阻断**：原文 `text/ch04_chapter_four.txt:114` `"Then we leave things as they are," Talasyn instructed. … Go search for survivors, and let the Dragon Queen know that we're on our way.` 修前 md 只写了「维持原状」，后两道命令缺失 → 已在原句 7 的读者视角提示补一句并显式标注「紧随的下一段里」，不冒充引语 |
| — | 派 Ileis 回 Iantas 盯局势 | 已由「情感弧线位置」覆盖（「派伊莱丝、牵她进舱」），不另补 |

### 编 / 错

无。块 4「雨泉＋萨里曼之血」对应 `the sariman's blood, and Rainspring`；块 5「父亲交出鸟时爽快得反常」对应 `his father had handed it over with a readiness that had struck him as odd then`；块 2「把所有人撕成碎片」对应 `rendered them to pieces`。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 素读 numbers 里 `two airships`（两艘飞船靠泊）未进 md | 记一行不改：属场景交代，不是事件；md 已写「把塔拉辛带上飞船」 |
| T2 | 关键词行长度（`⚠️ 关键词整句 8 处`） | 已收紧（`26e3efd2b`），复跑 0 ⚠️ |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️；`gate.sh` rc=0。
