# 《The Art of Charming a Changeling》独立五步审查 — 缺陷清单与整改记录

- 书籍：`notes/books/novels/the-art-of-charming-a-changeling-by-sylvie-cathrall/`（25 章精读 + 3 篇总览）
- 触发：用户主动发起「对目标书籍执行五步审查，输出缺陷清单并完成整改」
- 执行依据：`AGENTS.md` 第 10 条 + `docs/新书启动模板.md:706-716` a–e 五小标题与四条纪律、`:728-735` 开工前材料三样
- 口径：a–e 全部完整执行，不降级；同会话盲区只在结论部分标注
- 原始门禁输出：`.memory/raw-gates/the-art-of-charming-a-changeling/2026-10-02-a_review_gates_full.txt`

---

## a. 第 3 条提交门禁全量重跑（不信报告数字）

完整 lane（目录内有 epub）。`bash scripts/gate.sh notes/books/novels/the-art-of-charming-a-changeling-by-sylvie-cathrall` → **EXIT=0**。

| # | 检测器 | 结果 |
| --- | --- | --- |
| ① | `verify_quotes` | **278/278 引文可核实（100%）**｜完全干净文件 26/26｜`--full` **整串取证 0** |
| ② | `check_vocab` | 词条行 2309｜**FAIL 0**｜WARN 41 |
| ③ | `check_entities` | 未知实体 **0** |
| ④ | `corruption_scan` | FAIL **0**｜报告 **0** |
| ⑤ | `sweep_full` | ✅ 本章命中 254｜⚠️ 跨章 0｜🔶 跨标签拼接 5｜❌ 全书查无 **0** |
| ⑥ | `check_short_quotes` | 短引语 2 条，✅ 命中 2｜❌ 查无 **0** |
| ⑦ | `check_chapter_quotes` | 25 章**全部 X/X in 本章 text** |
| ⑧ | `check_block_coverage` | ✅ 25 文件每块都进 verify_quotes |
| ⑨ | 导航/总结层英文核对 | ❌ 0｜⚠️ 0 |
| ⑩ | `sweep_analysis_inline` | ✅ 逐字 2687｜⚠️ 跨章 68｜🔶 拼接 8｜🟠 部分命中 7｜❌ 零命中 **0** |
| ⑪ | `audit_structure` | ❌ 0｜⚠️ 0｜🔀 0 |
| ⑫ | `check_anchor` | ❌ 凭空造词 **0**｜⚠️ 松散关键词 2 |
| ⑬ | 空段扫描 | 0 处 |
| ⑭ | `verify_overview_quotes` | 00_金句精选 19/19 ✅｜00_概述 口径外（见假红） |
| ⑮ | `check_overview_full` | 整串 64｜🔶 3｜❌ 0｜C 跨章多重命中 0｜E H1 语义错配 0 |

**a 步结论：门禁全绿，但主门禁有结构性盲区——`verify_quotes` 常规口径只比对引语前 52 flat 字符**，凡「前半逐字 + 后半改写/拼接」全部逃过。a 步实际靠 `--full` + `sweep_full` 🔶 查出 **5 条真缺陷**（下表 a1–a5）。

### a 步修掉的缺陷（5 条，全部阻断型）

| 编号 | 位置 | 缺陷 | 原文取证 |
| --- | --- | --- | --- |
| a1 | `ch06 chapter 6.md` 原句 9 | 凭空造的归属句 `Dr Hyverfell continued` | `text/ch06_chapter_6.txt:397` 无此插话，实为 `…obstacles and frustrations… the likes of which…`。已改回 `…` 形式，中文同步 `……` |
| a2 | `ch05 chapter 5.md` 原句 8 | `He grinned, apparently delighted by his own revelation.` 与 `As far as I can tell` **全书查无（fabricated）** | 真句在 `text/ch05_chapter_5.txt:269`（`“He didn’t paint it,” explained Vern. … If there’s a cottage exterior, it must have an interior.`），与前半句（`:260`）隔 8 段。已改为 `…and I live there!” … “He didn’t paint it,” …`；关键词同步换入 |
| a3 | `ch06 chapter 6.md` 原句 2 | 两处分隔文本被写成连续 | `text/ch06_chapter_6.txt:14` 与 `:20` 之间隔 `:16` 整段。中间补 `…`，中文加 `……`，删两个不成立的关键词 |
| a4 | `ch04 chapter 4.md` 原句 8 | `…looked at my painting.” “Why, that’s impossible!”` 之间缺 `…` | `text/ch04_chapter_4.txt:193` / `:197` / `:199` 三处分离。已补 `…`，三段逐一 flat 断言命中 |
| a5 | `00_金句精选.md:87` ⑫ | 中间省掉整句 `“You told me yourself that the Fairies of changeling paintings continue to age and grow and change, long after the artist completes their final brushstrokes.”` 却无 `…` | 源 `text/ch20_chapter_20.txt`。已补 `… ` 与 `……` |

