# ch17 · R3 对账（三张单子）＋ R4 逐块对应

- 素读底稿：`review/ch17/1-suread.json`（254 行源文／143 events／24 rel／13 num／12 unresolved／30 traps；`checked=196 BAD=0`，投毒通过）
- 机器层：`review/ch17/2-machine.json`（`chapter.sh` rc=0；blocks 8／words 1894／`block_target [3,6]`／**`block_hint`「块数 8 偏离本章篇幅建议 3–6（本章 1894 词）」**／segments 8／`segment_miss 0`）
- md：`ch17 the dog in cheapside.md`（139 行；8 引语块；词表 22 条＝8/8/6）
- **读取顺序**：先 `text/ch17_chapter_17.txt` 全文 → 写 `1-suread.json`（子代理 R1，主会话复核 traps）→ 再开 md。铁律未破。

## 〇 结构要点

1. 正文 `:35`–`:254`；`:1`–`:34` 是提取件章节标题行。
2. POV **全程贴辛西娅**，无视角切换。`:176` `Act normal.` 是**海伦娜的眼神讯息**（`:173` `The message in her gaze was impossible to miss.`），不是心声、不是 POV 切换。
3. 全章四个空间：起居室（`:35`–`:44`）→ 马车（`:47`–`:122`）→ 齐普赛德街（`:125`–`:194`）→ 利珀特家门口（`:221`–`:254`）。**原文无场景分隔符**。
4. **访谈没有进行**：章末停在门口，开门的高大男人（`:227`，**无姓名 tag**）与从里屋出来的莉莉（`:233`）都还没谈上话。
5. 「偷力量」的猜测在**本章不被证实**，且后文明确否定：`ch19:342` `‘You aren’t stealing my magic, Cyn. Your power comes from within you.’`；`ch20:204` Aunt Rowan `You spoke of stealing Helena’s abilities, but that isn’t possible. Humans can’t steal our elemental power.`
6. 哈姆雷特是**狐狸**、雄性、**海伦娜的**魔宠（`:68` `Hamlet had curled up on the opposite bench. At Helena’s question, he lifted his own copper brows`）。

## 一 「漏」——素读有、md 无

| 编号 | 原文（`text/ch17:行`） | md 现状 | 档 |
|---|---|---|---|
| **L1** | `:212` `Perhaps they could bespell her to stop stealing Helena’s magic. A part of her ached at the thought. The rush was intoxicating. She would miss feeling the pulse of power. **But she would miss Helena more**, and she couldn’t imagine the woman remaining friends with Cynthia if she kept robbing her gifts.` | 全篇零提及。这是辛西娅**第一次把「失去海伦娜」排在「失去力量」之前**，也是 md:11「情绪从心动一路滑到恶心」这条弧线唯一的情感支点。 | **阻断** |
| L2 | `:125` `She wasn’t ignorant of her fortune, even if she was bound by golden chains. … They were just as trapped as Cynthia within society’s rules, and their cages were far less comfortable.` | **只出现在 md:139 一句话总结里**，导航 5 行与 8 个引语块的分析层全部没碰；而 md:64 反而写「作者没有站出来评论贫富」——**md 内部张力**（见 E7）。 | 提示（重） |
| L3 | `:137` `Or magic.` | 原句 6 分析（md:74）只说「用'奇迹'二字把解释推开」，**没写紧接着一行的自我更正**——而这一行才是本章的题眼（奇迹 → 魔法）。 | 提示 |
| L4 | `:146` `The coachman who had helped Helena from the carriage looked wide-eyed at the dog, then Helena, then Cynthia.` | **有目击者**。这正是海伦娜随即在 `:167` 用天气打岔的原因；md:10 只写「海伦娜用天气打岔遮掩」，没写当着谁。 | 提示 |
| L5 | `:149` `A strange calm flooded Cynthia, sweeping away her questions and filling her with confidence. She knew what needed to be done.` ＋ `:152` `Her voice resonated with command.` ＋ `:161` `As soon as the dog disappeared, so did her confidence.` | md:13 写了「狗一走，信心也跟着消失」，但**信心的来源**（一股陌生的镇定涌上来）与「声音里带着命令的分量」没写。 | 提示 |
| L6 | `:173` `‘I think it might be wise for Hamlet to stay in the carriage while we visit with Lily.’` ＋ `:176` `Act normal.`（海伦娜的眼神讯息） | 海伦娜的**两道遮掩指令**（把狐狸留在车上／装作正常）md 全篇未提。 | 提示 |
| L7 | `:191` `‘You’ll have to explain what just happened when we’re alone.’` | 是**辛西娅要求解释**，海伦娜才在 `:194` 回「今晚来布莱尔宅」。md:10 写成「海伦娜…要她当晚去布莱尔宅谈」，把主动方压成一边。 | 提示 |
| L8 | `:206` `Governess Smithers had taught her well with her biting birch stick.` | md 零提及（词表 `inadvertently` 用了这句作例句，分析层没碰）。**跨章陷阱**：本库另有 ch11 的管家 `Smith`，`Smithers` 是辛西娅的**家庭女教师**，两者不是同一人。 | 提示 |
| L9 | `:89`/`:92`/`:101`/`:107`/`:113`/`:116` 马车里的调情对答（`Your eyes are the most beautiful thing…` → `I shouldn’t have said that.` → `That you would be trouble.` → `You like trouble.` → `I find I like trouble far too much for my own good.`） | md:11 用「调笑」两字带过。`:92` 的自我刹车与 `:116` 海伦娜那句「我发现自己喜欢麻烦，对自己太没好处」是本章两人关系推进最实的两句，均未收。 | 提示 |
| L10 | `:227` `A large man with impressive hair that crept from his head down his cheeks and onto his chin rubbed his hand over his belly … ‘Who are ye?’` ＋ `:230` `Behind him, Cynthia heard a gasp.` | 开门的男人**无名无 tag**，md 未提；因此 md 读起来像「到了门口就看见莉莉」，实际是**先被一个陌生男人拦住、莉莉从里屋出来**。 | 提示 |
| L11 | `:236` `‘Oh my,’ Cynthia whispered.` ／ `:239` `‘Damnation,’ Helena cursed.` | 两人各自的反应；md 只写了辛西娅的恶心（`:254`），没写海伦娜**当场骂了一句**。 | 提示 |

