# ch09 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，266 行全读，72 事件 / 13 关系 / 7 数字 / 7 未决 / 10 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=9 / words=2756 / block_target=[5,9]）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`、`keyword_long=0`、`hole=0`。
> 补验（机器盲区）：本章 9 条引语**均无 `…`**（自建探针确认），故 `verify_fragments_indep.py` 无本章片段；本章 22 行词表例句 **22/22 逐字回源命中**（`/tmp/vocab_check_hx.py`）、**22/22 词头落在例句内**（`/tmp/vocab_head_hx.py`）。**引号配对**机器层零覆盖，另建探针 `/tmp/pair4_hx.py` 全书扫描（见 §五）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号 + 逐字） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:248`–`:266` 五段收束：`The primitive instinct resonated in her bones.` → `She blinked hard.` → `What madness is this?` → `She was water in a glassy pool.` → `But not now. Need coalesced with anger, rising like a wave mighty enough to crash upon the shore and destroy her enemies. It was chaos and power and glory.` → `She would reclaim her calm later.` → `This night, she would ride the crest of her magic into the heart of a devil’s lair.` —— **本章真正的收尾：占有念头没有压下去，而是与怒气凝聚成攻势，她要骑着魔法的浪峰闯进魔鬼的老巢** | md 的 9 个引语块**最末一块是 `:245` 的 `Mine.`**；`:248`–`:266` 全章 md 未覆盖，也无任何分析提及 | **阻断**（关键转折缺失，且是 E2「章末落到一个单词」误判的根因） |
| L2 | `:167` `Ensuring Cynthia’s safety was completely secondary to solving the case.` —— 海伦娜自认「保辛西娅的安全**完全次于**破案」（她跟进去的真理由是案子，不是救人） | md **未提这一层**；原句 9·读者视角提示只写到「先前那些『我只是来阻止她』的说法，已经撑不住了」（覆盖 `:38`／`:170`／`:173` 的表层） | **不构成阻断**（人物刻画细部）；**建议**在导航·人物弧线或原句 9 补一句「她跟进去的真理由是案子」 |
| L3 | `:53` `And she saw Cynthia in the centre of the Devil’s den. Trapped in a room swathed in crimson velvet and black lace.` —— 埃莉幻象里辛西娅**被困**在 crimson velvet 与 black lace 装点的房间 | md **分析层未提**；`velvet` 一行的例句正是这半句（`:53`），但没接回原句 8 的「私人办公室」邀请 | **不构成阻断**（词表已收录原句）；**建议**在原句 8·读者视角提示接上幻象（`:242` 海伦娜已把两者联起来） |
| L4 | `:104` `Saving the woman was Helena’s only option. She had no other choice.` —— 「救她是唯一的选项」 | md 未提 | **不构成阻断**（覆盖取舍） |
| L5 | `:113` `A resonant knowing pulled her to the woman as inevitably as river water flowed to the sea, eternally seeking its origin.` —— 「河水必然流向大海」的比喻（辛西娅是她的源头） | md 原句 5 的引语止于 `on a moonless night.`，未含此句；分析层也未用「河→海」这层 | **不构成阻断**（选段取舍；md 导航·叙事手法已把「河、海」列入水意象） |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–9 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的三处疑点：

- **「Mine.」是不是魔宠（哈姆雷特）的宣示**：`:245` `Mine.` 紧接 `:248` `The primitive instinct resonated in her bones.`，`:251` `She blinked hard.`、`:254` `What madness is this?` —— 归属对象是**辛西娅**（海伦娜对她的占有念头），不是狐狸。md 原句 9·为什么这样写「本能先替她答了话」：**成立**。
- **「哈姆雷特是不是跟着海伦娜到了门口」**：`:35` 哈姆雷特在车上，`:116` `Without thought, she slipped out of the carriage, locking a disgruntled Hamlet inside.` —— 狐狸**被锁在车里**，海伦娜是独自下车。md 导航只说「带着……狐狸哈姆雷特」，未说他随行到门口：**成立**（不构成编造）。
- **「辛克莱是不是马上被捕／定罪」**：`:77`–`:83` 叔叔关了他三小时后**因无证据被法官要求放人**，`:92` 叔叔与托马斯确信有罪但缺证据。md 导航·人物弧线写「扣人三小时就被律师带走」：**成立**（原文 `:77` 即以 `before his solicitors demanded his release` 收尾）。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 导航·一句话概括 ＋ 一句话总结 | 「海伦娜心里冒出一个『我的』，**又把它压了回去**」／「她心里冒出一句『我的』，**又硬生生按了回去**」 | `:245` `Mine.` → `:251` `She blinked hard.` → `:260` `But not now. **Need coalesced with anger**, rising like a wave mighty enough to crash upon the shore and destroy her enemies. It was chaos and power and glory.` → `:263` `She would reclaim her calm later.` → `:266` `This night, she would ride the crest of her magic into the heart of a devil’s lair.` —— 她**没有压下去**：`reclaim her calm` 明写是「**以后**再取回平静」，`But not now` 明写「不是现在」，全章收在**冲进魔鬼老巢**的攻势上 | **阻断**（故事层动作与原文相反；且 md 自身原句 9·为什么这样写「本能先替她**答了话**」、读者视角提示「已经撑不住了」⇒ md 内部自相矛盾） |
| E2 | 导航·叙事手法 ＋ 原句 9·读者视角提示 | 「**章末**用一串独立成段的短句收束，**最后落到一个单词**」／「整章的试探、争辩、靠近，**最后落在这么一个短促的词上**」 | `:266` `This night, she would ride the crest of her magic into the heart of a devil’s lair.` —— 全章**末句是完整句**；「一个单词」落在 `:245`，其后还有 `:248`–`:266` **五段** | **阻断**（叙事层结构断言与原文不符；同一字段在 ch08 写的是「章末用一次沉默和一句短念收束」，那与 ch08 原文 `:308`/`:314` 严丝合缝，可见本字段的口径＝**原文章末**） |
| E3 | 原句 1·中文理解 ＋ 读者视角提示 | 「可**没有裙撑、裙摆又是开衩的**，行动起来更方便」「**开衩是为了跑动**」 | `:35` `but the **lack of** bustle and split skirts would allow greater ability to manoeuvre` —— 英文 `the lack of bustle and split skirts` 语法上 `lack of` 统辖两项（＝**没有**裙撑、**没有**开衩裙摆）；md 取的是另一读法（骑装有开衩、无裙撑） | **提示**（英文本身歧义，md 取的是骑装惯例读法、与实物相合；不改，但须留记以免下一轮被当成错改） |
| E4 | 原句 2 相关表述（导航·Tropes） | 「海伦娜**自称只是来阻止麻烦**」 | `:38` `I’m just doing this to stop the foolish woman from getting into **even more trouble**.` —— 她说的是「不想让她**惹上更多**麻烦」，不是「来阻止麻烦」 | **提示**（措辞级；同章原句 2·中文理解写的是「不想让那个蠢女人惹上更大的麻烦」，与原文一致 ⇒ md 内部精度不匀） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 挪身子、骑装便于行动与藏身、狐狸贴上来 | 海伦娜挪动；哈姆雷特跳上座位 | 她身侧的座位 | 「深蓝是为了融进阴影」＝她的选择 | 对应成立 |
| 2 | 三层自我说服（回嘴／动机／预视） | 海伦娜对哈姆雷特说 | 「那个蠢女人」＝辛西娅 | 「比我以为的」＝她早就在估量辛西娅 | 对应成立 |
| 3 | 绿门后是「魔鬼的交易」与一千种恶习 | 海伦娜知道（叙述层判断） | 那扇新刷过漆的门 | 「她知道不是这么回事」＝海伦娜的先验 | 对应成立 |
| 4 | 溺水／掀面纱／学会游泳 | 叔叔掀开帷幕，海伦娜旁观 | 辛西娅的婚姻 | 「学会游泳」的是**辛西娅**，海伦娜只是看见 | 对应成立 |
| 5 | 深紫斗篷遮脸，仍认得出 | 海伦娜辨认 | 辛西娅 | 「认得出」的是海伦娜 | 对应成立 |
| 6 | 转过来、需要如重拳、几乎吻上去（停在想象） | 海伦娜转她；「need」作主语 | 辛西娅的榛色眼睛与胸口 | 「几乎把她击倒」的「她」＝**海伦娜**（`a punch of need nearly knocked her over`，主语是海伦娜） | 对应成立 |
| 7 | 不让别人左右选择，划界「问题／棋子」 | 辛西娅对海伦娜说 | 海伦娜·布莱尔（点名） | 「that includes you」＝把海伦娜并入「别人」 | 对应成立 |
| 8 | 侍者代辛克莱发出私人办公室邀请 | 侍者说 | 辛西娅、海伦娜 | 「该用哪种称谓都想好了」＝辛克莱事先知情 | 对应成立 |
| 9 | 一个词，没有主语宾语 | 海伦娜（内心） | 无 | 「本能先替她答了话」＝海伦娜 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 09. Chapter Nine`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 **9**，落在本书区间 [6,13] 与本章 `block_target=[5,9]` 内（**已触上限**：若因修复增块，会触发 `block_count`）。

