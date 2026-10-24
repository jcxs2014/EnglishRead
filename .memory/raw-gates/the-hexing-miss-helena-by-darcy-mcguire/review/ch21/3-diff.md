# ch21 深审 R3 三张单子（漏 / 编 / 错）

> 章：`text/ch21_chapter_21.txt` ↔ `ch21 the dawn confession.md`
> 流程：R1 素读（`1-suread.json`，先于 md）→ R2 机器（`2-machine.json`）→ R3 本文件 → R4 逐块对应（§四）→ R5 判定（见 `4-verdict.md`）
> 判据分级沿用 ch13–ch20 累积口径（(a) 否定断言被自家引语证伪／(d) 章级内容与原文相反且与同 md 自相矛盾／(f) 形式·句数·词数·比例断言可量化证伪／(g) 引语外新增情境事实＝阻断（轻），引语内名词属性补写＝提示／(i) 同章有反证的全称断言＝至少提示）

---

## 〇、结构底账（全部当场取证，后续判定的坐标系）

| # | 事实 | 证据（`text/ch21_chapter_21.txt` 行号） |
|---|---|---|
| 1 | 正文体范围 `:35`–`:371`（`:372` 起为空白；末字节为 `I won’t.’\n`＋尾随空格行） | `:35` `Helena shifted under her covers…` ／ `:371` 末句 `I can’t risk becoming like that, Cynthia. I won’t.’` |
| 2 | **单一视角＝海伦娜**，全章无空行分场、无 POV 标记行（与 ch19/ch20 的双段结构不同） | 通读 `:35`–`:371`；每段之间固定「一行空＋一行空」，无分隔符 |
| 3 | 推广／版权残留行 **0 条**（全书 8 行分布 in ch03/ch08/ch13/ch19/ch25，本章不含） | `/usr/bin/grep -c "Lokepub" text/ch21_chapter_21.txt` → `0`，**退出码 1**（见 §六 C） |
| 4 | 时间刻度：`from black to indigo`（起）→ `indigo to a much paler blue`＋`sun began her slow ascent to welcome morning`（中段）→ `In the warming light`（末） ⇒ 全章跨度＝**深夜将尽至黎明**，不是「一个连续的夜里」 | `:35` ／ `:260` ／ `:362` |
| 5 | **无引号心声**（free indirect）两处 | `:83` `Bloody hell. I want her.` ／ `:140` `That’s all this is. All this can ever be.`（另 `:161`/`:164` 为叙述层内心，带引号台词相邻） |
| 6 | **叙述者替辛西娅下假设句**一处（全章唯一，越出「只从动作与答话推断」） | `:116` `If she knew how enticing she looked, hopelessly rumpled, her breasts pushed up like an offering, her eyes still soft and sleepy, she wouldn’t relax so easily in Helena’s presence.` |
| 7 | 哈姆雷特**首次咬她** | `:50` `…cocked it, and nipped her arm.` ＋ `:53` `‘Hamlet!’ He’d never nipped her before.`（全书 `nipped` 仅此两行） |
| 8 | **胸骨上的树莓色星形胎记**：本章首次点名，ch27 结尾回收 | `:191` `Her thumbs paused on Helena’s sternum and traced the raspberry-coloured star.` ／ `:194` `‘It’s just a birthmark.’` ／ `text/ch27_chapter_27.txt:71` `The birthmark shaped like a star and placed perfectly on Helena’s sternum was almost the same colour of berry red.` |
| 9 | **阿斯彭姨妈**在全书唯一一次出场；同段给出三女巫在村中的职能与村民容忍的理由 | `:266` `There were always whispers about Mother, Aunt Aspen, and Aunt Rowan. The witches who could heal your ailing child or ripen the crops…The villagers allowed them to live peacefully because they knew the benefits of benevolent witches in their midst. But then Aunt Aspen left to follow her heart to its ultimate death.` |
| 10 | 三类魔法之外同一句还含**「我们立誓时自愿献血以加固誓言」**——与后文「不情愿给出的血」构成精确对照；该句被 md 的省略号跳开 | `:284` `When we committed to being witches who bring only health and healing, we willingly gave our blood to strengthen the oath.` |
| 11 | 母亲名＝**Willow**，且 `:311` 明写「她母亲对她做的，比不上海伦娜如何惩罚 Willow」 | `:311` `Whatever her mother had done to her was nothing compared to how Helena punished Willow.` |
| 12 | 坎贝尔太太是**撞见**她，不是她去找：`caught me right before I fell on my knees`，且叙述者补「她大概是赶集回来」 | `:305` |
| 13 | 告密链完整：`Old Mrs Campbell saw my wounds` → 海伦娜亲口说了爱情咒与害怕母亲 → 她跑回村子宣传「dark witches」 | `:326` |
| 14 | 水巫能力的全称自述：`I own the rain clouds, the rivers, and the seas.` | `:326` |
| 15 | **章末拒绝的证据是三段「最坏时刻」＋差点淹死 Lippert 的自白**；`:371` 一句内同时给出：界线重申、三次目睹、`Hexed Helena` 之问的答复、母亲的血、`I won’t` | `:371` |
| 16 | `should I call you Hexed Helena?` ＝**书名双关，全书唯一一次** | `:368`；全书 `grep -rn "Hexed Helena" text/` 仅 `ch21:368` |
| 17 | 气味归属：本段 `Honeysuckle and vanilla wrapped around Helena`（辛西娅身上的味道环绕海伦娜）——与 ch20 `:366` 海伦娜房门口的佛手柑＋柠檬成对 | `:260` ／ `text/ch20_chapter_20.txt:366` |
| 18 | 「灵魂交织」的反证在叙述层：`:146` `Because Cynthia was right. They couldn’t join together without being irrevocably altered.` ⇒ 本章唯一一次**叙述者盖章**支持辛西娅 | `:146` |
| 19 | 性事段落的「引导者反转」两处自供：`:209` `She was supposed to be showing Cynthia the glory of sexual congress…` ／ `:242` `‘I was supposed to bring you to climax.’` | `:209` `:242` |
| 20 | 水的隐喻链贯穿（与她的水巫身份同构）：`:77` `swept away in a wild river of need` → `:92` `like a gentle wave rolling onto shore` → `:227` `shattered against the shore of intentions…sucked back to the heart of the sea` → `:233` `returned to the earth` | `:77` `:92` `:227` `:233` |
| 21 | shield／armour 意象链：`:62` `cut past her shields` → `:164` `pull back the shield hiding her deepest wounds` → `:170` `dismantled all Helena’s armour` | `:62` `:164` `:170` |
| 22 | md 引语块 13 个（`md:18/28/38/48/58/68/78/88/98/108/118/128/138`），词表 24 行（9/9/6，`md:152`–`md:187`），导航 5 项（`md:10`–`md:14`），总结 1 段（`md:191`） | `2-machine.json`：`blocks=13`、`block_target=[7,11]`、**`block_hint` 非空（超限，提示型，rc 仍 0）**、`segments=15`、`segment_miss=0`、`words=3631`、`nav_count=5`、`issues=[]` |