> **L1 为什么是阻断**：md:11 把本章弧线定为「情绪从心动一路滑到恶心」，md:13 把辛西娅写成「机灵、逞强 → 追问自己做了什么 → 信心消失」。**这条线在原文里的转折点是 `:212`**——她愿意被施咒停止偷魔法，因为「她会想念力量的脉动，但她更想念海伦娜」。少了这一句，md 的「心动」没有落点，`:245`–`:254` 的「恶心」也就失去了对照物。属 S1「漏掉关键转折」。
> **修复位置**：块数 8 已**超** `block_target [3,6]` 上限 ⇒ **禁增第 9 块**，只能写进导航（见 `4-verdict.md` §四）。

## 二 「编」——md 有、原文无

**0 条独立凭空项。** 但有 1 条**与原文相反的内容断言**（归入 §三 E2，因原文两侧都有对应物）：md:24「信则被夹在同一张羊皮纸里」。

被排查后**不成立**的疑点（逐条留证）：

| md 位置 | 疑点 | 回原文结论 |
|---|---|---|
| md:10 | 「德文公爵夫人的吊唁信」 | **成立**。`:41` `My dear friend, the Duchess of Devon has no doubt written to extend her condolences.` |
| md:10 | 「商量以向莉莉道歉为名探访」 | **成立**。`:56` `I have wanted to apologise to Lily for Hubert’s abrupt and unwarranted dismissal. Perhaps that could be our reason for visiting?’` |
| md:10 | 「一条恶狗扑向哈姆雷特」 | **成立**。`:128` `a stray dog caught sight of Hamlet poking his copper nose out of the door`；`:131` `Hamlet had no escape as the much larger, much fiercer dog bunched his muscles to leap into the carriage.` |
| md:10 | 「辛西娅掌心射出一道能量」 | **成立**。`:134` `A snap of energy flew from her palm to the dog.` |
| md:10 | 「海伦娜用水把狗冲开」 | **成立**。`:143` `rushing water pooled around the animal’s feet, forcing him to lose his ground and be swept several feet away` |
| md:10 | 「辛西娅喝令它回家」 | **成立**。`:152` `‘Go home.’ Her voice resonated with command.` ＋ `:158` `‘Now.’ She pointed away from the carriage.` |
| md:10 | 「海伦娜用天气打岔遮掩」 | **成立**。`:167` `‘Such strange weather we’re having today.’ Helena spoke to the coachman as though nothing untoward had taken place.` |
| md:10 | 「莉莉掩不住身孕」 | **成立**。`:242` `Lily’s hastily altered dress couldn’t hide a painfully obvious swelling.` |
| md:10 | 「辛西娅明白休伯特当初开除她正是因为这个孩子」 | **成立**。`:245` `That is why Hubert fired her. Because she is with child.`（自由间接引语，POV＝辛西娅，未误挂叙述者） |
| md:12 | 「'需要女巫保护'的人反手用力量拦住恶狗」 | **成立**，且正是 ch15 `:95` `‘Unless I have a witch with me to keep me safe.’` 的反转。 |
| md:12 | 「结尾让'解雇女仆'接上'身孕'这条线」 | **成立**。`:56` dismissal → `:242`/`:245` with child。 |
| md:14 | 「全章贴辛西娅的限知，没有视角切换」 | **成立**。`:176` `Act normal.` 是眼神讯息（`:173`），不是 POV 切换。 |
| md:14 | 「也没有空行分场」 | **成立**。`:35`–`:254` 无场景分隔符（源文件的空行是提取件的段落分隔，不是分场）。 |
| md:14 | 「后半把句子切短，用连续问句和单句段落加快心跳」 | **成立**。`:164` 三连问；`:176` `Act normal.`／`:182` `Later.`／`:188` `Like a sensible person.`／`:200` `Hellfire.` 四处单句成段；`:197` 四连问。 |
| md:14 | 「章末停在一个生理反应上，不解释」 | **成立**。`:254` `Nausea washed through her.` 是全章最后一句。 |
| md:139 | 「海伦娜只回了一句'很多事'」 | **成立**。`:83` `‘Many things.’` |
| md:139 | 「自己虽被金链子拴住，别人的笼子却更不舒服」 | **成立**。`:125` `bound by golden chains` / `their cages were far less comfortable`。 |

