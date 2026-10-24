# ch68 判定表（At the Lake House）

- 覆盖：深审人判全块（4/4）+ 四件套齐全；素读 9 条（`1-suread.json`）
- 机器层：`bash scripts/chapter.sh "…/ch68 at the lake house.md" --json` → **rc=0**，块数 4，引语段 4/4 命中（63/30/44/30 词，pos 302/2187/3461/4530），查无 0，空引号 0，struct_bad 0，关键词异常 0，中文密度低 0，nav 5（5 项齐），H1 `68. At the Lake House` 形态正确，块数 4 vs 本书中位 6 / 区间 3–10（与任务表配额 ch68=4 一致）
- 报数：**逐字 0 · 对应 0 · 形态 0 · 断言 2（阻断，均低危）+ 提示 4**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 抬头日期与年龄：2054 年 6 月 19 日（周五）与 6 月 20 日（周六）；Clare 83、Beck 78 | text/ch68:18 `Friday, June 19, 2054, and Saturday, June 20, 2054 (Clare is 83, Beck is 78)` | md 全篇只写「深夜」「这一夜」，未落任何日期与年龄；与 ch67（2053 年 82 岁）接得上，不冲突 | 提示 |
| 「Beck:」「Clare:」「Beck:」三段第一人称 | text/ch68:23 `Beck:`；text/ch68:200 `Clare:`；text/ch68:205 `Beck:` | 三处署名位置、顺序、段数全对；md 第 15 行「三个署名切出三段第一人称，时间只有一夜」成立 | 已核实为正确 |
| 叙述者 Beck 的性别：全篇作「他」，并把两人写成「一对老夫妻」 | 本章第一人称无性别词；全书证据 text/ch04:65 `Beck is Alba’s stepmother`；text/ch11:113 `I feel a certain kinship with her: We both arrived late and married into the DeTamble family`；text/ch01:2099 `Beck is there. She closes the door behind me`；text/ch69:118 `I turn to Beck and she is young again` | **性别反了**：Beck 是 Clare 的妻子、Alba 的继母。md 命中：第 13 行 `一对老夫妻`、第 21/25/27/31/37/51/55/57/91 行共十余处「他」 | **阻断** |
| 「划到湖心」 | text/ch68:33 `we are close enough to shore that I can hear the water lapping around our pier`（另 text/ch68:23 `I can see Clare in the middle of the boat`＝船中间，非湖心） | **位置反了**：原文离岸很近、听得见水拍栈桥；md 第 11/13/91 行三处写「湖心」，第 91 行后半又写「划回岸边」自相矛盾。修法：改「湖上／近岸」 | **阻断** |
| 「他说她若信那套说法就能读掌纹」（块 1） vs 导航「起先能读掌纹」 | text/ch68:23 `I could read my palms in the moonlight if I knew or believed any of that nonsense.` | 块 1 中文理解忠实（`if`＝假设），导航第 14 行「起先能读掌纹」把假设写成能力，前后不一致 | 提示 |
| 「另一段人生」「另一段爱情」 | text/ch68:67-71 `“But you had another life . . .”` / `“And another love. But I love you, Beck.”` | 归属对：是 Beck 问 Clare（她的前一段人生＝Henry），md 第 11 行「她另一段人生和另一段爱情」未把「另一段」误挂到 Beck 身上 | 已核实为正确 |
| 「二十二个夏天」 | text/ch68:51 `“Twenty-two summers.”` | 数字对（md 第 11/91 行作「二十二年」），且是 Beck 回答 Clare 的「我们在这里住了很久」 | 对应 |
| 「你会进所有历史书」与「已经没有历史书了」的说话人 | text/ch68:120 `Clare says, “I always thought you were the one who would be in the museums. But, you’ll be in all the history books.”`；text/ch68:124 `“Clare, there aren’t any history books anymore.”` | 未对调：前者是 Clare 夸 Beck，后者是 Beck 自嘲；md 第 13 行反向引用「反转『艺术不朽』：她的画与雕塑有实体，他的工作却像蒸发」也未张冠李戴 | 已核实为正确 |
| 未来消息的来源链：Clare ← Alba | text/ch68:144 `She hesitates. “Alba.”`；text/ch68:148 `“And she went way into the future to check up on history?”` | md 第 47 行「她没有解释阿尔芭怎么知道，只报了名字」成立；消息不是 Clare 亲历，也不是 Beck 梦见 | 已核实为正确 |
| 死亡呈现：脸颊微凉、心跳已停，无「消失」 | text/ch68:205 `I put my hand on her cheek; she is only slightly cool. I listen for her heartbeat, but her heart is still.` | md 第 11/51 行只写温度与心跳，未写成时间旅行失踪、未写「她消失了」，属自然死亡 | 已核实为正确 |
| 「彼此的白发」 | text/ch68:23 `enveloped by her shining white hair; I can see my own hands’ deep creases` | 白发只属 Clare；Beck 本章无外貌，md 第 11 行并成「彼此的白发」属轻添加 | 提示 |
| 导航称「没有一句争吵」，但原文有质问回合 | text/ch68:172-176 `“But this is terrible! Why didn’t you tell me?”` / `“You didn’t want to know.”` | 这一问一答 md 未收，「没有一句争吵」因此偏软（Beck 实际是在质问） | 提示 |
| 零命中类断言（「湖心」） | `/usr/bin/grep -nE "湖心" "ch68 at the lake house.md"` → 命中 3 行（11 / 13 / 91），**退出码 0**；`/usr/bin/grep -nE "close enough to shore" text/ch68_at_the_lake_house.txt` → 命中 `33:`，**退出码 0** | 见「湖心」行 | — |

