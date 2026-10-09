# d 步二审 · ch15

## 结论：共 4 块，通过 4，缺陷 0，待复核 2

**核对基准说明**：任务给定路径 `text/ch15_chapter_13.txt` 在 text/ 下不存在；该目录中实际文件为 `text/ch15_chapter_1.txt`，且精读 md 自述提取件为 `text/ch15_chapter_1.txt`（见 md 第 8 行）。本次以 `text/ch15_chapter_1.txt` 为原文基准核对（内容与 md 完全对应）。此路径差异见「待人工复核」第 3 条。

| 块 | 引语逐字 | 说话人 | 引语↔分析 | 关键词回查 | 结构 | 判定 |
|---|---|---|---|---|---|---|
| 原句 1 | ✅ 命中 text 第 14 行 | ✅ 母亲（叙事描写） | ✅ | ✅ shears / stricken / sash 均在引语 | ✅ | 通过 |
| 原句 2 | ✅ 命中 text 第 26 行 | ✅ 母女摊牌（叙事+前文对白对照） | ✅ | ✅ a rare, true thing / take back / trunks 均在引语 | ✅ | 通过 |
| 原句 3 | ✅ 命中 text 第 42 行 | ✅ Henrie 做娃娃（叙事） | ✅ | ✅ simulacrum / tidbits / burial 均在引语 | ✅ | 通过 |
| 原句 4 | ✅ 命中 text 第 105 行 | ✅ Henrie 深夜幻想（叙事） | ✅ | ✅ mallet / unblemished / beads 均在引语 | ✅ | 通过 |

## 缺陷清单

无。

（逐项已核对：四条引语行均在 text/ch15_chapter_1.txt 中逐字命中，仅标点（弯/直引号、省略号两侧）差异；无实词改写；无引语截短——每条引语均为完整句，足以支撑其「中文理解」「为什么这样写」的分析。）

## 待人工复核

1. **原句 1 · 读者视角提示越出引语块**
   - 引语行原文：`> **原句 1:** "Her mother stood beside the deal table, ... but she wouldn't give it up."`（止于第 14 行）
   - 读者视角提示原文：「注意 Henrie 伸手去碰裙子却被母亲挥剪喝止的细节……」
   - 问题说明：该细节出自 text 第 17 行（She put out a hand to touch the dress, but her mother snatched it away, brandishing the shears at her…），位于引语块**之外**（紧邻其后）。这是指向下一句的前瞻提示，非引语截短，属常见手法；但因不在引语块内，请人工确认是否属意如此。
   - 建议修法：无需改；如求严格可注明「下句」。

2. **原句 4 · 读者视角提示「前一句」指代**
   - 引语行原文：`> **原句 4:** "Sometimes, when Henrie couldn't sleep, ... remove any risk."`（text 第 105 行）
   - 读者视角提示原文：「结合前一句能读出更冷的一层……她把自己能给的都列完了，却发现不够；这个'不够'正是章末转向命运的起点。」
   - 问题说明：「不够」实指**引语之后**的 text 第 108 行（But she knew it was not enough…），属章末后续句，而非「前一句」。指代方向用词与原文位置略有出入。
   - 建议修法：将「前一句」改为「本章末尾一句」或「下文一句」。

3. **原文提取件路径**
   - 问题说明：任务指定的 `text/ch15_chapter_13.txt` 不存在；实际提取件为 `text/ch15_chapter_1.txt`，精读 md 第 8 行也正确引用后者。内容与 md 完全对应，无章号错标（md 标题「Chapter 1（Part Two: 1795–1811）」与 text 首行「Chapter 1」一致）。仅为路径记录差异，非内容缺陷。
   - 建议修法：核对任务参数路径是否笔误。

---

ch15 完成：4 块，缺陷 0，待复核 2