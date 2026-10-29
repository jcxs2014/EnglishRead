# ch02 对账（R1 8 条 / relations / numbers 4 ↔ md 6 块）

## 漏（素读有、md 无）→ 已修
| 素读条目 | 修前 md | 处置 |
|---|---|---|
| 失联前二十分钟 Jelka 说闻到肉味；Leah 也这么想；Matteo 让她捏鼻子；Leah 没帮腔 | 只在导航「人物弧线」一句带过 | **已修**：新增原句 4（`There was nothing, of course… didn’t say anything to back her up.`，50 词） |
| 通讯面板先断、Matteo 让 Leah 找信号、她按键念无意义的话 | 无 | **已修**：新增原句 5（`At first it was only the comms panel… what I was on about.`，69 词） |
| 十分钟后整艇离线、通讯更像被关掉 | 原句 4（现原句 6）已有 | 保留，切为单句（43 词） |

## 编（md 有、原文无）
无。修前 Q4 的「衰减 vs 关掉」「more pressing things」均逐字在 `text/ch02_leah.txt` 末段。

## 错（两边不一致）
无。数字核对：`six thousand metres`（Q1）、`several centuries`（词汇表 Uneroded 例句）、`Twenty minutes`（Q4）、`Ten minutes`（Q6）全部逐字一致。

## 修复过程中的两次退稿（记录以免重犯）
1. 首版 Q4 把 `…something cooked.` 与 `When Jelka repeated…` 直接连写，中间漏掉两句（`I remember I looked to my own fingers…` / `There was nothing, of course…`）→ chapter.sh 报「查无 1」。**教训**：同一自然段内跳句也必须显式用 `…`，否则等于拼接。
2. 首版 Q6 把 `radio.` 直接接 `Ten minutes later`，跳过 `expecting the Centre to come back online…` → 同样「查无」。最终改为「Q5 = 前三句（69 词）+ Q6 = 末句（43 词）」。
