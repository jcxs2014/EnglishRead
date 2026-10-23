# ch10 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，272 行全读，74 事件 / 9 关系 / 7 数字 / 4 未决 / 10 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=9 / words=2912 / block_target=[5,9]）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`、`hole=0`、`empty_quote=0`。
> 补验（机器盲区）：本章 9 条引语**均无 `…`**（自建探针确认）；本章 22 行词表例句 **22/22 逐字回源命中**（`/tmp/vocab_check_hx.py`：`ch10: rows=22 missing=0`）、**22/22 词头落在例句内**（`/tmp/vocab_head_hx.py`，无输出＝零失配）；**引号配对**探针 `/tmp/pair4_hx.py` 全书扫描 ⇒ **本章 0 处偏离**（全书唯一 1 处在 ch09 原句 7）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号 + 逐字） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:41` `Cynthia wished they weren’t walking quite so briskly. … Her curiosity was piqued, and she would have loved to linger and watch the men wager away staggering sums of money while the painted doves giggled and flirted shamelessly. Unfortunately, their escort seemed to be on a tight schedule, and she rushed to keep pace.` —— 她**好奇被撩起**、本想留下来细看赌局，只是护送者行程紧才快步跟上 | md 原句 2·读者视角提示写「**她没有停下来看，只是被领着穿过**」，只保留「没停」，**丢掉了「本来想看」这一层**；`wager` 一行的例句正是 `:41` 全句 | **不构成阻断**（人物刻画细部，非事件／转折）；**建议**在原句 2·读者视角提示补「她其实想停下来看」 |
| L2 | `:59` `‘Mr Sinclair has strict rules of confidentiality, Lady Burrows. His patrons are guaranteed privacy. He would be… displeased if that promise was threatened.’` ＋ `:65`–`:71` 管家以沉默作答 | md **全章未提**（导航、原句 1–9 均无） | **不构成阻断**（覆盖取舍；块数已触 `block_target` 上限）；**建议**在导航·Tropes 或人物弧线补「辛克莱以保密规矩立威」一句 |
| L3 | `:104` 海伦娜「像雾一样」挡在醉醺醺的贵族老爷前，俯耳低语令其瘫坐回椅；`:119` `‘Not nearly as much as I wanted.’` | md 导航·人物弧线写「替她**挡人**」⇒ 事件已覆盖；但**那句带刺的回答**未收录 | **不构成阻断**（导航已覆盖事件本身） |
| L4 | `:176` `‘Have you ever considered the marvel of a viper’s venom? … Trust me when I tell you, Miss Blair is far more deadly than that venom.’` ＋ `:182` `‘… no one has attacked your intelligence. Have I been misled? Are you a fool?’` —— 辛西娅第一次为海伦娜出头、当面顶撞辛克莱 | md 原句 6 取的是 `:149` 的情感转折、原句 7 取的是 `:227` 的威胁，**中间的唇枪未选** | **不构成阻断**（9 块上限下的选段取舍；本章核心事件「进办公室→对峙→问债→问死因」链条完整）。⚠️ 但这是本章**最接近「关键转折缺失」的一处**：若后续主张「为海伦娜出头」必须在 md 可见，本条应升为提示项，须由执行方拍板后再改 |
| L5 | `:245`–`:263` 辛西娅回想起门口那一下、列出「三条理由」、并追问「为什么海伦娜一靠近我体温就升高」 | md **未覆盖**；原句 6 只到 `:149` | **不构成阻断**（内心独白层，非事件／转折） |
| L6 | `:239` `I could use a pair of women as formidable as you and Miss Blair.` ＋ `:242` 「他把我俩叫作『一对』像钩子勾住了她」 | md **未覆盖**，也**未做任何断言** | **不构成阻断**（原文该词的所指本身有歧义，md 未断言即不构成错误） |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–9 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的三处疑点：

- **「巴克尔索恩夫人」「上流淑女会」是否本书别处另有译名**——`/usr/bin/grep -rn "Buckland\|Buckle\|Genteel\|Kentmore" text/`：**`Lady Bucklethorne` 与 `Society of Genteel Ladies` 全书仅见于 `text/ch10_chapter_10.txt:53`**，别处无同实体 ⇒ md 的两个新译名**不构成跨章冲突**（成立）。
- **导航·人物弧线「辛克莱……是一个会衡量对手……的**赌场主人**」**——`:218` `‘As the owner of a gambling hell, …’`（辛西娅语）⇒ **成立**。
- **导航·Tropes「长得像魔鬼的男人没能让她心动」**——`:149` `she felt nothing. No hint of attraction, no whisp of need, no stirring low in her belly.`（指**辛克莱**）⇒ **成立**。
- **md 未提 `:203` 辛克莱称正在质问他智力的辛西娅为「Miss Blair」**（按上下文她应是 Lady Burrows，疑为原文笔误）⇒ md **没有**据此编出「故意混淆／早知互换身份」之类的情节，**无编造**。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 导航·情感弧线位置 | 「从**进门前的**失控恐惧，到赌厅里的好奇与警觉……」；一句话总结「辛西娅**走进**辛克莱的赌场」 | 进门发生在上一章：ch09 `:233` `Stringed music escaped on a cloud of cheroot smoke and perfume. Cynthia stepped in front of Helena … as they both faced a man dressed much like Cynthia’s butler.` —— 她们**上一章就已进入俱乐部内部并见到管家**；本章 `:38` 起是「The burly gentlemen led them past a room…」＝**已在里面往里走**；`:35` 的恐惧发生在**进入内部之后** | **提示**（措辞级·涉时序）：情感内容与位置（本章开场）正确，仅「进门前／走进」这一时点标签差一场。改法：`进门前的` → `刚进俱乐部时的`（一字级） |
| E2 | 原句 3·为什么这样写 | 「位置又高到天花板下方、**墙腰以上**」 | `:89` `They sat just below the ceiling and **extended halfway down the wall**.` —— 镜子从天花板下方延伸到**墙面中段**；同章原句 3·中文理解写的是「一直延伸到**墙壁中部**」（与原文一致） | **提示**（同章内两处措辞不齐）：`墙腰以上` 非错但比原文低了一档，与本块自己的「墙壁中部」不齐；改法：`墙腰以上` → `墙面中部` |
| E3 | 原句 8·中文理解 | 「她**听说**自己刚去世的丈夫欠了他的钱」 | `:236` `‘I understand my recently deceased husband was in debt to you. …’` —— 「I understand」＝**我明白／我了解到**，不带「听人转述」的意味 | **提示**（译法级）：`听说` 凭空加了一层「消息来源」，与原文语气不合；改法：`听说` → `明白` |
| E4 | 原句 2·读者视角提示 | 「**她没有停下来看，只是被领着穿过**」 | `:41` `Her curiosity was piqued, and she **would have loved to linger and watch** the men wager away staggering sums of money …` —— 她**本来很想**停下来看，是被行程逼着才快步跟上 | **提示**（措辞级·取舍）：现写法与她「好奇」的状态形成轻微落差；不构成事实错误，但读者会得到「她对场子没兴趣」的印象，与原文不符 |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 呕吐或晕厥、一辈子没这么紧张、连十五岁见女王也没有 | 辛西娅自评 | 自己的神经 | 「连见女王都没这么紧张」＝她自己的比较 | 对应成立 |
| 2 | 魁梧男人领她们穿过烟雾/喝彩/赌桌；女人像异国鸟飞旋不落 | 叙述层 | 那几个女人 | 「从不落下」写的是**那些女人**没有落脚的处所 | 对应成立 |
| 3 | 海伦娜抬下巴示意高处的镜子，只反吊灯光、无他用 | 海伦娜抬下巴 | 西墙高处那排镜子 | 「这个高度不像给人整理衣冠用的」＝叙述者的推断，非事实断言 | 对应成立 |
| 4 | 不是镜子而是单向窗：外边能看进来、她们只见倒影 | 海伦娜说 | 那排「镜子」 | 「权力方向」＝从里到外的视线差 | 对应成立 |
| 5 | 海伦娜要跨门槛时被她握紧手拦住 | 辛西娅握紧并拦住 | 海伦娜（跨门槛的动作） | 「被拽进去损害形象」＝辛西娅自己的顾虑 | 对应成立 |
| 6 | 怀疑自己还能否感受欲望；若有男人能，那也该是这个危险家伙；可她回头撞上海伦娜的目光才动了一下 | 辛西娅自问自答 | 自己的欲望 | 「动了一下」的对象是**辛西娅本人**，被看见的对象是**海伦娜** | 对应成立 |
| 7 | 他承认她的朋友也许危险，自己是死亡的化身 | 辛克莱说 | 「your friend」＝海伦娜 | 「他本人就是死亡」＝辛克莱自抬 | 对应成立 |
| 8 | 问欠了多少要结清；债务可落到活着的亲属头上；不想欠他人 | 辛西娅说 | 休伯特的债 | 「落到活着的亲属头上」＝辛西娅陈述的**债务规则**，非她本人 | 对应成立 |
| 9 | 丈夫的债与他的非正常死亡有没有关系 | 辛西娅问 | 债务与死因 | 「她问的是债，真正想知道的是死因」＝读者视角推断 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 10. Chapter Ten`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 **9**，落在本书区间 [6,13] 与本章 `block_target=[5,9]` 内（**已触上限**：若因修复增块，会触发 `block_count`）。

