# 4-verdict.md · ch48 判定表（R5）

- 被审：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch48 the case is rebuilt on the board.md`
- 参照：`text/ch48_48.txt`（16,432 字符；5 段，`* * *` 分隔；全书第 48 章）
- 执行：R1/R2 由审查代理完成（`1-suread.json` 9 条事件带区间 / `2-machine.json` 10 块全中）；**R3/R4/R5 由派工人接手**（代理一次 "Model request failed"、重派后挂起被 TaskStop）

## 四组数

| 组 | 结果 |
|---|---|
| **逐字** | 10/10 引语逐字命中（自写严格子串比对 10/10、跨自然段 0）；词条例句 27/27 逐字命中；`chapter.sh` 报「查无 0」 |
| **对应** | **10/10 块成立**（引语选短 0 · 不对应 0 · 密度不足 0） |
| **形态** | H1 `# 48. The Police Station`＝本书众数；导航 5 项＝profile（mystery-thriller nav 5 项）；子项 4 项＝本书众子项集；块数 10 ∈ 本书区间 5–10（中位 7）⇒ **0 偏离**（引语偏长 1 块属提示型，见下） |
| **断言** | 核 28 条：**属实 27 · 阻断 1（已改）· 提示 5** |

## 阻断型（1 → 0）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 导航·视角称「最后由 Matt 与 Caius 在街边单独对话收束」；导航·叙事手法称「最后收在街边一段只有两个人的低声交代上」 | `text/ch48_48.txt` 第 4 个 `* * *`（@10457）之后的第 5 段（@11409–16432）：Amy 回到威洛手抄的 Horatio Combe 疟疾年日记 → holy lady → Alice de Burge → `knocked through a basement wall and into any subterranean ruins` → `Isolde and Andy sit down at 9.37 p.m. They don't move until 1.01 a.m.` → Robbie 的红鲱鱼质问 → Amy 的行动清单 → `‘Let's do both.'` | **与原文不符**：街边对话是第 4 段（全章倒数第二段），不是结尾；且 md 自身「一句话总结」所引的修女、雕像、地下通道**全部来自其后的第 5 段** ⇒ 摘要与导航互相矛盾 | **阻断 → 已改** |

## 提示型（只记不改 / 小改，已在 3-diff.md 记明）

1. 原句 2 引语 126 词，超 100 词阈值（`chapter.sh` ⚠️）：本章唯一的清单式复盘独白，拆块会毁其写法；分析覆盖范围未越出引语 ⇒ 不改，理由入册。
2. 原句 7「日志里那个小教派」→「Horatio Combe 那个小教派」（小改，提升可回溯性；依据 `His little cult` + 语料 `He led a group of occultists that lived in these same four houses in the square.`）。
3. 导航·人物弧线把「一切都对得上」与「我以为她只是个红鲱鱼」写成递进，实为同一段话内的两句 ⇒ 分析口径，不改。
4. **漏（提示级）· DJ Sonikk/Cecil 的爆料**（Mel 曾失控／编舞者卖 Jennifer 的照片／`As it transpires I should have.`）未进 md 分析层：md 已在导航写明该段属「杂音」＝**写明取舍理由**，且块数已达上限 10/10 ⇒ 判提示级，登记备查。
5. 日记「tunnels / hearts with worms」一段未成块，但其地下线索已由原句 8 的分析承接 ⇒ 视为已覆盖。

## 假红 / 跳过

- **假红 0**、**跳过 0**。
- **归属错误 0**：10 块的说话人逐块回原文核对（含 R1-S4 点名的「But why?」实为 Matt 之句，md 未误记）。

## 未覆盖（声明，不当干净）

- 10 个引语块的中文评析是否有力（纯评论，不判）；词表分档是否恰当（量具口径，例如 `Reformation`、`cult` 列入 ⭐⭐⭐ 偏宽）。
- 导航「三段插叙」的口径：源文 `* * *` 分 5 段、街边对话为其中第 3 段插叙、其后第 5 段回到主线，本判定依此；若按「分隔符数」口径读则应为 4 段，属措辞口径差异，判提示。

## 复验

```
bash scripts/chapter.sh "…/ch48 the case is rebuilt on the board.md"   → EXIT 0
bash scripts/gate.sh   "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell" → EXIT 0
自写三条探针（严格逐字 / 单自然段 / 分析层英文专名）                → 全书 395 块：P1 0 · P2 0 · P3 0
```
