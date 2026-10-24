# ch41 wild thing variations — 对账单（R3）

原文 `text/ch41_wild_thing_variations.txt` 205 行／精读 `ch41 wild thing variations.md` 101 行；机器层 **rc=0**（verdict=ok，块 5／引语 5／段 5 全 ok，counts 九类全零，words 1832，导航 5，block_target [3,6]）。
声部：**贝克第一人称**（`:23` “Beck: It’s already too warm this morning.”），全章无第二个叙述者。

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文（行 + 逐字） | md 侧 | 档 |
|---|---|---|---|---|
| L1 | **「会不会是她自己在分割自己」——伊莎多拉异常的真正答案，也是本章的剧情钩子** | `text/ch41_wild_thing_variations.txt:175` ““Are you the person who’s been partitioning Isadora?””；`:179` ““I don’t code. Might she be partitioning herself?””；`:183` ““She might. As you said earlier, children can be secretive.” I feel a pang of sorrow at the idea of Isadora keeping secrets from me, growing away from me.”；取证：`/usr/bin/grep -nE "分割" "ch41 wild thing variations.md"` → 无输出 **rc=1**；`grep -nE "partition"` → 无输出 **rc=1**；`grep -nE "拆|分叉|分身|分版"` → 无输出 **rc=1** | 全章零落点。而 md `:15` 恰好写了「奥利弗常答非所问，用童话句式把解释留在门外」——**只留下「他把话岔开」这个动作，被岔开的那一问却整条删掉**。这是伊莎多拉线的引擎（她不是被入侵，是自己在长大、在分岔），也是贝克「一阵难过」的唯一来由 | **阻断** |
| L2 | 密码是 **130698**，且「对你没意义，阿尔芭要是够大也许会认出来」 | `:70` “It says 130698. “That’s for this lock.””；`:75-77` ““Does it mean anything?”… “Not to you. Alba might recognize it, if she’s old enough.”” | md `:11` 只写「他给出密码打开壁橱」，`:15` 只写「密码写在撕下的纸角上」；数字与「阿尔芭会认出来」全无（`grep -nE "130698"` → 无输出 rc=1） | 提示 |
| L3 | 奥利弗与伊莎多拉的交情年限与**两个年份**：认识 44 年，他 2041 年首见她、她 2013 年首见他 | `:88` ““I’ve been acquainted with Isadora for forty-four years. I first met her in 2041; she first met me in 2013. We’re old friends.”” | md `:101` 只有「认识伊莎多拉四十四年」；`grep -nE "2041|2013"` → 无输出 **rc=1**。两个年份一丢，「时间旅行者的双向时序」（他比她先老）就没了证据 | 提示 |
| L4 | 「**你在造一个新世界，而旧世界正在自我拆解**」——奥利弗对贝克所作所为的判词 | `:115` ““You are making a new world, while the old world unmakes itself. Shall we bring the scanner upstairs and get started?”” | 零落点：`grep -nE "新世界|旧世界"` → 无输出 **rc=1**。这是全章对「博物馆」这件事最重的一句定性 | 提示 |
| L5 | 「据我所知，**阿尔芭从没跟她母亲提过我**」——克莱尔不知道奥利弗存在 | `:97` ““Children can be a bit secretive with their parents if they think they’re going to get in trouble. Alba never mentioned me to her mother, as far as I know.”” | md `:47` 只保留前半句「孩子会瞒父母」；`grep -nE "从没.*提过"` → 无输出 **rc=1**。后半句才是信息（这个家还有第三个人被瞒着） | 提示 |
| L6 | 变奏曲的三段走向：**更暗更沉 → 开始摇摆 → 越走越远，像夜里在森林迷路 → 最后主题从混沌里浮回** | `:148` “The next variation is darker, more somber. As the piece goes on, it begins to swing, but it’s also deviating more and more from the original, like getting lost in the forest as night falls. Finally, “Wild Thing” emerges from the sonic chaos, and the last notes linger, suspended, in the air.” | md 只有 `:57`「旋律越走越远，最后又回来」一句概括；`grep -nE "森林"` → 无输出 **rc=1**；`grep -nE "摇摆"` → 无输出 **rc=1**。本章以曲名作章名，曲子的走向即结构本身，被压成「越走越远」 | 提示 |
| L7 | 「阿尔芭现在十六岁」＋「**文件柜里没有一首我能在十六岁的阿尔芭面前弹**」——为什么必须弹四十多岁写的曲子 | `:138` ““Sixteen.””；`:142` ““There’s nothing in the file cabinet that I could play if sixteen-year-old Alba were here…”” | `grep -nE "十六"` → 无输出 **rc=1**。md 直接跳到「她四十岁写的」，读者拿不到这条时间旅行的算术 | 提示 |
| L8 | 「他弹了**半个小时**」＋「她只有**手机**，只能将就」 | `:153` “He’s been playing for half an hour.”；`:142` “All I have is my phone; it will have to do.” | `grep -nE "半小时"` → 无输出 **rc=1**；`grep -nE "手机"` → 无输出 **rc=1**。半小时的长度与「只有手机」的将就感是这段录音的分量所在 | 提示 |
| L9 | 「我在试着教她善良。」——「那很好。我也是。」——两人当场结成同盟 | `:192-196` ““I’m trying to teach her to be kind.” / “That’s good. So am I.” Oliver stands and eases his back. All his joints pop and crack. He looks tired.”；取证：`grep -nE "善良"` → 无输出 **rc=1** | md `:14` 只说「两人在扫描仪前结成临时的同伴」，未落到具体那句话；这也是「伊莎多拉危险吗」那段的收束 | 提示 |
| L10 | 抬头年龄 **Beck is 42, Oliver is 57** | `:18` “Tuesday, July 17, 2018 (Beck is 42, Oliver is 57)” | `grep -nE "42|57|四十二|五十七"` → 无输出 **rc=1**。md 全篇未给两个成年人的年龄（奥利弗 57 与「中年」并置的落差感因此消失） | 提示 |
| L11 | 「谢谢你这些年来所有的杂货」——一句就把「她独自来过很多次」坐实 | `:60` ““Thank you for bringing such nice groceries. Thank you for all the groceries, over the years.”” | md `:21` 有「近几年她也独自过来」，功能已覆盖；只是原句那记温度没了 | 跳过 |
| L12 | 伊莎多拉不解：为什么要把一栋普通房子这么彻底地存档；她答「住宅博物馆，像 Dennis Severs' House 或 Edward Gorey House」，**却没告诉她这是阿尔芭的房子** | `:23` “Isadora finds it puzzling that we are archiving an ordinary house so thoroughly; I told her that it’s a house museum… I haven’t told her that this is Alba’s house.” | md `:27` 读者视角提示已完整保留（含 house museum 与「没告诉伊莎多拉这是阿尔芭的房子」），只是未进正文块——取舍成立 | 跳过 |

