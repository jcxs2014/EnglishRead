# ch14 深审判定表（R5）

章：`ch14 caught in the grow out barn.md`（书内 Chapter Thirteen，H1 `# 14. Chapter Thirteen` ✓）
语料：`text/ch14_chapter_thirteen.txt`（114 行／6,832 B）
流程：R1 素读（69 条事实／0 MISS）→ R2 机器层（verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 4／分片 5／MISS 0；`…` 拼接块经 `verify_fragments_indep.py` 逐片段独立取证（书级 313 条／443 片段／MISS 0）；词表 13 行例句展平逐字 0 MISS；直撇号 **0 站** | 🟢 全绿 |
| 对应 | 4 块 anchor 全在素读表内；缺项：:42 末句（habitat/sty 自嘲）、:66（Ironheart 点名）、:21（三箱之后 Harrison 没来＋no closer）、:75 后半句（unless Nova’s a liar）、:72（拔辫子幻想）、:84（事故起数追问）、:96（aimed for assertive） | 🔴 阻断 3（C-14-2／4／6）＋提示 5（T-14-2／6／8／9／10） |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 4 ∈ [2,4] ✓／words 1168／struct_bad 0／cjk_low 0／template 0 | 🟢 全绿 |
| 断言 | 单位误写并自相矛盾／语法术语误称并自相矛盾／与本章命令相抵并自相矛盾 | 🔴 阻断 3（C-14-1／3／5）＋提示 5 |

**本章合计：阻断 6 ／ 提示 10 ／ 假红-不报 7 ＋ 字形站 0**

## 缺陷形态归因

- **本章最密的形态是「导航层与块层各写一套，块层对」**：C-14-1（五指远 vs 五英寸）、C-14-5（没有换来任务 vs 只换来一句命令）。两处的错误面都在 md:10–md:14 这五句里，而 4 个精读块全部写对。⇒ 与 ch07／ch09／ch11／ch12／ch13 同一风险模型：**短章的承重判读压在导航五句，人判必须逐句把导航与块层对表**，只读块会漏掉整类。
- **自查报警信号（同卷两处口径不一致）在本章出现 2 次**，均已升级为阻断；这条规则的取证成本极低（同文件内 grep 同一实体两种写法即可），建议在整改批里作为独立一步跑。
- **分析层语法术语误称连续两章**（ch13 `I'd be creating`＝习惯性将来时；ch14 分裂句＝宾语前置）。同族还有 ch11/ch12 的「残句」「单音节」。⇒ 规则建议：**写「前置／倒装／省略／时态／单位」类判定前，先在原文里标出该结构的成分位置**；分裂句、强调句一律写明焦点落在哪个词之后。
- **对冲词漏收**（本章 `apparently` :21、`Surely … that would be impossible` :66、`probably` :72、`Maybe…Maybe` :54、`like` :60/:114）：md:13 保住了 `probably`（F-14-2），md:44 保住了两个 `like`（F-14-5），但 :21 整段没进 md，`Surely` 被 C-14-4 的漏收连带丢掉。**本库连续六章都在这一条上出红 ⇒ 属可预筛类。**

## 已核实为正确（下轮勿改坏）

