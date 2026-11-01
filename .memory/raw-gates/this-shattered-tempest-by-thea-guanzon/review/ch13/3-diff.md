# ch13 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch13 supper in the officers mess.md`
- 原文：`text/ch13_chapter_thirteen.txt`（`char_total` = 17069）
- 素读底稿：`review/ch13/1-suread.json`（events 8 / relations 5 / numbers 5，18/18 命中）
- 机器层：`review/ch13/2-machine.json`（verdict ok，块数 9、本章 2998 词、建议 5–9）

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | event 8：衣服解完后他退开一步，把她独自留在寒冷里（全章收束动作） | 该段仅 14 词（`text/ch13_chapter_thirteen.txt:207` `Then he was stepping back. Stepping away from her. Leaving her cold all over.`），低于 30 词硬线、无法单独成块 → 在块 9「读者视角提示」里逐字引该句并标明「紧接着的下一段」 |

### 编 / 错

无。块 2 的「伊安塔斯的卧室／城塞两回」对应 `:28` 附近两处交代；块 6 的「饭锅星座」对应 `“The cooking pot, maybe.”`；块 8 的「毁掉岛屿」对应 `A love powerful enough to destroy islands.`。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 素读把「船长」写作「舰长」的场合 | md 用「舰长」，与 `kaptan → 卡普坦` 区分（此处是凯萨斯舰长，非内纳瓦伦卡普坦），不改 |
| T2 | 块 1 的「被赶出自己舱房」在原文是 `driven from his own stateroom` | 一致，不改 |

## 修复后复跑

`chapter.sh` rc=0、0 ⚠️（块数 9）；`check_para_span.py` OK；`gate.sh` rc=0。
