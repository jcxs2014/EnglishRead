# ch19 · T3 判定表

- 章：Chapter Nineteen: 2025（md：`ch19 chapter nineteen 2025.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，不看 md）
- R2 机器层：`2-machine.json`（第二实现；重跑后 verdict=ok）
- R3 对账：`3-diff.md`
- 覆盖：全章 6 块，逐块 R4 + R5；无「只有机器层」的章

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 40 | Rockaway / condo / 117th Street | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 2 | 54 | jetties / eight lifeguard chairs / nobody depl | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 3 | 42 | expertise / two-piece bathing suits / National | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 4 | 56 | porpoise / pushing off the ground / bureaucrac | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |
| 5 | 35 | on her deathbed / never going into the ocean a | ✓ 命中 | ✓ | ✓ 与原文一致 | 已修·阻断 |
| 6 | 38 | body is slowing down / smaller wave / over six | ✓ 命中 | ✓ | ✓ 与原文一致 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| R1 转折点「Barbara 临终那句『Janet, I'm never going into the ocean again』」只出现在导 | text/ch19_chapter_nineteen_2025.txt:  原文逐字：When Barbara was on her deathbed, she said something that stuck with me: “Janet, I’m ne | R3 漏＝阻断（关键转折未在引语层出现） | 阻断 |
| 新增的原句 5 起初 29 词，低于 30–70 词软下限 | （见左）已修：向后扩一句（29→34 词，仍是原文连续一段，仍 3 句） | 表面成立，措辞正当 | 提示 |
| 「116 街两座防波堤之间摆八把救生椅，四把就够」 | text/ch19_chapter_nineteen_2025.txt:22：原文逐字：Between the two jetties at 116th Street, the Parks Department has dropped eight lifeguard chairs where fo | 回原文核对后成立 | 假红 |
| 「国家公园管理局早在 1994 年就给自己人配上了两件式」 | text/ch19_chapter_nineteen_2025.txt：原文逐字：the National Park Service got their own two-pieces back in 1994 | 回原文核对后成立 | 假红 |
| 「她管这种浪叫『过六十』的浪」 | text/ch19_chapter_nineteen_2025.txt：原文逐字：it’s what I call an over sixty wave | 回原文核对后成立 | 假红 |

## 分组计数（只报四组）

- **逐字**：6/6 块整串命中，查无 0（`2-machine.json` 重跑 verdict=ok）
- **对应**：阻断 0，提示 0
- **形态**：阻断 0（H1 形态、导航 5 项、4 子项齐备、块数 6 在本书众数区间、编号连续无撞车）
- **断言**：阻断 0，提示 0，假红 3

## 阻断

- **[漏]** R1 转折点「Barbara 临终那句『Janet, I'm never going into the ocean again』」只出现在导航层，引语层无对应块——块序上位于 porpoise 块之后、over sixty 块之前
  - 判据：R3 漏＝阻断（关键转折未在引语层出现）
  - 证据：text/ch19_chapter_nineteen_2025.txt:  原文逐字：When Barbara was on her deathbed, she said something that stuck with me: “Janet, I’m never going into the ocean again.” She didn’t elaborate, but she didn’t need to.
  - 处理：已修：新增第 5 块（32 词），原块 5 顺移为 6

## 提示（只记不改）

- **[形态]** 新增的原句 5 起初 29 词，低于 30–70 词软下限
  - 判定：已修：向后扩一句（29→34 词，仍是原文连续一段，仍 3 句）

## 已核实为正确

> 以下写法表面像错，回原文核对后成立——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 「116 街两座防波堤之间摆八把救生椅，四把就够」 | 回原文逐字核对一致 | 原文逐字：Between the two jetties at 116th Street, the Parks Department has dropped eight lifeguard chairs where four would be enough, while the ten blocks east and west have nobody deployed. | text/ch19_chapter_nineteen_2025.txt:22 |
| 「国家公园管理局早在 1994 年就给自己人配上了两件式」 | 回原文逐字核对一致 | 原文逐字：the National Park Service got their own two-pieces back in 1994 | text/ch19_chapter_nineteen_2025.txt |
| 「她管这种浪叫『过六十』的浪」 | 回原文逐字核对一致 | 原文逐字：it’s what I call an over sixty wave | text/ch19_chapter_nineteen_2025.txt |
