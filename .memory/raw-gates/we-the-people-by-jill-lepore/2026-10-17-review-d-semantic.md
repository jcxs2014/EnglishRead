# d/e 步语义二审报告

> 审查方：实例 Opencode-Mac（独立审查方）  
> 对象：`notes/books/non-fiction/we-the-people-by-jill-lepore/`（19 个精读单元 + 总览三篇）  
> 日期：2026-10-17  
> 口径：第 10 条 d 步（引语↔分析逐对核对）+ e 步（总览层事实核对）。只读，不改 md。

## 门禁数字（a 步复跑，不采信旧数字）

| 门禁 | 结果 |
|---|---|
| `verify_quotes.py`（完整 lane，epub） | 212/212 ✅，21/21 文件干净；2 条短引语未自动校验（`00_金句精选.md` 1 条、`ch18` 1 条），已人工 grep 兜底，均命中原文 |
| `check_vocab.py` | FAIL 0；WARN 2（`ch16`、`ch18` 词汇节外 2 行表格，格式提示） |
| `check_entities.py` | 未知实体 0 |
| `corruption_scan.py` | FAIL 0（U+FFFD/双句号 0） |
| `sweep_full.py --quiet` | 本章命中 169 ｜跨章 0 ｜跨标签拼接 0 ｜全书查无 0 |
| `check_chapter_quotes.py`（19 章） | 19/19 ✅，全部引语归属正确 |
| `check_crossref.py` | 交叉引用 0 对，报警 0 |
| `check_overview_full.py` | A 整串命中 43 ｜拼接 0 ｜查无 0 ｜短引语 1；B 章节标签 0/43（无标签，工具口径不适用，非缺陷）；E H1 语义错配 0 |
| `verify_overview_quotes.py` | 43/43 ✅（完整 lane） |

结论：机械层全部通过；d/e 步以下只报告机械层看不到的语义/事实问题。

## d 步：引语↔分析逐对核对

抽样范围：19 章共 169 个 `> **原句 N:**` 块 + 总览三篇引语层，逐块核对「引语↔中文理解」「关键词锚定」「说话人/人物」「数字/计数」「章节偏移」。

### 阻断型（必须改）

1. **`ch04 All Men Would Be Tyrants.md:103` 原句 9 — 引语为多段拼接，与中文理解不对应**  
   - 引语（全文 1426 字符，节选）：`"I agree to this Constitution with all its faults   As the convention neared the end of its work, only forty-one delegates were left in sweltering Philadelphia. Perhaps, of an evening, they sought relief in the parlor of Anne Willing Bingham… On September 17, 1787, the day the remaining delegates made ready to sign, Wilson read a speech written by Franklin… “I agree to this Constitution with all its faults, if they are such; because I think a general Government necessary for us…”"`  
   - 中文理解（全文）：`我同意这部宪法，连同它的全部缺点——如果那些真是缺点的话，因为我认为一个总的政府对我们来说是必要的。`  
   - 原文支撑：`text/ch04_…txt` 中该段为章节小标题 `I agree to this Constitution with all its faults` + 叙事段落 + Mason/Franklin 引语的多段文本，不是单一引语。  
   - 问题：引语把小标题、叙事与 Franklin 引语缝成一个块，中文理解只覆盖末句；属「引语与分析说的不是一回事」（类 100G ch86 ⑧⑨⑩）。  
   - 建议：引语截短为 Franklin 实际引语一句，其余分析拆出或删除。

### 提示型（只记不改）

1. **`ch05 Every Gentleman May Propose Amendments.md:39–41` 原句 1 — 中文理解超出引语范围**  
   - 引语：`"no society can make a perpetual constitution," because "the earth belongs always to the living generation"`  
   - 中文理解：`杰斐逊从巴黎写信给麦迪逊：没有一个社会能制定一部永久的宪法，因为地球永远属于活着的这一代人；因此美国应当每一代人召开一次新的制宪会议。`  
   - 说明：引语本身不含"因此美国应当每一代人召开一次新的制宪会议"，属分析延伸，非阻断；严格口径下中文理解应限于引语本身。

2. **`ch09 No Amendment Is Necessary.md:151` 词汇表表格格式缺陷**  
   - `school` 行的例句单元格被粘贴进一整段 unrelated 叙述（Grant 1875 Des Moines 演说等），使该行不可读。  
   - 说明：非引语层缺陷，属生成/粘贴损坏；corruption_scan 未覆盖此形态。建议行级重写该行。

3. **`ch19 Epilogue.md:63–69` 原句 4 — 长引语仅摘要两端**  
   - 引语为法戈学生请愿多句原文（含 "We, the undersigned, are suffering" … "We are young, but we ask, and we demand…"），中文理解只取首尾两句。  
   - 说明：引语逐字命中原文，无截短；但中文理解未覆盖中间句。属提示型，不阻断。

