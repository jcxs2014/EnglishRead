# Null Entity · d 步语义二审报告（ch09–ch16）

审查轮次：2026-10-10 d 步（与交付文件名一致）　审查代理：只读独立审查（未编辑任何书籍文件，未执行任何 git 写操作）
审查对象：`notes/books/novels/null-entity-by-seth-haddon/` 下 ch09–ch16 八个精读文件，逐块核对全部 `> **原句 N:**` 块（四件事：引语覆盖度／中文理解忠实度／关键词回查／为什么这样写·读者视角提示的事实性断言（说话人、在场、事件、数字、**时序**）对本章 `text/` 的支撑度）。
指令书：`.memory/progress/ne-review-brief.md`（铁律 1–10 逐条遵守；brief 第 9 条排除的 4 条报警——ch03:55、ch21:99、ch12:61、ch11:33——本次**未再报**）。

## 汇总

**阻断型 12 ／ 提示型 30 ／ 假红型 2**

按章分布：ch09 阻断 2／提示 2｜ch10 阻断 1／提示 2｜ch11 阻断 0／提示 3｜ch12 阻断 0／提示 3｜ch13 阻断 3／提示 5｜ch14 阻断 3／提示 3｜ch15 阻断 0／提示 6｜ch16 阻断 3／提示 6。

本项目缺陷第一名「时序写反」实证命中 3 处（B1、B8、以及 ch14 md:79 一类的指位错见 P），"第一次／唯一"类无出处断言命中 3 处（B2、B10、B11），施动方向写反命中 3 处（B4、B5、B12）。

---

## 一、阻断型（12）

### B1　ch09 原句 6·读者视角提示——时序写反（「数字出现前」实为数字出现后 33 行）
- ① md：`ch09 ten thousand masks.md:81`
  `**读者视角提示**：数字出现前 Aliers 用了“You can’t guess?”的挑衅句式；她投喂信息时反复配姿态动作（folded her arms、eyes gleaming、eyes narrowed），把慷慨写成施恩。`
- ② text：`text/ch09_chapter_9.txt:153`
  `She stared, lips pursed. Finally she said, “Ten thousand LYREBIRD masks.”`
  `text/ch09_chapter_9.txt:186`
  `Aliers looked disappointed. “You can’t guess? I’d start with Nacarat City.”`
- 判定：本块引语中的数字（ten thousand）在 ch09:153；被说成"数字出现前"的 `You can’t guess?` 在 ch09:186，全书该句式仅此一处（`grep -rn "guess" ch09` 只命中 186），且中间还隔着 ch09:177 `Of course she does.`、ch09:183 `So I did. “What will you do with ten thousand units?”`。句序被写反。
- 建议：改为「数字说出后，Aliers 又用“You can’t guess?”（ch09:186）反将一军」；姿态动作三项（folded her arms／eyes gleaming 见 ch09:45，eyes narrowed 见 ch09:201）经核对无误，可保留。

### B2　ch09 原句 4·读者视角提示——把叙述者的词归给 Aliers
- ① md：`ch09 ten thousand masks.md:59`
  `**读者视角提示**：fused、seized、preserved、redeployed 这几个动词后文会被 Aliers 用来描述 VisorForge 对意识的处理方式；同一个词从私人创伤滑向工业术语，是本书写「恐怖」的方法。`
- ② text：`text/ch09_chapter_9.txt:126`（Aliers 台词，只含后三个词）
  `…To them, you’re evidence the mind can be seized, preserved, redeployed—and they’ll use that to justify everything to come.”`
  `text/ch09_chapter_9.txt:93`（本块引语本身，是旁白/低语，不是 Aliers）
  `Here, something whispered. Here is where it happened. Here is where Fyster left you. Here is where they fused LYREBIRD to your skull.`
- 判定：seized／preserved／redeployed 确由 Aliers 在 ch09:126 说出（ch09:93 之后，"后文"成立）；但 `fused` 从未出现在 Aliers 口中——ch09:93 的施动者是 `they`（旁白叙述），ch09:90 是 `A chill ran through me`，Aliers 的下一句要到 ch09:99。四词并列归因错了一个。
- 建议：把 fused 从该清单剔除（或改写为「fused 留在叙述者的低语里，Aliers 后来只接过 seized／preserved／redeployed」——这反而更贴合本文件 md:57「对象从‘我’滑向‘you’」的论证）。

### B3　ch10 原句 5·为什么这样写——把叙述者用词说成终端记录的逐字转写
- ① md：`ch10 the cargo wing.md:65`
  `**为什么这样写**：终端查出三笔记录，叙述只逐字转写其中两个词（BASE 带引号、financiers），把官僚体压缩成两条线索加一记落空：目标在移动、且已搬家。`
