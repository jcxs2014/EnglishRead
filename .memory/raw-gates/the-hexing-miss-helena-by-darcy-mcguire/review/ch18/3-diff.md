# ch18 · R3 对账（三张单子）＋ R4 逐块对应【深审重做，取代 14:47 快审档】

- 素读底稿：`review/ch18/1-suread.json`（**深档**，子代理产出、主会话复核）：源文 398 行／`events 176`／`relationships_noted 16`／`numbers_verbatim 18`／`unresolved_in_source 13`／`traps_noted 55`
- 逐字复核（**主会话用自己的尺子重跑**，不复用代理的结论）：按 `…` 拆片段后 `frag-checked 213 · BAD 0`。未拆片段时 5 条不匹配，全部是 `relationships_noted` 里**用 `…` 连接两行**的合法省略（`:56+:62`／`:74+:236`／`:161+:227`／`:77+:284`／`:323+:362`），拆开后逐条命中 ⇒ **底稿逐字层无损**。
- 机器层：`chapter.sh --json` rc=0；`blocks 13`／`words 3577`／`block_target [7,11]`／**`block_hint`「块数 13 偏离本章篇幅建议 7–11」**／`segments 13`／`segment_miss 0`／`h1 "18. Chapter Eighteen"`／`nav_count 5`／issues 9 类全空
- md：`ch18 the lippert house.md`（192 行；**13 引语块**；词表 24 条＝9/9/6）
- 词表层：`/tmp/vocab_check_hx.py 18` → `rows=24 missing=0`；`/tmp/vocab_head_hx.py 18` → rc=0
- **读取顺序**：主会话本轮**先通读 `text/ch18_chapter_18.txt` 全 398 行**，再开 md。铁律未破。
- ⚠️ **块数 13 已超 `block_target` 上限 11 ⇒ 禁增第 14 块**；本章所有补漏只能写进导航 5 行。

## 〇 结构要点

1. 正文 `:35`–`:398`；`:1`–`:34` 是提取件排版（`:1` `Chapter 18`、`:22` 孤立页码 `18`、其余空行）。**本章零推广行**（Lokepub 推广只在 ch03/ch08/ch13/ch19/ch25）。
2. POV **全程贴 Helena**，第三人称限知，无视角换人。三处无引号独白（`:140` `She’s the very Devil!`／`:152` `What can she possibly know?`／`:164` `Damnation!`）**全部属于 George Lippert**，因 Helena 读心而被「听见」（`:143` `Fear amplified his thoughts, making them easy to hear.`／`:161` `as Helena sank deeper into his mind`）⇒ **不构成视角切换**。
3. **动物无直接心声**：`:323` `The poor thing must have been terrified` 是 Helena 的推测；`:326` `‘He was worried for us,’` 是 Cynthia 的转述（正是这句让她说漏，见 T41）。
4. 两个空间：利珀特家（`:35`–`:302`）→ 门外街上＋回程马车（`:305`–`:398`）。原文无场景分隔符。
5. **本章洗清 Lippert 的嫌疑**：`:161` `Not because he had taken a man’s life. But because he hadn’t.` ＋ `:167` `despised himself for being too late to kill Hubert Burrows.`
6. **`Hamlet` 是狐狸（Helena 的），`:350` `that dog in front of the carriage` 是另一只动物、且发生在 ch17**（T40）——两者不得混同。
7. `:209` `‘That isn’t⁠—’` 与 `:239` `‘Lady Burrows⁠—’` 都在破折号处被打断，且破折号前藏有不可见 U+2060（T22）⇒ **不得当完整台词引用**。

## 一 「漏」——素读有、md 无

> 本章 3577 词、13 块，是本书至今最长的一章；覆盖缺口集中在**马车后半**与**利珀特家的肢体／谈判节拍**。

