# ch01 判定（R4 逐块）

块数 12。判定符号：✅ 通过；❌→已修 = 判阻断并已就地修好。每条附「施事三问」中出问题的那一问。

| 块 | 引语起头 | 中文理解 ↔ 引语 | 关键词在引语内 | 为什么这样写 | 判定 |
|---|---|---|---|---|---|
| 1 | `Unyielding. In control.` | 一致（「不屈。冷静。」对应两个独立短句） | 3/3 | 「三个词单独成句」与原文 `Unyielding. In control.` 相符 | ✅ |
| 2 | `Then she’d come to him` | 一致；`his father’s eyes` 译作「借父亲的眼光」未越界 | 3/3 | 三个形容词的递进（changed / unraveled / reckless）确在引语内 | ✅ |
| 3 | `Broken glass stretched across` | 一致；`earthbound constellation` 译「坠地的星座」 | 3/3 | 材质→废墟→比喻的顺序与原文一致 | ✅ |
| 4 | `In the midst of all this devastation` | 一致 | 3/3 | 「第一次以全名登场」可核：`text/ch01_chapter_one.txt:27` 是本章唯一一次 `Alaric Ossinast` | ✅ |
| 5 | `But Alaric didn’t realize he was the last` | 一致 | 3/3 | 引语内 `transmuting` 解释到位 | ❌→已修：读者视角提示把黑衣人叫「七夫雷姆」（**谁做的**一问）；原文 `36:` 为 `Sevraim’s irate cry`，已改「塞夫雷姆」 |
| 6 | `The fracture began in the pit` | 一致 | 3/3 | 生理词汇与修补术两套语域的判断成立 | ✅ |
| 7 | `“By the ancestors, I’ve still got it!”` | 一致 | 3/3 | 「玩笑断在半途」可核：`text/ch01_chapter_one.txt:72` 结尾 `this old . . .` 后接 `He trailed off` | ✅ |
| 8 | `Alaric looked down.` | 一致 | 3/3 | 礼服对照成立 | ❌→已修：提示称贝洛克「此后反复出现」（**谁的**一问跨章）；`grep -l 贝洛克 ch*.md` 仅 ch01，本章 2 处（`102:` / `159:`），已改为「本章两次出现」；另修「高几分钟前**高**提过的伤」重复字 |
| 9 | `It would have been better` | 一致 | 3/3 | 「当众崩溃」读解成立 | ❌→已修：病房名单写「杰、尼亚姆哈、**高**」（**谁做的**一问）；`144:` 原文为 `Jie, and Niamha … Several other nobles … majority … Iantas’s soldiers`，Gao 不在病房；已改「几位受伤的贵族 + 中毒的伊安塔斯士兵」 |
| 10 | `Niamha sprang out of bed.` | 一致 | 3/3 | 「婚约经手人」可核：`144:` `who had once upon a time delivered the offer of marriage` | ✅ |
| 11 | `“My lady,” came Sevraim’s reply` | 一致 | 3/3 | 「命令只管用了第一天」与 `since the first day … because I was ordered` 相符 | ❌→已修：转述逼问漏 `halfway`（`267:` `I might as well make sure I’m halfway to the edge of Lir by then`），且写「**第一次**当众施压」属不可核计数断言；已补「走到去利尔的路上一半」并改为不计数表述 |
| 12 | `Because something tells me that”` | 一致 | 3/3 | 「末句归属作者故意不给」与原文双引号嵌套位置相符 | ✅ |

## 施事三问小结

- **谁做的**：块 5（黑衣人＝Sevraim）、块 9（病房名单不含 Gao）两处错，均已按原文改正。
- **谁的**：块 8 贝洛克「此后反复出现」跨章无据，已改为本章两次。
- **谁说的**：块 11 转述塞夫雷姆的逼问漏 `halfway`，已补；块 12 末句归属在原文中确实悬置，md 未擅自指派 ✓。

## 判定表

- 阻断 **5** 条（B1 / B2 / B3 / C1 / C2），全部已修，`chapter.sh` rc=0 复跑通过。
- 提示 **2** 条（重复字、关键词行长度），均已在本次修复（关键词收紧独立提交 `26e3efd2b`）。
- 假红 **0**。
- 跳过 **0**。

## 已核实为正确

- 12 条引语全部逐字命中原文（`quotes.py` 与 `chapter.sh` 双查，查无 0）。
- 块 4「全名首次登场」、块 7「玩笑断在半途」、块 10「婚约经手人」、块 11「命令只管第一天」四处可计数 / 可指认断言，已逐条回原文取证。
- 修复后 `bash scripts/chapter.sh` rc=0、0 ⚠️；`bash scripts/gate.sh` rc=0、正门结论 0 条阻断型。