## 三 「错」——两边都有但不一致

| 编号 | md 位置 | md 原文 | 原文依据 | 档 |
|---|---|---|---|---|
| **E1** | md:40（2 处） | 「再交给**拉克兰叔叔**，让苏格兰场去当面质问；或者现在就掉转马车…去找**拉克兰叔叔**」 | `ch11:44` `There’s a superintendent at Scotland Yard ’as nieces with the name of Blair. Lachlan MacDougal.`；`ch01:137` `Superintendent Lachlan MacDougal`；`ch06:273` `his infuriating (beautiful) niece`；`ch07:122` `took the necklace from his niece` ⇒ 他的侄女**姓 Blair**，关联走母系 ⇒ 「叔叔」（父之弟）错。 | **阻断**（跨章术语） |
| **E2** | md:24（原句 1 · 为什么这样写） | 「地址是这趟出门的目的，**信则被夹在同一张羊皮纸里**，两样东西一主一次，已经分出轻重。」 | `:35` `carrying a folded piece of parchment holding George Lippert’s address **and a letter**`（两样并列）；`:41` `Cynthia **pocketed the address** and **picked up the letter** to inspect the seal.` ⇒ 地址被揣进衣袋、信被单独拿起来验封蜡，**是两个独立物件**。**md 自己的词表 `pocketed` 行（md:119）用的正是 `:41` 这句**，与 md:24 自相矛盾。 | **阻断** |
| **E3** | md:94 / md:96（原句 8） | 「第二句没有点名…**读者会在这句之后自己补上那个名字**」／「读者读到这里…**却听不到那个名字被说出口**；这份**留白**让读者的判断和她的判断撞在一起。」 | `:251` `**Hubert**, you bastard.` ⇒ 名字在**三行之后**就由辛西娅自己在心里骂出来了，原文没有留白。**md:10 一句话概括自己也写了「又断定孩子的父亲就是休伯特」** ⇒ md 内部自相矛盾。 | **阻断** |
| E4 | md:13 | 「海伦娜**一路沉着**」 | `:167` `Her **painfully bright** smile made the man wince.`；`:83` `Helena’s grey eyes lightened a shade as she carefully watched her.`；`:173` `Her silver eyes slowly darkened back to grey.` ⇒ 她是在**用力装没事**，不是沉着。 | 提示 |
| E5 | md:12 | 「狐狸**灵兽**」 | 全书译名实测：**魔宠 53 ／ 使魔 13 ／ 灵兽 2**（`灵兽` 只出现在 ch06 与 ch17）。同一实体三个中文名字。 | 提示 |
| E6 | md:34 / md:36 | 「让读者明白这不是无意碰触，而是**两个人都在试探**」／「也看得出**海伦娜没有躲**」 | `:50` 引语内只有辛西娅一侧的反应（`A secret thrill ran through her.`）；海伦娜的主动要到 `:59` 才出现（`She lifted her pinkie up and down over the silk.`）。**引语内不足以支撑「两个人」与「没有躲」** ⇒ S3 分析层伸手到引语之外。 | 提示 |
| E7 | md:64 | 「**作者没有站出来评论贫富**，只让辛西娅的鼻子和眼睛先受不了」 | `:125` 紧接着一整段就是贫富评论（`bound by golden chains` / `their cages were far less comfortable`）；且 **md:139 一句话总结自己写了这一段** ⇒ md 内部张力。严格说「作者／叙述者」确实没评论（是辛西娅的自由间接思想），但「只让鼻子和眼睛先受不了」把 `:125` 整个抹掉了。 | 提示 |
| E8 | md:10 | 「辛西娅猜是德文公爵夫人的吊唁信，**随手搁下**」 | `:41` `Can you put this in my room? I shall read it later.` ⇒ 是**叫管家收走**，不是自己随手搁下；`:44` `Mrs Higgins retrieved the letter`。 | 提示 |
| E9 | md:74 | 「却又用'奇迹'二字把解释推开」 | 方向对，但漏了 `:137` `Or magic.` 这个**紧接的自我更正**（见 L3）；「推开」的说法因此不准——原文是推开了「奇迹」、马上换上「魔法」，再立刻否认（`:140` `But that is impossible.`）。 | 提示 |
| E10 | md:106 / md:120 | 词表 `unwarranted`、`dismissal` 两条例句开头残留原文开引号 `‘`（`‘I have wanted to apologise to Lily for Hubert’s abrupt and unwarranted dismissal.`），其余 20 条无 | `:56` 原句确有 `‘`，属**格式瑕疵**（`check_vocab.py` 不查） | 提示 |
| E11 | md:110 / md:111 | `Superintendent`、`attractions` 放在 ⭐⭐⭐ 高级 ⇒ **档位注水**（S4 ③）；两词在本书出现频率与难度都属进阶 | `:77` `While she respected Superintendent MacDougal…`；`:95` `But it was impossible not to appreciate Helena’s many attractions.` | 提示 |

