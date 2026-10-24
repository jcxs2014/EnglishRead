# ch19 · R3 对账（三张单子）＋ R4 逐块对应

- 素读底稿：`review/ch19/1-suread.json`（396 行源文／184 events／19 rel／18 num／14 unresolved／43 traps；主会话复核 `checked=251 BAD=0`，投毒通过）
- 机器层：`review/ch19/2-machine.json`（`chapter.sh` rc=0；blocks 11／words 3398／`block_target [6,11]`＝**触顶（无 block_hint）**／segments 12／`segment_miss 0`）
- md：`ch19 the duchess and the coven.md`（172 行；11 引语块；词表 24 条＝9/9/6）
- **读取顺序**：先 `text/ch19_chapter_19.txt` 全文（主会话本回合通读 396 行）→ 复核子代理 `1-suread.json` 的逐字与 43 条 traps → 再跑 `chapter.sh` → **最后**才开 md。铁律未破。
- ⚠️ 主会话第一轮把 md 文件名写成 `ch19 the blood moon ritual.md`（**不存在**），`chapter.sh` 仍返回 rc=0 并输出一份 `chapters 0 / blocks 0` 的空壳 JSON。**判据新记**：`chapter.sh` 对不存在的 md **不报错**——凡机器层数字异常整齐（blocks 0／words 0），先核 `book` 字段的路径是否真存在。空壳件已被真跑结果覆盖。

## 〇 结构要点

1. 正文 `:35`–`:396`；`:1`–`:34` 是提取件章节标题行（`:1` `Chapter 19`、`:22` `19`）。
2. **两段视角、一次切换**：`:35`–`:188` 贴辛西娅，`:216`–`:396` 贴海伦娜。分场处 `:189`–`:215` 是空白带，其中 **`:194`／`:197` 是 Lokepub 推广插行**（本章是全书 8 条推广行之一，见 §六）。原文**没有**场景分隔符，靠空白带切场。
3. 章内场景：梅菲尔宅客厅（`:38`–`:86`）→ 浴室（`:92`–`:137`）→ 卧室梳妆处（`:146`–`:188`）→ 布莱尔宅餐厅（`:216`–`:396`）。第 2、3 场之间无空行分场标记。
4. **无 tag 台词共 4 处**（本章最高危）：`:41`（公爵夫人，由 `:41` `The Duchess of Devon sat on Cynthia's rose settee` 定）、`:119` `‘Oh my.’`（辛西娅）、`:348`/`:351`/`:357` 的一问一答（`:351`/`:357` 属辛西娅，`:348` 是哈姆雷特的动作）、`:375` `Can you hear the thoughts of other animals?`（**无标签**，按 `:366` 罗温已开口推断）、`:396` `‘Because Hamlet is Cynthia’s familiar.’`（**无标签**，按 `:387` Clio asked their aunt ＋ `:390` 罗温点头推断）。
5. **无引号心声共 6 处**：`:59`（全章最重要的一条）、`:77` 末句、`:182`、`:240`、`:267` 末句、`:315`、`:273` `She’s nervous.`、`:384` `It was impossible.`（属海伦娜）。
6. 哈姆雷特是**狐狸**（`:354` `A low growl rumbled in the fox’s chest.`）、雄性、此前一直是**海伦娜**的魔宠：`ch02:38` `Hamlet, her familiar and constant companion`、`ch13:98` `Helena’s familiar`、`ch14:78`/`ch14:357` `her familiar`。`:396` 是「**也是**辛西娅的」这一反常事实的**首次点破**。
7. 「偷力量」在本章被**正面否定**：`:342` `‘You aren’t stealing my magic, Cyn. Your power comes from within you.’`；`:324` 海伦娜以母亲的先例否证；`ch20:204` 罗温姨妈进一步定为规则。**md 与后续修复都不得把它写成可能成立**。
8. 「一只魔宠事二主」的**解释在 ch20，不在 ch19**：`ch20:41` `So how the bloody hell is he Cynthia’s familiar as well?`、`ch20:47` `Hamlet is my familiar. He chose me. How can he also be Cynthia’s?`、`ch20:53` `Rare occurrences when a familiar chooses two witches. Those witches are bound to each other.` ⇒ **ch19 只抛出事实，未给机制**；md 若解释「为什么也是她的」就是跨章补写。

## 一 「漏」——素读有、md 无

