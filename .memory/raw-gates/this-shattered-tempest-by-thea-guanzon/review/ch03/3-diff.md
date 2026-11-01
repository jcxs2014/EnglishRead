# ch03 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch03 the hunting lodge approached from behind.md`
- 原文：`text/ch03_chapter_three.txt`（`char_total` = 23992）
- 素读底稿：`review/ch03/1-suread.json`（events 8 / relations 5 / numbers 6，19/19 命中）
- 机器层：`review/ch03/2-machine.json`（verdict ok）

## R2 对账

| 项 | 机器判定 | 人工对账 |
|---|---|---|
| 引语长度/句数 | 13 块，30–70 词 | 一致 |
| 逐字 | 查无 0 | 一致 |
| 形态 | 全绿 | 一致 |
| 块数 | 13（本章 4190 词，建议 8–13） | 一致 |

## R3 三张单子

### 漏

无。素读 8 条事件在 md 中全部有着落：从空中看火树（原句 1）→ 塞夫雷姆坚持从背后接近（原句 2）→ 温普克与「更简单的年月」（原句 3）→ 阿拉里克压制杀意（原句 4）→ 塔拉辛灵力被抽（原句 5）→ 拉帕特的警告（原句 6）→ 奥莉尔的控诉（原句 7）→ 供状与署名（原句 8）→ 混战、拉莉亚中毒、吉塔布被钉（原句 9/10）→ 供状被烧（原句 11）→ 影术洪流退去（原句 12）→ 尸堆前强吻（原句 13）。

### 编

无。块 1「已故拉詹·温普克的领地」、块 2「按伊莱丝发来的坐标找到她」、块 12「影术从以太空间放出」均可在引语内或紧邻原文找到出处。

### 错

| # | 位置 | 修前 | 判定 | 取证 |
|---|---|---|---|---|
| C1 | 原句 8 中文理解 | 「旧日**西林**王室的医者」 | 阻断（术语漂移） | 术语表 `Silim → 西利姆`（`Urduja Silim 乌尔杜佳·西利姆`，`Silim 王朝`）；md 其余段落用「西利姆」；已改「西利姆王室」 |

## 提示

| # | 问题 | 处置 |
|---|---|---|
| T1 | 关键词行原 4 条 / 整行 ≥7 词（`⚠️ 关键词整句 12 处`） | 已收紧为 3 条两词短语（`26e3efd2b`），复跑 0 ⚠️ |
| T2 | 「十人救援队」为可计数断言 | 已取证：`:45` `They were ten in their party`；`:63` 分工（Ileis/Surakwel 走地道，Gao 与 Lachis-dalo 随 Alaric 与 Sevraim） |

## 修复后复跑

- `bash scripts/chapter.sh "<ch03 md>"` → `rc=0`，查无 0，五项判据全 0，无 ⚠️
- `bash scripts/gate.sh "<书目录>"` → `rc=0`