| 编号 | 原文（`text/ch18:行`） | 为什么重要 | 档 |
|---|---|---|---|
| **L1** | `:191` `Lippert froze and blinked several times. **A name surfaced in his mind.** As clear as a shiny penny glinting at the bottom of a wishing well. **But it was impossible.**` ＋ `:194` `‘I ’aven’t a clue.’` ＋ `:197` `‘You’re lying.’ Helena’s words carried the bite of conviction.` | **海伦娜读到了那个名字**，而且当场判断「不可能」；名字全书未揭晓（U2）。md:10 只写「他嘴硬不说那晚进书房的人是谁」，把「她读到了、且认为不可能」这层**整个抹掉**——本章通往真凶的唯一线索因此消失。 | **阻断** |
| **L2** | `:371` `I can’t.` → `:374` `But she was moving before she knew it, taking Cynthia’s opposite side. It was a tight fit, but it gave her an excuse to rest her hand on Cynthia’s leg and gently squeeze her thigh through layers of silk and linen.` | **本章最重要的口是心非节拍**（T48）：心声拒绝、身体先动，还给自己找了个「借口」。md:13 只写「感情从维护变成承认」，md:136 只写「读者已经知道她为什么一路躲」，**这个动作全篇未收**。 | **阻断** |
| L3 | `:47` `‘I’m so sorry, Lady Burrows. I didn’t know how to tell ye.’`（**无说话人 tag**，从方言 `ye` 与 `:50` Lippert 随即反驳可定为 Lily） | 莉莉主动向女主人坦白；md 未提（T1） | 提示 |
| L4 | `:56` `She would kill George Lippert before she let him put a hand on **her woman**.` → `:62` `Do no harm. I made an oath. And **she isn’t my woman**.` | 承认→**三行内自我否认**（T3）。md:13 写「感情从维护变成承认」，收了这个否认才不至于把两人写成已确认关系。词表 `oath` 行用了 `:62` 作例句，分析层却没碰 | 提示（重） |
| L5 | `:116` `He **grabbed Cynthia’s hands and wrenched them from his daughter’s**. ‘Leave me girl alone.’ He leaned closer, **his finger jabbing into her chest** with blunt force.` ＋ `:119` `Cynthia stepped back, rubbing where his finger had poked.` | 冲突升级为**肢体接触**（T10/T11：扯开的是辛西娅握着莉莉的手、戳的是辛西娅的胸口）；md 全篇未提 | 提示 |
| L6 | `:137` `Whatever he saw in her face caused his cheeks to pale from ruddy red to ghostly white.` ＋ `:140` `She’s the very Devil!` ＋ `:143` `Fear amplified his thoughts, making them easy to hear.` | md:14 只笼统写「读心让她拿到利珀特没说出口的话」；**恐惧让心思易读**这条机制与「他就是魔鬼」这句都没收（T5） | 提示 |
| L7 | `:182` `‘Father!’ Lily lunged for his arm, but he **shook his daughter off like a rabid dog**` | 喻体是「像甩掉疯狗那样甩开女儿」（T17），不是把莉莉比作狗；md 未提 | 提示 |
| L8 | `:185` `‘…**Help us find Hubert’s killer, and we will leave here and never return.**’` ＋ `:188` `Cynthia stiffened.` | **海伦娜开出的交易条件**＋辛西娅的僵硬（T18：条件是 Helena 开的，僵硬说明她不愿走）；md 未提 | 提示（重） |
| L9 | `:203` `‘At least tell us how you got into his office. **Superintendent MacDougal’s men questioned all of the staff. No one recalls Hubert meeting with anyone that morning.**’` | 案情信息（麦克杜格尔的人问遍仆役、没人记得那天早上有人来访）；也是逼问者是**辛西娅**、不是海伦娜的证据（T20）。md 未提 | 提示 |
| L10 | `:206` 后半 `Too busy chasing after the innocent girls you put before ’im. **Like a lion tamer feeding ’er beast, you were.** Kept ’is attentions busy on ’elpless chits like my Lily while you swanned off to yer next damned ball or salon.` | 本章最狠的一句指控（把辛西娅比作喂兽的驯狮人，T21 比喻方向）；md 原句 9 只引了前半段 | 提示 |
| L11 | `:212` `‘Speak to her that way again, and you won’t need to worry about your neck winding up in the hangman’s noose. **I’ll break it myself** and save the courts having to decide if you’re innocent or guilty.’` | 海伦娜**说出口**的威胁（前面几次都只在心里）；与「两次杀意」的计数直接相关（见 §三 E2） | 提示（重） |
| L12 | `:236` `Cynthia straightened her spine, **transforming before Helena’s eyes into Marchioness Kentmore**. ‘You were my employee, and an excellent one at that. It is well within my rights to give you a parting gift. My husband granted me a **substantial living** upon his death. A portion of that money will be set aside for your child.’` | 钱的**具体来源与形式**、以及她此刻**主动披上头衔**（T28）；md:10 只写「提出给孩子一笔钱」 | 提示 |
| L13 | `:251` `George Lippert crossed his arms over his chest, **ignoring the slap his daughter landed on his right shoulder**.` | 莉莉打了父亲右肩一巴掌、父亲无视（T30）；md 未提 | 提示 |
| L14 | `:254` `She took Cynthia’s hands. ‘We should leave.’` → `:257` `**But Cynthia pulled back as Helena tried to tug her towards the door. She wouldn’t turn away from George Lippert.**` | 一个想走、一个不肯转身（T32 动作方向）；md 未提 | 提示（重） |
| L15 | `:263` `Helena ached to ease her suffering almost as fiercely as she wished to **funnel a stream of water at George Lippert’s face until he begged for mercy**. But all she could do was hold her hand` ＋ `:269` `**If they were alone, she would have caught the tear** that fell and let it sink past her skin and into her veins, absorbing Cynthia’s sorrow as her own.` | 又一次水的暴力冲动；以及**虚拟语气**的「接泪入血」（T33：没发生）——这是水巫吸收他人悲伤的设定 | 提示（重） |
| L16 | `:266` `‘When it came to my husband, I learned early and well that **life was far more pleasant if I didn’t ask any questions or make any demands. For myself or others.**’` | 辛西娅十年沉默的**自陈机制**，是她整条弧线的根；md 未提 | 提示（重） |
| L17 | `:275` `**If only Helena had the ability to put thoughts in other people’s minds instead of snatching them out.** … In lieu of that, she was seriously **contemplating hexing the man, regardless of her oath to do no harm**.` | 明确排除「和解是魔法胁迫」的误读（T34：她只能读取、不能植入；下咒也只是「考虑」）；md 未提 | 提示（重） |
| L18 | `:323`–`:341`：`Hamlet yipped at Helena, nearly bowling her over as he leapt … into her lap` → `:326` `‘**He was worried for us**,’ Cynthia said before **pressing her lips together as if she might somehow recall her words**.` → `:329` `‘**Did he tell you that?**’` → `:332` `Drat. This is hardly the right time to confront her with her powers.` → `:338` `‘Never mind.’` → `:341` `‘…You accuse me of being able to, what? **Speak to your fox?** I would be a lunatic if I thought I could communicate with animals.’` | **说漏→追问→撤回→断然否认**这条完整节拍（T41 `recall`＝收回话语；T43 反事实条件句）。md:10 只写「辛西娅否认自己有任何魔法」，**丢掉了她是先说漏才否认的** | 提示（重） |
| L19 | `:350` `‘You were magnificent with that dog in front of the carriage. **If you don’t believe you have magic running through your veins, explain that moment to me.**’` → `:353` `Cynthia **opened her mouth, shut it, opened it again**, and tears filled her eyes … ‘**I don’t know what that was.**’` | 海伦娜的正面逼问与辛西娅三次张嘴说不出话（T44：`that moment` 指 ch17 的狗，不在本章） | 提示 |
| L20 | `:362` `She whispered into his pointed ear. ‘**Go on.**’` → `:365` `he **bumped his head against her cheek** before nimbly hopping from one side of the carriage to the other, **making three tight circles** and settling himself in the snug space between the right side of the carriage and **Cynthia’s black skirts**.` | 哈姆雷特是**受命**去安慰的（T47 时序固定：蹭脸颊→跳过去→转三圈→卧在裙边）；md:10「海伦娜一边安慰她」把这层代理安慰抹掉了 | 提示 |
| L21 | `:377` `**I’m just being a friend. There’s no harm in being a friend.**` → `:380` `Cynthia held herself stiff for a moment before **slowly sliding down on the seat until her head rested on Helena’s shoulder**.` | 自我说服的心声（叙述不背书，T49）＋**辛西娅主动靠上去**；md 未提 | 提示（重） |
| L22 | `:380` `**Vanilla and honeysuckle blended with bergamot and lemon.**` | 无主语气味句（T50：是辛西娅靠肩后海伦娜闻到的）。⚠️ `honeysuckle` 是**全书术语争议词**（ch06 译「忍冬」／ch07、ch25 译「金银花」），本章 md 未译，一旦补写必须先定统一译名 | 提示 |
| L23 | `:383` `‘**It isn’t your fault**, you know. What your husband did to Lily.’ **Helena** turned so she could rest her chin on top of Cynthia’s head.` → `:386` `‘**How many girls did he abuse, Helena?** How many innocent women were hurt in my house while I fussed over my gowns and fripperies?’` → `:392` `‘**I expect me to know.** I’ve always thought myself rather clever, but I’m not. **I’m the world’s biggest fool.**’` | **安慰方向**（T51：是海伦娜安慰辛西娅，不是反过来）＋辛西娅的自贬（T52 `me`＝myself）；md 未提 | 提示（重） |
| L24 | `:395` `Instead, she let her body warm Cynthia’s. She let the quiet soothe her. **She funnelled her power and poured it over Cynthia in waves of comfort.** And **kept her thoughts well away from what any of this meant**.` | 安慰是**用魔法做的**（T53 施动者全是 Helena），且她刻意不去想这意味着什么；md:10「一边安慰她」没写出这两层 | 提示 |
| L25 | `:305` `Helena kept a wary gaze on Lippert as she led the way out … **she breathed a sigh of relief**.` ＋ `:308` `‘That could have been better, but it also could have been far worse.’` ＋ `:311` `**Cynthia didn’t answer.** She stared at the street …` ＋ `:314` `**What I wouldn’t give to hear her thoughts.**` ＋ `:317` `It was becoming a **constant refrain** whenever they were together.` | 出门后松一口气与那句总结都是**海伦娜**的（T38），辛西娅此刻沉默出神；「读不到她的心思」已成两人相处时的固定念头——这是本章后半的情感底色，md 未提 | 提示（重） |