| 编号 | 原文（`text/ch19:行`） | md 现状 | 档 |
|---|---|---|---|
| **L1** | `:59` `If only she knew. Imagine if I told her I was investigating Hubert’s murder while finding myself increasingly more attracted to an untitled, magical woman who thinks I might also be a witch. Scandalous indeed!` | **全篇零提及**。这是**无引号心声**，却把本章三件不可说之事（查谋杀案／被无头衔的女巫吸引／自己疑似女巫）一次说完，而且紧挨在公爵夫人的台词之后。md:46「公爵夫人不知道海伦娜是谁」这条判断的**证据正是这一段**——它没被说出来，所以公爵夫人不知道。md:12「公爵夫人关于『丑闻』的怂恿」用的 `Scandalous indeed!` 也出在这里。 | **阻断** |
| **L2** | `:324` `When Helena’s mother allowed her powers to be used by the man she chose to love, he never manifested the magic within himself. Helena couldn’t remember a single case of someone stealing another witch’s power and making it their own.` ＋ `:330`/`:333`/`:336` 三级递进（`‘There is another possibility.’` → `‘One that makes far more sense,’` → `‘One that would require you to accept a part of yourself you may have locked away for a very long time.’`） | md:10 只写「海伦娜说她的力量来自她自己」，md:12 只写「实际是她自己的力量在苏醒」。**海伦娜否定的两条依据（母亲先例＋无人有先例）与揭幕前的三级递进全篇未收**；而 md:12 自己把这一处列为「反转」——反转的文本机制没落进任何一个引语块或导航行。 | **阻断** |
| L3 | `:35` `the Mayfair mansion that would soon belong to another Marquess of Kentmore` ＋ `They agreed Cynthia would come to Blair House at eight that evening` ＋ `a gift of time she greatly needed` | md 全篇未提宅邸即将转给下一任侯爵（辛西娅寡居地位的时限），也未提「八点」这个约定时间；md:10 直接说「视角转到布莱尔宅」，读者不知道这是约好的地点。 | 提示（重） |
| L4 | `:101` `She had never engaged in self-play. As a child, she was taught that touching between her legs was forbidden. … she had no desire to touch herself because nothing inspired the tingling sensations that now erupted every time she saw Helena. Every time Helena touched her, even if it was just the innocent press of her fingers against Cynthia’s back.` | md:10 断言「第一次尝到这样的欢愉」，但**这句话的证据（从未自我抚慰＋此前任何触碰都不起感觉）没有进任何块**；`:101` 末两句还把 ch18 `:35`「海伦娜把手放在她后腰推进屋子」那一次接触接上了。 | 提示（重） |
| L5 | `:110` `Slow. Soft. Harder. Faster. Tighter circles… Would her grey eyes turn silver with desire? … She thought of kissing her in the rain` ＋ `:113` `The orgasm ripped through her with shocking speed… Water spilled over the side of her copper tub.` | 块 4 收 `:107`（事前）、块 5 收 `:131`（事后），**中间的高潮段整体跳过**；`:110` 的「雨里接吻」是跨章回指，md 未标。 | 提示（重） |
| L6 | `:125` `No wonder people made such a fuss.` ＋ `:128` `Just a thrusting invasion that ended with him wiping himself clean and wishing her a pleasant evening. If he had ever reached such a peak, he did so alone.` | md:66 说「这不是她想起丈夫的好，而是丈夫的罪把她的快乐截断」，但**这段对比才是那句话的内容**，md 全篇没写婚姻性事的具体质地。 | 提示（重） |
| L7 | `:143` `Something needed to be done. She couldn’t banish him from her memories until she first made some kind of amends for his horrific crimes.` | md:66「她还没有把休伯特的事处理完，所以这份新感情总会被打断」的**唯一原文依据**，md 未收进任何块。 | 提示（重） |
| L8 | `:146` `as she hadn’t replaced her lady’s maid, she dressed herself` | md 零提及。这一句既交代她**没有女仆**（与 `:41` 公爵夫人的 lady’s maid 形成对照），也解释她为何自己穿衣。 | 提示 |
| L9 | `:173` `Covering her quivering lips with her hand, Mrs Higgins blinked furiously. ‘Oh, Lady Burrows.’` ＋ `:179` `Her housekeeper cleared her throat and firmed her lips, always ready to tackle any mess, no matter how disastrous. ‘Of course. It would be my pleasure.’` | md:10 只写「叫来希金斯太太，要她找出地址」；**受托者本人的震动与应承、以及 `:179` 对她是 housekeeper 的定名**都没进 md。 | 提示 |
| L10 | `:182` `It would never be enough. But it would be something.` | 无引号心声，补偿这一决定的道德落点；md 零提及。 | 提示 |
| L11 | `:225` `He gave up on Helena’s twentieth turn from the dining room table to the hearth. Padding over to Ellie and Ophelia, the ferret scampered down Ellie’s bluebell skirt to wind herself around Hamlet, rubbing her face against his in interspecies infatuation.` | md 零提及。踱步圈数（第二十次）、雪貂奥菲莉亚的**雌性**（herself）与跨物种痴迷都没收；块 9/10 用到奥菲莉亚却未交代她与哈姆雷特的关系。 | 提示 |
| L12 | `:228` `Clio had joined them for dinner after receiving Helena’s desperate note.` ＋ `:231` `‘Murder!’ Sir Robin flapped his impressive wings.` ＋ `:234` `Sir Robin.` / the raven bobbed his head ＋ `Aunt Rowan raised her brow as the raven bobbed his head.` | 克莱奥是**被海伦娜的急信叫来的**、渡鸦罗宾爵士会开口答话（世界观要素）——md 全篇没写；md:10 只写「海伦娜为晚宴坐立不安」。 | 提示 |
| L13 | `:237` `‘She could reject her powers, decide we are a bunch of devil worshipers, and refuse to ever speak to us again.’ … But this was unprecedented.` | md:11 用「担心被拒绝」四字压缩，**海伦娜担心的三件具体事（拒绝自己的力量／认定她们是拜魔鬼／永不再来往）一条没落**；`unprecedented` 一词在词表 md:142 出现，但分析层没碰。 | 提示（重） |
| L14 | `:240` `As if the world weren’t about to end.` ＋ `:243`/`:246`/`:249`/`:252`（`You are an infuriatingly optimistic woman.` → `Hel! You say the sweetest things.` → `That wasn’t a compliment.` → `that is how I received it.`） | md 零提及。`:240` 是**海伦娜视角下的恼怒评注、不是台词**；这段对答还是本章唯一的喜剧减压。 | 提示 |
| L15 | `:255` `Aunt Rowan’s calm voice made the plants shift and sway as if a warm breeze blew through the dining room.` ＋ `:336` `As Aunt Rowan spoke, the potted palm in the corner vibrated, emitting a low hum similar to a cat purring.` | **罗温姨妈的声音带动植物**在本章出现两次，md 一次没写——这是她发言权重的设定证据，也是 `:390` 她能定音的铺垫。 | 提示（重） |
| L16 | `:267` `This ensemble had a scooped neckline… Tiny obsidian beads… making her glitter like a galaxy of stars. … Helena wished to strip her bare and see her true shape.` | md:10 只有「辛西娅穿黑裙到来」。**`:267` 末句是无引号的海伦娜心声**（欲望方向），md 未收，也未标它的归属。 | 提示（重） |
| L17 | `:270` `Cynthia addressed Aunt Rowan, but her gaze found Helena. She twisted her fingers together.` ＋ `:273` `She’s nervous.` | 「话给罗温、眼给海伦娜」的错位，与 `:273` 无引号心声（属海伦娜）均未收。 | 提示 |
| L18 | `:282` `Ellie elbowed her sister. ‘Don’t be a brat.’ As an empath who could read people’s auras, she would no doubt know exactly how much Cynthia needed all their reassurances.` | **埃莉是共感者、能读气场**——本章巫团能力的唯一说明句，md 零提及；`her sister`（＝克莱奥）这层姐妹关系也没写。 | 提示（重） |
| L19 | `:285` `‘There’s no need to fear, Cynthia. We are all here to support you. No matter what we discover tonight.’` | md 零提及；这句是 U13「今晚原计划要发现什么」的出处。 | 提示 |
| L20 | `:291`/`:294`（`Ellie’s turbot`／dill and butter sauce）＋ `:297` `Candles had been lit, and a window was open… fragrant with blooming jasmine.` ＋ `:306` `They talked of the apothecary shop, the investigation, London’s new obsession with crinolines, and the candidate running for the presidency in America.` ＋ `after Clio brought out the melange` | 晚宴实物与四项话题、蜡烛的**被动语态**（点蜡者原文未写）均未收；`:306` 的四项话题正是「她们把辛西娅当自己人」的证据。 | 提示 |
| L21 | `:312` 前半：`I know many women in the beau monde, from duchesses to baronets, but I have few chuckaboos, and none with whom I can be completely honest.` ＋ `And then I met Clio.` ＋ `She reached under the table and took Helena’s hand.` ＋ `Helena’s heart quickened.` | 块 8 的引语从 `Her fingers slipped away…` 起，**「先伸手握住」这半句在引语之外**，而 md:90 的「滑开」必须靠它才成立；`chuckaboos`／公爵夫人与从男爵的爵位倒序（T35）也没进 md。 | 提示（重） |
| L22 | `:315` `Helena’s chest tightened. What was she on about? Was something like that even possible? She looked to Aunt Rowan, whose brow crinkled in concern.` | 无引号心声＋罗温的**关切表情**（她早有预感）均未收；这块直接支撑 `:390` 的点头。 | 提示（重） |
| L23 | `:321` `‘Because it is the only explanation.’ … ‘If you can put some kind of hex or spell on me to get me to stop, I will willingly submit myself.’` | md 零提及。**这是 ch17 `:212`（`Perhaps they could bespell her to stop stealing Helena’s magic… But she would miss Helena more`）的兑现**——她当时愿失去力量换海伦娜不离开，此刻主动要求被施咒；两章连读才成立，md 两侧都没接。 | 提示（重） |
| L24 | `:327` `Cynthia shrugged, the neckline of her gown shifting with movement and momentarily distracting Helena.` | md 零提及（海伦娜注意力被身体牵走的细节）。 | 提示 |
| L25 | `:345`–`:360`：`‘It can’t be true. I can’t possibly be a witch.’` → `He yipped, and she shook her head.` → `‘I don’t know. Maybe I’m just imagining things.’` → `A low growl rumbled in the fox’s chest.` → `‘I am not being silly!’ Cynthia’s voice rose indignantly.` → `‘Darling, are you having an argument with Hamlet?’` | md:10 用「与哈姆雷特争执被埃莉撞见」一句带过；**这段里 `:351`/`:357` 两句台词没有说话人标签**（T38），md 未标；`:354` 首次以 `the fox` 定种也未标。 | 提示（重） |
| L26 | `:369` `Cynthia’s cheeks paled, and Helena reached for her hand. Cynthia’s fingers were like ice.` | md 零提及——这是本章海伦娜第二次主动接触（第一次是 `:276` 拥抱）。 | 提示 |
| L27 | `:384` 末句 `It was impossible.` | 块 11 的引语止于 `…from her head.`，把 `It was impossible.` 截在引语外；md:124 说「作者没有告诉她想到了什么」，但**这句正是海伦娜自己给那个念头盖章否定**，且被 `:396` 当场推翻——少了它，块 11 的「不肯接受」少一层。 | 提示 |

