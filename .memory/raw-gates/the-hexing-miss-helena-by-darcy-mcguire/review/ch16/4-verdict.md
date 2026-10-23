# ch16 · R5 判定表

- 书：`the-hexing-miss-helena-by-darcy-mcguire`
- 章：ch16（`ch16 lilys father.md` ↔ `text/ch16_chapter_16.txt`，290 行）
- 档位：**深审 R1–R5 全量**（用户确认升级）
- 日期：2026-10-23
- 配套：`1-suread.json`（R1）· `2-machine.json`（R2）· `3-diff.md`（R3＋R4）

## 一 报数（只报四组）

| 组 | 结果 |
|---|---|
| **逐字** | 引语 **9/9** verbatim（`chapter.sh` `segment_miss 0`；`verify_fragments_indep.py` 全书 312 片段 **MISS 0**、拼接未标省略号 **0**）· 词表例句 **22/22** 为 ch16 原句（`missing=0`）· 词头 **22/22** 在本章原文出现（`rc=0`）· 素读底稿逐字复核 **210 条 BAD=0**，投毒 0→1→0 |
| **对应** | **9/9**（R4 逐块三问全过；施事／归属调转 **0** 处） |
| **形态** | **8/8**（H1 ✅／导航 5 项 ✅／块数 9 ∈ `block_target [5,9]` ✅ **已触上限**／`block_hint` 空 ✅／子项集 4×9 ✅／词表标准 `\|` 表格 ✅／一句话总结 ✅／frontmatter ✅） |
| **断言** | 共核 **70** ＝ 相符 **41** ／ 提示 **26** ／ **阻断 3** ／ 假红 0 ／ 编 **0** |

## 二 阻断（3 条，全部附原文逐字）

### 阻断 1 · E1 「罗温**姑妈**」应为「罗温**姨妈**」（本章 8 处 / 6 行；全书 21 处 / 6 章）

**证据（逐字）**
- `text/ch02_chapter_2.txt:155` — `Willow Blair had been the prettiest of her three sisters, and the most monstrous.`
- `text/ch02_chapter_2.txt:212` — `Clio, Ellie, and Helena had all been raised together by their Aunt Rowan. While Clio and Ellie were true sisters, they treated Helena like another sibling.`
- `text/ch06_chapter_6.txt:35` — `the cherry wood table passed down to the Blair women through generations … Blair women strung together like beads of amber, stretching back to the 1600s … safe in the circle of sisterhood that bound them.`
- `text/ch06_chapter_6.txt:122` — `Aunt Rowan opened All Things Bright and Beautiful when they fled Scotland … the high-end products Clio and Aunt Rowan created, providing the Blair women with a lavish lifestyle they all enjoyed.`
- `text/ch07_chapter_7.txt:56` — `running from her mother as blood dripped down her arm … Aunt Rowan’s was a fifteen-minute walk from their cottage in the woods`
- `text/ch06_chapter_6.txt:50` — `‘Something is blocking your cousin’s powers.’ Aunt Rowan …`

**推理**：Blair 是**母系**女巫世家姓（`ch06:35`）；Rowan 被算进「the Blair women」这一群（`ch06:122`）；她是海伦娜、Clio、Ellie **三个表姐妹共同的姨**（`ch02:212`＋`ch06:50`＋`ch06:116`/`:119`），而三人只能通过各自的 Blair 母亲（Willow 的姐妹，`ch02:155`）相连 ⇒ Rowan 在**母系**。
**零命中取证**（R5-补，命令＋输出＋退出码见 `3-diff.md` §三 E1 专节第 6 条）：
```
/usr/bin/grep -nEi 'Helena.s (father|mother|parents)' text/*.txt  → 0 行，rc=1
/usr/bin/grep -nEi 'helena.s father|her father|…|Mr\.? Blair|…' text/ch01…ch07,ch14 → 4 行，rc=0，全部指 **Cynthia** 的父亲
正对照：/usr/bin/grep -nEi 'Willow' text/*.txt | /usr/bin/grep -Ei 'sister|Blair|…' → 1 行，rc=0（ch02:155）
```
⇒ 「姑妈」＝父亲之姐妹，而海伦娜的父亲在全书 27 章零提及。**「姑妈」在本库无立足点。**

**全书分布实测**：姑妈 **21**（ch04×1／ch06×4／ch07×1／ch14×4／ch15×3／ch16×8）｜姨妈 **25**（`00_概述`×1／`00_金句精选`×2／`00_情感节点`×1／ch24×3／ch25×2／ch26×16）。
⇒ 修复方向与多数派一致，**不需要「按多数派统一」的让步**；这是一次有原文依据的裁决，不是取多。

**改法（本章 6 行；其余 5 章在汇总指令里单独出）**

