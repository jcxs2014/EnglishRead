# R5 判定表 · ch44（A Fatal Legacy / Charlotte Vassell）

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch44 matt warns callie about peter.md`
- 权威源：`.../text/ch44_44.txt`（197 行，8,947 字符）
- 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch44/`（1-suread.json / 2-machine.json / 3-diff.md / 4-correspondence.md / 4-verdict.md）
- 档位：**阻断**（与原文不符/缺失）｜**提示**（措辞正当）｜**假红**（工具判错）｜**跳过**（没查）

## 0 · 流程与机器层

| 步骤 | 结果 |
|---|---|
| R1 素读 | 只读 `text/ch44_44.txt`（未看任何 md），20 条事件/9 条关系/10 条数字已落盘 `1-suread.json`，之后才开 md ✓ |
| R2 机器层 | `bash scripts/chapter.sh "…/ch44 matt warns callie about peter.md" --json > 2-machine.json`，**退出码 0 / verdict=ok**；quotes 7/7 `ok:true`；counts：segment_miss 0、struct_bad 0、empty_quote 0、keyword_bad 0、cjk_low 0；form：h1_shape_ok=true、nav_count 5（ok）、blocks 7、block_median 7、range [5,10]、profile mystery-thriller |
| R2 独立复核 | 自写 Python 逐条 exact-match：7 条引语**全部**在原文中原样命中（位置 2126 / 2298 / 2535 / 2977 / 4789 / 6532 / 8179）；词汇表 29 条例句**全部**逐字命中原文（另有 3 条表头行误判，已排除） |
| R3/R4 | 见 `3-diff.md`、`4-correspondence.md` |

