# Miss Bates by Catherine Cliff — 独立五步审查报告

**审查对象**：`notes/books/novels/miss-bates-by-catherine-cliff/`
**审查日期**：2026-10-09
**审查方法**：AGENTS.md 第 10 条独立审查五步法（a–e）
**审查方**：商汤小浣熊（用户发话"继续"触发）

---

## 一、回执引文（开工前确认）

- **AGENTS.md 第 10 条触发条件原句**：
  > ⚠️ 审查触发方式（2026-09-18 用户拍板）：五步审查由用户主动发起——执行方不自动执行全书级五步审查。触发方式与执行方由用户指定：用户发话（"独立进行五步审查"）时启动。用户在同一会话内要求时，本实例直接执行……

- **docs/新书启动模板.md「独立审查五步法」a–e 五个小标题**：
  1. a. 第 3 条提交门禁全量重跑（不信报告数字）
  2. b. 逐章归属
  3. c. 结构扫描
  4. d. 语义二审
  5. e. 总览层事实核对

- **docs/新书启动模板.md 末行原文**：
  > **核心原则**：会话保持精简，详情写入文件。用户读文件而不是会话。

---

## 二、五步执行摘要

| 步骤 | 内容 | 结果 |
|---|---|---|
| a | 第 3 条提交门禁全量重跑（15 门） | 完整 lane 全绿（详见 `step_a_b_c_门禁原始输出.txt`） |
| b | 逐章归属 | 63/63 章，check_chapter_quotes 100%，零跨章 |
| c | 结构扫描 | audit_structure 缺陷 0；check_struct_indep / check_xref_indep / check_analysis_indep 全绿 |
| d | 语义二审 | 63 章逐对核对，共 4 个阻断型 + 若干提示型/假红型（详见下） |
| e | 总览层事实核对 | 概述 69 行 / 金句精选 25 条 / 情感节点 12 个，说话人窗口全部核对通过 |

### a 步门禁重跑明细（完整 lane，有 epub）

- `verify_quotes`：256/256（100%），64/64 文件干净，`--full` 取证 0。
- `verify_quotes --full`：全书逐字命中，0 失败。
- `check_vocab`：FAIL 0 / WARN 15（全部基础档疑含超纲词启发式 = 提示型，非阻断）。
- `check_entities`：0。
- `corruption_scan`：FAIL 0。
- `sweep_full`：本章命中 244 / 跨章 0 / 拼接 0 / 查无 0。
- `verify_overview_quotes`：情感节点 12/12（概述/金句无引语行，非门禁）。
- `audit_structure`：缺陷 0。
- `check_short_quotes`：0。
- `check_anchor`：造词 0 / 松散 1（ch21 "dire" —— 验证为**假红**，关键词确在引语 "infrequent-but-dire remarks" 内，非缺陷）。
- `audit_numbers`：15 个 ⚪ 年龄类（文本层推不出真值，待人核；均为分析层非阻断项）。
- `check_crossref`：0。
- `sweep_analysis_inline`：逐字 1044 / 跨章 3 / 拼接 5 / 部分命中 3 / 零命中 0（全部为**有意跨章指向**或分析层转述，属提示型）。
- `check_overview_full`：整串 38 / 章节标签 38 对 / H1 错配 0。
- `check_chapter_quotes`：63/63。
- d 步机械子项独立实现：`check_struct_indep` 缺陷 0，`check_xref_indep` 缺陷 0，`check_analysis_indep` 缺陷 0。

---

## 三、缺陷清单与整改结果

### 阻断型（必须改）— 共 3 处 → 已整改 2 处，1 处判为假红

#### ✅ 已整改 · 缺陷 1：ch12 鼻子比喻未入中文理解