| md 行 | 改前 | 改后 |
|---|---|---|
| md:10（2 处） | `…海伦娜认出这是罗温姑妈发怒时出现过的天象，心里判断辛西娅和姑妈一样是地巫；…` | `…海伦娜认出这是罗温姨妈发怒时出现过的天象，心里判断辛西娅和姨妈一样是地巫；…` |
| md:20（2 处） | `**中文理解**：海伦娜从未被人施过咒，罗温姑妈倒有过一次；咒解开之后，姑妈把那种感觉说成从一场古怪的催眠里醒来。…` | `**中文理解**：海伦娜从未被人施过咒，罗温姨妈倒有过一次；咒解开之后，姨妈把那种感觉说成从一场古怪的催眠里醒来。…` |
| md:24 | `**为什么这样写**：先借姑妈的旧事立一个比喻，…` | `**为什么这样写**：先借姨妈的旧事立一个比喻，…` |
| md:70 | `…这样的天气她见过：罗温姑妈气到极点时，…` | `…这样的天气她见过：罗温姨妈气到极点时，…` |
| md:74 | `…只让读者跟着她想起罗温姑妈；…` | `…只让读者跟着她想起罗温姨妈；…` |
| md:80 | `**中文理解**：罗温姑妈警告过她，要小心行事：…` | `**中文理解**：罗温姨妈警告过她，要小心行事：…` |

> ⚠️ md:10／md:13／md:14 三行同时收到多条修复，**请用本文件 §四 的「整行合并版」**，不要按上表逐条打补丁（会互相覆盖）。

### 阻断 2 · E2 节奏断言被 md 自身引语量化证伪（判据 (f)）

- **位置**：md:54（原句 4 · 为什么这样写）
- **md 原文**：`句子一句比一句短，最后落到家训“我们不伤人”。`
- **证据**：md 自己的引语 `text/ch16_chapter_16.txt:137` —
  `‘He wants the riches your potions bring. He needs your power. That is not love. You are making love spells. I saw the ingredients. I know what that means. It isn’t right to steal someone’s will. You are breaking our most sacred oath for him. We do no harm.’`
  九句词数实测 **7, 4, 4, 5, 4, 5, 7, 9, 4** ⇒ **非单调递减**，第 8 句（9 词）反而是全段最长。
- **改前**：`**为什么这样写**：她把“钱”“力量”“爱”三样并排，先拆穿那个男人的动机，再指出母亲正在做的事；句子一句比一句短，最后落到家训“我们不伤人”。这不是劝，是当面定罪；“我见过那些材料”让指责有了物证，也让她后来的恐惧有了来处。`
- **改后**：`**为什么这样写**：她把“钱”“力量”“爱”三样并排，先拆穿那个男人的动机，再指出母亲正在做的事；九句话在四到九个词之间反复收紧，最后落回最短的那一档——家训“我们不伤人”。这不是劝，是当面定罪；“我见过那些材料”让指责有了物证，也让她后来的恐惧有了来处。`

### 阻断 3 · L1 私誓整条漏掉（S1「漏掉关键转折」）

- **位置**：md 全篇（导航 5 行＋9 个引语块均无）
- **证据**：
  - `text/ch16_chapter_16.txt:173` — `But she had created this mess because of deeply buried fear and a promise she made to herself long ago.`
  - `text/ch16_chapter_16.txt:176` — `The Blair women came from a prestigious line of light witches devoted to the arts of healing and health. They swore to do no harm and lived by that promise. When Helena’s mother strayed so far from her vow, Helena made another oath. **A private promise to never fall in love with another. To never give someone such control over her heart and her choices.**`
  - `text/ch16_chapter_16.txt:161` — `Though she endeavoured to be nothing like her mother, she still emulated the woman.`
- **为什么是阻断**：本章核心冲突（海伦娜为什么把 `:128` 那句玩笑式的 `‘Are you using me for my magic?’` 说成 `:155` `I just don’t like the idea of being used for my magic.`，并因此把辛西娅推开）**只有 `:176` 这条私誓能解释**，而原文自己把因果写死在 `:173`。md 漏掉它，导致 md:13 只能写成「她始终用'朋友'和'帮忙'给感情包一层壳」这种**没有来历**的概括。
  另：`原句 4` 只收了巫团家训 `We do no harm.`，**没有**收海伦娜自己另立的那条——两者是不同的誓，不可互相代替（与本项目既有记忆一致：「不做伤害」的誓属布莱尔家女巫团，破誓者是薇洛；海伦娜的私誓是「绝不爱上任何人」）。
- **改法**：**不得增第 10 块**（块数 9 已触 `block_target [5,9]` 上限）。改为写进 md:13 人物弧线，见 §四 整行合并版。

## 三 提示（26 条，只记不改；如执行方一并处理更好）