### E1 专节 · Lachlan 的中文称谓（跨章阻断）

**可确定的**：不是父系。`ch11:44` `nieces with the name of Blair`、`ch06:273` `his infuriating (beautiful) niece`、`ch07:122` `took the necklace from his niece` ⇒ 他的侄女／外甥女**姓 Blair**，而 Blair 是**母系**女巫世家姓（`ch06:35` `passed down to the Blair women through generations … circle of sisterhood`）。**「叔叔」＝父之弟，无立足点。**

**不可确定的**：舅舅（母之兄弟，血缘）vs 姨父（母之姐妹之夫，姻亲）。Lachlan 姓 **MacDougal** 不姓 Blair；零命中取证：
```
① /usr/bin/grep -nEi 'Rowan.{0,80}(husband|wife|married|spouse)|(husband|wife|married|spouse).{0,80}Rowan' text/*.txt
   → 0 行，rc=1（Rowan 全书无配偶表述）
② /usr/bin/grep -nEi '(Lachlan|MacDougal).{0,80}(husband|wife|married|brother|sister)|…' text/*.txt
   → 15 行，rc=0；逐行读毕：brother 全部指 Thomas（辛西娅之兄）、husband 全部指 Hubert（辛西娅之亡夫），
     没有一条写 Lachlan 自己的兄弟或配偶。
```
⇒ **舅／姨父不裁决。**