### 判为合法、不改的 🔶（4 处）

`ch08 chapter 8.md` 原句 5 / 原句 6、`ch09 chapter 9.md` 原句 8 / 原句 9 —— 均为「对着同一对象的平行观察」，`…` 处省略的是另一个人的动作/反应，两半各自逐字命中（源：`text/ch08_chapter_8.txt:113`+`:116`、`:128`、`text/ch09_chapter_9.txt:350`+`:377`、`:353`）。属正当省略，`sweep_full` 的 🔶 是**措辞归类**（工具 `halves()` 把它归入「跨标签拼接」而非「省略号图式」），非缺陷。

**修复后复核**：`verify_quotes --full` 整串取证 **4 → 0**；`verify_overview_quotes` → `00_金句精选.md: 19/19 ✅`。

---

## b. 逐章归属

`python3 scripts/check_chapter_quotes.py <NN> "<md>" --out-dir "<书目录>/text"` 逐章实跑：

ch01–ch18 各 `10/10 in chNN text`｜ch19 `12/12`｜ch20 `14/14`｜ch21 `14/14`｜ch22 `13/13`｜ch23 `10/10`｜ch24 `9/9`（另有 1 条短引语未校验）｜ch25 `7/7`。

**b 步结论：无跨章错配，无遗漏块。**

---

## c. 结构扫描

| 检查 | 结果 |
| --- | --- |
| `audit_structure.py` | 扫 28 md / 281 引语块，❌ 0｜⚠️ 0｜🔀 0 |
| `check_overview_full.py` | A 整串 64 命中｜🔶 3｜⚪ 0｜❌ 0｜短引语 13；B 章节标签 不符 0；C 跨章多重命中 0；E H1 语义错配 0 |
| `check_struct_indep.py` | 报 25 处「引语块超出 3–8 配额」→ **假红型，只记不改** |

**`check_struct_indep` 假红定性依据**：`docs/新书启动模板.md:153` 明写「**格式自成一派的书是合法的**；模板只降低手打出错概率，**不作判红依据**」；脚本硬编码 `PROFILES["summary"]["RANGE"] = (3, 8)`（`scripts/check_struct_indep.py:51`）。实测本库含 `> **原句 N:**` 格式的书 **325 本**，块数众数 8（2986 次，25.5%）；仅 `notes/books/novels/` 203 本 7148 样本中 **9–14 块占 11.0%、>8 块占 14.7%**；同体裁参照书 `notes/books/novels/daggerbound-by-t-kingfisher/` 自身用 8/9/10 块。本书块数分布（ch01–18/23/24 各 10、ch19 12、ch20 14、ch21 14、ch22 13、ch25 7）属同体裁法内自选配额。

---

## d. 语义二审

### d-mech. 机械子项（模板指定的三个 `*_indep.py` 独立实现）

| 脚本 | 结果 |
| --- | --- |
| `check_struct_indep.py` | 25 处配额报警（假红，见 c 步） |
| `check_xref_indep.py` | 6 处 chNN 引用；英文证据报警 **0**；中文式待人判 6 → 逐条回原文核验**全为真引用** |
| `check_analysis_indep.py` | 抽出分析层英文片段 **405** 条，**全部逐字命中**，⚠️ **0** |

`check_xref_indep` 的 6 条逐条取证（全为真）：`ch04 chapter 4.md:12→ch03`｜`ch05 chapter 5.md:14→ch04`（`text/ch04_chapter_4.txt` 含 `no one else has ever looked`）｜`ch05 chapter 5.md:77→ch04`｜`ch06 chapter 6.md:67→ch04`（`second conversation`）｜`ch13 chapter 13.md:124→ch01`（`trouble`）｜`ch14 chapter 14.md:94→ch12`（`text/ch12_chapter_12.txt:455` `Florrie reached into the left pocket of her dress` + `:458` `She grasped in vain, finding nothing.`）。