---

## 一、漏（md 未记 / 未展开的原文事实）

| # | 原文事实（逐字锚点） | md 现状 | 判定 |
|---|---|---|---|
| L1 | `:59` `‘Why can’t I hear what you’re thinking? Or what she is thinking? Because Aunt Rowan’s hypothesis is completely barmy.’` ＋ `:62` `Hamlet’s golden eyes cut past her shields, piercing deep. Maybe she didn’t want to hear what he was thinking.` ＋ `:65` `‘Stay here.’ It was bad enough she would be wondering what Cynthia was thinking without having to wonder what her fox was saying to the woman.` — 海伦娜**自己给出的替代解释**（不是听不见，是不想听）＋她把狐狸单独留在房里的那点醋意；连同 shield→armour 三段意象链（`:62`→`:164`→`:170`） | `md:13` 只收「荒唐透顶」一句结论；`:62` 的「也许她并不想听见」、`:65` 的 `Stay here` 与意象链在导航与 13 块分析层里**全无** | **阻断（漏）** |
| L2 | `:266` 阿斯彭姨妈出场（全书唯一）＋三女巫「能治好病孩、能让灾后田里催熟庄稼」的村中职能＋「村民容忍她们因为知道善良女巫的好处」＋「阿斯彭为跟随 hearts 走到它终极的死亡」 | 全书 md **`aspen`/`阿斯彭` 0 命中**（§六 B，退出码 1）；`md:10` 概括与 `md:68` 块只讲「母亲爱上铁匠」，未记这条家族与村社背景 | **阻断（漏）** |
| L3 | `:371` `I’ve seen you in the worst of times. The day your husband died. In Sinclair’s office. Even facing off against Lippert.…When Lippert threatened you, I was a thought away from drowning him with my powers. I would kill anyone who tried to hurt you. That is not the way of a light witch.` — 拒绝的**举证方式**是三段「她的最坏时刻」＋一次差点动用力量淹死利珀特的自证 | `md:138` 块（原句 13）只截 `Love twisted her…` 起，导航与总结均无「辛克莱办公室／利珀特／差点淹死他」；`:368` 的 `the only curse here is believing history must repeat itself` 也未记 | **阻断（漏）** |
| L4 | `:191`＋`:194` 胸骨上的**树莓色星形胎记**（海伦娜称「只是块胎记」，辛西娅吻它并说「它很美」）——该胎记在 ch27 `:71` 结尾原样回收 | `md:152`–`md:187` 词表有 `birthmark｜胎记` 一行，例句正是 `:194`；但**星形／位置（胸骨）／树莓色／与 ch27 的回收**在分析层与导航都没写 | **阻断（漏）** |
| L5 | `:146` `Helena’s heart stuttered. Because Cynthia was right. They couldn’t join together without being irrevocably altered.` — 叙述者当场承认辛西娅说得对，是全章唯一一次叙述层盖章 | `md:58`（原句 4）分析层只讲「她怕自己的信号被当真」；`:146` 这条反证未提，读者会以为全书叙述站在海伦娜一边 | 提示 |
| L6 | `:284` `When we committed to being witches who bring only health and healing, we willingly gave our blood to strengthen the oath.` — 「自愿献血加固誓言」与「不情愿给出的血」是同一句里的镜像对照，正是判罪逻辑的支点 | `md:88` 引语用 `…` 恰好把这句跳开；`md:90` 分析层称「省略号跳开的部分讲的是血魔法可以违背意志被夺走」——**跳开的其实是这句自愿献血**（`:284` 内 `can be taken against someone’s will` 在跳开段之后，未做完整说明） | 提示 |
| L7 | `:272` `Mother was a firewitch with the power of potions, much like Clio.` — 母亲与克莱奥的能力被明写为同类 | `md:10`/`md:191` 只说「母亲是会做药水的火巫」（此为 `md:10` 未记、`md:191` 记了），`much like Clio` 的对应关系无 | 提示 |
| L8 | `:368` `Henceforth, should I call you Hexed Helena?` — 书名双关，全书唯一一次 | `md:10`–`md:14`、`md:191` 无；词表无 | 提示 |
| L9 | `:260` `Honeysuckle and vanilla wrapped around Helena` ＋ `:356`–`:359` `his tail briefly curled around her ankles`／`bumped his head against Helena’s in a foxy version of a hug`／`his nose at Helena’s elbow, his tail at Cynthia’s feet` | `md:11` 只称「气味」不定位，`md:191` 只说「卧在两人之间」；狐狸入房的三段身体接触细节未记 | 提示 |
| L10 | `:209` `She was supposed to be showing Cynthia the glory of sexual congress, but the contradictory woman had once again shaken Helena’s plans into chaos.` ＋ `:242` `‘I was supposed to bring you to climax.’` — 两次「本该由我引导」的自供，与 `:233` 的 `There you go, trying to tell me what to do again.` 构成同一条控制线 | `md:58` 块收了「你总是打乱我的计划」，未收性事段这两处同源句；控制／被控制的反转不显 | 提示 |
| L11 | `:239` `Never had her explorations with other women been so enthralling.` — 明写她**既往与女性有过经验** | `md:152` 词表收了 `enthralling` 例句，但分析层与导航都没记这条事实（对「她只给朋友名分」的成因有影响） | 提示 |
| L12 | `:185` `‘Shh. Ellie was lying. They aren’t that far away, and the walls are thinner than you think.’` — 回收 ch20 埃莉关于房间距离的谎话 | 无 | 提示 |
| L13 | `:167`（`:170` 末）`‘If you want me stop…’` — 原文此句**缺问号**（`If you want me stop…`），海伦娜话未说完即被接走 | 无（md 未截此句，也未记章内「她始终说不完要求」这一形态） | 提示 |
| L14 | `:179` `nipples as red as hawthorn berries` 与 `:191` `raspberry-coloured star`、`:200` `Her nipples were a brighter red, the same colour as her star` — 红色意象三次串联（山楂→树莓→星） | `md:48` 收了 `as red as Cynthia’s lips`（`:80`），未收这三处 | 提示 |
| L15 | `:326` `I’m a waterwitch. I own the rain clouds, the rivers, and the seas.` — 能力的全称自述，与她「水变成雾」的失败构成规模对照 | `md:128` 块收了后半句 `my water turned to mist`，`I own…` 这句未进引语也未进分析层 | 提示 |

