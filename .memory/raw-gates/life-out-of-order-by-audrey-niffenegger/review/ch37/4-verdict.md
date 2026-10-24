# ch37 coffee and pancakes with ghosts — 判定表（R5）

- 原文 295 行 / 精读 131 行；机器层 `2-machine.json` **rc=0**（verdict=ok，8 块 / 8 段全逐字，counts 全零，words 2605）
- 报数四组：**逐字 8/8 通 · 对应 8/8 通 · 形态 通（H1 `37. Coffee and Pancakes with Ghosts`／导航 5 条／子项四件齐／块数 8 = block_target 上限）· 断言 漏 7（阻断 1·提示 5·跳过 1）· 编 1 提示 · 错 4 提示**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| **L2** 父母这场早餐的落点（「几时能再见到你」／「一直都可以，何必克制」／马维尔诗句互答）整段未进 md | `text/ch37_coffee_and_pancakes_with_ghosts.txt:273` ““So,” Dad says, “when can I see you again?””；`:277` “My mother says, “All the time. Why hold back? ‘Let us roll all our strength and all / Our sweetness up into one ball, / And tear our pleasures with rough strife / Through the iron gates of life.’””；`:282` “And my father replies, “‘Thus, though we cannot make our sun / Stand still, yet we will make him run.’” My face is hot; I shouldn’t have overheard that.”；取证：`grep -nE "All the time|Marvell|马维尔|诗|ball|iron gates" "ch37 coffee and pancakes with ghosts.md"` → 无输出 rc=1 | 她专程来看的那场戏**缺了落点**：关系起点（All the time）与「时间」主题的第一次正面出场都在这里；md 未写取舍理由 | **阻断** |
| **L1** 调情高峰（「你绝对是女神」／狄俄尼索斯／雅典娜＋阿佛洛狄忒／「人们总想把我变成缪斯」）未进 md | `:180` ““You are definitely a goddess,” Dad says… this is what we’ve come for: the flirting.”；`:185` ““More likely Dionysus, I’m afraid. You’re a combination of Athena and Aphrodite.””；`:190` ““People keep trying to make me into a muse,” Mama says. “I’m not interested in that one bit.””`；取证 `grep -nE "缪斯|女神|雅典娜|阿佛洛狄忒|狄俄尼索斯"` 于 md → 无输出 rc=1 | 原文自注「三个小孩 all ears 等的就是这段」；md 只剩艺术观对谈 | 提示 |
| **L4** 三个小的盘问的四十九／已婚／「同一个人怎么可能遇见三次」／渡鸦，全无 | `:114` ““Forty-nine.””；`:122` “I almost never lie to my younger self; it would only wreak havoc.”；`:140` ““How could you meet the same guy three times?””；`:162` ““‘Why is a raven like a writing desk?’”” | md 仅「被追问得招架不住」一句概括 | 提示 |
| **L5** 多莉羊的时代错位（1991 年多莉还要五年才出生，父亲失言改口） | `:226` ““Like Dolly the Sheep?” my dad says.”；`:230` “This is lucky, because we’re in 1991 and Dolly won’t be born for another five years.”；`:235` “Dad realizes his mistake. “Someone I read about.”” | 总结只留结尾「讲讲克隆羊多莉」，失言这层暗号丢了 | 提示 |
| **L3** 驳回咖啡改橙汁＋女侍「Next they'll be wanting to smoke」 | `:37-41` ““We want coffee, too,” says an Alba. / “Nope, orange juice for you,” I say. The waitress says, “Next they’ll be wanting to smoke,”” | 未收；点单段只剩词汇表 `bacon` 一条 | 提示 |
| **L6/L7** 多给小费以补偿逃单、「餐馆让我焦虑」；父母各自点的早餐 | `:258` “I always overtip when I can, to make up for all the times I’ve had to run out on a check.”；`:61` “two eggs sunny-side up with toast for my mother, pancakes and bacon for my dad” | 自述与生活细节，不承载事件 | 跳过 |
| **F1** Tropes 写「四个自己……分煎饼、借鞋子、**抢一根吸管**」 | `:166` “I filch a forkful of pancake from the missing Alba’s plate.”；`:68` “One Alba notices me noticing this one, so I **hand it back to her**.”；`:61-62` 借鞋成立 | 「借鞋子」准确；「抢」与原文「递回」方向相反，「分煎饼」也与「偷一叉」不符 | 提示 |
| **E1** 块 2 中文理解「三个年幼的阿尔芭**睡饱了**，咯咯直笑」 | `:28` “My twelve-year-old selves are **wide-awake** and giggly.” | wide-awake＝清醒，与「父母都不是早起的人」成对照；「睡饱了」凭空添了睡眠信息 | 提示 |
| **E2** 块 5 读者视角「替乔什**和他的朋友**编一段来历」 | `:73` “we’d invent a history for Josh and **his angry lover and friend**” | 原文三人（Josh／生气的情人／朋友），md 把情人并进「朋友」 | 提示 |
| **E3** 块 7 读者视角「我是神／我是白痴」 | `:176` “I veer back and forth between ‘**I am a goddess**’ and ‘I am an idiot.’” | goddess 应作「女神」；与父亲「You are definitely a goddess」本是同词呼应，写「神」把呼应拆了 | 提示 |
| **E4** 总结句序：先「结账时女侍告诉她」后「父亲出门前回头看她」 | `:286` 父亲点头出门 → `:291` “I signal the waitress for the bill. She says, “The gentleman paid your check.”” | 时序对调（原文是先目送出门、再叫账单）；块 8 读者视角（`:97`）次序正确 | 提示 |
| 块 1–8 引语逐字（8 段 segment 全 ok，pos 267/621/1872/3367/4272/5356/7592/12687） | 例：`:19` 块 1 “My parents are sitting two booths away, blissfully unaware of our existence/proximity/interest.”；`:89` 块 8 “I meet his eyes. It is almost enough to be here, with him. I try not to mind that he doesn’t know me, that this is my reunion, not his.” | 逐字命中，无一段查无 | 已核实 |
| 抬头三人年龄与 md 所述一致 | `:18` “Sunday, October 27, 1991 (Henry is 28, Clare is 20, Alba is 49 and 12 x 3)” | 导航「二十岁的母亲」「二十八岁的父亲」「四十九岁的阿尔芭」全部对上 | 已核实 |
| 付账者是父亲、付账发生在父亲离席之后 | `:291` “The gentleman paid your check.”；`:286` “Dad turns to me, studies me as though trying to memorize me” | 归属正确（未错挂给母亲），只有总结句序倒置（E4） | 已核实 |
| 词汇表 14 条例句逐字 | `:23` blissfully、booth／`:166` syrup-saturated、lukewarm／`:243` identicality／`:253` misdemeanor／`:110` banquette／`:61` commotion／`:73` eavesdrop／`:230` puzzlement／`:68` straw／`:33` bacon／`:105` refill | 全部回原文命中，无一改写（含标点） | 已核实 |
| 「三个自己只有两双鞋」「留下一双赤脚」 | `:62` “my three selves only have two pairs between them.”；`:263` “running and laughing to distract eyes from one Alba’s bare feet.” | md 人物弧线「留下一双赤脚」符合原文（只有一个人光脚），不是「三个都光脚」 | 已核实 |

## 已核实为正确（防下一轮误修）

1. 数字别改：Alba **49 岁**、三个 **12 岁**的自己、Henry **28**、Clare **20**（`:18`）。「12 x 3」是三次十二岁，不是「十二点三次」。
2. 「四十九」（`:114`）是 Alba 回答年幼自己的原话，不是叙述者旁白，改的时候别挪进括号。
3. 「我们是克隆人」是**十二岁的 Alba** 说的（`:222` ““We’re clones,” Alba deadpans.”），不是 49 岁的她；导航（`:14`）与总结（`:131`）都把它挂在「三个年幼的阿尔芭／最小的那个」名下，正确。
4. 「Baaaa」（`:239`）是 Alba 学羊叫，不是父亲；「像多莉羊？」才是父亲（`:226`）。二者不可对调。
5. 「The gentleman paid your check.」是**女侍应**说的（`:291`），不是父亲当面说；修 E4 时不要把说话人改掉。
6. 母亲那段「Longing. Loss. Beauty.」是**分两次**说出的（`:91` 停顿后补），块 6 中文理解处理为「停了一会儿，答『渴望、失去、美』」——符合原文的停顿，勿改成一句连读。
7. 「Zach」（md 作「扎克」，`:67`）是原文人名（`:73` “If Zach were here…”），不是 md 虚构的人物；找不到解释是正常的（本章只此一见）。
8. 机器层 rc=0 是真通过（`bash scripts/chapter.sh "…/ch37 coffee and pancakes with ghosts.md" --json`，退出码 0，issues 八类全空）；块数 8 触及 block_target 上限但未越界，不构成形态缺陷。
