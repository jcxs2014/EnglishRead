# ch13 深审判定表（R5）

章：`ch13 processing spaces and alligator bones.md`（书内 Chapter Twelve，H1 `# 13. Chapter Twelve` ✓）
语料：`text/ch13_chapter_twelve.txt`（256 行／13,476 B）
流程：R1 素读（139 条事实／0 MISS）→ R2 机器层（verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 6／分片 8／MISS 0；无孤立 `…` 拼接（原句2／原句5 各含 1 个省略号，两段均已在素读表内独立取证）；词表 15 行例句展平逐字 0 MISS；**直撇号 8 站** | 🟠 逐字本体全绿，字形 8 站待改 |
| 对应 | 6 块 anchor 全在素读表内；缺项：:198–:201（监管与通融）、:216（第二次挥棒）、:219（鼻子贴玻璃）、:180（抠电池比喻）、:192（她在不在乎）、:249（本姓 Beaumont） | 🔴 阻断 4（C-13-2／7／8／9）＋提示 1（T-13-5） |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 6 ∈ [4,7] ✓／words 2286／struct_bad 0／cjk_low 0／template 0 | 🟢 全绿 |
| 断言 | 施事归错（叙述者同位语安进角色嘴里）／计数断言／凭空时距×2／语法术语误称／词义误读／无据心理结论且与 :225 相抵／自造对照 | 🔴 阻断 5（C-13-1／3／4／5／6）＋提示 5 |

**本章合计：阻断 9 ／ 提示 6 ／ 假红-不报 6 ＋ 字形站 8**

## 缺陷形态归因

- **「把叙述语言当角色台词」的新形态**（C-13-1）：本章 Harrison 的讲解全部走转述（`explaining that…`／`He named each room`），md 却把破折号后的同位语读成他「当场承认」。⇒ 规则建议：**分析层凡是「某某自己说出／当场承认／亲口」类判定，先确认该串英文在原文里是否位于引号内**；不在引号内的一律改写成「叙述语言」。同族：ch12 C-12-2（把叙述者推断升格为结构结论）。
- **认知对冲与限定词再次被削平**（C-13-6 的「不是恐惧」、T-13-4 的 `at least`、C-13-9 的 :192 两问）：同族 ch09 C-09-1、ch11 T-11-4、ch12 C-12-3。本库连续五章都在这一条上出红，**属可预筛类**。
- **凭空时距（成组，一次两站）**（C-13-3）：「两分钟」「过了几秒」都为原文没有的时间量词。与前四章「无据时刻」同族，整改时应全卷 grep「分钟／秒／一会儿」再判。
- **计数断言把真实漏项吃掉**（C-13-2）：「自报两件事」正好漏掉 :249 本姓 Beaumont——而这一条按既有第 30 类（叙述者真名落点）是高价值信息。**写「本章自报／提到 N 件事」前先枚举。**
- **本章风险模型与 ch07／ch09／ch11／ch12 一致**：引语层机器全绿，人工红点集中在导航五句（md:10–md:14）与块内「为什么这样写」；精读的中文理解栏反而基本对应（只有 C-13-5 一处词义）。

## 已核实为正确（下轮勿改坏）