> **L1 为什么是阻断**：md:46 的「公爵夫人不知道海伦娜是谁」与 md:12 的「关于『丑闻』的怂恿」都把 `:59` 当前提使用，却全篇不引它；同时这段是本章**最容易被读者误当公爵夫人台词**的一行（无引号、紧接其台词之后）。属 S1「漏掉关键转折 ＋ 判据 (b) 关键证据链缺位」。**修复位置**：块数 11 已**触** `block_target [6,11]` 上限 ⇒ **禁增第 12 块**，只能写进导航（md:10 或 md:14）。
> **L2 为什么是阻断**：md:12 明写「反转有三处：辛西娅以为自己在偷力量，实际是她自己的力量在苏醒」——本章最大的一次反转，其**全部文本依据**在 `:324`/`:330`/`:333`/`:336`，md 一处未收；判据 (d)（内容断言与其自身证据缺失并存）＋ S1。同属**禁增块**，写进 md:12 或 md:13。

## 二 「编」——md 有、原文无

**0 条独立凭空项。** 有 3 条「由原文未写推来的否定／归属断言」，均归入 §三（E9/E10/E12，因原文两侧都有对应物或可 hedge）。

被排查后**不成立**的疑点（逐条留证）：

| md 位置 | 疑点 | 回原文结论 |
|---|---|---|
| md:10 | 「德文公爵夫人不请自来」 | **成立**。`:38` `pushed open the door to her parlour and nearly screamed in shock`；`:41` 她已坐在沙发上；`:50` `I thought it best I come check on you` |
| md:10 | 「邀她两周后赴夏季宴会」 | **成立**。`:68` `To my summer soirée`；`:86` `The ball is in a fortnight.` |
| md:10 | 「还要她『带上情人』」 | **成立**。`:86` `Bring your paramour with you to my party. I dare you.` |
| md:10 | 「说她已经躲快乐太久」 | **成立**。`:86` `You have spent far too long hiding from pleasure, Cynthia.` |
| md:10 | 「浴缸里第一次尝到这样的欢愉」（证据见 L4） | **成立**。`:101` `She had never engaged in self-play.`＋`:113` `The orgasm ripped through her with shocking speed.` |
| md:10 | 「想到海伦娜，随后被休伯特的影子打断」 | **成立**。`:98`/`:110` → `:131` `Thoughts of Hubert destroyed the echoes of pleasure` |
| md:10 | 「要她找出所有被休伯特辞退的女仆地址，准备补偿」 | **成立**。`:164` `I need you to find all the addresses of the maids Hubert terminated.`＋`:170` `I am going to make reparations. For Lily, and the rest.` |
| md:10 | 「视角转到布莱尔宅」 | **成立**（地点由 `:35` `Cynthia would come to Blair House at eight that evening` 推得；`:258` 前门有knock、`:297` 餐桌）。原文第 2 场未再复述宅名 ⇒ 属**有据推断**，非凭空。 |
| md:10 | 「辛西娅穿黑裙到来」 | **成立**。`:267` `She was wearing yet another black gown.` |
| md:10 | 「海伦娜不由自主地抱了她」 | **成立**。`:276` `Forgetting her own jitters in the need to reassure Cynthia, she closed the distance… before realising her actions.` |
| md:10 | 「席间辛西娅坦白『我想我一直在偷海伦娜的力量』」 | **成立**。`:312` 逐字（引号内原话即 `I think I have been stealing Helena’s power.`） |
| md:10 | 「海伦娜说她的力量来自她自己」 | **成立**。`:342` `Your power comes from within you.` |
| md:10 | 「辛西娅与哈姆雷特争执被埃莉撞见」 | **成立**。`:345`–`:357` 争执；`:360` `‘Darling, are you having an argument with Hamlet?’`（埃莉，`:359` 前句无 tag 但 `:360` 由 `Ellie cleared her throat.` 定） |
| md:10 | 「因为哈姆雷特**也**是辛西娅的魔宠」 | **「也」字有跨章背书**：`ch02:38` `Hamlet, her familiar`（海伦娜的）＋`ch20:41` `how is he Cynthia’s familiar as well?`＋`ch20:53` `a familiar chooses two witches` ⇒ 「也是」不是凭空，但 **ch19 本身没给「为什么也能」的机制**（见 §〇 8），md 不得补写。 |
| md:11 | 「休伯特的阴影又把她拉回罪责，最后她把羞愧转成补偿行动」 | **成立**。`:137` `The heavy weight of her husband’s sins`→`:149` `She couldn’t escape the shame of her own blindness`→`:170` reparations |
| md:11 | 「拥抱被发现」 | **成立**。`:279` `Clio’s sly comment had Helena dropping Cynthia’s hands and stepping back awkwardly.` |
| md:11 | 「最后在『魔宠』真相前失去掌控」 | **成立**。`:393` `Helena’s world spun out of control.` |
| md:12 | 「爱管闲事的贵妇、浴缸里的自我发现、晚宴坦白、魔宠认主都在」 | **成立**（四处各有对应：`:41`/`:95`–`:125`/`:312`/`:396`） |
| md:13 | 「她对海伦娜的感情从想象走到说出口的边缘」 | **成立**。`:98`/`:104`/`:110` 想象；`:270` 致谢时 gaze found Helena；`:312` 说出口的是偷力量不是爱 |
| md:13 | 「她一直用『朋友』包装自己」 | **成立**（跨章）。`:377` ch18 `I’m just being a friend.`；本章 `:312` `Your friendship means so much` |
| md:13 | 「公爵夫人是催化剂，罗温是揭幕者」 | **成立**（评价性判断）：`:95` 公爵夫人的话在她脑中回放；`:390` 罗温点头、`:396` 定音 |
| md:14 | 「中间隔着一道空白和水印广告（引语不碰）」 | **成立**。`:194`/`:197` 推广行，md 明确排除 |
| md:14 | 「浴缸一段用短句和生理细节」 | **成立**。`:110` `Slow. Soft. Harder. Faster.`；`:113`/`:116` 生理 |
| md:14 | 「章末用连续短段加速：问句、眼神、点头、揭晓，一句一顿」 | **成立**（实测）：`:387` 问句 1 句／`:390` 眼神＋点头 2 句／`:393` 1 句／`:396` 1 句；`:381`/`:384` 亦短段 |
| md:26 | 「公爵夫人是不请自来的；她坐在辛西娅的沙发上，却像主人」 | **成立**。`:41` `The Duchess of Devon sat on **Cynthia’s** rose settee`；`:86` 她离场 `swept out of the door` |
| md:44 | 「她没有问辛西娅有没有情人，直接把这件事当成既成事实」 | **成立**。`:86` 直接 `Bring your paramour`，无疑问句 |
| md:56 | 「下一段她的体验才会构成转折」 | **成立**。`:107`（块 4）→`:110`/`:113`（体验）顺序正确 |
| md:66 | 「她还没有把休伯特的事处理完」 | **成立**。`:143` |
| md:86 | 「克莱奥随后的打趣会点破这一点」 | **成立**。`:279` |
| md:96 | 「她说的是『我想』，不是『我知道』；这是她的推断」 | **成立**。`:312` `I think I have been stealing` |
| md:116 | 「这次测试只证明她听不见罗宾爵士和奥菲莉亚，不等于她没有魔法」 | **成立**。`:378` 挨个盯看 →`:381` `‘No. I can’t. How strange.’`；且 `:342` 已肯定她自有力量 |
| md:124 | 「作者没有告诉她想到了什么，只让身体先反应」 | **成立**（`:384` 只写 Prickles/premonition/Fear，念头内容直到 `:396` 才落地） |
| md:126 | 「罗温看她一眼、点头，**章末那句**才把答案说破」 | **成立**，且**没有把 `:396` 归给具体说话人** ⇒ 这是本章最稳妥的一处 hedge（与 md:171 相对，见 E12） |
| md:171 | 「罗温看了海伦娜一眼，点头**说**——因为哈姆雷特是辛西娅的魔宠」 | 前半成立（`:390`）；**「说」把无标签句归给了罗温** ⇒ 见 E12 |