- ② text：`text/ch10_chapter_10.txt:174`／`177`／`180`（三笔记录全文）
  `TEST_SUBJECT_RELOCATION—Subjects 1–10, containment BASE`
  `UPCOMING EXPORT—Syndicate pickup, CY 339.260`
  `DATA_TRANSFER_COMPLETE—RHIZOME_DIRECTORY > Subsidiary_Prime`
  `text/ch10_chapter_10.txt:183`（叙述者自己的转述句）
  `Hangar logs confirmed a vessel had already departed for this “BASE,” though no coordinates were supplied. And in three days, a Syndicate ship was scheduled to dock and carry the demonstration masks to its financiers. …`
- 判定：三笔记录逐字枚举后，`financiers` 不在其中任何一条；从记录里被逐字带出的词是 BASE（ch10:174→183 带引号）、Rhizome Directory／Subsidiary Prime（ch10:180→183）、pickup→ Syndicate（转写）。"只逐字转写其中两个词（BASE、financiers）"这一枚举错。
- 建议：改为「叙述只把 BASE 一词原样带进正文并加上引号，其余记录被改写（financiers、three days 都是叙述者的话）」——这样"官僚体被压缩"的论证仍然成立且更有力。

### B4　ch13 导航（一句话概括）——给原文没有施动者的动作补了施动者，且与同文件分析自相矛盾
- ① md：`ch13 hostile fusion.md:10`
  `…Aliers 把两人都绑上那台 rig、推向还在脉动的 Directory，而"我"宁可以杀掉 Wylla Sotain、毁掉一具 Subsidiary 来吓她，也不肯再碰自己的刑具…`
  同文件 `ch13 hostile fusion.md:53`（原句 2 分析）：
  `…本章没有说明这个 she 是谁，读者只能确定被绑上装置的是两具存在，而它们正被推向目录。`
- ② text：`text/ch13_chapter_13.txt:33`
  `We were strapped to the rig. LYREBIRD PRIME had been slotted free, and she and I had taken its place. With LP’s copied credentials clearing the way, Aliers pushed us toward the pulsing Directory.`
  `text/ch13_chapter_13.txt:117`
  `…in the real world Aliers was fighting to rip free of the rig. … Her body spasmed as she dropped from the rig.`
- 判定：`We were strapped` 是无施动者被动式；"推向 Directory" 才是 Aliers 的动作。而 ch13:117 显示 Aliers 本人正在装置上挣扎、随后从 rig 跌落——她不可能是"把两人绑上"的那个人。导航替原文补了施动者，并与 md:53 的正当悬置直接冲突（铁律 8）。
- 建议：改为「两具存在被绑上那台 rig（原文未写是谁绑的），Aliers 把他们推向还在脉动的 Directory」，或删去"Aliers 把两人都绑上"。

### B5　ch13 导航（一句话概括）——恫吓清单的对象与筹码写反
- ① md：`ch13 hostile fusion.md:10`
  `…而"我"宁可以杀掉 Wylla Sotain、毁掉一具 Subsidiary 来吓她，也不肯再碰自己的刑具…`
- ② text：`text/ch13_chapter_13.txt:54`
  `“Stop moving.” I whispered it the way one might to a lover. “I’ve overrun Wylla Sotain, whom I love. I’ve usurped a Subsidiary stronger than you. I could bludgeon your consciousness to death. I could raise your own blaster, burn a hole in your heart, puppet your corpse. Should I do that, General Aliers? Or will you stop moving?”`
- 判定：被威胁要毁掉的是 **Aliers**（your consciousness／your heart／your corpse）；Wylla Sotain 与那具 Subsidiary 在原文里是被声称"已经占领／已经篡取"的筹码（I’ve overrun…／I’ve usurped…），不是"要杀掉／要毁掉"的对象。导航把筹码读成了靶子。同文件原句 4 分析（md:67）自己也提醒"别把威胁当成已被证实的能力清单"，方向与此处一致。
- 建议：改为「宁可声称自己已经占了 Wylla 与那具 Subsidiary、并威胁把 Aliers 的意识砸死，也不肯再碰自己的刑具」。

### B6　ch13 原句 5——引语分段与原文不符（把一整段拆成两个引语段）
- ① md：`ch13 hostile fusion.md:93`＋`ch13 hostile fusion.md:95`（同一 `>` 块内，中间 md:94 为空行 `>`）
  `> Her eyes were raw, lips pursed, plants swaying in an invisible breeze. Then her form shifted. She became a girl.`
  `> Not so young that she was unrecognizable, but young, nineteen or twenty, all dewy-faced and bright-eyed.`
- ② text：`text/ch13_chapter_13.txt:84`（**单段**）
  `Her eyes were raw, lips pursed, plants swaying in an invisible breeze. Then her form shifted. She became a girl. Not so young that she was unrecognizable, but young, nineteen or twenty, all dewy-faced and bright-eyed.`
- 判定：两句逐字都对（门禁全绿），但原文是一整段；md 用空行 `>` 造出一个不存在的段落边界，使读者以为叙述者单起一段强调"Not so young…"，中文理解（md:105）也随之切成两个节拍（"她变成一个女孩。／年轻到还认得出的地步——"）。这正是"引语逐字正确、结构却失真"的 d 步可见缺陷。
- 建议：把 md:93–95 合并为一条引语段（去掉中间的空行 `>`），并相应把中文理解连成一句。

