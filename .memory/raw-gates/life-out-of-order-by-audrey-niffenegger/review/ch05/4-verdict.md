# ch05 判定表（R5）

章：`ch05 ghost bikes.md`（151 行，10 块，词汇 13 条）
原文：`text/ch05_ghost_bikes.txt`（979 行 / 7651 词）
机器：`2-machine.json` rc=0；块数 10；引语 10 段 ok；`segment_miss` 0；空引号 0；子项缺 0；`keyword_bad` 0；`cjk_low` 0。**`block_target`=[14,15]、实做 10**：这是本章唯一的形态异常（未判红，但按 7651 词计，块数明显偏少）。
素读：`1-suread.json` 18 条，`quote in line` 校验 18/18（首版三处已改：`:137`→`:128`、`:259`→`:257`、决定论句去掉误加的左引号）。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 牙被交给医生、留存 DNA 的整场戏应进块 | `:922`「“**Alba, are you losing teeth?**”」；`:937`「**Can you preserve them? The DNA in them?**」；`:941`「“**You want to bank them? Why?**”」；`:966`「“Okay. **I’ll take care of them.**” He tucks the baggie into his briefcase.」；`:974`「“**You are every bit as crazy as your dad**”」；md 侧 `/usr/bin/grep -nE "Kendrick\|DNA\|保管\|保存" "ch05 ghost bikes.md"` → **exit=1（无任何命中）** | 本章最后一场戏、也是「牙」这条伏笔唯一交代用途的地方，块与导航全无 | **阻断**（漏） |
| Gomez 讲 Clare 崩溃与 Beck 救她 | `:755`「It was as though all the damage came down on her at once, when Henry was killed… **Beck saved her.** I don’t know what Clare would do without Beck.」；`:761`「I feel as though I’m **dating two girls simultaneously**… But future Alba is something else: **She knows too much.**」；md `grep -nE "Beck 救了\|两个女孩\|知道得太多"` → exit=1 | 人物背景＋Zach 处境的核心自述全缺 | 提示（漏） |
| 第 50 选区无人机政治 | `:111`「**a dead drone landed on a kid in Indian Boundary Park**…Gomez has proposed a no-fly zone and the City Council is dithering about it.」；md `grep -nE "无人机\|Indian Boundary"` → 0 | 仅 md:137 词汇例句 `dithering` 带出「no-fly zone」 | 提示（漏） |
| 结尾移民突袭应有块 | `:778`「“**Immigration raid! Tear gas!**”」；`:783`「**ICE and some marines in riot gear** forming a line blocking off Halstead」；`:802`「We arrive at the barricade, and **enter the fray**」；md `grep -nE "移民\|催泪\|ICE"` → 0 | 只有 md:97 一句提示带过，无块 | 提示（漏） |
| 「共守一个秘密」的条件 | `:566`「Let’s have a secret together.」；`:574`「**I’m a year ahead of you. July 15, 2024, is the day I came from.**」；`:535`「your parents’ divorce was finalized last week.」；md `grep -nE "7 月 15\|离婚"` → 0 | 时间锚点未落 | 提示（漏） |
| 探视通行证与 Nadia 口信 | `:487`「I’ve got passes for **five different hospitals**.」；`:326`「**Nadia sends her love.** She’s very worried about you.」；md `grep -nE "通行证\|Nadia"` → 0 | 细节 | 提示（漏） |
| md:14「Caralora…最后是**踩油门**、拉车门、踢司机的人」 | `:263`「**Caralora shouts, “Drive, dammit,”** and the Camry quickly backs up.」＋同段「**I floor it**」（主语 I＝Zach）；「dragged the Camry driver out of his car and are taking turns kicking him」两句对 | 「踩油门」主语错（拉车门、踢司机对） | 提示（严格读法为「错」） |
| md:117「**一个十二岁孩子骑过的车**被刷成白色」 | `:23`「a battered yellow Huffy **that reminds me of the bike I had when I was twelve**」 | 只是「让她想起」，被写成同一辆车 | 提示（严格读法为「错」） |
| md:35「磨砂纸的动作是给一辆**陌生人的车**做准备」 | `:37`「“A girl named Lily Hanko. We knew her from Critical Mass.”」；`:73`「this is the third ghost bike we have made」；Huffy 是捐赠旧车（`:242`「an old Trek ladies’ hybrid that Caralora has donated」，另 Huffy 见 `:23`） | 死者并非陌生人、车也不属于死者，措辞易生歧义 | 提示 |
| md:11「她在半空消失」是否与原文冲突 | `:263`「I can’t see if she vanished or just fell.」但同段「her clothes, strewn all over the sidewalk…curled on her side, naked」，`:351` Alba 自述「I must have time traveled」 | 目击者不确定、结果确为时间旅行，导航按结果归纳不算错 | **假红** |
| md:83（块 6）「死的人没死，凶手进了监狱」 | `:407`「Those other girls are dead…we got that asshole」＋`:437`「Instead of killing another person, he’s in jail」 | 指「本该被撞死的人没死」，读法成立 | **跳过** |
| 10 块对 7651 词（`block_target` 14–15） | `2-machine.json`：`"block_target": [14, 15]`、`"block_hint"` 只给块数偏少提示；`:161`–`:260` 设伏整段无块 | 块数偏少＝覆盖稀疏（与第 1 条并列构成主要形态问题） | 提示（形态） |

