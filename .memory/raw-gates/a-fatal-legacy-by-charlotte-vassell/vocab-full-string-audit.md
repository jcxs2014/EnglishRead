# 词表例句全串核验 · 《A Fatal Legacy》（2026-10-21，主会话收口）

> **为什么做这件事**：交接件 §四·3·① 记了一笔工具盲区——`scripts/check_vocab.py` 的例句取证**只取前 60 字符且抹掉引号**，
> 因此「例句被截短」与「例句里 `he're`/`he's` 一类被改动」**一条都抓不到**；书里 ch09 两处例句缺陷正是由此漏过。
> 共享脚本本轮**未动**（并行实例正在跑门禁，改共享检查器会影响所有书）⇒ 改用**书级第二实现**补这一层。

## 探针（可复跑）

- 取每章 `## 本章词汇` 三列表格的第 3 列（例句），
- ① **全串逐字**：例句（去除外层直双引号）必须是本章 `text/chNN_N.txt` 的**连续子串**；
- ② **非中途截断**：例句结尾处若源文还有字母/数字续接 ⇒ 判截短。

脚本：`/tmp/afl_vocab_full.py`（会话临时脚本，未入库；逻辑见上，可按此重写入库）。

## 结果

**核 1458 条例句 → 逐字 MISS 10 · 中途截断 0**（修前）→ **修后 MISS 0 · 截断 0**。

| # | 章 | 词 | md 原写 | 原文 | 档 | 处置 |
|---|---|---|---|---|---|---|
| 1 | ch05 | disbanded | `‘…A bit of a shock when that happened so suddenly.’` | 原文这句对白**仍在延续**（后面还有 `Your team had had some real success…`），md 补了个原文没有的收尾引号 | **阻断** | 去掉收尾引号，按原文留到句末 |
| 2 | ch09 | pavement | `‘The police cars had strewn past and blocked the pavement.’` | 原文该句是**叙述**（无引号），md 给它套了对话引号 | **阻断** | 去掉对话引号 |
| 3 | ch23 | lasagne | `‘Can’t I have lasagne? Or cottage pie?’` | 原文该对白**仍在延续**（`A cheeseburger? What about a roast?…`），且开引号在更前面的 `‘Chicken again.` 处 | **阻断** | 去掉凭空的开引号与收尾引号 |
| 4 | ch31 | mews | `‘It’s not Chelsea. There are no mews.` | 原文该句是**叙述**（前一句才是对白），md 给它加了开引号 | **阻断** | 去掉开引号 |
| 5 | ch31 | accident | `'This one looks like an accident.` | 原文该对白**仍在延续**，md 补了个原文没有的收尾引号（且用直引号） | **阻断** | 改回原文的弯引号、不补收尾引号 |
| 6 | ch31 | crumbling | `'This one looks like an accident. … crumbling stone steps.` | 词句逐字无误，只是**直引号 ≠ 原文弯引号** | 提示 | 归一为原文的 `‘…’` |
| 7 | ch31 | body | `'What is this case you’re working on?' Barry asked, …` | 同上 | 提示 | 同上 |
| 8 | ch31 | square | `'But I wouldn’t want to live on this square. …'` | 同上 | 提示 | 同上 |
| 9 | ch31 | intruder | `'He was in the middle of a live-stream when an intruder was spotted on camera.` | 同上 | 提示 | 同上 |
| 10 | ch31 | memoir | `'It looks like Jimmy wrote a memoir,' Matt said, …` | 同上 | 提示 | 同上 |

**直引号用法的分布**：全书 1458 条例句里，弯引号 818 条、**直引号仅 6 条且全在 ch31** ⇒ 属该章的孤例，不是本书约定，按提示级归一。

## 复验

```
python3 /tmp/afl_vocab_full.py     → 例句行 1458 条｜逐字 MISS 0｜疑似截短 0
bash scripts/gate.sh <书目录>       → EXIT 0（词条行 1458、FAIL 0）
python3 /tmp/afl_probe.py           → 395 块：P1 0 · P2 0 · P3 0
```

## 结论（可复用到别的书）

- **`check_vocab` 的 FAIL=0 只说明「例句前 60 字符能对上」**，不说明例句整体逐字、也不说明例句没被从中间截断。
- 补这一层的最小成本：**对每条例句做一次全串 `in` 判断 + 结尾续接检查**（脚本 60 行）。
- 例句的**引号形态**是这一层最容易漏的一处：凭空加引号（叙述被写成对白）、把仍在延续的对白截断并补上收尾引号——
  这两种都会让「逐字」判绿（因为 60 字符指纹落在对白开头）。

---

## 追加（2026-10-21，第二次）：例句引号的三态判定与 41 条归零

> 用户复核时在 ch31 `accident` 一条上指出：句子逐字无误、截在标点处，但**留着一个不闭合的开引号**——
> 这是「截断」的第三种形态：**引号不对称**。回查全书发现这一形态共 **41 条**（38 条存量 ＋ 2 条上轮引入 ＋ 1 条直引号归一后暴露）。

### 引号三态（判据）

| 形态 | 含义 | 是否缺陷 | 处置 |
|---|---|---|---|
| ① 引号成对 `‘…’` | 完整引语 | 否 | 不动 |
| ② 只有**开**引号 | 摘录从对白开头起、原文仍在延续 ⇒ 开引号是唯一的截断痕迹 | **是**（形态类） | 回原文看**结束处**：原文正好收尾 ⇒ **补收尾引号**；原文仍在延续 ⇒ **去掉开引号**（与全书 1198 条无引号例句同形） |
| ③ 只有**收**引号 | 摘录从对白**中间**起头，原文此处本就有收引号 | **否** | **不要动**（我第一版检查脚本把它误判成缺陷，须按「开引号计数 > 收引号计数」才判） |

### 实际改动

- **A 类 12 条**（原文该处正好收尾、后接字符就是 `’`）⇒ **补上收尾引号**，例句成为完整引语：
  ch11 `offloading`、ch16 `backstory`、ch19 `Arrivederci`、ch21 `security`/`covering`/`received`/`apparently`/`coincidence`、ch24 `makeshift`、ch35 `procrastinating`、ch47 `dodgy`/`metaphors`。
- **B 类 29 条**（原文仍在延续）⇒ **去掉开引号**，改成裸摘录：
  ch05 `flats`、ch10 `whizzbang`、ch13 `catalogue`、ch16 `ex-boyfriend`、ch19 `half-cut`/`school dinner lady`/`PO Box`、ch21 `trialling`/`multiple`/`computer program`、ch22 `M&S Food`、ch24 `seances`/`basement door`、ch27 `zoo`/`toddler`、ch31 `supermodel`、ch33 `pentagram`、ch37 `salad`、ch47 `Harrogate`、ch48 `dogsbody`/`subterranean`/`alibied`/`corpse`/`taxi driver`、ch53 `hundreds`、ch54 `plummeted`，以及上轮引入的 ch05 `disbanded`、ch31 `accident`、ch31 `intruder`。
- 两种改法**都保持逐字**（改后 1458 条全串核验 MISS 0 · 截断 0）；未闭合开引号计数 41 → **0**。

### 复验

```
python3 /tmp/afl_vocab_full.py   → 例句行 1458｜MISS 0｜截断 0
未闭合开引号扫描（count(‘) > count(’)）→ 0
bash scripts/gate.sh <书目录>      → EXIT 0
```