### B7　ch14 原句 1·为什么这样写——计数断言错（重复三遍的是称呼，不是所有权陈述）
- ① md：`ch14 a wife turned extremist.md:25`
  `**为什么这样写**：本章不从场景开始，而从一次过载的呼喊开始——同一个所有权陈述被名字隔开、重复三遍，没有引号也没有说话人标签…`
- ② text：`text/ch14_chapter_14.txt:15`（本块引语第一段，md:17 逐字一致）
  `Wylla, I am yours, Wylla, I missed you, Wylla!`
- 判定：当场点数即知：`Wylla` 出现 3 次；所有权／思念陈述各 1 次（`I am yours` ×1、`I missed you` ×1），且两句不是"同一个陈述"。"重复三遍"的宾语指错了。
- 建议：改为「同一个称呼被名字隔开、敲了三遍，中间挂着两句各说一次的话（I am yours／I missed you）」。

### B8　ch14 原句 7·读者视角提示——把 51 行之后的后述内容说成"已有铺垫"（时序写反）
- ① md：`ch14 a wife turned extremist.md:93`
  `…**end like 一词在本章双关成立（落得那样的结局／那样的死法），而书里对 Aliers 的处境已有铺垫：“Her life was finite, but it could be worth something”，所以“下场”这个词的分量读者已经领教过。`
- ② text：`text/ch14_chapter_14.txt:363`（本块引语在 ch14:312／315）
  `Aliers laughed softly, licking her lips. Later, when I split myself into LYREBIRD PRIME, I’d revisit its stores and see fragments of her memory: … found a morbid comfort in the decision she’d made all those years ago: Her life was finite, but it could be worth something.`
- 判定：`grep "Her life was finite"` 全书仅 ch14:363 一处，位于本块引语（ch14:312）**之后 51 行**，而且被 `Later, when I split myself into LYREBIRD PRIME, I’d revisit its stores…` 明确标为后述回望。读者在原句 7 处领教不到这个词的分量；"已有铺垫"方向反了。
- 建议：改为「这一判决的真正注脚要到本章后段才给出（ch14:363，且被 ‘Later…’ 标为回望）」，或把铺垫换成确在前文的 ch14:309 `I thought of Aliers, her fury narrowed to a single end, burning herself to nothing…`（本文件 md:91 已正确使用该句）。

### B9　ch14 原句 8·为什么这样写——条件方向写反（设条件的是 Wylla，不是 Aliers）
- ① md：`ch14 a wife turned extremist.md:103`
  `…最后唯一悬置的就是她的身体——“we’ll talk”因此既是奖赏也是缰绳：Aliers 的合作要等这一步兑现，读者的下一章也被拴在同一件事上。`
- ② text：`text/ch14_chapter_14.txt:366`
  `All of this pushed Aliers to look up, smiling. “I’ll follow your lead. What’s the plan, Sotain?”`
  `text/ch14_chapter_14.txt:372`（本块引语第二段，md:97 逐字一致）
  `“Get me back in my body,” you said, “and we’ll talk.”`
- 判定：Aliers 的合作在 ch14:366 已经当场兑现（I’ll follow your lead），被 ch14:372 挂上条件的是 **Wylla 对计划的保留**（谁回身体、谁才开口）。"Aliers 的合作要等这一步兑现"把施动方向倒了过来。
- 建议：改为「Aliers 已经交了底（ch14:366 ‘I’ll follow your lead’），现在扣着下一步的是 Wylla——‘we’ll talk’ 是对合作者下的缰绳」。

### B10　ch16 原句 1·为什么这样写——「第一次直说」被 ch12 证伪
- ① md：`ch16 infinity mirror.md:23`
  `…末句「That’s all I’d ever wanted for you.」把叙述者的欲望第一次直说——「我」不是工具也不是系统，她想要的东西与爱人对自己的感觉同构。`
- ② text：`text/ch12_chapter_12.txt:195`
  `My love had nowhere to go. I writhed in loneliness and grief. All I wanted was you.`
  `text/ch16_chapter_16.txt:15`（本块引语，逐字一致）
  `Your return to your flesh was triumphant and bittersweet. You cradled your body with a tenderness you’d spent years refusing yourself. How beautiful it was, to see you so adoring. That’s all I’d ever wanted for you.`
- 判定：`grep -nE "I wanted|All I want|wanted only"` 显示 ch12:195 已是同一形式的欲望直陈，且本库 ch12 文件中文理解已把它译作"我想要的只是你"（`ch12 like knows like.md:149`）——同一条线索在四章之前就已直说过；更早还有 ch09:96 `I wanted you to notice my suffering`。"第一次"不成立。
- 建议：改为「把欲望说成一件**为她**的事（for you）——ch12:195 的 ‘All I wanted was you’ 是要她，这一句是要她好」，差异处的论证反而更精确。

