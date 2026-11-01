# ch15 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch15 a decade since the last lady maid.md`
- 原文：`text/ch15_chapter_fifteen.txt`（`char_total` = 14969）
- 素读底稿：`review/ch15/1-suread.json`（events 8 / relations 5 / numbers 5，18/18 命中）
- 机器层：`review/ch15/2-machine.json`（verdict ok，修前块数 8、本章 2578 词、建议 5–8）

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | event 5/6/7：凯德承认越狱靠塔拉辛提供的监狱布局与安保情报、阿米兰特参与策划；随后直说「阿米兰特怕你已被策反」 | 修前 8 块完全没有这段（只有导航一句「被指为通敌者」）→ 新增 **原句 6**（`text/ch15_chapter_fifteen.txt:135`，41 词、单段：`“The Amirante fears that you’re compromised.”…I take it.`）；越狱/劫狱那几句（`:117`/`:120`/`:123`）在同一段对话前半，提示里标注 |

### 编 / 错

无。块 1 的 `a decade` 对应 `:18` 附近；块 7 的「父亲插了手」对应 `:219` `You have done well, Emperor.`

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 素读 `two sails short of a fleet`（习语）未进 md | 记一行不改（凯德的损人话，非情节） |
| T2 | 素读 `almost a year` / `two fronts` 未进 md | 记一行不改（时间与战略交代） |

## 修复后复跑

`chapter.sh` rc=0、0 ⚠️（块数 9，落在本书区间 5–13）；`check_para_span.py` OK；`gate.sh` rc=0。