## 三 「错」——两边都有但不一致

| 编号 | md 位置 | md 原文 | 原文依据 | 档 |
|---|---|---|---|---|
| **E1** | md:114（块 10 · 为什么这样写） | 「这个测试比一句结论更有说服力，**也给罗温的追问铺了路**。」 | `:366` `Aunt Rowan’s gaze sharpened. ‘You can hear him?’` 与 `:375` `‘Can you hear the thoughts of other animals?’` **都在 `:378`（块 10 的引语）之前**；`:378` 之后是 `:381` 辛西娅答『No. I can’t.』、`:387` **克莱奥**发问、`:390` 罗温点头。**罗温的追问在前，测试在后 ⇒ 章内时序写反**（本库缺陷簇第一名）。 | **阻断** |
| **E2** | md:44（块 3 · 为什么这样写） | 「**三个短句**像连发的挑衅：先给邀请，再下战书，最后把『反叛』说成一种可以尝的东西。」 | 块 3 的引语（md:38）实为 **4 句**：`Bring your paramour with you to my party.`／`I dare you.`／`Do something inappropriate, for once.`／`You might find you quite like rebellion.`（8-3-6-8 词）。**被 md 自己引的这段当场可数证伪** ⇒ 判据 (f)。 | **阻断** |
| E3 | md:80（块 7 · 中文理解） | 「于是走近，把她**轻轻**抱住」 | `:276` `pulled her into a **quick** hug`——原文写的是**快**（随即 `:276` `before realising her actions`），不是「轻柔」。md:84 的论点（动作先于意识）正靠这个「快」支撑，译成「轻轻」削掉了它。 | 提示（重） |
| E4 | md:84（块 7 · 为什么这样写） | 「**作者把顺序倒过来写**，拥抱就显得不是设计好的礼节」 | `:276` 本身**按时间顺序写**：`Forgetting… she closed the distance and pulled her into a quick hug… before realising her actions`。真正倒置的是「觉」与「行」（先做后觉），不是叙述顺序；md 前半句「动作发生在意识之前：先『忘了』，再『抱住』，最后才『意识到』」已经说对了，后半句自我矛盾。 | 提示（重） |
| E5 | md:24（块 1 · 为什么这样写） | 「**作者不写辛西娅怎么惊讶**，先用『你没回信』把公爵夫人的理直气壮摆出来」 | `:38` 就在引语上一行：`…and nearly screamed in shock`——惊讶写了，只是不在块 1 的引语里。判据 (i)（同类否定断言但字面仍可成立）⇒ 判提示不判阻断。 | 提示（重） |
| E6 | md:50 / md:54 / md:56（块 4） | 「辛西娅**一直觉得**，那只是……又一次夸张」／「最后用『**一直觉得**』把辛西娅的怀疑坐实」／「记住『她**一直觉得**是夸张』」 | `:107` `Cynthia **thought** it was one more exaggeration`——过去时单次判断，无持续体；「一直」是补写的时距。判据 (g)（引语内属性被补写、同章可核）。 | 提示 |
| E7 | md:94（块 8 · 为什么这样写） | 「碎屑**越拢越小**，话却越说越重」 | `:312` `gathering crumbs into a **small pile**`——原文只说拢成一小堆，没有渐进过程；「越…越…」是本可数的形式断言（此处不可数，故降档）。 | 提示 |
| E8 | md:104（块 9 · 为什么这样写） | 「不用解释，读者也能看出**它在替谁说话**」 | `:342` 只写哈姆雷特把爪子放在同一处、呜咽注视；「替谁说话」把「位置呼应」升级成「代言」。引语外新增解释 ⇒ 判据 (e)。 | 提示 |
| E9 | md:106（块 9 · 读者视角提示） | 「哈姆雷特**不是在讨食**，它是在**回应辛西娅的情绪**」 | 原文两处都没写动机：`:342` 只给动作（paw／Whining／golden gaze），`:354` 才给 growl。本章亦**没有任何进食场景与哈姆雷特相关**（`:291` turbot、`:306` melange 都是人的食物）。前半是「原文未写 ⇒ 否定」，后半是动机断言 ⇒ 判据 (c)（暗示升级为定论）。 | 提示 |
| E10 | md:46（块 3 · 读者视角提示） | 「公爵夫人**不知道**海伦娜是谁」 | 原文只写了她**没说出来**（`:59` 是无引号心声）；「不知道」是由 `:80` `something, or someone has brought joy back to your face`（她只是察觉「有人」）推来的否定。**方向没错，但需要 hedge**：写成「原文没写她知道」。 | 提示 |
| E11 | md:12（Tropes 第 2 条） | 「公爵夫人关于『丑闻』的怂恿，**反而成了她面对真相的推力**」 | 本章有两条独立因果链：① `:95` 公爵夫人的话回放 →「Hiding from her true self?」→ 浴室；② `:137` 丈夫的罪 + `:149` 对自己盲见的羞愧 → `:170` reparations。**补偿行动的推力是②，不是①**；md:12 把两条并成一条。 | 提示（重） |
| E12 | md:10／md:171 | md:10「罗温看了海伦娜一眼，点了点头——因为哈姆雷特也是辛西娅的魔宠」；md:171「罗温看了海伦娜一眼，**点头说**——因为哈姆雷特是辛西娅的魔宠」 | `:396` **无说话人标签**。按 `:387` `Clio asked their aunt.` 推断最可能是罗温（U8／T43），但原文未证实；**md:126 用「章末那句」不点名，md:171 却用「点头说」定人**——同一 md 内部对同一件事一 hedge 一定，属自相矛盾。 | 提示 |
| E13 | md:11 | 「后半是海伦娜的紧张与失控：**从担心被拒绝**」 | `:237` 的具体内容是「辛西娅可能拒绝自己的力量／认定她们是 devil worshipers／永不再理她们」；「担心被拒绝」压缩到可读成「海伦娜怕辛西娅不接受她的感情」。不算错，但丢内容。 | 提示（轻） |
| E14 | md:134 / md:135 | `embroidery`、`expectations` 放在 ⭐⭐⭐ 高级 | 两词都是常用词（`expectations` 更是基础词频）⇒ **档位注水**（S4 ③，与 ch17 E11 同类）。建议降到 ⭐⭐／⭐。 | 提示 |
| E15 | md:137 | `dunderheads` 的例句 `‘Decorum is for dunderheads.`——**开头残留原文开引号 `‘`、且无闭引号** | `:80` 原句确有 `‘`，属格式瑕疵（`check_vocab.py` 不查）；与 ch17 E10 同型。 | 提示 |

