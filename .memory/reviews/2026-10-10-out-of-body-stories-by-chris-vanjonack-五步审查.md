# Out of Body Stories by Chris Vanjonack —— 五步审查报告

**审查日期**：2026-10-10
**审查方**：Hermes（同会话审查，用户主动发起，a–e 全量执行，未自我豁免）
**书籍**：`notes/books/short-story-anthologies/out-of-body-stories-by-chris-vanjonack/`
**规模**：10 篇精读 md（短篇合集格式）｜text/ 10 件｜**完整 lane**（epub 在位）

---

## 一、审查前基线（完工时报告的数字）

- verify_quotes 75/75（100%）
- sweep_full 0 跨章 0 拼接 0 查无
- corruption_scan 0
- check_entities 0
- commit `4d0e0f95f`

## 二、a 步：第 3 条门禁全量重跑（不信报告数字）

| 门禁 | 结果 |
|---|---|
| ① verify_quotes | 75/75（100%），干净 10/10 |
| ② verify_quotes --full | 整串取证 0 |
| ③ **check_vocab** | **FAIL 0，但 10 个文件全部「文件名无 chNN 前缀」⇒ ch_corpus 为空，例句校验整层空跑**（471 条 ❓ + 36 条 WARN 均因此产生） |
| ④ check_entities | 0 |
| ⑤ corruption_scan | 0 |
| ⑥ sweep_full | 0 跨章 0 拼接 0 查无 |

**关键发现**：`check_vocab` 的「X/0」是**假绿**——文件名 `NN Title.md` 无 chNN 前缀且 frontmatter 无 `source_text/chapter`，导致每条例句都判未命中，FAIL 数字被灌水、真实缺陷被掩盖。⇒ 必须自建口径逐条核对。

## 三、a 步自建口径：词表逐条核对（241 词条行）

自建判据：① 词头带词边界命中**本章** text/（含屈折形态）② 例句去省略号/粗体后是**本章**逐字子串 ③ 例句含词头。

**查出并修复 54 处词表缺陷**：

### A 类：词头本章查无（虚构/跨章词条）22 条
| 文件 | 原词头 | 处置 |
|---|---|---|
| 01 | retromodernism | → retrofuturism |
| 01 | confluence | → infrastructure |
| 01 | futility | → approximation |
| 01 | incongruous | → disintegrated |
| 02 | bifurcation | → condescension |
| 04 | ransack | → paraphernalia |
| 05 | oblivious | → dispassionate |
| 06 | stasis | → indoctrinations |
| 07 | anachronism | → refashioned |
| 07 | sleep | → penetrative |
| 07 | alone | → incorporeal |
| 08 | precarious | → reacclimating |
| **09** | **anachronism / boisterous / elegy / linearity / severance / precarious / grovel / frisking** | **整档（进阶 8 条）从 ch08 串入，全部换成 ch09 自己的词** |

### B 类：词形错误（词真在，词头形态错）11 条
lambely→lamely｜prophesy→prophesied｜metastasize→metastasizing｜implacable→implacably｜coalesce→coalescing｜waylay→waylaid｜insinuate→insinuating｜vulnerable→vulnerability｜manifestation→manifesting｜convulsion→convulse(ch06)/convulsing(ch10)

### C 类：例句非本章逐字 / 不含词头 21 条
（含 ch01 portal/scream/proud、ch02 accident/drink/dance、ch03 park/sex/drive/camp/alone、ch04 photo、ch05 dead/alone、ch06 blood/walk、ch07 love/body、ch08 time/past/love、ch09 phone/happy、ch10 transcend/obliteration/home/choose）

### 重复行 3 条
ch07 `penetrative`/`incorporeal`（换词时重复添加）、ch09 `literalization`

## 四、b 步：逐章归属

`check_chapter_quotes.py` 逐章：**10 章全部 X/X in 本章 text**（ch01 10/10、ch02 12/12、ch03 8/8、ch04 8/8、ch05 8/8、ch06 6/6、ch07 6/6、ch08 4/4、ch09 7/7、ch10 5/5）。

**发现 2 处引语缺陷**（a/b 步交界）：
- **ch01 原句 6 人称错**：md 写 `He's had dates like this...`，原文是 **`She's had dates like this...`**（第三人称指 Grace）→ 已修
- **ch09 原句 4 标点错**：md 写 `...feel like home," Kate says.`，原文是 **`...feel like home.”`**（句号结尾，无叙述标签）→ 已修

## 五、c 步：结构扫描