| 编号 | 位置 | 问题 | 原文依据 |
|---|---|---|---|
| E3 | md:12 | 「吻后被管家**撞见**」→ 实为被敲门**打断**，整理好才开门 | `:41` `‘Just a moment,’ Cynthia called to the door`；`:47` `They were as ready as they would ever be.`；`:50` `‘Come in.’` |
| E4 | md:10 | 「**捧着**家具清单进来」→ 端的是茶点托盘，清单从围裙掏出 | `:53` `entered with a tray in her hands carrying fresh coffee and tea … pulled out a piece of parchment from her apron` |
| E5 | md:10 | 「辛西娅由此**追问出**莉莉的父亲就是乔治·利珀特」→ 名字是管家先自己说的；问句无 tag | `:77` `Say what you will about George Lippert…`；`:80` `‘Lily’s father is George Lippert?’`（无 tag，见 U1） |
| E6 | md:10 | 「海伦娜**被'利用'二字**勾起旧事」→ 触发点是她自己那句玩笑 | `:128` `‘Are you using me for my magic?’ She said the question in jest, but no sooner had it escaped than fear, sudden and sickening, coursed through her. An old memory surged forth.` |
| E7 | md:12 | 「把**一句求援**听成了拒绝」→ 被听岔的是自我防卫＋先前的同行之约 | `:155` `I just don’t like the idea of being used for my magic.`；`:158` `You asked to come with me` |
| E8 | md:14 | 「以**无提示**的闪回插入」→ 有明文提示，只是无排版标记 | `:128` 末 `An old memory surged forth.`；`:131` 直接起对白 |
| E9 | md:40 | 「脸上的纹路**松开**」→ `creased into` 是皱出／挤出，方向相反 | `:92` `Mrs Higgins’ face creased into lines of kindness` |
| E10 | md:58/60 | **引语截短**：中文理解讲了「眼睛睁大」，该句不在引语内（S2 ①） | `:158` `Cynthia’s hazel eyes widened as her lips parted on an inhalation. ‘Used? …’` |
| E11 | md:74 | 「她**没有说破**是谁在呼风唤雨」→ 只就引语成立，下一行就说破了；与 md:10 内部张力 | `:212` `She’s an earthwitch, just like Aunt Rowan.` |
| E12 | md:96 | 「哈姆雷特**先替海伦娜**走近了辛西娅」→ 原文未给狐狸任何代理动机 | `:251` `Hamlet hopped nimbly from the couch and wound his way to Cynthia` |
| E13 | md:14 | 「**章末**让哈姆雷特去蹭辛西娅」→ 蹭腿在 `:251`，其后还有 19 行 | `:254`–`:290` |
| E14 | md:10/md:14 | 星尘念头写成确定的「海伦娜心声」→ 原文自陈来源不明（对比 ch15 md:10 保留 hedge 的做法） | `:257` `She blinked, not sure if the thought came from her own mind or the cosmos.` |
| E15 | md:119 | `vulnerable` 放在 ⭐⭐⭐ 高级 ⇒ **档位注水**（S4 ③）；同档其余 7 条均较难或为本书自造 | `:197` `The courageous woman had no idea how vulnerable she was amongst murderers and madmen.` |
| E16 | md:132 / md:140 | `prospects`、`address` 两条例句末尾残留原文闭引号 `’`，其余 20 条无（`check_vocab.py` 不查） | `:92` / `:95` |
| L2 | md:13 | 辛西娅自陈「我也知道被利用是什么滋味」并**主动解除义务**，md 未收 | `:191` `But I also know what it is to be used. I won’t do that to you. You are under no obligation to come with me.` |
| L3 | md:11 | 海伦娜的**恐惧换了对象**（怕失去自己 → 怕失去辛西娅），md 未写 | `:197` `A new fear blossomed in Helena. Not that she might lose herself in Cynthia, but that she might lose Cynthia altogether.` |
| L4 | md:12 | 辛西娅「贵族女子该当一朵装饰性的花」整段，是 ch15 性别主题的直接续写，md 未点出 | `:209` `Society believes women of the peerage should behave as gentle, bright blossoms … no opinions, no personal drive, no purpose beyond decorative value.` |
| L5 | md:14 | 海伦娜**换招失败**这一拍没写，而正是它引出「我们？」 | `:236` `Switching tacks…`；`:242` `Hecate help me, I’m making things worse.`；`:248` `‘We?’` |
| L6 | md:106 | 「她本可以退开」这个岔路口没写 | `:263` `Helena could still back away. But every tiny piece of her wanted to join Cynthia on this adventure.`；`:266` `On every adventure.` |
| L7 | md:11/13 | 「剧烈的嫉妒」是本章海伦娜最直白的自我暴露，md 零提及 | `:275` `Imagining anyone else stepping into such an intimate role filled Helena with violent jealousy.` |
| L8 | md:98 之后 | 真正的收尾三句（`Will you let me help you?` / `I never wanted to do this alone.` / `Then we shall do it together.` ＋ `A fractured piece of her heart clicked into place.`）**不在任何引语块里**，而 md:11／md:14 都在指它 | `:278` `Because she wasn’t just asking about this investigation.`；`:281`；`:284` |
| L9 | md:14 | 「雷雨跟着辛西娅的情绪走」只写了前半，**雨过天晴**没写 | `:281` `a smile breaking over her as the sun tentatively peeked through the storm clouds` |
| L10 | md:13 | 词表收了 `endeavoured` 用这句作例句，**分析层完全没碰** | `:161` `Though she endeavoured to be nothing like her mother, she still emulated the woman.` |
| L11 | md:10/13 | 误会**当页就被海伦娜自己想通了**，md 读起来像延续到章末 | `:164` `Of course Cynthia wasn’t trying to use her. She was nothing like the man Willow chose.` |
| L12 | md:13 | 海伦娜**先道歉**这一拍没写 | `:188` `‘Cyn, I’m the one who should be asking for your forgiveness.’` |
| L13 | md:11 | 「章末没有告白」方向对，但没点出原文是**又一次自我否认**，与 `:179` 首尾呼应 | `:290` `She didn’t have time to worry about falling in love with a witch…`；`:179` `But I’m not falling in love with Cynthia.` |

