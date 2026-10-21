# ch13 三张单子（漏 / 编 / 错）

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch13 matt and amy hunt for the real isolde.md`
- 唯一权威源：`text/ch13_13.txt`（11292 字符 / 280 行）；引用逐字抄，字符区间为 0-based `[start,end)`。
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch13/`

---

## 一、单子「漏」（素读有、md 无）

### L1 ｜图书馆里那套 Horatio Combe 手写日记原件（提示）
- 原文 `text/ch13_13.txt:141`：
  > ‘There was a set of his handwritten journals. I looked in one of them but it was barely legible.’
- 原文 `text/ch13_13.txt:144`：
  > ‘Those are what Willow was typing up. Digby was using them as research for his book.’
- md 现状：导航「线索结构」只写了「不见了了 Willow 研究笔记与「Apologia」草稿」；「Horatio 的日记原稿在架、正是 Willow 在誊录、Digby 拿它当写书素材」这一层没有进分析层。
- 取证：
  ```
  /usr/bin/grep -n -E "日记|journal" "…/ch13 matt and amy hunt for the real isolde.md"
  → exit=1（零命中）
  ```
- 判定：md 未声称「日记不见了」，没有把「日记在架」写反，属**信息未覆盖**而非错误；「笔记失踪＝杀人动机」这条主线已被导航写对。建议在「线索结构」补一句（并注意这是第 33 章「失踪的日记卷」的伏笔）。**档位：提示。**

### L2 ｜Horatio 的玄学/疟疾设定（提示）
- 原文 `text/ch13_13.txt:232`（Nathan 转述 Digby）：
  > ‘He was telling me about this one journal where Horatio had gone proper off the deep end and got into seances. Lots of creepy occult stuff. He said he thought he was sniffing powdered Egyptian mummy and all sorts. He said his granddad dismissed it as old Horatio having a bad case of malaria the year before he died but Digby thought it was sinister.’
- md 现状：这段**只以词汇表 `sinister` 一条的例句出现**（md:97），导航与八块分析里都没有「降神会／木乃伊粉／疟疾」这条线。
- 取证：
  ```
  /usr/bin/grep -n -E "降神会|木乃伊|疟疾|seance|malaria" "…/ch13 ….md"
  → 命中 1（md:97，词汇表例句）；exit=0
  ```
- 判定：这是全书后段（第 33 章缺失的日记卷、第 43 章论坛故事）反复回收的暗线；本章只给了口述转述，属**背景级信息未进入分析层**。**档位：提示。**

### L3 ｜Nathan 电话这一场（约占全章 40%）在引语层零覆盖（提示）
- 原文 `text/ch13_13.txt:181-241` 整场（Nathan 提供：Fenella 让他回电、Digby 两个周末前来看过他、Digby 从未与 Isolde 见面、她只自述「dark-haired」、Digby 打算卖研究所搬回 York 写家族回忆录、Horatio 玄学、去年 Digby 改变心意）。
- md 现状：八块引语无一取自这一场；只在导航「线索结构」留下「一个只写着「深色头发」、连长相都没说清楚的纸面人物 Isolde」，在原句 6/7/8 里间接触及（卖楼脱身、Apologia、「假 Isolde」）。
- 判定：场景的决定性内容（从未见面＝纸面人物、卖研究所搬 York）**已被导航与原句 6/8 覆盖**，未出现「把她的版本写成事实」的错配。**档位：提示**（非阻断：md 未写错，只是没给这一场引语位）。

---

## 二、单子「编」（md 有、原文无 / 原文相反）

### J1 ｜「还在吃三明治的 Matt」——施事归属反转（阻断）
- md:72（**原句 8 · 为什么这样写**）：
  > 「而负责去敲每扇门的是三人组里那个刚输了比赛、还在吃三明治的 Matt。」
- 原文 `text/ch13_13.txt:20`：
  > ‘What have you got today then?’ Matt asked, **peering into Caius’s stainless-steel lunch box** with suspicion.
- 原文 `text/ch13_13.txt:95`：
  > ‘Nope,’ **Caius said, picking up his sandwich.**
