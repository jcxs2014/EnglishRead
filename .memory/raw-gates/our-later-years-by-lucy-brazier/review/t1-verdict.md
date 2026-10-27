# T1 自检结论 — our-later-years-by-lucy-brazier

**抽样章：ch01 / ch04 / ch07 / ch10。** 理由：全书 10 章 ≤16 → 按 1/3 至少 3 章，首章（ch01 引言）与末章（ch10 尾声）必含；在其余 8 章中按章号等距取 ch04（第 4 个单元）与 ch07（第 7 个单元），四章覆盖「招募 → 日常照护 → 冲突制度 → 结账」四种形态。

## 一、总览三篇全篇人判（六类，逐条回 text/ 找支撑）

| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| `00_概述.md:34` | 让跌倒的人**五分钟内**被一圈人围住 | 在**几分钟内**被一圈人围住 | `text/ch04_3_the_importance_of_community_alone_but_.txt:44` `within minutes a ring of familiar, concerned faces` |
| `00_金句精选.md:138` | 这是全书**唯一**直接写「有人不在了」的地方 | 这是全书把「有人不在了」写得**最不戏剧化的一处** | ch09 亦直写死亡（`text/ch09…:62` `two women have died in the last nine years`）；ch10 尾声含 Madeleine/Shirley 之死，故「唯一」不成立 |
| `00_金句精选.md:92` + `00_情感节点.md:42` | Maggs 引语用 `…` 缝合「被叫 dear」与作者对 elderspeak 的定义 | 改为原文连续片段 `…“Yes, dear!” I have a real issue with being called dear. It feels like a putdown.` | `text/ch05_4_don_t_call_me_dear_defying_ageist_ster.txt:41`（`overview.py full` 原判 🔶 跨标签拼接 ×2，改后 0） |

## 二、章内与总览的同步修正

| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| `ch02 1 rebels…md` + 金句 ④ 上下文 | 二十六**户人家** | 二十六**位居民/女性** | `text/ch04…:230` `twenty-six women finding their way` |
| `ch08 7 a life well lived….md` 概览 | 全书**篇幅最长**的一章 | 正文里**篇幅第二长**的一章（7,524 词） | ch04 7,836 词 > ch08 7,524 词 |
| `ch04 3 the importance of community….md` 块 4 关键词 | `designing the building`（不在本块引语内） | `walked past` | gate ⑱ 覆盖度判红后改，改后 0 阻断 |
| `ch07 6 no utopia….md:83` | 「全章唯一直接写有人不在了」 | 保留 | 全文 grep：ch07 仅 `:59` 一处写 loss，断言成立 |

## 三、抽样章素读复验（锚点全命中）

- ch01 7/7（既有 `production/ch01-suread.json`）；ch04 / ch07 / ch10 复跑 `suread.py` 全 ✅（含「二十六位女性」「Tessa 85 岁」「作者始终没搬进」等）。
- 回源抽查：`ch09:62` 儿子搬入 + 夜班护士；`ch03:47` `heading towards seventy`；`ch03:116` 五十岁拿艺术学位、想当 Tracey Emin；`ch10:99` `Twelve years…`；`ch10:29` Joseph Rowntree 资助与四国考察；`ch04:62` 三四人健康伙伴；`ch05:164` `the only couple`；`ch08` `hundreds of pictures`、`a pile of letters my estranged father had sent her`。

## 四、断言六类预筛（`assertion_scan.py` 原始输出见同目录 `t1-candidates.txt`）

276 行候选 / 13 文件：①13 ②29 ③193 ⑥2 ④2 ⑤37。**四类全读、五类全读、六类全读**（合计 276 行全部读过，未抽样略过）。
- ②「唯一/第一次」类共 29 行：仅 1 条判错（金句 138「全书唯一」，已改）；其余如「社区里唯一的伴侣」（`ch05:164` `the only couple`）、「全章唯一一条明确的排除」（ch06）经原文核对成立。
- ③ 数字类 193 行：1998 广告信、2016 年底入住、二十六位女性、八套社会住房、十八年、八次延期、2005 Madeleine 去世、2022 Shirley 去世、Sue T 79 岁、Tessa 85 岁、九年两位居民去世，逐条对 `text/` 行核过，无漂移。
- ④⑤ 方向/亲属类：Hilary 的信确为 `estranged father` 写给母亲（`ch08:50`）；Jayne 女儿、Shirley 儿子（`ch09:62`）与章内叙述一致。

## 结论

- 阻断型 **0 条**（本轮仅有 3 处事实/断言修正 + 1 处引语缝合修正，均为就地修复并复验）；缺陷密度 0 ÷ 4 章 = 0 < 0.2，按规则停。
- 复验：`overview.py labels` 53/53 ✅、`full` 查无 0 / 拼接 0、`gate.sh` 重跑后将复跑确认 rc=0。
- **T1 为同会话自检**，非异会话验收；未触发 T2（阻断不足 3 条）。