### d1. 6 条「改写冒充逐字」（`check_analysis_indep` 抓出，全部阻断型，已改）

首跑抽出 **404** 条，报 **6 条**「整串查无但每个词都在书里」——即分析行里被引号包裹的英文。**逐条回原文定性，6 条全为真缺陷**：

| 位置 | 原写 | 原文 |
| --- | --- | --- |
| `ch05 chapter 5.md:75` | `"She had already nodded ten times"` | `Alas, she’d already nodded ten times in their conversation` → 改为 `"she’d already nodded ten times in their conversation"` |
| `ch05 chapter 5.md:93`（关键词） | `a cottage exterior must have an interior` | 实为 `If there’s a cottage exterior, it must have an interior` → 补 `If there’s` |
| `ch10 chapter 10.md:77`（读者视角提示） | `"he never once made a grand gesture of love"` | 实为 `That I had never once made a grand gesture of love.`（Vern 转述 Ardant，主语 I）→ 改 `That I had never once made…` |
| `ch10 chapter 10.md:105`（为什么这样写） | `"he might have concealed your message a little too brilliantly"` | 实为 Florrie 对 Lord Mauve 说的 `you might have concealed…`（人称 you→he）→ 改回 you |
| `ch15 chapter 15.md:15`（叙事手法） | `（她谈 relation like a conservator talk about a code）` | **既不逐字也不合语法**；`relation`/`code` 在 `text/ch15_chapter_15.txt` 中均 **0 次**。真句为 `those were the rules. The most vulnerable requires careful handling by the least vulnerable, to address the imbalance.` 与 `there are many ways to achieve a balance with someone.` → 已改写并逐段断言 |
| `ch20 chapter 20.md:153`（关键词） | `not especially burdensome` | 实为 `didn’t seem especially burdensome` → 补 `didn’t seem` |

**修复后**：`check_analysis_indep` ⇒ 405 条全部逐字命中、⚠️ **0**。

### d2. ⑩/⑫ 两项「⚠️ 提示」的复核（非缺陷）

- **⑩ `sweep_analysis_inline` 🔶 拼接 10 条**：8 条为合法的转述式省略号（`Oh, please don't cry! … If it's any consolation` / `I do not love your creation … it is that self I love` / `Please don’t stop … Don’t you dare.` / `growing... like blades of grass` / `He didn’t paint it… that’s my guess` / `was not … but …` / `The reason why … is because`），两半各自逐字命中且同章。
  另 **2 条是真缺陷（假红转真）**，属词表例句「凭印象重建英文」：
  - `ch08 chapter 8.md:222` 原写 `he asked whether a carrot would need its internal scales removed` —— 原文 `text/ch08_chapter_8.txt:320` 为 `he asked whether a carrot would need its “internal scales” removed`（**引号缺失**）→ 已补弯引号，逐字断言通过。
  - `ch19 chapter 19.md:209` 原写 `And you, replied Vern, are still wearing your gloves.` —— 原文实为 `“And you,” replied Vern, “are still wearing your gloves.`（**归属插话的引号全缺**）→ 已补，逐字断言通过。
  **修复后 🔶 10 → 8**，逐字 2685 → **2687**。
- **⑫ `check_anchor` 松散关键词 2 处**：工具自述「词在全书内、只是不在本引语块——多半是中译英或章内他处」，属**提示型**，只记不改。

---

## e. 总览层事实核对（独立子代理执行）

### E1. 章节标签对账（自写抽取器，非复用 `verify_overview_quotes`）

抽取 **56 条**引语↔`chNN` 配对，逐条 `in` 断言。初测 9 条 FAIL，逐条回查后拆分：

| 位置 | 原标注 | 实际 | 定性 |
| --- | --- | --- | --- |
| `00_金句精选.md:71` | Ch.20 | **ch15**（`text/ch15_chapter_15.txt:383` `"I can be patient, I promise."`） | **阻断型 · 已改** |
| `00_金句精选.md:99` / `:106` | Ch.24 / Ch.20 | 各自的引语标注无误，只是行内「紧接着」指代关系略绕 | 抽取器误配，**非缺陷**（提示型） |
| `00_情感节点.md` 6 处 | — | 5 条为脚本把前导 `"` 带进比对造成的假 FAIL | 假红型 |