## 1 · 断言表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 章名/文件名断言「马特提醒卡莉提防彼得」 | `text/ch44_44.txt:47` `anyone being a bit stalkery with you recently?`；`:53` `They may not be following you…`（未指名）；`:56`/`:158`/`:164` 警告所指＝Eulalia；`text/ch44_44.txt:197` `I'll get Peter's lawyer on it though. He keeps him on a retainer.`；`/usr/bin/grep -c "Peter" text/ch44_44.txt` → `1`（退出码 0） | 原文全章「Peter」只出现 1 次，是卡莉**动用父亲那位律师**，与马特的警告无关；md 正文（`ch44…md:87`）自己也写明「彼得…是卡莉拿得出手的资源，**而不是被提醒的对象**」。**错的只是文件名里的 keyplot 断言**（H1 `44. Frithsden Old Hall` 无误） | **阻断** |
| 2 | 导航「一句话概括」：有人跟踪她，还对**她的委托人和凯厄斯**格外上心 | `ch44…md:11` vs `text/ch44_44.txt:56` `I've just completed a design consult for Eulalia…`、`:158` `Eulalia has been writing slightly disturbing erotic fiction` | 跟踪者**就是**她的委托人本人；被「格外上心」的对象只有凯厄斯。md 并列读法写成跟踪者对委托人上心＝跟踪者与委托人分家（施事/归属反转）。同文件 `:13`「线索结构」与 `:136`「一句话总结」写的是正确链条，`:11` 为孤例 | **阻断** |
| 3 | 导航「视角」：第三人称限知，主要贴着卡莉 | `text/ch44_44.txt:41`、`:158`、`:182`、`:194`（凯厄斯内心）、`:20`（全知口吻写 Georgie 少年史） | 体裁定性不准；「主要贴着卡莉」成立 | 提示 |
| 4 | 原句 4「这套**双生**结构」 | `text/ch44_44.txt:59` `They're sisters.` | 原文只说姐妹，未言双胞胎 | 提示 |
| 5 | 原句 1「马特**又**打来电话」 | `text/ch44_44.txt:29` `Matt was calling.`、`:38` 同一通话内寒暄、`:47` `Hi again` | 原文是唯一一通电话；「Hi again」是招呼已聊过的 Matt | 提示 |
| 6 | 原句 7「在我看挺**温情**的」（`:81`/`:85`/`:15`） | `text/ch44_44.txt:197` `Seems pretty suburban to me.`；同文件词汇表 `:114` `平淡乏味的（此处指不够刺激）` | 译法与本文件词汇表冲突，把「嫌弃/不刺激」读成「温情」 | 提示 |
| 7 | 「按**年费**养着的律师」/「常年付费」（`:81`/`:87`/`:101`） | `text/ch44_44.txt:197` `He keeps him on a retainer.` | retainer 未言「年费」 | 提示 |
| 8 | 原句 5「前一句卡莉刚说完对方因为喜欢这里的历史才搬来」 | `text/ch44_44.txt:101` `She said she moved there because she liked the history` | 原文是卡莉转述欧拉莉亚的话，md 去掉转述层级 | 提示 |
| 9 | 原句 3「她还没意识到，被卷进来的是她自己那单咨询工作」 | `text/ch44_44.txt:56` `I've just completed a design consult for Eulalia.` | 卡莉明知自己做过这单咨询；她没意识到的是「跟踪者＝客户」 | 提示 |
| 10 | 导航「场景在网球场与露台」/「在露台上接到电话」 | `text/ch44_44.txt:38` `as she walked round the side of the house and past the walled garden`、`:182` `He looked out across the grounds` | 通话横跨露台→房子侧边→围墙花园→草坪 | 提示 |
| 11 | 导航「因利益冲突被撤下」 | `text/ch44_44.txt:128` `I'm not allowed near it because of the potential conflict` | 原文＝不得靠近；撤案义由 `:131`/`:149` 卡莉的话支持 | 提示 |
| 12 | 漏：面包线（Purple Toad Bakery／砒霜酸面包假恐慌）未被分析 | `text/ch44_44.txt:89`、`:92`、`:98` | 仅存于词汇表 `bread` 一条 | 提示 |
| 13 | 漏：Amy 引歌词说漏身份 | `text/ch44_44.txt:65` | 7 块引语未取用；导航仅间接提到 | 提示 |
| 14 | 漏：宝宝与工作—生活平衡之争（含 `Do I love you? More than anything in the world.`） | `text/ch44_44.txt:143`、`:149`、`:152` | 无引语无分析；导航「人物弧线」提「生气」却未交代来源；md 未写取舍理由 | 提示 |
| 15 | 漏：开场两拍（`She's rung again` / `Turn your phone off`） | `text/ch44_44.txt:23`、`:26` | 全文无 | 提示 |
| 16 | 漏：`restraining order` 只在词汇表出现例句，无解读 | `text/ch44_44.txt:110` | 例句在 md 里，未分析 | 提示 |
| 17 | 漏：网球与 Georgie 少年往事只有导航半句 | `text/ch44_44.txt:20` | 喜剧开场，非转折 | 提示 |
| 18 | 引语逐字（7 条） | `text/ch44_44.txt:47/53/56/62/104/158/197` | 7/7 原样命中 | 通过 |
| 19 | 说话人（7 块） | `:47`(Matt,`:53` Matt continued)、`:53`、`:56`、`:62`(`Callie added`)、`:104`(`Matt asked`)、`:158`(Caius)、`:197`(Callie) | 7/7 正确 | 通过 |
| 20 | 警告对象＝Eulalia/Mel 姐妹（Mel 出声音、妹妹出面用 Eulalia 之名、娃娃头遮对口型） | `:56`、`:59` `They're sisters.`、`:62`、`:158`、`:164` | 与原文一致 | 通过 |
| 21 | 「Peter」＝彼得·辛普森（卡莉生父、垮台议员/快时尚巨头） | `text/xx_characters.txt:26`；`text/ch08_8.txt:20` `Peter, her biological father`；`text/ch35_35.txt`（23 次，父女线） | 身份认定正确；且全书从未把他与跟踪/骚扰线挂钩 | 通过 |
| 22 | 35 号 Priory Square | `:101` `Priory Square.`、`:104` `number 35` | 正确 | 通过 |
| 23 | 一周设计咨询 | `:56` `a week-long consulting gig` | 正确 | 通过 |
| 24 | 分部 SATURDAY／导航「周六在 Frithsden Old Hall」 | 文本本身无星期标注；依据分部约定：`ch42 mel is the voice and eulalia is the face.md:10`（md 标注「分部「SATURDAY」」）＋ `text/ch40_40.txt:35` `It's four in the afternoon on a Friday`（周五下午抵达）＋ `text/ch48_48.txt:114` `driven to another village nearby on Sunday`（周日离开）＋ `text/ch48_48.txt:199` `the events of Saturday` | 与全书分部一致，**不构成缺陷**（依据是全书约定而非本章原文） | 通过 |
| 25 | 词汇表 29 条例句逐字出自本章 | `text/ch44_44.txt`（逐条 exact-match 全中） | 通过 | 通过 |
| 26 | 地点 Frithsden Old Hall | `text/ch44_44.txt:17` | 正确 | 通过 |

（表内「通过」行 = 已核对成立；本表共 26 条断言：**2 阻断 / 13 提示 / 11 通过**。）

