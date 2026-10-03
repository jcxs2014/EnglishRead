---
name: 2026-10-03-carry-me-to-my-grave-五步审查
description: Carry Me to My Grave 五步审查：50 处阻断型，根因是亲属关系凭印象填入分析层
metadata:
  type: project
---

# 《Carry Me to My Grave》独立五步审查（2026-10-03，Qoder-Mac，同会话不降级）

**结论：门禁全绿状态下查出并整改 50 处阻断型（54 处替换）＋ 1 处提示型撤回。**

## 五个根因（按规模）

1. **亲属关系凭印象填入分析层 —— 37 处（占 74%）**。引语逐字无误，错的是引语下方那句中文里谁是谁的哥哥/姐姐/妻：
   - `ch17` 「弟弟」×11（Elias 是 **哥哥**，ch13:241 `This was his older brother`）
   - `ch31`「妹妹/兄妹」×4、`ch29` ×3、`ch23` ×3、`ch24` ×4、`ch46` ×2（把 Maggie 写成妹妹）、`ch06` ×2、`ch07` ×2、`ch04` ×1、`ch08` ×1、`ch09` ×1、`ch21` ×1、`ch34` ×1、`ch26` ×1
   - **合法未改**：ch02「未指明是兄长还是弟弟」（原文确实未定）、ch06/ch10 的「弟弟」指 Joe→Alfie、ch55「哥哥让着弟弟」正确、ch23/ch51 的「兄妹」指 Jennie+Malcolm 同胞。
2. **分析层英文「每词都在、连续串不在」—— 8 处**。`blew/blow`、`grinned/grins`、`caught/catch`、`painted/paint`、`cutting/cut`、`her hunger/hungry`、`Alfie Hannigan/Alfie`、以及 `see through him, hear their voices` 这种把两处片段并成一句。
3. **主体归属错 —— 3 处**。ch30（Dwight 其实**听不见**琴声，ch35 有明文 `His boss had been unable to hear the music`）、ch37（撒粉的是 **Jennie** 不是 Malcolm，Violet 只是提议）、ch45（Elias 并非「一个字都没有」，原文 :81 有 `What are you doing?`）。
4. **叙述次序错 —— 3 处**。ch26（人群是被枪吓退、Violet 的谎话在前 Malcolm 踩油门在后）、ch28（Violet 跳车发生在该句**之后**）、ch13（视角切换点提前了约 3 段）。
5. **可核伪断言 —— 4 处**。ch17「第一次叫出母亲的名字」（ch15 已四次）、ch29「全章最后一句」、ch07「他们一齐解释成音乐盒」（只有 Malcolm 一人 `wondered`）、ch43 导航与分析互斥。

## 工具盲区（本次实证，全库成立）
- **`sweep_analysis_inline` 只收带引号英文 + 引号从左到右配对** ⇒ 一行里先出现长度 <4 的中文引号片段，后面真英文全部失明；**完全不带引号的裸英文本就不在口径内**。本次 8 处形态缺陷它一条没报。
- `check_analysis_indep` 补上了裸英文，但仍漏 4 处（它只抽带引号片段）。
- **补法**：`scripts/attic/cmtmg_full_flat.py`——按「本章 text/ 优先、全书次之」核每一个 ≥2 词英文串，并支持 `A ... B` 两半各自命中即算合法省略。**首跑抓到 20 条，14 真 / 6 省略记法。**
- **该脚本自身踩了两次坑**（都是判据按自己的书写习惯定）：①把弯撇号 `’` 当切段符（它是英语词内字符）②grep 带上下文长度要求，靠近行首行尾时假阴性。**报错不指人的时先怀疑判据。**

## 已撤回的假红/幻觉
- 子代理合计报 9 条幻觉，复核后全部撤回（ch11 `I wasn't always this` 实在 text/ch11:126；ch30「Dwight 上楼」实为 `bottom of the stairs` 但 md 未指方向；ch36「第一次」实指第二次出现；ch31「唯一一次说兄妹关系」实指对白非叙述）。
- `if... would` 是**虚拟式句法记法**，属禁令 3 明列豁免，不改。

## 遗留 ⚠️（提示型，不阻塞）
- `check_overview_full` 2 条：`Are you fucking my wife, brother?` 在 **ch17 与 ch19 都真实出现**（原文复述），章节标注有歧义。人工判：标 ch17 为首次出处可接受。
- `check_vocab` 48 条「基础档疑含超纲词」＝词长 ≥9 字符启发式。

相关：[[carry-me-to-my-grave-reading]] [[gate-tool-pitfalls-selfcheck]]