## 二、编（md 有、原文无）

| # | md 侧 | 原文核对 | 档 |
|---|---|---|---|
| — | 逐条核对 md 的 5 块与 5 条导航，未发现凭空出现的情节、关系或数字 | `:23`（黄房子／补货／碰运气）、`:39`（椅中人／亚麻西装／赤脚）、`:47`（姓名与身份）、`:79`（四抽屉文件柜、全扫）、`:88`（44 年）、`:106`（婴儿怪物／女主角）、`:142`（四十多岁／1970s）、`:147-148`（Wild Thing／Troggs／几百遍）、`:170`（禁播）、`:205`（后视镜）——md 所写皆有出处 | 无 |

## 三、错（两边都有但不一致）

| # | md 侧 | 原文（行 + 逐字） | 性质 | 档 |
|---|---|---|---|---|
| E1 | `ch41 wild thing variations.md:12`「转折落在录音的去处——**他说阿尔芭近来为音乐消沉**，这段曲子不能给她听」 | `:166` ““I wish she could hear that now,” I say. “She’s been so despondent about her music. About everything, really.”” ——**说这话的是贝克**（“I say”）；奥利弗的回应是 `:170` 的警觉与禁令 | 发言归属反了：贝克的观察被记到奥利弗名下。同段后半句（禁播）归属正确，故只判提示 | 提示 |
| E2 | `ch41 …md:11`「弹了她**四十岁**写的《Wild Thing 变奏曲》」；`:101`「他弹了她**四十岁**写的」 | `:142` “This piece was written by Alba in her **forties**, mostly in the 1970s.”——forties＝四十多岁（md 词汇表 `:97` 自己就写「四十多岁」） | 数字／时段不符：四十岁 ≠ 四十多岁。两处同错，属同一处修订点 | 提示 |
| E3 | `ch41 …md:27`「留意她**后来**说这房子像『house museum』」 | `:23` 是本章**第一段**的叙述（“I told her that it’s a house museum”），并非「后来」 | 时序措辞小偏，不影响理解 | 提示 |

