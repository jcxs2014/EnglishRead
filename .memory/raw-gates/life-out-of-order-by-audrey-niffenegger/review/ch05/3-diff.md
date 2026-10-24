# ch05 对账（R3）

素读：`1-suread.json`（18 条，全部 `text/ch05_ghost_bikes.txt:行` + 逐字，脚本校验 18/18；首版三条行号错——`:137`→`:128`、`:259`→`:257`、决定论那句去掉了误加的左引号，已改并复验）。
机器：`2-machine.json` rc=0；块数 10；引语 10 段全 ok；`segment_miss` 0；空引号 0；结构 0；关键词全中；`cjk_low` 0；词数 7651。注意 `block_target`=[14,15]——本章 7651 词，机器按长度给的区间是 14–15 块，实做 10 块，**块数偏少是本章主要形态风险**（`block_count` 未判红，只提示）。
md 151 行，10 块 + 5 条导航 + 词汇 13 条。
块→原文行：1 `:23`、2 `:73`、3 `:257`、4 `:263`、5 `:307`、6 `:452`、7 `:521`、8 `:737`、9 `:915`、10 `:979`（顺序与原文一致，无倒置）。

## 一、漏（素读有、md 无）

### 1. 【阻断】Kendrick 医生发现牙、答应留存 DNA 的整场戏全缺

原文 `:915` 之后，Alba 把牙藏到枕头下，Kendrick 医生来查房，发现了那只密封袋——这是本章最后一场戏，也是「牙」这条伏笔唯一被说明用途的地方：

- 原文 `:922`：「“**Alba, are you losing teeth?**”」
- 原文 `:937`：「**Can you preserve them? The DNA in them?**」
- 原文 `:941`：「“**You want to bank them? Why?**”」
- 原文 `:966`：「“Okay. **I’ll take care of them.**” He tucks the baggie into his briefcase. “**Whose teeth are they?**”」
- 原文 `:970`：「**It’s a secret.**」
- 原文 `:974`：「“**You are every bit as crazy as your dad**,” he says, turning out the light.」

md 侧：`/usr/bin/grep -nE "Kendrick|DNA|保管|保存" "ch05 ghost bikes.md"` → exit=1，全无命中；块 9 停在「Don't tell」，块 10 直接跳到「这是给 Isadora 的礼物」，中间整场戏被删掉。导航五条也无一句提到医生接过牙。因此读者在 md 里只看到「Alba 收下一袋牙」，看不到「牙被交给医生做 DNA 保存」——伏笔的机关被抽掉了。
判断：关键场景整段缺失、无取舍说明 ⇒ 阻断。

### 2. 【提示】Gomez 讲 Clare 与 Beck 的那段被砍掉

- 原文 `:755`：「It was as though all the damage came down on her at once, when Henry was killed. We thought she knew how to live that strange, out-of-order life because she'd known Henry since she was a kid. But it turns out it had a delayed effect. **Beck saved her.** I don't know what Clare would do without Beck.」
- 原文 `:761`：「I feel as though I'm **dating two girls simultaneously**. Alba-in-the-present is wonderful… But future Alba is something else: **She knows too much.**」
- md：`grep -nE "Beck 救了|两个女孩|知道得太多"` = 0。块 8 只取了「tone it down」那半段，Gomez 的私人交底全丢。
- 判断：人物背景与 Zach 的核心困境，提示。

### 3. 【提示】第 50 选区的无人机政治只在词汇例句里出现

- 原文 `:111`：「people have been shooting at drones and yesterday **a dead drone landed on a kid in Indian Boundary Park**. The 50th Ward is officially anti-drone and pro-child, so Gomez has proposed a no-fly zone and the City Council is dithering about it.」
- md：`grep -nE "无人机|Indian Boundary"` = 0，只有 md:137 词汇表 `dithering` 的例句带出「no-fly zone / anti-drone」。
- 判断：世界状态（城市治安崩坏）的一手细节，提示。

### 4. 【提示】移民突击搜查只落在一条「读者视角提示」里

- 原文 `:778`「“**Immigration raid! Tear gas!**”」→ `:783`「we can see **ICE and some marines in riot gear** forming a line blocking off Halstead」→ `:802`「We arrive at the barricade, and **enter the fray**」。
- md：`grep -nE "移民|催泪|ICE"` = 0；只有 md:97（块 8 的读者视角提示）写「Belmont 方向就有人喊着 Immigration raid 跑来」。
- 判断：本章结尾的动作高潮（两个主角冲进冲突）没有块，只有一句提示带过；提示。

### 5. 【提示】「共守秘密」的具体条件未落

- 原文 `:566`「Let's have a secret together.」→ `:574`「**I'm a year ahead of you. July 15, 2024, is the day I came from.**…when you get to me, next July, I'll give you my answer.」；另 `:531`「your parents' divorce was finalized last week」。
- md：`grep -nE "7 月 15|七月十五|离婚"` = 0；导航只写「她把答案留到明年七月」。
- 判断：条件（她来自 2024-07-15、答案明年七月给）是后续章节的时间锚，提示。

### 6. 【提示】探视通行证与 Nadia 的口信

- 原文 `:487`「I've got passes for **five different hospitals**.」；`:326`「**Nadia sends her love.** She's very worried about you.」
- md：`grep -nE "通行证|Nadia"` = 0。
- 判断：细节，提示。

## 二、编（md 有、原文无）

