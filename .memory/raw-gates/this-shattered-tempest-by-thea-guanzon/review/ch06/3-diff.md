# ch06 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch06 the deliverance returns to port.md`
- 原文：`text/ch06_chapter_six.txt`（`char_total` = 16872）
- 素读底稿：`review/ch06/1-suread.json`（events 8 / relations 5 / numbers 5，18/18 命中）
- 机器层：`review/ch06/2-machine.json`（verdict ok，块数 9，本章 2899 词、建议 5–9）

## R2 对账

9 块、30–70 词、逐字查无 0、形态全绿、块数 9；`check_para_span.py` 通过。

## R3 三张单子

### 漏

无。素读 8 条事件（拯救号不告而别 → 领进舰桥、全线静默 → 她冷淡回应、他盼她发火 → 她说明「王宫有内奸」→ 埃拉格比求援、叛军北犯 → 她隐瞒乌尔杜佳之罪 → 十九艘小艇五支箭形编队 → 帕苏阿号射空弩炮、座艇撞上敌舰后甲板）在 md 原句 1–9 中对应齐全。

### 编

无。块 4「有没有魔法你都是难对付的对手」对应 `You are a formidable opponent, magic or no` ；块 7「凯德只做了几个小时的丈夫」对应 `Khaede had been a husband for only a few hours`。

### 错

| # | 位置 | 修前 | 判定 | 取证 |
|---|---|---|---|---|
| C1 | 原句 8 中文理解 | 「**帕苏亚号**」 | 阻断（术语漂移） | 术语表 `Parsua → 帕苏阿号`，ch44/45 已统一；本章 2 处已改 |
| C2 | 原句 3 中文理解 | 「通知**天穹之顶**」 | 阻断（术语漂移） | 术语表 `Roof of Heaven → 天穹宫`；本章 1 处已改 |

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 关键词行长度（`⚠️ 关键词整句 9 处`） | 已收紧（`26e3efd2b`），复跑 0 ⚠️ |
| T2 | 「十九艘 / 五艘指挥舰」两个数目 | 已与素读一致（`nineteen`、`five`），md 两处均现 |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️；`gate.sh` rc=0。