> **L1／L2 为什么是阻断**：本章的两条主线各有一个决定性节拍被漏掉。案件线——海伦娜**读到了名字**并判断「不可能」（L1），md 写成「他嘴硬不说」，把「她知道、读者不知道」这个悬念结构改成「他藏着」；感情线——`I can’t.`／`But she was moving before she knew it`（L2）是全书「口是心非」母题在本章的落点，md:13 的「承认」少了它就悬空。均属 S1「漏掉关键转折」。
> **修复位置**：块数 13 已**超**上限 11 ⇒ **禁增第 14 块**，L1 写进 md:10，L2 写进 md:13。

## 二 「编」——md 有、原文无

**0 条独立凭空项。** 排查后**不成立**的疑点（逐条留证）：

| md 位置 | 疑点 | 回原文结论 |
|---|---|---|
| md:10 | 「利珀特骂辛西娅是婊子」 | **成立**。`:50` `‘You owe this bitch nothing!’ Lippert **spat the words at Cynthia**.`（骂的对象是辛西娅，**不是海伦娜**——T2 未踩） |
| md:10 | 「莉莉挡在父亲和女主人之间」 | **成立**。`:74` `‘Father, sit down.’` ／ `:215` `‘Enough!’ … She turned to her father … She turned to Helena. ‘And you stop threatening my father.’` ／ `:218` |
| md:10 | 「辛西娅把休伯特的罪揽到自己十年没看见上」 | **成立**。`:89` `‘Or even see what was right under my nose the whole **ten bloody years** I was married to such an evil creature.’` |
| md:10 | 「读利珀特的心，发现他恨的是自己没赶上亲手杀休伯特——他到过现场，只看见尸体」 | **成立**。`:161` `Not because he had taken a man’s life. But because he hadn’t.` ／ `:167` `despised himself for being **too late to kill** Hubert Burrows.` ／ `:170` 画面里休伯特**已死**（T14/T15 双双未踩） |
| md:10 | 「最后为'让休伯特在坟里不得安生'收下钱」 | **成立**。`:284` `But only because I’ll know **the bastard is rolling over in ’is grave** with every penny of ’is that lines our pockets.`（`the bastard`＝休伯特，T35 未踩） |
| md:10 | 「回程马车上，辛西娅否认自己有任何魔法」 | **成立**。`:341` `I would be a lunatic if I thought I could communicate with animals.` ／ `:347` `There is nothing magical about me.` |
| md:10 | 「海伦娜…承认这个女人让她动心，而爱对她太危险」 | **成立**。`:359` `Cynthia Burrows was the kind of woman she could give her heart to. And that was impossible for Helena. This day had reminded her why **love was dangerous for her**.` |
| md:11 | 「接上一章门前的恶心」 | **成立**。ch17 `:254` `Nausea washed through her.` 是上一章最后一句 |
| md:11 | 「这一章从进门就被敌意包围」 | **成立**。`:50`／`:77`／`:116`／`:251` |
| md:12 | 「以为凶手是利珀特」 | **成立**（但**未标出是谁以为**，见 §三 E11）。`:41` `They still needed to determine if George had killed Hubert.` ／ `:38` `Helena would be more surprised if Lippert **hadn’t** tried to kill Hubert.` |
| md:12 | 「嘴硬心软的底层父亲」 | **成立**。`:224` `A better father would ’ave killed ’im fer what ’e did to you.` ／ `:227` `he wrapped his burly arms around her tightly` ／ `:182` `his mind screaming at him not to frighten Lily` |
| md:12 | 「反转有三处」 | **成立**（md 自己逐条列出，可自证） |
| md:13 | 「海伦娜…再被自己的念头吓到」 | **成立**。`:125` `Dear goddess, I’m becoming just like her.`（`her`＝**母亲**，`:128` `her mother’s sickness` 为证，T4 未踩） |
| md:14 | 「全章贴海伦娜的限知，读心让她拿到利珀特没说出口的话」 | **成立**。`:143`／`:161`；三处无引号独白都归 Lippert（T5 未踩） |
| md:14 | 「两次杀意都借水的意象（球、矛、浪）」 | 意象**成立**：`:53` 球＋矛／`:212` 浪；但**「两次」这个计数错**（见 §三 E2） |
| md:14 | 「章末从对话转为马车里的静，最后用两句内心话收尾」 | **成立**。`:395` 起无对话；`:398` 恰为两句（`But Helena was in no place…` ／ `What a pair they made.`）＝md 原句 13 |
| md:14 | 「不写辛西娅的反应」 | **成立**。`:392` 是辛西娅最后一句话，此后 `:395`–`:398` 全是海伦娜 |
| md:191 | 「也暗示那晚有人自己开门进了书房」 | **成立且 hedge 得当**（「暗示」）——但 md:104 把同一件事写成「把一条线索说漏了」，两处口径不一（见 §三 E5/E6） |
| md:24 | 「作者不站出来评论，读者自己会算」 | **成立**。`:35` 是描述（`at least two of George Lippert’s many children`），不是叙述者评论 |
| md:96 | 「这幅画面是利珀特记忆里的现场，不是海伦娜亲眼所见；它能证明他到过那里，不能证明人是他杀的」 | **成立且是本章最准确的一句读者提示**（`:170` `pulled from Lippert’s thoughts`） |

