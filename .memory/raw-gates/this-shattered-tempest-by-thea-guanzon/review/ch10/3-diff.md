# ch10 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch10 sticky rice and a bad day.md`
- 原文：`text/ch10_chapter_ten.txt`（`char_total` = 11753）
- 素读底稿：`review/ch10/1-suread.json`（events 8 / relations 5 / numbers 5，18/18 命中）
- 机器层：`review/ch10/2-machine.json`（verdict ok，修前块数 6、本章 2089 词、建议 4–7）

## R2 对账

修前 6 块（逐字查无 0）；修后 **7 块**（新增 1 块），落在本书区间 5–13 内，0 ⚠️。

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | 信鹰送来信、吉的母亲求女儿回家；塔拉辛以 Lachis'ka 身份命令她回家 | md 只在「一句话概括」写「把吉强行送回家」，**逐块引语里没有这道命令**（`吉` 在块 1–6 中只作为「劫难清单」出现）→ 新增 **原句 2**（`text/ch10_chapter_ten.txt:66`，31 词、单段）；信的内容在紧随的上一段，已在提示里标注 |

### 编 / 错

无。块 4「回夜帝国本就是交易的一部分」对应 `It was always part of the bargain`；块 6「龙没有咒语也没有命令，只有情绪在起作用」对应 `Summoned from the water by her agitation`。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 块 3「她挑了别人劝她别去的那座阳台」属读者推断（原文只说 Steer clear of Iantas's balconies 与 outside her chambers） | 记一行不改（推断未冒充原文事实） |
| T2 | 关键词行长度 | 已全局收紧（`26e3efd2b`） |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️（块数 7）；`check_para_span.py` OK；`gate.sh` rc=0。