---

## 二、编（md 有、原文无）

| # | md 位置 | md 说法 | 取证 | 判定 |
|---|---|---|---|---|
| B1 | `md:34` | 「"童话变成真的"又把克莱奥、埃莉的恋爱说成一种**她们小时候一起嘲过的东西**」 | `:68` 原文给的童年三件事是 `spinning fairy tales, sharing fears, and commiserating over mothers who had sacrificed themselves on the altar of love`——三件都是**一起编、一起说、一起替母亲叹息**，无一处「嘲笑恋爱」；`As they transitioned into womanhood, fairy tales became reality` 也没有「嘲」的语义 | **阻断（凭空 1）** |

**成立取证表（md 的其余事实主张逐条回原文，成立，不再列疑）**

| md 主张 | 原文证据 |
|---|---|
| 「整夜睡不着，天亮前决定去把话说清楚」 | `:35`＋`:65`＋`:74` |
| 「先看光了对方裸露的胸」 | `:80` `One breast spilled out, and Helena couldn’t rip her gaze away…` |
| 「先拿床罩替她盖上」 | `:86` `taking a coverlet at the end of the bed, draping it over Cynthia’s body to cover her nudity` |
| 「问出"你要我吗"，得到两次"是"」 | `:125` `‘Do you want me?’`／`:128` `‘Yes.’`／`:131` `‘Now?’`／`:134` `…nodded. ‘Yes.’` |
| 「追加"就算这不会改变我们之间的一切"」 | `:137` |
| 「辛西娅回说无论如何都会改变一切」 | `:143` |
| 「在辛西娅手里接连到达高潮，直到求停」 | `:227` `past the first orgasm and eased her into the second`／`:230` `‘Stop. Please. You must…’`／`:233` `she redoubled her efforts`／`:233` 末 `reached yet another peak` |
| 「父母只在爱丁堡的萨温节共度一夜」 | `:266` |
| 「母亲爱上村里铁匠／为发财卖爱情药水」 | `:266`＋`:272` `He knew, and he craved the riches they could bring.`／`dealing in love tonics` |
| 「违背布莱尔女巫"不作恶"的誓言」 | `:278` `The oath of all the Blair witches. To do no harm.` |
| 「魔法分三种，血魔法最强，要不情愿给出的血」 | `:284` |
| 「母亲取的正是海伦娜自己身上的血」 | `:290`（绷带）＋`:305`（`I was bleeding, scratched from Mother trying to catch me`）＋`:326`（`Old Mrs Campbell saw my wounds`） |
| 「小时候醒来发现手脚缠绷带、装睡等"魔鬼"、等到握圣刃的母亲」 | `:290` |
| 「逃去找坎贝尔太太」→（此项见 §三 E8，**方向写反**）；「村民因此得知黑暗女巫」 | `:326` `told the people dark witches were in our midst` ✔ |
| 「把母亲和铁匠锁进屋里烧死」 | `:320` `locked her inside with the blacksmith, and burned them to cinders` |
| 「七岁／水巫／能灭任何火／水变成雾」 | `:332`／`:326`／`:344` |
| 「辛西娅反驳：她是背叛你的人、你当时只是孩子、你同样是仇恨的受害者」 | `:341`／`:302`＋`:329`／`:347`（三条内容都成立；「三次」这一计数见 E7） |
| 「海伦娜只说"我是个诅咒"」 | `:353` `‘I’m a curse.’` |
| 「哈姆雷特抓门进来卧在两人中间」 | `:356` `A scratch on Cynthia’s door…let in a desperate Hamlet`／`:359` `slumping down between them` |
| 「辛西娅问"若你真这么邪恶它会选你吗"」 | `:362` |
| 「要求她别拿自己对休伯特那套标准要求自己」 | `:368` `You told me I wasn’t to blame for Hubert’s crimes.…What about you?` |
| 「母亲的血也流在她身上」 | `:371` `My mother’s blood runs through me.` |
| 「爱把母亲扭成冷酷残忍的东西／她不敢冒变成那样的风险」 | `:371` |
| 「章末停在海伦娜的"我不会"，不写辛西娅的反应」 | `:371` 末 `I won’t.’` 即正文最后一句，`:372` 起无内容 ✔ |
| 「哈姆雷特第一次咬了她」 | `:50`＋`:53` |
| 「罗温的假设被斥为荒唐透顶」 | `:59` |
| 「魔宠再次站在她一边（"也许它是想把我赎回来"）」 | `:365` `‘Perhaps he is trying to redeem me.’` |
| 「全章单一海伦娜视角，中间没有空行换 POV」 | 见 §〇 2 |
| 「"我要沉进甜蜜的失去知觉里"」 | `:296` 语句成立 ✔（但位置与文体见 E2） |