1. `:9`→`:18` 清晨段全链：`a piece of wet fabric dragging on the floor, maybe`／`The electric hum accompanied it, too, but that was becoming familiar.`／`I heard the sound again—and was that a footstep?`／`“Hello?” I called groggily, half raising myself from my bed.`／`No one replied, and I wrote it off as a remnant of my dream.` ✓——md:24「破折号里的比喻自带修正」、md:14「三个声源未明的响动」均有凭据；`maybe`／`was that` 两层不确定都被保住。
2. `:21` `Drowsy from my lost hour of sleep, I almost missed my ride with Gazzie.` ✓（md:11 未把「误了车」写成迟到）。
3. `:24` 午饭与箱塔幻想：`a ham sandwich packed by Aunt Virginia, pickles on the side for extra salt`／`I imagined it toppling over, the moldy files crushing my skull. It would be hours before anyone found me.` ✓——md:13「黑色幽默」逐字对应。
4. `:27` 主动性的自我动员：`Locked away like this, I’d never make progress with Gazzie. I had to find her. Show initiative. Tell her I could help with something more important.`／`The night before, I’d asked Aunt Virginia for proper shoes, and she’d unearthed a pair of old work boots. Now I was ready to handle the alligators. Feed them, maybe.` ✓（词表 `initiative`／`unearthed` 两行例句逐字）。
5. `:30`→`:39` 出门过前台：`the processing area door still closed`／`“Problem?” Nova asked, eyes flicking up from her phone`／`“Left something in the car,” I replied, trying to sound sheepish.`／`Her eyes slid back to her phone.` ✓——md:13「对 Nova 撒谎（东西落车里）」成立，且 md:12 的「逃办公室」有凭。
6. `:42` 开车经过的三段：`the midday sun weighed on my shoulders`／`the golf carts all had keys in their ignitions, and no one was in sight`／`fifty alligators sunbathed on the shore`／`only some low-lying, yellowed strips`／`alligators gravitated toward long grasses, especially patches sticking out of water`／`My chest squeezed with an emotion close to sympathy` ✓（md:30／md:34 的数目、状态、`close to` 三点均对；`sty` 一句见 C-14-2）。
7. `:45` 一辆车上的两个男人：`another golf cart was approaching, driven by the goateed guy`／`A blond, thickset man next to him slapped his shoulder, and they both stared at me.`／`I raised my hand in greeting, hoping I looked confident, like I was exactly where I belonged.`／`They didn’t stop, and I breathed a sigh of relief.` ✓（md:11 的引语逐字；「两个高尔夫车上的」的歧义见 T-14-1）。
8. `:48`→`:51` 进棚：`After several minutes of fruitless searching, I decided to peek inside one before I got too light-headed.`／`The doors were heavier than I’d expected, and the wood handle scratched my palm`／`the now-familiar stink of rotten eggs and stagnant water`／`I’d forgotten how dark the other one had been, how it took a few moments for my eyes to adjust.`／`Dozens of alligators lay in the first pen, each about a foot long.`／`the same bright green algae I’d seen on my tour`／`save a few softball-sized spots… their delicate torsos angled downward, little claws spread wide` ✓——md:10「几十条」与 md:12「幼鳄」均按 :51／:114 有据。
9. `:54` `“I’ll let them know about the algae,” I promised.`／`Maybe alligators, like cats, vaguely understood what people said. Maybe my tone would comfort them.` ✓（两个 `Maybe` 的悬置，md 未升格）。
10. `:57`→`:63` 转头与嘶鸣：`a thin sound, like a sharp exhale`／`each and every alligator, in unison, slowly turned to face me`／`like they were memorizing my face`／`a wave of unceasing venom, like the juveniles had with Gazzie`／`The hair on the nape of my neck stood at attention… my hands so sweaty I could barely grip the door handle` ✓——md:40／md:44 的两层 `like` 分法与原文一致。
11. `:66` 自我安抚段：`I forced myself to breathe slowly, counting to ten while my thoughts sorted themselves.`／`Surely the alligators hadn’t moved perfectly in sync; that would be impossible.` ✓（`Surely`＋否定式，md:46 只引 `that would be impossible` 未改写，判对应正确；Ironheart 半句缺失见 C-14-4）。
12. `:69`→`:75` 被当场抓到：`Behind me, someone cleared their throat.`／`Harrison next to her, looking satisfied with himself`／`Nova, out of breath, turned the corner. She’d probably tattled on me.`／`“You’re not supposed to wander,” Gazzie said.` ✓——md:13「告状（叙述者判断）」保住 `probably` ✓；Gazzie 那句 `And unless Nova’s a liar, she told you that already.` 的**条件层未收**，见 3-diff 的 T-14-10（提示，勿反向改坏 :75 引语）。
13. `:78`→`:84` 呛话与事故论：`cringing as soon as the bitter words left my mouth`／`I wasn’t the kind of person who lashed out, I reminded myself. Anyway, I was trying to win Gazzie over, not antagonize her.`／`“People don’t plan on accidents. That’s why they’re called accidents.”`／`Nova had mentioned accidents, too.` ✓（词表 `antagonize` 行例句逐字；md:10 引 :81 全句逐字）。
14. `:87`→`:96` 请缨三连：`Gazzie continued her scolding. “What did you think you were doing?”`／`Sucking in a deep, calming breath, I said, “Looking for you. I was hoping I could help—”`／`“Help?” she interrupted, scowling.`／`The sun shone too brilliantly, and I shielded my eyes.`／`“I feel like I could be better utilized elsewhere?”` ✓（破折号收尾的半句、以及「出口成问句」的形态见 T-14-9）。
15. `:99`→`:108` 权力小动作：`Gazzie’s mouth tightened, and she half turned to Harrison.`／`“On it,” he said.`／`She whipped around, assuming I’d follow.`／`Harrison twitched his lips into an exaggerated grimace—no doubt repressing a smug smile—before trailing behind her.`／`Nova caught up to him, muttering something in his ear.` ✓（词表 `repressing` 行例句逐字；md:13「留下命令走人」对应 :105/:108）。
16. `:111`→`:114` 收尾：`I blinked back tears. Getting Gazzie to love me was starting to feel like an impossible task.`／`the line of three people who clearly thought me useless`／`I wondered if they’d been able to sense Gazzie outside, or if they were directing all that hatred toward me.` ✓——md:11 引 :111 逐字、md:14「章末悬置问题…不给答案」判定成立（两个 `if` 并列未裁）。
17. 词表 13 行例句全部为原文逐字子串（0 MISS）；`hum`／`五英寸`／`probably`／`apparently` 等字形与限定词的 md 侧写法已逐一核对。

## 不许裁决（本章内）

- **湿布拖地声／疑似脚步／电流嗡鸣的声源**：:9／:12 一律未给（且 :18 她自己 `wrote it off as a remnant of my dream`）；不得判定房内有他人、不得与 ch10:174 的 `The hissing started first` 合并成同一事件。
- **几十条鳄鱼是否同步转头**：:60 `in unison` 出自叙述者视角，:66 她自己立刻否定（`Surely… that would be impossible`）；超自然与农场两种读法原文并列且未调和，不得选边。
- **本章 grow-out 棚与 ch08 那「ten smaller rectangular barns where juvenile alligators were housed」（ch08:177）是否同一批动物**：:60 用 `like the juveniles had with Gazzie` 作比，:51 又说 `I’d forgotten how dark the other one had been`；原文未写明，不得坐实。
- **幼鳄的恨意冲谁**：:114 明示两问（`if they’d been able to sense Gazzie outside, or if they were directing all that hatred toward me`），不得裁决。
- **Nova 是否真去告状**：:72 带 `probably`；:108 她在 Harrison 耳边低语的内容原文未写。
- **最近事故「究竟几起」**：:84 只是她的追问；本章未给数字，不得据 ch12:105 折算。
- **Harrison 的「On it」接的是哪件事**：:99 Gazzie 半转身、:102 他应答，中间无宾语；不得写成他去查藻类或去处理她擅用车（两种都有可能，原文未裁）。
- **Gazzie 说 `If you can manage it.` 的本意**（真质疑还是激将）：本章无第二句支撑；不得裁决。