### B11　ch16 原句 4·为什么这样写（并见导航）——「对复仇的第一次正面发问」被 ch13／ch14 证伪
- ① md：`ch16 infinity mirror.md:53`
  `…末问句把本章从战术会议拔到伦理层：这是叙述者对复仇这套行动纲领的第一次正面发问。`
  `ch16 infinity mirror.md:11`：`中段被 Sey 的离席与赴死志愿刺开一道缝（叙述者第一次质问复仇喂养的人生）`
- ② text：`text/ch13_chapter_13.txt:105`
  `I was scared. I’d fallen for temptation before. What if I wanted what she offered? What if revenge cost me you, entirely?`
  `text/ch14_chapter_14.txt:72`
  `…Even if I could make peace with my rage, even if we took our revenge, would it grant us freedom? Or were we condemned to fight until our end?`
  `text/ch16_chapter_16.txt:141`（本块引语，逐字一致）
  `A drop of empathy sparked in me. … What kind of life remains if it only ever feeds on vengeance?`
- 判定：发问式（Would it grant us freedom?／What if revenge cost me you?）在前两章已正面出现，且 ch08:420 `Your vengeance was bound to justice. Mine was a blood hunger.` 已是自评式区分。本章的新意是**把复仇与"还剩哪种人生"绑定**、并落在 Rahn／Sey 的离场之后，不是"第一次"。
- 建议：两处"第一次"改为「本章第一次把问题从‘代价’换到‘余生’（对照 ch13:105、ch14:72）」。

### B12　ch16 原句 4·读者视角提示（并见导航）——「在场领命」与 ch16:132 的当场拒绝相反
- ① md：`ch16 infinity mirror.md:55`
  `**读者视角提示**：Rahn 与 Sey 此刻一个在场领命、一个刚夺门而去——the way it was leading Rahn 点名的是前者；这句发问恰好落在「 won’t be on the field」之后，两位读者可自行对照。`
  `ch16 infinity mirror.md:12`：`Rahn 与 Sey 的分裂公开化——一个领命赴战场，一个在癫痫后夺门而出、不再上场`
- ② text：`text/ch16_chapter_16.txt:132`
  `Rahn stared at him for a long moment before realization broke across the sick man like a tremor. “No.”`
  `text/ch16_chapter_16.txt:135`
  `Rahn reached for Sey’s shoulder, but Sey wrenched away and stormed out, his steps ragged with fury.`
  `text/ch16_chapter_16.txt:120`／`129`（是 Sey 在点人，不是 Rahn 在受命）
  `“Then I know two soldiers who will be happy to—”`／`“Fine,” Sey spat. “Who’s the other one?”`
- 判定：施动核验（前后 ~200 字符）显示：被 Sey 点名为深入 VisorForge 的人选后，Rahn 的反应是 realization + `“No.”`（ch16:132），并且下一秒是 Rahn 伸手去拦 Sey（ch16:135）。本章没有任何"领命"动作；"不再上场"的是 Sey（ch16:138，癫痫一句的归属经 ch16:27 `the latter…convulsing` 核为 Sey，md 这一点正确）。
- 建议：md:55 改为「一个刚被点名为人选并当场说了‘No.’、一个刚夺门而去」；md:12 的"领命赴战场"改为"被点名赴战场"。

---

## 二、提示型（30）

### ch09（2）
- **P1**　`ch09 ten thousand masks.md:79`「"我"随即补一句"Of course she does."再接"You were sharp, frustrated"」——本块引语止于 ch09:156（`We both gasped. “What?!”`），而 `Of course she does.` 在 ch09:177，中间隔着 Aliers 两段长说明（ch09:159、171）与叙述者两次沉默（ch09:162、168）。"随即"应改「在 Aliers 把一万张面具的用途讲完之后」。
- **P2**　`ch09 ten thousand masks.md:91`「同一段落紧接着给出硬件细节——suppress the prefrontal cortex 与 trick the amygdala and hippocampus」——两句逐字在 ch09:171，但在本块引语（只取该段前半）之外。因 md 已明示"同一段落"，不判截短；建议把引语扩到整段。

### ch10（2）
- **P3**　`ch10 the cargo wing.md:75`「紧接其后的独立短段落…原文用第二人称直接指控自己」＋「全章唯一一句不带辩解的自我判词」——所指句为 ch10:210 `I’d betrayed you for almost nothing.`：主语是第一人称 `I`，`you` 是被背叛者；准确说法是"用第一人称认下背叛、把‘你’放在受词位"。"全章唯一"未枚数，按启发式保留。
- **P4**　`ch10 the cargo wing.md:77`「而"I"说"betrayed you"时，通讯那头的人仍然无法回应」——原文只写 ch10:198 `But you weren’t there`，未写任何通讯频道；"通讯那头"是机制补全。

