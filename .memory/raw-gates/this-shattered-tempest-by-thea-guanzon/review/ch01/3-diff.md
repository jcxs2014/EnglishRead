# ch01 对账（R2 机器层 + R3 三张单子）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch01 the ballroom full of broken glass.md`
- 原文：`text/ch01_chapter_one.txt`（`char_total` = 21945，`wc -l` = 246）
- 素读底稿：`review/ch01/1-suread.json`（events 8 / relations 4 / numbers 4）
- 机器层：`review/ch01/2-machine.json`（`chapter.sh --json`，verdict = ok，块数 12，查无 0）

## R2 对账

| 项 | 机器判定 | 人工对账 |
|---|---|---|
| 引语句级与长度 | 12 块，逐块 30–70 词 | 一致 |
| 引语逐字 | 查无 0 | 一致 |
| 形态（H1 / 导航 5 项 / 4 子项 / 三档表 / 一句话总结） | 全绿 | 一致 |
| 块数 vs 本书众数 | 12 块（本章 3727 词，建议 7–12） | 一致 |
| 中文密度 | 通过 | 一致（无整段英文） |

## R3 三张单子

### 漏（素读有、md 无 → 阻断）

无。素读 events 8 条逐一在 md 中有着落：

1. 战镰砍倒最后一名刺客 → 原句 4
2. 飞刀掷向走近的黑衣人（Sevraim）→ 原句 5
3. 翻找确认 Talasyn 不在 → 原句 6（前接叙述）
4. Gao 报已派搜索队 → 导航「一句话概括」+ 原句 9 的病房场景
5. Elagbi 按肩劝他去治伤 → 原句 8
6. Sevraim 报城堡搜遍、Ileis 也失踪 → 原句 9
7. 掀帘冲向 Surakwel → 导航 + 原句 11
8. Gao 报 Ileis 小艇坐标指向 Silklands → 一句话总结

### 编（md 有、原文无 → 阻断）

| # | 位置 | md 原文 | 判定 | 取证 |
|---|---|---|---|---|
| B1 | 原句 5 读者视角提示 | 「那道被飞刀招呼的黑影其实是**七夫雷姆**」 | 阻断（人名错） | `/usr/bin/grep -n "Sevraim’s irate cry" text/ch01_chapter_one.txt` → `36:` `Sevraim’s irate cry pierced through the haze of Alaric’s bloodlust.` 全文无「七夫雷姆」，此为错字 |
| B2 | 原句 8 读者视角提示 | 「贝洛克……**此后他反复**以精心制作的服装形象出现」 | 阻断（跨章断言无据） | `/usr/bin/grep -l "贝洛克" ch*.md` → 仅 `ch01 … .md` 命中；原文本章 2 处（`102:` 礼服、`159:` 亮粉），此后章节 0 处 ⇒ 「此后反复」不成立 |
| B3 | 原句 9 读者视角提示 | 「这间病房随后会被逐一点名：杰、尼亚姆哈、**高**，还有那些中毒的伊安塔斯士兵」 | 阻断（名单造人） | `/usr/bin/grep -n "Unfortunately, the infirmary was full" → 144:` 原文名单为 `Jie, and Niamha, the Daya of Catanduc … Several other nobles … But the majority of the beds were occupied by Iantas’s soldiers`；Gao 在病房无任何出现（他在宴会厅下令，见 `87:` / `93:`） |

### 错（两边不一致 → 阻断）

| # | 位置 | md 原文 | 判定 | 取证 |
|---|---|---|---|---|
| C1 | 原句 11 读者视角提示 | 「（要是陛下因为想先开会讨论而救不回妻子，）我就走到利尔岛边缘去」 | 阻断（漏 half-way 语义） | `text/ch01_chapter_one.txt:267`：`I might as well make sure I’m halfway to the edge of Lir by then` ⇒ 是「走到去利尔的路上一半」，不是「走到岛的边缘」 |
| C2 | 原句 11 读者视角提示 | 「是他对主角的**第一次**当众施压」 | 阻断（不可核的计数断言） | 全文 `grep -c "first time"` 与语境均不支撑「第一次」；已改为不计数表述 |

## 提示（不判红，已顺手修）

| # | 位置 | 问题 | 处置 |
|---|---|---|---|
| T1 | 原句 8 中文理解 | 「才想起高几分钟前**高**提过的伤」——「高」重复 | 已改为「高几分钟前提过的伤」 |
| T2 | 全书体例 | 关键词行 4 个词条 / 整行 ≥7 词，触发 `⚠️ 关键词整句 12 处` | 已把 ch01（及 ch02/03/04/05/06/07/09/10/11/12/54）收紧为 3 条两词短语；复跑 0 ⚠️（独立提交 `26e3efd2b`） |

## 修复后复跑

- `bash scripts/chapter.sh "<ch01 md>"` → `rc=0`，`引语块 12，片段 12，查无 0`，`空引号 0｜子项缺 0｜关键词不成立 0｜中文过薄 0｜模板套话 0｜残句缺词 0`，`⚠️` 0
- `bash scripts/gate.sh "<书目录>"` → `rc=0`，正门结论 0 条阻断型