- `audit_structure.py`：10 md / 82 引语块，**❌ 结构缺陷 0 ｜ ⚠️ 提示 0 ｜ 🔀 映射不一致 0**
- 第二实现 `check_struct_indep.py`：因文件名无 chNN 前缀**不适用**（报「下没有 ch*.md」）——属工具口径，非缺陷

## 六、d 步：语义二审

**子代理失败**（API key 401），按规则**主会话自执行不可省**。

**逐块核对 74 个引语块**（引语↔分析对应 / 说话人归属 / 人物关系断言 / 计数断言）：

- **引语↔分析对应**：74 块逐块读「中文理解/句子结构/关键词/表达方式/为什么这样写」，**无错位**
- **说话人归属**：抽查 ch04（Lilith/Devon/Jon/Trevor）、ch05（Henry/Sol/Chloe/Elizabeth）、ch06（Lee/Corbin/Ward/Isaac）、ch09（Kate/Tom/Naomi/Speaker）、ch10（Elizabeth/Mom/Morgan/Trevor），**均与原文窗口一致**
- **发现 1 处错字**：ch04 原句 2 分析 `okady` → `okay`（已修）
- **第二实现**：`check_analysis_indep.py` 抽出分析层英文片段 0 条；`check_xref_indep.py` chNN 引用 0 处报警 0
- **自建换口径扫描**：分析层行内英文 5 条「未命中」，逐条核实均为**描述性英文/语法记法/刻意假设**（禁令 3 豁免）——其中 `I miss you`（ch05）、`take this heart`（ch09）改为纯中文以消除走形风险；`Jimmy manages to open an interdimensional portal`（ch01 句子结构主干标注）保留

## 七、e 步：总览层事实核对

**不适用**——本书是短篇合集，**无总览三篇**（`00_*.md` 不存在），按库内先例豁免（同 The Language of Knives / fold-catastrophes-by-peter-watts）。

## 八、终验（复跑，0 阻断）

| 门禁 | 终值 |
|---|---|
| verify_quotes | **74/74（100%）**，干净 10/10 |
| verify_quotes --full | 整串取证 0 |
| check_vocab | **FAIL 0 ｜ WARN 0** |
| check_entities | 0 |
| corruption_scan | FAIL 0 |
| sweep_full | 本章命中 5 ｜ 跨章 0 ｜ 拼接 0 ｜ 查无 0 |
| check_short_quotes | **8/8 命中**，0 跨章 0 拼接 0 查无 |
| audit_structure | ❌ 0 ｜ ⚠️ 0 ｜ 🔀 0 |
| b 步逐章 | 10 章全 X/X |

## 九、三档定性

| 档 | 数量 | 内容 |
|---|---|---|
| **阻断型** | **57** | 词表 54（虚构词条 22 + 词形错 11 + 例句问题 21 + 重复行 3，去重后 54）+ 引语 2（ch01 人称、ch09 标点）+ 分析错字 1 |
| **提示型** | 2 | 分析层描述性英文（ch01 语法主干标注、ch05/ch09 已改中文） |
| **假红型** | 2 | ① `check_vocab` 因文件名无 chNN 前缀整层空跑（例句校验 0/241 实际执行）② `check_struct_indep` 因同样原因不适用 |

## 十、commit

- `70939af33` —— a/b/c 步修复（词表 54 处 + 引语 2 处）
- 待提交 —— d 步修复（ch04 错字 + ch05/ch09 分析层英文改中文）

## 十一、同会话审查的已知局限（如实标注）

1. **说话人/施动归属**：本项目已实测该类不可靠机械化（`check_speaker_consistency.py` 全库仅 1 条真缺陷、约 1/3 假阳）⇒ 本轮靠主会话人判 + 原文窗口核对，**未逐块开窗全部 74 块**，只覆盖了人物密集的 5 章。
2. **语义终判在同一会话**：执行方＝审查方，d 步子代理因 API 401 失败，语义层由主会话自判——建议如需最高保证，另派异实例抽样复核（重点 ch05/ch09/ch10 的长叙述章）。
3. **ch10 是 3108 行超长终章**：「无数宇宙」的分支叙述中，分析层对某个具体宇宙情节的概括**未逐句回原文核**（只核了 6 个引语块及其分析）。
4. **`check_vocab` 工具口径缺陷未修**：本轮用自建口径绕过，**未改工具**（文件名无 chNN 前缀的短篇合集仍会整层空跑）——建议后续把该口径补进 `check_vocab.py`。
