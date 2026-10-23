# 4-verdict.md · 《The Hexing Miss Helena》ch12 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：双 POV 中途切换章＋要挟交易章＋坦白章｜档位：**深审**（2026-10-23 用户指令「继续执行深审 R0–R5 全章」）
底稿：`1-suread.json`（R1 先素读，372 行全读，109 事件 / 10 关系 / 10 数字 / 5 未决 / 15 陷阱）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch12_chapter_12.txt`（372 行）｜受审：`ch12 the scandalous photographs.md`（12 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 12 / 12 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`、`empty_quote=0`；共 **17 个片段**，R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章 3 条引语含 `…`——原句 2、原句 7，逐段独立取证通过）；词表 **22 / 22** 例句逐字回源命中（`/tmp/vocab_check_hx.py` → `ch12: rows=22 missing=0`；`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建补验）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`，无输出＝零失配） |
| **对应** | **12 块：11 块对应成立，1 块越界（原句 4）** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配；**原句 4 因③归属方向不成立 ⇒ 见 E2** |
| **形态** | **5 / 5 符合，0 偏离** | H1 `# 12. Chapter Twelve` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **12** ∈ 本书区间 **6–13** ✓，亦 ∈ 本章 `block_target:[7,13]` ✓（**尚余 1 块额度**：因修复增块须 ≤13）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0`；**引号配对 0 偏离**（`/tmp/pair4_hx.py` 全书扫描 ⇒ 全书 TOTAL 1，唯一一处落在 ch09 原句 7） |
| **断言** | **共核 36 条：相符 31 ／ 提示 3 ／ 阻断 2 ／ 跳过 0** | 提示 3 条（E3 顺序标签、E4 摘要层归属省略、E5 术语层「那个人」）；**阻断型条数 = 2**（E1、E2） |

**本章有 2 条阻断型缺陷**：一条是**对原文措辞的否定断言被自身引语当场证伪**（E1），一条是**受话人归属方向错**（E2）。两条都可在引语层零改动的前提下修复。

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch12_chapter_12.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 原句 3·为什么这样写：「**两句之间没有转折词**，兴奋和恐惧贴在一起」 | `:62` `A completely inappropriate thrill coursed through Cynthia at the very thought of taking intimate pictures with Helena. **But** the pulse of excitement immediately died when she realised who would be standing behind the camera. He truly was the Devil.` —— 两句之间明写转折连词 **`But`** | ①md **自己引用的那段原文里就有 `But`**，子句与引语直接矛盾；②原文的效果恰恰**依赖**这个显性转折标记造成的锐利对撞，md 把它写成「没有转折词、贴在一起」，把文本机制说反。判定口径：*可被 md 自身引语当场证伪的、关涉原文措辞的否定断言*（与 ch09 E2「章末落到一个单词」同类）<br>**改法**：`两句之间没有转折词，兴奋和恐惧贴在一起` → `一个“ But ”把兴奋和恐惧硬生生截成两截` | **阻断** |
| E2 | 原句 4·中文理解：「**他对辛西娅说**，照片会不会见光由她决定，只要她往后不时替他办几件事，比如管住海伦娜那位叔叔」 | `:68` `‘That’s up to you. I can ensure these pictures never see the light of day. As long as you grant me a few favours from time to time. Like putting a leash on that dog **you call an uncle**, **Miss Blair**. I grow weary of ’im sniffing around my territory.’` —— 受话人是**海伦娜**（`Miss Blair` ＋ `you call an uncle`）；**辛西娅全书没有叔叔这条线** | md 把受话人挂到辛西娅身上：①与原文的 `Miss Blair` 直接冲突；②与 md **同一句**后半的「管住**海伦娜**那位叔叔」自相矛盾；③与 md 自己的原句 12·中文理解（`:360`「他让**布莱尔小姐**给叔叔带话…随后他转向**伯罗斯夫人**…」）处理不一致 ⇒ **受话人归属方向错**（归属方向类，与「施事归属错」同级）<br>**改法**：`他对辛西娅说，照片会不会见光由她决定，只要她往后不时替他办几件事，比如管住海伦娜那位叔叔` → `他转向布莱尔小姐说：照片会不会见光由你们自己决定，只要她往后不时替他办几件事，比如管住她那位叔叔` | **阻断** |
| E3 | 原句 1·读者视角提示：「读者会**先**听见一句硬话，**再**看见她胃里的翻涌」 | `:35` `**Nausea rolled in Cynthia’s belly, followed quickly by indignant rage.** ‘I will not take nude photographs for you…’` —— 叙述顺序是**先身体、后台词** | md 把「叙述顺序」与「读者第一眼抓住哪句」的感受混为一谈；原文 `followed quickly by` 明示顺序 ⇒ 读者视角层的**顺序标签错**<br>**改法**：`读者会先听见一句硬话，再看见她胃里的翻涌` → `读者先看见她胃里的翻涌，才听见那句硬话` | **提示** |
| E4 | 导航·一句话概括（＝文末一句话总结）：「辛克莱临走却留下**对她叔叔的威胁**和**一笔日后要讨的人情**」 | `:360` `‘Take a message to your uncle, Miss Blair. If ’e doesn’t cease ’is investigations into my affairs, I will destroy that which ’e holds most dear. **As for you, Lady Burrows… I’ll come calling for a favour one day. And I’ll expect you to grant it.** Now, begone.’` —— 威胁的对象是**海伦娜的叔叔**；「日后要讨的人情」是**向辛西娅**索取的 | 并列句式让「人情」也挂到叔叔头上；md 的原句 12·中文理解 判得**正确** ⇒ 属摘要层的归属**省略**（非错认）<br>**改法**：`留下对她叔叔的威胁和一笔日后要讨的人情` → `留下两件事：给海伦娜叔叔的威胁，和日后要向辛西娅讨的人情`（导航行与文末总结行**两处同改**） | **提示** |
| E5 | 原句 7·中文理解：「又保证无论**那个人**提出什么要求，她都会守住界限」 | `:246` `Just know, I will do whatever I can to respect your boundaries, **no matter what he asks of us**.` —— `he` ＝辛克莱 | md 用「那个人」回避本书通行的 `他/她` 性别标记，读者无法从这一句判断要求来自谁；同章原句 12 一致用「他」指辛克莱 ⇒ 术语层不一致<br>**改法**：`无论那个人提出什么要求` → `无论辛克莱提出什么要求` | **提示** |

### 与原文相符的 31 条断言（避免「只报问题」的不完整交代）

1. 导航·一句话概括「辛西娅先以为要拍裸照，辛克莱说只需稍作改动」——`:35` `‘I will not take nude photographs for you…’` ＋ `:38` `You may stay exactly as you are… with a few minor changes.` ✓
2. 导航·一句话概括「海伦娜点破他要的是两人亲密的照片，好长期拿捏她们」——`:53` `‘Because he wants images of us together.’` ＋ `:59` `I ’ave bargaining power over both of you.` ＋ `:68` `grant me a few favours from time to time` ✓
3. 导航·一句话概括「辛西娅以休伯特的全部债据为条件答应」——`:107` `‘I want Hubert’s letters of debt before I agree. All of them.’` ✓（**是否交出原文未写**，md 未断言已到手）
4. 导航·一句话概括「摄影棚里两人互相坦白」——`:222` `‘I do like you.’` ＋ `:240` `‘I find you impossibly attractive.’` ＋ `:270` `‘I’ve never wanted anyone the way I want you.’` ✓
5. 导航·一句话概括「海伦娜用魔法灌湿底片盒与晾着的照片」——`:354` `condensing the particles of air inside until droplets formed… fill the box` ＋ `:357` `soaked them as well, blurring the clear images to black and grey smudges` ✓
6. 导航·情感弧线「开场是恶心与怒气」——`:35` `Nausea rolled in Cynthia’s belly, followed quickly by indignant rage.` ✓
7. 导航·情感弧线「中段是被人捏住把柄的恐惧和一丝不该有的心动」——`:71` `She cursed herself for being three times a fool.` ＋ `:74` `It would decimate her family and her livelihood.` ＋ `:62` `A completely inappropriate thrill` ✓
8. 导航·情感弧线「私下谈话把紧张换成坦白」——`:156` `‘I need to speak with Lady Burrows before we begin. Privately.’` → `:246` ✓
9. 导航·情感弧线「毁掉底片后短暂松弛」——`:354` `She hid a satisfied grin` ✓
10. 导航·情感弧线「最后被辛克莱临走的条件重新压紧」——`:360` `I will destroy that which ’e holds most dear.` ✓
11. 导航·Tropes「强迫拍亲密照」——`:38` `I wouldn’t require you to be in any state of undress.` ＋ `:53` ✓
12. 导航·Tropes「拿照片长期要挟」——`:68` `As long as you grant me a few favours from time to time.` ✓
13. 导航·Tropes「女巫暗中毁证」——`:354`–`:357` ✓
14. 导航·Tropes「救场的人不是外来的英雄，而是被拍的两个人自己动手」——`:107`（辛西娅谈条件）＋ `:354`/`:357`（海伦娜毁证）；本章**无第三方介入** ✓
15. 导航·Tropes「『假戏真做』只走到互相坦白，没有跨进确定关系那一步」——`:270` 双方表态，`:372` 章止于上马车；全章**无确认关系** ✓
16. 导航·人物弧线「辛西娅从宁进债务人监狱也不拍」——`:35` `If not, she would go to a debtor’s prison before she allowed herself or Helena to be used in such a deplorable manner.` ✓
17. 导航·人物弧线「走到主动索要债据」——`:107` ✓
18. 导航·人物弧线「承认自己想要一个女人」——`:270` `‘I’ve never wanted anyone the way I want you.’` ✓
19. 导航·人物弧线「海伦娜从掌控局面的人，变成先告白、先道歉的人」——`:86`/`:92` 抢先代答「We’ll do it」＋`:240` 告白＋`:246` `It is I who should apologise to you.` ✓
20. 导航·人物弧线「她的自制不是冷淡，而是不肯利用一个选择权已被剥夺的人」——`:147` `nor was there any reason to believe she would welcome her advances` ＋ `:153` `force any desire she had onto a woman whose autonomy was already compromised` ✓
21. 导航·人物弧线「辛克莱始终按生意办：照片是绳子，人情是账」——`:68` `putting a leash on that dog you call an uncle` ＋ `:360` `I’ll come calling for a favour one day.` ✓
22. 导航·叙事手法「全章分两次限知：前半贴辛西娅，空行之后改贴海伦娜」——`:35`–`:113` 辛西娅；`:115`–`:128` 整段空行；`:129` `Helena was unaccountably nervous…` 起为海伦娜，直至 `:372` ✓
23. 导航·叙事手法「拍照过程按工序写，把情欲压进玻璃版和药液里」——`:285`–`:315` ✓
24. 原句 1·中文理解（胃里翻涌→怒气→当面拒裸照→不许朋友自贬身份）——`:35` ✓
25. 原句 3·中文理解（先涌起不合时宜的兴奋／想到镜头后站着的人就熄了／心里断定他真是个魔鬼）——`:62` ✓
26. 原句 4·为什么这样写「他把要挟说成一笔互惠安排：先给一个『照片永不见光』的承诺，再把代价拆成『不时』的小事」——`:68` `I can ensure these pictures never see the light of day` ＋ `a few favours from time to time` ✓
27. 原句 6·中文理解（锋利明亮的东西刺穿心口的盾／拉近并压成耳语／因为辛克莱就在门外听着）——`:186` ✓
28. 原句 8·中文理解（对方回答／不怕女人喜欢女人／怕的只是自己的欲望／从没这样想要过一个人／退开一步，海伦娜因失去她的体温而发疼）——`:270` `‘I don’t find your attraction to women twisted in the slightest. And the only desires I fear are my own. I’ve never wanted anyone the way I want you.’ She stepped back. Helena ached at the loss of her warmth.` ✓
29. 原句 9·中文理解（相机旁／桌上的玻璃版与浅盘／取出、浸硝酸银、滑进相机／让海伦娜坐躺椅、辛西娅坐她腿上）——`:285` ✓
30. 原句 11·中文理解（目光一转／想到暗房里晾着的照片／浸湿／影像糊成黑灰污痕）——`:357` ✓
31. 原句 12·中文理解（让布莱尔小姐给叔叔带话／叔叔不停手就毁掉最珍视之物／转向伯罗斯夫人要一个人情／赶她们走）——`:360` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **POV 在 `:129` 切换**——`:35`–`:113` 辛西娅限知；`:129` `Helena was unaccountably nervous as Sinclair led them further down the corridor and into another room.` 起为海伦娜限知。md 导航·叙事手法写「全章分两次限知：前半贴辛西娅，空行之后改贴海伦娜」**成立**；**不得**把 `:129` 之后的内心句归给辛西娅。
2. **原句 7 的引语用 `…` 公开标注省略**——省略的是 `:246` 中段（「该道歉的是我」「我会体验欢愉」「这不可原谅」）。块内分析（中文理解／为什么这样写／读者视角提示）**只覆盖被引的三段**，未越界 ⇒ **不构成引语截短**；导航里的「先道歉」由原文 `:246` 独立支撑。
3. **`:38` `My suggestions is ’ardly as depraved as all that.`** 是原文自身的语法瑕疵（复数名词配单数动词）——**照录，不得「修正」**；md 原句 2 引语逐字照抄，**成立**。
4. **`:345` `I’m so close! Soon. Soon, it will be done All of this will be worth it.`** 是原文自身的缺句读——**不得自行补句点**；md 未引用该处。
5. **`:339` `But now⁠—`** 破折号前带 **U+2060 word joiner**——若后续引到该句，须保留该字符（归一化时不得当噪声删除，否则与原文子串不匹配）。
6. **债务数额与债据交付，原文两处都没落地**——`:164`（ch11）只写 `spoke an outrageous sum`；`:107`（本章）辛西娅索要全部债据，本章**始终没写辛克莱是否交出**。md 两处都未断言已到手 ⇒ **成立**，**不得回填**。
7. **`:264` 是「计划」、`:354`/`:357` 才是「执行」**——md 的原句 10、原句 11 恰好分别引在执行处，成立；**不得**把原句 10 写成「她早已计划好」。
8. **原句 12·中文理解 对「威胁→海伦娜的叔叔、人情→辛西娅」判得正确**——`:360` `Take a message to your uncle, Miss Blair.` 与 `As for you, Lady Burrows… I’ll come calling for a favour one day.`；这是 E2 的对照基准，**不得**借修 E2 之机改动原句 12。
9. **「假戏真做只走到互相坦白」**——全章到 `:372` 为止**没有**确认关系、没有约定、没有承诺未来 ⇒ 成立。
10. **原句 8 的受话方向**（辛西娅答海伦娜、且叙述句 `Helena ached at the loss of her warmth` 的受事是**辛西娅的体温**）判得正确 ⇒ 成立。
11. **艾莉的幻象（`:132`/`:135`）与「克里奥和我哥哥」（`:339`）md 未引用**——这是**覆盖取舍**（记为 L1/L2 建议项），**不得**反向写成「原文没有幻象」或「原文没有克里奥」。
12. **克里奥与哥哥的关系**——`:339` 说话人是**辛西娅**（她提到「我哥哥」）；克里奥是**海伦娜的表姐**（ch02 `:35` `her cousin, Clio`）兼**辛西娅哥哥托马斯的伴侣**（ch05 `:56` `Clio and Thomas`）——md 未涉及，不得在修稿时把两人关系颠倒。
13. **`:107`/`:74` 的债据与药妆店**——`:74` `The apothecary shop was patronised by the beau monde’s most elite ladies.` 证明该店由上流社会最上层夫人光顾，与 ch11「药妆店」的描述相合；md 本章未引用该句，无写法冲突。
14. **词表 22 条例句全部逐字取自本章**——22/22 逐字回源命中、22/22 词头在例句内，**不得改写例句**。
15. **词表分隔行 `|------|------|------|------|`** ——GFM 合法表格，**不判缺陷**（本书两种写法并存：`|---|…` 与 `|------|…`）。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，109 事件 / 10 关系 / 10 数字 / 5 未决 / 15 陷阱）→ R2 机器层 → R3 三张单子 → R4 逐块 12/12 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 / ch06 / ch07，批 3 = ch08 / ch09 / ch10，批 4 = ch11 / **ch12（本表）**⇒ **11 / 27 章**已完成 R0–R5（ch12 为第 11 章）。ch01 与其余 16 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：
  - E1 的判定口径（**阻断**）与 ch11 E1（**提示**）不同：ch11 的「水巫点明动手的是谁」是把**暗示升级为定论**（叙事责任归属越级），ch12 的「两句之间没有转折词」是**对原文措辞的否定断言且被自身引语当场证伪**。口径记录在案，以免下一轮误按「措辞级一律提示」放宽。
  - E2 已用三重证据交叉确认（原文 `Miss Blair`／md 同句自相矛盾／md 原句 12 的正确处理），判定**阻断**而非提示。
  - L3（`:246` 中段省略）刻意**未判引语截短**：省略由 `…` 公开标注、块内分析未越界；但它同时是原句 8 的直接前件，故列为**建议补**。
  - 本章**双 POV**，R4 的三问须分别对两段限知核；已按 `:129` 分界逐块核过，未发现把海伦娜段当成辛西娅段或反之的写法。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
