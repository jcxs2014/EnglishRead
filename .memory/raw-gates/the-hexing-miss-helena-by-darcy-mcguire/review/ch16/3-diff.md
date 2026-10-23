# ch16 · R3 对账（三张单子）＋ R4 逐块对应

- 素读底稿：`review/ch16/1-suread.json`（290 行源文／151 events／28 traps／BAD=0，投毒 0→1→0）
- 机器层：`review/ch16/2-machine.json`（`chapter.sh` rc=0；blocks 9／words 2858／`block_target [5,9]`／`block_hint ""`／segments 12／`segment_miss 0`）
- md：`ch16 lilys father.md`（149 行；9 引语块；词表 22 条＝8/8/6）
- **读取顺序**：先 `text/ch16_chapter_16.txt` 全文 → 写 `1-suread.json`（子代理 R1，主会话复核 traps）→ 再开 md。铁律未破。

## 〇 结构要点（素读得出，供 R3 用）

1. 场景单一：全章都在辛西娅的起居室，`scene_split` 1–34 是提取件章节标题行（`:1` `Chapter 16`、`:22` `16`），正文 35–290。
2. POV **全程贴海伦娜**，无视角切换（`1-suread.json` pov 字段）。
3. 时间：`ch15:162` `on a sunny Wednesday afternoon` ＋ `ch15:153` `It had been a week since the dinner party` ⇒ 晚宴一周后的周三下午；ch16 紧接 ch15 客厅那场吻（`:35`–`:41` 两人整理衣鬓）。
4. 两段心声归属必须分清：`:71`／`:86` 是**希金斯太太的念头被海伦娜读心读到**（证据 `:65` `Helena gleaned from Mrs Higgins’ thoughts`、`:74` `Helena quirked her head at Mrs Higgins’ sentiment`）；`:194`／`:212`／`:227`／`:242`／`:254`／`:266`／`:272` 才是海伦娜自己的。
5. **海伦娜读不到辛西娅的心**（`:179` `understand why I can’t read her thoughts`）。
6. 闪回 `:131`–`:149`：打人的是**薇洛**（`:140` `The sting of Willow’s slap shocked Helena. Her mother had never hit her before.`），被打的是**海伦娜**。
7. `:254` `We are creatures shaped from the same stardust.` 的**来源原文自陈不明**：`:257` `She blinked, not sure if the thought came from her own mind or the cosmos.`
8. 天象是辛西娅（earthwitch）情绪的外化：`:209` 起风闪电 → `:212` `She’s an earthwitch, just like Aunt Rowan.` → `:233` `Thunder shook the windowpanes.` → `:281` `the sun tentatively peeked through the storm clouds`。**放晴这一半与雷雨同样属于该母题。**
9. 本章动因的钥匙在 `:173`＋`:176`：`But she had created this mess because of deeply buried fear and a promise she made to herself long ago.` / `When Helena’s mother strayed so far from her vow, Helena made another oath. A private promise to never fall in love with another. To never give someone such control over her heart and her choices.`

## 一 「漏」——素读有、md 无

