# ne-g2 交付报告（ch04 / ch05 / ch06）

组前缀 ne-g2 · 书：Null Entity by Seth Haddon · 精简格式 · 完整 lane（library/ 有 epub，text/ 为章级提取件）

## 逐章交付

| 章 | 文件 | 引语块数 | ne_strict 阻断数 | 词表行数（高/进/基） |
|---|---|---|---|---|
| ch04 | `ch04 part of the subsidiary was in your head.md` | 8 | 0（WARN 0） | 10 / 8 / 4 |
| ch05 | `ch05 we revolted together.md` | 6（短章 4.7K，3–6 档） | 0（WARN 0） | 8 / 8 / 4 |
| ch06 | `ch06 i feel sick.md` | 8 | 0（WARN 0） | 10 / 8 / 4 |

引语与分析层英文全部在动笔前经 `/tmp/ne_g2_assert.py` 对各自 `text/` 做 `assert frag in src` 逐字断言（ALL OK）；引语无省略号、末尾均落句读边界；词表行一律从 `vocab_candidates.py --ch N --tiers` 输出粘贴后做减法。

## 跨章指涉（当场 grep 的行号）

- ch04 ↔ ch03：spores 修复／RABBIT 被侵染 = ch03:372,375,402,408,417,426；“Four shot calf” = ch03:393 ↔ ch04:18,60；Vick = ch03:180–195（Governor Elric Vick 被 Four 以合约条款逐下）↔ ch04:33。
- ch04 内部：Facility 34X 私信 = ch04:261；Thorned Root／sabotage 解码 = ch04:288,415。
- ch05 ↔ ch04：上一章末行“举枪” = ch04:515 ↔ ch05:15（开篇拍上 RABBIT 承接）；求救对象 Thorned Root = ch04:288,415 ↔ ch05:27；“If I didn't know better...”RABBIT 拟人 = ch04:149（仅中文转述，未在该章 md 引英文）。
- ch05 内部计数：Wylla 台词仅一处 = ch05:75（grep `you asked|you said` 唯一命中）；Thorned Root 全章仅 1 现 = ch05:27（grep）；末行两词 = ch05:117。
- ch06 ↔ ch05：枪响承接 = ch05:117 ↔ ch06:15–21（ch06 首三自然段顺序经 `src.find` 验证）；“heard it before, on GTM-11” 的声线 = ch03:438–444（“It was her, that measured voice…”＋Thorned Root 公告原文）↔ ch06:402–408。
- ch06 内部回指：kiss/“code inside a mask” = ch06:150（未向更早章锚定——ch02/ch03 grep `kiss` 无命中，故不指章）。

## 页码 bleed 规避（ch04）

- 避开 `Nervous system:…`（ch04:72，含粘连省略号形态）——本章引语从其后的 ch04:78 段落起取；
- 避开论坛串中 `one confessed n called himself “Iron Vine.”`（ch04:347，疑似 bleed 断句）与 `To think it was human once…`（ch04:182，行尾粘连省略号）——均未入引语块。

## 不敢下判断的清单（总览层需用）

1. **换体机制**：ch05 末枪响 → ch06 “I 在 Wylla 体内 / Wylla 在 Subsidiary 体内”的因果，书中未解释；ch06:261 只有 “This was probably LYREBIRD's fault, somehow”——不可当定论。
2. **ch04 双重读法未裁决**：daemon 是“把两人引到站”（ch04:485 the daemon had meant for us to arrive）还是“第二次跳跃根本未发生、Four 一直在船上”（ch04:515,518）——两种读法文本兼容，本组未择一。
3. **RABBIT 的“变新”**：ch06:378 Brighter. Livelier. 原因未写（可能与 ch05:18 植入 daemon/凭据有关，书中未确认）。
4. **船牌 TR.Δ.SAB.05.（ch06:396）与论坛代号 Δ-SAB-TR（ch04:285,288）同组织无疑，是否同一支小队在编未核**。
5. **首章「She's back」的 she、I＝LYREBIRD 的全书等式**：本组三章内 Wylla／Sable／Sable Veonya／Wylla Sotain 均有点名（ch04:101,167；ch05:90；ch06:87），但「开篇的 I 即此 Sable」需以 ch01–03 证据链裁决，超出本组章。
6. **Pell 现状**：ch04:155 仅“swiped away VisorForge's update reminder”（Pell 不在场也未提及），不可推断其状态。
7. ch04:33 “And then there was Vick” 的具体含义（Vick 案与“控制市场/改写能动性”论据的连接）为叙述者压缩表达，本组按 ch03 原文事实引用，未再加演绎。

## 其他

- 未执行任何 git 写操作；只写了上述三个 md 与本报告；临时脚本在 `/tmp/ne_g2_assert.py`。
- 短引语说明：ch05 原句 1 的第三段 `But I had no choice.`（21 字符）、ch04 原句 5 第二段 `The Subsidiary, I said.`（25 字符）均逐字在各自 text/（已在断言脚本内校验）；无 <20 字符裸引语。
- 五步审查：未做（待用户发起）。