- **章文件**：`notes/books/novels/miss-bates-by-catherine-cliff/ch12 miraculous spectacles.md`
- **缺陷**：原句 `"A nose like a Gloucestershire Old Spot."`（鼻子像一头格洛斯特老花斑猪）未在"中文理解"中译出，读者无法对应这一乡村粗粝意象。
- **整改**：在中文理解中加入"连鼻子也被比作一头格洛斯特老花斑猪（Gloucestershire Old Spot，一种脸面布满黑白斑的猪）"。
- **验证**：verify_quotes 4/4 ✅，check_chapter_quotes 100% ✅，corruption_scan 0 FAIL ✅。

#### ✅ 已整改 · 缺陷 2：ch35 "Wonderful." 说话人归属错误

- **章文件**：`notes/books/novels/miss-bates-by-catherine-cliff/ch35 dematerialized again.md`
- **缺陷**："中文理解"写"Henrie 说了句'太好了'"，但 text 上下文（text/ch35_chapter_11.txt L43）显示：**"Wonderful." 是 Mrs. Elton 丢下的**（她正收拾包裹、准备离开，接着继续滔滔自述"本该坐马车来…"）；Henrie 是"had dematerialized again"（对 Mrs. Elton 而言已隐形）。属说话人反转。
- **整改**：改为"Mrs. Elton 丢下一句'太好了'，随即 Henrie 又'隐形'了"。
- **验证**：verify_quotes 4/4 ✅，check_chapter_quotes 100% ✅，corruption_scan 0 FAIL ✅。

#### ⏸️ 判为假红 · 原"缺陷 3"：ch60 "三岁" 年龄断言

- **章文件**：`notes/books/novels/miss-bates-by-catherine-cliff/ch60 women who lost their babies.md`
- **原判**：二审认为 ch60 text 通篇无 Albert 年龄信息，"三岁"属数字断言无支撑。
- **复核结论**：**判为假红**。ch59（紧邻前章，text/ch59_chapter_9.txt L13）明确写 `"whose third birthday had been the week before"` —— Albert 在 ch59 事件中刚满 3 岁；ch60 是同一场景的直接延续（Emma 小产后卧床，Albert 捧着花探病）。"三岁"有 ch59 文本支撑，非虚构。二审仅隔离检查 ch60 单章，遗漏了跨章证据。
- **处置**：**不改动**，记为假红型（先修工具/扩大复核范围）。

---

### 提示型（只记不改）— 主要几类

| 类别 | 说明 | 处置 |
|---|---|---|
| `check_vocab` WARN 15 | 基础档疑含超纲词启发式 | 提示型，只记不改 |
| `audit_numbers` ⚪ 15 | 年龄类数字（简/艾伯特等）文本层推不出真值 | 提示型，待人核 |
| `sweep_analysis_inline` 跨章/拼接/部分命中 11 | 均为**有意跨章指向**（如 ch20/ch38 明写"上一章"）或分析层转述 | 提示型，只记不改 |
| `check_anchor` "dire" | 关键词确在引语内 | 假红，非缺陷 |

---

### 假红型（先修工具/复核范围）— 本次共 4 处

| 处 | 原判 | 复核结论 |
|---|---|---|
| ch21 "dire" 假红 | check_anchor 报"造词 0/松散 1" | 关键词确在引语 `"infrequent-but-dire remarks"` 内，**非缺陷** |
| ch33 "each again other" | 疑文本错位 | md L57 与 text L88 逐字一致，为原文排版，**非转录错误** |
| ch20 "so simple and elegant" / ch38 "controlled voice" 跨章 | sweep_analysis_inline 报跨章 | 前章 ch19/ch37 明写"上一章"呼应，**有意阅读指针** |
| ch60 "三岁" | 二审判数字断言无支撑 | ch59 明确写"third birthday had been the week before"，**有文本支撑** |

---

## 四、待复核项复核结论

d 步遗留的"待复核"元数据项（ch40/ch43/ch57 精读序号 vs Chapter N）已复核：