无独立条目。两处措辞越界，并入下面的「错」一起看（都不构成新情节）。

## 三、错（两边都有但不一致）

### 1. 【提示·严格读法为「错」】导航把「踩油门」记在 Caralora 名下

- 原文 `:263`：「**Caralora shouts, “Drive, dammit,”** and the Camry quickly backs up.」——催 Zach 开车的是她，踩油门的是 Zach（同段「I floor it」）。
- md:14：「Caralora 从头反对到尾，**最后是踩油门、拉车门、踢司机的人**。」
- 「拉车门、踢司机」对（`:263`「Caralora and Joe have dragged the Camry driver out of his car and are taking turns kicking him」），「踩油门」主语错。按作业单「主语/归属方向不一致＝错」，严格读法应判阻断；因只涉及导航一句压缩、同句另两个动作均正确，此处降为提示，交派工方定档。

### 2. 【提示·严格读法为「错」】块 10 把 Huffy 说成「一个十二岁孩子骑过的车」

- 原文 `:23`：「a battered yellow Huffy **that reminds me of the bike I had when I was twelve**」——是「让她想起」，不是她十二岁那辆。
- md:117（块 10 读者视角提示）：「一个十二岁孩子骑过的车被刷成白色，送给一个十八岁的死者」。块 1 的中文理解写对了（「让 Alba 想起自己十二岁骑的那辆」），提示里又说反了。

### 3. 【提示】块 2 说「给一辆陌生人的车做准备」

- 原文 `:73` 同一段：「this is the third ghost bike we have made in the last six weeks」；Lily 不是陌生人（`:37`「We all knew her」），车也不是 Lily 的（一辆捐赠的旧 Huffy）。
- md:35：「磨砂纸的动作是给一辆陌生人的车做准备」——「陌生人」既可能指死者也可能指车主，易生歧义；提示。

### 4. 【假红】导航「她在半空消失」

- 原文 `:263` Zach 视角：「I can't see if she vanished or just fell.」——目击者不确定；但 `:263` 同段「I see her clothes, strewn all over the sidewalk…there she is, curled on her side, naked」＋`:351` Alba 自己「I must have time traveled」，实际就是时间旅行。
- 导航写「她在半空消失」是对结果的正确归纳，不是与原文冲突；判假红。

## 四、R4 逐块对应（10 块）

| 块 | 引语（text 行） | 是不是在讲这句引语 | 三问要点 |
|---|---|---|---|
| 1 | `:23` | 是。GHOST KIT 的内容物＋铺塑料布＋推来黄色 Huffy＋「让我想起十二岁那辆」 | 施事 Rosa／Caralora；「让我想起」的主语是 Alba，md 未颠倒 |
| 2 | `:73` | 是。铅笔写 Lily 名字与生卒日期＋砂纸钢丝球磨旧漆＋六周第三辆＋「我们很生气」 | 施事 Alba（写）／Rosa（磨）；「angry」的主语是 we |
| 3 | `:257` | 是。心里喊别在学校门口→加速→听见车加速→被抛起→翻转疼痛 | 全程第一人称内视角，受事是「我」；md 未改成旁观 |
| 4 | `:263` | 是。明知何时何地仍震惊→像罚球悬空→不见了→分不清消失还是摔落 | 主语 I＝Zach，受事 Alba；「vanished or just fell」的不确定被保留 |
| 5 | `:307` | 是。不必因「已经发生过」就照做→可以拒绝→不是决定论机器→在当下永远可以选→别放大她的鲁莽 | 说话人 Clare，受话人 Zach；md 未把「放大」译成「纵容」以外的意思 |
| 6 | `:452` | 是。有时能护我有时不能→他跟所有人一样→他要找的是可撞的女孩→他在牢里→风险是我选的、伤是我受的 | 说话人＝未来的 Alba；「he」＝凶手，方向未反 |
| 7 | `:521` | 是。求婚＋翻来覆去想了几周＋自觉不够格＋「未来我们已婚」的确定感 | 主语 Zach；「warm it to my touch」译「搓热」保住了触觉隐喻 |
| 8 | `:737` | 是。为一个人冒所有人的险＋他只是随机杀人犯＋不归你们管＋要安静＋打根上的问题 | 说话人 Gomez，受话人 Zach；「ours」的边界译对 |
| 9 | `:915` | 是。Lucinda 刚要否认（否认「你真好」）→大人回来→把袋子塞枕头下→互道「别说出去」 | 「deny it」指否认前一句夸奖，md 译「刚要否认」未错指 |
| 10 | `:979` | 是。给 Isadora 的礼物＋她不懂用途＋所有可能都让人不安＋梦见飞却始终不落地 | 主语 Alba；「I never do」＝始终没落地，译对 |

密度：10 块中文理解 60–120 字，「为什么这样写」80–150 字，均扣句内词（depressingly / free throw / determinism machine / warm it to my touch / fuss over me），无一块转去讲全书主旨。
形状问题：7651 词只做 10 块，等于平均 765 词一块；`:161`–`:260` 的「设伏」整段（练习跑、分工、粉裙、红 BMW、Rosa 逆向堵路、Max 与 Joe 藏身、黑色 Camry 的预告）没有一块，只在导航一句话里压缩。这一段的「计划伦理」（谁被放在危险位置）正是后文 Clare 与 Gomez 两段训话的靶子，缺块使那两段失去具体所指。此点与「一、1」并列，作为本章主要形态问题记录。
