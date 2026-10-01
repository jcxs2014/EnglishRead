# 《Nine Perfect Strangers》独立五步审查 · 缺陷清单

- **审查方**：DSH-Mac（与写作方同会话；按 AGENTS 第 10 条「用户在同一会话内主动要求时，本实例直接执行」，a–e 五步**完整执行、未降级**，局限只在报告结论处如实标注）
- **被审对象**：`notes/books/novels/nine-perfect-strangers-by-liane-moriarty/`（79 章 md + 79 件 `text/` + epub，完整 lane，**无总览三篇 `00_*.md`**）
- **时间**：2026-10-01
- **门禁原始逐行输出**：`.memory/raw-gates/nine-perfect-strangers/2026-10-01-review-a-e-gates.txt`（a 步全量重跑，135 行）
- **分档口径**：AGENTS 第 3 条三档（阻断型必改／提示型只记不改／假红型先修工具）

---

## 一、缺陷汇总（实缺陷 **14 条**，全部已修）

> 计数规则：只把「md 中必须改的事实/措辞/结构错误」计入；**假红型与工具口径错一律不计入**（列于第三节留痕）。

### 阻断型 9 条（引语与原文不符 —— 六道门禁全部漏网）

| # | 位置 | md 写作 | 原文实际 |
|---|---|---|---|
| 1 | `ch22 Yao.md` 原句15 | `said into her ear` | `said into his ear` |
| 2 | `ch25 Masha.md` 原句14 | `She had only ever seen her baby` | `She had only ever seen him as her baby` |
| 3 | `ch31 Lars.md` 原句17 | `we should just go for it?`（Jessica 台词） | `we should just go with it?`（同块 Lars 答句 `go for it` 本身正确） |
| 4 | `ch41 Zoe.md` 原句21 | `He gripped his arm` | `He gripped her arm` |
| 5 | `ch65 Masha.md` 原句16 + 关键词行 | `Yet he offended him` | `Yet she offended him` |
| 6 | `ch75 One week later.md` 原句3 | `the crooks of her arms` | `the crooks of their arms` |
| 7 | `ch13 Masha.md:206` | 引语 `"We will begin."` + 中文理解/关键词全部围绕该句 | 该块讲 humility，**引语与四子项整体错配**；真引语为 `People in this country admired humility. The biggest compliment you could give a successful woman was to describe her as "humble."` |
| 8 | `ch14 Frances.md:76`、`:326` | 分析层写 `"Touch me, please, please touch me"（ch07）` | ch07 原文 `Touch me, she thought, and in her head it was an anguished wail. Please, please touch me.`（`…` 拼接会被 flat 比对判查无） |
| 9 | `ch47 Frances.md:226` | 「ch29 里 Zoe 那句"他没留下一句短信"（ch26：Zach didn't leave a note or a text）」 | 章号与措辞**双错**：原文在 **ch26**，说话人是 **Napoleon**，原文 `The kid did not leave a note or a text. He did not choose to explain his actions.` |

### 阻断型 1 条（分析层虚构原文，全书查无）

| # | 位置 | 问题 |
|---|---|---|
| 10 | `ch06 Frances.md:36` | 分析层以引号引用 `"It was a beautiful smile: warm and generous."` —— **该句在 epub 全文查无**（`beautiful smile` / `warm and generous` 均 0 命中）。属「引用冒充逐字」类虚构 |

### 阻断型 2 条（无候选档位被误删 / 结构缺失）

| # | 位置 | 问题 |
|---|---|---|
| 11 | `ch56 Yao.md` / `ch77 Epilogue 1.md` / `ch78 Epilogue 2.md` | 三章**无高级候选**，按「某档无候选整段删除」删除了 `### ⭐⭐⭐ 高级` 标题 —— 该处置**正确**，但 `check_struct_indep.py` 的通用模板会报缺档。**判定：非缺陷，是工具口径错**（见第三节） |
| 11 | `ch67 Heather.md` | 编号 `[0,1,…,8,10,…,21]`：首块编号 **0**、**原句 9 整块丢失**（批次 22 修重复引语删块后未重排）。已补写原句 9（Masha 用 HR 程序威胁 Yao、Napoleon 拆弹式回应）并全章重排为连续 **1–22** |