| 编号 | 原文（`text/ch16:行`） | md 现状 | 档 |
|---|---|---|---|
| **L1** | `:173` `a promise she made to herself long ago` ＋ `:176` `Helena made another oath. A private promise to never fall in love with another. To never give someone such control over her heart and her choices.` | 全篇零提及。md:10 概括、md:12 Tropes、md:13 人物弧线、md:14 手法、9 个引语块都没有这条**私誓**。原句 4 只收了巫团家训 `We do no harm.`（`:137`），没收海伦娜自己另立的那条。 | **阻断** |
| L2 | `:191` `But I also know what it is to be used. I won’t do that to you. You are under no obligation to come with me.` | md:13 只写到「退回体面」（对应 `:170` `She was slipping back into the proper host.`）。辛西娅自陈「我也知道被利用是什么滋味」并**主动解除海伦娜的义务**，是本章对位最工整的一句，md 未收。 | 提示 |
| L3 | `:194` `She bloody well won’t be fine without me there to keep her safe.` ＋ `:197` `A new fear blossomed in Helena. Not that she might lose herself in Cynthia, but that she might lose Cynthia altogether.` | md:13「身体的反应却先一步泄露」概括过去了，但**恐惧换了对象**（怕失去自己 → 怕失去辛西娅）这个转折没写。 | 提示 |
| L4 | `:209` `Society believes women of the peerage should behave as gentle, bright blossoms. We should bring colour and fragrance into a room but have no opinions, no personal drive, no purpose beyond decorative value.` | md:13 一句「把'被人替她做主'的怒火整段说出来」带过。这段是 ch15 `:68`「By “us”, do you mean the men?」那条性别主题的直接续写，md 未点出承接关系。 | 提示 |
| L5 | `:236`–`:245` `Switching tacks, Helena nodded her head. ‘You’re right. Of course. You can feel however you want to feel.’` → `:242` `Hecate help me, I’m making things worse.` → `:248` `‘We?’` | md:14 只写了「被劝'保持冷静'那句，她一字一顿地吼回来」，没写海伦娜**换招失败**这一拍——而正是这个失败的「我们」引出后面哈姆雷特与星尘。 | 提示 |
| L6 | `:263`–`:266` `Helena could still back away. But every tiny piece of her wanted to join Cynthia on this adventure.` / `On every adventure.` | 原句 9 直接从 `:269` 的答复起笔，**她本可以退开**这个岔路口没写。 | 提示 |
| L7 | `:275` `Imagining anyone else stepping into such an intimate role filled Helena with violent jealousy.` | md 零提及。「剧烈的嫉妒」是本章海伦娜最直白的一次自我暴露。 | 提示 |
| L8 | `:278` `‘Will you let me help you?’ … Because she wasn’t just asking about this investigation.` ＋ `:281` `‘Of course I will let you help me. I never wanted to do this alone.’` ＋ `:284` `‘Then we shall do it together.’ The last word resonated through Helena like the crash of waves over rocks. A fractured piece of her heart clicked into place.` | md 的最后一块停在 `:269`。md:11「章末没有告白，只有一个'我们'」与 md:14「最后收在'一起'上」**指的就是这一段，但它不在任何引语块里**，读者无从对照。 | 提示（重） |
| L9 | `:281` `a smile breaking over her as the sun tentatively peeked through the storm clouds` | md:14 只说「雷雨跟着辛西娅的情绪走」，**没写雨过天晴**。母题只收了一半。 | 提示 |
| L10 | `:161` `Though she endeavoured to be nothing like her mother, she still emulated the woman.` | 词表收了 `endeavoured` 并用了这句作例句，但**分析层完全没碰**——「她终究活成了母亲」正是 L1 私誓的由来。 | 提示 |
| L11 | `:164` `Of course Cynthia wasn’t trying to use her. She was nothing like the man Willow chose.` | 误会其实**当页就被海伦娜自己想通了**，md 读起来像误会一直延续到章末。 | 提示 |
| L12 | `:188` `‘Cyn, I’m the one who should be asking for your forgiveness.’` | 海伦娜**先道歉**这一拍没写；md:13 只写了后面的「承认自己犯傻」（`:269`）。 | 提示 |
| L13 | `:290` `She didn’t have time to worry about falling in love with a witch when they were confronting a potential killer.` | md:11「章末没有告白」方向对，但没点出原文是**海伦娜又一次自我否认**（与 `:179` `But I’m not falling in love with Cynthia.` 首尾呼应）。 | 提示 |

> **L1 为什么是阻断**：本章的核心冲突（海伦娜为什么把一句玩笑式的「你在利用我的魔法吗」说成「我不喜欢被利用」，并因此把辛西娅推开）**只有 `:176` 那条私誓能解释**。原文自己把因果写死了——`:173` `she had created this mess because of deeply buried fear and a promise she made to herself long ago`。md 把这个动因整个漏掉，导致 md:13 只能写成「她始终用'朋友'和'帮忙'给感情包一层壳」这种没有来历的概括。属 S1「漏掉关键转折」。

## 二 「编」——md 有、原文无

**0 条。**

被排查后**不成立**的疑点（逐条留证，防下一轮误报）：