### E1 专节 · 本章的「问—答」链（时序纠错的底账）

```
:366 Aunt Rowan’s gaze sharpened. ‘You can hear him?’          ← 罗温追问①（有 tag）
:369 Cynthia’s cheeks paled, and Helena reached for her hand.
:372 ‘Yes.’                                                    ← 辛西娅（无 tag，答①）
:375 ‘Can you hear the thoughts of other animals?’              ← 追问②（无 tag，推断＝罗温）
:378 Cynthia blinked rapidly. She turned to Sir Robin, then Ophelia… ← **测试**
:381 ‘No. I can’t. How strange.’                                ← 辛西娅答②
:384 Prickles erupted over Helena’s skin… It was impossible.
:387 ‘Why would she only be able to hear Hamlet’s thoughts?’ Clio asked their aunt. ← 克莱奥发问
:390 Aunt Rowan met Helena’s gaze… She nodded her head.
:393 Helena’s world spun out of control.
:396 ‘Because Hamlet is Cynthia’s familiar.’                    ← 无 tag，推断＝罗温
```
⇒ 块 10（`:378`）能铺的是 **`:387` 克莱奥的发问**，不是罗温的追问。**改法见 `4-verdict.md` §四。**

### 时序专查（其余无缺陷）

| md 断言 | 原文顺序 | 结论 |
|---|---|---|
| md:10 全章顺序（公爵夫人 → 浴缸 → 希金斯 → 布莱尔宅 → 到客 → 拥抱 → 坦白 → 否定 → 与哈姆雷特争执 → 罗温问 → 只听得见哈姆雷特 → 克莱奥问 → 点头 → 揭晓） | `:41`–`:86` → `:92`–`:137` → `:158`–`:188` → `:216`–`:258` → `:261`/`:267` → `:276` → `:312` → `:342` → `:345`–`:357` → `:366`/`:375` → `:378`/`:381` → `:387` → `:390` → `:396` | **成立**（唯一反例是 E1，出在块内分析层，不在导航行） |
| md:11「前半…第一次为自己活，休伯特的阴影又把她拉回罪责，最后她把羞愧转成补偿行动」 | `:113`/`:125` → `:131`/`:137` → `:143`/`:149`/`:170` | **成立** |
| md:56「下一段她的体验才会构成转折」 | `:107` → `:110`/`:113` | **成立** |
| md:64「三句从身体内部走到外部温度」 | `:131` 三句：destroyed the echoes（内）→ couldn’t hold Helena（心）→ shivered in water now cold（外） | **成立**（实测 3 句） |
| md:126「克莱奥随后问出…罗温看她一眼、点头，章末那句才把答案说破」 | `:381` → `:384` → `:387` → `:390` → `:396` | **成立** |

