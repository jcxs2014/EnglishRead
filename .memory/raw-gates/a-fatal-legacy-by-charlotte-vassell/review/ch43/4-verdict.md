# 4-verdict.md · ch43 判定表（R5）

- 被审：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch43 the forum stories are read.md`
- 参照：`text/ch43_43.txt`（4,650 字符；场景标题 `The Police Station`；全书第 43 章）
- 执行：R1/R2 由并行会话的审查代理完成（`1-suread.json` 21 条事件带区间 / `2-machine.json` 6 块全中、issues 全空）；代理在 R3 阶段停摆，**R3/R4/R5 由派工人接手**；派工人另自行素读原文（116 行）后再开 md

## 四组数

| 组 | 结果 |
|---|---|
| **逐字** | 6/6 引语逐字命中（严格子串比对 6/6、跨自然段 0）；词条例句 30/30 逐字命中；`chapter.sh` 报「引语块 6，片段 6，查无 0」 |
| **对应** | **6/6 块成立**（引语选短 0 · 不对应 0 · 密度不足 0） |
| **形态** | H1 `# 43. The Police Station`＝本书众数（且＝原文场景标题）；导航 5 项＝profile（mystery-thriller nav 5 项）；子项 4 项＝本书众子项集；块数 6 ∈ 本书区间 5–10（中位 7）⇒ **0 偏离** |
| **断言** | 核 24 条：**属实 23 · 阻断 1（已改）· 提示 6** |

## 阻断型（1 → 0）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 导航·一句话概括与一句话总结都称，骑士学徒、艳妇之死、给公主裁衣的丰满少女是 Amy 与 Matt「自己亲手办过的案子」 | `text/ch43_43.txt` L80 `‘I remember that case, it was one of the first ones **he** worked on as a DS.’`；L86 `‘**Caius** worked on both of these.’`；L92 `That’s Callie’s hats` | **与原文不符**：办这些案子的是凯厄斯，Amy 与 Matt 是认出它们的人；且「给公主裁衣的丰满少女」是卡莉本人、不是案子 | **阻断 → 已改**（两行均改） |

## 提示型（只记不改）

1. 原句 5 中文理解「听他念出」：原文未标这段韵文的朗读者（Matt 在朗读 ✓，但 Amy 也在其肩前；并行 R1 底稿判为 Amy）——原文未与 md 冲突，属推断未标注。
2. 原句 6 为什么这样写「一直沉默滑动的 Matt」：Matt 前文一直在出声朗读与评点，原文只说 `continued scrolling`。
3. 导航·线索结构把「狄更斯」与「草莓过敏」并列为「私人信息」泄漏：狄更斯属文体指纹而非私密事实。
4. 漏（提示级）：`most of her sales for the year come from Ascot` 与「怪物掳走女孩＝Eliza Chapel 案」两处支撑细节未成块；本章转折已覆盖，不判漏。
5. 原句 2 中文理解「立刻指出这条设定正是从迪吉的书信里摘来的事实」：原文是问句＋ Amy 的 `‘Yeah,’` 确认。
6. 导航·一句话概括「被月桂遮住的艳妇」：原文 `Neath a laurel`（在月桂之下），非「被遮住」。

## 假红 / 跳过

- **假红 0**、**跳过 0**。
- **归属错误 0**（6 块说话人逐块回原文核对）。

## 未覆盖（声明，不当干净）

- 6 个引语块的中文评析是否有力（纯评论，不判）；词表分档是否恰当（量具口径）。
- 韵文朗读者究竟是谁（原文未标，本表按「原文未与 md 冲突」判提示）。

## 复验

```
bash scripts/chapter.sh "…/ch43 the forum stories are read.md"            → EXIT 0
bash scripts/gate.sh   "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell" → EXIT 0
自写三条探针（严格逐字 / 单自然段 / 分析层英文专名）                     → 全书 395 块：P1 0 · P2 0 · P3 0
```
