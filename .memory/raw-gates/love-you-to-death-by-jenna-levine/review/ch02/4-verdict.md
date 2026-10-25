# ch02 · T3 判定表

- 章：Chapter One（md：`ch02 the retirement party.md`；原文 `text/ch02_chapter_one.txt`）
- R1 素读：`1-suread.json`（**审查方自读 `text/`**——本章 md 出自本会话写作者侧，故 R1 独立性打折，见「独立性声明」）
- R2 机器层：`2-machine.json`（第二实现，verdict=ok；12 块 / 31 片段查无 0）
- R3 对账：`3-diff.md`
- 覆盖：**全章 12 块逐块 R4 + R5**；无「只有机器层」的块

## 独立性声明（本章特有）

R1 的「先读 `text/` 后开 `md`」顺序在本章成立（原文先读、md 后开），但**读者是本书的写作者本人**，
R1 不具备「独立代理先读」的外部性。本章 R3「漏」一单的效力因此弱于独立代理章，
故本章对「漏」的判定一律从严：只把**本章转折点**级别的缺失记为阻断，背景性取舍一律记提示型。

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 58 | seventh circle / top ten | ✓ 命中 | ✓ | ✓ 我躲、他配合 | 通过（另见 R5 断言 1） |
| 2 | 50 | forgot the plaque | ✓ 命中 | ✓ | ✓ 我忘带 → Skellar 无物可颁 | 通过 |
| 3 | 49 | Ice-blue eyes | ✓ 命中 | ✓ | ✓ 我的目光 | 通过 |
| 4 | 52 | it’s…Daniel? | ✓ 命中 | ✓ | ✓ 他的迟疑 | 通过 |
| 5 | 41 | It's only September 3 | ✓ 命中 | ✓ | ✓ 服务员误读 | 通过 |
| 6 | 47 | the cup of bad omen | ✓ 命中 | ✓ | ✓ 她自嘲 / 他追问后后悔 | 通过 |
| 7 | 47 | Russian, maybe | ✓ 命中 | ✓ | ✓ 口音是她的**猜**（读者视角提示已标注） | 通过 |
| 8 | 49 | I am…stuck | ✓ 命中 | ✓ | ✓ 他的处境 | 通过 |
| 9 | 51 | the ex–work situationship | ✓ 命中 | ✓ | ✓ 他=Sims/Ashley 二人 | 通过（措辞见 R5 提示 2） |
| 10 | 49 | Vanished, like he was never there | ✓ 命中 | ✓ | ✓ 她伸手 → 他惊异 → 他消失 | 通过 |
| 11 | 56 | the pain is from cold, not heat | ✓ 命中 | ✓ | ✓ 痛因由她先误判后更正 | 通过 |
| 12 | 60 | Name: Lucy McKenzie | ✓ 命中 | ✓ | ✓ 卡片写的是她自己 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 1「为什么这样写」称本段是「**全书第一句**」 | `text/ch01_prologue.txt` 首句逐字："Wherever I thought I might end up after the explosion that killed me"；本书第一章是 Prologue，ch02 是 Chapter One | 与原文不符（跨章断言错） | **阻断** |
| 原句 1「为什么这样写」称「**读者还没见到死神，先听见了关于地狱的说法**」 | 序章 5 处地狱：`text/ch01_prologue.txt:25` "…painted elaborate pictures of Heaven and Hell"、`:28` "At least it ain’t Hell."、`:52` "If we were all bound for Hell—"、`:79` "the level of Hell for which you were all previously destined"、`:85` "skip all that Hell nastiness" | 与原文不符（读者在序章已听过地狱） | **阻断** |
| 导航把这场退休宴写成「**公司**退休宴」 | `text/ch02_chapter_one.txt`："a workplace retirement party"、"university staff like me"、"Professor Shiran"、"Tennessee College" | 原文是大学教职退休宴；同章正文各块均写明教授/行政助理，读者不会被误导 | 提示 |
| 原句 9 中文理解把 "situationship" 译作「前后脚**的事故**」 | 同块关键词括注作「工作场合的那段关系」；原文 "The ex–work situationship who told me he didn’t want a relationship five minutes before ending it with me" | 同块两层口径不同，但后句已把「一段关系」讲明 | 提示 |
| 原文的「家世背景」「Jess 婚期与六年关系」「我们也许真有共同点」三段未被引用 | `text/ch02_chapter_one.txt`："I'm not telling him that my dad walked out on us when I was four" / "Jess is getting married in a few weeks" / "Maybe we have actually something in common" | 均为背景而非本章转折；「她对陌生人有所保留」正是本章主题 | 跳过（记录取舍） |
| 原句 5「读者视角提示」把「万圣节 / 9 月 3 日 / 卡片上的日期」并置 | `text/ch02_chapter_one.txt` 末三行逐字："Name: Lucy McKenzie" / "Age: 28 years, 1 month, 3 days" / "Date: September 3"；正文另有 "It's only September 3, but I let it go" | 回原文核对后成立 | 已核实为正确 |