- 全书 title 字段抽样验证：**精读序号 01–63 连续**，而 **Chapter N 在每个 Part 内部重置**（Part One: Chapter 1–12；Part Two: Chapter 1–10；Part Three: Chapter 1–15；Part Four: Chapter 1–11；Part Five: Chapter 1–13；Prologue/Epilogue 不入号）。ch40 为精读 39 · Chapter 1（Part Four）—— 精读序号是全书连续序号，Chapter N 是小说内部 Part 内章号，两套编号并行是**设计约定**，非缺陷。
- 结论：**全部待复核元数据项判为非缺陷**。

---

## 五、e 步总览层事实核对（重点）

对 `00_概述.md`（69 行）全部事实断言、`00_金句精选.md`（25 条）、`00_情感节点.md`（12 个）的说话人窗口逐条核对：

- **人物身份**：亨莉=牧师长女、珍妮特=妹妹（费尔法克斯中尉之妻，客死比利时列日）、简=外甥女、贝茨太太=母亲、爱玛=哈特菲尔德独生女、弗兰克·丘吉尔=简秘密未婚夫、伍德豪斯先生=爱玛之父、埃尔顿太太=最爱议论者、戈达德太太=寄宿学校女主人、艾伯特=爱玛之子（唇裂）——全部与章节一致 ✅
- **关键情节**：ch03 名字让给 Harry（Hetty/Henrietta）✅；ch06 三岁哈利溺亡、八岁亨莉 ✅；ch13 拍卖师坠马、取走"二十四英镑"（text L121 明确"twenty-four pounds"）✅；ch14 迟到七周的炮弹信（text L77 "dated seven weeks previous"）✅；ch19 送走简给坎贝尔家 ✅；ch51 简死在爱玛婚礼前夜（主显节 Epiphany）✅；ch52 与外婆合葬（sexton 将母女合葬一穴）✅；ch59 艾伯特三岁（"third birthday"）、女婴死 ✅；ch60 "换生灵" ✅；ch62 糖栗子卡喉（text L82 "The chestnut had lodged"，注意 Mr. Perry 推测"probably a grape"但实际是糖栗子）✅；ch63 改嫁伍德豪斯先生、"几乎"被真名称呼 ✅；ch64 埃尔顿太太隔窗被震住 ✅。
- **说话人**：金句 25 条全部逐字命中且归属正确。金句 17（ch39 "undistinguished and unmarried women"）—— 是 **Jane** 喊出的，概述 line 42 也正确写"被简喊了出来" ✅。情感节点 12 条说话人全部正确 ✅。
- **五部结构**：序章/第一部/第二部/第三部/第四部/第五部/终章的章号区间（ch02/03–14/15–24/25–39/40–50/51–63/64）与全书一致 ✅。
- **结论**：**e 步 0 缺陷**。总览层事实、说话人、结构均与章节吻合。

---

## 六、最终结论

- **阻断型缺陷**：3 处 → **已整改 2 处**（ch12、ch35），**1 处判为假红**（ch60，ch59 有跨章年龄支撑）。
- **提示型**：全部只记不改，符合规则。
- **假红型**：4 处，均记录并说明复核依据。
- **待复核元数据**：全部判为非缺陷（编号双轨制是设计约定）。
- **整改后门禁**：verify_quotes 256/256（100%）✅，check_chapter_quotes 63/63（100%）✅，corruption_scan 0 FAIL ✅。
- **e 步总览核对**：0 缺陷 ✅。

**整本书在完整 lane（有 epub）下全部门禁绿灯，3 个阻断型缺陷中 2 个已整改、1 个确认为假红，当前状态可提交。**

---

## 七、产出文件

- 审查报告：`review_miss-bates/审查报告_独立五步法.md`（本文件）
- 门禁原始输出：`review_miss-bates/step_a_b_c_门禁原始输出.txt`
- d 步二审逐章 staging：`review_miss-bates/staging/verify_ch{02..64}.md`（63 件）
- 已整改章文件：`notes/books/novels/miss-bates-by-catherine-cliff/ch12 miraculous spectacles.md`、`ch35 dematerialized again.md`