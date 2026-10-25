# ch01 · T3 判定表

- 章：Chapter 1（md：`ch01 a house and a home.md`）
- R1 素读：`1-suread.json`（独立代理，只读 `text/`，8 条，自检 OK 8/8）
- R2 机器层：`2-machine.json`（第二实现；verdict=ok，8 块整串命中、查无 0、`…` 计数 0）
- R3 对账：`3-diff.md`
- 覆盖：全章 8 块，逐块 R4 + R5；本章无「只有机器层」的部分

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 61 | a beating heart of its own / a very good dog / bready-smelling kitchen | ✓ | ✓ 讲 house 与 home 的差别本身 | ✓（三个温暖例子都在引语内） | 通过 |
| 2 | 65 | requisite number of walls and beds / not a single beating heart / ossified and blackened | ✓ | ✓ 讲「祖父无心脏、自己有」 | ✓（祖父、恐龙粪、三年级均在引语内） | 通过 |
| 3 | 58 | near downtown Savannah, Georgia / older than sliced bread / aging prima donna | ✓ | ✓ 讲地点钉死＋树的古老＋房子拟人 | ✓（无引语外人名） | 通过 |
| 4 | 47 | looks her up and down / dentures that could take off a finger / you’re gonna like it | ✓ | ✓ 讲第一次出场的三件事 | ✓（Roger 在引语内；读者提示里的第二处引语已修，见 R5） | 阻断→已修 |
| 5 | 62 | I’m old school / I’ll make myself a problem / You understand? | ✓ | ✓ 讲租约口语版＋威胁包装成怀旧 | ✓（主语全为 Roger/I，与原文一致） | 通过 |
| 6 | 62 | She needs a home of her own / a bland white and gray apartment / curious, squirming, noisy humanity | ✓ | ✓ 讲排除法式选择＋「不想被看见」 | ✓（门卫/清洁工/信箱前邻居在 `:133` 同段原文内） | 通过 |
| 7 | 63 | a riot of greenery / a mismatched army of cracked pots and bowls / yawning after a good stretch | ✓ | ✓ 讲失控的园子与容器全破 | ✓（无引语外人名） | 通过 |
| 8 | 63 | A screen of magenta flowers / almost hiding the patio below from view / a little Eden, all hidden away | ✓ | ✓ 讲「遮蔽」与伊甸园自带的下文 | ✓（无引语外人名） | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 4 读者视角提示「中间只隔了一小时」 | `text/ch01_chapter_1.txt:148` 原文 `The noise? Nah, just an hour a day, maybe.`（该「一小时」是 Saskia 每天练杠铃的时长，与两次对话的间隔无关） | 数字来源拼错、章内无时长依据 | **阻断（已修）**：改为「中间只隔着一场看房」 |
| 导航「用『我有两个女孩也想要这套房』逼她当场掏钱」 | `text/ch01_chapter_1.txt:154`：`I got two more girls who want this place. And somebody’s looking at another one of my units in fifteen, so if we’re doing this, let’s do it.` | 漏译 `more`（「还有两个」）；方向与筹码一致 | 提示（措辞） |
| 人物弧线「『不给钱就把你扔出窗户』」 | `text/ch01_chapter_1.txt:163`：`And if it bounces, I’ll throw you out the window.` | 原文条件是「支票跳票」，md 概括为「不给钱」；威吓方向一致 | 提示（条件概括） |
| 情感弧线「开头那句『有些人住过几十栋房子却从没找到家』是全章的判词」 | `text/ch01_chapter_1.txt:4`：`Some people live in dozens of houses without ever finding a home.` | 回原文核对后成立（同段第 4 句，未入引语块但属开篇同一自然段） | 假红／已核实为正确 |
| 人物弧线「『I’m Lucy』拒绝被叫 baby」 | `:28` `“Lucy baby?” says an older man…`；`:31` `“I’m Lucy,” she says, because she’s no one’s baby. Not anymore.` | 成立 | 已核实为正确 |
| 人物弧线「『I have a bicycle』拒绝被当成没车的人」 | `:124`：`“I have a bicycle.”` | 成立 | 已核实为正确 |
| 叙事手法「『Hopefully that won’t be a constant』轻轻放下」 | `:25`：`Hopefully that won’t be a constant. The ad she found online promised it would be quiet.` | 成立 | 已核实为正确 |
| 叙事手法引「Clunk-thud」／一句话总结引「clank-thud」 | `:136` `Clunk-thud. Clunk-thud.`（初听）；`:193`/`:196` `Clank-thud.`（章末兑现） | 两种拼法**都是原文**，分别对应初听与章末，非笔误 | 已核实为正确 |
| 原句 6 分析「公寓楼有门卫、清洁工、在信箱前跟她打招呼的邻居」 | `:133`：`She does not wish to be known, to have doormen and custodial staff and the same neighbors waving at the mailboxes, so many eyes, staring at her, judging her.` | 成立（同段原文逐字支持） | 已核实为正确 |
| 人物弧线引「我会给你找麻烦」 | `:97`：`if I don’t get it, I’ll make myself a problem.` | 原文为 `make myself a problem`（把自己变成问题＝给你找麻烦），md 同章原句 5 分析处又写作「给自己找点麻烦」；两处方向都落在「他来当那个麻烦」，不构成施受反转 | 提示（同一句两种译法） |

## 分组计数（只报四组）

- **逐字**：8/8 块整串命中，查无 0；受检片段 0 MISS、拼接未标省略号 0（`verify_fragments_indep.py`）
- **对应**：阻断 0（原 1 条已修），提示 1
- **形态**：阻断 0（H1 `01. Chapter 1`、导航 5 项、4 子项齐、块数 8 在本书分布内、编号连续）
- **断言**：阻断 1（已修），提示 3，假红 0，已核实为正确 5

## 已核实为正确（防误修）

1. `:4` `Some people live in dozens of houses without ever finding a home.` —— 情感弧线引的「判词」确实在开篇段。
2. `:136` 与 `:193/:196` 的 `Clunk-thud` / `Clank-thud` 并存 —— 两处 md 各引一种，均对。
3. `:28/:31` 的 `Lucy baby?` → `I’m Lucy` —— 「拒绝被叫 baby」成立。
4. `:124` `I have a bicycle.` —— 成立（注意第二章她才真去买车，本章是宣称）。
5. `:133` 的门卫/清洁工/信箱前邻居 —— 分析层用词有原文支撑。
