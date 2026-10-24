# ch48 Night Music — R5 判定

- 机器层：`bash scripts/chapter.sh "ch48 night music.md" --json` → rc=0，verdict `ok`
- 块数：6（本书 71 章中位 6、最高 10；lo 2 / hi 15，未触上限）
- 原文 2165 词 / 精读 113 行

## 一、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 六块引语逐字 | 逐块与 `text/ch48_night_music.txt` L24/L41/L130/L223/L285/L297 对齐，6/6 命中，0 处改字 | 真 | 跳过 |
| 抬头与年龄 | `text/ch48_night_music.txt:18` `Tuesday, November 5, 2041 (Oliver is 13 and 35)` | md 作「二〇四一年十一月五日…三十五岁的奥利弗」，一致 | 跳过 |
| 「第四晚失眠」 | `:23` `Tonight is the fourth night of bad sleep.` | md 作「又一次失眠」＋b5「第四次睡不着」，一致 | 跳过 |
| 猫 Gwen 从 Madeline 椅子上看他 | `:24` `Gwen the Cat is staring at me from Madeline's chair, her eyes strangely reflective in the moonlight.` | b1 中文全对 | 跳过 |
| 黑雨衣一段未收 | `:24` `There's a black raincoat that I remember Madeline wearing, big and billowy; it will have to do.` | 未进任何块；导航与一句话总结未交代取舍 | 提示 |
| 十三岁自己看生日视频 | `:34` `Thirteen-year-old me is sitting up in bed.` | 未收 | 提示 |
| 中餐馆与幸运饼干 | `:84` `She took me to a Chinese restaurant yesterday.` | 未收（幸运饼干两句原文同段） | 提示 |
| 芝加哥的朋友 | `:195` `He's in America, in Chicago.` | 未收 | 提示 |
| 父母将死于狱中 | `:291` `When my parents die in prison, under circumstances that are still unknown to me, Madelin…` | 未收；系 b3 同段预言的后半，md 以「说音乐会成为他的家」概括同段 | 提示 |
| 父母怕她不收他／叔叔不知情 | `:219` `My parents thought you would not accept me as a student if you knew I was a time traveler…` | 未收 | 提示 |
| 一句话总结「为少年与自己弹」 | `:285` `I mean to reassure my young self, and to beguile Madeline—it is her favorite.` | 受事应为「少年与玛德琳」；b5 中文正确，仅总结句可读成「与自己」 | 提示 |
| 三十段变奏、三百年前 | `:297` `Bach was commissioned to write these variations by an insomniac, Count von Keyserling…` | b6 中文（30 段、300 年、烛光）全对 | 跳过 |
| 导航五项 | 「失眠第四晚」「从贝尔塞兹公园跌进琴房」「上楼见十三岁的自己」「中文说一夜话」「被玛德琳撞见→弹《哥德堡变奏曲》」 | 五项均有原文对应 | 跳过 |

## 二、报数

- **逐字**：6/6 块引语逐字命中，0 偏差（含省略号处均按分段独立取证）。
- **对应**：6/6 块中文确实在讲该块引语；无「引语选短到失真」、无「拿一句讲全书主旨」、无「只复述字面」。
- **形态**：H1 `# 48. Night Music` 形态与本书一致；导航 5 项；子项 4 项齐（中文理解／关键词／为什么这样写／读者视角提示）；块数 6＝本书中位。
- **断言**：md 内可核数字/时序断言 6 条（日期、13/35 岁、第四晚、30 段变奏、300 年、三点式预言）全对；1 条受事表述待改（见上表）。

## 三、已核实为正确（下一轮勿误改）

1. 抬头「二〇四一年十一月五日」「十三岁与三十五岁」——原文 `:18`。
2. 「今夜是第四晚睡不好」（b5 中文）——`:23` `Tonight is the fourth night of bad sleep.`
3. 猫「格温」从 Madeline 的椅子上盯他、眼睛反光——`:24`。
4. b2「像母亲当年搂他那样」——原文 `the way my mother used to do`，施动者是母亲，不是 35 岁的他。
5. b3「你会是她的缪斯，她的乐器」——`:130` `her muse, her instrument`，her＝「为你写音乐的女人」。
6. b4「可以教他弹琴，只要这能让他留在英格兰；但不能为一个总消失的孩子负责」——`:223`。
7. b5「练的是《哥德堡变奏曲》，也是她最喜欢的一首」——`:285`。
8. b6「三十段变奏」「烛光下」「三百年前」——`:297`。
9. 一句话总结「说学琴最重要的是爱难题、有耐性」——`:139` 附近的 Madeline 原话，与 `:223` 同场，非虚构。
10. 「中文与英文之间靠翻译机承接」——`:208` `He reaches for the translation bot on the nightstand`。