## 三 「错」——两边都有但不一致

| 编号 | md 位置 | md 原文 | 原文依据（逐字） | 档 |
|---|---|---|---|---|
| **E1** | md:136 | 「这是海伦娜**第一次**在心里把'爱'这个字和自己、和辛西娅放在一起。」 | `ch16:179` `But I’m **not falling in love with Cynthia**. I admire her. I find her fascinating. … But that is all. That is not love.` ／ `ch16:176` `A private promise to **never fall in love with another**.` ／ `ch16:290` `She didn’t have time to worry about **falling in love with a witch**…` ⇒ 上一章已三次把「爱＋自己＋辛西娅」放在一起（且是**否认式**）。 | **阻断**（跨章「第一次」断言被证伪） |
| **E2** | md:10／md:11／md:14 | 「海伦娜**两次**动了杀心又用誓言压住」／「保护欲**两次**滑到杀意」／「**两次**杀意都借水的意象（球、矛、浪）」 | 水的暴力冲动实测**至少 5 次**：`:53` `that sphere could turn into a **spear** of water that would **cleave Lippert in two**`／`:80` `intent on **throwing a water spear right through George Lippert’s heart**`／`:122` `it would only take **a flick of her wrists to destroy this man**. **Water** brought life, but it could also herald death.`／`:212` `Helena’s rage reared once more like a **rogue wave**, ready to **ram him**`／`:263` `she wished to **funnel a stream of water at George Lippert’s face until he begged for mercy**`；另加非水的 `:212` `**I’ll break it myself**` 与 `:275` `contemplating **hexing** the man`。**md:66 自己就承认了第三次**（「紧接着她仍想到'只要一挥手就能毁掉这个人'」＝`:122`）⇒ md 内部自相矛盾。 | **阻断**（计数） |
| **E3** | md:13 | 「辛西娅从被骂到**自辩**，再把责任说清、把补偿给出；她**没有求原谅**，只请求对方让她做事。」 | ①「自辩」被证伪：`:83` `‘Don’t.’ She exhaled a shaky breath. ‘**He’s right.**’` ／ `:260` `‘**You are right, sir.** I should have known what was going on in the hallways and rooms of my own house.’` ⇒ 她**两次认下指控**，没有自辩。②「没有求原谅」被证伪：`:89` `‘**Please forgive me.** I should have known. I should have stopped him.’`（对莉莉说的，就在 md 原句 4 所引 `:89` 同一段的三行之后）。 | **阻断**（否定断言＋章级内容断言双双被原文证伪） |
| **E4** | md:84 | 「**三个短句**把反转拆开…**最后半句只有三个词**」 | md:88 引语自身即可量化：`But as Helena sank deeper into his mind, it was hatred for himself that eclipsed all else.`＝**17 词**（不是短句）／`Not because he had taken a man’s life.`＝**8 词**／`But because he hadn’t.`＝**4 词**（不是 3 词）。 | **阻断**（形式断言被 md 自身引语量化证伪，判据 f） |
| E5 | md:104 | 「话里带着讥讽，却也**把一条线索说漏了**：那晚有人进过书房，而且是休伯特不想让家里人看见的人。」 | `:206` `Answered the door ’imself, **I’ll bet**.` ⇒ 是乔治的**猜测**，不是他目击的事实（T21）；且 `:203` 的口径是 `No one recalls Hubert meeting with anyone **that morning**`（那天早上）⇒ 「那晚」不得写成已确认的时间。 | 提示（重） |
| E6 | md:106 | 「读者要抓住'半夜''自己开门''不想让家里人知道'**这三个点**，它们比他的脏话更有用。」 | 同 E5：三个点全部出自 `I’ll bet`／`Didn’t want…` 的推测句。**md:191 自己写的是「暗示」**，两处口径不一。 | 提示 |
| E7 | md:116 | 「她不让父亲把辛西娅当仇人，**也不让海伦娜把父亲当凶手**。」 | `:185` `**I don’t think you killed him, George.** But I’m guessing you have a good idea who might have done the deed.` ⇒ 海伦娜**早已明说不认为他是凶手**；莉莉 `:215` 对她那句是 `‘And you stop **threatening** my father.’` | 提示 |
| E8 | md:11 | 「章末转成**海伦娜对自己的恐惧**。」 | `:398` 是自省＋自嘲（`But Helena was in no place to tell her such things when she wasn’t facing her own set of uncomfortable truths. **What a pair they made.**`）；「恐惧」在 `:359`（`Two things Helena was **scared** to provide`／`why love was **dangerous**`），不在章末。**md:144 自己写的是「半自嘲」**⇒ md 内部口径不一。 | 提示 |
| E9 | md:11 | 「场景**以利珀特收钱收束**。」 | 收钱在 `:284`；其后还有 `:290` `I shall have my **man of business** visit you next week`／`:293`–`:296` 辛西娅与莉莉的告别／`:299` 拳手挨拳的比喻／`:302` `‘I think it is time for us to leave.’` ⇒ 场景收在**两个女人的告别**上。 | 提示 |
| E10 | md:126 | 「这是她这一章里**最不像侯爵夫人**的一刻。」 | `:236` `Cynthia straightened her spine, **transforming before Helena’s eyes into Marchioness Kentmore**. ‘…It is **well within my rights** to give you a parting gift.’` ⇒ 恰恰是在开这个条件时她**主动披上头衔**（T28）。 | 提示 |
| E11 | md:12 | 「**以为凶手是利珀特**，读心却证明他没能下手」 | 未标出**是谁**以为。`:41` 是「她们仍需查明」，`:38` 是海伦娜的推断（`Helena would be more surprised if Lippert hadn’t tried to kill Hubert.`）⇒ 应写成「她们此来就是要查明利珀特是不是凶手」，否则读者会以为是警方结论。 | 提示 |
| E12 | md:24 | 「一个动作交代了**谁在主导、谁在犹豫**」 | 引语（`:35`）里只有 `pushing her into the dingy room`；**「犹豫」在引语内无据**（辛西娅的迟疑要到 `:257` `Cynthia pulled back` 才有动作）。 | 提示（S3 分析层伸手到引语之外） |
| E13 | md:36 | 「注意她的手留在背后——**她不想让辛西娅看见**自己准备做什么。」 | `:53` 只写 `kept it behind her back`；**动机是补写的**（原文未写她怕被辛西娅看见）。 | 提示 |
| E14 | md:46 | 「莉莉是这间屋里**唯一**同时握着两边的人；她的证词…**也让利珀特的怒气失去一半理由**。」 | 「唯一」是全称断言：海伦娜同样站在两边之间（`:65` 替辛西娅立规矩、`:215` 被莉莉反过来制止）；「一半」是凭空数量，原文无任何比例表述。 | 提示 |
| E15 | md:64 | 「**前面刚写**她想象水矛劈人，这里立刻搬出身份和誓言」 | 水矛劈人在 `:53`、穿心在 `:80`；紧邻 `:122` 三句之前的是 `:116`–`:119`（扯手、戳胸口、退后揉胸口）⇒ 「刚写」不准（隔 42／69 行）。**md:66 说的「紧接着她仍想到…」（`:122` 后半）才是准确的方位。** | 提示 |
| E16 | md:174（词表） | `hissed` 释义「**压低声音怒斥**」，例句 `:86` `‘You didn’t do this,’ she hissed, **willing Cynthia to listen to reason**.` | 此处是**咬着牙劝**（T7：`she`＝Helena），不是怒斥；释义与例句语境不合。建议改「（因愤怒或急切）咬着牙低声说」。 | 提示 |
| E17 | md:155／md:161（词表） | `sympathise`、`admirable` 放 ⭐⭐⭐ **高级** | 两词的频率与难度都属进阶（`sympathise` 是常见动词、`admirable` 是 `admire` 的常规派生）⇒ **档位注水**（S4 ③） | 提示 |