### 引号配对（机器层零覆盖，自建探针）

`/tmp/pair4_hx.py` 全书扫描 27 章：判据＝**引语块内层以闭引号 `’`/`”` 结尾、且全块不含任何开引号 `‘`/`“`**。全书 **TOTAL 1**，唯一一条在 ch09 原句 7；**ch10 九个引语块全部配对完整**（含原句 7 这种从对白中途切起、但首尾引号成对的形态）⇒ **本章引号配对 0 偏离**。

### 表头分隔行体例

本章词表用 `|------|------|------|`，ch03/ch04/ch06/ch11–ch16 同款；其余 17 章用 `|---|---|---|`。两种写法都是合法 GFM，`gate.sh` 全书 RC=0 ⇒ **不判缺陷**，仅记录体例分布。

## 六、语料层观察（非 md 缺陷，不计入三张单子）

本章**无**站点宣传行注入（全书 5 章 6 行：ch03:188 / ch08:170+173 / ch13:185 / ch19:197 / ch25:214，见 ch08 的 §六）。本章 md 9 条引语**无一跨过**空行断裂，`segment_miss=0` 已证逐字。

### 原文层记录（**不可据此断言**，仅备查）

- `:203` 辛克莱对**正在质问他智力的辛西娅**说 `‘No one’s ever dared question my intellectual acumen, Miss Blair.’` —— 按上下文她此时应是 Lady Burrows；`:227` 他又对她说 `give your protector ’er dues`，而 `:206` 辛西娅称海伦娜为 `my friend` ⇒ `:203` 的「Miss Blair」疑为**原文笔误**。**md 未提及此事，故无缺陷**；但后续章节若要引用此句，须先确认是笔误还是刻意。
- `:74` 原文拼作 `Bacarat`（通行为 Baccarat）；`:194` 原文拼作 `lightening`（通行为 lightning）——均为原文用字，**不得在 md 里「改正」原文引语**。
