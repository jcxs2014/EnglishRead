# ch29 对账（Henry Calls Home）

原文：`text/ch29_henry_calls_home.txt`（352 行，Clare 第一人称，凌晨一通电话）
md：`ch29 henry calls home.md`（111 行，6 块，block_target=[4,7]）
机器层：rc=0，6 块，6/6 命中，words=2258

## 一、漏（素读有、md 无）

| 编号 | 素读要点 | 原文（逐字） | md 侧取证 | 判定 |
|---|---|---|---|---|
| L1 | **转折点**：Henry 说「Listen, I meant to—」被一声闷响截断（话没说完），Clare 对着空房间说「I'm listening」，并点明「I love you, is what I wanted to hear, to say.」——他终究没说出口，这才轮到 Beck 说 | `:286`「“Yeah,” he replies. “Listen, I meant to—” There’s a muffled sound, perhaps the receiver hitting the carpet?」`:290`「“I’m listening,” I say to the empty room where Henry was, just a moment ago. But he’s gone. I love you, is what I wanted to hear, to say.」 | `/usr/bin/grep -c -F "meant to"` → `0`；`"I love you, is what"` → `0`；`"I'm listening"` → `0`。导航 `:12` 只写「低点是挂断后面对空房间」，总结 `:111` 只写「天亮前她们把「我爱你」说出口」 | **漏（阻断）**：本章标题事件（他打电话回家）的收束句与全章转折全部缺失；没有这句，「第一次互说我爱你」就少了一半重量 |
| L2 | 信的母题：Clare 说「你见过我老去」，Henry 一惊问「How did you know?」，她答「You wrote me a letter. Or, you will write a letter.」——「It's one of my most treasured possessions. No pressure.」 | `:247`「“You’ve seen me old,” I say.」`:251`「“I have,” Henry says, startled. “How did you know?”」`:255`「“You wrote me a letter. Or, you will write a letter.”」`:263`「“It’s one of my most treasured possessions. No pressure.”」 | `"letter"` → `0`；`"信"` → 1（且是「不真实」里的字，非本义）；`"treasured"` → `0` | **漏（阻断）**：Henry 写给 Clare 的信是全书核心道具，而这里是它第一次在对话里被确认、且是 Henry 唯一一次「被未来的自己惊到」；md 三个层面（块/导航/总结）零覆盖 |
| L3 | Alba 会活到六十几岁：Clare 说「I've seen her in her sixties」，并说这份安心是她每次女儿消失几天都不至崩溃的原因 | `:237`「“Yes,” I assure him. “I’ve seen her in her sixties.” It’s ease of mind, to know that Alba will make it that far. It’s what stops me from spiraling into a panic every time she disappears for days.」 | `"六十几岁"` → `0`；`"sixties"` → `0` | 漏（提示）：Clare 这个人物「为什么不慌」的唯一解释 |
| L4 | Alba 写的独奏赋格：二十几岁、长期独处时写成；Henry 说「She's hearing ideas I can't even formulate.」 | `:101`「“Yeah. It was a fugue for solo violin. It sounded amazing and looked sort of—strenuous. …She said she was spending a lot of time alone”」 | `"赋格"` → `0`；`"fugue"` → `0` | 漏（提示）：「孩子已远超过我们」的具体证据，只剩「聊小提琴」四个字 |
| L5 | Blue Teddy：卡在枕头与墙之间，Clare 把它抽出来放回床尾「Most Favored Toys」阵列正中，并说「Richard hasn't called in a panic. That's a first.」 | `:221`「Blue Teddy is wedged between her pillow and the wall; I extract him and put him in his rightful place at the center of an assembly of Most Favored Toys at the foot of Alba's bed.」 | `"Teddy"` → `0` | 漏（提示）：块 5 的引语从这句之后才开始，动作被切掉 |
| L6 | Jasper：Beck 说自己一直在哀悼没死的 Jasper，久不想他他就打来电话——「But it does seem less world ending since I met you.」 | `:334`「“That’s sort of how it is with Jasper. Though he’s not dead, I’ve been grieving him, and then, when I haven’t thought about him in a while, he calls. But it does seem less world ending since I met you.”」 | `"Jasper"` → `0` | 漏（提示）：末场唯一的「双向」——不只 Clare 在哀悼，Beck 也在；缺它则安慰成了单向 |
| L7 | Beck 的正面提问：会不会有另一条时间线，Henry 没死、我们没遇见或只是朋友？Clare 答「If that time exists, we don't know or care what we missed. But here and now, I love you.」 | `:315`「“Do you think there’s an alternate timeline where Henry didn’t die? And we never met, or we met and we were just friends?”」`:320`「“If that time exists, we don’t know or care what we missed. But here and now, I love you.”」 | `"另一条时间线"` → `0`；`"here and now"` → `0` | 漏（提示）：「新恋情不是背叛」这个主题唯一被正面回答的地方 |
| L8 | 年龄与年级：标题行四人岁数；Henry 问「How old is she, for you? Eight?」她答「Yeah. Nine, in a couple of months.」 | `:18`「Sunday, July 18, 2010 (Henry is 43, Clare is 39, Beck is 34, Alba is 8)」；`:196`「“Yeah. Nine, in a couple of months.”」 | `"43"`/`"39"`/`"34"` 均 `0`；`"九岁"` → `0` | 漏（提示）：同批 ch24/ch26 亦缺岁数；「快九岁」是父女对话里唯一的时间刻度 |
| L9 | Beck 没化妆的样子：白睡衣、和服袖绿松石浴袍、樱花纹丝巾包发，「She looks like a sleepy empress.」 | `:304`「She’s wearing white pajamas, a turquoise blue bathrobe with kimono sleeves and a silk scarf with a cherry blossom pattern wrapping her hair. She looks like a sleepy empress.」 | `"浴袍"` → `0`；`"睡衣"` → `0` | 漏（提示）：导航 `:15` 只留「绣球花与垃圾的气味」，人不在了 |
| L10 | 开篇一瞬：她以为身边睡着的是 Henry，随即想起是 Beck | `:23`「There’s someone sleeping next to me and I think it’s Henry and then I remember, Beck.」 | `"以为是 Henry"` → `0`（总结仅「身边睡着 Beck」） | 漏（提示）：全章「背叛感」的种子，就在这半秒的错认里 |
| L11 | 小提琴老师之争：Henry 怀疑当初该不该让父亲教；Clare 说另有良师缓冲吼叫，但「You can't mention this to your dad」——Older Albas 说 Richard 把 Alba 教成好琴手，却也让她不想再拉琴 | `:88`「Older Albas have said that Richard made her a very good player but also made her not want to play. So, not a perfect success.」；`:93`「“No. I want her to love music.”」 | 正文 `"Richard"` → 0（唯一出现是词汇表 `:88` 的例句行）；`"拉琴"` → `0` | 漏（提示）：「未来情报」被用来护住孩子兴趣的一次实操，只在词汇表里留下半句 |