### 时序专查（无缺陷）

| md 断言 | 原文顺序 | 结论 |
|---|---|---|
| md:10「进门→骂→杀心→莉莉挡→辛西娅揽罪→提钱→读心→嘴硬→收钱→回程马车→否认魔法→安慰＋承认动心」 | `:35`→`:50`→`:53`→`:74`→`:83`/`:89`→`:113`→`:161`/`:170`→`:194`→`:284`→`:305`/`:323`→`:341`/`:347`→`:359`/`:395` | **成立** |
| md:11「从对峙降到疲惫的依偎」 | `:284` 收钱 → `:305` 出门松口气 → `:323` 哈姆雷特跳怀 → `:380` 头靠肩 | **成立** |
| md:12「利珀特收钱不是为了和解」 | `:116` 第一次拒绝 → `:251` 第二次拒绝（措辞不同，T30）→ `:284` 接受并给出理由 | **成立**；**两次拒绝不得合并** |
| md:14「章末从对话转为马车里的静」 | 最后一句对话是 `:392`；`:395`–`:398` 无对话 | **成立**（实测） |

## 四 R4 逐块对应（人判，含固定三问）

| 块 | md 行 | 引语落点 | 中文是在讲这句引语吗 | ①动词主语 ②受事 ③归属方向 | 关键词在引语内 |
|---|---|---|---|---|---|
| 原句 1 | md:18 | `:35` | ✅（「犹豫」越界见 E12） | `put her hand / pushing` 主语＝**Helena** → md:20「海伦娜把手放在辛西娅后腰，把她推进」✅；`served as … bedroom for at least two of George Lippert’s many children` → md:20「至少是利珀特两个孩子的卧室」✅ **未写成「利珀特有两个孩子」** | small of Cynthia’s back ✅／dingy ✅／at least two ✅ |
| 原句 2 | md:28 | `:53` | ✅ | `felt her power swell` 主语＝Helena ✅；`dropped her hand from **Cynthia’s waist**` → md:30「把手从辛西娅腰间收回」✅ **未调转**；`cleave **Lippert** in two` 的受事＝Lippert → md:30「把利珀特劈成两半」✅ | power swell ✅／sphere ✅／spear ✅／cleave ✅ |
| 原句 3 | md:38 | `:74` | ✅ | 说话人＝**Lily**（`‘Father, sit down.’ Lily frowned at Lippert`）→ md:40 归属正确 ✅；`gripped **his** arm` 的 his＝Lippert → md:40「抓住他的胳膊」✅；`none of **her** doing` 的 her＝Lady Burrows → md:40「跟她无关」✅ | sit down ✅／small frame ✅／kind ✅／none of her doing ✅ |
| 原句 4 | md:48 | `:89` | ✅ | `A bitter laugh shook **Cynthia’s chest**` → md:50「震着辛西娅的胸口」✅；`I was married` 的 I＝Cynthia（T8）→ md:50「我跟这么个恶东西过了整整十年」✅ **未误挂海伦娜**；md:54「她不去接海伦娜'你没做'的安慰」✅ **`:86` 的 `she hissed` 正确归 Helena（T7 未踩）** | Nor did I stop it ✅／bitter laugh ✅／under my nose ✅／ten bloody years ✅ |
| 原句 5 | md:58 | `:122` | ✅（「前面刚写」方位不准见 E15） | 三句主语全＝Helena ✅；`an oath with **her coven**` → md:60「与巫团立誓」✅；md:66「紧接着她仍想到'只要一挥手就能毁掉这个人'」✅ 施动者＝Helena（T12 未踩） | light witch ✅／violence ✅／oath ✅／do no harm ✅ |
| 原句 6 | md:68 | `:128` | ✅ | `**she** felt **her mother’s** sickness` → md:70「母亲那种病」✅ **T4 未踩**（不是辛西娅、不是莉莉）；`the **second** time in as many hours` → md:70「两小时内第二次」✅ **T13 未踩**；`twist **her** magic` 的 her＝Helena ✅ | mother’s sickness ✅／cruel and lethal ✅／destroying Lippert ✅／hideous mess ✅ |
| 原句 7 | md:78 | `:161` | ✅（词数错见 E4） | `as **Helena** sank deeper into **his** mind` → md:80「海伦娜更深地探进他的脑子」✅；`hatred for **himself**` 的 himself＝Lippert → md:80「他对自己的恨」✅；`Not because **he** had taken a man’s life. But because **he** hadn’t.` → md:80「不是因为他杀了人，而是因为他没杀成」✅ **T14 双重否定未读反** | sank deeper ✅／hatred for himself ✅／eclipsed ✅／he hadn’t ✅ |
| 原句 8 | md:88 | `:170` | ✅ | `An image flashed, **pulled from Lippert’s thoughts**` → md:90「从利珀特的脑子里闪出来」✅ **T15 未踩**（不是叙述者回放、不是行凶画面）；`**Lippert** cursed God for denying **him** the chance` → md:90「利珀特在骂上帝，怪它不给自己亲手复仇的机会」✅ | image flashed ✅／dark-red halo ✅／cursed God ✅／justified vengeance ✅ |
| 原句 9 | md:98 | `:206` | ✅（把猜测写成线索见 E5/E6） | 说话人＝**Lippert**（`:206` `A small, smug smile curled **his** lips.`）→ md:104「他不直接回答，先反问」✅；`Answered the door ’imself` 的省略主语＝**Hubert**（T21）→ md:100「八成是自己开的门」✅ **未误读成乔治开门**；`’is fine ’ousehold` ＝ Hubert 的宅子 ✅ | dead o’ the night ✅／answered the door ✅／’is fine ’ousehold ✅／company ’e kept ✅ |
| 原句 10 | md:108 | `:215` | ✅（第二个听话人写错见 E7） | 说话人＝**Lily** ✅；`**Lily’s** soft voice … when **it** finally rose in anger` → md:110「莉莉的声音轻，可一旦真的发火」✅；`She turned to **her father**` → md:110「她转向父亲」✅ **T23 两个听话人只写对一个** | Enough ✅／rose in anger ✅／not each other’s enemies ✅／pointing a finger ✅ |
| 原句 11 | md:118 | `:272` | ✅ | 说话人＝**Cynthia**（`:272` `Sniffing, **Cynthia** cleared her throat and continued`）→ md:120 归属正确 ✅；`I should have been better, and **I wasn’t**` → md:120「可我没有」✅ | braver ✅／better ✅／wasn’t ✅／better now ✅ |
| 原句 12 | md:128 | `:359` | ✅（「第一次」跨章错见 E1） | `**she** could give **her heart** to` 的两个 she/her 都＝Helena → md:130「她可以把心交出去的女人」✅ **未调转**；`impossible for **Helena**` → md:130「对海伦娜来说不可能」✅；`love was dangerous for **her**` 的 her＝Helena ✅ | give her heart ✅／impossible ✅／love was dangerous ✅ |
| 原句 13 | md:138 | `:398` | ✅ | `when **she** wasn’t facing **her own** set of uncomfortable truths` 的 she/her＝**Helena**（T54）→ md:140「海伦娜自己也没面对那些不舒服的真相」✅ **未安到辛西娅头上**；`What a pair they made` 是 Helena 的总评 → md:140「这两个人凑在一起，真是绝配」✅ | uncomfortable truths ✅／What a pair ✅ |