### ch11（3）
- **P5**　`ch11 cheap echoes of me.md:113`「她当时的回答是：那 easier to show you。」——中文理解半英半中，`That’s` 被拆成"那"＋裸英文。建议整句中译（"那更容易演给你看"），英文留在关键词行（`easier to show you`，逐字在 ch11:159）。
- **P6**　`ch11 cheap echoes of me.md:117`「"And this" 的 this 一直到本章倒数第二段才落地」——`And this, I knew, was what she had wanted us to see.` 是 ch11:162，本章**最末一段**（ch11 文件正文止于 162）；md 同一行前文又称本块为"本章的最后两段"，两处口径相抵。
- **P7**　`ch11 cheap echoes of me.md:61`「同一批物体在两处获得不同称呼」——ch11:15 是六个**活着的守卫**（`six of my cousins, each guard masked in LYREBIRD`），ch11:48 是**被撕下丢在尸体间的面具**（`Masks lay torn from their platforms, dented among corpses—cheap echoes of me`）。宜作"同一类物体"。

### ch12（3）
- **P8**　`ch12 like knows like.md:29`「随后三段全是物质描写」＋「第四段把"像"分了级」——本块引语（md:17/19/21/23）可点数为 4 段：命名／面具物质描写／设计与 like knows like／But the name. The name!；"物质描写"只有 1 段，而"第四段"与同行"末段"同指第 4 段。因 md 的"段"在"原文段落"与"引语块内语义层次"之间不统一（详见假红型 J1），此处只记提示。
- **P9**　`ch12 like knows like.md:97`「是本段唯一一处自我批判」——同段 ch12:93 另有 `When I realized my mistake, I let rage bubble over.`，"唯一"有风险；建议改「最淡的一处自我批判」。
- **P10**　`ch12 like knows like.md:153`「她早已为这句话杀过一个人，语气却像在补充时间地点」——原文 ch12 的 `“That’s what Fyster said. Before I boiled his brain.”` 只给时序（Before），未给因果（"为这句话"）也未给地点。

### ch13（5）
- **P11**　`ch13 hostile fusion.md:11`「章末用三个极短段完成视角回到现实」——章末四段 ch13:120／123／126／129 中只有 123（`You had happened.`）与 129 算短，126 是全章最长的情话段。
- **P12**　`ch13 hostile fusion.md:29`（原句 1 中文理解）「在现实这根太阳底下枯萎了」——原文 ch13:18 `withered under the sun of reality`；量词"根"误用，宜"现实这轮太阳"或"现实的烈日"。
- **P13**　`ch13 hostile fusion.md:33`「第三段 "I preferred nothingness…" 与第四段 "Because I’d found myself through you"」——原文分别是 ch13:24（第 4 段）与 ch13:27（第 5 段）：md 在计数时跳过了 ch13:21 的 rapport 段。同行"第一句／第二段／末段"三项正确（ch13:15／18／30），全章七词计数（"Renata Aliers’s mind was full of thorns."＝7 词）已点数无误。
- **P14**　`ch13 hostile fusion.md:85`「下一段就会翻转」——本块引语（md:69–77）的下一段是 ch13:66 `“Do you forgive the subterfuge?”`／ch13:69，并不构成翻转；Aliers 一方的解释要到 ch13:75（`When I heard you’d killed the bastard, I knew you’d come soon.`），且原文始终没有收回 "Why? She was a stranger."（ch13:63）——建议改「本章后段给出 Aliers 的说法（ch13:75），但原文没有替叙述者收回这句判断」。
- **P15**　`ch13 hostile fusion.md:133`「紧接的两段把你说成 angel、savior」——angel／savior 同在 ch13:126 **一段**内（`You’d come like an angel. A savior. …`）；"两段"应为"下一段"。同句「"You had happened." 独立成段、三个词」经核正确（ch13:123）。

### ch14（3）
- **P16**　`ch14 a wife turned extremist.md:27`「（不敢去看被救出的那个女孩究竟是谁）」——括注有两个问题：其一"紧接着的一段"实为 ch14:21 `I’m sorry for coming here alone…`，被引用的 `I couldn’t tell you I’d been too afraid to look. No.` 在 ch14:27（隔两段）；其二本章 ch14:24 的问句 `Have you figured out who she is yet?` 紧接 ch14:30 `You turned back to Aliers`，指向 Aliers 本人；text 里也没有"被救出的那个女孩"这个角色（最接近的是 ch13:84 幻境里十九二十岁的女孩，而 ch13:90 明确她是"把‘我’弄出去的人"）。按铁律 8 不裁决所指，只建议删括注、保留悬置。
- **P17**　`ch14 a wife turned extremist.md:37`「两个名字重复两遍，节奏本身就是一记一记的敲」——引语（ch14:48／51）中 `Renata Aliers` ×1、`Renata Alzian` ×3（含 `—Renata Alzian, Renata Alzian—` 的复沓）；"两个名字各重复两遍"与原文不符。
- **P18**　`ch14 a wife turned extremist.md:79`「They spilled out 延续本章的液体链：开头的 flooded、上一段的 emptied me out、后文的 burning」——`emptied me out` 在 ch14:51（原句 2 那段），本块引语为 ch14:273／276，其"上一段"（ch14:273）没有该词；建议标作「原句 2 的 emptied me out（ch14:51）」。同行"真正的转折在下一段的‘But you stayed’"经核正确（ch14:279 紧邻 ch14:276）。