| md 位置 | 疑点 | 回原文结论 |
|---|---|---|
| md:10 | 「晚宴一周后的周三下午」 | **成立**。`ch15:153` `It had been a week since the dinner party`；`ch15:162` `on a sunny Wednesday afternoon`。 |
| md:10 | 「紧接上一章的吻」 | **成立**。`:35` `Helena felt similarly as she stared at Cynthia from across the couch cushions.`＋`:38` `They were both breathing hard and … hopelessly dishevelled. Cynthia’s mouth was bruised from her kisses`。 |
| md:10 | 「阿盖尔夫人索要的家具清单」 | **成立**。`:56` `I have the list of furnishings Lady Argyle requested, my lady.` |
| md:10 | 「被辞退的年轻女仆莉莉」 | **成立**。`:62` `Poor Lily will be counting her lucky stars she got the chop`（`got the chop`＝被解雇，不是被杀）。 |
| md:10 | 「利珀特正是辛克莱脑中闪过的那个名字」 | **成立**。`:110` `then he clearly thought George Lippert’s name`。 |
| md:10 | 「母亲却答愿为他违背所有誓言」 | **成立**。`:143` `I will break every oath I’ve made for him. That is what love demands.` |
| md:10 | 「心里判断辛西娅和姑妈一样是地巫」 | **成立**（称谓另议，见 §三 E1）。`:212` `She’s an earthwitch, just like Aunt Rowan.` |
| md:10 | 「她即将满二十八岁」 | **成立**。`:221` `Cynthia was approaching her twenty-eighth year.` |
| md:11 | 「章末没有告白」 | **成立**。`:290` `She didn’t have time to worry about falling in love with a witch`——是否认，不是告白。 |
| md:12 | 「怒火引来雷雨」 | **成立**。`:233` `Thunder shook the windowpanes.` 紧跟 `Do. Not. Tell. Me. To. Remain. Calm!’` |
| md:12 | 「狐狸当和事佬」 | **成立**。`:251` 哈姆雷特去蹭辛西娅，紧接 `:260` 辛西娅重新问「你要跟我一起去吗」。 |
| md:14 | 「全章贴海伦娜的限知，没有视角切换」 | **成立**。全文 `:35`–`:290` 无第二 POV 段；`:71`／`:86` 的他人念头是**读心所得**，不是视角切换。 |
| md:14 | 「句点像锤子，雷声接在最后一下」 | **成立**。`:233` 六个句点＋雷声紧随。 |
| md 原句 2 | 「她不是在闲聊，是在替自己的决定记账」 | **成立**。`:86` `A decision I’ll always regret. How can Georgie ever forgive me?` |
| md 原句 3 | 「唯独没有一句提到莉莉本人是否真的来信」 | **成立**。`:92` 只有 `I’m sure she is quite happy there`，无任何直接音讯。 |

## 三 「错」——两边都有但不一致

