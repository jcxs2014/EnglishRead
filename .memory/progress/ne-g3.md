# ne-g3 交付报告（ch07 / ch08）

生成方式：`/tmp/ne_g3_build.py`——所有引语从本章 `text/` 程序化切片并 `assert q in src`；分析层英文片段动笔前按 ne_strict 同口径逐条断言；词表行为 `vocab_candidates.py --ch N --tiers` 原行粘贴、只填释义（释义纯中文）。

## ch07 `ch07 welcome to the thorned root.md`

- 章体量：9,661 字符（中章），块数 **7**（前/中/末覆盖：正文偏移约 4%→100%，位置升序）
- ne_strict：块 7 | **FAIL 0** | WARN 0
- corruption_scan：全目录 FAIL 0
- 本章内核过的计数/首现断言（以 src 偏移取证）：
  - Sable 在本章出现 2 次，首次落在怒骂句内（骂句起 2167 / 首现 2182，此前无 Sable）
  - `me—LYREBIRD` 自我等式本章仅 1 次
  - Earth 一词本章仅 1 次（`returned Earth names`）
- 人名裁决执行：叙述者只写「被 Wylla 叫作 Sable」「自说 me—LYREBIRD」；Aliers 点名 "Wylla Sotain and LYREBIRD" 按「点名≠证实」处理（导航与 B7 提示均明示本章未裁决）

## ch08 `ch08 a feast just out of reach.md`

- 章体量：17,807 字符（长章 >10K），块数 **8**（约 7%→98%，位置升序；含 4 个原文相邻连续多段块：L48/51/54、L252/255/258、L270/273/276、L411/414/417，均逐段 assert）
- ne_strict：块 8 | **FAIL 0** | WARN 0
- 短引语备案：`Auren Pell.`（10 字符）为独立成段短句，仅作为相邻三段块的中段使用，非裸短块；逐字回源 ch08 text 行 255 ✓

## 跨章指涉（当场 grep，记行号）

| md 位置 | 指涉 | 被引章 text/ 行号 | 结论 |
|---|---|---|---|
| ch08 B6「第一章写过的内应与凭据」 | Pell 给授权凭据 | ch01 text:51（`They were a gift from Pell, a chatty VisorForge tech…`） | 核上，md 只用中文转述、未引 ch01 英文 |
| ch08 B6 引语本体 | `Pell had slipped us the codes for BSMC-07` | ch08 text:258（本章内） | 核上 |
| ch07 nav/B3 | 身体分配（trapped in a Subsidiary / strut around in my skin） | ch07 text:39、63 | 全部本章内 |
| ch08「首次分离」 | `I left you behind, for the first time` | ch08 text:30 | 本章内自足 |

## 不敢下判断的清单（总览层勿采信任何补全）

1. **LYREBIRD 的本体**与叙述者是否等同：ch07 仅有自我等式（:105）与面罩眼描写（:117）、ch07:201/ch08 的点名不算证实；ch08:75 android 报错 `Two biological entities detected. One recognized.` 全库语境下含义本章未解。
2. **Aliers 点名时知道多少、凭何知道**（ch07:201）——本章不写。
3. **战舰的前主人与夺船经过**（ch08 只推到「他们夺了它」:51-54）。
4. **"我"（Sable）的来历**：`what had been done to me`（ch07:78）无内容；ch08:123 只写结果（太久没有感觉）不写原因；Fyster 在 ch08 仅有 `Fyster's bed on our wedding night`（:189）——婚姻在本章可写，**Fyster 之死不在 ch08 文本内**（仅 ch01:72 有 dead husband 佐证，若总览要用须引 ch01:72）。
5. **死亡影像的检索来源**：ch08:246-249 只写 `Four pinged LYREBIRD … you sent through footage`，不得断言「影像是 Four 的处刑日志」这一推断。
6. **Wylla 状态**：ch08 后半她封锁生命体征权限（:330）、沉默至章末，其结局/和解与否本章未写。
7. ch07:54 `the daemon … not affecting you any longer` 中 daemon 是什么，本章零解释——总览勿展开。

—— ne-g3（本组只写上述两章 md 与本报告；未做任何 git 写操作）