## 2 · 四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | **7/7 引语逐字命中**（100%）；另词汇表例句 **29/29** 逐字命中原文 | 自写 Python exact-match（非只信 `chapter.sh`）；`2-machine.json` 同为 7/7 |
| **对应** | **7/7 块成立**（每块「中文在讲这句引语」= 是；无引语选短、无主旨/生平错位、无密度不足）；其中 4 块带提示级瑕疵（原句 1 通话次数、原句 2 跨块推断未标注、原句 3 所指标的不清、原句 7 译法） | `4-correspondence.md` 逐块三问（主语/受事/归属） |
| **形态** | **偏离 0**（H1、导航项名与项数、子项集、块数四项全部落在本书众数/profile 内，无偏离需理由） | 见下 §3 |
| **断言** | **26 条**：**阻断 2 / 提示 13 / 通过 11** | 见上 §1 |

## 3 · 形态组（详）

| 项 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 44. Frithsden Old Hall` | 同书同场景章一形：`# 40. Frithsden Old Hall`、`# 42. Frithsden Old Hall`、`# 46. Frithsden Old Hall`；与原文 `text/ch44_44.txt:17` 的 `Frithsden Old Hall` 对应 | 无 |
| 导航项名与项数 | 5 项：`一句话概括` / `视角` / `线索结构` / `人物弧线` / `叙事手法` | 本书 54/54 章**完全同集**、同为 5 项（众数 5，`nav_count_ok=true`） | 无 |
| 子项集 | `中文理解` / `关键词` / `为什么这样写` / `读者视角提示`（4 项） | profile `mystery-thriller` 要求的 4 项全在；profile 可选项 `句子结构` 未用——本书 54/54 章同样未用 | 无 |
| 块数 | 7 | 本书 54 章分布 5:5、6:17、7:11、8:6、9:8、10:7 → 众数 6、中位数 7、范围 [5,10]；7 = 中位数，`chapter.sh` 报 `block_median 7.0`、`block_range [5,10]` | 无（7 在众数区间内） |

## 4 · 已核实为正确（防误修，任何人不得以「读着不对」改动）

1. **「彼得不是被提醒的对象，只是律师资源」**——`text/ch44_44.txt:197` `I'll get Peter's lawyer on it though. He keeps him on a retainer.`；`/usr/bin/grep -c "Peter" text/ch44_44.txt` → `1`（退出码 0）。md `:87` 的写法成立；要改的是**文件名**，不是这句话。
2. **警告对象是「不具名的跟踪狂（复数 They）」而非某个具名个人**——`text/ch44_44.txt:47`、`:53` `They may not be following you to your car or anything`；md 把 They 译作「对方」未擅自具名，成立。
3. **原句 4 中「她的姐姐」＝ Mel 那位更漂亮的姐妹**——`text/ch44_44.txt:62` `While her prettier sister is making the appearances and going by Eulalia`（her＝承前 Mel）；md 指代正确。（待改的是「双生」二字，不是这一指代。）
4. **35 号 / Priory Square**——`text/ch44_44.txt:101`、`:104`；md 数字与地名逐字一致。
5. **`suburban` 在本章语境＝平淡/不够刺激**（md 词汇表 `:114` 写法正确）——`text/ch44_44.txt:197`；待改的是 `:81`/`:85`/`:15` 三处「温情」。
6. **马特问话里的 `Personal stuff` / `asking lots of questions about Caius and your relationship`**（原句 2 中文理解）——`text/ch44_44.txt:53`；md 未把问问题的人安到卡莉/梅尔头上，成立。
7. **分部 SATURDAY**——`text/ch40_40.txt:35`（周五下午抵达）、`text/ch48_48.txt:114`（周日开车去别村）、`text/ch48_48.txt:199`（`the events of Saturday`）、`ch42 mel is the voice and eulalia is the face.md:10`（同分部标注「分部「SATURDAY」」）；`/usr/bin/grep -nE "four in the afternoon on a Friday|driven to another village nearby on Sunday|events of Saturday" text/*.txt` → 3 命中（退出码 0）。
8. **「Do I love you? More than anything in the world.」等 29 条例句均为本章原句**（无手写编造例句）——逐条 exact-match 全中。

## 5 · 覆盖声明

- 本次**只审第 44 章**（任务范围所限）。本书其余 53 章**只有机器层**（`chapter.sh`/既有门禁），**不写「通过」**。
- 第 44 章的人工判定做到 R1–R5 全程：素读（含落盘）→ 机器层 → 三张单子 → 逐块对应 → 判定表。
- **未查**：本章词汇的档位注水判断（⭐/⭐⭐/⭐⭐⭐ 分档合理性）本轮只做了例句逐字核验，未逐条评档；`docs/实测档案/` 未读（按任务要求）。
- 阻断型 **2 条**（均为 md 自身内容/命名层面，无一条要求改动英文引语；7 条引语逐字全部正确）。
