# ch12 The Yellow House · R3 对账（素读 vs md）

- 素读：`review/ch12/1-suread.json`（只读 `text/ch12_the_yellow_house.txt` 时写定，13 条候选，正文取 8 条 + 转折点一句）
- 机器层：`review/ch12/2-machine.json`，`chapter.sh` rc=0，10 块 / 10 引语 / 查无 0 / 空引号 0 / 子项缺 0 / 关键词 0 / 块数 10（本书中位 6、上限 10，触及上限但未越界）
- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch12 the yellow house.md`（149 行）

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文（text/ch12:181-195） | md 侧 | 判 |
|---|---|---|---|---|
| 1 | 最后一间卧室：提琴太大、走音但是好琴；衣柜门关着、门把上方一把大挂锁；Alba 说「那里面关着所有怪物」 | 181 `We found a violin in the last bedroom.` / 185 `“It’s too big,” I said.` / 190 `A large, ominous-looking padlock had been installed above the doorknob.` / 195 `“That’s where they keep all the monsters,” I said.` | 全文只出现「壁橱里是 where they keep all the monsters」（第 14 行人物弧线），提琴、走音、挂锁均无对应块，也无导航句 | **提示**（覆盖缺口）。理由：这一段是看房途中一个房间的过场，不是本章转折；本章转折（房主身份、temporal landmarks、Other Teddy、手套）都已进块与导航，10 块配额已满，取舍可理解。但提琴是全书后文 Alba 学琴的伏笔物件，建议下一轮补一句。 |

结论：无阻断型漏。

## 二、编（md 有、原文无）

| # | md 侧 | 原文侧 | 判 |
|---|---|---|---|
| 1 | 第 11 行导航：「却看中了一只像 Blue Teddy 兄弟的熊，**取名** Other Teddy」 | 176 `The bear’s name was Other Teddy.`（原文只给名字，未写谁取的名；158-176 段里 Alba 只说「Can I take him home?」，Mama 说「Leave him here」） | **提示**（归属推断）。「取名」把未写明的主语补成 Alba；改成「那只熊叫 Other Teddy」即与原文同强度。 |
| 2 | 第 13 行 Tropes：「后院攒着空酒瓶和麦片盒」 | 72 `There was a small back porch full of empty liquor bottles and cereal boxes waiting to be recycled.` | **提示**（地点）。是后廊（back porch）不是后院；同一句里「门窗不锁」也比原文宽（原文只说 `why the back door was never locked`，37 行）。 |

结论：无阻断型编造（无凭空情节/关系/数字）。

## 三、错（两边都有但不一致）

| # | md 侧 | 原文侧 | 判 |
|---|---|---|---|
| 1 | 第 14 行人物弧线：「这一天她做的事几乎都是「不」——不吃蛋糕、不把熊带走、**不肯读便条**、不肯留下手套」 | 238-241 `“Can I read it?” I asked.` / `“Later,” she said.` | **阻断**。原文是 Alba 主动要求读便条、母亲说「以后」；md 把「想看而没读成」写成「不肯读」，意愿方向颠倒，且被用来支撑「做的事几乎都是不」这一判断。 |
| 2 | 第 45 行：「末句短得只有**四个词**」 | 39 `The cake said, Welcome, Alba!` → The / cake / said / Welcome / Alba = 5 words | **提示**（计数）。不影响理解，但属可核数字断言。 |
| 3 | 第 14 行：「不肯留下手套」（同句列出，与同章第 12 行「她开始留下东西」自相矛盾） | 255-263 `I suddenly loved them—I didn’t want to leave them there.` … `I pulled off the mittens and carefully arranged them by her note` | **提示**。原文是「舍不得但还是留下了」；「不肯留」与同章情感弧线的说法打架。 |

结论：1 条阻断（#1），2 条提示。

## 四、逐块对应（R4 结论）

10 块全部「中文讲的就是这句引语」，无一块跑去讲全书主旨或作者生平：

- 原句 1（safe house 三连定义）→ 中文逐句拆否定，`depend on` 的温度落在「可靠」而非「眷恋」，与引语同层。
- 原句 2（房子是日历）→ 中文复述 presence/absence 与两个阈值年份（1987/1958），未越界。
- 原句 3（厨房与蛋糕）→ 中文把「白红 + 铬 + 歪扭红字」逐项落地；`shaky` 的解释（越抖越像连夜赶出来）与原句 5 的括注互为印证。
- 原句 4（童话禁令）→ 中文点明 she never says「糖果屋」，与原文一致。
- 原句 5（括号里的烤蛋糕夜）→ 中文点明「括号是时间机器」，并把 `both still there` 读成「能不能留下她自己也没把握」，贴原文。
- 原句 6（Other Teddy 是门）→ 中文把落点（衣柜前地毯）与紫色衣裙柜接上；核对 158 行确为同一柜，成立。
- 原句 7（留下手套）→ 中文解释 `Leave something here` 与「押金/标记」，未把受事方向弄反（Alba 给、Mama 收）。
- 原句 8（后窗望远镜）→ 中文抓 `spyglass` 的单筒义与「没有一句告别」，与引语一致。
- 原句 9（购物车）→ 中文明确 Oliver 帮 Mama、Mama 道谢走人，方向正确；`disengage` 的「拆机械」义成立。
- 原句 10（会见家人 / Beck）→ 中文把 `do meet` 的强调、`I’ve never met your dad` 的完成时封口讲清；「Reasons.」两字解释对应 346 行。