| 编号 | md 位置 | md 原文 | 原文依据 | 档 |
|---|---|---|---|---|
| **E1** | md:10（2 处）、md:20（2 处）、md:24、md:70、md:74、md:80 | 「罗温**姑妈**」共 **8 处** | `ch02:155` `Willow Blair had been the prettiest of her three sisters, and the most monstrous.`；`ch02:212` `Clio, Ellie, and Helena had all been raised together by their Aunt Rowan.`；`ch06:35` `the cherry wood table passed down to the Blair women through generations … Blair women strung together like beads of amber, stretching back to the 1600s … safe in the circle of sisterhood`；`ch06:122` `the high-end products Clio and Aunt Rowan created, providing the Blair women with a lavish lifestyle they all enjoyed`；`ch07:56` `running from her mother … Aunt Rowan’s was a fifteen-minute walk from their cottage` | **阻断**（跨章术语，见下方专节） |
| **E2** | md:54（原句 4 · 为什么这样写） | 「句子**一句比一句短**，最后落到家训'我们不伤人'」 | md 自己的引语 `:137` 九句词数实测 **7,4,4,5,4,5,7,9,4**——非单调递减，第 8 句反而是全段最长的 9 词 | **阻断**（判据 (f)：节奏断言被 md 自身引语量化证伪） |
| E3 | md:12 | 「吻后被管家**撞见**」 | `:41` `‘Just a moment,’ Cynthia called to the door`；`:47` `They were as ready as they would ever be.`；`:50` `‘Come in.’` ⇒ 是**被敲门打断**、整理好才开门，没有「撞见」 | 提示 |
| E4 | md:10 | 「管家希金斯太太便**捧着阿盖尔夫人索要的家具清单进来**」 | `:53` `entered with a tray in her hands carrying fresh coffee and tea … then pulled out a piece of parchment from her apron` ⇒ 手里端的是**茶点托盘**，清单是从围裙口袋里掏出来的 | 提示 |
| E5 | md:10 | 「辛西娅由此**追问出**莉莉的父亲就是乔治·利珀特」 | `:77` 名字是**管家先自己说出来的**：`Say what you will about George Lippert, but he has always been a devoted parent`；`:80` `‘Lily’s father is George Lippert?’` **无说话人 tag**（按 `:89`/`:95`/`:101`/`:107` 的话轮链判为辛西娅，成立，但不是「追问出」） | 提示 |
| E6 | md:10 | 「海伦娜**被'利用'二字**勾起母亲威洛的旧事」 | `:128` 触发点是海伦娜**自己**那句玩笑：`‘Are you using me for my magic?’ She said the question in jest, but no sooner had it escaped than fear, sudden and sickening, coursed through her. An old memory surged forth.` ⇒ md 读起来像是别人说了「利用」二字 | 提示 |
| E7 | md:12 | 「'利用'这个词把**一句求援**听成了拒绝」 | 被听岔的是海伦娜 `:155` `I just don’t like the idea of being used for my magic.`——那是**自我防卫**，不是求援；被听成拒绝的是她 ch15 给出的**同行之约**（`:158` `You asked to come with me`） | 提示 |
| E8 | md:14 | 「母亲的旧事以**无提示**的闪回插入」 | `:128` 末尾有明文提示 `An old memory surged forth.`；「无提示」只对**排版**成立（`:131` 直接起对白，无分隔符、无斜体、无时态标记） | 提示 |
| E9 | md:40（原句 3 · 中文理解） | 「管家脸上的纹路**松开**，堆出和善」 | `:92` `Mrs Higgins’ face creased into lines of kindness`——`creased into` 是**皱出／挤出**纹路，方向与「松开」相反 | 提示 |
| E10 | md:58（原句 5 · 中文理解） | 「辛西娅听到'利用'两个字，**眼睛睁大**，急忙说……」 | 「眼睛睁大」在 `:158` 的**前一句** `Cynthia’s hazel eyes widened as her lips parted on an inhalation.`，**不在 md 引语里** ⇒ S2 ①「引语截短：分析覆盖的原文比引语长」 | 提示 |
| E11 | md:74（原句 6 · 为什么这样写） | 「她**没有说破**是谁在呼风唤雨」 | 就引语本身成立，但 `:212` 紧接着就说破了：`She’s an earthwitch, just like Aunt Rowan.`；md:10 自己也写了「心里判断辛西娅和姑妈一样是地巫」⇒ md **内部张力** | 提示 |
| E12 | md:96（原句 8 · 读者视角提示） | 「哈姆雷特**先替海伦娜**走近了辛西娅」 | `:251` 只写 `Hamlet hopped nimbly from the couch and wound his way to Cynthia`——原文没给狐狸任何「代海伦娜行事」的动机 | 提示 |
| E13 | md:14 | 「**章末**让哈姆雷特去蹭辛西娅」 | 蹭腿在 `:251`，其后还有 `:254`–`:290` 共 19 行；不是章末 | 提示 |
| E14 | md:10／md:14 | 「海伦娜心里冒出一句'我们都是由同一捧星尘捏成的'」／「一句…**的心声**」 | `:257` `She blinked, not sure if the thought came from her own mind or the cosmos.` ⇒ 原文**自陈来源不明**，md 把不确定写成了确定（对比 ch15 md:10 保留 hedge 的做法） | 提示 |

### E1 专节 · 「罗温姑妈」→「罗温姨妈」（跨章阻断，8 处 / 本章）

**裁决：Rowan 是海伦娜的母系姨，「姨妈」对、「姑妈」错。**

证据链（全部逐字）：

1. `ch02:155` — `Willow Blair had been the prettiest of her three sisters, and the most monstrous.`
   ⇒ 海伦娜之母 **Willow 姓 Blair**，且有**三个姐妹**（四姐妹）。
2. `ch06:35` — `the cherry wood table passed down to the Blair women through generations … Women cut herbs at this table … Blair women strung together like beads of amber, stretching back to the 1600s, all gathered here to share burdens from the past … safe in the circle of sisterhood that bound them.`
   ⇒ **Blair 是母系女巫世家的姓**（代代相传、sisterhood、可上溯 1600 年代）。
3. `ch06:122` — `Aunt Rowan opened All Things Bright and Beautiful when they fled Scotland … Ladies of the beau monde paid exorbitant fees for the high-end products Clio and Aunt Rowan created, providing the Blair women with a lavish lifestyle they all enjoyed.`
   ⇒ **Rowan 被算进「the Blair women」这一群**，与 Clio 合伙、供养整个 Blair 女性家族。
4. `ch02:212` — `Clio, Ellie, and Helena had all been raised together by their Aunt Rowan. While Clio and Ellie were true sisters, they treated Helena like another sibling.`
   ＋ `ch06:50` — `‘Something is blocking your cousin’s powers.’`（Rowan 对海伦娜说）
   ＋ `ch06:116`/`:119` — `her cousin could accompany Uncle Lachlan` / `Her cousin was addicted to anything sweet`（Ellie 是海伦娜的 cousin）
   ⇒ Rowan 是**海伦娜、Clio、Ellie 三个表姐妹共同的姨**。三人是表亲，只能通过**各自的 Blair 母亲**（Willow 姐妹）相连；若 Rowan 是海伦娜的**父系**姑妈，她不可能同时是 Clio 与 Ellie 的姑妈（父亲不同）。