**全书分布实测**：`拉克兰叔叔` **12**（ch02×2／ch04×2／ch06×3／ch09×2／ch14×1／ch17×2）｜`拉克兰舅舅` **9**（ch23×3／ch24×2／ch25×1／ch26×3）。
**建议**：全书统一为 **`拉克兰舅舅`**——理由三条：① 唯一有原文支撑的方向是母系，「叔叔」必错；② 后段 4 章（ch23–ch26，含结局）已在用「舅舅」；③ 舅／姨父既然不裁决，取一个**母系且不新增第三套译名**的既有词，改动量最小（12 处）。**依据须写进 `.memory/review-ledger.md`。**

**另记一条原文自身的不一致（不裁决，不判 md 缺陷）**：Lachlan 是谁的 uncle，原文两处口径不同——
`ch03:315` `Thomas stood directly in front of **her uncle**.`（`her`＝Cynthia）vs `ch16:209` `already **my brother, your uncle**, and now you…`（辛西娅对海伦娜说 ⇒ 海伦娜的 uncle）。若是同一位长辈，辛西娅该说 `our uncle`。

### 时序专查（无缺陷）

| md 断言 | 原文顺序 | 结论 |
|---|---|---|
| md:10「地址＋信 → 乘马车 → 商量道歉为名 → 恶狗扑哈姆雷特 → 辛西娅拦狗 → 海伦娜冲水 → 喝令回家 → 怀疑偷力量 → 海伦娜遮掩 → 约当晚 → 门口见身孕」 | `:35`/`:41` → `:47`/`:56` → `:128`/`:131` → `:134` → `:143` → `:152`/`:158` → `:140`/`:197` → `:167` → `:194` → `:221`–`:254` | **成立**。唯一需注意：「怀疑偷力量」**第一次出现在 `:140`**（`Unless I’m somehow stealing power from Helena.`），第二次在 `:197`；md:10 把它排在「喝令回家」之后，与 `:197` 一致，不算错（`:140` 的那次紧随拦狗）。 |
| md:11「马车里先是靠近、调笑和轻敌，狗一扑…轻松立刻变成惊恐」 | `:50`–`:116` 调情 → `:122` 街景 → `:131` 狗 → `:134` 出手 → `:164` `What the bloody hell just happened?` | **成立** |
| md:14「前半用对话和细小动作推进，后半把句子切短」 | 前半 `:35`–`:125` 以对话为主；后半 `:131`–`:254` 单句成段 4 处、连问 2 组 | **成立**（实测） |

## 四 R4 逐块对应（人判，含固定三问）

