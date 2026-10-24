# ch06 Rosehill — 判定（R5）

- 机器层：`bash scripts/chapter.sh "…/ch06 rosehill.md" --json` → **rc=0**，verdict=ok，块数 4、words 1395、空引号 0、查无 0、子项缺 0、关键词 0 缺、形态偏离 0、块数区间 [3,10] 内。
- 素读锚点：8/8 命中（脚本核对，行号全中）。
- 报数：**逐字 0 / 对应 0 / 形态 0 / 断言 1**（1 阻断、4 提示）——漏 2（墓园中段、Lucinda 提议理由）、编 0、错 2（甜筒、一年之内）。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| md :91「墓碑上，Jasmine 与 Malcolm 后面跟着同一组日期」 | `text/ch06_rosehill.txt:108` `Jasmine` + `:111` `3-8-1976—2-10-2014`；`:114` `Malcolm` + `:117` `11-2-1976—2-10-2014` | 生年日期不同（3-8 vs 11-2），仅卒日相同。改「两人卒于同一天 2-10-2014」 | **阻断** |
| md :91 与 :13「拎着化掉的甜筒穿过大门／走进去」 | `:53` “licking our rapidly melting ice cream”（边走边吃）；`:88` “Lucinda takes the last bite of her ice cream cone…”（进门前已吃完）；`:93` 才进大门 | 细节外推，原文无「拎进墓园」；删或改为「边走边吃」 | 提示 |
| md :12「父母、外婆、两个舅舅，一年之内全没了」 | `:122` “but a year later there was a fire, probably from a gas leak” | 火在父母死后一年，五人死亡跨约一年；非硬数字错，宜写「一年后」 | 提示 |
| 漏：墓园中段（“Tell me again what they said?” → 《You're All I Need to Get By》→ 忍哭 → 种树／墓园将成森林） | `:127–131`、`:154–155`、`:164` | 四个块未覆盖，仅 `:91`「只有一首歌的旋律」一句带过；导航 :11 仍交代了墓园线与时间旅行，情节未断 ⇒ 记提示 | 提示 |
| 漏：Lucinda 提议去 Rosehill 的理由（回家会被派活） | `:48` “If we go back to my house they’ll just put us to work,” Lucinda points out, correctly. “Let’s go to Rosehill.” | 非关键事件，未损因果 | 提示 |
| md :14「Celia 在正文里没有一句台词，只出现在别人的转述里」 | `:23/:30/:67/:71/:75` 均为叙述或转述；`:174` “Celia arrives a few minutes after we do.” 只有动作 | 断言成立 | 假红（核后成立） |
| md 引语 4 块 / 词汇 13 条例句 | 逐条回 `text/ch06` 命中本行（见 `3-diff.md` 第五节） | 逐字无误、未跨章 | 假红（核后成立） |
| 抬头 `Alba is 42`（2023-09-07） | `:18` “Thursday, September 7, 2023 (Alba is 42, Lucinda is 16)” | 原书原文，非缺陷；md 未据此刻算年龄（`grep -n "42 岁"` 零命中） | 假红（按派工方口径） |

## 处置建议（只报不改，审查方不动书稿）

1. 必改 1 处：`:91` 的「同一组日期」。
2. 可选 3 处：甜筒画面、`一年之内`、墓园中段可加一块（`We love her very much` + 歌名 + 忍哭是全章情绪落点，加块比写在总结里更贴 R4）。

## 已核实为正确

- **抬头年龄**：`text/ch06_rosehill.txt:18` 原文即 `Alba is 42`，属原书自相矛盾（2023 年 Alba 不可能是 42），**不作为本书缺陷**；md 未据此推算，记录备查。
- **「Celia 无台词」**：六处出现均为叙述/转述 + 一次进门动作，成立。
- **5'10" → 5 英尺 10 英寸**：`:25`，换算正确。
- **350 acres**：`:98`，照抄未夸大。
- **词汇 13 条**：例句全部落在本章，无跨章搬句、无改写。