---

## 三、错（md 有、原文相反 / 越界）

| # | md 位置 | md 说法 | 反证（逐字） | 判据 | 判定 |
|---|---|---|---|---|---|
| E1 | `md:124` | 「作者让辛西娅的安慰（"你还是个孩子"）和**海伦的反驳**正面相撞」 | 人名缺字；全书 md 中 `海伦` 后不接「娜」仅此一处（`/usr/bin/grep -rn "海伦[^娜]" --include="*.md" .` 唯一命中即 `ch21:124`，见 §六 A） | 专名损坏（同「摘要句主体张冠李戴」族） | **阻断** |
| E2 | `md:26`（原句 1 读者提示） | 「**章末**她向辛西娅**承认**"想沉进甜蜜的失去知觉里"，与此处呼应…同一个人前后**两次的自供**」 | `:296` `She wanted to sink into sweet oblivion and never emerge.` 位于 `:35`–`:371` 的**中段**（坦白刚开始之前），且是**叙述层**的她所想，不是对辛西娅说出的话；她向辛西娅说出的自供是 `:353` `‘I’m a curse.’` 一类 | 章内时序写反＋「叙述」升级为「承认」 | **阻断** |
| E3 | `md:44`（原句 3 分析层） | 「这段是"下决心的独白"，**句式一遍比一遍长**」 | `:74` 四句实测 3／4／3／23 词（`‘I am dithering.` 3；`And I don’t dither.` 4；`This is ridiculous.` 3；末句 23）——**第三个比第二个短**，不是递进；实际形态是「三个短句后甩出一个 23 词长句」 | (f) 形式·长度断言可量化证伪 | **阻断（轻）** |
| E4 | `md:54`（原句 4 分析层） | 「"something more"**这四个字**说穿了她真正怕的东西」 | `:137` `…wouldn’t risk her lust being mistaken for something more.` — `something more` 是**两个词**；md 自身 `md:10` 也把它当词组引用 | (f) 计数断言可量化证伪（与 ch19 E2「三个短句」、ch21 E3 同族） | **阻断（轻）** |
| E5 | `md:124` | 「**三句层层收小**：年龄、义务、失败」 | `:332` 引语内三句实测 3／6／12 词（`I was seven.` 3；`Old enough to have done something.` 6；`And I tried, but my powers weren’t enough to stop the fire.` 12）——句长**递增**。「收小」只有在读成语义收敛时才成立 | (f) 的可宽读法：语义收束可辩护 ⇒ 不判阻断 | 提示 |
| E6 | `md:134`（原句 12 分析层） | 「作者让她把天赋解释成诅咒，正是**下一章**她要用来拒绝辛西娅的逻辑起点」 | 拒绝发生在**本章章末** `:371`（即原句 13 的引语本身：`My mother’s blood runs through me. Love twisted her…I won’t.’`），`:372` 起正文结束；不存在「下一章才用它拒绝」 | 章内时序／相对位置写反 | **阻断** |
| E7 | `md:191`（一句话总结） | 「辛西娅**三次反驳**：你还是孩子、是她背叛了你、你同样是仇恨的受害者」 | 同章辛西娅否定海伦娜自责的台词至少 5 处：`:302` `I will cry for you! How dare your mother abuse you so horrifically? You were just a child.`／`:329` `‘You were just a child.’`／`:335` `‘You cannot blame yourself, Helena.’`／`:341` `‘She betrayed you. She was using you.’`／`:347` `you were just as much a victim of their hatred as your mother.`／`:368` `the only curse here is believing history must repeat itself.` | (f) 计数断言证伪（三条内容本身成立，错在「三次」） | **阻断（轻）** |
| E8 | `md:10`（导航·一句话概括） | 「她逃去**找**坎贝尔太太，村民因此得知"黑暗女巫"」 | `:305` `so I kept running until I came to the village. **Old Mrs Campbell caught me** right before I fell on my knees. She must have been on her way back from the market.`——是**被撞见**，且她原本要去找的是罗温（`:305` `I should have found Aunt Rowan. But she wasn’t at her cottage`）；md 自家 `md:191` 写的正是「她逃到村里，坎贝尔太太**看见**伤口」⇒ 同一 md 内自相矛盾 | (d) 章级内容与原文相反且与同 md 另一处冲突 | **阻断** |
| E9 | `md:14`（导航·叙事手法） | 「**辛西娅的内心始终不给出**，只能从她的动作与答话推断」 | `:116` 叙述者以假设句直接写辛西娅会怎么想／会不会放松；这是全章唯一一处，但确实存在，且**不属**「动作与答话」 | (i) 全称断言有同章反证 ⇒ 至少提示（`:116` 属海伦娜口吻的推测，不判阻断） | 提示 |
| E10 | `md:114`（原句 10 分析层） | 「**前两句的动词全部朝向村民**（涌进、锁住、烧），但**两句的主语都是"我"**」 | `:320` 引语三句：`I’m the reason she died.`（动词 `am`／`died`，不朝向村民）；`It’s because of me the villagers swarmed…locked…burned…`（三个动词都在第二句，其**语法主语是形式主语 `It`**，施事是 villagers）；`A firewitch consumed by mortal flames.` | 语法类别名用错（中文分析层第四族）＋范围越界 | 提示 |
| E11 | `md:11`（导航·情感弧线） | 「全章在**一个连续的夜里**走完五档」 | `:35` 已 `the sun was just beginning to warm the skies from black to indigo`；`:260` `The sky had drifted from indigo to a much paler blue as the sun began her slow ascent to welcome morning`；`:362` `In the warming light` ⇒ 深夜将尽至**黎明之后** | 时段事实偏差 | 提示 |
| E12 | `md:90`（原句 8 分析层） | 「**这一句是全章唯一的设定说明**」 | 同章另有 `:272`（母亲是火巫、会做药水）、`:278`（布莱尔女巫的誓＝不作恶）、`:326`（水巫拥有雨云河流海洋）、`:266`（三女巫的村中职能）——均属设定说明 | (i) 全称／唯一性断言有同章反证 | 提示 |
| E13 | `md:60`（原句 5 中文理解） | 「把哈姆雷特像共同的爱子一样**轮流**分享的命定伴侣」 | `:248` `…shared Hamlet between them like the familiar version of a love child.` — 原文是「在两人之间共享」，**无「轮流」义**；md 自行加上 | (g) 引语内新增副词性情境 ⇒ 提示（不改变方向，只加频率） | 提示 |
| E14 | `md:36`（原句 2 读者提示） | 「读者要记住这是她的视角，**不是书中人物的实际遭遇细节**」 | 同章内母亲威洛确为「把自己献给爱」而死于火（`:266`＋`:320`），md `md:34` 自己就写「为后面母亲为爱情倒贴性命铺路」；`md:36` 这句若被读成一般性否定，即与同块 `md:34` 打架 | 措辞越界（易被读成否定断言）⇒ 只要求收窄表述 | 提示 |
| E15 | `md:64`（原句 5 分析层） | 「辛西娅的"我错了"式的回答（**若有悔意才会道歉**）先落地」 | `:245` `‘I would apologise for disrupting your plans if I felt even an ounce of remorse.’` — 原句是**虚拟式否定**：她不会道歉，因为她毫无悔意；md 括注的「若有悔意才会道歉」方向对，但「"我错了"式的回答先落地」会让读者以为辛西娅确实道了歉 | 引语理解表述含混（非反向） | 提示 |
| E16 | `md:86`（原句 6 关键词行）／`md:88` 块 | 「作者把她这么做的理由写成…"我始终不懂"是全章最软的一句」等 | `:266` `I never understood what finally drew her to him.` ✔；但 `md:88` 把该句列为「全章最软」并与 `:296`、`:353` 争「最」——**可核的最高级须查**：本章另有 `:296` `She wanted to dissolve into Cynthia’s embrace and forget` 与 `:344` `I was completely useless` 同级柔软句 | 「最」类断言：未证伪但范围可核 ⇒ 只提示 | 提示 |

