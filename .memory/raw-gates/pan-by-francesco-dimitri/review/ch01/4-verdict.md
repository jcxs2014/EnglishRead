# ch01 判定表（R4 逐块 + R3 三单）

审查：异会话（用户点名 T3）｜素读先于读 md｜机器层 `2-machine.json` rc=0

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 一句话总结「三个孩子各得到一件现实禁止的东西（家人…）」 | `text/ch01_things_that_happen_on_roman_nights.txt:18` `His family has been wiped out by something` | Timoteo 未得到家人，只在梦里逃向藏身处 | **阻断**（已改为「藏身处／完整的脸／饱饭」） |
| 块 2 未写「他知道有个安全的地方、会有英雄保护他」 | 同上 `:18` `he knows that there is a safe place where a hero will protect him` | 本章唯一一次给出希望、也是主线伏笔，属漏 | **阻断→已补**（读者视角提示） |
| 块 3 中文理解「她不想让这个辉煌的生物在胎记那块污染她的嘴唇」 | `:21` `she doesn’t want this splendid creature to taint her lips on the Mark` | 英文 `taint her lips on the Mark` 的施受可两读（胎记污染美人鱼的唇／美人鱼的唇落在胎记上），中文取了字面语法，属歧义非错 | 提示 |
| 块 2 引语是否跨段拼接 | `:18` 连续同段两句（`…villages. His family has been wiped out…`） | 同段连续子串，非拼接 | 假红 |
| 块 9 耳语者归属 | `:174` `a graceful figure comes close` + `lowers their lips to his remaining ear` | 「那个声音贴着 Luca 的耳朵」成立（Luca 只剩一只耳） | 假红 |
| 导航「三节用罗马数字分格」 | `:15` `I`、`:42` `II`、`:90` `III` + 三次 `These things happen, on Roman nights.` | 成立 | 假红 |
| 块 8 中文理解含 San Basilio 街景（引语外） | 该段原文在块 8 引语前一段 | 分析层引上下文属本书通篇体例，机器层亦不判 | 提示（不修） |
| 词表「children sleep」列为主谓短语 | 表内释义已写「本章第一句的主谓」 | 词条形态偏离（应为词/短语），不产生事实错误 | 提示（不修） |

## 已核实为正确

- 块 2 引语为同段连续两句：`text/ch01_things_that_happen_on_roman_nights.txt:18`，原文 `Curled up in a tattered blanket…His family has been wiped out by something…` 之间无空行、无省略，属单段连续子串，后续不得以「跨句拼接」改动。
- 块 9 的施事：`text/ch01…:174` `a graceful figure comes close. A bare foot, too big for a child…they whisper`——低语者是那个赤脚身影（复数 they），不是「孩子们」，md「那个声音」的写法成立。
- 导航「叙事手法」的罗马数字分格：`text/ch01…:15`（I）、`:42`（II）、`:90`（III），三节确为 I/II/III，回环句在 `:40`、`:88`、`:176` 各一次。
- Wendy 年龄与档期：`text/ch01…:45` `She is twenty-five`、`:47` `Tonight is the Eve of the Epiphany`——「二十五岁」「主显节前夜」成立。
- Giulio/Luca 家世：`text/ch01…:165` `sons respectively of an architect and one of Rome’s leading business consultants`——块 8 的「建筑师与罗马顶级商业顾问」逐字对应。