### ch15（6）
- **P19**　`ch15 i am lyrebird.md:10`（导航）「Wylla 则先**烧掉**它的身份」——原文 ch15:189 是 `you tore away its identity … You scythed the braid clean`；"burned" 属于 Four 的 ID 的意象（`Four’s ID burned like a sigil`），不是动作。宜"撕下身份／割断编结"。
- **P20**　`ch15 i am lyrebird.md:25`「叙述者把它写在同一句里、紧跟在 priority one 之前」——`not even to me` 与 `priority one` 分属相邻两句（ch15:18 的第二、三句），不是同一句；"紧跟在前"正确。
- **P21**　`ch15 i am lyrebird.md:27`（原句 1 读者视角提示）「按行文顺序，这句判词属于随后接手解释技术限制的那个人」——ch15:15 全书无任何说话人标签（紧随的是 ch15:18 旁白、ch15:21 Wylla 复述、ch15:24 Rahn 出场）；推断方向合理（ch15:27 `He sagged`＝Rahn），但按铁律 8，宜明示"原文未标说话人"而非以行文顺序裁决。本条为该句唯一可议处，其余（"首句没有说话人标签""Rahn 手臂吊着吊带、伤口封着树脂"逐字合 ch15:24）均核过。
- **P22**　`ch15 i am lyrebird.md:31`（原句 1 中文理解）「你始终没把更大的盘算漏给**任何人**」——原文 ch15:18 只有 `You hadn’t let slip your broader plan—not even to me`，未写"任何人"，"始终"亦为增译。
- **P23**　`ch15 i am lyrebird.md:47`「本章稍后 Wylla 回的那句"let’s make the bastards suffer"」——该句就在本块引语的**下一段**（ch15:51），`You’re safe, she was telling you` 也在同段；"稍后"弱化了紧邻关系。
- **P24**　`ch15 i am lyrebird.md:101`「eaten alive by its hybrid nature 把**上一段**的杀法收拢成一句因果」——杀法描写在 ch15:204（biocode 反灌），与本块首段引语（ch15:210）之间还隔着 ch15:207（钟铃／删副本）；宜作"前面几段"。

### ch16（6）
- **P25**　`ch16 infinity mirror.md:35`「留意 put me on 与下一场的 take me off 构成本章关系的动词对」——`put me on` 在本块引语之外的同段前半（ch16:18 `…you put me on. Once, you couldn’t have imagined…`，引语从段中起），`take me off` 在 ch16:174，中间隔着整场对 Aliers／Rahn／Sey 的复盘（ch16:21–153），"下一场"不确。建议：引语扩到段首，并把"下一场"改为"后段私下解剖时（ch16:174）"。
- **P26**　`ch16 infinity mirror.md:37`＋`md:43`（原句 3）——引语截掉了段首 `Here you grinned beneath me.`（ch16:111，本块说话人归属的唯一线索）与段尾 `You glanced between them. “I’m sure you can think of something.”`，而分析仍以"你把人家的公关辞令当场翻成战术地图"归因于 Wylla。归因正确，但锚点被截掉，宜补全段首。
- **P27**　`ch16 infinity mirror.md:59`（原句 5 中文理解）「剖开一具尸体的 **visceral** 动作」——关键词行已列 visceral，中文理解仍留裸英文，读感与 ch11 P5 同类。
- **P28**　`ch16 infinity mirror.md:55`「这句发问恰好落在「 won’t be on the field」之后」——引文前多一空格、缺主语，原文为 ch16:138 `He won’t be on the field.`（时序本身正确：ch16:141 在 ch16:138 之后）。
- **P29**　`ch16 infinity mirror.md:93`（原句 8）「所以 **she** 移开视线」——中文行内夹生英文（同文件其余处以"她"称叙述者，如 md:83）。
- **P30**　`ch16 infinity mirror.md:108`／`124`／`125`／`135`（本章词汇·例句）——引号不闭合或整对缺失：`“I said I’d apprehended…before I arrived.`、`Since those coordinates aren’t meant for Subsidiaries to know, …base.`（无引号，实为 ch16:42 长引语的中段）、`“Rather than waste resources…myself.`、`“They’ll see our heat signatures a mile away.`。例句文字逐字均在本章（ch16:63／42／72／93），但把说话人引语抽成无引号残句，读者会误当叙述。

---

## 三、假红型（2，判据自陈）