1. `:9` 全段：`seven thirty each day`／`before Florida’s heat grew relentless`／`by my second afternoon`／`labeling it with Mama’s words the next. The devil’s inside.`／`was beginning to feel guilty that I’d strayed from my quest` ✓——md:10「第二天工作到下午」与 md:11「钝 guilt」都有原文凭据，`The devil’s inside.` 无引号 ✓（md:24）。
2. `:15`→`:24` Harrison 端咖啡出场链：`The acrid smell of fresh coffee drew me out of a sorting stupor`／`My vision tunneled`／`:18` `his eyes were the pale blue of clean bathwater`＋`Greer Fine Alligators muscle T-shirt and bootcut jeans`＋`he could’ve been a porn star`／`handle extended toward me` ✓（md:12 的「单方面有吸引力的评点」由此而来，见 T-13-2 的边界）。
3. `:30`→`:39` 双方措辞：`“I don’t know if I have time, given the pressing need to organize these files.”`／`“My reaction was warranted.”`／`“Sure.” I leaned into my salty tone`＋`lock me in a closet with boxes that haven’t been touched for half a century` ✓——md:13「讽刺但不在乎」与「半世纪」逐字对。
4. `:42`→`:54` `like he was deciding whether to pour the coffee over my flip-flops`／`I wasn’t a coffee drinker—my heart couldn’t handle much of it`（:45）／`indignity of fainting in front of my newfound nemesis, who, to my annoyance, smelled like dryer sheets`（:48）／`I’d expected him to smell like mud or a hatchling barn` ✓。
5. `:51`→`:66` `“Pen burst on you?”`／ink-stained fingers／`“Astute observation.”`／`“I draw.”`／`“Good for you. I can’t draw a circle.”`＋`like he’d spilled a terrible secret`／`“What do you draw?” Politeness strained his voice.`／`“Nightmares.”` ✓——md:13 的「画不圆」「nightmares」两条自报逐字有凭。
6. `:69`→`:93` 空间与动机：`Greer House creeps you out, too?`／`“How long do you think you’ll stay?” He was going for casual, but eagerness crept into his voice.`（:75）／`So that’s why he’d brought me the coffee… I wouldn’t make it easy for him to get answers.`（:78，全章 `answer` 仅 1 处）／`we stood two feet apart`＋`he had at least six inches on me`（:90）／`“Well, it seems like Gazzie, for one, really wants you to stick around.”`＋`He had some nerve.`（:84/:87） ✓。
7. `:96`→`:105` 休息室里 Nova：`gave me a half smile that froze in place when her eyes flicked to Harrison behind me`／`trying a little too hard to pretend she was immune to his biceps`／`the ghost of a frown on Nova’s face`／`Perhaps she liked to keep Harrison to herself. That, or Gazzie had asked her to keep me isolated in my filing cave and she worried this constituted a breach.` ✓——**两种解释并列未裁**，md 未替她挑一个 ✓。
8. `:111`→`:132` 骗带路一段：`remembering Gazzie’s interrogation during our first dinner`／`“Didn’t she already take you on a tour?”`／`“Outside. I didn’t get to see inside.”`／`:120` `‘Florida Man Brings Farm Gator to Local Bar.’`＋`“Maybe you could show me around?”`／`He wasn’t buying my act, but he wasn’t dismissing me, either` ✓（md:13「故意压下 pride、摆出 dejected 表情」另见 :141 `I repressed my pride, adopted my most dejected expression`）。
9. `:135`→`:147` 加工区：`the doors Nova had declared off-limits`／`pulled a key off his belt loop ring and opened one of them`／`slaughtering room, skinning room, skin salting, skin storage`／`smelling faintly of bleach`／`“You can’t go inside with open-toed shoes. Not safe.”`（:138）／`“We can peek in the slaughtering room if you’re not squeamish. It’s the only room with windows.”`（:144）／`I’d been drawing dead and decaying animals for years`（:147） ✓。
10. `:150`→`:159` 屠宰间外观：`Two large windows covered with open vinyl blinds`／`About double the size of a school classroom`／`concrete walls and floors that sloped to a center drain`／`the telltale mark of an old leak trailed down the wall`／`another copy of Ida’s primary portrait hung`＋`her delicate shoes poking out of the grass`／`Hollywood could use this as a slasher film set`／`his face was tinged green. Maybe he was the squeamish one.` ✓。
11. `:162`→`:177` 宰杀动作链：`duct tape`／`she still wore the jeans and white button-down shirt she’d arrived in`／`too focused to notice or decided to ignore us`／`wrestled the alligator above the drain`／`Without any fanfare`／`blood spraying across her shirt`／`The alligator stopped moving, but its eyes were open. It was stunned.`／`Gazzie waved the man from the room`＋`his lip curled in disgust`／`Shirt untucking as she moved… plunged it into the top of its head, yanking it to the side. The alligator thrashed a few times before it stilled.` ✓。
12. `:183`→`:192` captive bolt：`“She’s severing the spinal cord,” Harrison whispered`／`It’s like a gun, but it fires a metal rod through an animal’s skull. It’s less painful. We have one, but Gazzie says it’s not traditional, so.`／`His tone—slightly disgusted, slightly guilty—gave me pause` ✓（md:13「低声讲得出更无痛的 captive bolt」、md:14「价值观冲突塞进 whisper 对白」成立）。
13. `:207`→`:213` 改造意愿：`“I wonder if she’d reconsider the slaughtering process.”`／`He scoffed. “Not a chance.”`／`With a confidence I didn’t feel, I retorted, “Maybe the right person hasn’t asked her.”`／`Harrison rolled his eyes, dismissing me, but I was in earnest, already brainstorming ways I could update the farm if I took over.` ✓（md:13 的 brainstorming 一句逐字对，且 `With a confidence I didn’t feel` 的对冲在 md 中未被升格 ✓）。
14. `:222`→`:225` Mama 的声音与退开：`Mama’s voice ghosted in my ear. You’d better tame that devil in you.`／`Closing my eyes, I stepped backward`／`a raging creature drawn to darkness` ✓（引语逐字；md:11 引这两句时只需把撇号改回弯形，见 T 节字形站）。
15. `:228`→`:246` 收尾问答：`Gazzie pulled a hose off the wall and sprayed the floor. Puce-red water swirled into the drain.`／`“They’ll take the body to skinning. Then the hide cures while the meat goes to the butchering team.”`／`“And where do the bones go?”`／`It was the phrase on Mama’s closet wall, haunting me: The Greers built their fortune on alligator bones.`／`“We keep some of the skulls and trash the rest.”`＋`“Show’s over, Miss Greer.”` ✓。
16. `:249`→`:255` `“It’s Beaumont,” I said absently.`／`I’d already won by tricking him into showing me the processing facility`／`For a breath—only a breath, no longer—she bowed her head, like she was praying.` ✓——md:10「像在祈祷」保住了 `like`，未升格为「在祈祷」✓。
17. 词表 15 行例句全部为原文逐字子串（0 MISS，展平后现算）。