### 问答链底账（说话人逐条回原文，供 R4 归属核对）

`:41` 海伦娜 → `:44` 哈姆雷特叹气 → `:47` 海伦娜 → `:50` 哈姆雷特咬 → `:53` 海伦娜 → `:56` 哈姆雷特低吼 → `:59` 海伦娜 → `:65` 海伦娜 → `:74` 海伦娜 → `:83` 海伦娜（心声）→ `:89` 海伦娜 → `:95` 辛西娅 → `:98` 辛西娅 → `:101` 辛西娅 → `:107` 海伦娜 → `:110` 辛西娅 → `:113` 海伦娜 → `:116` 辛西娅 → `:119` 海伦娜 → `:122` 辛西娅 → `:125` 海伦娜 → `:128` 辛西娅 → `:131` 海伦娜 → `:134` 辛西娅 → `:137` 海伦娜 → `:143` 辛西娅 → `:146` 海伦娜（叙述）→ `:149` 海伦娜 → `:152` 辛西娅 → `:155` 辛西娅 → `:164` 海伦娜 → `:170` 海伦娜（未完句）→ `:173` 辛西娅 → `:185` 海伦娜 → `:191` 辛西娅 → `:194` 海伦娜 → `:197` 辛西娅 → `:203` 辛西娅 → `:215` 海伦娜 → `:218` 辛西娅（growled）→ `:230` 海伦娜 → `:233` 辛西娅 → `:236` 辛西娅 → `:242` 海伦娜 → `:245` 辛西娅 → `:248` 海伦娜 → `:251` 辛西娅 → `:254` 海伦娜 → `:257` 辛西娅 → `:263` 辛西娅 → `:266` 海伦娜 → `:269` 辛西娅 → `:272` 海伦娜 → `:275` 辛西娅 → `:278` 海伦娜 → `:281` 辛西娅 → `:284` 海伦娜 → `:287` 辛西娅 → `:290` 海伦娜 → `:293` 辛西娅 → `:299` 海伦娜 → `:302` 辛西娅 → `:305` 海伦娜 → `:308` 辛西娅 → `:314` 海伦娜 → `:317` 辛西娅 → `:320` 海伦娜 → `:323` 辛西娅 → `:326` 海伦娜 → `:329` 辛西娅 → `:332` 海伦娜 → `:335` 辛西娅 → `:338` 海伦娜 → `:341` 辛西娅 → `:344` 海伦娜 → `:347` 辛西娅 → `:353` 海伦娜 → `:362` 辛西娅 → `:365` 海伦娜 → `:368` 辛西娅 → `:371` 海伦娜（末句）。
⇒ **13 个引语块的说话人与底账一致，零张冠李戴**；md 全部用「她说」，未把任一台词安错人。