## 二、编（md 有、原文无）

**0 条。** 逐条核过：导航「她删掉一个名字」＝`:221`「I don't want to mention Beck」；「他说自己成了负担」＝`:146`；「她愿意拿几乎一切换他回来」＝`:150`；「时间旅行像一份只能等下班的工作」＝`:163`「doing something useless and waiting to clock out」；「三个人的桌游」＝`:127`「all four of us」减去 Henry。均无凭空情节。

## 三、错（两边都有、但不一致）

| 编号 | 断言 | 原文（逐字） | md 侧 | 判定 |
|---|---|---|---|---|
| E1 | 导航称「兑现『跨越时间的爱人』：同一句『你在哪』问出两个年份」 | `:41`「“Where are you?”」→ Henry 答 `:46`「“I’m at the Newberry, in my office”」（**地点**）；年份是另一问 `:60`「“Um, when are you coming from?”」→ `:64`「“2006. Thursday, November 2.”」 | 导航 `:13` | 错（提示）：把两问并成一问；「你在哪」问出来的是 Newberry，不是 2006 |

## 四、逐块对应（R4）

| 块 | 引语起（原文行） | 中文是不是在讲这句？ | 主语 / 受事 / 归属 |
|---|---|---|---|
| 1 | `:41` 出门带门、Beck 似乎还睡着 | 是。中文点出「不合常理：铃那么响却没醒」，这正是原文 `:41` 的叙述意图 | 主语 Clare ✓；「睡着的人」＝Beck ✓ |
| 2 | `:68` 听出难过、想象他光身坐在别人的办公室 | 是。「在他自己的时间里，一个月前才失去双脚」把 `in his present` 译准了 | 主语 Clare（想象）✓；受事 Henry 的身体 ✓ |
| 3 | `:122` 对他毫无间隔、对她一年多 | 是。中文「两个时钟」＝原文分号结构 | 主语「我」✓；`for him` / `for me` 方向对 ✓ |
| 4 | `:181` need each other / cramming | 是。「他必须在两年里过完一辈子」＝`these last couple of years of my life` ✓ | 说话人 Henry ✓；受事「一辈子的父女相处」✓ |
| 5 | `:221` 谎称昨天是明天、怕被听见 | 是。「两扇门加一条短走廊」＝`Two doors and a short hallway` ✓ | 主语 Clare ✓；被隐瞒者 Henry、被提防者 Beck，两者未混 ✓ |
| 6 | `:351` 早上、杯子、两把椅子 | 是。「两个声音并排放着」= Henry 的 `it all balances` + Beck 的 `I love you, too` ✓ | 归属清楚：前句 Henry、后句 Beck ✓。**但引语起点切在 `Henry seems far away`，「In the morning」被切掉**（中文理解补了「到了早上」，不构成错） |

**R4 结论**：6 块对引语全部忠实，无一块讲引语之外上下文；块 3/4 密度最好。真正的问题是「块选得太少」——6 块只覆盖了这通电话的头尾与两句自述，中间的负担/后悔/信/赋格/老年 Alba 五个回合全部落在块外。

## 五、形态

H1 `29. Henry Calls Home` ✓；导航 5 项 ✓；子项 4 齐 ✓；6 块在 [4,7] 内 ✓；块序单调（`:19→:29→:39→:49→:59→:69`）✓；`cjk_low=0`、`keyword_bad=0`、`struct_bad=0`。
