# ch13 判定表（R5）

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch13 matt and amy hunt for the real isolde.md`
- 唯一权威源：`text/ch13_13.txt`（11292 字符 / 280 行）
- 机器层：`bash scripts/chapter.sh "…/ch13 matt and amy hunt for the real isolde" --json` → 退出码 **0**，verdict `ok`，issues 全空；输出存 `2-machine.json`
- 语料前置：`python3 scripts/verify_corpus.py "…/a-fatal-legacy-by-charlotte-vassell"` → 退出码 **0**，`=== P0-0 语料验收: PASS（FAIL 0 / WARN 3）===`（3 条 WARN 均为全书级：未给 --expect / ch23 页码 bleed 提示 / 未给 --anchors，与本章无关）
- 审查覆盖声明：**仅第 13 章**（R1–R5 全跑）；其它 53 章与总览三篇**只有机器层**，未做人判，不写「通过」。

---

## 一、四组数

| 组 | 计数 | 说明 |
|---|---|---|
| **逐字** | **35 / 35 命中，0 miss** | ① 引语 8/8：程序核对每块为源文**单段连续串**（`q in src` 全 True；位置 515、923、2206、2810、3500、8358、10326、10890），**无 `…` 缝合、无跨话轮拼接、无空引语**；② 词汇表例句 **27/27** 逐字来自本章（`ex in src` 全 True），词头词形与原文一致；③ 24 个关键词（8×3）**全部命中本块引语** |
| **对应** | **8 / 8 块成立** | 每块「这段中文是不是在讲这句引语」＝是；**无**「讲引语之外的上下文」、**无**「滑向全书主旨/作者生平」、**无**「只复述字面、密度不足」三类；**无「引语选短」**。R4 固定三问（施事/受事/归属）失手 **2 块**（原句 5、原句 8）→ 其错误计入断言组，不重复计对应 |
| **形态** | **0 偏离** | H1＝`13. The Police Station`（本书众数 `N.` 写法，54/54 ✓；源文小标题 `The Police Station`，`:17` ✓）；导航 **5 项**：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法（＝本书众数 5 项，缺项 0 ✓）；子项集 **4 项**：中文理解 / 关键词 / 为什么这样写 / 读者视角提示（＝本书众数/profile 子项 ✓）；块数 **8**（本书每章块数中位 7.0、范围 5–10；profile mystery-thriller 允许 3–10 ⇒ **在区间内，无偏离**） |
| **断言** | **核对 22 条，12 条不合（阻断 4、提示 8），10 条成立** | 明细见 §二（12 行）与 §三（10 行） |

> 机器层的 `cjk_ratio` 全块 ≥0.71（中文理解 0.71–0.84）、`cjk_low` 0、`keyword_bad` 0、`struct_bad` 0、`empty_quote` 0 —— 中文层无夹杂、无过薄。

---

## 二、判定表（有问题的断言，12 条）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md:72「负责去敲每扇门的是三人组里那个刚输了比赛、**还在吃三明治的 Matt**」 | `text/ch13_13.txt:20`（区间 41-148）『Matt asked, **peering into Caius’s stainless-steel lunch box**』；`:95`（区间 2206-2452）『**Caius said, picking up his sandwich.**』；原句 8 位置区间 10890-11112，对应 `:268` | 三明治是 **Caius 的**；Matt 只是探头去看，且到本章末尾（`:274-280`「Pub?」/「Monday Funday」）午饭早已结束 ⇒ **施事/属性错配（编）** | **阻断** |
| 2 | md:24「留意这个「谁最怪」的比赛**从头到尾没有结算结果**」 | `text/ch13_13.txt:80`（区间 1747-1846）『My ruling stands. **Caius 11, Matt 7.**』；`:86`（区间 1892-2038）『**You’ve lost this month’s “how weird is Caius’s lunch” contest** and will have to buy us all bánh mì on Friday.’ | 比赛**有**明确裁决与比分，Matt 当场输掉并被罚请客 ⇒ 与原文直接矛盾；且赛制是「Caius 的午饭有多怪」，不是「谁最怪」 | **阻断** |
| 3 | md:23「**这句玩笑落在案情刚被改写成「他杀」之后**」 | 比赛规则叙述在 `text/ch13_13.txt:44`（区间 515-921）；「It was murder.」在 `:95`（区间 2206-2452）⇒ 玩笑在**前**、「他杀」改写在后；md 自身 md:37 写「偏偏这句结论被放在一只三明治旁边说出来」，两处自相矛盾 | 时序倒置（若本意是「读者自前章已知此案为他杀」，「刚」与「落在……之后」仍与 md:37 冲突，需改写措辞） | **阻断** |
| 4 | md:51「『他受够了』……**也是他可能会对警察说、却没说的那句心里话**」 | `text/ch13_13.txt:132`（区间 3500-3875）『Caius remembered how immaculate his own home had been though. **‘He was neglecting it. He’d had enough. Those two partial fingerprints could’ve stuck around for quite a while.’**』 | 「He'd had enough.」是**已说出口的台词**（引号内，当着 Amy 说）；md:49 的中文理解已分对，分析层又说反 | **阻断** |
| 5 | md:52「**作者把最关键那层猜测留给了叙述，而不是台词**」 | `text/ch13_13.txt:132`（同上）：叙述句只有 "Caius remembered how immaculate his own home had been though." 一句，其前后皆为台词；最关键的猜测（旧指纹/他受够了）在**台词**里 | 哪一层算「最关键」可争议，但「留给叙述、而不是台词」与原文结构不合（与 #4 配套） | 提示 |
| 6 | md:11 / md:121「**周一上午**的警局被一顿三明治比赛和**一场毒芹排查同时占满**」 | 饭盒场景 `:20`（区间 41-148）；`:268`（区间 10890-11112）『One for us tomorrow, Matt, while Amy is off.’（本章只**派**任务）；章末 `:274-280`「Pub?」 | 「上午」无原文依据（本章在中午与傍晚各有落点）；「毒芹排查占满警局」把次日任务写成本章正在进行的事；「摊成一张名单」的名单实物在 ch16 | 提示 |
| 7 | md:21「Matt 和 Amy **轮流当对方不在时的裁判**」 | `text/ch13_13.txt:44`（区间 515-921）『Matt and Amy switched out every other month with the other adjudicating.』 | 原文只说每隔一个月换人裁定，无「对方不在」一层；但该英文句本身有歧义（switched out 亦可读作「一方轮空」）⇒ 不判阻断 | 提示 |
| 8 | md:14「也清楚自己其实**羡慕**迪吉能靠卖掉这栋楼干净脱身」 | `text/ch13_13.txt:235`（区间 8358-8927）『…had a handsome payout for ridding himself of the guilt **rankled him**.』 | rankled＝被刺痛/耿耿于怀，非「羡慕」；md 原句 6 的中文理解「他心里并不痛快」是对的 | 提示 |
| 9 | md:12「中途穿插 **Matt 从迪吉公寓打来的电话汇报**」 | `text/ch13_13.txt:144`（区间 4273-4448）『**Caius called Matt, placing him on speakerphone.**』 | 电话是 Caius **打到**迪吉公寓（Matt 在那头回话）；Matt 主动拨出的那次（给 Nathan）在 `:181`（区间 5229-5368），此时他已在警局 ⇒ 方向写反 | 提示 |
| 10 | 漏：Horatio Combe 手写日记原件在架、正是 Willow 在誊录/Digby 拿它当素材 | `text/ch13_13.txt:141`（区间 4173-4271）『There was a set of his handwritten journals…』；`:144`（同上）『Those are what Willow was typing up. Digby was using them as research for his book.’ | md 未把「日记在架」写反，但该层完全缺席（取证：`/usr/bin/grep -n -E "日记\|journal" "ch13 ….md"` → exit=1）；它是第 33 章「失踪的日记卷」的伏笔 ⇒ 建议补入导航「线索结构」 | 提示 |
| 11 | 漏：Horatio 的玄学设定（降神会 / 吸木乃伊粉 / 被祖父归因于疟疾 / Digby 觉得 sinister） | `text/ch13_13.txt:232`（区间 7605-8356）『…Horatio had gone proper off the deep end and got into seances… sniffing powdered Egyptian mummy… a bad case of malaria the year before he died but Digby thought it was sinister.’ | 该线只以**词汇表 `sinister` 一条的例句**出现（md:97），导航与八块分析层均无（取证：`/usr/bin/grep -n -E "降神会\|木乃伊\|疟疾\|seance\|malaria" "ch13 ….md"` → 命中 1（md:97），exit=0）⇒ 全书后段反复回收的暗线未进入分析层 | 提示 |
| 12 | 漏：Nathan 电话这一场（约占全章 40%）在引语层零覆盖 | `text/ch13_13.txt:181-241`（区间 5229-9101） | 该场的决定性内容（从未见面＝纸面人物、卖研究所搬 York）**已被导航与原句 6/8 覆盖**，未出现「把她的版本写成事实」的错配；仅引语层未取材 ⇒ 不判阻断 | 提示 |

---

## 三、已核实为正确（R5.5 防误修固定节）

> 以下条目**看起来像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非给出反证。

| # | 写法 | 原文逐字（`text/ch13_13.txt`） | 状态 |
|---|---|---|---|
| 1 | md:33/md:35 食品标准局邮件：毒芹与「是谋杀」的结论 | `:95`（区间 2206-2452）『Just had an email from the Food Standards Agency. They’ve investigated the farm where Digby’s bagged salad originated and there was no trace of hemlock in their polytunnels whatsoever. **It was murder.**』 | 逐字一致 ✓（本章专属判据②） |
| 2 | md 未出现「十人名单（一人在养老院、七人在上小学、最后只剩两个）」 | 该构成**不在本章原文**：`/usr/bin/grep -n -E "nursing home\|primary school\|ten Isoldes\|Isoldes in the entire" text/ch13_13.txt` → **exit=1（零命中）**；md 侧 `/usr/bin/grep -n -E "十人\|养老院\|上小学\|小学\|nursing\|primary school\|十个" "ch13 ….md"` → **exit=1（零命中）**。真正出处是 `text/ch16_16.txt:32`『there are only ten Isoldes in the entire UK. One is in a nursing home in Surrey. Seven are in primary school within either Chelsea, Fulham, Putney or Chiswick… **That leaves one each for me and you.**』 | 无编造 ✓（本章专属判据①；若日后有人把「十人」写进 ch13，即为跨章搬运） |
| 3 | md:15「章末一句「Monday Funday」把这一章扣回分部 A MONDAY IN MAY 的周一」 | `:280`（区间 11264-11292）『**‘Monday Funday,’ said Matt.**』；分部名是**全书结构标签**（同分部章 md 同样写法：ch49:15 / ch50:15 / ch51:11「分部 A MONDAY IN MAY」） | 成立 ✓（本章专属判据③；源文本身无「MONDAY IN MAY」串，不构成错引） |
| 4 | md:63「假 Isolde」的方向：她早盯上这个地方、算准穿着实习生打扮进门不惹怀疑 | `:262`（区间 10326-10861）『“Fake Isolde” wore a “Willow costume” because **she’d been watching the place** and calculated that **she wouldn’t look suspicious** entering the building dressed as the intern.’』 | 施事/归属全对 ✓ |
| 5 | md:14/md:63「罪责不能继承、责任却要继承」 | `:262`（同上）『**You can’t inherit blame, but you do inherit responsibility.**』 | 逐字 ✓ |
| 6 | md:13 线索结构四项 | `:95`（FSA 结论）、`:114`（区间 2810-3108，两枚残缺指纹与位置）、`:247`（区间 9187-9320，『Willow’s notes and the draft of his “Apologia” are missing.』）、`:220`（区间 7034-7258，『She’d described herself as dark-haired… a nondescript description.』） | 四项均可回原文 ✓ |
| 7 | md:42 指纹位置归属：「一枚在图书馆门上，另一枚在那扇已经被漆盖住的地下室门上」 | `:114`（区间 2810-3108）『One on the library door and one on the door to the basement that has been painted over.’ | 位置与归属方向全对 ✓ |
| 8 | md 词汇表 27 条（高级 8 / 进阶 10 / 基础 9） | 程序核对 `ex in src` → **27/27 True**；词头 27/27 命中（`leftovers` 首字母大小写差异系句首，非词形错） | S4 通过 ✓ |
| 9 | md 各块关键词 24 项 | 逐块 `关键词 in 本块引语` → **24/24 True** | 通过 ✓ |
| 10 | md:12「主要贴着顾问警员 Caius」 | 「顾问警员」是全书既定称法（ch05:13、ch09:12 同用）；本章确以 Caius 为主视角（`:235` 内心段、`:262` 推断段），Matt 仅在 `:105`/`:181` 两处以行动/电话出现 | 成立 ✓（仅「打来的电话」方向一句记提示，见 #9） |

---

## 四、跳过（没查的，不写成「通过」）

| 项 | 状态 | 原因 |
|---|---|---|
| 其它 53 章的 R1–R5 | 未查 | 本次职责仅为第 13 章 |
| 总览三篇（`00_概述.md` / `00_情感节点.md` / `00_金句精选.md`） | 未查 | 同上；本章 md 与总览的一致性未核对 |
| 全书级 `check_vocab.py` 门禁 | 未跑 | 已用自建脚本对本章 27 条例句做等效逐字核对（27/27），但未跑该门禁脚本本身 |
| 全书 `corruption_scan.py` | 未跑（脚本只接目录，传文件路径会报「该目录下无 md 文件」） | 已手工核对本章 md：U+FFFD 0、`..` 0、`。。` 0；8 块引语无重复前缀、无复制截断 |
| `check_summary_names.py` 摘要层人名探针 | 跑了（退出码 0） | ch13 **无命中**；两条 ⚠️ 属 ch37，超出本次范围 |
| 跨章搬句系统比对（本章 8 块引语是否被别章 md 重复使用） | 未查 | 超范围；但已确认本章 8 块全部落在 `ch13_13.txt` 内且逐字 |
| `verify_fragments_indep.py`（省略号分段独立取证） | 未跑 | 本章 8 块均**无省略号**、均为单段连续串（`q in src` 全 True），该探针无适用对象 |

---

## 五、结论

- **逐字 35/35 ｜ 对应 8/8 ｜ 形态 0 偏离 ｜ 断言 22 条核对 / 12 条不合（阻断 4、提示 8）**
- **阻断型 4 条**，全部集中在**分析层（中文）与原文的不符**，引语层本身零缺陷：
  1. #1「还在吃三明治的 Matt」（施事/属性错配）
  2. #2「比赛从头到尾没有结算结果」（与 `:80`/`:86` 直接矛盾）
  3. #3「笑话落在改写成他杀之后」（时序倒置，与 md 自身 md:37 冲突）
  4. #4「『他受够了』……却没说的心里话」（台词被当内心话）
- 最要紧的一条：**#2**——它把本章最显眼的数字（Caius 11、Matt 7）与裁决写成了「没有结算结果」，且把赛制「Caius 的午饭有多怪」改写为「谁最怪」；读者若据此读，得到的结论与原文相反（原文里 Matt 当场认输、罚请 bánh mì），而这正是本章「用玩笑盖住不安」结构的收口处。