## R4 逐块对应（三问）

| 块 | 这段中文是不是在讲这句引语？ | ①动词主语 | ②受事 | ③归属方向 |
|---|---|---|---|---|
| 1（原句1，pos 302） | 是（`Everything casts deep shadows` 到 `I don’t need any hints`） | 景物（影子／湖面）；看的人是 Beck | 白发、手纹、掌纹 | `her shining white hair`＝Clare 的，`my own hands’ deep creases`＝Beck 自己的；md 第 21 行未颠倒 |
| 2（原句2，pos 2187） | 是（`When I watch you drawing` 到 `presence in the world`） | Beck（wish）；Clare（have stacks / sculptures） | Clare 的画与雕塑 | `Your art`＝Clare 的艺术，md「他把她的作品一件件数出来」「她的艺术在世上是有分量的存在」方向对；不得改成 Beck 自己有作品 |
| 3（原句3，pos 3461） | 是（整段转述） | Clare 说、Alba 是消息源；`everything tears itself apart` 的主语是 everything | 未来、艺术 | md 第 41/45 行未把「art will be there」写成幸存，而按原文写成「等世界重新准备好就回来」，条件方向对 |
| 4（原句4，pos 4530） | 是（`Clare is asleep—but no` 到 `her heart is still`） | Clare（is asleep / is silent / is cool）；Beck（put my hand / listen） | Clare 的脸、心跳 | `she is only slightly cool`＝Clare 微凉，`her heart is still`＝她的心停了；md 第 51 行方向对，不得改成「他冷／他的心停了」 |

## 已核实为正确（防下一轮误修）

1. **三段署名的边界** —— text/ch68:23 `Beck:`、text/ch68:200 `Clare:`、text/ch68:205 `Beck:`。中间 Clare 那段只有一段（第 200 行），**不要**把它扩成整节，**不要**把最后一段（第 205 行）并回 Clare 段。
2. **死法是自然死亡** —— 全章只有体温（`slightly cool`）与心跳（`heart is still`）两个证据，没有消失、没有时间旅行、没有「他赶到时她已不见」。修任何东西都不得引入「她在时间里消失」的读法。
3. **「你会进所有历史书」是 Clare 说的，「已经没有历史书了」是 Beck 说的** —— text/ch68:120 / 124，勿对调。
4. **「另一段爱」指 Clare 的前夫 Henry，不是 Beck 的前夫 Jasper** —— 问句 `But you had another life . . .` 的主语是 Clare（text/ch68:67）；md 第 11 行「她另一段人生」代词正确，改性别时不要连这句一起改错。
5. **「二十二个夏天」是 Beck 的回答** —— text/ch68:39 Clare 说 `We’ve been here a long time`（指住得久，不是要回屋），text/ch68:51 Beck 答 `Twenty-two summers.`；Clare 在 text/ch68:47 特意纠正过「我是说住了很久」。
6. **未来的消息不是 Clare 亲历** —— text/ch68:144-148 明确来源是 `Alba`，且 Beck 追问「她去到很远的未来查历史了？」Clare 不答（text/ch68:152）。md 第 47 行「她没有解释阿尔芭怎么知道，只报了名字」精确，**不得**改成「克莱尔从未来回来」。
7. **词汇例句 13 条全部逐字可查** —— doubled-up（text:79）、illuminates（text:164）、sculptures（text:105）、vaporized（text:96）、precision（text:23）、sorrowful（text:101）、invisible（text:110）、collapses（text:160）、presence（text:105）、pier（text:33）、pines（text:23）、cheek（text:205）、future（text:23），无一改写。
8. **引语 2 末尾的 `world.”"`** —— 第 29 行末多一个卷引号（od 验：`w o r l d . ” "`），机器仍判 rc=0；这是排版瑕疵，修时只删那个 `”`，**不要**动 `world.` 与前置的 `”`（原文 `Your art has a presence in the world.”` 本身带 Clare 引号）。