- 原文 `text/ch13_13.txt:274-280`（原句 8 所在位置是本章末尾）：
  > ‘Pub?’ ／ ‘Monday Funday,’ said Matt.
- 问题：三明治是 **Caius 的**（Matt 全程只是探头去看他的饭盒，Amy 端的是自己的 leftover pasta salad，输的人还要请大家吃 bánh mì）；而且到原句 8 时午饭早已结束（本章结尾才去酒吧）。md 把「吃三明治」安到 Matt 头上＝S3 第 ⑥ 类**施事/归属反转**（机器四道探针全绿，只有 R4 三问能抓）。
- 判定：**阻断。**

### J2 ｜「这个『谁最怪』的比赛从头到尾没有结算结果」——与原文直接矛盾（阻断）
- md:24（**原句 1 · 读者视角提示**）：
  > 「留意这个「谁最怪」的比赛从头到尾没有结算结果，它的作用是把不安盖住；也留意 Matt 为什么这一天格外在意。」
- 原文 `text/ch13_13.txt:80`：
  > ‘I feel like I could buy that as a packet mix in a big Tesco. My ruling stands. **Caius 11, Matt 7.**’
- 原文 `text/ch13_13.txt:86`：
  > ‘Sorry, Matt, I’m going to call it. **You’ve lost this month’s “how weird is Caius’s lunch” contest** and will have to buy us all bánh mì on Friday.’
- 问题一：比赛**有**明确裁决与比分（Caius 11、Matt 7），Matt 当场输掉并被罚请客——「没有结算结果」被原文直接推翻。
- 问题二：比赛的对象是「**Caius 的午饭有多怪**」，不是「谁最怪」——md 改写了赛制。
- 判定：**阻断。**

### J3 ｜「这句玩笑落在案情刚被改写成『他杀』之后」——时序倒置（阻断）
- md:23（**原句 1 · 为什么这样写**）：
  > 「一整套月度打分制度被写得像公司里真实存在的规章，偏偏赌的内容是「今天会不会很怪」。**这句玩笑落在案情刚被改写成「他杀」之后**，读者会听出两层意思：今天果然很怪，而且「怪」在这里是可以被计分、被推迟处理的。」
- 原文顺序：`text/ch13_13.txt:44`（比赛规则叙述）→ `:47-86`（对话）→ `:95`（FSA 邮件「**It was murder.**」）。
- 问题：md 说玩笑落在「他杀」改写**之后**，而原文里「他杀」结论出现在**这场午饭玩笑的最后**（第 95 行），玩笑在**前**。md 自己的原句 3 分析也写「偏偏这句结论被放在一只三明治旁边说出来」（md:37），两处**自相矛盾**。
- 判读：若本意是「读者自前章已知这是他杀案」，则「刚」字与「落在……之后」的写法仍与原句 3 冲突，需改写措辞。**档位：阻断（时序）。**

---

## 三、单子「错」（两边都有但不一致）

### C1 ｜「『他受够了』……却没说的那句心里话」——台词被当成未说出口（阻断）
- md:51（**原句 5 · 为什么这样写**）：
  > 「『他受够了』这四个字既是他对房子的评价，**也是他可能会对警察说、却没说的那句心里话**。」
- 原文 `text/ch13_13.txt:132`（全在引号内＝Caius 当着 Amy 说出口的台词）：
  > ‘I doubt Digby dusted that place. Lord knows how long those prints might have been there.’ Caius remembered how immaculate his own home had been though. **‘He was neglecting it. He’d had enough. Those two partial fingerprints could’ve stuck around for quite a while.’**
- 问题：「He'd had enough.」是**已说出口**的台词（「可能会对警察说」说他对着同事 Amy 说了；「却没说」不成立）。md 自己在 md:49 的中文理解里分对了（叙述＝「Caius 想起自己家一向一尘不染」，台词＝「他受够了」），到分析层又说反。
- 判定：**阻断。**