### E2. 说话人与情节事实（逐条回 `text/` 前后 ~200 字符窗口，56 条）

| 位置 | 缺陷 | 原文取证 | 处置 |
| --- | --- | --- | --- |
| `00_情感节点.md:79` | **说话人错：Vern → 应为 Florrie** | `text/ch15_chapter_15.txt`（offset 14363）：`"I know you don't expect it." Florrie glanced down again. "But I was, well, rather under the impression that those were the rules. The most vulnerable requires careful handling by the least vulnerable, to address the imbalance." "Well, it is my inexperienced opinion," said Vern…` —— **Vern 是反驳者** | 已改为 Florrie |
| `00_金句精选.md:69` | 同源同错：「**他说出**」→ 应为「她说出」（该行 70 行自相矛盾：「Florrie 奉行半生的正是这条规则」） | 同上 | **错误源在此行**，已改 |
| `00_情感节点.md:64` | **说话人错：Florrie → 应为 Vern** | `text/ch09_chapter_9.txt`：`He seized the nearest hand-spindle… "I feel utterly useless." Before she knew what she was doing, Florrie placed her hand on his shoulder.` —— **Vern 说"utterly useless"，Florrie 是放手的人** | 已改为 Vern |
| `00_情感节点.md:30` | 引语不逐字：`"Yes,` | 原文 `text/ch03_chapter_3.txt:131` 为 `"Yes. The Resolute…`（**句点非逗号**） | 已改为句点 |

**最高级措辞计数（回原文数过）**：
- 「画中**唯一**的拱门」→ `text/ch01_chapter_1.txt:316` `"But the painting famously features only one arch"`，**计数 1 ✓**
- 「职业生涯**第一次**真正意义上的失手」→ `text/ch01_chapter_1.txt:19` 确证其 "utmost caution" 惯例 ✓
- 「Ceru 是全书**唯一**掌握技术真相的人」→ `text/ch18_chapter_18.txt:349` `"I can find no records whatsoever – not even a single footnote – that refer to someone leaving a changeling painting."` ✓，且 Ceru = Sir Cerulean（ch11 为 Mauve 作伪的 court artist）✓

**省略号判据（3 条告警全为合法）**：`Oh, please don't cry!`(ch01)…`If it's any consolation`(ch01)、`I do not love your creation`(ch20)…`it is that self I love`(ch20)、`Please don't stop`(ch19)…`Don't you dare`(ch19) —— 两半各自逐字命中且同章。

### E3. 跨书污染（58 个专有名词逐个 `grep -rl "<名字>" notes/books/ --include=*.md`）

| 名字 | 别书命中 | 回本书 `text/` 确证 | 结论 |
| --- | --- | --- | --- |
| Ardant / Chary Tesserine / Mim Glossmith / Lord Mauve / Petiole / Commonplace Palace / The Resolute Portrait / Old Amethyst Road / Stillscape / Predelle / Pigments / Paramours / The Sunken Archive / My Chorus | 无 | — | 干净 |
| **Ceru** | `the-ugly-history-of-beautiful-things…` | 本书 ch11–ch24 共 12 章 **148 次** | 本书伪造者，**非污染** |
| Idylls / Dwell | `leave-it-to-the-march-sisters…` | `text/ch22_chapter_22.txt:131/164` = 画名 `I Dwell in Idylls by Vetchley Glase` | 别书为常见词，**非污染** |
| Orbit | `translation-state…` | 本书 `text/` 中**不存在** | `00_概述.md:8` 出版社名（元数据行），**非污染** |
| Florrie / Vern / Mim / Mire | 4 本无关书 | 别书均为独立角色/常见词（`Verna`、`Mires`、ghost-tales 中 17 世纪士兵之妻 Florrie） | **无污染入本书** |

**相邻卷 Book 1（The Sunken Archive）专名零命中本书三篇** ⇒ E3 结论：**0 条跨书污染**。

### E4. 三篇内部一致性