### 时序专查（13 块落点单调性）

| 块 | 落点行 | 与前一块 |
|---|---|---|
| 原句1 | `:35` | — |
| 原句2 | `:68` | ↑ |
| 原句3 | `:74` | ↑ |
| 原句4 | `:137` | ↑ |
| 原句5 | `:248` | ↑ |
| 原句6 | `:266` | ↑ |
| 原句7 | `:278` | ↑ |
| 原句8 | `:284` | ↑ |
| 原句9 | `:290` | ↑ |
| 原句10 | `:320` | ↑ |
| 原句11 | `:332` | ↑ |
| 原句12 | `:344` | ↑ |
| 原句13 | `:371` | ↑ |

⇒ **块序单调，零调转**（本章缺陷簇不在块序，而在 E2／E6 两处「相对位置」表述）。

---

## 四、R4 逐块对应表（三问：动词主语／受事／归属方向）

| 块 | md 行 | 原文行 | 动词主语 | 受事 | 归属方向 | 结论 |
|---|---|---|---|---|---|---|
| 1 | md:18 | `:35` | Sleep（拟人）拒 give／她 lay／太阳 warm | her（oblivion）；the skies | 「她想要→被拒」方向 ✔；但 md:26 把 `:296` 的叙述写成「向辛西娅承认」⇒ **E2** | 对应 ✔／分析层 ✘ |
| 2 | md:28 | `:68` | 海伦娜 stop／memories spill／她们 spent／everything was changing | 童年三事 | 「母亲献祭于爱」= 海伦娜的框架 ✔；md:34 新增「小时候一起嘲过」⇒ **B1** | 对应 ✔／凭空 ✘ |
| 3 | md:38 | `:74` | 她（I）dither／I shall push・wake・explain | door／Cynthia／道理 | 决心主体 ✔；md:44 的「一遍比一遍长」量化不成立 ⇒ **E3** | 对应 ✔／形态断言 ✘ |
| 4 | md:48 | `:137` | 她（I）couldn’t lie／wouldn’t risk | Cynthia／her lust 被误认 | 「她怕自己信号被当真」方向 ✔；md:54「四个字」⇒ **E4** | 对应 ✔／计数 ✘ |
| 5 | md:58 | `:248` | Reality reasserted／她 had come／they shared Hamlet | things／Cynthia／哈姆雷特 | 「她来解释界线」✔；md:60 加「轮流」⇒ **E13**；未收 `:146` 叙述盖章 ⇒ L5 | 对应 ✔ |
| 6 | md:68 | `:266` | 母亲 fell in love／give her heart／他们 had known／她 spent | 铁匠／一夜 | 信源＝海伦娜记忆，md:74 已 hedge ✔；漏阿斯彭 ⇒ **L2** | 对应 ✔ |
| 7 | md:78 | `:278` | 我 don’t know／those love spells violated／We can’t steal | 誓言／人的意志 | 「不定论＋钉罪名」层次 ✔；md 明确「不是判定药水无效」✔ | 对应 ✔ |
| 8 | md:88 | `:284` | There are／Blood magic demands／we gave／Mother needed | 誓／血／药水 | md:94 已声明「口述分类，非全书体系」✔；`…` 跳开句实为「自愿献血」⇒ **L6**；md:90「唯一设定说明」⇒ **E12** | 对应 ✔ |
| 9 | md:98 | `:290` | 我 didn’t know／I would wake／I pretended／It was Mother | 绷带／魔鬼／圣刃 | 儿童无知视角 ✔；md:102 未推断圣刃来历 ✔ | 对应 ✔ |
| 10 | md:108 | `:320` | 我’m the reason／villagers swarmed・locked・burned | 母亲与铁匠 | 「动作让给别人、责任留给自己」方向 ✔；md:114 两句主语与动词范围错 ⇒ **E10**；`六个词` ✔（实测 6） | 对应 ✔ |
| 11 | md:118 | `:332` | 我 was seven／I tried／powers weren’t enough | 火 | 反驳对象是「年龄的含义」✔；md:124 人名缺字 ⇒ **E1**；「三句层层收小」⇒ **E5** | 对应 ✔ |
| 12 | md:128 | `:344` | 我 thought／I can douse／my water turned／I was useless | 火／雾 | 「以成年标准判七岁自己」✔（md:130 已注）；md:134「下一章」⇒ **E6** | 对应 ✔ |
| 13 | md:138 | `:371` | Love twisted／I can’t risk／I won’t | her／becoming like that | 「从恐惧滑到决定」✔；md:142 已划清「理由不是不爱」✔；漏三段最坏时刻与 Lippert ⇒ **L3** | 对应 ✔ |