### C2 ｜「最关键那层猜测留给了叙述，而不是台词」（提示）
- md:52（**原句 5 · 读者视角提示**）：
  > 「注意说话方式的变化：先是当着 Amy 说的判断，接着才是只有读者看得见的心里话——**作者把最关键那层猜测留给了叙述，而不是台词**。」
- 原文 `text/ch13_13.txt:132`：叙述句只有 "Caius remembered how immaculate his own home had been though."（一句），其前后都是引号内的台词；**最关键的猜测**（指纹是旧的、迪吉已经受够了）恰恰在台词里。
- 判定：哪一层算「最关键」可争议，但「留给叙述、而不是台词」与原文结构不合。**档位：提示**（与 C1 配套，建议同改）。

### C3 ｜「周一上午的警局被……一场毒芹排查同时占满」（提示）
- md:11（导航 · 一句话概括）与 md:121（## 一句话总结）：
  > 「**周一上午**的警局被一顿三明治比赛和**一场毒芹排查同时占满**……」
- 原文：场景时序是午饭（饭盒 `text/ch13_13.txt:20`）→ 警局查档与电话（`:105`）→ 傍晚去酒吧（`:274-280`「Pub?」）；**本章根本没有发生排查**，排查是被派到明天的任务：
  > `text/ch13_13.txt:268`：‘It’s a long shot if it’ll throw up anything useful, but we really do need to check that every woman called Isolde within a hundred miles of London isn’t murdering their dates. **One for us tomorrow, Matt, while Amy is off.**’
- 判定：「上午」无原文依据（本章在中午与傍晚各有落点）；「毒芹排查同时占满」把次日任务写成本章正在进行的事。属概括层措辞失准。**档位：提示。**
- 附带：「摊成一张需要逐个敲门排查的名单」——名单本身是**第 16 章**的内容，本章只有任务分派（见 §四）。

### C4 ｜「轮流当对方不在时的裁判」（提示）
- md:21（**原句 1 · 中文理解**）：
  > 「Matt 和 Amy **轮流当对方不在时的裁判**。」
- 原文 `text/ch13_13.txt:44`：
  > ‘At the end of the month whoever had the lowest number of points bought lunch. **Matt and Amy switched out every other month with the other adjudicating.** The rules were straightforward by British standards and so far, no one had endeavoured to cheat.’
- 判定：原文只说「每隔一个月换人裁定」，没有「对方不在」这一层；但该英文句本身有歧义（switched out 也可读作「一方轮空」），故按**提示**处理而非阻断。**档位：提示。**

### C5 ｜「羡慕」vs「rankled」（提示）
- md:14（导航 · 人物弧线）：
  > 「也清楚自己其实**羡慕**迪吉能靠卖掉这栋楼干净脱身」
- 原文 `text/ch13_13.txt:235`：
  > ‘Caius understood, he was in a similar situation himself, but the fact that Digby would’ve had a handsome payout for ridding himself of the guilt **rankled him**.’
- 判定：rankled＝被刺痛／耿耿于怀，不是「羡慕」；md 自己在原句 6 的中文理解写「他心里并不痛快」是对的。**档位：提示。**

### C6 ｜「Matt 从迪吉公寓打来的电话汇报」——方向反（提示）
- md:12（导航 · 视角）：
  > 「第三人称限知，主要贴着顾问警员 Caius，中途穿插 **Matt 从迪吉公寓打来的电话汇报**与 Amy 的判断」
- 原文 `text/ch13_13.txt:144`：
  > ‘Those are what Willow was typing up. Digby was using them as research for his book.’ **Caius called Matt, placing him on speakerphone.** ‘Hombre, are you still at Digby’s flat?’
- 判定：这一场是 **Caius 把电话打到迪吉公寓**（Matt 在那头回话），非「Matt 打来」；且本章 Matt 主动拨出的电话是给 Nathan（`:181`），此时 Matt 已在警局。属方向性措辞不准。**档位：提示。**

---

## 四、本章专属判据的两条定点核对