## 四 R4 逐块对应（人判，含固定三问）

| 块 | md 行 | 引语落点 | 中文是在讲这句引语吗 | ①动词主语 ②受事 ③归属方向 | 关键词在引语内 |
|---|---|---|---|---|---|
| 原句 1 | md:18 | `:41` | ✅ | `didn’t respond` 的逻辑主语＝Cynthia、说话人＝公爵夫人（`:41` 后句 `The Duchess of Devon sat…`）→ md「你没回我的信」+ 归给公爵夫人 ✅ **未把开场白安给辛西娅（T5 未踩）**；`her lady’s maid` 的 her＝公爵夫人 → md「让她的女仆」✅ 未调转 | didn’t respond ✅ / rose settee ✅ / silver hair ✅ / hours to create ✅ |
| 原句 2 | md:28 | `:80` | ✅ | `swished over`／`taking her chin`／`moving her head` 主语＝公爵夫人 ✅；`her chin` 的 her＝**Cynthia** → md「捏住她的下巴」✅ 未误成公爵夫人自己的下巴；`you are a marchioness whose closest friend is a duchess` → md「你是侯爵夫人，最好的朋友是公爵夫人」✅ | Decorum ✅ / dunderheads ✅ / closest friend ✅ / chin ✅ |
| 原句 3 | md:38 | `:86` | ✅（句数错，见 E2） | 说话人＝公爵夫人 ✅；`Bring your paramour` 的 your＝Cynthia → md「把你的情人带来」✅；`I dare you` 的施动者＝公爵夫人、受事＝Cynthia ✅ 未倒 | paramour ✅ / I dare you ✅ / inappropriate ✅ / rebellion ✅ |
| 原句 4 | md:48 | `:107` | ✅（时距补写见 E6） | `She had heard of` 的 She＝Cynthia ✅；`her dear friend, the Duchess of Devon, waxed poetical` 主语＝公爵夫人 → md「公爵夫人…讲起」✅；`Cynthia thought it was one more exaggeration` 的判断者＝Cynthia ✅ **未把「夸张」这个评价安给叙述者或公爵夫人** | cataclysmic ✅ / paroxysms of pleasure ✅ / exaggeration ✅ / drama ✅ |
| 原句 5 | md:58 | `:131` | ✅ | `Thoughts of Hubert destroyed…` 施动者＝念头 ✅；`She couldn’t hold Helena in her mind` 的 She＝Cynthia、被留住者＝Helena ✅ 方向未倒；`water now cold` 属辛西娅的浴水 ✅ | destroyed ✅ / echoes of pleasure ✅ / lingered ✅ / water now cold ✅ |
| 原句 6 | md:68 | `:188` | ✅ | `held hostage to a man like Hubert Burrows` 的 hostage-holder＝男人、被扣者＝women → md「被…扣作人质」✅ 未倒；`Including me` 的 me＝Cynthia → md「包括我」✅；`The woman who was beginning to teach Cynthia…` 的 The woman＝Helena → md「那个正在教她想象更好生活的女人」✅ **未把教导者写成辛西娅自己** | hostage ✅ / Including me ✅ / evening plans ✅ / dream of something better ✅ |
| 原句 7 | md:78 | `:276` | ✅（manner 词错见 E3；叙述顺序见 E4） | `she closed the distance / pulled her into a quick hug / pressing a kiss to each cheek` 主语＝**Helena**（`:273` `She’s nervous.` 是她的心声）→ md「她…抱住…两边脸颊各亲了一下」✅ 未安给辛西娅；`reassure Cynthia` 的受事＝Cynthia ✅；`before realising her actions` 的实动者＝Helena ✅ | Forgetting ✅ / quick hug ✅ / kiss to each cheek ✅ / before realising ✅ |
| 原句 8 | md:88 | `:312` | ✅ | `Her fingers slipped away from Helena’s` ＝辛西娅的手指离开海伦娜的手指 → md「她的手指从海伦娜手里滑开」✅ **未把「抽回」安给海伦娜（T34 未踩）**；`she released her hand / began gathering crumbs` 主语＝Cynthia ✅；`‘…I think I have been stealing Helena’s power’` 偷的方向＝辛西娅←海伦娜 → md「偷海伦娜的力量」✅ 未调转 | fingers slipped away ✅ / crumbs ✅ / kept her focus ✅ / stealing Helena’s power ✅ |
| 原句 9 | md:98 | `:342` | ✅（动机断言见 E8/E9） | `Hamlet stood… He padded… put **his** paw on **Cynthia’s** lap` → md「把爪子搭在辛西娅膝上」✅ 施受未倒；`where he was curled up with Ophelia` 的 he＝哈姆雷特 ✅；`almost exactly where Helena had squeezed her knee` 的施动者＝Helena → md「海伦娜刚才捏过的地方」✅ | stood from the pillow ✅ / paw on Cynthia’s lap ✅ / exactly where ✅ / Whining ✅ |
| 原句 10 | md:108 | `:378` | ✅（时序反例见 E1） | `Cynthia blinked / turned to Sir Robin, then Ophelia / staring at each animal` 主语＝Cynthia ✅；`Sir Robin cawed, and Ophelia chittered` 各自主语正确 ✅；`ferret outrage for being abandoned **by Hamlet**` → md「被哈姆雷特丢下的雪貂」✅ **抛弃方向未调转（T40 未踩）**；`what one could only assume` 的推测标记 → md「只能理解成」✅ 保留了 hedge | blinked rapidly ✅ / Sir Robin ✅ / Ophelia ✅ / ferret outrage ✅ |
| 原句 11 | md:118 | `:384` | ✅（引语止点见 L27） | `Prickles erupted over Helena’s skin` 的 experiencer＝Helena ✅；`she pushed the idea from her head` 的 she＝Helena → md「她把这个念头从脑子里推出去」✅ **未把「不肯接受」安给叙述者盖章（T41 未踩）**；`A premonition of what was to come` 归属＝海伦娜 ✅ | Prickles ✅ / premonition ✅ / Fear spiked ✅ / pushed the idea ✅ |