### 引号配对（机器层零覆盖，自建探针）

`/tmp/pair4_hx.py` 全书扫描 27 章：判据＝**引语块内层以闭引号 `’`/`”` 结尾、且全块不含任何开引号 `‘`/`“`**（即孤儿的闭引号）。

```
ch09 into the devils den.md
   原句7 内层末尾 '’ 且全块无开引号 → 孤儿闭引号 | I’m tired of letting other people’s opinions control my choi...
TOTAL 1
```

**全书仅 1 处**，在 ch09 原句 7：md 引语为 `"I’m tired of … your pawn to control.’"` —— 外层是直双引号 `"`，内层末尾多出一个 `’`（原文 `:212` 整句的闭引号），**开引号 `‘` 被切掉时一并丢了**。全书其余 28 个「内层以 `’` 结尾」的引语块**块内都含配对的开引号**，不属此类。

对照本库体例：ch08 原句 7 同样从对白中间切起（`We’ve been tryin’ to get something on Sinclair…`），但**末尾不带 `’`** ⇒ 本库对「切段引语」的规定是**连同闭引号一起去掉**。ch09 原句 7 漏了这一步。

## 六、语料层观察（非 md 缺陷，不计入三张单子）

本章**无**站点宣传行注入（全书 5 章 6 行：ch03:188 / ch08:170+173 / ch13:185 / ch19:197 / ch25:214，见 ch08 的 §六）。本章 md 9 条引语**无一跨过** `:256` 一类的空行断裂，`segment_miss=0` 已证逐字。