| 事实项 | 概述 | 金句精选 | 情感节点 | 一致 |
| --- | --- | --- | --- | --- |
| 失手溶掉「唯一的拱门」(Ch.1) | :12 | :13 | :12 | ✓ |
| 规则作废 Ch.15、Florrie 为奉行者 | :30 正确 | :69/:70 **原自相矛盾** | :79 **原标错** | 已修 |
| "I can be patient"(Vern, ch15) | :30 正确 | :71 **原标 Ch.20** | — | 已修 |
| Ceru 身份（伪造者/画家） | :40 | — | — | ✓（`text/ch18_chapter_18.txt:349` 支撑） |
| Ch.13 = 用准备工夫回答 Ceru 的挑战 | :34 | — | 节点九 Ch.15 | ✓ |

**错误源定位**：说话人错的**源头是 `00_金句精选.md:69` 的「他说出」**，`00_情感节点.md:79` 跟随；章节号错的源头是 `00_金句精选.md:71`。均已就地修正。

**e 步改动范围**：`00_概述.md` **无改动**；`00_金句精选.md` 2 行；`00_情感节点.md` 3 行。全部经 dry-run（命中数均为 1）后 apply。

### e 步主会话独立复核

改动后由主会话直接回原文验证 5 处断言，全部正确：
- `text/ch15_chapter_15.txt`（offset 14192）确认「those were the rules…」由 **Florrie** 说出，Vern 是 `"Well, it is my inexperienced opinion," said Vern` 的反驳方 ✓
- `text/ch15_chapter_15.txt`（offset 20901）确认 `"I can be patient, I promise."` 紧接 `"I must finish those studies," she said` 之后、`"I just hope it will be worth your while," she murmured` 之前 ⇒ **Vern 所说** ✓
- `text/ch09_chapter_9.txt`（offset 19358）确认 `"I feel utterly useless."` 由 **Vern** 说出 ✓
- `text/ch03_chapter_3.txt`（offset 10186）确认 `"Yes. The Resolute Portrait…is a forgery."` 为**句点** ✓

---

## 工具盲区（本轮审查最有价值的产出）

1. **⭐⭐ `verify_quotes` 的 52 字符指纹盲区**：常规口径只比对引语**前 52 flat 字符**，凡「前半逐字 + 后半被改写/拼接」的缺陷全部逃过主门禁，**只有 `--full` 与 `sweep_full` 的 🔶 档能看见**。⇒ **完工报告里「278/278 100%」这句话不等于整串逐字**，必须同时报 `--full` 条数与 `sweep_full` 🔶 条数。本书 a 步的 5 条真缺陷有 4 条来自 `--full`。
2. **⭐⭐ 分析层里被引号包裹的英文同样受「逐字」约束，但两道引语门禁都看不见**（只锚 `> **原句 N:**` 行），只有 `check_analysis_indep.py` 抽得出。它报的「整串查无但每个词都在书里」应**默认按真缺陷处理**——那正是「凭印象重建英文」的指纹（本书 6 条全中）。
3. **⭐ 词表例句是独立于引语块的第二条「逐字」通道**，`sweep_analysis_inline` 的 🔶 与 `check_analysis_indep` 都能覆盖到例句行；本轮靠它抓出 `ch08` 引号缺失与 `ch19` 归属插话引号缺失 2 条。
4. **`verify_overview_quotes` 对 `00_概述.md` 报「覆盖缺口」是假红**：根因 `scripts/verify_overview_quotes.py:160-162` 的 `looks` 分支未过 `is_quoteish` 判定（后者注释 `scripts/verify_overview_quotes.py:82-86` 明说该判定就是为拒掉「中文说明行含引号」），而 `00_概述.md:8` 是出版社元数据行。**同库 `notes/books/novels/daggerbound-by-t-kingfisher/` 同报 ⇒ 全库性问题**，只记不改。
5. **`check_struct_indep` 的 3–8 块配额是假红**（见 c 步实测分布）。
6. **`verify_overview_quotes` 只验逐字、不验章节标签**（B 章节标签「不符 0」是因为 64 条「无标签未判」——总览层引语大多不带 `chNN` 标签）。e 步必须自建抽取器补这一层。

---

## 缺陷总计