4. **`00_金句精选.md` ⑥ 说话人归属措辞不精确**  
   - 引语 `"Law-makers thought as little of comprehending us in their code of liberty as if we were pigs or sheep."` 实为 Charles Brockden Brown 1798 年小说《Alcuin》中一位女性角色的台词，非"一位女性作者"。  
   - 说明：归属对象应改为"布朗小说中的女性角色"。

### 假红型（先修工具）

- 0 条。本轮未出现检查器口径导致的假红；`check_overview_full` B 段 0/43 为"无章节标签"的正常状态，不是工具缺陷。

### 抽样核对示例（10 条逐对 ✅）

| # | 文件:行 | 引语（节选） | 中文理解 | 结果 |
|---|---|---|---|---|
| 1 | `ch01:39` | "We the People. The Constitution…" | 开篇并置序言与生命意象 | ✅ |
| 2 | `ch03:63` | "A clock, too, has a constitution…" | 亚当斯钟表"宪法"定义 | ✅ |
| 3 | `ch04:87` | "in proportion to the whole number of white & other free Citizens…" | 代表基数计算规则 | ✅ |
| 4 | `ch05:79` | "Before Massachusetts, no states had formally recommended amendments…" | 马萨诸塞前/后对照 | ✅ |
| 5 | `ch07:79` | "“The word white is a modern term…" | "白人"是立法新词 | ✅ |
| 6 | `ch08:111` | "twelve white men and twelve Black men posed…" | 二十四名陪审员合影 | ✅ |
| 7 | `ch10:71` | "We have before us this grave and extraordinary proposition…" | 千名盎格鲁-撒克逊人统治八万"异类" | ✅ |
| 8 | `ch12:111` | "Was it the Rock of Gibraltar? Or was it a bowl of Jell-O?" | 岩石还是果冻 | ✅ |
| 9 | `ch14:55` | "“They are turning it into a mummy…”" | 木乃伊比喻 | ✅ |
| 10 | `ch18:95` | "“In American constitutional law, silence… counts as consent…”" | 沉默被洗成同意 | ✅ |

## e 步：总览层事实核对

### 阻断型

1. **`00_概述.md`（ch07 条）与 `00_金句精选.md` ⑩ — 年份事实错误**  
   - 现文：`1835 年琼斯在伊利诺伊州制宪会议上要求删去"白人"一词` / `1835 年要求在州宪中删去「白人」一词`。  
   - 事实：John Jones 参与的是 **1847 年**伊利诺伊州制宪会议（1848 年新宪法公投批准）；"Let us examine the word white" 出现在 1847 年会议的辩论中（`text/ch07_…txt` 第 455 段）。  
   - 建议：两处 "1835" 统一改为 "1847"。

2. **`00_金句精选.md` ⑥ — 说话人归属错误**（同上 d 步提示型 4，e 步事实层重复记录）  
   - 建议：改为 "布朗小说《Alcuin》中的女性角色"。

### 提示型

1. **`00_概述.md` ch16 条 — 小组委员会撤销年份表述略宽**  
   - 现文 "1977 年小组委员会被撤销"；原文为 Eastland 于 1978 年辞职前解散，并受 1977 年《立法重组法》影响。  
   - 说明：不阻断，但建议改为 "1977–1978 年间"。

2. **`00_概述.md` ch10 条 — "参议员质问"未指名**  
   - "1898 年兼并辩论中，参议员质问共和是否要'退化为殖民者与土地掠夺者'"。原文该问句出自夏威夷女王利留卡拉尼/反对派陈述，参议员身份未在本库 text 中明确。  
   - 说明：建议补注"（引自兼并辩论中的发言）"。

### 总览引语说话人对账

对 `00_金句精选.md` 28 条引语的说话人标题（`chNN · 说话人`）与原文逐条核对：27/28 一致；唯一偏差为 ⑥（见上）。其余包括：威尔逊、亚当斯、杰斐逊、利伯、杜波依斯、霍姆斯、罗斯福、戴维斯、杜鲁门、巴克利、贝赫、肯尼迪、施拉夫利、乔丹、斯卡利亚等均与 `text/` 前后 ~200 字符窗口一致。

`00_情感节点.md` 8 个节点的叙事概括与章节 md 一致；关键引语归属正确（含 "It is virtually unamendable."、"It's dead. Dead, dead, dead!" 等短引语已 grep 命中原文）。

## 结论

- 阻断型：**2 条**（`ch04` 原句 9 多段拼接；总览两处 1835 年份/说话人 attribution 错误）  
- 提示型：**7 条**（含 ch05 中文理解延伸、ch09 表格格式、ch19 摘要两端、金句 ⑥ 措辞、总览年份/归属措辞）  
- 假红型：**0 条**

整改建议：阻断型 2 条应由执行方在下一轮修复；提示型按需处理，不阻塞 commit。审查方只输出报告，未改任何 md。