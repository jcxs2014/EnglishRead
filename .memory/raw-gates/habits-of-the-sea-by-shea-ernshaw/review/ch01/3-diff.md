# ch01 素读 vs md 差异（人判）

素读清单：`1-suread.json`（9 条事实，锚点全部命中 `text/ch01_prologue.txt`）。以下逐条比对。

## 对应关系（R4）

| 块 | 引语覆盖的原文区间 | 分析所指 | 结论 |
|---|---|---|---|
| 1 | :17 风暴／外赫布里底 | 尺度、snell、骨头 | 对应 ✅ |
| 2 | :20 抱尸出门 | 身体拆成零件、wet dishrags | 对应 ✅ |
| 3 | :26 两块石头／三尺坟 | 转喻、nested | 对应（但见 D1） |
| 4 | :56 传说版本／四公顷 | sift、深与广、传说层 | 对应 ✅ |
| 5 | :68 Eleanor Mills | veer off course、被记住也被遗忘 | 对应 ✅ |

## 查出的问题

### D1 · 分析层把比喻读成情节：`被换成两块石头` / `只留下替代物`

- **位置**：md:49（原句 3 的「为什么这样写」）
- **改前**：`两个没出世的婴儿被换成两块石头，还特意注明"还没长成"。作者先让读者以为真有两具尸体，再抽掉其中两具，只留下替代物`
- **改后**：`两个没出世的婴儿被写成"两块石头"，还特意注明"还没长成"。作者先让读者以为真有两具尸体，随即用一句"They were merely stones"把它们降格成两块没熟的南瓜——尸体没有被换掉，只是被一句话写没了`
- **原文依据**：
  - `text/ch01_prologue.txt:26`：`He strode back to the house to retrieve the two smaller bodies. They were merely stones, tiny as garden squash, not yet ripe.`
  - `text/ch01_prologue.txt:29`：`the night Clay Lockhart buried his wife and his newly born twins in the soil beside the sea` ← 他埋的就是那对双胞胎本身，没有替代物
- **判据**：原文 `They were merely stones` 是对"两个更小的身体"的比喻式贬抑（未成熟），不是"用石头代替尸体"；`:29` 直接否证了"替代物"读法。
- **同源扩散**（同一读法出现在另两处，须同批改）：
  - `00_概述.md` 第 1 段：`双胞胎只得以两块小石头代替`
  - `00_金句精选.md` ①「为什么重要」：`两个没出世的婴儿被换成两块小石头`

### D2 · 导航层「唯一的目击者」与原文不符

- **位置**：md:11（一句话概括）
- **改前**：`邻居 Neil Hagdorn 是唯一的目击者`
- **改后**：`邻居 Neil Hagdorn 是清早第一个发现房子不见了的人（此前已有邻居在闪电里看见他抱着尸体出门）`
- **原文依据**：
  - `text/ch01_prologue.txt:23`：`Neighbors farther up the coastline saw his silhouette in the flashes of moonlight between storm clouds`（复数邻居看见）
  - `text/ch01_prologue.txt:47`：`Neil, even with his bad hip, was the first to amble up the steep shore`（Neil 是"第一个"上崖查看的人）
- **判据**："唯一"与 `Neighbors` 冲突；Neil 的独特性在于"第一个走到崖下"，不在"唯一看见"。

## 已核实为正确（不要改坏）

- 块 2「最后再被一个字 `her` 点醒」：`her` 确实在紧接的 `:26`（`He carried her out to the cliff’s edge`），引语本身不含 `her` 但叙述延续如此，**成立**。
- 块 3 的 36 词/1 句切分与 `:26` 连续句边界一致，**不要为了凑 30 词把 `:26` 首句并进来**。
- 「四公顷土地」= `four hectares`（`:56`），非"四英亩"，**正确**。
- 「盐井岛」= Saltwell Island 的既定译名（全书统一），**不要改成"盐泉岛/索尔特韦尔"**。
