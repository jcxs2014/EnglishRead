# ch17 Haymarket — R5 判定表

- 原文 `text/ch17_haymarket.txt`（196 行）／精读 `ch17 haymarket.md`（143 行）
- 机器层 `2-machine.json`：rc=0，verdict ok，9 块 / 9 引语 / segment_miss 0 / 查无 0 / 空引号 0 / 结构坏 0 / 关键词坏 0 / 字 1914 / block_target [3,6]
- 声部核对：全章 Zach 第一人称（`text/ch17:153` `Zach:`），**未**把 Oliver/Alba 的话错记到 Zach 名下；两段日期 `:18` / `:151` 的年龄（Alba 34 / Zach 35 / Oliver 31）与 md:11 一致。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| md:11 五人「被**白衣人**抬走」是错的、属编造 | `text/ch01_the_last_party.txt:1936` `White-clad figures appear—I can’t tell where they’ve come from—they are wearing hoodies and masks… wrapping prone figures in white sheets, lifting them and carrying them out of the room. Five bodies.`；`:1964` `“Streets and San are here to take them,” Max whispers. “They’re in the alley, in white vans.”` | 跨章有据，写法成立（假红） | 假红 |
| md:11「Charisse 小腿**中弹**」 | `text/ch17:156` `Charisse was wounded just below her knee, in the muscle in the back of her left calf, so she is on crutches.` | 原文只写「受伤」，未写枪伤；md 把推断写成事实 | 提示 |
| md:13「连**货车**原址上的雕塑」 | `text/ch17:65` `a sculpture on the spot where the wagon used by the speakers as a platform had stood—workers on a wagon that seemed to be disintegrating—but last year, after the mayoral election, it disappeared entirely.` | `wagon` 是演讲者当讲台的马车/板车，不是货车；`/usr/bin/grep -c "马车" md` → `0`（rc=1） | 提示 |
| md:15「最后一段悄悄换到**过去时与完成时**（has changed、has come）」 | `text/ch17:161` `I have to look up the number online…I wait to dial it…`；`:183` `He answers and I nearly hang up…I can’t see myself…`；`:195` `When I put the phone down, the light has changed in the bedroom and I am sitting in near-darkness.`；`/usr/bin/grep -n "has come" text/ch17_haymarket.txt` → 无输出 rc=1 | 末段是现在时为主，只有 `has changed` 一处现在完成；「过去时」与 `has come` 均不成立 | 提示 |
| md:97（块 8 读者视角）「Zach **还不知道**……这个落差在这一刻最锋利」 | `text/ch17:135` `…pinning my arm, hisses, “Stay still, don’t be a bloody fool,” and I suddenly realize who he is but that doesn’t make sense—` | 原文写 Zach 当场认出 Oliver，只是觉得不合情理；md 的「还不知道」与引语同段前句相反 | 提示 |
| md 全章缺「五人外形」：卡其裤/Polo 衫/棒球帽/Wrigley Field 玩笑 | `text/ch17:97` `five white men…dressed in khakis and polo shirts, some wearing baseball caps; they look like they got lost on their way to Wrigley Field.`；`/usr/bin/grep -nE "卡其\|Polo\|棒球帽\|Wrigley" "ch17 haymarket.md"` → 无输出 rc=1 | 关键识别人物的外形细节未进导航、也未进任何引语块 | 提示（漏） |
| md 全章缺「楼宇未清 + 五人乘车逃走」 | `text/ch17:129` `“Did they sweep the buildings?” Caralora asks…There are hundreds of windows that would give a clear vantage point, an easy shot.`；`:133` `Rosa sees me and yells, “Get them!”`；`:133` `see a black van pull up at the end of the alley. The men get in, the door shuts, the van drives away.`；`/usr/bin/grep -nE "厢车\|窗\|楼扫" "ch17 haymarket.md"` → 无输出 rc=1 | 袭击前的警备漏洞与五人逃走的结果都缺；导航在「按在车底」处收束 | 提示（漏） |
| md:14「他讲到美国为什么从不愈合**就被打断**」 | `text/ch17:56` `That’s why America never heals . . .” Gomez looks exhausted; he told me this morning that he and Charisse were at the hospital with Max most of the night.`；另核集会进程：`:76-90` 他们还在卸车、争论要不要撤，`:110` 之后即遇袭，Gomez 在集会上未开讲 | 省略号是「话没说完＋他疲惫」，与「被打断」方向一致（话未说完），只是措辞更狠；且这句确实出自采访而非集会演讲，md:14 未把它写成集会发言 | 假红 |
| md:11「Zach 抬头看见街对面站着五个白人男子」 | `text/ch17:97` `He’s pointing across the street…Griffin hands me a pair of fancy binoculars…I adjust the binoculars and peer at the men.` | 是 Griffin 指给他、借望远镜看的；md「抬头看见」省略了中介，但 sighting 成立 | 假红 |
| md:11 三个年龄（Alba 34 / Zach 35 / Oliver 31）与日期 | `text/ch17:18` `Sunday, May 4, 2036 (Alba is 34, Zach is 35, Oliver is 31)` | 逐字一致 | 通过 |
| 9 块引语逐字 | `2-machine.json` `segment_miss 0`；另抽 9 块首尾句与 `text/ch17` 原段逐字比对 | 全部命中 | 通过 |

## 报数（四组）

- **逐字**：0 问题（9/9 块引语命中原文；15/15 词汇例句 `flat()` 比对 `miss 0`）
- **对应**：0 阻断（9 块逐块核「中文是否在讲这句引语」＋主语/受事/归属三问，全部对上；无整块跑题）
- **形态**：1 提示（md:15 时态概括失实：现在时被说成过去时，并引出原文没有的 `has come`）
- **断言**：5 提示（漏 2：五人外形、楼宇未清＋乘车逃走；错 3：货车/wagon、Zach「还不知道」、Charisse「中弹」未核）

**阻断 0 / 提示 6 / 假红 2 / 跳过 0**；回执：`ch17 rc=0 块数9 漏2 编0 错4 提示6`

## 已核实为正确（防下一轮误修）

1. `text/ch17:18`／`:151` 两个日期与三家年龄（Alba 34 / Zach 35 / Oliver 31）是原书抬头，**勿改**；同一年龄在不同章不同（ch15 是 Oliver 27 / Alba 30 / Zach 30），不要跨章统一。
2. 「白衣人抬走五人」有 ch01 原文支撑：`text/ch01_the_last_party.txt:1936` `White-clad figures…wrapping prone figures in white sheets…Five bodies.` ＋ `:1964` `in white vans`。md:11 写法正确。
3. 五人名单逐字：`text/ch17:102` `Junior Olson, Buddy Franz, Arthur Memling, Richard Alden and Terry Fell.`，md:11「Junior Olson 一伙」与块 6 引语均对。
4. `crown shyness` 译「树冠羞避」正确（植物学固定译名）；`text/ch17:92` `like trees with crown shyness`。
5. `inner compass is broken` 译「内心的罗盘坏了」（md:14）——原文 `:156` 逐字。
6. `text/ch17:195` 末句 `the beginning of goodbye` 与 md:11「那是告别的开始」对应正确。
7. `That’s why America never heals`（`:56`）确实出自 **Gomez 的采访**，md:13 的归属（采访而非集会演讲）正确——集会尚未开始即遇袭。
