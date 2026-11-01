# ch09 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch09 iantas in lockdown.md`
- 原文：`text/ch09_chapter_nine.txt`（`char_total` = 17127）
- 素读底稿：`review/ch09/1-suread.json`（events 8 / relations 4 / numbers 6，18/18 命中）
- 机器层：`review/ch09/2-machine.json`（verdict ok，修前块数 9、本章 2933 词、建议 5–9）

## R2 对账

修前 9 块（逐字查无 0）；修后 **10 块**（新增 1 块），落在本书区间 5–13 内，0 ⚠️。

## R3 三张单子

### 漏

| # | 素读事件 | 取证与处置 |
|---|---|---|
| L1 | 韦奈供出厨子迪仓，动机是哥哥死于阿拉里克在贝利安牢外那一击 | 供词本身（`:207`）只有 25 词、低于 30 词硬线；其动机段（`:219`，93 词）可用省略号在同段内压到 38 词 → 新增 **原句 9**（`“That night, on Belian…betrothal to you."`）；韦奈供词本身在块 9 提示里显式标注「同一场审讯里、不在本块引语之内」 |
| L2 | 新卡普坦 **埃克利**（高的继任者）与胡桑吉特一同汇报防务 | md 通篇只写「这位卡普坦」，人名缺失（`埃克利` 全书仅 ch43 出现）→ 在块 3 提示补一句并标注「上文交代过」 |

### 编 / 错

无。块 4「蟹眼果＋陶壳炸弹＋厨子失踪」与 `:105` 一段逐项对应；块 6「只有感谢」对应 `There is no penalty to bestow. Only gratitude.`

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 修前块数 9 已到「建议 5–9」上沿 | 已补 1 块；10 块仍在硬限 2–15 与本书区间 5–13 内 |
| T2 | 关键词行长度 | 已全局收紧（`26e3efd2b`） |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️（块数 10、片段 12：两处省略号同段跳过）；`check_para_span.py` OK；`gate.sh` rc=0。