⇒ **13/13 引语逐字全部 `ok`（`segment_miss=0`）；对应调转 0；说话人 0 错。**

---

## 五、形态层

| # | 检查项 | 结果 |
|---|---|---|
| 1 | 导航 5 项齐全（概括／情感弧线／Tropes／人物弧线／叙事手法） | ✔ `md:10`–`md:14`，`nav_count=5` |
| 2 | 引语块格式 `> **原句 N:**`（冒号在粗体内）13 块连续无跳号 | ✔ |
| 3 | 每块四子项（原句／中文理解／关键词／为什么这样写＋读者视角提示） | ✔ 13/13（原句 1 无「读者视角提示」？——`md:26` 有；逐块核：1–13 均带读者提示，`md:26/36/46/56/66/…/md:146`）✔ |
| 4 | 词表三档表体为标准 Markdown 表格（新规则①） | ✔ 9/9/6，`check_vocab` rc=0，`rows=24 missing=0` |
| 5 | 词表逐行回原文核对（`vocab_head` 门禁） | ✔ rc=0 |
| 6 | 引语块**结尾闭合引号**体例：原句 5/6/7/8/10/12/13 块末**缺 `’`**（截到句号即止） | 提示（全书体例一致问题，引语仍是原文逐位子串 ⇒ 不判阻断；进台账待全书统一） |
| 7 | 原句 10／13 块**开头缺 `‘`**（从句子中间截起） | 同上，提示＋台账 |
| 8 | 块数档位：`blocks=13` vs `block_target=[7,11]`，`block_hint` 非空 ⇒ **超限** | 提示型（rc 仍 0）⇒ **禁止增第 14 块**，补漏一律进导航或现有块分析层 |
| 9 | 中文分析层裸英文片段扫描（`sweep_analysis_inline`） | 无未注形态；`md:54` 的「这四个字」是**对英文词组的中文计数表述**，已由 E4 处理 |
| 10 | 专名一致性：`威洛`（本章 `md:10`）vs 总览 `薇洛` | 提示（全书译名台账） |
| 11 | 誓的译法：本章 `不作恶`（4 处）vs ch26／总览 `不伤害`、项目记忆另有 `不做伤害` | 提示（全书译名台账） |