- **J1　「第 N 段／N 段／上一段」类指位判据在本库不可靠**。同一判据在四处得出不同结论：ch13 md:33（段序少 1，但被引句子逐字与相对顺序全对）、ch14 md:79（`emptied me out` 距本块 222 行，却被称"上一段"）、ch15 md:101（杀法在"上上两段"）、ch12 md:29（"三段／第四段／末段"互相牵连）。原因是 md 的"段"有时指 `text/` 段落、有时指引语块内的语义层次，且 ch13 案例证明两者**可能不一致**（见 B6：md 把一段拆成两段）。故本次凡此类只记提示型，不判红；只有能拿 md 自身显示的引语当场点数的计数（如 B7 的"重复三遍"）才升级为阻断型。
- **J2　「分析引用块外原文＝引语截短」这条判据必须带例外**。ch09 md:91、ch16 md:35／37 都在分析里引用了块外原文；机械套用会误报——md:91 已明写"同一段落紧接着给出"，属正当的位置交代。本次把这三处统一降为"扩段建议"（P2／P25／P26），其中只有当块外原文承担**说话人归属**功能时（ch16 md:37 截掉 `Here you grinned beneath me.`）才值得优先修。

---

## 四、导航层附带发现（不计入报警，供修复代理参考）

1. `ch15 i am lyrebird.md:13`「RABBIT 被逐出与重新回来构成节奏的两次落空」——原文只有一次被逐（ch15:150 `Four had booted it from the system.`），而它的回归是凯旋（ch15:207 `A second later it returned victorious`）。"两次落空"缺乏对应事件，但因属叙事手法评述、非事实断言，未判红。
2. `ch16 infinity mirror.md:13`「尸体解剖与身份重铸全程无第三人称」——该段落确有第三人称主语（ch16:192 `They whirred in delight…`、ch16:195 `The biocode had brushed you…`）。若"第三人称"指叙述视角则无误，指词法则不成立；建议改"全程不出现对二人的第三人称指代"。
3. `.memory/progress/ne-facts-part2.md` 对 ch14 交易条目（"I 的意识回身体"）的记载与 text 的暧昧一致——ch14:96 `Help me, and I’ll get you back in your body.` 的对象是 Wylla；底稿本身的这一读法可能偏了，但 ch14 md 忠实镜像了原文歧义，故不算 md 缺陷。
4. ch14 与 ch15/ch16 的术语建议统一：`建构空间`（ch14:243 `I met you in the construct`／ch14:354 `Outside the construct`／ch15:57 `you’d built a construct`）与 `链接空间`——`ch14 a wife turned extremist.md:69` 用"上一章链接空间"指 ch13 的审讯 construct（ch13:60 `generate a construct for interrogation`），与 ch13 文件自身的"幻境／建构"称呼不一致（该句所指 ch13:90 `Who do you think got you out of here?` 经核无误）。

---

## 五、核过未报（已逐字／枚数验证为正确的关键断言，含枚数结果）