**对应 13/13。** 施事／归属调转 **0 处**。本章最高危的五处——`:86` `she hissed` 是谁（T7）／`:125` `just like her` 的 her 是谁（T4）／`:161` 双重否定的方向（T14）／`:206` `Answered the door ’imself` 的省略主语（T21）／`:398` 结尾自省的归属（T54）——**md 全部未踩**。

## 五 形态

| 项 | 实测 | 本书众数／profile | 结论 |
|---|---|---|---|
| H1 | `# 18. Chapter Eighteen` | `# NN. Chapter NN(英文序数)` | ✅ |
| 导航子项 | 5 | 5 | ✅ |
| 引语块数 | **13** | `block_target [7,11]`（3577 词）；本书众数 9–13 | ⚠️ **提示**——`block_hint` 已报偏离，rc 仍 0。判提示不判阻断：13 块与本书最长几章同量级。**但⇒ 禁增第 14 块，L1/L2 只能进导航。** |
| 子项集 | 中文理解／关键词／为什么这样写／读者视角提示 ×13 | 同 | ✅ |
| 词表 | 标准 Markdown 表格 `\| 词/短语 \| 释义 \| 例句 \|`，24 条＝9/9/6 | 新判据（`96b7e557e`） | ✅ |
| 一句话总结 | 有（md:191） | 有 | ✅ |
| frontmatter | `状态: 未读` / `modified: "2026-10-23"` | 同 | ✅ |
| `…` 拼接 | 13 块全为单段连续引语，`segment_miss 0` | — | ✅ |
| 破折号截断句 | 未引用 `:209`／`:239`（含 U+2060） | — | ✅（T22 未踩） |

