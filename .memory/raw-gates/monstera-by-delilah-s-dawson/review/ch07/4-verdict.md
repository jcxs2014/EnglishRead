# ch07 the seed in her lashes —— R4 逐块追问 + R5 定档

## R4：固定追问（主语是谁／受事是谁／归属方向）
| 原句 | 主语 | 受事 | 归属方向 by/to/from/of | 判定 |
|---|---|---|---|---|
| 1 | Saskia | 牙缝里的糖霜 | `in her bathroom`／`in her teeth` | 通过 |
| 2 | Saskia | 她自己（处境） | `like Lucy`／`around the country` | 通过 |
| 3 | Saskia（自问） | 那几个小时／Lucy | `in Lucy’s apartment`／`by a steamroller` | 通过 |
| 4 | Saskia | 她自己的身体 | `behind her knees`／`of her thighs` | 通过 |
| 5 | Saskia | 睫毛与绿藤 | `apart`／`at its end` | 通过 |
| 6 | Saskia | 种子与她自己 | `in the toilet`／`to Lucy` | 通过 |

## R5：定档（阻断／提示／假红／跳过）
| # | 观察 | 档位 | 说明 |
|---|---|---|---|
| 1 | 引语逐字 6/6（含新增块）、词表 12/12 | — | `chapter.sh` rc=0；`check_vocab` 过 |
| 2 | 形态：H1 07. Chapter 7 / 导航 5 项 / 块数 6 | — | 落 ⑱ 3–8；本章 374 词，块数偏多属短章特例 |
| 3 | 导航把 `promises` 当引语分析，但该句不在任何块内 | **提示 1（已修）** | 补写原句 6（`:52` 整段），块数 5→6 |
| 4 | `It’s better this way.`（`:500`）／`She deserves so much more.`（`:2096`）未入块 | 假红（非缺陷） | 均为独立单句段、3–5 词；不可单块、不可跨段拼接，内容已由导航与一句话总结承载 |
| 5 | 「just popcorn and lemonade and cake」「They totally did」 | 已核实为正确 | `text/ch07_chapter_7.txt:16`／`:22` |
| 6 | 四个独立成段的短句（She wanted to? 等） | 已核实为正确 | `:10/13/31/34`，与导航「叙事手法」所述一致 |
| 7 | 「another」指她此前拔过一粒 | 已核实为正确 | `:49` `another tiny black seed`；前一次在第四章（手腕） |

## 计数
- 阻断 **0** ／ 提示 **1（已修）** ／ 假红 **1（非缺陷）** ／ 跳过 **0**
- 逐字：引语 6/6、词表 12/12｜对应：0｜形态：合规｜断言：0 条落空

## 已核实为正确
1. `brushing the sugary frosting out of her teeth` 与两条理由——`text/ch07_chapter_7.txt:4`。
2. 远程办公、同事一个也没见过、`It’s better this way.`——`:4`。
3. `Did she really spend hours in Lucy’s apartment?`——`:7`。
4. 拥抱与 `permafrost thawing`——`:25`。
5. 检查部位清单与 `horrorscape of skin`——`:40`。
6. `another tiny black seed tipped with blood`——`:49`。
7. 丢马桶＋承诺＋`The poor girl deserves that much.`——`:52`／`:55`。

结论：**本章补 1 块（提示），无阻断**；修后 `chapter.sh` rc=0、`structure.py order` 29 md / 167 块 · 0 缺陷。