## 四 整行合并版改法（md:10–md:14 ＋ 分析层 6 行）

> md:10／11／12／13／14 各自同时收到 2–6 条修复。**必须整行替换，不要逐条打补丁。**
> 替换后须重跑：`bash scripts/chapter.sh "…/ch16 lilys father.md"`（期望 rc=0）＋ `python3 scripts/check_chinese_layer.py`（期望无新增夹杂）。

**md:10 · 一句话概括**（收 E1×2、E4、E5、E6、E14＋消歧）

- 改前：
  `- **一句话概括**：晚宴一周后的周三下午，紧接上一章的吻，海伦娜在辛西娅的客厅里刚整理好衣鬓，管家希金斯太太便捧着阿盖尔夫人索要的家具清单进来；她提起被辞退的年轻女仆莉莉，辛西娅由此追问出莉莉的父亲就是乔治·利珀特、家住齐普赛德，并拿到了地址。利珀特正是辛克莱脑中闪过的那个名字，辛西娅提议当天就去齐普赛德会他。海伦娜被“利用”二字勾起母亲威洛的旧事——她当面指责母亲身边的那个男人看中的是魔药与力量，母亲却答愿为他违背所有誓言——随后脱口说“不愿因魔法被人利用”，辛西娅听成拒绝同行，退回主妇式的客气。窗外骤起风雨，海伦娜认出这是罗温姑妈发怒时出现过的天象，心里判断辛西娅和姑妈一样是地巫；她又想起封住辛西娅魔法的咒似乎正在松动、她即将满二十八岁。辛西娅被劝“保持冷静”后爆发，雷声震窗；哈姆雷特去蹭她，海伦娜心里冒出一句“我们都是由同一捧星尘捏成的”。最后她收回前言，答应与辛西娅同行。`
- 改后：
  `- **一句话概括**：晚宴一周后的周三下午，紧接上一章的吻，海伦娜在辛西娅的客厅里刚整理好衣鬓，管家希金斯太太便端着茶点托盘进来，又从围裙里掏出阿盖尔夫人索要的家具清单；她提起被辞退的年轻女仆莉莉，顺口说出莉莉父亲乔治·利珀特的名字，辛西娅当场追问确认，问出他家住齐普赛德，拿到了地址。利珀特正是辛克莱脑中闪过的那个名字，辛西娅提议当天就去齐普赛德会他。海伦娜自己玩笑式的一句“你是在利用我的魔法吗”勾起母亲威洛的旧事——她当面指责母亲身边的那个男人看中的是魔药与力量，母亲却答愿为他违背所有誓言——随后脱口说“不愿因魔法被人利用”，辛西娅听成要收回同行之约，退回主妇式的客气。窗外骤起风雨，海伦娜认出这是罗温姨妈发怒时出现过的天象，心里判断辛西娅和姨妈一样是地巫；她又想起封住辛西娅魔法的咒似乎正在松动、辛西娅即将满二十八岁。辛西娅被劝“保持冷静”后爆发，雷声震窗；哈姆雷特去蹭她，海伦娜脑中浮起一句“我们都是由同一捧星尘捏成的”，而她也说不准这念头是来自心里还是来自宇宙。最后她收回前言，答应与辛西娅同行。`

**md:11 · 情感弧线位置**（收 L3、L7、L13）

- 改前：
  `- **情感弧线位置**：这是紧接上一章那场吻之后的场景，情绪从吻后的失神与整理，转到探得地址的振奋，再被海伦娜的旧记忆拖回恐惧；一句“不愿被利用”把辛西娅推远，雷雨和“保持冷静”又把两人逼到爆发点，最后落在重新靠近、答应同行上。章末没有告白，只有一个“我们”。`
- 改后：
  `- **情感弧线位置**：这是紧接上一章那场吻之后的场景，情绪从吻后的失神与整理，转到探得地址的振奋，再被海伦娜的旧记忆拖回恐惧；一句“不愿被利用”把辛西娅推远，雷雨和“保持冷静”又把两人逼到爆发点，最后落在重新靠近、答应同行上。中途海伦娜的恐惧换过一次对象：从怕在辛西娅身上失去自己，变成怕整个失去辛西娅；而“想象别人来担这个角色”让她生出剧烈的嫉妒。章末没有告白，只有一个“我们”——原文最后一句仍是她的自我否认：她没工夫操心自己是不是爱上了一个女巫。`