**形态 8/9**（块数 1 项为提示型偏离，已给理由）。

## 六 语料层与跨章核实（实跑）

```
$ bash scripts/chapter.sh "…/ch18 the lippert house.md" --json ; echo $?
0     blocks 13 · words 3577 · block_target [7,11] · block_hint「块数 13 偏离本章篇幅建议 7–11」· segments 13 · segment_miss 0 · issues 9 类全空

$ python3 /tmp/vocab_check_hx.py 18      →  ch18: rows=24 missing=0   rc=0
$ python3 /tmp/vocab_head_hx.py 18       →  （无输出）                rc=0
```

**词表 24 条例句逐条抽核（行号）**：`terminated:38`／`sympathise:53`／`marchioness:65`／`grievously:101`／`infatuated:131`／`intimidated:185`／`substantial:236`／`admirable:203`／`contemplating:275`／`monstrous:38`／`scuttling:38`／`determine:41`／`flinched:200`／`smug:191`／`leashed:176`／`hissed:86`／`shrewd:278`／`hysterical:347`／`oath:62`／`rage:110`／`carriage:305`／`tear:269`／`money:236`／`father:227`。

**语料层「像广告的正文」扫描**：ch18 **零推广行**（全书推广行只在 ch03:188／ch08:170,173／ch13:182,185／ch19:194,197／ch25:214）。