5. `ch07:56` — `Helena was running from her home, running from her mother as blood dripped down her arm … Aunt Rowan’s was a fifteen-minute walk from their cottage in the woods`
   ⇒ 海伦娜从**母亲**身边逃出去，十五分钟就到 Rowan 家；Rowan 与 Willow 是苏格兰时期的近邻，`ch06:122` 又写她们**一起**逃到伦敦。
6. **零命中取证（R5-补）**：全书 27 章从未提及海伦娜的父亲。
   ```
   ① 命令：/usr/bin/grep -nEi 'Helena.s (father|mother|parents)' text/*.txt > /tmp/hx_p4.txt 2>&1; echo "rc=$?"; /usr/bin/grep -c '' /tmp/hx_p4.txt
      输出：rc=1 ／ 0 行
      ⇒ 全书没有一处写「海伦娜的父亲／母亲／双亲」（母亲只以 `her mother`／`Willow` 出现，见下条正对照）。

   ② 命令：/usr/bin/grep -nEi 'helena.s father|her father|fathers name|Mr\.? Blair|Helena.s parent' text/ch01…ch07 ＋ ch14 > /tmp/hx_f1.txt 2>&1; echo "rc=$?"
      输出：rc=0 ／ 4 行，全部是 **Cynthia** 的父亲（ch05:149 `Her father had instructed her she must agree.`、ch06:246 `her father’s endless property`、ch06:258 `the will of her father`、ch06:267 `funds she inherited from her father`）
      ⇒ `her father` 这个模式在本库只命中辛西娅；`Mr Blair` 零命中。

   ③ 正对照（证明探针不是恒空）：
      命令：/usr/bin/grep -nEi 'Willow' text/*.txt | /usr/bin/grep -Ei 'sister|Blair|married|husband'
      输出：rc=0 ／ 1 行 → `text/ch02_chapter_2.txt:155: … thanks to her mother. Willow Blair had been the prettiest of her three sisters, and the most monstrous.`
   ```
   ⇒ 「姑妈」＝父亲之姐妹，而**海伦娜的父亲在全书不存在**；Blair 又是母系姓。**「姑妈」在本库无立足点。**

**分布实测**（`for f in *.md; do grep -o 姑妈/姨妈 …`）：

| 用「姑妈」（错） | 处数 | 用「姨妈」（对） | 处数 |
|---|---|---|---|
| ch04 | 1 | 00_情感节点.md | 1 |
| ch06 | 4 | 00_概述.md | 1 |
| ch07 | 1 | 00_金句精选.md | 2 |
| ch14 | 4 | ch24 | 3 |
| ch15 | 3 | ch25 | 2 |
| **ch16** | **8** | ch26 | 16 |
| 合计 | **21** | 合计 | **25** |

⇒ 修复方向与多数派一致（姨妈 25 > 姑妈 21），**不需要**「按多数派统一」的让步；本章 8 处全部要改。

**附：Lachlan 的称谓（不裁决，但「叔叔」错）**
`ch01:137` `Superintendent Lachlan MacDougal`；`ch11:44` `There’s a superintendent at Scotland Yard ’as nieces with the name of Blair. Lachlan MacDougal.`；`ch06:273` `his infuriating (beautiful) niece`；`ch07:122` `took the necklace from his niece`；`ch16:200` `Uncle Lachlan will string me up by my toes`。
⇒ 他的侄女／外甥女**姓 Blair**，关联走的是 Blair 女性这一侧 ⇒ **不是父系，「拉克兰叔叔」错**。
但 Lachlan 姓 MacDougal 不姓 Blair，原文从未写他是 Willow/Rowan 的**兄弟**还是**娶进来的丈夫**；`ch14:156`/`:159` 反而写他与 Rowan 之间有秘密与「strange enmity」、Ellie 看不到「any possible future for them」。