**ch09**：`Of course she does.`（ch09:177）与 `You were sharp, frustrated`（ch09:180）确在本块之后 ✓；`Sable Veonya, not Alzian` 确在原句 5（ch09:114）**之后** ch09:117，"接下来的本能纠正"时序正确 ✓；"upload／download 这对冷词在本书此前从未露面"——`grep -niE "upload|download"` ch01–ch08 **零命中**，本章首现即 ch09:114 ✓；姿态动作三项 folded her arms／eyes gleaming（ch09:45）、eyes narrowed（ch09:201）均逐字属 Aliers ✓；四个 Here 排比＝4 句 ✓。
**ch10**：seven of us 枚举（ch10:18＋ch10:57 五名随行分工）✓；CY 339.260（ch10:177）✓；continuum 全书唯一（ch10:222）✓；"量产面具与‘我’共用配色"有 ch03:159 `LYREBIRD's bronze visage` 支撑 ✓；`I'd betrayed you for almost nothing.` 全书唯一（ch10:210）✓。
**ch11**：`Veonya` 全书仅 ch11:114（ch11:126 的 `Wylla` 属叙述者内心）✓；`mutiny` 全书仅 ch11:120 ✓；三个过去完成时（ch11:159/162 的 `I'd asked`／`she'd said`／`had wanted`）✓；原句 8 的两句确属 ch11 自身最末两段（ch11:159／162），非跨章搬句 ✓。
**ch12**：`You're not Wylla Sotain, are you?` 全书首次明示 ch12:165 ✓；`It was your body, and I loved you` 8 词（ch12:174）✓；四个并列动作 murdered／swiped／stolen／returned（ch12:93）＝4 ✓；原句 6 的无标签问句 `“Sotain, you good?”`（ch12:100）由 md:113 归给 Aliers，支撑句为紧随的 `“Sotain, hey! Hey!” Aliers shook my shoulders`（ch12:109），且同段 `You weren’t there.`（ch12:103）排除 Wylla 在场 ⇒ 归因成立 ✓。
**ch13**：`Renata` 首次出现在 ch13:15 ✓；"第一句七个词"✓；`appearing as Sable-wearing-LYREBIRD`（ch13:60）是本章唯一一处形状自述 ✓；`You had happened.` 三词、独立成段（ch13:123）✓；末句 `“Get your head out of my girlfriend, bitch.”`（ch13:129）md 明确写"没有说话人标签"、未替原文裁决 ✓；"第二次被要求配合装置（第一次在 ch12）"有 ch12:129／132 支撑，"训练室里等着咬进植入体的接口"逐字在 ch11:81 ✓；md:53 对 `she` 的悬置处理是本项目应有的写法 ✓；md:111「`killed the bastard` 由 Aliers 在上段说出，`Fyster` 由叙述者在下一段独自补出」时序正确（ch13:75→78）✓。
**ch14**：`I love you, too.` 是全书首次回应（ch14:282；ch06:291 的 `I love you.` 无回应）✓；`A wife turned extremist` 与 `another of my futures` 两句确在正文 ch14:63 且为叙述者所写 ✓；`Which modules?`＋`tinged with understanding`（ch14:144）✓；`Aliers was past altruism`（ch14:213）紧随原句 4（ch14:210），"立刻加了保留"✓；`I had a ping set for the Alzian name`（ch14:219）在原句 5（ch14:225）之前，md:69"（原句 5 之前的那段）"✓；`burning herself to nothing`（ch14:309）在原句 7（ch14:312）之前 ✓；`You'd use her the way you were used` 逐字在 ch14:93 ✓；`What's the plan, Sotain?`（ch14:366）／`You've got yourself a deal, Sotain`（ch14:168）✓；原句 5 末尾省略系动词的并列（ch14:225 `our father the trauma…our mother the fantasies…`）✓。
**ch15**：`“I am LYREBIRD.”` 全书唯一，且无任何先行的第一人称自名（`grep -rniE "(i am|i'm|my name is|this is|call me) (the )?(lyrebird|sable|prototype)"` 仅 ch15:129）⇒ 导航与情感的"第一次宣告名字"成立 ✓；三词宣告 ✓；`The consciousness inside of LYREBIRD`（ch15:123）确为本块前一语轮 ✓；"下一段 Four 就叫出了 Fugitive Sotain"（ch15:132 紧随 ch15:129）✓；`null entity` 用于 Wylla 有 ch01:259／ch02:325／ch03:267／ch04:125／ch08:90 五处先行实证，扣回机器头上（ch15:192）确为反转 ✓；"与上一章那张种田、耕种、医药的清单同源"＝ch14:147 `“Terraforming, farming, medicine,”` ✓；`Thousands of me crushed Four`（ch15:174）／`I deleted my copies`（ch15:207）逐字在本章 ✓；RABBIT 回扣（ch15:87／207）✓；说话人核验（`Take Sable.`＝Aliers，由 ch15:30 `Aliers unfolded from the corner` 承接至 ch15:36；`He sagged`＝Rahn，ch15:24 引入后 ch15:27）✓；md:103 拒绝替 `clutched something new` 补解释 ✓。
**ch16**：`shared a code base` 全书唯一（仅 ch16:186）⇒ 导航"本章揭出底牌"成立 ✓；本块引语 ch16:15／18／111／141／162／180／186／210 全部逐字（含原文 `compatible— they` 的空格异形也被如实保留）✓；`It won’t be dead for long`（ch16:57）确在"前段"、`calling its nanobots to life`（ch16:192）确在"后文"✓；`Hello, Sable`／`Hello, Wylla` 紧邻 ch16:210 之后（ch16:213／216），"紧接着的两行"✓；`But VisorForge wouldn't see us coming` 确为章末句（ch16:219）✓；`three thousand strong`（ch16:72）✓；Sey 的癫痫归属（ch16:27 `the latter…convulsing`→ch16:138 `after his seizure`）✓；ch02:181 确有 `you found me on Pholan’s World`，md:65"不作解释、不代拟"的处理正确 ✓；词汇表例句逐字全部落在 ch16 ✓。

---

## 六、自数（已核对块数与引语总条数）

| 文件 | 原句块数 | 引语条数（md 内显示段数） |
|---|---|---|
| ch09 ten thousand masks.md | 8 | 13 |
| ch10 the cargo wing.md | 8 | 10 |
| ch11 cheap echoes of me.md | 8 | 20 |
| ch12 like knows like.md | 8 | 38 |
| ch13 hostile fusion.md | 6 | 36 |
| ch14 a wife turned extremist.md | 8 | 13 |
| ch15 i am lyrebird.md | 8 | 12 |
| ch16 infinity mirror.md | 8 | 8 |
| **合计** | **62** | **150** |

- 逐对核对覆盖：62／62 块（非抽查），每块四件事全部执行。
- 引语总条数 150 条，其中 1 条（ch13 原句 5 的 `Not so young that she was unrecognizable…`）系 md 不当分段所生成，对应 `text/` 实为 **149 段**（见 B6）。
- 报警自数：阻断型 12（B1–B12，含 3 条导航／跨章位置已标注）、提示型 30（P1–P30）、假红型 2（J1–J2）。brief 第 9 条要求排除的 4 条报警未再报。
- 每条报警均已给齐三件证据（① md 文件:行号＋逐字摘录 ② `text/chNN:行号`＋原文逐字摘录 ③ 两者同在本次读取输出内）；做不到同文件相邻核实的两处（ch14 原句 1 括注所指、ch13 `she` 的先行词）按铁律 5／8 降为提示型或未裁决。