**md:12 · Tropes 兑现/反转**（收 E3、E7、L4）

- 改前：
  `- **Tropes 兑现/反转**：吻后被管家撞见、旧日创伤、误会、怒火引来雷雨、狐狸当和事佬、“我们一起”的承诺都在。反转有两处：被劝“保持冷静”的人恰恰最不能听这句话；“利用”这个词把一句求援听成了拒绝。`
- 改后：
  `- **Tropes 兑现/反转**：吻后被敲门打断、旧日创伤、误会、怒火引来雷雨、狐狸当和事佬、“我们一起”的承诺都在。反转有两处：被劝“保持冷静”的人恰恰最不能听这句话；“利用”这个词把海伦娜先前给的同行之约，听成了要收回。辛西娅那段怒火也不只是家事——她把“贵族女子该当一朵温柔明亮的花，只负责添色添香、不许有主张、不许有目标”整段掀了出来，正接上一章海伦娜那句“这个‘我们’是不是只指男人”。`

**md:13 · 人物弧线**（收 **阻断 3 / L1**、L2、L10、L12）

- 改前：
  `- **人物弧线**：海伦娜从吻后的失序，到用“不愿被利用”把辛西娅推开，再到承认自己犯傻、答应同行；她始终用“朋友”和“帮忙”给感情包一层壳，身体的反应却先一步泄露。辛西娅从主妇式的周到，到被“利用”刺伤后退回体面，再到把“被人替她做主”的怒火整段说出来；她的强硬和脆弱在同一章里交替。希金斯太太的闪烁其词则把莉莉这条线悄悄往前推。`
- 改后：
  `- **人物弧线**：海伦娜从吻后的失序，到用“不愿被利用”把辛西娅推开，再到先开口道歉、承认自己犯傻、答应同行；她始终用“朋友”和“帮忙”给感情包一层壳，身体的反应却先一步泄露。这层壳有来历：母亲薇洛为一个男人违背了“我们不伤人”的家训，海伦娜于是给自己立下私誓——绝不爱上任何人，绝不把心与选择的主导权交出去；她这一章的每一次推开，都是在跟这条私誓拉扯，也正应了那句“她努力不像母亲，却仍旧活成了母亲”。辛西娅从主妇式的周到，到被“利用”刺伤后退回体面——体面里还包着一句“我也知道被利用是什么滋味，我不会那样对你，你没有义务陪我去”——再到把“被人替她做主”的怒火整段说出来；她的强硬和脆弱在同一章里交替。希金斯太太的闪烁其词则把莉莉这条线悄悄往前推。`

**md:14 · 叙事手法**（收 E1×1、E8、E13、E14、L5、L8、L9）

- 改前：
  `- **叙事手法**：全章贴海伦娜的限知，没有视角切换；管家那段靠读心补足话外音，母亲的旧事以无提示的闪回插入，雷雨跟着辛西娅的情绪走。被劝“保持冷静”那句，她一字一顿地吼回来——“Do. Not. Tell. Me. To. Remain. Calm!”——句点像锤子，雷声接在最后一下。章末让哈姆雷特去蹭辛西娅，再用一句“We are creatures shaped from the same stardust.”的心声把两人的相似说破，最后收在“一起”上。`
- 改后：
  `- **叙事手法**：全章贴海伦娜的限知，没有视角切换；管家那段靠读心补足话外音，母亲的旧事接在一句“一段旧记忆涌了上来”之后直接切入，闪回本身不加任何排版标记，雷雨跟着辛西娅的情绪走。被劝“保持冷静”那句，她一字一顿地吼回来——“Do. Not. Tell. Me. To. Remain. Calm!”——句点像锤子，雷声接在最后一下；海伦娜改口说“你想怎么感觉就怎么感觉”，反而更糟，只换来一个反问：“我们？”临近结尾让哈姆雷特去蹭辛西娅，再用一句“We are creatures shaped from the same stardust.”把两人的相似说破（原文紧接着自陈：她说不准这念头来自自己的心还是来自宇宙），最后落在“那我们就一起做”上——辛西娅答应的那一刻，太阳也试探着从暴云里露出来，风暴随之放晴。`

**md:40 · 原句 3 中文理解**（E9）

- 改前：`**中文理解**：管家脸上的纹路松开，堆出和善；她说莉莉的父亲在齐普赛德有房子，莉莉跟家里人住着，想必很快活，工作的事不必夫人操心。`
- 改后：`**中文理解**：管家脸上皱出一道道和善的纹路；她说莉莉的父亲在齐普赛德有房子，莉莉跟家里人住着，想必很快活，工作的事不必夫人操心。`

**md:54 · 原句 4 为什么这样写**（**阻断 2**）— 见 §二 阻断 2。

**md:58 · 原句 5 引语**（E10，**首选**：扩引语到句首，不增块）

