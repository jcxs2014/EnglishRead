# 派工模板 · The Mysterious Affair of Judith Potts

> 写章前先读本文件全文，再读 `docs/rules/创建卡.md` 全文，然后读本章 `text/` 全文。
> 仓库根：`/Users/jcxs2014/Documents/Works/EnglishRead`

## 目录与本章

- 书目录：`notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/`
- 本章原文：`text/chNN_<slug>.txt`（唯一真值，一切引语只能从这里取）
- md 文件号 = 书内章号 + 1（ch01=Prologue，ch02=书内 Chapter 1 …… ch38=书内 Chapter 37）
- H1 用 `# <书内章号两位>. <书内标题>`，例：书内 Chapter 3 → `# 03. Chapter 3`

## 形态（照此写，不要自创）

```
---
状态: 未读
modified: "2026-10-26"
source_text: chNN
---

# NN. Chapter N

## 本章导航

- **一句话概括**：…
- **情感弧线位置**：…
- **线索结构**：…
- **人物弧线**：…
- **叙事手法**：…

## 精读

> **原句 1:** "…"
**中文理解**：…
**关键词**：…
**为什么这样写**：…
**读者视角提示**：…

## 本章词汇

### ⭐⭐⭐ 高级
| 词/短语 | 释义 | 例句 |
|---|---|---|
| … | … | … |

### ⭐⭐ 进阶
（同上表头）

### ⭐ 基础
（同上表头）

## 一句话总结

…
```

- 导航 5 项、项名固定；精读 4 子项；词表三档标题固定 `⭐⭐⭐ 高级` / `⭐⭐ 进阶` / `⭐ 基础`。
- 表体必须是标准 Markdown 表格 `| 词/短语 | 释义 | 例句 |`（斜杠分隔工具解析不到）。
- `## 一句话总结` 必须有正文，不能只有标题。

## 硬线（一条都不许破）

1. 引语逐字：从本章 text 里 grep 出来，不改一个字。宁可换引语，也不许凭记忆写。
2. 引语是句级：每块 **1–3 句、30–70 词、≤4 行**；超了按原文句界拆成两块。
3. **绝不许用 `…` 缝合跨自然段的引语**；两段隔着叙述就拆成两块独立引语。
   - ⚠️ **实证（ch18 实测）**：把相邻的几段对话用 `…` 连成一块，看着「中间无叙述句」，仍是跨自然段缝合——
     `verify_quotes` 逐段验全绿，只有 `gate.sh` ⑱ 的拼接红线抓得到。
     ⇒ **每块引语必须是一个自然段内的连续片段**（可含原文本段内的 `…`，但不可跨段）。
     段落太短放不下一块 30 词引语时，就**换一段更长的自然段**来引。
4. 分析里出现的人名/动作/关系必须在这一块引语里能找到；找不到说明引语选短了。
5. 关键词每个词必须出现在本块引语或本章原文里；单个关键词不超过 8 个词（整句照抄会被判假）。
6. 中文理解 ≥6 汉字；为什么这样写 ≥8 汉字且中文占比 ≥15%。
7. 不许模板句（「本句描写了场景与人物的反应」「把 X 重新定义 as Y」「为后续情节的转折埋下伏笔」等），
   同一字段同一句式重复 ≥3 次也判红。
8. 中文句子要读得通：`的` 后直接跟动词＝缺词残句。
9. 块数 2–15 硬限；按本章篇幅取，chapter.sh 会打印建议区间，尽量落在建议区间内。
10. 导航层与总结层出现的英文也只能原文复制。

## 生产步骤（顺序不可换）

① **素读清单**：读本章 text 全文后列 5–8 条「谁做了什么」，每条挂一段**原文逐字锚点**（15–60 字符），
   写进 `/tmp/jp/chNN.facts`，每行格式 `原文逐字片段 || 谁做了什么`。

② ```
   python3 scripts/suread.py "notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/" chNN /tmp/jp/chNN.facts
   ```
   锚点必须 100% 命中。查无就改事实，不要改锚点去凑。

③ **写 md**：`notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/chNN <小写英文短语>.md`
   （文件名唯一分隔符是单空格，去掉所有标点，只留字母数字空格）

   词表用脚本生成，**不许手写例句**：
   ```
   python3 scripts/vocab_candidates.py "<书目录>" --ch NN --tiers --limit 300 --max-sent 400
   ```
   从候选里挑词 + 自己写中文释义 → `/tmp/jp/chNN_glosses.json`（形如 `{"freefall":"自由落体"}`）→ 再跑：
   ```
   python3 scripts/build_vocab_section.py "<章 md>" NN --glosses /tmp/jp/chNN_glosses.json
   ```
   脚本会断言词头来自本章候选、例句逐字命中本章；报错就换词。
   **词表总量 30–45 条**，三档都要有词但不许注水（actually/following/thinking 之类不进 ⭐⭐ 进阶）。
   脚本固定输出 `### ⭐ 基础` 抬头，保持原样不要改。

④ **门禁**（必须 rc=0）：
   ```
   bash scripts/chapter.sh "<章 md>"
   ```
   红了就按它点名的地方改，改到 rc=0 为止。

## 译名统一（本书既有章已定型，照用）

朱迪思（Judith）、艾勒尼（Eleni）、贝克斯（Becks）、苏齐（Suzie）、塔妮卡·马利克（Tanika Malik）、
贝思尼·怀斯（Bethany Wise）、加里·怀斯（Gary Wise）、哈里·阿斯奎特（Harry Asquith）、玛丽·珀特（Mary Pert）、
菲利波斯·德米特里乌（Philippos Demetriou）、米凯拉·帕菲德斯（Michaela Paphides）、
奥利弗·贝雷斯福德（Oliver Beresford）、塞雷娜·萨克森（Serena Saxon）、迈克·萨克森（Mike Saxon）、
贾米拉（Jamilah）、布伦丹·佩里（Brendan Perry）、爱丽丝（Alice）、艾琳（Erin）。

## 不许做

- 不许 `git add` / `commit` / `push`（多实例共用工作树，暂存区各自负责）。
- 不许整文件 `write` 覆盖已存在的其他文件；你只写自己这一章。
- 不许读 `scripts/` 源码反推判据。

## 回执六项（缺一退回）

1. md 绝对路径 + 字节数；
2. 每块引语的前 6 个词；
3. 事实清单：谁做了什么、数字/时间，每条能回到原文；
4. 最没把握的一处：明写哪句是推断、哪句是原文；
5. `chapter.sh` 原始输出尾部 + 退出码；
6. 素读清单产出路径 + 「锚点命中 N/N」那一行。
