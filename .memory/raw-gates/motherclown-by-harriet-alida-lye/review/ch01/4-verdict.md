# ch01 · T3 判定表

- 章：Prologue（md：`ch01 prologue a dream of leaving.md`；原文 `text/ch01_prologue.txt`，2,046 字符 / 368 词）
- R1 素读：`1-suread.json`（**独立子代理**，只读 `text/`，未开任何 md；7 条事实，锚点 7/7 唯一且 `text[start:end]==anchor` 自检通过）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok，6 块 / 6 片段，查无 0）
- R3 对账：`3-diff.md`（漏 3 提示 / 编 0 / 错 1 轻阻断）
- 覆盖：**全章 6 块逐块 R4 + R5**，无「只有机器层」的块

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 36 | finally / out of love / leave him | ✓ | ✓ 讲的是「三遍递进」这一写法本身 | ✓ **她**告诉**他**要走（不是他告诉她） | 通过 |
| 2 | 43 | freedom / orgasm / cresting | ✓ | ✓ 讲「自由＝梦中高潮、被醒来切断」 | ✓ 感受属于她；打断者是「醒来」本身 | 通过 |
| 3 | 36 | falling / dim milky light / first conscious | ✓ | ✓ 讲感官先到、人最后出现 | ✓ 醒来的是她，第一个念头指向女儿 | 通过 |
| 4 | 39 | retrospect / only forty / second life | ✓ | ✓ 讲「not just in retrospect」的自我防守与年龄条件 | ✓ 她替自己辩护 | 通过 |
| 5 | 40 | slow motion / jaw slack / river stone | ✓ | ✓ 讲四段坠落与「用温度代替死亡」 | ✓ 她走向他、她看见他的脸 | 通过 |
| 6 | 39 | only thing / any reason / dead | ✓ | ✓ 讲「先喊人再讲道理」的惊慌语序与举证式母爱 | ✓ **他**已死（被动事实）、**她**在自审 | 通过 |

形态（R2）：H1 `# 01. Prologue` ✓｜导航 5 项 ✓｜每块四子项齐全 ✓｜块数 6（本书中位 13、硬限 2–15，短章偏离已在生产期说明）｜中文密度：六块分析均 ≥100 汉字，CJK 占比远高于 15%。

## R5 判定表

| # | 断言（md 原文） | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 导航「发现丈夫已经**僵硬**」 | `text/ch01_prologue.txt` 1564–2046：`He was cold as a river stone.`（全文无 stiff/rigor） | 与原文不符（冷 ≠ 僵） | **阻断（轻）** → 已改为「已经冷透」 |
| L1 | （md 无此内容）女儿在 Max 家 | `text/ch01_prologue.txt` 589–638 | md 未收，非转折 | 提示（不修） |
| L2 | （md 无此内容）橙色反光紧身裤 | `text/ch01_prologue.txt` 935–987 | md 未收，物象后续章复现 | 提示（不修） |
| L3 | （md 未点明）他往常此时会看书 | `text/ch01_prologue.txt` 1564–1628 | md 用「身体先于意识」概括，未误导 | 提示（不修） |
| R4-6 | 「他死的那天早上写下罪名」 | `text/ch01_prologue.txt` 1970–2046 `whether her daughter would have any reason to love her now that he was dead` | 成立 | 通过 |

## 四组报数

- 逐字：6/6 块引语可核实（R2 查无 0）；词汇例句 4/4 逐字命中
- 对应：R4 6/6 块通过（含施事/受事追问 0 处反转）
- 形态：H1 ✓ 导航 5 项 ✓ 子项齐全 ✓ 块数 6 在硬限内
- 断言：1 条阻断（E1，已修）+ 3 条提示（不修）

## 已核实为正确（防误修）

| 写法 | 原文 | 说明 |
|---|---|---|
| 「她才四十岁」 | `text/ch01_prologue.txt` 1216–1287 `She was only forty.` | 年龄断言成立，后续章节的「四十一年」类表述才是错的（T1 已修） |
| 「她醒来后第一个念头是女儿」 | 1564 之前 1287–1564 `Her first conscious thought was, as always, to her daughter.` | 次序成立：先女儿、后丈夫 |
| 「他冷得像河里的石头」 | 1812–1861 `He was cold as a river stone.` | 温度比喻成立，不得改成「僵硬/尸僵」之外的体征描写 |
| 「梦里的自由像高潮」 | 589 之前 400–589 `like having an orgasm in a dream` | 成立；不要把它读成性描写 |
