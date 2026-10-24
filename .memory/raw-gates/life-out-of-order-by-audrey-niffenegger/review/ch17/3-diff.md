# ch17 Haymarket — R3 对账（漏 / 编 / 错）

- 原文：`text/ch17_haymarket.txt`（196 行）
- 精读：`ch17 haymarket.md`（143 行）
- 机器层：rc=0，9 块 / 9 引语 / segment_miss 0 / 查无 0 / 空引号 0 / 字 1914
- 声部：全章 Zach 第一人称（`text/ch17:153` `Zach: A few days after…`）；两段日期 `:18` / `:151`

## 一、漏（素读有、md 无）

| # | 素读事实 | 原文（text/ch17:行） | md 侧 | 档 |
|---|---|---|---|---|
| 1 | 五人的外形被写得很具体：卡其裤、Polo 衫、有人戴棒球帽，「像去 Wrigley Field 看球走错了地方」——这是「他们变得普通」的实物证据 | `:97` `a group of five white men of various heights and builds, dressed in khakis and polo shirts, some wearing baseball caps; they look like they got lost on their way to Wrigley Field.` | 全章无「卡其」「Polo」「棒球帽」「Wrigley」；`/usr/bin/grep -cE "棒球帽|卡其|Wrigley" md` → `0`（rc=1）。导航只写「五个白人男子」，块 6 引语从 `How many years has it been…` 起，正好跳过这段外形描写 | 提示 |
| 2 | 现场警备的两个具体追问 + 五人逃走的过程：Caralora 问「楼扫过了吗」（几百扇窗都是射击位）、Gomez 答昨天已下令封锁街区；Rosa 喊「抓住他们」，Zach 追进小巷，看见黑色厢车接走那五人 | `:129` `“Did they sweep the buildings?” Caralora asks, gesturing upward. There are hundreds of windows that would give a clear vantage point, an easy shot.`；`:131` `“Yes—they were ordered to secure the block as of yesterday,” Gomez replies.`；`:133` `Rosa sees me and yells, “Get them!”`；`:133` `I look over my shoulder and see a black van pull up at the end of the alley. The men get in, the door shuts, the van drives away.` | 导航（md:11）写到「Oliver 把 Zach 按在 Joe 的 SUV 底下，叫他别动」即收，未提楼宇未清、也未提五人乘车逃走。取证：`/usr/bin/grep -nE "厢车\|窗\|楼扫" "ch17 haymarket.md"` → 无输出，rc=1（`van` 仅命中 md:79 引语里的 `vanishes`） | 提示 |

## 二、编（md 有、原文无）

| # | md 断言 | 原文 | 档 |
|---|---|---|---|
| — | 未发现凭空出现的情节、关系或数字。 | — | — |

## 三、错（两边都有但不一致）

| # | md 侧 | 原文（text/ch17:行） | 差异 | 档 |
|---|---|---|---|---|
| 1 | md:13「连**货车**原址上的雕塑也在选举后消失」 | `:65` `Until recently there was a sculpture on the spot where the wagon used by the speakers as a platform had stood—workers on a wagon that seemed to be disintegrating—but last year, after the mayoral election, it disappeared entirely.` | `wagon` 是演讲者当讲台用的**马车/板车**（干草市场现场的那辆），不是「货车」（truck）。`/usr/bin/grep -c "马车" md` → `0` | 提示 |
| 2 | md:15「最后一段悄悄换到**过去时与完成时**（has changed、has come）」 | `:161` `I have to look up the number online, it’s been so long. I wait to dial it…`；`:183` `I can’t see myself…`；`:195` `When I put the phone down, the light has changed in the bedroom and I am sitting in near-darkness.` | 最后一段是**现在时**为主（have to / wait / answers / I tell / He tells），只有 `has changed` 一处现在完成；`has come` 全书查无（`/usr/bin/grep -n "has come" text/ch17_haymarket.txt` → `0`，rc=1）。既非「过去时」，也没有 `has come` | 提示 |
| 3 | md:8（块 8 读者视角）「这里没有让 Zach 认出 Oliver 的来路……**Zach 还不知道**——这个落差在这一刻最锋利」 | `:135` `…he drops next to me, pinning my arm, hisses, “Stay still, don’t be a bloody fool,” and I suddenly realize who he is but that doesn’t make sense—` | 原文明确写 Zach **当场认出**（`suddenly realize who he is`），只是觉得「不合情理」；md 把「认不出」当成叙事效果，与引语同段的前半句相反 | 提示 |
| 4 | md:11「Charisse **小腿中弹**」 | `:156` `Charisse was wounded just below her knee, in the muscle in the back of her left calf, so she is on crutches.` | 原文只说「膝盖下方、左小腿后侧肌肉受伤」，未写「中弹」（枪伤是推断）；同段只写 Caralora 在她膝上扎止血带 | 提示 |

## 四、R4 逐块对应（人判）

9 块逐块核过「这段中文是不是在讲这句引语」＋三问（动词主语 / 受事 / 归属）：

| 块 | 引语（节） | 主语 / 受事 / 归属 | 判 |
|---|---|---|---|
| 1 | `These protections are hard-won…` `it was a rally` | Gomez 说、记者听；`hard-won` 指 protections（他们已有的保障） | 对 |
| 2 | `later pardoned, but by then they were martyrs…` `always come undone` | 被绞死者（受事）后被赦免；`you` 指听者 | 对 |
| 3 | `complete lack of any plaque or statue` | 城市（施事，隐含）；现场（受事） | 对 |
| 4 | `1927 a streetcar jumped its tracks…` | 司机说、电车撞像；`sick of seeing` 是司机的理由 | 对（md 的「民意表决」是解读，未越界） |
| 5 | `crown shyness` + 名单 | 人群（主语）；组与组留空隙 | 对 |
| 6 | `the night I met Alba` + 五人 `staring back` | 五人看他（方向未翻）；`taken away` 的施事原章未点名 | 对 |
| 7 | `angry-bee-swarm…` `Alba vanishes` | 无人机（施事）；Gomez/Alba/Zach（受事） | 对 |
| 8 | `Oliver’s determined face` `Not yet` | Charisse 抱 Gomez 的头（受事＝Gomez）；Caralora 撕自己的裙子、扎在 Charisse 膝上（受事＝Charisse） | 对（仅读者视角一句失实，见上表错 3） |
| 9 | `can’t see myself in the mirror` `the beginning of goodbye` | Zach（主语）；镜子（处所） | 对 |

结论：**无整块错位**（没有哪一块在讲引语之外的上下文），9 块的主语/受事/归属方向均与原文一致；问题集中在导航与读者视角的概括层。

## 五、词汇例句

15 条例句全部逐字命中原文（`flat()` 归一后子串比对，`miss 0 / 15`）。
