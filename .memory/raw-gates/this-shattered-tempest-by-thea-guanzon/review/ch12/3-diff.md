# ch12 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch12 daya rasmey and the withdrawal.md`
- 原文：`text/ch12_chapter_twelve.txt`（`char_total` = 19188）
- 素读底稿：`review/ch12/1-suread.json`（events 8 / relations 5 / numbers 4，17/17 命中）
- 机器层：`review/ch12/2-machine.json`（verdict ok，修前块数 10、本章 3326 词、建议 6–10）

## R2 对账

修前 10 块（逐字查无 0）；修后 **11 块**（新增 1 块），落在本书区间 5–13 内，0 ⚠️。

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | 她提出「现在把我送回伊安塔斯也不迟」，他拒绝：不拿她的安全换自己的难受，并说带她去看「我们的舱房」 | 修前 10 块里只有导航「同舱而眠」提到结果，**没有这场交涉** → 新增 **原句 9**（`text/ch12_chapter_twelve.txt:171`，60 词、单段）；她的提议那句（`:168`，23 词、低于硬线）在提示里标注 |

### 编 / 错

无。块 7「母亲与辛坦·西利姆合谋」与 `:78` 一致（`辛坦·西利姆` 已与 ch03 统一，非「西林」）；块 10「摘婚戒」对应结尾一句。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 块 2 把 Lueve 的失言读成「顺着自己的话头往下滑」 | 记一行不改（读解语气，有 `absentminded nod` 支撑） |
| T2 | 关键词行长度 | 已全局收紧（`26e3efd2b`） |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️（块数 11）；`check_para_span.py` OK；`gate.sh` rc=0。