**零命中取证（两条，均贴命令＋输出＋退出码）**：
```
① 命令：/usr/bin/grep -nEi 'Rowan.{0,80}(husband|wife|married|spouse)|(husband|wife|married|spouse).{0,80}Rowan' text/*.txt > /tmp/hx_p1.txt 2>&1; echo "rc=$?"; /usr/bin/grep -c '' /tmp/hx_p1.txt
   输出：rc=1 ／ 0 行
   ⇒ Rowan 在全书 27 章里没有任何 husband／wife／married／spouse 的近邻表述。

② 命令：/usr/bin/grep -nEi '(Lachlan|MacDougal).{0,80}(husband|wife|married|brother|sister)|(husband|wife|married|brother|sister).{0,80}(Lachlan|MacDougal)' text/*.txt > /tmp/hx_p2.txt 2>&1; echo "rc=$?"; /usr/bin/grep -c '' /tmp/hx_p2.txt
   输出：rc=0 ／ 15 行
   ⇒ 逐行读毕：15 条命中里的 brother 全部指 **Thomas（辛西娅之兄）**、husband 全部指 **Hubert（辛西娅之亡夫）**，
     没有一条写 Lachlan 自己的兄弟或配偶。（这条是「命中≠证据」的实例：模式对了，语义全在别处。）
```
⇒ **舅舅（血缘）vs 姨父（姻亲）不裁决**。建议：全书统一为一个**母系**称谓（如「拉克兰姨父」，或含糊处理为「拉克兰长辈」需另议），并在 `.memory/review-ledger.md` 记依据。**本条不在 ch16 判缺陷**——ch16 md 未给 Lachlan 任何中文称谓（词表 `brother` 行只保留了英文例句）。

**另记一条原文自身的不一致（不裁决，不判 md 缺陷）**：Lachlan 是谁的 uncle，原文两处口径不同——
- `ch03:315` `‘…Lachlan, this is my sister we’re talking about.’ Thomas stood directly in front of **her uncle**.`（`her`＝Cynthia ⇒ 辛西娅的叔／姨父）
- `ch16:209` `already **my brother, your uncle**, and now you are dictating where I can go`（辛西娅对海伦娜说 ⇒ 海伦娜的叔／姨父）
若是同一位长辈，辛西娅该说 `our uncle`。md 未涉及此处，**不改**。

### 时序专查（无缺陷）

| md 断言 | 原文顺序 | 结论 |
|---|---|---|
| md:10「吻后 → 管家进来 → 问出地址 → 提议当天去 → '利用'勾起旧事 → 脱口说不愿被利用 → 辛西娅退回客气 → 骤起风雨 → 想起封印松动 → 被劝保持冷静后爆发 → 哈姆雷特去蹭 → 星尘 → 答应同行」 | `:35`–`:53` → `:56`–`:104` → `:113` → `:128`–`:149` → `:155` → `:158`–`:170` → `:209` → `:221` → `:218`→`:233` → `:251` → `:254` → `:269` | **成立**。唯一需注意：`:218`（海伦娜说「保持冷静」）在 `:221`（想起封印松动）**之前**，md:10 的排列把「想起封印」放在「被劝保持冷静后爆发」之前，与原文一致（`:221` 是 `:218` 之后的补叙，仍早于 `:233` 爆发）。 |
| md:14「雷雨跟着辛西娅的情绪走」 | `:209` 起风闪电（辛西娅激怒中）→ `:233` 雷声（吼完）→ `:281` 放晴（她笑了） | **方向成立**，但只写了前半；放晴见 L9。 |

## 四 R4 逐块对应（人判，含固定三问）