| 块 | md 行 | 引语落点 | 中文是在讲这句引语吗 | ①动词主语 ②受事 ③归属方向 | 关键词在引语内 |
|---|---|---|---|---|---|
| 原句 1 | md:18 | `:35` | ✅ | `summoned` 主语＝Cynthia ✅；`knocked` 主语＝Mrs Higgins ✅；`carrying…` 的逻辑主语＝Higgins → md「希金斯太太先敲了门，手里拿着…」✅ | summoned ✅ / parchment ✅ / folded ✅ |
| 原句 2 | md:28 | `:50` | ✅（分析层越界见 E6） | `could have sat / pressed` 主语＝Cynthia ✅；`Helena’s pinkie brushed against **her** black silk skirt` 的 her＝**Cynthia** → md「海伦娜的小指擦过她的黑绸裙」✅ **未调转**；`A secret thrill ran through her` 的 her＝Cynthia ✅ | squabs ✅ / pinkie ✅ / thrill ✅ |
| 原句 3 | md:38 | `:74` | ✅ | 说话人＝**Helena**（`:77` 前一段是 Cynthia 的思考，`:74` 起 `Helena shook her head.`）→ md「海伦娜摇头，说…」✅；`take that to Uncle Lachlan` 的施动者＝她们两人 ✅ | aware ✅ / evidence ✅ / Scotland Yard ✅ / confront ✅ |
| 原句 4 | md:48 | `:80` | ✅ | 说话人＝**Cynthia**（`:83` 才轮到 Helena `‘Many things.’`）→ md「辛西娅说…」✅ **未把话安到海伦娜头上**；`And I have a witch to protect me` 的 witch＝Helena、me＝Cynthia → md「身边还有一位女巫护着」✅ | utmost ✅ / frightening ✅ / tempt fate ✅ |
| 原句 5 | md:58 | `:122` | ✅ | `spilled` 主语＝children ✅；`The heat was amplified by the brick buildings` → md「砖楼把太阳吸进去，又反射到…把热气放大」✅ **`by` 的施动者方向正确**；`distracted Cynthia` 的施动者＝街景 ✅ | spilled ✅ / amplified ✅ / putrid ✅ / crammed ✅ |
| 原句 6 | md:68 | `:134` | ✅ | `screamed / throwing her hand out` 主语＝Cynthia ✅；`A snap of energy flew from **her palm** to the dog` 的 her＝Cynthia → md「一道能量从她掌心飞出」✅ **未误挂到海伦娜**；`he jerked back` 的 he＝狗（阳性）✅；`An invisible leash **she** controlled` 的 she＝Cynthia → md「由她控制的隐形牵绳」✅ | tether ✅ / strained ✅ / invisible leash ✅ |
| 原句 7 | md:78 | `:197` | ✅ | `Nerves threatened to choke **her**`＝Cynthia ✅；`Helena looked very serious` → md「海伦娜神色很严肃」✅；`What if **Cynthia’s** suspicions were correct and **she** was stealing **Helena’s** powers` → md「她真在以某种方式偷走海伦娜的力量」✅ **偷的方向（辛西娅←海伦娜）正确，未调转** | suspicions ✅ / stealing ✅ / jolt ✅ |
| 原句 8 | md:88 | `:248` | ✅（**但分析层的「留白」断言被 `:251` 证伪，见 E3**） | `Suspicion slithered in **Cynthia’s** mind` → md「在她脑子里滑行」✅；`**she** knew exactly who sired the babe` 的 she＝Cynthia → md「她太清楚这个孩子的父亲是谁了」✅；`sired` 的施动者＝孩子的父亲（`:251` 点名 Hubert）✅ | slithered ✅ / poisonous ✅ / sired ✅ |

**对应 8/8。** 施事／归属调转 **0 处**——本章最高危的三处（`her palm` 是谁的掌心／`invisible leash she controlled` 的 she／`stealing Helena’s powers` 的方向）**全部未调转**。

## 五 形态

| 项 | 实测 | 本书众数／profile | 结论 |
|---|---|---|---|
| H1 | `# 17. Chapter Seventeen` | `# NN. Chapter NN(英文序数)` | ✅ |
| 导航子项 | 5 | 5 | ✅ |
| 引语块数 | **8** | `block_target [3,6]`（1894 词，短章）；本书众数 9–13（ch15=10／ch16=9／ch18=13） | ⚠️ **提示**——`block_hint` 已报偏离，但 `chapter.sh` rc=0（提示型）。**判提示不判阻断**，理由：短章按词数折算的建议区间偏严，8 块与本书众数同量级。**但⇒ L1 的补漏禁增第 9 块。** |
| 子项集 | 中文理解／关键词／为什么这样写／读者视角提示 ×8 | 同 | ✅ |
| 词表 | 标准 Markdown 表格 `\| 词/短语 \| 释义 \| 例句 \|`，22 条＝8/8/6 | 新判据（`96b7e557e`） | ✅ |
| 一句话总结 | 有（md:139） | 有 | ✅ |
| frontmatter | `状态: 未读` / `modified: "2026-10-22"` | 同 | ✅ |
| `…` 拼接 | 8 块全部为**单段连续引语**，无 `…` | — | ✅（`segment_miss 0`） |

**形态 7/8**（块数 1 项为提示型偏离，已给理由）。

## 六 语料层与引语逐字（实跑）

```
$ bash scripts/chapter.sh "…/ch17 the dog in cheapside.md" --json > review/ch17/2-machine.json ; echo $?
0
counts.blocks 8 · counts.words 1894 · block_target [3,6] · block_hint「块数 8 偏离本章篇幅建议 3–6」· segments 8 · segment_miss 0
form.h1 "17. Chapter Seventeen" · nav_count 5 · issues 9 类全空

$ python3 /tmp/vocab_check_hx.py 17      # 例句是否本章原句
rows=22 missing=0

$ python3 /tmp/vocab_head_hx.py 17       # 词头是否在本章原文
rc=0（无输出）

$ python3 scripts/verify_fragments_indep.py "…/the-hexing-miss-helena-by-darcy-mcguire"
引语条数 270 ｜ 受检片段 312 ｜ ❌ MISS 0 ｜ ❌ 拼接未标省略号 0 ｜ 缺参照章 0
```

