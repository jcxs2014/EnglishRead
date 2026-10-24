# ch58 A Handbag Full of Rain —— R5 判定

- 章：ch58（`text/ch58_a_handbag_full_of_rain.txt`，929 行 / 6439 词；抬头 `:18` 2041-10-09，Zach 40）
- md：`ch58 a handbag full of rain.md`，151 行，**10 块**（＝本书硬上限，已满）
- 机器层：`bash scripts/chapter.sh` → **rc=0**，verdict=ok；10 引语全逐字；empty_quote=0；struct_bad=0

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「两座博物馆之间搭了桥」 | `:713` "they each took the Museum, as it was on the day Beck left Detroit, and each of them made it their own. Jasper built the Interstices from it" | 编（同一座博物馆的两个分支，非两座） | 提示 |
| 「在郁金香农场从接零活做起」 | `:574` "Then I did some favors, and someone saw what I could do, and recruited me for the Tulip Farm." | 错（时序：做事在受招前） | 提示 |
| 块 3 中文大半落在引语之外 | `:220` "Her eyes roll back and she crumples sideways onto the sofa cushions, passed out cold." | 对应偏移 | 提示 |
| Nadia 拒绝细讲逃亡、受招次序未写 | `:574` "“I’m going to be vague about that, if you don’t mind.”" | 漏（块满，导航已交代） | 提示 |
| Oliver 多年铺垫「我的妻子」未写 | `:796` "he was trying to prepare me for this without ever quite telling me that his wife was my wife" | 漏（块 8 只写醒悟） | 提示 |
| 露辛达无植入体未在正文落地 | `:914` "“But Lucinda doesn’t have the implant. Does she?”" | 漏（读者提示里有，正文无） | 提示 |
| 口信日期/交付/送达窗口 | `:97` "“Friday, June 13, 2098.”"；`:187`；`:189` "“I was told to deliver it after May 1, 2041.”" | 正确 | 跳过 |
| 「另一个丈夫」＝Nadia 当面所说 | `:157` "“Ah,” she says, her voice sad but her face expressionless. “The other husband.”" | 正确 | 跳过 |
| 扎克的醒悟「我一直以为自己是丈夫」 | `:789` "I’m the other husband. I’d thought I was the husband. But no." | 正确 | 跳过 |
| 植入位置（后颈一道细疤＋新标志） | `:402` "pointing to a tiny barely healed scar just above the tattoo" | 正确 | 跳过 |
| 蓝老鼠五次迭代、五分钟、留下痕迹 | `:731` "she was eight or ten iterations along, but she was on the Interstices for five minutes, and that left a trace, and that trace must be what Isadora followed" | 正确 | 跳过 |
| 包在车头接雨、倒水不吭声、不回头 | `:773` "Her purse is sitting on the hood, full of rain. She tips the water out of it without comment and climbs into the back seat."；`:780` "She doesn’t look back." | 正确 | 跳过 |
| 结尾留条、雨里回家、穿衣服睡 | `:929` "I leave a note to thank them, and I drive back to our empty house in the never-ending rain, where I climb into bed in my clothes because what even is the point anymore." | 正确 | 跳过 |
| 群像与家务细节（热汤、斜切三明治、烤肉卷、松香酒） | `:309`；`:929` "They ply me with gyros and retsina" | 正确 | 跳过 |

## 报数（四组）

| 组 | 数 | 说明 |
|---|---|---|
| 逐字 | 10/10 ✅ | segment_miss=0；人工 `/usr/bin/grep -nE` 十条块首全部命中（`:23 :60 :220 :309 :418 :528 :731 :773 :908 :929`） |
| 对应 | 9/10 ⚠️ | 块 3 中文覆盖了引语之外的大段捎话内容 |
| 形态 | 10 块＝硬上限；子项四件齐；导航 5 条 | 通过 |
| 断言 | 阻断 0 · 提示 5 · 跳过 8 | 见上表 |

## 判词

ch58 **0 阻断**（提示 5）。6439 词的长章压在 10 块的上限上，选句反而极稳：暴雨赖床、湿透的陌生人、倒下与尖叫、斜切的三明治、感知力、贾斯珀的幻听、蓝老鼠、车头接雨的包、贝克的「我们等」、雨里回家——每一块都踩在情节骨节上，逐字 10/10。两处需要修的都是小账：一是「两座博物馆」为原文所无（同一座馆被两人各取一份），二是「接零活」被放进了农场之后。块 3 的中文覆盖了引语之外太多内容，读起来像「文不对块」，建议把引语上移到捎话那几句。

## 已核实为正确（防下一轮误修）

命令：`/usr/bin/grep -nE "thunder-storming all morning|thousand-mile|eyes roll back|wrap dress and a green cardigan|You can become your avatar|Jasper started behaving strangely|Blue Mousie, to show her|purse is sitting on the hood|We wait,” Beck says|never-ending rain" text/ch58_a_handbag_full_of_rain.txt`，命中 `:23 / :60 / :220 / :309 / :418 / :528 / :731 / :773 / :908 / :929`，**退出码 0**。

- 原句 1 ＝ `:23` "It’s been thunder-storming all morning and I’m in bed. Alba is still gone, and it was hard to see the point of getting up, so instead of starting the day I just turned over and dozed through an hour or two."
- 原句 2 ＝ `:60` "There’s something a little off about her: she has a spacey, thousand-mile stare and seems uncoordinated, as though she has had a mild stroke. “Okay,” I say. I hold the door open for her."
- 原句 3 ＝ `:220` "“This one, of course. Goodbye, then,” Isadora says. Her eyes roll back and she crumples sideways onto the sofa cushions, passed out cold. Before I can react, her eyes open again and she struggles to sit up. She sees me and starts screaming."
- 原句 4 ＝ `:309` "Nadia is sitting at our kitchen table looking stylish in a wrap dress and a green cardigan I don’t remember seeing on Alba."
- 原句 5 ＝ `:418` "“Not superpowers, just perceptivities. You can become your avatar—everything looks better, smells better, you can see in the dark, all the empty places are full of things and people again. You can hang out with people who’ve died, or are far away. The best thing is being able to travel without leaving home.”"
- 原句 6 ＝ `:528` "“They worked on it together for about a year,” Nadia says. “But things got weird. Jasper started behaving strangely: … that the Museum was in danger.”"
- 原句 7 ＝ `:731` "And I resurrected Blue Mousie, to show her my own first try. I sent Blue Mousie into our apartment and let her run around for a while—not long, maybe five minutes?"
- 原句 8 ＝ `:773` "She does her spooky thing with the Interstices and says that she does. It’s not raining as hard as it was earlier. I take an umbrella and usher Nadia to her car, which is parked around the corner. Her purse is sitting on the hood, full of rain. She tips the water out of it without comment and climbs into the back seat."
- 原句 9 ＝ `:908` "“We wait,” Beck says. “I wish we knew where Lucinda is right now. I know Alba said she would be okay, but if there’s one person I can imagine Isadora seeking out in this world, it’s Lucinda.”"
- 原句 10 ＝ `:929` "Of course I would; I’m desperate for human interaction. … In the morning, I leave a note to thank them, and I drive back to our empty house in the never-ending rain, where I climb into bed in my clothes because what even is the point anymore."
- 「另一个丈夫」＝ `:157` → **Nadia 当面所说，勿改成扎克自述**
- 「Obit 不含时间旅行」＝ `:340` "“I didn’t find any mention of time travel in my obituary.”" → 正确
- 「Poor soul」＝ `:890` "Beck says, “Poor soul.”" → 正确