| 块 | md 行 | 引语落点 | 中文是在讲这句引语吗 | ①动词主语 ②受事 ③归属方向（回原文核 `by/to/from/of`） | 关键词在引语内 |
|---|---|---|---|---|---|
| 原句 1 | md:18 | `:35` | ✅ | `hexed` 主语＝（无人）／被动；`she described it` 的 she＝**Aunt Rowan**（`When the spell was finally broken, she described it`）→ md「姑妈把那种感觉说成」✅；`Helena felt similarly` → md「觉得自己也差不多」✅ | hexed ✅ / hypnosis ✅ / couch cushions ✅ |
| 原句 2 | md:28 | `:83` | ✅ | `looked from Cynthia to Helena` → md「先看看辛西娅，又看看海伦娜」✅；`I’ve known Georgie` 主语＝Higgins ✅；`It was my doing that got Lily here` → md「正是她自己」✅ | leading strings ✅ / dear friend ✅ / my doing ✅ |
| 原句 3 | md:38 | `:92` | ✅ | `face creased` 主语＝Higgins 的脸 ✅（**但 md 译成「松开」，方向反，见 E9**）；`No need to worry yourself` 的 yourself＝Cynthia（`my lady`）→ md「不必夫人操心」✅ | creased ✅ / kindness ✅ / job prospects ✅ |
| 原句 4 | md:48 | `:137` | ✅ | 全段说话人＝**闪回里的海伦娜**，受话人＝**母亲薇洛** → md「记忆里的海伦娜对母亲说」✅；`He wants / He needs` 的 He＝薇洛身边的男人 ✅；`You are breaking our most sacred oath for him` 的 You＝母亲 ✅ | riches ✅ / power ✅ / sacred oath ✅ |
| 原句 5 | md:58 | `:158` | ✅（**引语截短**：中文理解多讲了 `:158` 前半句「眼睛睁大」，见 E10） | `Used?` 说话人＝Cynthia ✅；`You asked to come with me` 的 You＝**Helena**、me＝Cynthia → md「她以为海伦娜是想帮她，才提出同行」✅ **方向正确，未调转**；`a smile that contradicted the pain there` → md「那笑和眼里的痛对不上」✅ | Used ✅ / investigations ✅ / contradicted ✅ |
| 原句 6 | md:68 | `:209`（3 片段，同段内） | ✅ | `When Aunt Rowan was particularly vexed, there was no telling how **her** connection to the earth would manifest` 的 her＝**Rowan** → md「她与土地的那点牵连」✅；`This felt the same` 主语＝眼前这场风雨 ✅ | lightning ✅ / connection to the earth ✅ / the same ✅ |
| 原句 7 | md:78 | `:221` | ✅ | `Aunt Rowan had warned Helena` → md「罗温姑妈警告过她」✅（称谓见 E1）；`contain Cynthia’s magic` 的受事＝辛西娅的魔法 ✅；`Cynthia was approaching her twenty-eighth year` → md「辛西娅快满二十八岁」✅ **未张冠李戴** | contain ✅ / slipping ✅ / twenty-eighth ✅ |
| 原句 8 | md:88 | `:251` | ✅ | `hopped / wound his way / bumping his head` 主语＝**Hamlet（狐狸，雄性，海伦娜的魔宠）**→ md「哈姆雷特从沙发上轻巧跳下，绕到辛西娅脚边，用头蹭她的腿」✅；`Cynthia looked down … ‘I’m fine.’` 说话人＝Cynthia ✅；`a gesture Helena had made a million times with her familiar` → md「海伦娜对自己的使魔做过千百次」✅；`watching Cynthia seeking comfort from Hamlet` → md「看辛西娅向哈姆雷特讨安慰」✅ **安慰方向正确** | nimbly ✅ / copper fur ✅ / familiar ✅ |
| 原句 9 | md:98 | `:269` | ✅ | 说话人＝**Helena**（`:260` 辛西娅问 `‘Are you saying you’ll come with me?’` → `:269` 海伦娜答）→ md「海伦娜给出答案」✅ **未把答复安到辛西娅头上**；`the bastard who murdered your husband` 的 your＝Cynthia ✅ | Yes, we ✅ / stupid ✅ / alone ✅ |

**对应 9/9。** 施事／归属调转 **0 处**。

**⚠️ 已推翻的子代理主张（不得沿用）**：`1-suread.json` 的 **T17** 断言「`:209` `already my brother, your uncle, and now you are dictating…` ⇒ Lachlan 是 Cynthia 的兄弟、Helena 的叔叔」。**这是错的**——该句是**三项并列**：`my brother`＝Thomas（辛西娅之兄）／`your uncle`＝Lachlan（海伦娜的叔／姨父）／`now you`＝海伦娜。反证：
- `:200` 海伦娜已把两人分开说：`Your brother would have a fit, and Uncle Lachlan will string me up by my toes`
- `ch01:206` `‘Lachlan.’ Her brother’s strangled response`（Thomas 说出 Lachlan 的名字 ⇒ Lachlan 是第三人）
- `ch03:315` `Lachlan, this is my sister we’re talking about.` ＋ 同章 `these old friends`（Thomas 与 Lachlan 是**朋友**，不是兄弟）

⇒ **教训**：R1 可外包，但底稿里的 `traps_noted` / `unresolved_in_source` 是「主张」不是「事实」，R3 起必须逐条回原文核。

## 五 形态

| 项 | 实测 | 本书众数／profile | 结论 |
|---|---|---|---|
| H1 | `# 16. Chapter Sixteen` | 全书 `# NN. Chapter NN(英文序数)` | ✅ |
| 导航子项 | 5（一句话概括／情感弧线位置／Tropes／人物弧线／叙事手法） | 5 | ✅ |
| 引语块数 | 9 | `block_target [5,9]`（2858 词） | ✅ **已触上限**——补 L1/L8 只能改导航或换块，**禁增第 10 块** |
| `block_hint` | `""`（空） | — | ✅ 无提示 |
| 子项集 | 中文理解／关键词／为什么这样写／读者视角提示 ×9 | 同 | ✅ |
| 词表 | 标准 Markdown 表格 `\| 词/短语 \| 释义 \| 例句 \|`，22 条＝8/8/6 | 新判据（`96b7e557e`）要求标准表格 | ✅ |
| 一句话总结 | 有（md:149） | 有 | ✅ |
| frontmatter | `状态: 未读` / `modified: "2026-10-22"` | 同 | ✅ |