## 四、归属方向复核（R4 三问）

对 5 块逐一追「谁做的／对谁做的／谁的」。

1. **块 1（原句 1）**：主语＝贝克（“Clare and I come here”＋“I’ve dropped by”），对象＝黄房子／阿尔芭的朋友。中文理解 `:21` 主语保持贝克，「碰巧遇见」的方向正确。**成立**。
2. **块 2（原句 2）**：主语＝那个男人（存在句），受事＝贝克（被吓到的是她）。中文理解 `:31`「他大概一直不出声地坐在那儿，听她满屋子走动」——「听」的主语是他、宾语是她，与 `:39` “listening to me barging around” 一致。**成立**。
3. **块 3（原句 3）**：`you` ＝贝克（“Beck, you know how these stories go”），`she` ＝伊莎多拉，`our Isadora monster` 是同位语。中文理解 `:41` 三处人称全对；「她同时也是女主角」未误挂给阿尔芭。**成立**。
4. **块 4（原句 4）**：主语＝他（奥利弗弹）；受事＝《Wild Thing》旋律；`so beloved by Isadora` 的 by 指向伊莎多拉（她爱这首歌），不是「她写的」。中文理解 `:51`「那是 The Troggs 唱红的歌，伊莎多拉爱到能高高兴兴连弹几百遍」——`by` 的方向解对了。**成立**。
5. **块 5（原句 5）**：主语＝贝克（停、看、踩油门），受事＝后视镜里的奥利弗；`he turns and begins to walk back` 的主语是他。中文理解 `:61` 两个动作主体未混。**成立**。

另核 md `:13` Tropes「他认识伊莎多拉多年，**替她保存所有版本**」——原文 `:79` 是 “Isadora will want everything, so we scan everything”，即「因为她要全部，所以我们全扫」；md 的「替她保存」方向不错（为她保存），但把「全扫」的理由说成「保存所有版本」略偏——`grep -nE "三个版本|最后一版"` → 无输出 **rc=1**，原文「三个版本、阿尔芭会说只留最后一版」这层对比未进 md。**不另立档，并入 L6 同一处密度不足**。

## 五、可核验断言（命令 + 输出 + 退出码）

```bash
cd notes/books/novels/life-out-of-order-by-audrey-niffenegger
M="ch41 wild thing variations.md"
/usr/bin/grep -nE "分割" "$M"        # 无输出 rc=1
/usr/bin/grep -nE "partition" "$M"   # 无输出 rc=1
/usr/bin/grep -nE "2041|2013" "$M"   # 无输出 rc=1
/usr/bin/grep -nE "130698" "$M"      # 无输出 rc=1
/usr/bin/grep -nE "新世界|旧世界" "$M"  # 无输出 rc=1
/usr/bin/grep -nE "从没.*提过" "$M"   # 无输出 rc=1
/usr/bin/grep -nE "森林" "$M"        # 无输出 rc=1
/usr/bin/grep -nE "摇摆" "$M"        # 无输出 rc=1
/usr/bin/grep -nE "十六" "$M"        # 无输出 rc=1
/usr/bin/grep -nE "半小时" "$M"      # 无输出 rc=1
/usr/bin/grep -nE "手机" "$M"        # 无输出 rc=1
/usr/bin/grep -nE "善良" "$M"        # 无输出 rc=1
/usr/bin/grep -nE "42|57|四十二|五十七" "$M"  # 无输出 rc=1
/usr/bin/grep -nE "三个版本|最后一版" "$M"    # 无输出 rc=1
# 正面核对（原文侧）
/usr/bin/grep -nE "partitioning|making a new world|130698|forty-four years|2041|sixteen" text/ch41_wild_thing_variations.txt
#   → 70:130698 / 88:forty-four years…2041…2013 / 115:making a new world / 142:sixteen / 175,179:partitioning
# 归属核对
/usr/bin/grep -nE "despondent" text/ch41_wild_thing_variations.txt
#   → 166: “I wish she could hear that now,” I say. “She’s been so despondent about her music.”
```
