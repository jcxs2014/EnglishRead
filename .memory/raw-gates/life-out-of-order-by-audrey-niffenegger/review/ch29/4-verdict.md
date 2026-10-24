# ch29 判定表

机器层 rc=0，6 块（block_target=[4,7]）。人判结论：**漏 11 · 编 0 · 错 1 · 提示 10**（表内 12 行，其中阻断 2 行）；**阻断 2 条**（L1 转折句、L2 信的母题）。本章的问题不是「块内讲错」，而是「只留了 6 块」——这通电话的中间五个回合（负担/后悔/老年 Alba/信/赋格）几乎全在块外。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 全章转折句整体缺失：Henry 的话被截断、他终究没说出的「I love you」，以及 Clare 对着空房间点明这一点的那句 | 原文 `:286`「“Listen, I meant to—” There’s a muffled sound, perhaps the receiver hitting the carpet?」；`:290`「“I’m listening,” I say to the empty room where Henry was, just a moment ago. But he’s gone. I love you, is what I wanted to hear, to say.」；md `/usr/bin/grep -c -F "meant to"` → `0`、`"is what I wanted to hear"` → `0`、`"I'm listening"` → `0` | 漏：本章标题事件（他打电话回家）的收束与转折全缺；没有它，「第一次互说我爱你」失去对照 | **阻断** |
| Henry 写给 Clare 的信（全书核心道具）在对话里首次被确认，整段缺失 | 原文 `:247`「“You’ve seen me old,” I say.」；`:251`「“I have,” Henry says, startled. “How did you know?”」；`:255`「“You wrote me a letter. Or, you will write a letter.”」；`:263`「“It’s one of my most treasured possessions. No pressure.”」；md `"letter"` → `0`、`"treasured"` → `0`、`"信"` → 1（「不真实」里的字，非本义） | 漏：Henry 唯一一次「被未来的自己惊到」被删，读者无从得知 Clare 手里有那封信 | **阻断** |
| Alba 会活到六十几岁——Clare 撑得住的理由 | 原文 `:237`「“Yes,” I assure him. “I’ve seen her in her sixties.” It’s ease of mind, to know that Alba will make it that far. It’s what stops me from spiraling into a panic every time she disappears for days.」；md `"六十几岁"`/`"sixties"` → `0` | 漏：人物动机的唯一解释 | 提示 |
| Alba 二十几岁写的独奏赋格（Henry：「She’s hearing ideas I can’t even formulate.」） | 原文 `:101`；md `"赋格"`/`"fugue"` → `0` | 漏：「孩子已超过我们」的具体证据只剩「聊小提琴」 | 提示 |
| Blue Teddy 与「Most Favored Toys」阵列、Richard 没打电话来慌 | 原文 `:221`「Blue Teddy is wedged between her pillow and the wall; I extract him and put him in his rightful place at the center of an assembly of Most Favored Toys at the foot of Alba’s bed.」；md `"Teddy"` → `0` | 漏：块 5 引语起点切在这句之后 | 提示 |
| Jasper：Beck 也在哀悼一个没死的人，「But it does seem less world ending since I met you.」 | 原文 `:334`；md `"Jasper"` → `0` | 漏：末场安慰成了单向 | 提示 |
| Beck 的正面提问（另一条时间线）与 Clare 的正面回答（「But here and now, I love you.」） | 原文 `:315`、`:320`；md `"另一条时间线"`/`"here and now"` → `0` | 漏：「新恋情不是背叛」唯一被正面回答处 | 提示 |
| 四人岁数（43/39/34/8），以及「Nine, in a couple of months」 | 原文 `:18`、`:196`；md `"43"`/`"39"`/`"34"`/`"九岁"` 全 `0` | 漏：与 ch24/ch26 同病 | 提示 |
| Beck 未化妆的睡容（白睡衣、和服袖绿松石浴袍、樱花丝巾，「a sleepy empress」） | 原文 `:304`；md `"浴袍"`/`"睡衣"` → `0`（导航 `:15` 只留窗外气味） | 漏：人从画里消失了 | 提示 |
| 开篇半秒错认：她以为身边是 Henry，随即想起是 Beck | 原文 `:23`「…I think it’s Henry and then I remember, Beck.」；md 无 | 漏：全章「背叛感」的种子 | 提示 |
| Richard 教琴之争（Older Albas 说他让 Alba 不想再拉琴）只在词汇表留半句 | 原文 `:88`「Older Albas have said that Richard made her a very good player but also made her not want to play.」；md 正文 `"Richard"` → 0（唯一出现是词汇表 `:88` 例句） | 漏：未来情报护住孩子兴趣的一次实操 | 提示 |
| 导航称「同一句『你在哪』问出两个年份」 | 原文 `:41`「“Where are you?”」→ 答 `:46`「“I’m at the Newberry, in my office”」（地点）；年份来自另一问 `:60`「“Um, when are you coming from?”」→ `:64`「“2006. Thursday, November 2.”」；md 导航 `:13` | 错：把两问并成一问 | 提示 |

**报数（四组）**

- 逐字：6 块 / 6 段引语全部命中（机器 `segment_miss=0`；手核 `:41`、`:68`、`:122`、`:181`、`:221`、`:351` 起止一致）→ **0 缺陷**
- 对应：6 块全部在讲自己的引语，无一跑题（`3-diff.md` 第四节）→ **0 缺陷**；问题在覆盖，不在对应
- 形态：H1 ✓、导航 5 ✓、子项 4 齐 ✓、6 块在 [4,7] ✓、块序单调 ✓、`cjk_low=0` → **0 缺陷**
- 断言：编 0；1 条表述把两问并一问 → **错 1**

## 已核实为正确（防下一轮误修）

| 看着可疑的写法 | 原文 | 核实结果 |
|---|---|---|
| 「他一个月前才失去双脚」 | `:68`「he only lost his feet a month ago, in his present」 | **正确**：指他所在时间（2006-11）的一个月前，不是 Clare 的现在。别改成「多年前」 |
| 「她删掉了 Beck 的名字」 | `:221`「This errand actually took place yesterday, but I don’t want to mention Beck.」 | **正确**：「不提」写成「删掉」是本篇的合理修辞，方向对（被删的是 Beck，不是 Henry） |
| 「时间旅行像一份只能等下班的工作」 | `:163`「Time travel feels like a terrible job now, doing something useless and waiting to clock out.」 | **正确**：原话确由 Henry 说，别改成 Clare 的感慨 |
| 「他必须在两年里过完一辈子」 | `:181`「into these last couple of years of my life」 | **正确**：原话是「我生命最后这两年」，不是「两年内死」 |
| 「三个人玩桌游」 | `:127`「all four of us spent the day…」 | **正确**：四人含 Henry，除他之外三人；别改成「四个人」 |
| 「低点是挂断后面对空房间」 | `:290`「I say to the empty room where Henry was」 | **正确**：空房间这个说法原文有 |
| 「天亮前她们把「我爱你」说出口」 | `:351`「It’s the first time we’ve said it to each other.」 | **正确**：是「第一次互相说」，不是 Clare 单方面 |
| 「stumps」译作「残肢」 | `:68`「his stumps new and painful」 | **正确**：此处指截肢后的残端（残肢），不是「树桩」；译法对，别改 |
