# ch12 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，372 行全读，109 事件 / 10 关系 / 10 数字 / 5 未决 / 15 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=12 / words=4006 / block_target=[7,13] / segments=17）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`、`hole=0`、`empty_quote=0`。
> 补验（机器盲区）：本章 12 条引语中 **3 条含 `…`**（原句 2、7，另原句 7 为多段省略）⇒ R0 全书级 `verify_fragments_indep.py`（312 片段 / 0 MISS）已逐段独立取证通过；本章 22 行词表例句 **22/22 逐字回源命中**（`/tmp/vocab_check_hx.py` → `ch12: rows=22 missing=0`）、**22/22 词头落在例句内**（`/tmp/vocab_head_hx.py`，无输出＝零失配）；**引号配对**探针 `/tmp/pair4_hx.py` 全书扫描 ⇒ **本章 0 处偏离**（全书唯一 1 处在 ch09 原句 7）。
> 素读底稿自检：109 条逐字引文全部为 `text/ch12_chapter_12.txt` 的精确子串（自建 `/tmp/val_suread_hx12.py`，初检抓出 1 条转写错误 `:255` `can’t you?`→`can you?`，已改）。

---

## 〇、本章结构要点（R1 先行结论，供 R4/R5 引用）

**POV 在 `:129` 切换**：`:35`–`:113` 为辛西娅第三人称限知；`:129` 起（`Helena was unaccountably nervous as Sinclair led them further down the corridor and into another room.`）改为海伦娜第三人称限知，直至章末 `:372`。切换点在辛克莱带两人离开办公室、进入摄影棚的转场处，其间 `:115`–`:128` 为整段空行。