| 步骤 | 阻断型（已改） | 提示型（未改） | 假红型（只记不改） |
| --- | --- | --- | --- |
| a | **5** | 0 | 0 |
| b | 0 | 0 | 0 |
| c | 0 | 0 | 1（3–8 配额） |
| d | **6**（分析层改写冒充逐字）+ **2**（词表例句引号缺失） | 2（松散关键词） | 0 |
| e | **5**（2 说话人 + 1 逐字 + 1 章节标签 + 1 同源） | 2（索引指代略绕） | 2（概述覆盖缺口 / 情感节点散文体） |
| **合计** | **18 条，全部已改** | 4 | 3 |

**涉及文件**：`ch04 chapter 4.md`、`ch05 chapter 5.md`、`ch06 chapter 6.md`、`ch08 chapter 8.md`、`ch09 chapter 9.md`（d2 复核）、`ch10 chapter 10.md`、`ch15 chapter 15.md`、`ch19 chapter 19.md`、`ch20 chapter 20.md`、`00_金句精选.md`、`00_情感节点.md`。`00_概述.md` 无改动。

## 复验（整改后终态）

```
① verify_quotes            === 总计 278/278 引文可核实（100%）；完全干净文件 26/26；--full 整串取证 0 ===
② check_vocab              词条行合计: 2309 / --- FAIL (0) --- / --- WARN (41) ---
③ check_entities           === 实体一致性检测：0 个文件存在未知实体 ===
④ corruption_scan          FAIL 0 处 / 报告 0 处
⑤ sweep_full               ✅ 本章命中 254 ｜ ⚠️ 跨章 0 ｜ 🔶 跨标签拼接 5 ｜ ❌ 全书查无 0
⑥ check_short_quotes       ✅ 命中 2 ｜ ❌ 全书查无 0
⑧ check_block_coverage     ✅ 块覆盖对账：25 个文件，每块都进了 verify_quotes 校验
⑨ 导航/总结层英文核对      ❌ 0 ｜ ⚠️ 0
⑩ sweep_analysis_inline    ✅ 逐字 2687 ｜ 🔶 拼接 8 ｜ 🟠 部分命中 7 ｜ ❌ 零命中 0
⑪ audit_structure          ❌ 结构缺陷 0 ｜ ⚠️ 提示 0 ｜ 🔀 映射不一致 0
⑫ check_anchor             ❌ 凭空造词 0 处 ｜ ⚠️ 松散关键词 2 处
⑭ verify_overview_quotes   00_金句精选.md: 19/19 ✅
⑮ check_overview_full      A 整串 命中 64 ｜ 🔶 拼接 3 ｜ ❌ 查无 0 ｜ E H1 语义错配 0
gate.sh EXIT=0
```

独立复核：`check_analysis_indep` ⇒ 抽出分析层英文片段 **405** 条，**全部逐字命中**、⚠️ **0**；`check_xref_indep` ⇒ 英文证据报警 0；主会话自写逐段核验器（按 `…` 切段 + `flat()` 断言）⇒ 25 章 260 个引语块**不命中 0 条**，总览三篇对 epub 直接核验**不命中 0 条**。

## 同会话审查的已知局限（`AGENTS.md` 要求仅在结论部分标注）

- a–e 五步全部完整执行，未以「同会话」跳过任何步骤；d 步的机械子项按模板要求用了 `*_indep.py` 三个独立实现，未复用写作期的 `audit_structure`/`check_crossref`/`sweep_analysis_inline` 口径。
- **但审查方与执行方仍是同一实例**：本书 25 章由 6 个并行子代理产出，本次审查除 e 步外均由主会话完成。同一实例的「换实现」能换掉代码路径，**换不掉同一套阅读习惯**——本轮 18 条缺陷中有 14 条的根因是同一个「先写中文、后凭印象重建英文」的写作模式，说明**写作期的自查习惯本身就是缺陷源**，而不是检查不够多。
- **说话人正确性无法机械化**（`AGENTS.md` 实测：`check_speaker_consistency.py` 全库 315 本只 1 条真缺陷、约 1/3 假阳，已明确不进门禁）。本轮 2 条说话人错全部由 e 步人工逐条回窗口发现，**若将来只跑门禁不跑 e 步，这两条会漏**。
- **建议固化的写作期动作**：对每一个英文串（引语正文、词表例句、分析行内的引号内容）做**逐串 `in` 断言**，而不是目视核对——目视时这些句子读起来都「像原文」。