**E1 跨章取证（实跑）**：
```
$ /usr/bin/grep -nEi 'fall(ing)? in love|in love with' text/ch01*.txt … text/ch17*.txt ; rc=0（5 行，逐行读毕）
ch13:176  Clara was in love with the stable master’s son.   ← 与 Helena 无关
ch15:192  I’m in love with a ferret.                        ← 反面陷阱（Clio 的玩笑）
ch16:176  A private promise to never fall in love with another.        ★
ch16:179  But I’m not falling in love with Cynthia. … That is not love. ★
ch16:290  She didn’t have time to worry about falling in love with a witch… ★
```
⇒ **md:136 的「第一次」被 ch16 三处证伪**（其中 `:179` 是同一主体、同一对象、同一「在心里」的形态）。

## 七 不裁决（U1–U13，取自素读底稿并经主会话逐条回原文核）

| 编号 | 事项 | 为什么不裁决 |
|---|---|---|
| U1 | 莉莉腹中孩子的父亲身份 | 只有 Lippert 的指控（`:77`）与 Helena 的推断（`:38`），**莉莉本人始终没有正面确认** ⇒ md 不得写实 |
| U2 | `:191` 浮现在 Lippert 心头的那个名字是谁 | **全书未揭晓**；只有 Helena 一句 `But it was impossible` ⇒ **任何补名都是凭空**（T19） |
| U3 | Lippert 如何进入 Hubert 的办公室／Hubert 是否深夜自己开门 | 只有 `:206` 的猜测，他对 `:203` 的直接追问**始终没有回答** |
| U4 | Lippert 到场时是否看见凶手 | 读心画面（`:170`）只显示他面对**已死**的 Hubert 咒骂上帝，其余空白 |
| U5 | Cynthia 是否真是女巫、马车前对狗做的到底是什么 | 本章只有 Helena 的判断（`:335`/`:350`）与 Cynthia 的否认（`:341`/`:347`/`:353`） |
| U6 | 为什么 Helena 能读 Lippert 的心，却听不见 Cynthia 的想法 | 原文未解释（`:314`/`:317` 只写她的无奈） |
| U7 | `:128` `mother’s sickness` 指什么、母亲是谁 | 本章只提发作，未交代来历（薇洛的旧事在 ch16） |
| U8 | `:350` `that dog in front of the carriage` 的经过 | 本章只回指，事件在 ch17 ⇒ **不得与车上的狐狸 Hamlet 混同**（T40） |
| U9 | 为什么「爱」对 Helena 是危险的 | `:359` 只说这一天提醒了她原因，原因本身未展开（私誓在 ch16:176） |
| U10 | 莉莉本人是否接受这笔钱 | `:284` 是 George 以 `We accept yer offer` **代答**；莉莉 `:239` 欲言又止后再无表态 |
| U11 | Sinclair 列出的疑似凶手名单还有谁 | `:38` 只一笔带过 |
| U12 | Hamlet 的真实内心状态 | 全经 Helena 推测（`:323` `must have been terrified`）与 Cynthia 转述（`:326`）⇒ **原文没有任何直接的动物心声**，md 不得写狐狸的想法 |
| U13 | `:332` Helena 口中 Cynthia 的 `powers` 具体包括什么 | 本章只列举现象，未定义 |