- 改前：`> **原句 5:** "‘Used? I would never, that is, I thought you wanted to help me. You asked to come with me if I was going to continue the investigations, and I thought…’ She closed her eyes tight, shaking her head. ‘Oh. You weren’t serious. Of course.’ She blinked open her hazel eyes, her lips curling into a smile that contradicted the pain there."`
- 改后：`> **原句 5:** "Cynthia’s hazel eyes widened as her lips parted on an inhalation. ‘Used? I would never, that is, I thought you wanted to help me. You asked to come with me if I was going to continue the investigations, and I thought…’ She closed her eyes tight, shaking her head. ‘Oh. You weren’t serious. Of course.’ She blinked open her hazel eyes, her lips curling into a smile that contradicted the pain there."`
- **备选（不动引语）**：md:60 改前 `**中文理解**：辛西娅听到“利用”两个字，眼睛睁大，急忙说自己绝不会那样；…` → 改后 `**中文理解**：辛西娅听到“利用”两个字，急忙说自己绝不会那样；…`
- 改完必须重跑 `python3 scripts/verify_fragments_indep.py "<书目录>"`（期望 MISS 仍为 0）。

**md:74 · 原句 6 为什么这样写**（E1＋E11）

- 改前：`**为什么这样写**：先写天色的骤变，再写海伦娜的“见过”，最后用“一模一样”把两件事扣在一起。她没有说破是谁在呼风唤雨，只让读者跟着她想起罗温姑妈；天气因此不再只是背景，而成了怒气的外在显形。`
- 改后：`**为什么这样写**：先写天色的骤变，再写海伦娜的“见过”，最后用“一模一样”把两件事扣在一起。她在这句里没有说破是谁在呼风唤雨，只让读者跟着她想起罗温姨妈——下一行的心声才把答案交出来；天气因此不再只是背景，而成了怒气的外在显形。`

**md:96 · 原句 8 读者视角提示**（E12）

- 改前：`**读者视角提示**：读者看得出哈姆雷特先替海伦娜走近了辛西娅；海伦娜的“挪了位”没有经过推理，是她用身体承认的事。`
- 改后：`**读者视角提示**：读者看得出是哈姆雷特先走到辛西娅身边，替海伦娜完成了她没敢做的那个动作；海伦娜的“挪了位”没有经过推理，是她用身体承认的事。`

**md:106 · 原句 9 读者视角提示**（L6＋L8 的一部分）

- 改前：`**读者视角提示**：读者等了一整章的“同行”在这里落定；她避开了“爱”这个字，却把“不让你一个人”说得很实。承诺已经给出，接下来要看她们怎样一起出门。`
- 改后：`**读者视角提示**：读者等了一整章的“同行”在这里落定——而就在上一行，她还完全可以退开。她避开了“爱”这个字，却把“不让你一个人”说得很实；后面还要再问一句“你愿意让我帮你吗”，那一句问的已经不只是这桩案子。承诺已经给出，接下来要看她们怎样一起出门。`

**md:132 / md:140 · 词表两条例句**（E16，可选）

- 改前：`| prospects | 前途，前景 | No need to worry yourself about job prospects for Lily.’ |`
- 改后：`| prospects | 前途，前景 | No need to worry yourself about job prospects for Lily. |`
- 改前：`| address | 地址 | You don’t happen to have their address?’ |`
- 改后：`| address | 地址 | You don’t happen to have their address? |`
- ⚠️ 改完须重跑 `/tmp/vocab_check_hx.py 16`——**这两条例句去掉闭引号后仍是原句逐字子串**（原文 `:92`/`:95` 的 `’` 属引号而非词内字符），不会造成 `missing`。

**md:119 · `vulnerable` 档位**（E15，可选）：整行从 `### ⭐⭐⭐ 高级` 表移到 `### ⭐⭐ 进阶` 表末尾；移后 ⭐⭐⭐＝7 条、⭐⭐＝9 条，总数仍 22。**不改也不判红**（`check_vocab.py` 不查档位合理性）。

## 五 R5.5 · 已核实为正确（41 条，后续任何人不得以「读着不对」为由改动，除非能给出反证）

