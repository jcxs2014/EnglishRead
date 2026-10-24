# ch31 wild thing — 对账单（R3）

- 原文：`text/ch31_wild_thing.txt`（412 行）
- 精读：`ch31 wild thing.md`（112 行）
- 机器层：`2-machine.json`，rc=0，verdict=ok，块数 6，段数 7（块 6 以省略号分两段），segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，words 2272

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 为什么 Alba 会跟去：Richard 今晚有歌剧票 | `text/ch31_wild_thing.txt:44` “Richard has tickets to the opera tonight, so I take Alba with me.” | 导航只写「克莱尔带阿尔芭冒雨赶去」/「带上阿尔芭」（`ch31 wild thing.md:11`、`:27`），一句话总结同，均无缘由 | 提示（交代性细节，不影响事件链） |
| L2 | Beck 的博物馆有名字与馆藏清单：Museum of Lost Souls，用真实地点/图书馆/博物馆做数字副本，已收大英博物馆、摩根、斯坦福三个音乐库 | `text/ch31_wild_thing.txt:339-342` “she has built a Museum of Lost Souls from real places, real libraries and museums… She already has several music libraries—the British Museum, the Morgan, Stanford…” | 导航只留功能义「只想把一座房子收进自己的馆藏」（`ch31 wild thing.md:13`）；块与总结均无馆名与清单 | 提示（索要黄房子的动机靠「馆藏/收藏者」已传达，馆名属可省细节） |
| L3 | 被索要那一刻的三个动作：Alba 惊慌看母亲、Beck 先反问「Why do you ask?」、Alba 后来说「Can you turn her off?」 | `:300` “Now all three of us are silent. Alba looks at me, panicked.”；`:304`；`:317` “Alba says, urgently, “Can you turn her off?”” | 导航只写「伊莎多拉随即索要那座房子」（`:11`）；一句话总结写「阿尔芭惊慌地要把它关掉」（`:112`）——惊慌与关机保留了，Beck 的反问未留 | 跳过（核心反应已在总结中，Beck 一句反问属过程） |

## 二、编（md 有、原文无）

无。逐块与导航核过：所有情节断言都能在原文找到出处，包括容易写错的几处——
「伊莎多拉换了玻璃眼珠」`:82`、“像剥了皮的尸体”`:82` “like a cadaver missing its skin”、“它自称不是女孩是 wild thing”`:142`、“数学做的”`:158`。

## 三、错（两边都有但不一致）

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `ch31 wild thing.md:11` 一句话概括、`:112` 一句话总结 | 「又**即兴**奏出黄房子笔记本里的曲子」/「又即兴奏出从黄房子笔记本里学来的曲子」 | `:283` Clare 问 “You improvised that? Wow.”；`:287` Alba 当场更正 “I sort of did. **That’s written music**, but I couldn’t remember it very well so I kind of **filled it in**. It’s music from the notebooks at the Yellow House.” | 提示（「即兴」是 Clare 的第一反应、Alba 随即更正为「有谱、记不全、自己补的」；md 两处都停在「即兴」，且与同句「学来的」自相抵。此层是后文「她将来会写出来／她若已背熟怎么还会写」的关键前提，建议改「半记半补地奏出」） |
| E2 | `ch31 wild thing.md:21` 块 1 中文理解 | 「她只凭对方叫她名字的口气，就听出**贝克出了事**」 | `:23` “I can tell by the way she says my name that Beck is upset.” | 跳过（upset＝心绪不宁，译文往前推了半步；下句即揭示割胎，不构成事实错误） |
| E3 | `ch31 wild thing.md:14` 人物弧线 | 「贝克从受害者变成决定者：她承认这颗脑袋太分散注意力，**要换一种形态**」 | `:351` “But maybe the head is too distracting. It’s time for something else.” | 已核实（「换一种形态」是对 “something else” 的合理落地，非增情节） |
| E4 | `ch31 wild thing.md:13` Tropes | 「阿尔芭不退，嫌它丑，**还要给它一张女孩的脸**」 | `:124` Alba: “Why don’t you give her a nice face?”；`:133` “You should let a girl make your face.” | 已核实（两处合写，均有原文支点） |

## 四、归属方向复核（R4 三问）

- 块 2「有人翻过铁丝网，只为割**她的**胎」⇄ `:46` “Someone climbed the chain-link fence just to slash **Beck’s** tires.” —— 受事是 Beck 的车，未误挂成 Clare 或工作室。
- 块 4「贝克说我是数学做的」⇄ `:158` “Beck says I’m made out of math” —— 说话人 Isadora、定义来源 Beck，方向正确（不是 Isadora 自我定义）。
- 块 5「她拿回声当对手，把旋律摞在持续低音上」⇄ `:274` “she’s playing against the echoes, stacking melody on top of harmonic drones” —— 施事是 Alba，正确。
- 导航「伊莎多拉索要房子」⇄ `:304` “You can get it for me?” —— 索要者是 Isadora、被要求者是 Beck，未写成 Alba 索要。
- 收尾「克莱尔请贝克搬来同住」⇄ `:394` “maybe you could just, um, move in?” —— 邀请方是 Clare，接受方是 Beck（`:407` “Yes. I’d like that.”），方向正确。