**本章三段式**：① 办公室谈条件（辛西娅 POV，`:35`–`:113`）→ ② 摄影棚私下谈话（海伦娜 POV，`:129`–`:270`）→ ③ 摆拍与毁证（海伦娜 POV，`:276`–`:372`）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号 + 逐字） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:132` `Dear God. This is what Ellie saw in her vision.` ＋ `:135` `Ellie said Cynthia was desperate to leave the room but couldn’t.` —— 海伦娜意识到摄影棚的布景（`swathed in crimson and black lace`，`:129`）正是**艾莉幻象**里那个房间；艾莉还预言过「辛西娅极想离开这个房间却走不了」 | md **全章无「艾莉」「幻象」二字**（`/usr/bin/grep -n "艾莉\|幻象" ch12 …` → 0 命中）⇒ ch09 `:53` 埋下的钩子在 ch12 完全断线 | **不构成阻断**（md 未就此作出任何相反断言）；**建议**在导航或原句 5 之后补一句——这是 ch09→ch12 的跨章兑现点 |
| L2 | `:339` `‘I never understood until now. I’ve seen the way Clio and my brother are together…` ＋ `:342` `He swept the curtain aside and strode back to them, **halting Cynthia from revealing what remained infuriatingly hidden from Helena**.` —— 辛西娅说直到此刻才明白，提到「克里奥和我哥哥」；辛克莱**打断**了她没说完的话 | md **未提克里奥、也未提这次打断** | **不构成阻断**（md 未作相反断言）；属被截断的悬念钩子 |
| L3 | `:246` 中段（被原句 7 用 `…` 省略的部分）：`I won’t have you apologising for putting me in a situation that, were Sinclair not present, would pose no hardship for me. It is I who should apologise to you. Try as I might, I fear I won’t escape this evening without experiencing some element of pleasure in our intimacy that I know you won’t share. It’s unforgiveable, but I can’t see a way around it.` —— 海伦娜**承认并预告自己在亲密中会有欢愉**、称之「不可原谅」，并说「该道歉的是我」 | 原句 7 的引语以 `…` **公开标注**省略，md 的中文理解／为什么这样写／读者视角提示**只覆盖被引的三段**；但导航·人物弧线写了「先告白、**先道歉**的人」（依据即 `It is I who should apologise to you.`，在省略段内） | **不构成引语截短阻断**（省略由 `…` 标注、块内分析未越界）；**建议**补一句，因为这是原句 8（`:270`「我唯一害怕的欲望是我自己的」）的**直接前件**，缺了它，原句 8 的「对方回答」少了被回答的对象 |
| L4 | `:83` `Cynthia lurched forward and would have slapped him had Helena not grabbed her arm and pulled her back.` ＋ `:86` `‘We’ll do it.’` ＋ `:89` `Helena squeezed her arm gently.` ＋ `:95` `Trust me.` ＋ `:98` `Which made them allies instead of adversaries.` | md 未收「辛西娅要扇他」「海伦娜抢先代答」「相信我」「临时同盟」这四个具体动作 | **不构成阻断**（导航·一句话概括与人物弧线已覆盖「海伦娜点破」「同盟」「互相坦白」的主线） |
| L5 | `:156` `‘I need to speak with Lady Burrows before we begin. Privately.’` ＋ `:180` `‘Five minutes. No more. And when I return, I want ’er hair unbound.’` ＋ `:183` `‘Just look at my dress… I look like a trollop.’` `‘You’ll be ruined because of me. I can’t allow this. I won’t.’` | md 未收「五分钟」「头发散开」「我像个婊子」「你会因为我被毁掉」 | **不构成阻断**（原句 6 已引用 `:186` 的「辛克莱正在门外听着」，其前提未铺陈但不与原文矛盾） |
| L6 | `:264` 巫水毁底片的方案 ＋ `:273` 拆发、闻香草与**忍冬** ＋ `:315` 吮脖子 ＋ `:333` 辛西娅为失控道歉 ＋ `:363`–`:369` `But he is still a threat. Devils are not so easily destroyed.` | md 未收这些动作与细节 | **不构成阻断**（导航·一句话概括、原句 8/9/10/12 覆盖主线）；其中 `:273` 的 **honeysuckle＝忍冬** 正是跨章术语项（ch26/ch27 有「金银花」写法），**记入汇总文件** |
| L7 | `:107` `‘I want Hubert’s letters of debt before I agree. All of them.’` —— 辛西娅索要休伯特的**全部债据**；**本章始终没有写辛克莱是否交出**（`:110` 只回应「不只我一个聪明人」） | md 只在导航里写「辛西娅以休伯特的全部债据为条件答应」，**未点明债据是否到手亦未写** | **不构成阻断**（md 未断言已到手）；**建议**在导航补一句——与 ch11「债务数额原文从未写出」并列，本章**债据交付**同样悬空，两处应一起记入总览层 |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–12 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的六处疑点：

- **「辛西娅先以为要拍裸照」**——`:35` 她开口即拒 `I will not take nude photographs for you`，`:38` 辛克莱当场纠正 `I wouldn’t require you to be in any state of undress. You may stay exactly as you are… with a few minor changes.` ⇒ 确是原文连续两句构成的反应—纠正结构，**不是编造**。
- **「救场的人不是外来的英雄，而是被拍的两个人自己动手」**——`:107` 辛西娅谈条件、`:354`/`:357` 海伦娜毁证；本章**无任何第三方介入或解围** ⇒ 成立。
- **「『假戏真做』只走到互相坦白，没有跨进确定关系那一步」**——`:222`–`:270` 双方各自表白，`:372` 章止于上马车；全章**没有**确认关系或约定 ⇒ 成立。
- **「照片是绳子，人情是账」「把情欲压进玻璃版和药液里」**——md 自己的比喻句，不是对原文的事实断言 ⇒ 不构成编造。
- **未把原文瑕疵当成内容**——`:38` `My suggestions is ’ardly as depraved as all that.`（复数名词配单数动词）、`:345` `I’m so close! Soon. Soon, it will be done All of this will be worth it.`（`done` 与 `All` 之间无句读）——md 既未「修正」也未据此编造情节 ⇒ 成立。
- **未把 `:339` 的 `But now⁠—` 破折号（带 U+2060）当作正文省略**——md 未引用该处，不存在截断问题。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 原句 3·为什么这样写 | 「**两句之间没有转折词**，兴奋和恐惧贴在一起」 | `:62` `A completely inappropriate thrill coursed through Cynthia at the very thought of taking intimate pictures with Helena. **But** the pulse of excitement immediately died when she realised who would be standing behind the camera. He truly was the Devil.` —— 两句之间明写转折连词 **`But`** | ①md 自己的引语里就有 `But`，子句与引语**直接矛盾**；②原文的效果恰恰**依赖**这个显性转折标记造成锐利对撞，md 把它说成「没有转折词、贴在一起」，把文本机制说反了 ⇒ **对原文措辞的否定断言**（原文有 ⇒ md 说无） | **阻断**（判定口径：可被 md 自身引语当场证伪的、关涉原文措辞的否定断言；与 ch09 E2「章末落到一个单词」同类） |
| E2 | 原句 4·中文理解 | 「**他对辛西娅说**，照片会不会见光由她决定，只要她往后不时替他办几件事，比如管住海伦娜那位叔叔」 | `:68` `‘That’s up to you. I can ensure these pictures never see the light of day. As long as you grant me a few favours from time to time. Like putting a leash on that dog **you call an uncle**, **Miss Blair**. I grow weary of ’im sniffing around my territory.’` —— 受话人是**海伦娜**（`Miss Blair` ＋ `you call an uncle`）；**辛西娅全书没有叔叔这条线** | md 把受话人挂到辛西娅身上：①与原文的 `Miss Blair` 直接冲突；②与 md 同一句后半的「管住**海伦娜**那位叔叔」自相矛盾；③与 md 自己的原句 12·中文理解（`:360`「他让**布莱尔小姐**给叔叔带话…随后他转向**伯罗斯夫人**…」）的处理不一致 ⇒ **受话人归属方向错** | **阻断**（归属方向类，与「施事归属错」同级） |
| E3 | 原句 1·读者视角提示 | 「读者会**先**听见一句硬话，**再**看见她胃里的翻涌」 | `:35` `**Nausea rolled in Cynthia’s belly, followed quickly by indignant rage.** ‘I will not take nude photographs for you…’` —— 叙述顺序是**先身体、后台词** | md 把「叙述顺序」与「读者第一眼抓住哪句」混为一谈；原文的 `followed quickly by` 明示顺序 ⇒ 读者视角层的**顺序标签错** | **提示**（读者视角层；改法：调换先后，或改为「读者会先看见她胃里的翻涌，再听见那句硬话」） |
| E4 | 导航·一句话概括 | 「辛克莱临走却留下**对她叔叔的威胁**和**一笔日后要讨的人情**」 | `:360` `‘Take a message to your uncle, Miss Blair. If ’e doesn’t cease ’is investigations into my affairs, I will destroy that which ’e holds most dear. **As for you, Lady Burrows… I’ll come calling for a favour one day. And I’ll expect you to grant it.** Now, begone.’` —— 威胁的对象是**海伦娜的叔叔**；「日后要讨的人情」是**向辛西娅**索取的 | 并列句式让「人情」也挂到叔叔头上；原句 12·中文理解 判得**正确** ⇒ 属摘要层的归属**省略**（不是错认） | **提示**（措辞级） |
| E5 | 原句 7·中文理解 | 「又保证无论**那个人**提出什么要求，她都会守住界限」 | `:246` `Just know, I will do whatever I can to respect your boundaries, **no matter what he asks of us**.` —— `he` ＝辛克莱 | md 用「那个人」回避了本书通行的 `他/她` 性别标记，读者无法从这一句判断要求来自谁；同章原句 12 一致用「他」指辛克莱 ⇒ 术语层不一致 | **提示**（措辞级） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 胃里翻涌→怒气→当面拒裸照→不许朋友自贬 | 辛西娅（叙述＋台词） | 辛克莱的要求；她的「朋友」 | 「我的朋友」指**海伦娜** | 对应成立（另见 E3：读者视角的顺序标签） |
| 2 | 他瞬间从桌边到门口挡路；叫她镇定；不须脱衣、稍作改动 | 辛克莱 | 辛西娅的去路；辛西娅的衣服 | 「他叫她镇定」＝对辛西娅说 | 对应成立 |
| 3 | 想到拍亲密照片先涌起不合时宜的兴奋；想到镜头后的人就熄了；断定他是魔鬼 | 辛西娅（叙述层） | 「拍亲密照片」这件事；「镜头后面站着的人」 | 「魔鬼」＝她**心里**的判断 | 中文理解对应成立（**为什么这样写**含 E1 的错误断言） |
| 4 | 耸肩；西装不皱；照片见光与否；不时替他办事；管住海伦娜的叔叔 | 辛克莱 | 照片；「几件小事」；海伦娜的叔叔 | **受话人是海伦娜（`Miss Blair`），md 挂给辛西娅** | **不成立（③归属方向）→ E2** |
| 5 | 认得出欲望；记得辛西娅榛色眼里的饥渴；危险的一时冲动不等于她喜欢女人；不愿把欲望强加给自主权被剥夺者 | 海伦娜（自述） | 「自己的欲望」；「一个自主权已被剥夺的女人」 | 克制落在**海伦娜自己**这边 | 对应成立 |
| 6 | 锋利明亮的东西刺穿心口的盾；拉近、压成耳语；因为辛克莱在门外听着；她能毁掉胶片 | 海伦娜 | 辛西娅；「这句话」 | 「门外听着」＝辛克莱 | 对应成立 |
| 7 | 不以欣赏女人为耻；许多人视为扭曲；承认藏不住欲望；保证守界限；只求别怕她 | 海伦娜 | 「喜欢女人这件事」；「对眼前这个人的欲望」；「你的界限」 | 约束的承受方＝辛西娅（`your boundaries`／`you fear me`） | 对应成立（省略段另见 L3） |
| 8 | 对方回答；不怕女人喜欢女人；怕的是自己的欲望；从没这样想要过一个人；退开一步，海伦娜因失去体温而发疼 | 辛西娅（台词）＋叙述（`Helena ached…`） | 「自己的欲望」；「她的温暖」 | 「对方回答」＝**辛西娅答海伦娜**；「海伦娜因失去她的体温而发疼」＝受事是**辛西娅的体温** | 对应成立 |
| 9 | 走到相机旁；桌上的玻璃版与浅盘；取出、浸硝酸银、滑进相机；让海伦娜坐躺椅、辛西娅坐她腿上 | 辛克莱 | 玻璃版；硝酸银；相机；两人的姿势 | 「他让辛西娅坐在**她**（海伦娜）腿上」 | 对应成立 |
| 10 | 拉着手往门口走；回头看木盒；聚力把空气压成水滴、灌满；水从外壁淌下；藏起满意的笑 | 海伦娜 | 盒内的空气；木盒 | 「满意的笑」藏起来＝不给辛克莱看见 | 对应成立 |
| 11 | 目光一转；想到暗房里晾着的照片；浸湿；影像糊成黑灰污痕 | 海伦娜 | 晾着的照片 | 「她」（辛西娅）不在受事位 | 对应成立 |
| 12 | 让布莱尔小姐给叔叔带话；叔叔不停手就毁掉最珍视之物；转向伯罗斯夫人要一个人情；赶她们走 | 辛克莱 | 布莱尔小姐的叔叔；伯罗斯夫人 | **威胁→海伦娜的叔叔；人情→辛西娅**（判得正确） | 对应成立 |

**R4 结果：12 块中 11 块对应成立，原句 4 因③归属方向不成立 ⇒ 1 块越界。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 12. Chapter Twelve`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 **12**，落在本书区间 [6,13] 与本章 `block_target=[7,13]` 内（**尚余 1 块额度**：若因修复而增块，须 ≤13，超过即触发 `block_count`）；词表 22 行（8/8/6 三档）。