### 提示型 4 条（已改）

| # | 位置 | 问题 | 处置 |
|---|---|---|---|
| 12 | 39 章共 **105 个精读块**缺「关键词」子项 | 只有 3 子项（中文理解/为什么这样写/读者视角提示） | **已补齐 105 块**，关键词一律从该块引语原文抽真实英文短语 |
| 13 | `ch16 Jessica.md` 原句9 | 用「**中文解读**」代替「中文理解」 | 已改 |
| 14 | 6 章导航层 **Tropes 标签用英文**（ch01/ch02/ch03/ch04/ch05/ch08） | `the patient who refuses help` / `the reluctant retreat-goer` / `arrival as disillusionment` / `brochure vs barbed wire` / `retail therapy for a marriage` / `the silenced whistle-blower` | 全部改为纯中文标签（既有教训：导航栏英文 trope 名会触发实体检查误报） |
| 15 | `ch48 Zoe.md:42` | 关键词含原文不存在的词形 `because of the fainting?` | 已删（原文只有 `fainted` / `faint`） |

---

## 二、⭐ 本轮最有价值的发现

### 发现 1：**词级改写**是六道门禁的共同盲区，只有整串 flat 比对能抓

本批 6 条引语缺陷（#1–#6）全部是**一个代词/一个虚词的替换**（his↔her、he↔she、her↔their）与**固定搭配改写**（go for it↔go with it）。这类缺陷：

- `verify_quotes.py`（52 字符指纹）**看不见** —— 指纹匹配对长句只比头尾片段
- `check_chapter_quotes.py`（逐章归属）**看不见** —— 句子在本章，只是字不对
- `check_vocab.py` / `check_entities.py` / `corruption_scan.py` / `sweep_analysis_inline.py` 均**看不见**
- ✅ **只有 `sweep_full.py`（整串 flat 比对）能抓**

**⇒ 建议：`sweep_full.py` 应从「条件性工具」升为**长篇常规门禁的第 ⑯ 项**（它有 epub 依赖，但在完整 lane 里恒定可用）。本书 25 批次全绿下仍藏 6 条，全部由该口径一次扫出。

### 发现 2：「分析层引用冒充逐字」是六道门禁的**全盲区**

`ch06:36` 的 `"It was a beautiful smile: warm and generous."` 是**凭印象编造的引语**（写分析时顺手补一句"应有的原句"）。它不在引语行（`> **原句 N:**`）内，因此：

- `verify_quotes` / `check_chapter_quotes` 不扫分析层
- `sweep_analysis_inline.py` 扫分析层行内英文 —— 但该句是**带引号的整句**，属它「引号内片段」口径……实测 ✅ 逐字 5009 / ❌ 零命中 0，**即它也没抓到**（疑似被 52 字符或引号内逃逸豁免）

**⇒ 处置：`check_analysis_indep.py`（d 步第二实现）是本类缺陷的唯一拦截点，且它只报「整串查无但每个词都在书里（拼接或改写冒充逐字）」为 ⚠️ 不判红。本轮该 ⚠️ 报了 30 条，人判后确认 1 条真缺陷。强烈建议把「分析层带引号整句回查 epub」列入五步审查 d 步的固定动作。**

### 发现 3：自写校验脚本会**双向**出错（本轮两度）

- **第一次**：自写 flat 比对工具因 `re.split(r"/|\.\.\.")` 只比最长段 + `SequenceMatcher` 窗口锚定失准，一轮报出 30+ 假红（ch03/ch06/ch08/ch11/ch12/ch16/ch53/ch76 …），**经 grep 逐条回查全部确实存在于本章 text**。
- **第二次**：为核 30 条 ⚠️ 自写的批量比对脚本**全报 ❌**（包括 `It was a beautiful smile` 这种真缺陷与 `Frances's fear peaked` 这种合法缩短一并判错）。

**⇒ 已固化的纪律：自写脚本报「大面积报警」时必须先怀疑脚本，逐条 grep 原文的上下文窗口（而非整串匹配）再定级。** 判据要放宽到「合法截断／换主语／词形变化」都算命中，只把「原文查无 + 只在别章」当缺陷。