### 判据①：排查名单的人数与构成「十人：一人在养老院、七人在上小学、最后只剩两个」
- **该构成不在本章原文**。本章只有两句相关：
  > `text/ch13_13.txt:268`：‘…we really do need to check that **every woman called Isolde within a hundred miles of London** isn’t murdering their dates. One for us tomorrow, Matt, while Amy is off.’
  > `text/ch13_13.txt:271`：‘**I bet there’s no more than fifteen Isoldes in the country**,’ Matt said.
- 该名单的真正出处是**下一章之后**：
  > `text/ch16_16.txt:32`：‘Not really. A few phrases here and there. I should learn.’ Caius swung around on his desk chair. ‘In good news, **there are only ten Isoldes in the entire UK. One is in a nursing home in Surrey. Seven are in primary school within either Chelsea, Fulham, Putney or Chiswick.** Names have geo-social currency, I guess.’ He paused for a moment as he considered baby names before getting back on track. **‘That leaves one each for me and you.’** Caius handed Matt a printout.’
- 取证：
  ```
  /usr/bin/grep -n -E "nursing home|primary school|ten Isoldes|Isoldes in the entire" text/ch13_13.txt
  → exit=1（零命中）
  /usr/bin/grep -n -E "十人|十个人|养老院|上小学|小学|nursing|primary school|十个" "ch13 ….md"
  → exit=1（零命中）
  ```
- 判定：md **既没有搬运该构成，也没有写错它**（本章原文不含此内容）⇒ **无编造、无错**。⚠️ 但注意：若日后有人把「十人」写进 ch13，即为跨章搬运（该数属 ch16）。
- **档位：无缺陷（已核实为正确）**；附带记一笔：md「一句话总结」里「摊成一张需要逐个敲门排查的名单」在**本章**尚无名单实物（名单印件在 ch16:32），故 C3 里按「措辞失准」记提示。

### 判据②：食品标准局那封邮件关于毒芹与「是谋杀」的结论是否逐字
- md 引语（md:33）：
  > "‘Nope,’ Caius said, picking up his sandwich. ‘Just had an email from the Food Standards Agency. They’ve investigated the farm where Digby’s bagged salad originated and there was no trace of hemlock in their polytunnels whatsoever. It was murder.’"
- 原文 `text/ch13_13.txt:95`（**逐字一致**，程序核对 `q in src` → True，位置 2206-2452）：
  > ‘Nope,’ Caius said, picking up his sandwich. ‘Just had an email from the Food Standards Agency. They’ve investigated the farm where Digby’s bagged salad originated and there was no trace of hemlock in their polytunnels whatsoever. It was murder.’
- md 中文理解（md:35）：
  > 「不会。Caius 拿起三明治说，刚收到食品标准局的邮件：他们已经查过 Digby 那袋沙拉的来源农场，那边的温室里压根没有毒芹的痕迹——是谋杀。」
- 判定：**逐字与中译均对得上**，关键词 `Food Standards Agency / hemlock / murder` 三项全在本块引语内。**档位：无缺陷（已核实为正确）。**

### 判据③：分部「A MONDAY IN MAY」
- 本章源文**没有**「MONDAY IN MAY」这个串（`/usr/bin/grep -n "MONDAY\|May" text/ch13_13.txt` → 只命中 `:280 ‘Monday Funday,’ said Matt.`）。
- 该串是**全书分部标签**，不是本章文本；同书同分部的其它章 md 同样这样写：`ch49:15`、`ch50:15`、`ch51:11` 均写「分部 A MONDAY IN MAY」。
- 判定：md:15「章末一句「Monday Funday」把这一章扣回分部 A MONDAY IN MAY 的周一」**成立**（章末逐字为 `text/ch13_13.txt:280` 的 `‘Monday Funday,’ said Matt.`）。**档位：无缺陷（已核实为正确）。**

---

## 五、三张单子小结

| 单子 | 条数 | 其中阻断 |
|---|---|---|
| 漏 | 3（L1、L2、L3） | 0（均提示） |
| 编 | 3（J1、J2、J3） | **3** |
| 错 | 6（C1–C6） | **1**（C1）；另 C2–C6 提示 |