## 分组计数（只报四组）

- **逐字**：12/12 块整串命中，查无 0（`2-machine.json` verdict=ok；31 片段逐条回查，segment_miss=0）
- **对应**：阻断 0，提示 0（12 块的中文均在讲本块引语；施事/受事逐块核过，无反转）
- **形态**：阻断 0（H1 `02. Chapter One` 合本书形态 · 导航 5 项 · 4 子项齐备 · 12 块在本书众数区间 3–12 内 · 编号连续无撞车 · 词表 24 条三档齐）
- **断言**：阻断 2，提示 2，未核 0

## 阻断

- **[断言]** 原句 1「为什么这样写」写「全书第一句就把两件事钉死」
  - 判据：跨章断言必须与原文一致；本书第一章是 Prologue（`text/ch01_prologue.txt`），ch02 是第二章（Chapter One）
  - 证据：`text/ch01_prologue.txt` 首句逐字："Wherever I thought I might end up after the explosion that killed me"
  - 处理：改「**这一章的第一句**」，并把「读者还没见到死神，先听见了关于地狱的说法」改为「"地狱"在序章里已是公共词汇（那三个人自己就提过），这一句妙在**用自嘲把它说出来**」；「职场笑话 + 地狱典故」的分析不变
  - 复验：`chapter.sh` rc=0（改后重跑）

## 提示（只记不改）

- **[断言]** 导航「公司退休宴」——原文是大学教职退休宴（"workplace retirement party" / "university staff" / "Professor Shiran" / "Tennessee College"）
- **[断言]** 原句 9 中文理解「那个前后脚的事故」与同块关键词括注「工作场合的那段关系」口径不同

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 原句 7「也许是俄罗斯口音？」被当成作者坐实 | 原文自己就标着不确定，中文层保留问号、读者视角提示明写「是**猜的**」 | "Russian, maybe?" | `text/ch02_chapter_one.txt` |
| 原句 5 读者视角提示把「万圣节 / 9 月 3 日 / 卡片日期」并置 | 三处都逐字在原文，且「Date: September 3」与「It's only September 3」确为同一日 | "It's only September 3, but I let it go" / "Date: September 3" | `text/ch02_chapter_one.txt` |
| 原句 9「我撞见他在办公室里和 Ashley Robinson 教授在一起」 | 原文是 "I walked in on him in his office with Professor Ashley Robinson"，"his office"＝Sims 的办公室 | "…about seven minutes before I walked in on him in his office with Professor Ashley Robinson." | `text/ch02_chapter_one.txt` |
| 原句 10 读者视角提示说「他问的是『你是怎么做到的』，不是『别碰我』」 | 原文确为 "How are you doing that?"，先惊异后消失，未出现拒绝字样 | "How are you doing that?" He sounds—looks—shocked out of his wits. | `text/ch02_chapter_one.txt` |