### 引号配对（机器层零覆盖，自建探针）

`/tmp/pair4_hx.py` 全书扫描 27 章 ⇒ 全书 **TOTAL 1**（唯一一条在 ch09 原句 7）；**ch12 十二个引语块全部配对完整**（含原句 7 这种 `…` 多段省略、首尾引号仍成对的形态；含原句 12 以 `’` 收尾且块内有对应 `‘`）⇒ **本章引号配对 0 偏离**。

## 六、语料层观察（非 md 缺陷，不计入三张单子）

本章**无**站点宣传行注入（全书 5 章 6 行：ch03:188 / ch08:170+173 / ch13:185 / ch19:197 / ch25:214，见 ch08 的 §六）。本章 12 条引语中 3 条含 `…`（原句 2、7），省略号两侧均为原文，R0 全书级 `verify_fragments_indep.py` 已逐段独立取证（312 片段 / 0 MISS）。本章含 2 处**原文自身的排版瑕疵**：`:38` `My suggestions is`（复数误用）、`:345` `it will be done All of this`（缺句读）——均照录，未被 md 引用，不影响引语层。

### 跨章术语不一致（进汇总修复指令文件，**本章不改**）

| 词 | 本章写法 | 其他章节写法 | 处置 |
|---|---|---|---|
| honeysuckle | 本章未出现在正文（`:273` 仅在原文，未被引语或词表引用） | `:273` 原文 `inhaled vanilla and honeysuckle`；ch26/ch27 的 md 有「忍冬」与「金银花」两种写法 | 列入汇总（若后续引到 `:273`，须与全书多数派统一） |
| apothecary | `:74` 原文 `The apothecary shop was patronised by the beau monde’s most elite ladies.` —— 本章 md 未引用该句，故无写法冲突 | ch11 作「药妆店」；ch06 词表作「药草店；药剂师」；`:74` 此句证明该店**由上流社会最上层夫人光顾**，与 ch11「药妆店」的性质描述相合 | 列入汇总，二选一后全书统一 |
| Lady Burrows / Miss Blair | 本章两称交替（`:156` 海伦娜称 `Lady Burrows`、`:159` 辛克莱称 `Miss Blair`） | 全书一致 | 无需处理 |
