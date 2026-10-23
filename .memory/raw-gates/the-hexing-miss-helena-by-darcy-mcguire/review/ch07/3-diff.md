# ch07 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，397 行全读，89 事件 / 15 关系 / 7 数字 / 8 未决 / 18 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=10 / words=3128 / block_target=[6,10]）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`。
> 补验（机器盲区）：`verify_fragments_indep.py` 全书 312 片段 0 MISS；本章 22 行词表例句 22/22 逐字命中（`/tmp/vocab_check_hx.py`）、22/22 词头落在例句内（`/tmp/vocab_head_hx.py`）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:38–47` `Since childhood, she had lived by three unbreakable rules: Don’t reveal your powers to anyone outside of kin and coven. Don’t trust anyone outside of kin and coven. Don’t love anyone outside of kin and coven.` —— 三条规则本身（不显露力量／不信任／不爱） | md 引语从 `:50` 起，导航只写「破了一条规矩」，**读者无从知道规矩是什么**；原句 1·为什么这样写「第一句只交代『破了一条规矩』，不说是哪一条」在**该引语内部**成立，但把整条规则清单排除在 md 之外 | **不构成阻断**（md 的分析本身准确；属选句取舍），但建议在导航「一句话概括」或原句 1 补一句「三条规矩：不显露力量／不信任／不爱」 |
| L2 | `:62` `She pulled the water from the air and rushed forward on a wave of power made even more potent by her fear. … a girl running on a river of water that disappeared like mist in a moment`（童年已能召水驱身）；`:65` 老坎贝尔太太的苏格兰方言 `‘Yer bleeding’, lass.` | md 导航把童年段概括为「母亲变成了可怕又扭曲的东西，她带伤逃到罗温姑妈家却扑了空，最后把一切告诉坎贝尔老太太」，**未提召水与方言** | **不构成阻断**（本章主题是「信任外人的代价」，非能力展示） |
| L3 | `:378–381` `‘The evidence to exonerate Cynthia.’ It was the first time Helena used Cynthia’s name. Tingles washed over her skin before she processed the words that came before her name.` | md 全章未提「第一次叫她的名字」与随之而来的战栗 | **不构成阻断**（人物弧线的细微推进，未覆盖不算错） |
| L4 | `:360` `I chased the bastard for twenty blocks. He lost me in the Seven Dials.`（警司追了二十个街区，仍在七钟区被甩掉，裤脚滴泥） | md 导航「Tropes」写了「入室窃贼」，但**追捕结果**未提 | **不构成阻断** |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–10 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的三处疑点：

- 「辛西娅主动把开保险箱的责任揽到自己身上」的**归属方向**：`:363` `‘It was my idea.’ Cynthia didn’t need to give Helena another reason to mistrust her.` ——受益方是**辛西娅自己**（她不愿给海伦娜多一个怀疑她的理由），md 导航写成「替海伦娜挡了一次怀疑」⇒ 见 E3。
- 「DOSD」是人名还是缩写：`:291` `A curious combination of letters was repeated often. DOSD.` ⇒ 是**反复出现的字母组合**，md 原句 8·中文理解写「那个神秘的字母组合」：**成立**。
- 「Newgate」是监狱：`:321` `Newgate will be in charge of my room and board until I hang for murder.` ⇒ 监狱名，md 词表 `noose` 一行的中文理解写「绞刑架上的绞索」并把 Newgate 译作「新门监狱」：**成立**。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 导航·Tropes 兑现/反转 | 「海伦娜的水魔法**制住了**贼，却把他送出墙外」 | `:176` `She pooled her powers, throwing a blast of water that tumbled the boy across the manicured lawn, **inadvertently aiding his escape**. He recovered his feet and dove through the hedges before she could lobby a second attack.` ——她**没有制住**他，反而帮了他逃；同句「制住了」与「送出墙外」自相矛盾 | **提示**（措辞级；md 同章「一句话概括」写的是「反倒帮他逃走」，与原文一致 ⇒ md 内部不一致） |
| E2 | 导航·一句话概括 | 「三人上三楼撞见**正在撬保险箱**的窃贼」 | `:158` `He was holding a painting he’d just removed from the wall. Behind the painting was the steel glint of Hubert’s safe.`；`:185` `she turned from the window to assess whether the thief had managed to open the safe.` ——他刚**取下画作**、保险箱尚未打开 | **提示**（措辞级） |
| E3 | 导航·Tropes 兑现/反转 | 「辛西娅主动把开保险箱的责任揽到自己身上，等于**替海伦娜**挡了一次怀疑」 | `:363` `‘It was my idea.’ Cynthia didn’t need to give Helena another reason to mistrust her.` ——她抢责是**为自己**：不给海伦娜多一个不信她的理由 | **提示**（归属方向错） |
| E4 | 原句 10·为什么这样写 | 「信里**把对方称作魔鬼**，但这一章没有点名魔鬼是谁」 | `:396` `The deadline has passed. Fulfil your bargain or pay your debt in full. Breaking a deal with the Devil carries profound consequences.` ——信中「你」是收信人，**魔鬼是收信人所交易的对象**，不是收信人；「对方」在中文里最自然地读成「收信人」 | **提示**（指代含混，易被读成「收信人＝魔鬼」） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 破了一条规矩＋被气味与眼睛击溃 | 她刚破了一条规矩；女人俯身发问 | 榛色眼睛、香草与忍冬 | 「失去理智」＝海伦娜 | 对应成立 |
| 2 | 从家里逃出、母亲变成可怕扭曲的东西 | 她跑，血顺手臂滴 | 母亲 | 「变成了别的东西」 | 对应成立 |
| 3 | 从裙褶取出吊坠＋承认昨天撒谎 | 辛西娅伸手入裙褶、承认撒谎 | 那件要命的珠宝 | 「我昨天对你撒了谎」＝辛西娅对海伦娜 | 对应成立 |
| 4 | 怒其冷酷、礼物转送情妇是存心残忍 | 愤怒升起；他冷酷地对待妻子 | 求爱时送她的礼物 | 「求爱时送给她的」＝辛西娅 | 对应成立 |
| 5 | 窃贼僵住、画后是保险箱 | 年轻男子取下画后僵住；男仆被绑 | 保险箱的钢光 | 「休伯特的保险箱」 | 对应成立 |
| 6 | 水击把贼掀翻、反而助其逃走 | 她聚力掷出水浪 | 少年、修剪整齐的草坪 | 「无意中帮他」的正是她这一击 | 对应成立 |
| 7 | 「我没有罪」＋两人近得能数清雀斑 | 她转身面对海伦娜 | 辛西娅鼻梁上的雀斑 | 「你让我害怕」＝辛西娅 | 对应成立 |
| 8 | 账本上的巨额与 DOSD | 辛西娅翻页 | 丈夫笔迹的条目、神秘的 DOSD | 「休伯特欠 DOSD」 | 对应成立 |
| 9 | 触电般的欲望＋「海伦娜＝电流本身」 | 她抓向带电的线 | 穿过自己的电流 | 「每次碰到海伦娜」 | 对应成立 |
| 10 | 期限已过、履约或还债 | 信上写 | 三句条文 | 「与魔鬼毁约的后果」 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 07. Chapter Seven`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 10，落在本书区间 [6,13] 与本章 `block_target=[6,10]` 内（**已触上限**：若因修复增块，会触发 `block_count`）。