计数（只数阻断档）：漏 1 · 编 0 · 错 0；提示 8（其中 2 条严格读法属「错」，已注明）；假红 1；跳过 1。

## 已核实为正确

1. 抬头：`:18`「Saturday, July 1, 2023 (Alba is 21, Zach is 22)」；`:161`「Saturday, July 8, 2023–Monday, July 10, 2023 (Alba is 21 and 22)」；`:598`「Sunday morning」；`:810`「Monday evening」——md 导航与叙事手法对日期、声部切换的叙述与之一致。
2. 死者：`:37`「A girl named Lily Hanko. We knew her from Critical Mass. She was only eighteen.」；`:41`「the girl who was killed in that hit and run on Leavitt」——md:11「在 Leavitt 被撞的十八岁女孩 Lily Hanko」逐项对。
3. 第三辆：`:73`「this is the third ghost bike we have made in the last six weeks, and we are good at it now, and we are angry.」——块 2 引语与中文理解均逐字对。
4. 私密手势：`:101`「He makes the small circling gesture that means causal loop in our private code. No one sees but me.」
5. 主意来源：`:128`「“I have an idea, or actually, it’s **Older Alba’s** idea,”」；反对：`:132`「“No,” C-lora snaps…“That’s a shitty idea. What if she gets killed?”」
6. 车与装束：`:225`「“A black Camry.”」；`:237`「a pink skirt and a neon-yellow hoodie…**I feel like a tennis ball**」；`:242`「“Hello, my little **kamikaze** biker, can you hear me?”」——导航「粉裙和荧光黄连帽衫」「黑色 Camry」成立。
7. Clare 那段：`:307`「You are not caught up in some kind of determinism machine. You can choose. In the present, you can always choose. Use your own damn judgment, Zach. Don’t amplify Alba’s recklessness.」——块 5 引语完整、译文准确。
8. Rosa 伤情与医生插话：`:312`「Rosa is going to be fine…just bruised from the airbags. If she were taller, she might have been unscathed.」；`:317`「“David, don’t encourage them,” Mama says to Dr. Kendrick.」——导航「骂完医生还要补一句『别鼓励他们』」成立。
9. 未来 Alba 的辩护：`:407`「Those other girls are dead. Don’t you feel amazing, knowing that we got that asshole?」；`:434`「July 2024. Not so long from now.」
10. 求婚与秘密：`:521`「Let’s get married.」＋`:525`「I have a pretty strong notion that in the future, Alba and I are married.」；`:566`「Let’s have a secret together.」
11. 新闻处理：`:638`「The media are calling the killer the **Wicker Park Maniac**.」；`:648`「just before Alba vanishes, one camera cuts to another and we see Rosa’s rental car ramming the Camry」；`:678`「he’s going to plead guilty」；`:737`「I had to exert myself to get your faces and plate numbers scrubbed from the CCTV video.」——导航「只看得见撞击和 Rosa 那辆车撞向 Camry」「名字一个也没出现」成立。
12. 牙的来历：`:843`「I had two of my wisdom teeth out today」；`:875`「One of my older selves asked me to ask you. She said it was important, and that it’s for Isadora.」；`:906`「It’s for some sort of treatment. **Stem cells**, or something.」——块 9 与导航对（缺的只是医生那一场，见阻断条）。
13. 结尾：`:979`「It’s a gift for Isadora, Lucinda said…I dream I am flying . . . I am waiting to hit the ground, but I never do.」——块 10 逐字。