---

## 三、假红型与工具口径错（不改内容）

| 来源 | 报警 | 复核结论 |
|---|---|---|
| `check_struct_indep.py` | ch54/55/58/59/60/61/62/63/64/65/66/67/68/69/71/72/73/74/75/76「引语块超出 3–8 配额」 | **假红**：工具用**通用模板默认值**，本书自校准众数为 **14**（`audit_structure.py` 按书内众数自校准，⚠️21 全为提示型）。本书是长篇群像，多章引语 14–38 条属正常 |
| `check_struct_indep.py` | ch56/ch77/ch78「词汇档位标题缺 `### ⭐⭐⭐ 高级`」 | **假红**：三章原文候选为 0（ch77）或不足（ch56/ch78），按 AGENTS 规则「某档无候选必须整段删除该档标题」，**删掉才是正确** |
| 自写脚本 | 24 条分析层短语「原文查无」 | **假红**：全部是**合法缩短／换主语／词形变化**（如 md `He remembered the feeling of the needle in her neck`、原文 `He remembered the feeling of the needle in his neck`……经逐条 grep 确认）；判据过严所致 |
| `check_vocab.py` | 「基础档疑含超纲词」WARN | **假红**：长度型提示（`len(w)>=9` 且不在 209 词表内），AGENTS:154 列为「只记不改」 |

---

## 四、终态门禁（整改后全量重跑）

| 项 | 结果 |
|---|---|
| ① `verify_quotes` | **1503/1503（100%）**｜完全干净文件 **79/79** |
| ② `check_vocab` | 词条行合计 **3796** / **FAIL 0** |
| ③ `check_entities` | **0** 个文件存在未知实体 |
| ④ `corruption_scan` | **FAIL 0** |
| ⑤ `sweep_full` | 本章 **1478**｜跨章 0｜跨标签拼接 25｜**全书查无 0** |
| ⑥ `check_short_quotes` | 命中 **7**｜others 0 |
| ⑦ 逐章归属 | **79 章全部 X/X in 本章 text** |
| ⑧ 块覆盖 | 79 个文件，每块都进校验 |
| ⑨ 导航/总结层英文 | **❌ 0 ｜ ⚠️ 0** |
| ⑩ `sweep_analysis_inline` | 逐字 **5009**｜跨章 69｜拼接 7｜部分命中 41｜词形 1｜**零命中 0** |
| ⑪ `audit_structure` | **❌ 0 ｜ ⚠️ 21（全为引语数偏离众数）｜ 🔀 0** |
| ⑫ `check_anchor` | 凭空造词 **0** |
| ⑬ 空段扫描 | **0 处** |
| ⑭⑮ | N/A（本书无 `00_*.md`） |

**d 步第二实现**：`check_struct_indep` / `check_xref_indep` / `check_analysis_indep` 三份全部运行；`check_xref_indep` 英文证据报警由 **3 → 0**；`check_analysis_indep` ❌ 由 7 → 0。
**e 步**：N/A（本书无总览三篇）。
**独立结构复扫**（自写，79 文件）：编号连续性 0 异常、四子项齐备 0 异常、块内重复引语 0。

---

## 五、同会话审查的已知局限（如实标注）

- 审查方与写作方同属一个会话上下文，**不能排除共享同一批认知偏差**（例如同一处情节理解错误会在写作与审查中同时成立）。真正的独立防线是**把 md 里每个 `chNN` + 紧随的英文片段抽出来回查 `text/chNN`**，本轮已对 3158 条分析层片段全量执行。
- `check_speaker_consistency.py` 经实测不可靠（全库 3159 本只 1 条真缺陷、约 1/3 假阳），本书**未跑**，说话人正确性只做了抽查级核对（本轮抓到 #3、#9 两处说话人/归属问题）。
- 四类机械层查不了的项（说话人是否正确、跨章引用是否指对、引语与分析是否仍对应、计数断言）本轮以人工逐对核对 + 第二实现补充，但**不构成形式化保证**。