## 不许裁决（本章内）

- **山羊胡男人的表情**：:165 只写 `his lip curled in disgust`，且叙述者立刻声明 `Before I could analyze his expression`；不得判定他反感的是宰杀方式、Gazzie 本人还是她在场。
- **Gazzie 低头是不是祈祷／在对谁祈祷**：:255 用 `like she was praying` 且时长被叙述者自我限定（`only a breath, no longer`）；与 :150 门上方那张 Ida 画像的关系不得坐实。
- **她第二次挥棒之后有没有打死**：:216 止于 `Then she raised it again.`，随后 :228 直接是冲地；第三次是否落下、鳄鱼何时死亡，原文未写。
- **「叙述者是否会接手农场」**：:141 `I wouldn’t be able to convince Gazzie to let me inherit if…` 与 :213 `if I took over` 全部是她的意愿与假设，Gazzie 本章未表态（且全程无台词）。
- **Nova 对 Harrison 的态度属于哪一种**：:105 明示两条并列解释（`Perhaps… That, or…`），不得择一。
- **「农场确有违规」**：:195 `the exact regulations my grandmother was surely violating. Probably not.`（对同事不知情而非对违规本身）＋:198 `“The farm must not get regular inspections,” I mused` 属她的推测，:201 Harrison 的答复只讲检查频率与通融，不承认违规；不得裁决农场是否真的在违法。
- **Harrison 为什么脸发绿**：:159 `If I wasn’t mistaken—and I wasn’t—his face was tinged green. Maybe he was the squeamish one.` 带 `Maybe`；不得写成他从未进过屠宰间或他不忍杀生。
- **「Mama 那句 The devil’s inside 指什么」**：:9 明写 `I still didn’t know what Gazzie had done to make my mother write such desperate phrases`；本章不得补写其因。