**形态 8/8。**

## 六 语料层与引语逐字（实跑）

```
$ bash scripts/chapter.sh "…/ch16 lilys father.md" --json > review/ch16/2-machine.json ; echo $?
0
counts.blocks 9 · counts.words 2858 · block_target [5,9] · block_hint "" · segments 12 · segment_miss 0
form.h1 "16. Chapter Sixteen" · nav_count 5 · issues 9 类全空

$ python3 /tmp/vocab_check_hx.py 16      # 例句是否本章原句
rows=22 missing=0

$ python3 /tmp/vocab_head_hx.py 16       # 词头是否在本章原文
rc=0（无输出）

$ python3 /tmp/pair4_hx.py               # 引号配对
TOTAL 1（唯一一条仍是 ch09 原句7 的孤儿闭引号，与 ch16 无关）

$ python3 scripts/verify_fragments_indep.py "…/the-hexing-miss-helena-by-darcy-mcguire"
引语条数 270 ｜ 受检片段 312 ｜ ❌ MISS 0 ｜ ❌ 拼接未标省略号 0 ｜ 缺参照章 0
```

**原句 6 的 `…` 拼接专项复核**（三片段全部落在 `:209` **同一行**内，两侧均为原词，合法）：

| 片段 | 原文位置 | 前接 | 后接 |
|---|---|---|---|
| `The sky outside darkened … most violently.` | `:209` 中段 | `She put her hand up, staying Helena’s counterargument. ‘I know you mean well. …’` | `‘Society believes women of the peerage…’` |
| `A crack of lightning … white-hot electricity.` | `:209` 中段 | `…never question my place.’` | `Helena glanced out the window and raised a brow.` |
| `She’d seen weather like this. … This felt the same.` | `:209` 行末 | `Helena glanced out the window and raised a brow.` | 段末 |

**语料层「像广告的正文」扫描**：ch16 **零推广行**（Lokepub 三行推广只出现在 ch03/ch08/ch13/ch19/ch25 共 5 章 8 行）。反面陷阱已避开：ch16 无 `I’m in love with a ferret.` 类狐狸心声（那是 ch15:192）。

## 七 不裁决（U）

| 编号 | 事项 | 为什么不裁决 |
|---|---|---|
| U1 | `:80` `‘Lily’s father is George Lippert?’` 的说话人 | **无 tag**。按 `:89`/`:95`/`:101`/`:107` 话轮链判为辛西娅（`Helena’s body tightened as Cynthia sat straighter in her chair` ⇒ 海伦娜因认名而僵、辛西娅因警觉而坐直），md 的读法成立但**不宜写成「追问出」**（见 E5）。 |
| U2 | `:254` 星尘念头的来源 | `:257` 原文自陈 `not sure if the thought came from her own mind or the cosmos` ⇒ **不得武断归属**（见 E14）。 |
| U3 | Lachlan 是舅舅还是姨父 | 见 §三 E1 专节附注，原文未写血缘或姻亲。 |
| U4 | Lady Argyle 是否即 ch15 那位「堂兄之妻」 | `:56` 只给 `Lady Argyle requested`；ch15 那封信未署名。 |
| U5 | `:251` `from the couch` 与 `:44` `She chose a new chair`、`:203` `the chaise where Helena sat` 的家具不一致 | **原文自身**的不一致，md 未涉及，不裁决。 |
| U6 | 希金斯太太与乔治·利珀特的确切关系 | `:83` `I’ve known Georgie since we were little mites in leading strings` ＋ `:86` `A decision I’ll always regret. How can Georgie ever forgive me?` ⇒ 青梅竹马＋自悔，但原文未写更深关系。 |
| U7 | `:284` `‘Then we shall do it together.’` 的说话人 | **无 tag**。按话轮（`:281` 辛西娅刚答完 `Of course I will let you help me`）判为海伦娜；`:284` 后半 `The last word resonated through Helena` 支持这一读法。 |
| U8 | `:290` 海伦娜的自我否认是否会在后章翻转 | ch16 内不裁决；md:11「章末没有告白」写法**正确**（保留了未翻转状态）。 |