---

## 六、实跑取证（命令 → 输出 → 退出码，原样粘贴）

**A. `海伦[^娜]` 全书 md 扫描（E1）**
```
$ /usr/bin/grep -rn "海伦[^娜]" --include="*.md" . | /usr/bin/grep -v "^./text"
./ch21 the dawn confession.md:124:**为什么这样写**：作者让辛西娅的安慰（"你还是个孩子"）和海伦的反驳正面相撞，…
rc=0
```
⇒ 全书仅此 1 处。

**B. Aspen / 阿斯彭 全书 md（L2）**
```
$ /usr/bin/grep -rin "aspen\|阿斯彭" --include="*.md" .
rc=1
```
⇒ 零命中（原文 `:266` 有）。

**C. 本章推广残留行计数（§〇 3）**
```
$ /usr/bin/grep -c "Lokepub" text/ch21_chapter_21.txt
0
rc=1
```

**D. 星形胎记跨章回收（L4）**
```
$ /usr/bin/grep -rn "raspberry-coloured star\|birthmark" text/
text/ch27_chapter_27.txt:71:Sunlight turned Helena’s hair ablaze. Her eyes were full of need. Pert and perfect breasts…
text/ch21_chapter_21.txt:191:‘My turn.’ Cynthia gasped, …traced the raspberry-coloured star.
text/ch21_chapter_21.txt:194:‘It’s just a birthmark.’
```
ch27:71 全文：`…The birthmark shaped like a star and placed perfectly on Helena’s sternum was almost the same colour of berry red.`

**E. `Hexed Helena` 全书（L8）**
```
$ /usr/bin/grep -rn "Hexed Helena" text/
text/ch21_chapter_21.txt:368:‘So what do you propose? …should I call you Hexed Helena?’…
```

**F. 句长量化（E3／E5／md:114 的「六个词」）**
```python
line 74 : 3 | ‘I am dithering.   4 | And I don’t dither.   3 | This is ridiculous.   23 | I shall just push open…
line 320: 2 | ‘I don’t.   5 | I’m the reason she died.   21 | It’s because of me the villagers swarmed…   6 | A firewitch consumed by mortal flames.
line 332: 3 | ‘I was seven.   6 | Old enough to have done something.   12 | And I tried, but my powers weren’t enough to stop the fire.
```
⇒ `:320` 末句 6 词 ✔（md:114 正确，**不许改**）；`:74` 非单调（E3）；`:332` 递增（E5）。

**G. 引语逐字（R2 机器）**
`chapter.sh --json` → `verdict: ok`，`quotes` 13 块全 `ok:true`，`segment_miss: 0`；`blocks: 13`、`block_target: [7,11]`、`block_hint` 非空；`words: 3631`；`issues: []`。md/corpus 两条路径**先打印确认存在**（沿用 ch19 教训：该脚本对不存在路径也返回 rc=0 空壳）。

**H. 独立第二把尺子（不依赖门禁）**
```
$ python3 /tmp/hx_md_frag.py "ch21 the dawn confession.md" "text/ch21_chapter_21.txt"
checked=13 BAD=0
$ python3 /tmp/hx_frag_check2.py .memory/.../review/ch21/1-suread.json text/ch21_chapter_21.txt
checked=225 BAD=0
```
⇒ md 13 块按 `…` 拆片段后全部为原文子串；R1 素读底稿 225 条证据片段全部为原文子串。

---

## 七、悬置（原文未给，任何一方都不得判定）

| # | 悬置点 | 取证结果 |
|---|---|---|
| U1 | 海伦娜父亲是谁／与母亲的关系 | `text/` 内除 `ch21:266` `my father` 外无具名；不裁决 |
| U2 | 阿斯彭姨妈的结局细节（`follow her heart to its ultimate death` 的死法、地点、对象） | 仅 `:266` 一句，全书 `grep` 再无；不补写 |
| U3 | 爱情药水究竟使人相爱还是使人被奴役 | `:278` 海伦娜自己 `I don’t know if…or…`；书内不定，不得写成结论 |
| U4 | 「圣刃」是哪一种仪式用具／是否即 ch25 的血咒用器 | 仅 `:290` `a sacred blade`；不推断 |
| U5 | 血魔法三分法是否全书通用体系（其他角色是否认同） | 仅 `:284` 海伦娜口述；ch25 辛西娅以血解咒与本章是否同一套，留待 ch25 判定 |
| U6 | 辛西娅当夜是否已知道母亲往事的全部（她的每次反应只有 `:287`/`:293`/`:302` 等台词与动作） | 全章不给辛西娅内心，不得替她补写「她想」 |
| U7 | `:368` `Hexed Helena` 是否即书名副标题的正式呼应（书内再无第二次） | grep 唯一命中；只记双关，不断言作者意图 |
| U8 | 章末 `I won’t.’` 之后辛西娅的反应 | `:372` 起正文结束；md 已如实写「不写辛西娅的反应」✔ |
