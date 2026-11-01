# ch11 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch11 the eagle from surakwel.md`
- 原文：`text/ch11_chapter_eleven.txt`（`char_total` = 16883）
- 素读底稿：`review/ch11/1-suread.json`（events 8 / relations 5 / numbers 5，18/18 命中）
- 机器层：`review/ch11/2-machine.json`（verdict ok，块数 9、本章 2972 词、建议 5–9）

## R2 对账

块数 9（修前修后同，逐字查无 0）；落在本书区间 5–13 内，0 ⚠️。

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | 乌尔杜佳说明死去的附魔师都是「达雅·维卡尔的旧日学徒」、且都出身内战战败方领地 | 该句（`text/ch11_chapter_eleven.txt:87`）在块 4 引语之后的下一段，md 修前无 → 在块 4 提示补注并标注「紧接着的一段」 |

### 错

| # | 类型 | 改前 | 改后 | 取证 |
|---|---|---|---|---|
| E1 | 术语 | 高船长 | 高卡普坦 | 术语表 `kaptan → 卡普坦`；ch06/ch09 同 |

### 编

无。块 5「把丁香树皮当作一种预防手段在服用」已按上一轮修改保留（不写「避孕」，因原文只说 the bark of the wisewoman's lilac 与 every time…went down to the kitchens）。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 块 2「他有借口不带她回 Kesath 而松了口气」属推断（原文有 relieved 语义但非直陈） | 记一行不改（读解语气） |
| T2 | 关键词行长度 | 已全局收紧（`26e3efd2b`） |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️；`check_para_span.py` OK；`gate.sh` rc=0。