1. md:10「晚宴一周后的周三下午」——`ch15:153` `It had been a week since the dinner party`；`ch15:162` `on a sunny Wednesday afternoon`。
2. md:10「紧接上一章的吻」——`:35` `she stared at Cynthia from across the couch cushions`；`:38` `Cynthia’s mouth was bruised from her kisses`。
3. md:10「阿盖尔夫人索要的家具清单」——`:56` `the list of furnishings Lady Argyle requested`（**清单本身没错**，错的只是「捧着…进来」，见 E4）。
4. md:10「被辞退的年轻女仆莉莉」——`:62` `she got the chop`＝**被解雇**，md 未误读成「被杀」。
5. md:10「利珀特正是辛克莱脑中闪过的那个名字」——`:110` `then he clearly thought George Lippert’s name`（**是 thought，不是说出口**，md 写「脑中闪过」正确）。
6. md:10「母亲却答愿为他违背所有誓言」——`:143` `I will break every oath I’ve made for him.`
7. md:10「心里判断辛西娅和姑妈一样是地巫」——`:212` `She’s an earthwitch, just like Aunt Rowan.`（**判断内容正确**，只有称谓错，见阻断 1）。
8. md:10「她即将满二十八岁」——`:221` `Cynthia was approaching her twenty-eighth year.`（**未误挂到海伦娜**）。
9. md:11「章末没有告白」——`:290` `She didn’t have time to worry about falling in love with a witch`＝否认，不是告白。
10. md:12「怒火引来雷雨」——`:233` `Thunder shook the windowpanes.` 紧跟吼声。
11. md:12「狐狸当和事佬」——`:251` 蹭腿 → `:260` 辛西娅重新问 `‘Are you saying you’ll come with me?’`。
12. md:12「被劝'保持冷静'的人恰恰最不能听这句话」——`:230` `Helena, like a complete simpleton, had gone a step further by saying the one thing no woman wanted to hear when they were courting fury.`
13. md:14「全章贴海伦娜的限知，没有视角切换」——`:71`／`:86` 的他人念头是**读心所得**（`:65` `Helena gleaned from Mrs Higgins’ thoughts`），不是 POV 切换；md 未把两者混为一谈。
14. md:14「管家那段靠读心补足话外音」——`:65`／`:71`／`:74`／`:86`。
15. md:14「句点像锤子，雷声接在最后一下」——`:233` `‘Do. Not. Tell. Me. To. Remain. Calm!’ Thunder shook the windowpanes.`（六个句点实测）。
16. md:20「姑妈把那种感觉说成从一场古怪的催眠里醒来」——`:35` `When the spell was finally broken, **she** described it as…`，`she`＝**Aunt Rowan**。**本章最高危的施事陷阱（T1）md 未踩**：被下咒的是 Rowan，海伦娜从未被下咒（`Helena had never been hexed before`）。
17. md:30「她打小就认识'乔治'」——`:83` `I’ve known Georgie since we were little mites in leading strings.`
18. md:30「当初把莉莉送进这户人家做事的人，正是她自己」——`:83` `It was my doing that got Lily here in the first place.`
19. md:34「她不是在闲聊，是在替自己的决定记账」——`:86` `A decision I’ll always regret. How can Georgie ever forgive me?`（**分析层读到了引语之外的心声，且读对了**）。
20. md:44「'想必'把话说成了猜测」——`:92` `I’m sure she is quite happy there`，原文无任何实证。
21. md:50「记忆里的海伦娜对母亲说」——`:131`–`:137` 闪回，说话人＝海伦娜、受话人＝薇洛。**T11 陷阱未踩**：闪回里打人的是薇洛（`:140` `The sting of Willow’s slap shocked Helena. Her mother had never hit her before.`），md 未把这一巴掌安到海伦娜头上。
22. md:56「'我们不伤人'既是家训，也是她拿来衡量母亲、也衡量自己的尺子」——`:176` `They swore to do no harm and lived by that promise.`＋`Helena made another oath`。
23. md:60「她以为海伦娜是想帮她，才提出同行」——`:158` `You asked to come with me`：**同行之约是海伦娜先提的，方向未调转**。
24. md:70「把绣球花抽得乱颤」——`:209` `thrashing the hydrangea blooms most violently`。
25. md:70「罗温姑妈气到极点时，她与土地的那点牵连」——`:209` `how **her** connection to the earth would manifest`，`her`＝**Rowan**（md 未误挂到辛西娅）。
26. md:80「女巫的力量七岁显现，此后每七年更强一分」——`:221` `A witch’s power manifested at seven, then grew more potent every seven years.`
27. md:84「'似乎'和'怕'都留在猜测范围内——她知道的是迹象，不是结论」——`:221` `seemed to be slipping` / `Helena worried`。**hedge 未被升级成定论。**
28. md:86「叙述只说到'似乎'，没有人证实封印已经破了」——同上。**这是全章写得最好的一条读者提示**，与 ch25 才揭开的真相保持了正确距离。
29. md:90「哈姆雷特从沙发上轻巧跳下，绕到辛西娅脚边，用头蹭她的腿」——`:251`。**T21 陷阱未踩**：哈姆雷特是**狐狸**、雄性、**海伦娜的**魔宠，md 未写成猫／她的。
30. md:90「这个动作海伦娜对自己的使魔做过千百次」——`:251` `a gesture Helena had made a million times with her familiar`（归属正确）。
31. md:90「看辛西娅向哈姆雷特讨安慰，她心口有什么东西挪了位」——`:251` `watching Cynthia seeking comfort from Hamlet … shifted something at her centre`（**安慰方向正确**：辛西娅向狐狸讨安慰，海伦娜是旁观者）。
32. md:100「海伦娜给出答案：对，我们」——`:260` 辛西娅问 `‘Are you saying you’ll come with me?’` → `:269` 海伦娜答。**T23 陷阱未踩**：md 没把答复安到辛西娅头上。
33. md:104「开头两个词就是答复」——`‘Yes, we.’` 实测 2 词。
34. md:104「再把理由说成三件事：帮你、找出凶手、不让你一个人」——`:269` 实测 3 件（`I want to help you` / `I want to find the bastard…` / `I don’t want you to do this alone`）。
35. md:104「最后一句落在'一个人'上，和开头的'我们'合成一个闭环」——`:269` 语序实测成立。
36. md:106「接下来要看她们怎样一起出门」——ch17 标题即 `The Dog in Cheapside`，正是这趟出门。
37. `原句 6` 的 `…` 三片段**全部落在 `:209` 同一行内**，两侧均为原词 ⇒ 不是 Darling Girls 式跨段拼接造假（`verify_fragments_indep.py` MISS 0 佐证）。
38. 词表 **22 条例句全部是 ch16 原句**（`/tmp/vocab_check_hx.py 16` → `rows=22 missing=0`），**22 条词头全部在本章原文出现**（`/tmp/vocab_head_hx.py 16` → `rc=0` 无输出）。逐条抽核：`dishevelled:38`／`belligerent:74`／`visceral:275`／`endeavoured:161`／`prestigious:176`／`vulnerable:197`／`precipice:278`／`waterwitch:125`／`hypnosis:35`／`chignon:41`／`parchment:53`／`fleeting:65`／`sentiment:74`／`prospects:92`／`glassy:98`／`coven:182`／`address:95`／`killer:107`／`brow:44`／`apron:53`／`brother:200`／`mother:83`。
39. 词表 `brother` 行例句保留原文 `Your brother would have a fit, and Uncle Lachlan will string me up by my toes…`（`:200`）——**`Your brother` 指辛西娅之兄 Thomas，不得「修正」**。
40. 词表 `mother` 行例句 `His mother, God rest her, was a dear friend to my own mother.`（`:83`）——`His` 指**乔治·利珀特**，不是笔误。
41. 语料层：ch16 **零推广行**（Lokepub 三行推广只出现在 ch03:188／ch08:170,173／ch13:182,185／ch19:194,197／ch25:214 共 5 章 8 行）；本章也无 `I’m in love with a ferret.`（那是 `ch15:192` 的狐狸心声，反面陷阱）。

