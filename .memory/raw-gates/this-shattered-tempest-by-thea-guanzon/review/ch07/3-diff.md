# ch07 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch07 the wolf and the outrigger.md`
- 原文：`text/ch07_chapter_seven.txt`（`char_total` = 7371）
- 素读底稿：`review/ch07/1-suread.json`（events 7 / relations 4 / numbers 4，16/16 命中）
- 机器层：`review/ch07/2-machine.json`（verdict ok，修前块数 4、本章 1244 词、建议 2–4）

## R2 对账

修前 4 块（30–70 词、逐字查无 0）；修后 **5 块**，块数落在本书分布区间 5–13 内，无 ⚠️。

## R3 三张单子

### 漏

| # | 素读事件 | 处置 |
|---|---|---|
| L1 | 拉詹·班特格拨开人群拔剑、声称要为达雅·穆萨尔与拉詹·吉塔布复仇 | **阻断**：`text/ch07_chapter_seven.txt:48` `Rajan Banteg pushed angrily through their ranks…` 修前 4 块引语里没有班特格出场 → 新增 **原句 4**（`:96` `“Kneel,” she told Rajan Banteg…everything you hold dear.”`，45 词、单段），原 4 顺移为 5 |
| L2 | 她因班特格「不知其意」而怀疑奥莉尔未死 | **阻断→降为标注**：`:63` `Had Oryal’s body not been among the dead…crept away?` 只有 28 词，单独成块会低于 30 词硬线 → 在块 2 的读者视角提示里显式标注为「同一场对峙里她心里还问过一句……」，不冒充引语 |

### 编 / 错

无。块 2「士兵在旧誓与军饷之间被撕开」对应 `torn between that loyalty and the one they…`；块 3「桅杆烧成灰烬、徽记随烟散掉」对应 `Masts were incinerated, various emblems going up in smoke`。

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 修前块数 4 落在「建议 2–4」上沿，导致两处事件无处安放 | 已补 1 块解决（见 L1） |
| T2 | 关键词行长度（`⚠️ 关键词整句 4 处`） | 已收紧（`26e3efd2b`），复跑 0 ⚠️ |

## 修复后复跑

`chapter.sh` rc=0、查无 0、0 ⚠️（块数 5）；`check_para_span.py` OK；`gate.sh` rc=0。