**对应 11/11。** 施事／归属调转 **0 处**——本章最高危的六处（`:41` 开场白归公爵夫人／`:276` 拥抱者＝海伦娜／`:312` 松手者＝辛西娅／`:342` 爪子归属／`:378` 雪貂被谁抛弃／`:384` 念头由谁推开）**全部未踩**。md 对全部 6 处无引号心声中的 4 处（`:59`/`:182`/`:240` 未收，`:267`/`:315` 未收，`:273` 未收）属「漏」不是「错」——见 §一。

## 五 形态

| 项 | 实测 | 本书众数／profile | 结论 |
|---|---|---|---|
| H1 | `# 19. Chapter Nineteen` | `# NN. Chapter NN(英文序数)` | ✅ |
| 导航子项 | 5 | 5 | ✅ |
| 引语块数 | **11** | `block_target [6,11]`（3398 词）＝**恰好触顶，`block_hint` 为空、rc=0**；本书众数 9–13 | ✅ **但⇒ 补漏禁增第 12 块** |
| 子项集 | 中文理解／关键词／为什么这样写／读者视角提示 ×11 | 同 | ✅ |
| 词表 | 标准 Markdown 表格 `| 词/短语 | 释义 | 例句 |`，24 条＝9/9/6 | 新判据（`96b7e557e`） | ✅ |
| 一句话总结 | 有（md:171） | 有 | ✅ |
| frontmatter | `状态: 未读` / `modified: "2026-10-23"` | 同 | ✅ |
| `…` 拼接 | 块 8 的 `tell you that… I think` 对应 `:312` 原文自带的省略号（单段连续引语），非人为拼接；`segments 12 / segment_miss 0` | — | ✅ |

**形态 8/8。**

## 六 语料层与引语逐字（实跑）

```
$ bash scripts/chapter.sh "…/ch19 the duchess and the coven.md" --json > review/ch19/2-machine.json ; echo $?
0
counts.blocks 11 · counts.words 3398 · block_target [6,11] · block_hint 空 · segments 12 · segment_miss 0
form.h1 "19. Chapter Nineteen" · nav_count 5 · issues 9 类全空

$ python3 /tmp/vocab_check_hx.py 19      # 例句是否本章原句
ch19: rows=24 missing=0

$ python3 /tmp/vocab_head_hx.py 19       # 词头是否在本章原文
rc=0（无输出）

$ python3 scripts/verify_fragments_indep.py "…/the-hexing-miss-helena-by-darcy-mcguire"
引语条数 270 ｜ 受检片段 312 ｜ ❌ MISS 0 ｜ ❌ 拼接未标省略号 0 ｜ 缺参照章 0

$ python3 /tmp/hx_frag_check2.py text/ch19_chapter_19.txt review/ch19/1-suread.json   # 主会话复核子代理底稿
checked=251 BAD=0
```

