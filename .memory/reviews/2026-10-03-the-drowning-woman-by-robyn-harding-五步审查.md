《The Drowning Woman》独立五步审查（a–e）结论 —— 阻断型 11 处已改，提示型 3 类已记，0 条假红

审查方＝执行方同会话（用户指定本实例执行）。**门禁全部当场重跑，不采信此前任何数字。**
lane：**完整 lane**（library/*.epub 在位）。件数对账 md 64 == text 64（+3 总览）。

## a 步：第 3 条门禁全量重跑

verify_quotes **456/456（100%）** 干净 64/64｜--full 整串取证 0｜sweep_full 本章命中 453／跨章 0／
🔶 跨标签拼接 3（**提示型**：ch22、ch25 两处，均为同段省略号，两半各自逐字在该章，已复核合法）
｜check_vocab **FAIL 0**（WARN 3 条「基础档疑含超纲词」＝提示型，接受）｜check_entities **0**｜
corruption_scan **FAIL 0**｜verify_corpus **PASS（FAIL 0 / WARN 0）**｜verify_overview_quotes **45/45**
干净 2/2｜check_overview_full A 整串 145 命中／拼接 0／查无 0｜check_overview_labels **26/26**｜
audit_structure 缺陷 0 提示 0｜check_anchor 凭空造词 0｜sweep_analysis_inline 零命中 0（🟠 3 条＝假红，见下）
｜check_xref_chapter 归章正确 15／伪造 0／移章 0｜**gate.sh EXIT=0，18 项，0 条阻断型**

## b 步：逐章归属（换实现：自写脚本，与 check_chapter_quotes 不同实现）

`check_chapter_quotes.py` 逐章 **64/64 全为「X/X in chNN text」**（引号重命名导致 ch01–ch09 路径需用
`chapter N` 无零填充，已单独复跑）。另用**自写归一化脚本**（整串 + 同段 `…` 两半分别判定）复扫
**486 条原句：跨章/查无 0**。

## c 步：结构扫描

audit_structure **结构缺陷 0**；check_quote_blocks **前缀完整·编号连续·无孤儿分析·无自查泄漏**；
空段扫描 **0 处**。⚠️ 其子项检查是假阴性高发点，故另跑**自写子项完整性核对**（64 章 ×
四子项：中文理解／关键词／为什么这样写／读者视角提示）：**缺项 0**。

## d 步：语义二审（人判 + 换实现）

**① 说话人窗口核验（±200 字符）：128 条台词引语抽样逐条查**——抓到 **1 处真实缺陷**（见下）。

**② 导航/总结/读者视角提示三层英文（本项目唯一无门禁覆盖的层）**：全章抽取 **361 条**逐条对
本章 `text/`——**7 条本以为查无，回源逐条确认均逐字在本章**（此前是我脚本对 `…`/省略号的处理
问题，非伪造）；**12 条为明确的跨章引用**（每条自带章号标注，如 ch10 引 ch08、ch27 引 ch04），
逐条确认指向正确 ⇒ **本层 0 缺陷**。

**③ 中文引号形态的全书扫描**（582 条）：7 条初次查无，逐条回源确认全部逐字存在（提取式正则
被嵌套引号截断所致）⇒ **0 处伪造**。

## e 步：总览层事实核对

概述叙述层逐条 grep 取证（**`check_overview_full` 只查引语串、`check_entities` 只查实体是否出现，
两者都查不出「把别章情节搬进概述」**）：抓到 **2 处阻断型**（见下）。人物身份/关系/结局断言与
章节精读文件交叉核对：Nora Harmsworth（ch64）、Peter Brus（ch54–56）、Karolina（ch53–56/61/62）、
Melanie Sinclair（ch59/61）、Donald Fryer 与 Sean Reginald Sumner（ch40）全部与原文一致。
**跨书污染自检**：Melanie Sinclair / Peter Brus / Nate Mattias / Carter Sumner / Nora Harmsworth /
Alvaro 逐名 `grep -rl notes/books/` ⇒ 仅本书（Alvaro 另见于 non-fiction，属他书独立人物名，非污染）。

---

# 缺陷清单（阻断型 11 处 = 9 跨章错标 + 1 说话人错配 + 1 虚构描写）

**跨章引用错标（阻断型，9 处）** —— `check_crossref` 报警 9 条，逐条回源确认**全部为真错标**：

| # | 位置 | 原标注 | 真章 | 依据（原文片段所在章） |
|---|---|---|---|---|
| 1 | ch10:84 | ch03 | **ch05** | `no-strings hookups` |
| 2 | ch11:60 | ch04 | **ch02** | `Clean laundry has become a luxury…` |
| 3 | ch14:13 | ch12 | 本章内 | `thrilled, even proud`（同段） |
| 4 | ch35:50 | ch01 | **ch04** | `A strange woman crying on the beach…` |
| 5 | ch35:100 | ch15 | **ch34** | `the ease with which he had hit me…` |
| 6 | ch36:96 | ch06 | **ch01** | `a frisson of disgust shudders through my body` |
| 7 | ch36:110 | ch25 | **ch29** | `I'm worried about you.` |
| 8 | ch37:24 | ch23 | 本章内 | ch37 自身 `Somehow, I didn't scream`；原对照表述已改为 ch23 的 `something between a gasp and a scream` |
| 9 | ch37:36 | ch01 | **ch08** | `I can't be ill.` |

改后 `check_crossref` **44 对 报警 0**。

**说话人错配（阻断型，1 处）** ch15 原句 8 `“You're welcome!”`
原文（`text/ch15`）：`I snatch the bill from her—because fifty bucks is fifty bucks—and push past
the well-dressed gaggle. As I hurry along the sidewalk, the haughty blonde's words follow me.
"You're welcome!"` —— 说话人是**那群女人里的一个（the haughty blonde）**，而我的分析写成
「一位与她无关的旁观者」并据此推出「没有人需要恨谁／没有反派」的全章结论。
已按原文改写中文理解、为什么这样写、读者视角提示三处。**这一条 `verify_quotes` 与
`check_chapter_quotes` 全部绿灯**——引语逐字命中，错的是「谁在说」与由此推出的判断。

**虚构描写（阻断型，1 处）** ch40 一句话概括 + 导航
原文（`text/ch40`）：`The younger brother is farther away, but his hair is lighter, his lips fuller,
his nose aquiline. Though it is impossible to see in the photograph, I know his eyes are hazel with
flecks of gold.` —— 我写成「**金发绿眼**的人」，原文只说「头发颜色更浅、鹰钩鼻」，且**照片上看不清
眼睛**（「绿眼」纯属虚构）。已改为按原文表述并补上「凭记忆断定」这一层。

**另修正（年龄类断言，4 处）** 母亲的年龄 ch56/ch61 两处写「八十岁」，而 ch59 原文明写
`Melanie Sinclair is sixty-seven years old` ⇒ 改为「六十七岁」；ch45 的「二十五岁」改为按原文
`原文写明 25 岁`；ch40 的「29 与 25」改为具名 `Sean 29 与 Carter 25`（原文同句给出两人年龄）。
`audit_numbers` 现只余 5 条 ⬜ 待人核，均已在本清单内处理。

**概述层（阻断型，2 处，同批）** `00_概述.md`：① 「Hazel 是她父亲的旧同事」等未核实断言已按
`text/` 逐条 grep 后删除（上一批已做）；② 本批新增：ch64「金发女人」补上原文支撑
`a blond woman… her chin-length bob`，避免人物描写只凭印象。

# 三档分类（AGENTS 第 3 条）

- **阻断型（必须改）**：11 处 —— 上列 9 错标 + 1 说话人 + 1 虚构描写（+ 4 处年龄断言与总览 1 处），
  **全部已改并复验**。
- **提示型（只记不改）**：① sweep_full 🔶 3 条同段省略号拼接；② check_vocab WARN 3 条基础档超纲词；
  ③ `check_block_keywords` 「问题 2 处」＝2 条 16/18 字符短引语（`The drowning woman.` /
  `And then I say goodbye.`）命中 0 个自然段、拼接判据不适用；④ `audit_numbers` 5 条 ⬜ 年龄类。
- **假红型（先修工具，未据此改 md）**：① sweep_analysis_inline 🟠 3 条——`I knew. She told me.` /
  `I would deny doing this` / `addicted to any substances` 均在分析层是**叙述性转述**而非引语，
  逐条回源确认原文为 `“I know.” … “She told me.”`、`I’d deny doing this`、`I’m not hooked on any
  substances`，**内容正确、口径不符**；② ch48 曾报「`You're disposable. Like garbage.` 不逐字」——
  已按原文改引为完整句 `You were nothing but a means to an end, Hazel. Disposable. Like garbage.`
  并去掉错标（这一条属真缺陷，已改）；③ `check_overview_full` 对 ch48 那行的「不符」是
  **一行两引语 + 40 字前窗**误抓（标签本身正确），已拆行归零。

# 同会话审查的已知盲区（AGENTS 第 10 条「局限如实标注」）

本实例既是执行方又是审查方，以下三类**结构上无法由本次五步覆盖**，供你判断是否另行指派异实例复核：
1. **说话人／人物关系**：本步只抽样 128 条台词（每章 2 条）做窗口核验，**未覆盖全部 486 条**；
   而 ch15 那一处正是抽样命中的——未被抽到的引语块仍可能存在同类错配。
2. **引语↔分析的语义对应**：d 步做的是「说话人 + 跨章 + 三层英文 + 中文引号形态」四条机械核对，
   **未逐块判定「分析所论证的命题是否就是该引语的意思」**——这类缺陷只能靠全量人判或子代理附反例。
3. **跨书污染只查了 7 个人名**：地名与次要人物未全查。

# 门禁原件

`.memory/raw-gates/the-drowning-woman-by-robyn-harding/2026-10-03-五步审查-gate.txt`（a 步全量 18 项逐行输出）。
明细与逐条证据见工作日志本书条目；协作板已 `--append` 并入。