## 六 覆盖声明

- **本章做到哪一步**：R1 素读（子代理产出 → 主会话逐条复核 traps，**推翻 T17**）→ R2 机器层（`chapter.sh --json` rc=0）→ R3 三张单子（漏 13／编 0／错 14）→ R4 逐块对应 9/9（含固定三问）→ R5 判定表 ＋ R5.5 ＋ R5-补 零命中取证。**R1–R5 全量，无跳过项。**
- **未做的**：本章无「跨章引语归属」抽查（ch16 的 9 条引语全部落在 `text/ch16`，`verify_fragments_indep.py` 报「缺参照章 0」）。
- **本章特有盲区（下一轮复核请重点看）**：
  1. **块数 9 已触 `block_target [5,9]` 上限** ⇒ 任何补漏都不得增第 10 块；只能改导航或在现有块内扩引语。若执行方增块，`chapter.sh` **仍会 rc=0**（`block_hint` 是提示型），只有本判定表能拦。
  2. `:254` 星尘念头、`:80` 问句说话人、`:284` 答句说话人**三处原文无 tag 或自陈不明** ⇒ 任何把它们写实的改动都应判红。
  3. `:71`／`:86` 是**希金斯太太的心声被读心读到**，不是海伦娜的 ⇒ 若后续修复把这两句归给海伦娜，判阻断。
  4. **海伦娜读不到辛西娅的心**（`:179`）⇒ 任何写「她听见辛西娅心里…」的表述判阻断。
  5. 闪回 `:131`–`:149` 的施事方向（薇洛打海伦娜）是全章最易调转处，md 目前正确。
  6. `:59` `the wages you’ll earn by staying here` 是**辛西娅出不起更高价**，不是希金斯太太求去（T28）；md 未涉及，但词表／导航若补写须注意。
  7. 中文分析层的**事实断言无任何门禁覆盖**（本项目既有记忆）——本章 26 条提示全部落在这一层。
  8. 子代理底稿的 **T17 已被证伪**（详见 `3-diff.md` §四末）⇒ 复核 ch17–ch27 时，凡引用底稿 traps 的判定都要回原文重核。

## 七 结论

**本章不通过。** 阻断 3 条（E1 称谓 8 处／E2 节奏断言／L1 私誓漏），提示 26 条，编 0，假红 0。
修复后须重跑：`bash scripts/chapter.sh "…/ch16 lilys father.md"`（期望 rc=0，块数仍 9）＋ `python3 scripts/verify_fragments_indep.py "<书目录>"`（期望 MISS 0）＋ `python3 scripts/corruption_scan.py`。
**本会话只出指令，不改稿。**