**词表 22 条例句逐条抽核（行号）**：`condolences:41`／`uncommonly:47`／`unwarranted:56`／`cobblestones:122`／`inadvertently:206`／`suspicions:197`／`Superintendent:77`／`attractions:95`／`summoned:35`／`parchment:35`／`pocketed:41`／`dismissal:56`／`friction:59`／`scrunched:77`／`damnably:62`／`sensation:59`／`carriage:35`／`letter:35`／`chin:227`／`babe:248`／`bloody hell:164`／`head:77`。

**语料层「像广告的正文」扫描**：ch17 **零推广行**（Lokepub 推广只在 ch03:188／ch08:170,173／ch13:182,185／ch19:194,197／ch25:214）。本章亦无 `I’m in love with a ferret.`（`ch15:192`）。

**「偷力量」跨章核实（供 R5.5 用）**：
```
$ /usr/bin/grep -nEi 'steal|stole|robbing|siphon|drain' text/ch18…text/ch27 > /tmp/hx_c.txt ; rc=2（ch24 文件名不是 ch24_chapter_24.txt，见下）
命中关键两条：
  text/ch19_chapter_19.txt:342  ‘You aren’t stealing my magic, Cyn. Your power comes from within you.’
  text/ch20_chapter_20.txt:204  ‘Magic doesn’t make mistakes.’ Aunt Rowan grounded her. ‘You spoke of stealing Helena’s abilities,
                                but that isn’t possible. Humans can’t steal our elemental power.’
```
⇒ **md:86 的 hedge「书里没有谁证实她真的在偷力量」不仅正确，而且被后文两处正面否定所支持。**
（rc=2 的原因：上面记录时把命令写成了省略号简写 `text/ch18…text/ch27`，grep 对不存在的字面文件名报错；实际逐章实跑的是 `text/ch18_chapter_18.txt`…`text/ch27_chapter_27.txt` 全部存在的真名——`ls text/ | grep ch24` 只有 `ch24_chapter_24.txt` 一件，本书 `text/` **没有**按情节命名的提取件。）

## 七 不裁决（U）

| 编号 | 事项 | 为什么不裁决 |
|---|---|---|
| U1 | `:227` 开门的高大男人是谁 | **无姓名 tag**。按地点（利珀特家）与 `:233` 莉莉从「门后那间黑屋子」出来推断，很可能是乔治·利珀特本人，但原文未点名 ⇒ md 未写他是谁，**不算缺陷**；若后续修复要补写，只能写「一个无名的男人」。 |
| U2 | 德文公爵夫人的信里究竟写了什么 | `:41` 辛西娅只是**猜**（`has no doubt written`），当场没拆（`I shall read it later`）⇒ 不得写实。 |
| U3 | 辛西娅是否真的在偷海伦娜的力量 | 本章不裁决；后文 `ch19:342`／`ch20:204` 明确否定 ⇒ md:86 的 hedge 正确。 |
| U4 | Lachlan 是舅舅还是姨父 | 见 §三 E1 专节，原文未写血缘或姻亲。 |
| U5 | Lachlan 是辛西娅的 uncle 还是海伦娜的 uncle | `ch03:315` 与 `ch16:209` 两处口径不同，原文自身不一致。 |
| U6 | `:245` `That is why Hubert fired her.` 是否确为事实 | 这是辛西娅的**推断**（自由间接思想），不是叙述者断言；后文 ch18 才有莉莉一侧的说法 ⇒ 本章不裁决。md:10 写「辛西娅明白…」已正确标为她的认知。 |
| U7 | `:248` `who sired the babe` 的答案 | 原文 `:251` `Hubert, you bastard.` 已给出（辛西娅的判断）；**是否属实**本章不裁决。 |
| U8 | `:170` `‘Yes, Miss Blair. Awful odd weather the last few days.’` 马车夫是否真看出了什么 | `:146` 他 `looked wide-eyed`，但 `:167`–`:170` 他顺着海伦娜的话头接了下去 ⇒ 不裁决。 |
