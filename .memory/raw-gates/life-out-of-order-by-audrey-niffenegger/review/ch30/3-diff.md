# ch30 chance encounter — 对账单（R3）

- 原文：`text/ch30_chance_encounter.txt`（230 行）
- 精读：`ch30 chance encounter.md`（101 行）
- 机器层：`2-machine.json`，rc=0，verdict=ok，块数 5，引语 5 段全逐字，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，words 1625

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 章末收束场景：她给 Alba 读完几章《Harriet the Spy》，趁 Alba 快睡着问她有没有见过叫 Oliver 的人，Alba 不高兴地提醒她班上有两个男孩叫这名，她就不再追问 | `text/ch30_chance_encounter.txt:229` “In the evening, after we’ve read a few chapters from Harriet the Spy, as Alba is falling asleep, I ask her if she’s ever met anyone named Oliver, and she grumpily reminds me that there are two boys in her class with that name. I leave it at that.” | md 导航末句只写「收尾是收拾房间的安稳」（`ch30 chance encounter.md:12`）；一句话总结止于「她收拾好房间，觉得事情兜了一圈回到原处」（`:101`），无此场景 | 提示（非转折；母亲试探女儿这一笔属余味，不进块不构成关键事件缺失） |
| L2 | 数字类锚点未落地：Clare 39 / Oliver 59（抬头）、Alba 八岁、婚礼 2014、Beck 与 Clare 去年冬天相识 | `:18` “Monday, August 2, 2010 (Clare is 39, Oliver is 59)”；`:105` “Eight.”；`:141` “2014, Alba says.”；`:132` “Last winter” | 五块与导航均未出现任何年龄／婚期数字 | 跳过（块选句未覆盖，且原文自身 Alba 年龄与 `:41` 的 teenage 冲突，md 按任务口径写「十几岁」是正解，不必强塞数字） |
| L3 | 「Oliver 本名不是这个」这层身份信息 | `:184` ““It wasn’t, originally, but it is now.”” | md 块 4 只保留「见过更年长的她＋别告诉 Alba」；导航亦未提本名 | 提示（身份钩子之一，未进块；与块 4 的选句取舍有关，不判阻断） |

## 二、编（md 有、原文无）

无。逐条核过五个块的「中文理解」与导航五条：所增细节均可在原文同段找到出处（例：块 1「抱着杂货」对应 `:24` “gather up some of the grocery bags”；块 2「穿着楼上壁橱里的亚麻长裤」对应 `:41` “linen trousers from the closet upstairs”）。

## 三、错（两边都有但不一致）

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `ch30 chance encounter.md:41` 块 3 中文理解 | 「他讲父亲当年**在男厕刮胡子**，警察进来问有没有看见一个年轻女人……」 | `:109` “…Then the police came and asked him if he’d seen a young woman, and he said no.”；引语本身不含刮胡子，该细节在前一句 `:109` “He was in the men’s room, shaving, when he realized that someone was hiding in one of the stalls.” | 提示（引语选短了一点点：中文理解补了引语外紧邻的一句原文；事实无误、非编造，故不判阻断） |
| E2 | `ch30 chance encounter.md:12` 情感弧线 | 「直到「有人命系于此」，**她笑不出来了**」 | `:193` “This is so unexpected that I laugh, but Oliver doesn’t.”；`:212` ““All right. I’ll do what I can.” I don’t want to know whose lives he means.”——原文只写她笑过、随后答应且不愿追问，未写「笑不出来」 | 跳过（属解读性表述，未被原文反证；不作事实断言判） |

## 四、归属方向复核（R4 三问）

- 块 4「在她年长得多、他反而更年轻的时候」⇄ `:171` “I’ve met you before, when you were much older, and I was somewhat younger.” —— 方向正确（她更年长、他更年轻），未颠倒。
- 块 5「贝克必须是教纳迪娅的那个人」⇄ `:207` “lives depend on Beck being the one to teach Nadia” —— 受事是 Nadia、施事是 Beck，未把「谁教谁」写反。
- 块 3「父亲说没有」⇄ `:109` “and he said no” —— 主语是父亲，未误挂到母亲或警察。
- 导航「她不请自来」⇄ `:24` “I walk around the house to the back door and quietly let myself into the kitchen.” —— 闯入者是 Clare，方向正确。
