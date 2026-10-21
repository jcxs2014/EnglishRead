# the-dues-don-ts-of-magic-by-delemhach · 复核判定表（2026-10-21）

抽样：ch01 首章 / ch31 夜谈·重述章 / ch43 末章 + `00_概述.md` 全篇。
机器层：全书 43 章 + 总览三篇全量。

## 机器层（全绿）
| lane | 结果 |
|---|---|
| `gate.sh` 20 lane | **EXIT=0，阻断型 0** |
| 引文逐字 | 487/487（100%），428 条本章命中、跨章 0、拼接 0、全书查无 0 |
| 逐章归属 | 全部命中，跨章 0 |
| 总览引文 | 59/59（100%），跨缝隙拼接 0 |
| 中文层 | 430 块 / 密度 100% / 夹杂 0 |
| 语料 | `verify_corpus --expect 43` PASS |

## 人判层

| # | 位置 | 问题 | 原文依据 | 档位 |
|---|---|---|---|---|
| D1 | `ch31 …md:10` 导航 · `:167` 一句话总结 | 「她……**因此欠了 Pesch 一笔后酬**」——方向反了 | `text/ch31:124` "I may have taken some of my **back pay** that he would've refused to give me"；`:199` 同 ⇒ **Pesch 欠她**，她自行取走 | 阻断 |
| D2 | `ch31 …md:114`（原句 10 分析） | 「**提议的是 Spidena**……她自己也招架不住」 | `text/ch31:316-319`：酒是 **Paulav** 提的——前一句是他切洋葱，紧接着 "He rose in a hurry and darted over to **his** caravan" | 阻断（说话人错配） |
| D3 | `ch31 …md:10`、`:167` | 「**Spidena** 结结巴巴地提议『今晚该喝点酒』」 | 同 D2；「我——我觉得」的结巴也是 Paulav 的 | 阻断 |
| D4 | `ch43 …md:110` 中文理解、`:167` 一句话总结 | 「他得到了**她的**第一个吻」 | `text/ch43:208` "at least **he'd had his first kiss**" ⇒ 是**他的**初吻 | 阻断 |
| D5 | `00_概述.md:13` | 「他七岁那年被父母卖掉，**原因是母亲被带走**后家里需要钱」 | 「母亲被人带走」是 **Spidena** 的（`text/ch31:199`/`:223`、`text/ch14:115`「The Hounds are why I lost my mother」由 Spidena 说）。Ben 只说「父母在卖我那天早上才告诉我」（`text/ch11:34`） | 阻断 |
| P1 | `ch31 …md:44`（原句 3 分析） | 「她**还在乎那个人**」——若指 Pesch，与原文相反 | 她骂 Pesch「ick／slimy」，维护的是**那帮打手** | 提示 |
| P2 | `ch43 …md:10`、`00_概述.md:36`、`:57` | 「Wolf **衔着**烧到珠子的丝线落下」 | `text/ch43:175-181`：弹珠与丝线是 **Earhav** 掏出、点燃的，Wolf 只是「在火焰烧到弹珠时俯冲而下」 | 提示 |
| P3 | `ch01 …md:10` | 未提门外的二十个大个子（Ben 不敢出店是因为他们在外面） | `text/ch01:211` "helping those **thugs outside**"、`:112` "I can’t leave this shop right now" | 提示（漏） |
| P4 | `ch01 …md:94` | 同一段落里「本章最见功力的一处」出现两次 | — | 提示（重复措辞） |
| P5 | `ch31 …md:14` | 术语 Hound 译作「猎巫犬」 | `text/ch13:16-37`：Hounds 是军中单位，负责抓捕魔法使用者；译名可商榷 | 提示 |

## 结论
阻断型 **5**（全部是「谁做的 / 谁的 / 欠谁的」这类关系与归属断言）；提示型 **5**。
`verify_quotes` 487 条全绿、总览 59/59、中文层 430 块密度 100% —— 这 5 条在机器层**结构上不可见**。

## 订正（2026-10-21，审查方自查；执行方回原文指出，逐条复核后确认）

审查方有三条「前提不成立」，执行方未照抄、按原文处置，**处置正确**：

| 编号 | 审查方原断言 | 实际 | 根因 |
|---|---|---|---|
| C10-1 | 「全书 `lightning|bolt|struck by` 零命中，无雷击情节」 | `text/ch10:265` 有 "It's like seeing someone get **struck by lightning five times** in a row" | 用了 `grep 'a\|b'`，**BSD grep 的 `\|` 不生效**，当字面量匹配 ⇒ 假零命中 |
| P25-1 | 「`seven` 全章零命中，七个红大衣士兵无出处」 | `text/ch25:137` "Behind him were **seven other** soldiers"；`text/ch25:112` "all wearing matching red coats" | 同上（交替式未生效 + 上下文不匹配） |
| P11-2 | 「军营谚语全章未覆盖」 | `ch11 doddering around.md:13` 已用中文写进「叙事手法」 | 只查了引语块，没查导航层 |

⇒ 审查方新增纪律（已写入 `docs/rules/审查表.md` R5-补）：
**「零命中」类断言必须贴命令与输出，交替匹配一律用 `grep -E`；给不出命令的只能写「未核」。**
本文件的 C10-1 / P25-1 / P11-2 三条前提作废，其「改后文字」以执行方按原文的版本为准。