**词表 24 条例句逐条抽核（行号）**：`embroidery:41`／`expectations:53`／`scintillating:56`／`dunderheads:80`／`cataclysmic:107`／`exaggeration:107`／`meticulous:170`／`reparations:170`／`unprecedented:237`／`gossamer:41`／`sapphires:41`／`outrageous:56`／`waxed:107`／`paroxysms:107`／`indignantly:357`／`premonition:384`／`corseted:267`／`voluminous:267`／`settee:41`／`bathtub:95`／`crumbs:312`／`napkin:312`／`gown:267`／`hug:276`。**释义 24 条逐条读毕，无一错解**（`waxed | 变得（poetical，诗兴大发）`、`paroxysms | 阵发，突发`、`reparations | 赔偿，补偿` 三条最易错，均正确）。

**语料层「像广告的正文」扫描**：ch19 **含推广行 2 条**——本章正是判据里的 8 行之一起。
```
$ /usr/bin/grep -nE "Lokepub|can wait quietly|Add one to your list" text/ch19_chapter_19.txt
194:A new book can wait quietly in the background.
197:Add one to your list from Lokepub.
rc=0
```
⇒ md:14 已明确写出「中间隔着一道空白和水印广告（引语不碰）」，**这是本章最该保留的一句**；任何修复都不得删。全书分布：ch03:188／ch08:170,173／ch13:182,185／**ch19:194,197**／ch25:214。

**「偷力量」在本章的定性（供 R5.5 与全书汇总用）**：
```
:342 ‘You aren’t stealing my magic, Cyn. Your power comes from within you.’
:324 Helena couldn’t remember a single case of someone stealing another witch’s power and making it their own.
ch20:204 ‘Magic doesn’t make mistakes.’ Aunt Rowan grounded her. ‘You spoke of stealing Helena’s abilities,
         but that isn’t possible. Humans can’t steal our elemental power.’
```
⇒ **md:10／md:96 的 hedge 与断言方向都正确**（辛西娅没在偷）；修复时不得反向加强成「她确实偷了」。

**「一只魔宠事二主」跨章取证（E12／L 项）**：`ch02:38`（海伦娜的 familiar）→ `ch03:246` `A familiar did not abandon his witch. Ever.`→ `ch07:272` → `ch13:98` → `ch16:251` → **`ch19:396`** → `ch20:41`（`as well`）→ `ch20:47` → `ch20:53`（`chooses two witches`）。⇒ md:10 的「也是」成立，但**机制在 ch20**，ch19 不得补写。

## 七 不裁决（U）

| 编号 | 事项 | 为什么不裁决 |
|---|---|---|
| U1 | `:396` 章末句是谁说的 | **无说话人标签**；按 `:387` `Clio asked their aunt.`＋`:390` 罗温点头推断为罗温，原文未证实 ⇒ md 应标「推断」，不得写成定论（E12）。 |
| U2 | `:375` `Can you hear the thoughts of other animals?` 是谁问的 | 同样**无 tag**；`:366` 是罗温开口，`:372` `‘Yes.’` 是辛西娅，中间这句最可能仍属罗温，但原文未写。 |
| U3 | `:119` `‘Oh my.’`／`:134` `‘You monstrous bastard.’` | 引号内无 tag；按 `:113`–`:137` 全段贴辛西娅推断为她本人（`:134` 的对象＝休伯特）⇒ 可按推断写，不得扩写成他人台词。 |
| U4 | `:188` 那句是**说出口还是心里想** | 带引号但无 tag，`:185` 之后没有听觉动词；`md:70` 用引号呈现是正确做法，**不得判定她「对自己说」或「对希金斯太太说」**（屋里无人在场，但原文也没写她说出声）。 |
| U5 | `:194`/`:197` 与两场之间的时间关系 | 推广行是出版方插入，不是情节时间；`:216` 起已是当晚八点前后的布莱尔宅。原文未给辛西娅出发与到场的时刻。 |
| U6 | 希金斯太太找没找到那些女仆的地址、补偿如何执行 | `:185` 只写 `Mrs Higgins off to find her employment records` ⇒ 本章无下文（U4@底稿）。 |
| U7 | `:86` `summer soirée`（`:68`）与 `The ball`（`:86`）是否同一场 | 原文两个称呼并用，未澄清规模与形式。 |
| U8 | 罗温与海伦娜／克莱奥／埃莉的确切亲缘 | `:216` 海伦娜称 `Aunt Rowan`，`:387` 却写 Clio `asked **their** aunt` ⇒ 血缘还是巫团尊称原文未写。 |
| U9 | `:384` `the idea` 具体是什么 | 原文此处未明写（`:396` 才落地）；md:124「作者没有告诉她想到了什么」是正确处理，**不得在此处提前写出「魔宠」二字**。 |
| U10 | `:324` 「她选择去爱的男人」是不是海伦娜的父亲 | 原文未写 ⇒ 不得指认（底稿 T36）。同时原文也没写这男人是谁、后来如何。 |
| U11 | `:297` `Candles had been lit` 是谁点的 | **被动语态，施动者原文未写** ⇒ 任何指派都是编造（底稿 T33）。 |
| U12 | `:35` `would soon belong to another Marquess of Kentmore` 的新侯爵是谁 | 原文不点名（U1@底稿）。 |
| U13 | `:285` `No matter what we discover tonight` 的「原计划」是什么 | `:309` 之后只出现辛西娅的自白，罗温一方是否有既定议程原文未写（U13@底稿）。 |
