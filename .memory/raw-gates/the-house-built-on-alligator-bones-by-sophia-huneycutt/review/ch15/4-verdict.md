# ch15 深审判定表（R5）

章：`ch15 the second inexplicable person.md`（书内 Chapter Fourteen，H1 `# 15. Chapter Fourteen` ✓）
语料：`text/ch15_chapter_fourteen.txt`（114 行／7,110 B）
流程：R1 素读（57 条事实／0 MISS）→ R2 机器层（verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 4／分片 5／MISS 0；`…` 拼接块（原句 2）已在书级 `verify_fragments_indep.py`（313 条／443 片段／MISS 0）逐片段命中；词表 13 行例句展平逐字 0 MISS；直撇号 **0 站** | 🟢 全绿 |
| 对应 | 4 块 anchor 全在素读表内；缺项：:30 先假设是 Gazzie＋:33 本能排除（只落词表）、:33 茉莉＝ch09:30 前兆未登记、:72 `the man’s voice from a few nights before`（＝ch06:12）、:69 `“Actually, I guess you don’t.”` | 🔴 阻断 3（C-15-5／6／7）＋提示 4（T-15-1／3／4／6） |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 4 ∈ [2,4] ✓／words 1143／struct_bad 0／cjk_low 0／template 0 | 🟢 全绿 |
| 断言 | 时点被升成刻度／对冲被抹平／跨章「第一次」无枚举／全称断言被同块反证＋方向自相矛盾／陈述＋反讽误称「自问」 | 🔴 阻断 5（C-15-1／2／3／4／8）＋提示 2（T-15-2／5） |

**本章合计：阻断 8 ／ 提示 6 ／ 假红-不报 8 ＋ 字形站 0**

## 缺陷形态归因

- **本章的 3 条「漏」全部是同一种漏法：承重句只进了词表例句，没进导航与块层。** :33 `I knew, instinctually, that…` 是词表 `instinctually` 行的例句、:30 与 :72 连词表都没进。⇒ 既有规则「进了词表≠已登记」在本章第三次独立成立，建议作为预筛项：**对每章的词表 13 行例句反向 grep 导航与块层，命中只在词表行内的，逐条人判是否属承重信息**。
- **跨章引用是本短章的第二大风险面**：茉莉（ch09:30）、男人的声音（ch06:12）、Lena 已被点名（ch05:189）、downtown 散步（ch11:12）四处都真的存在，而 md 一处未接。**「第一次／第二次」类计数断言必须先枚举**——本章 md:56 写「第二次」写对了（:93 逐字 `the second time`，属原文自数），md:90 写「第一次应下屋外的邀请」却与 ch11 相抵；同一句里前者有据、后者无据 ⇒ **同一段落里两类「第 N 次」要分别取证，不能靠邻居句背书**。
- **总结句（`## 一句话总结`）与导航五句同为强化位**：C-15-2、C-15-3 都在 md:90，两处都是把原文的缓冲词（`sometimes`／`probably`／无「第一次」）写成判定（「坐实」「名分」「第一次」）。⇒ 建议在整改批把「总结句回查缓冲词」列为独立一步（与 ch14 的「导航—块层对表」并列）。
- **分析层句式误称连续第五章**（ch11 残句／ch12 单音节／ch13 习惯性将来时／ch14 宾语前置／ch15 陈述＋反讽误称「自问」）。同族规则建议已在 ch14 提出，本章追加一条更省事的判据：**写「她自问／她问」前，先 grep 该句是否含 `?`**；`:24` 两句皆句号，`Great.` 是反讽不是问。
- **审查方自查（本轮新增，非章内缺陷）**：素读初稿把 :90 记作 `I shook her head.`，anchor 立刻 MISS，实为 `I shook my head.` ⇒ 凡拟写入「书内不一致／不许裁决」的原文，必须先过逐字 anchor；本表与 3-diff 均未采用该说法。

## 已核实为正确（下轮勿改坏）

1. `:9` 农场独处段全链：`After my escapade to the grow-out barn, I spent no more than twenty minutes alone at the farm.`／Nova 三问 `how far I’d gotten, when I’d finish, whether a tax return was stained`／`making stilted small talk, mostly about the growing, roofer-resistant ceiling leak`／`Beyond our silent drive back to Greer House Friday evening, I didn’t see her.` ✓——md:10「追问文件」「搭话」「显然是被派来盯她（见 T-15-2）」与「一次也没来看过她」（F-15-8）均有凭；`apparently` 与反证同句的结构未被打乱。
2. `:12`→`:15` 梦境段：`surfacing on a marsh shore in the moonlight`／`two yellow eyes glided toward me`／`A delicate, cold hand pressed into the center of my back, pushing me forward, and I took one step into the water. Another.`／`An impossibly large alligator raised its head`／`Water ran down its snout in rivulets as it opened its jaws, revealing jagged yellowed teeth`／`A deafening hiss whooshed toward me, growing louder and louder. I slammed my hands over my ears.` ✓——md:22 引文逐字、md:24 的四点判读（主语是眼睛、delicate 的并置、连动、孤句 `Another.`）全部成立。
3. `:18`→`:21` 醒来段：`My eyes flew open.`／`Adrenaline coursing through me, I held my breath until I was sure the hiss had disappeared with the dream.`／`Nothing out of the ordinary lay in wait for me.` ✓（md 未把「无异常」写成「确认安全」；`held my breath` 的「屏息直到确信嘶声随梦消失」保住条件）。
4. `:24` 梦的判读：`The dream had echoed Ida’s legendary hunt for Ironheart. So now I was facing alligators in my dreams as well as at work. Great.` ✓——引用与「梦里与上班都要面对鳄鱼」两处对应均对；**句式定性见 C-15-8，整改时只改「自问」二字，勿动 `:24` 引语与「Ironheart 传说」这条关联**。
5. `:27`→`:30` 起身段：`Then a step on the stair creaked, and the walls hummed with electricity.`／`Something pulled at me, drawing me out from under my covers.`／`The stairway banister faded as I reached toward it, my fingers meeting cold, smooth wood.` ✓——md:10 的「脚步／嗡鸣」两感与词表 `banister` 行例句逐字；**「天亮前」的时点问题只属 md:10 措辞（C-15-1），原文 :27 在 :21 与 :45 之间的悬空段这一事实不得被改写成别的序**。
6. `:33` 三级出场本体：`The smell came next: jasmine, slightly off. A concentrated perfume rather than the light scent of fresh flowers.`／`more a gauzy, black blur than anything`／`glided from the bottom of the stairs into the dining room, out of sight`／`All that remained was the faintest swish of a long, heavy skirt.` ✓——md:34 的嗅觉先于视觉、`glided` 与梦共用（F-15-5）、最轻声音配最重裙子三点均成立；**缺的是跨章气味前兆登记（C-15-6），补写时勿把 `slightly off` 译成「发酸」（那是 ch09 的词）**。
7. `:36`→`:39` 结论与呼救：`Someone must have broken into the house.`／`Clinging to the banister, hands suddenly slick with sweat, I screamed for help.` ✓（md:10「尖叫求救」；`must have` 是她的第一套解释，与 :33 的本能否决构成两拍，见 C-15-5 的补法）。
8. `:42`→`:54` 来人段：`“Dart?” Aunt Virginia called, rushing from the dining room into the entryway no more than fifteen seconds later.`（F-15-1）／`her white hair glimmered. I nearly crumpled to the floor with relief.`／`A woman I’d never met appeared behind her, peering over her shoulder.`／`“Dart, this is Lena.”… “She owns the cleaning service?”`／`She was wearing a bright red polo shirt; I would have noticed that, even in the dim light.`／`Both women shook their heads.`／`eyes settling on something behind me. I whirled around, hands raised to fend off whatever approached.` ✓——md:10「十五秒内来人带来的松气」与词表 `entryway` 行例句均有据；**三拨人并成一拨属 T-15-1（提示），整改时保持 :42 只有 Virginia 一人 `rushing` 这一事实**。
9. `:57`→`:60` Harrison 现身：`his hair slightly tousled, cheeks pink. Shirtless.`／`the line of golden hair trailing down his stomach and into a pair of long pajama bottoms dotted with squirrels`／`His skin was smooth and bronze, like a surfboard model’s.`／`Averting my eyes, I crossed my arms over my T-shirt, cursing myself for not throwing on a bra.` ✓——md:10「光着上身、穿松鼠睡裤」与 md:11「先移开视线、骂自己没穿胸罩」逐字对应；词表 `tousled` 行例句命中。
10. `:63`→`:69` 留宿问答：`“I stay in the spare room sometimes,” he said casually, managing to look slightly triumphant. “After late nights.”`／`“Late nights doing what?” I snapped. My fear seemed to stoke my annoyance.`／`“Checking the books,” he said, stuffing his hands into his pockets.`／`“Reviewing quarterly goals. Gazzie inevitably pushes some whiskey on me—you know how she is.”` ✓——md:10「查账、过季度目标、被灌威士忌」三件齐全，词表 `triumphant`／`inevitably` 两行例句逐字；**「其实我猜你不懂」半句缺失见 C-15-7，勿与 `you know how she is` 混为一句**。
11. `:75`→`:78` 心证两拍：独立成段的 `A surrogate grandson.`／`All those years I’d been alone with my mother, this man had been worming his way into my grandmother’s heart. No wonder she wanted him to inherit.` ✓——md:11「那些年独自陪妈妈的自己缺席时，正往外婆心里钻的人」对应 `worming his way`；md:44 引 `A surrogate grandson.` 作为「钉得更死」的下锤 ✓。
12. `:81`→`:84` 复述折扣：`“You’re sure you didn’t just see Lena?”`／`Swallowing the sting of pain, I refocused on the problem at hand.`／`“No,” I said, turning to peer down at her. “She wore something dark. A long skirt, maybe.”` ✓（md 未把「黑裙」写成她的确定记忆；T-15-4 只是建议把 `maybe` 点出来）。
13. `:87`→`:90` 噩梦问与摇头：`“Could it have been a bad dream?”`／`I shook my head.` ✓——F-15-2「不算升格」与此句一字不差；**原文即 `my head`，不得反向改成「人称滑移」类发现**。
14. `:93` 规律句本体：`Goosebumps covered my arms, refusing to subside as I rubbed them. The hum had quieted. Despite Aunt Virginia’s perfectly reasonable explanation, I only ever heard it before something odd happened. I wanted to buy her other explanations, too, but this was the second time I’d seen an inexplicable person in Greer House, and it was more difficult to explain away than a distorted reflection in bathwater.` ✓——md:52 引文逐字，四点判读（先打分再否决／`buy` 的交易隐喻／`the second time` 计数／`explain away` 的 away）全部有据；**「第二次」＝原文自数，与 md:90 的「第一次」性质不同，整改时只动后者**。
15. `:96`→`:99` Gazzie 与瞪视：`“Bull,” came Gazzie’s voice from behind Harrison and me, shortly followed by the woman herself, hair pulled back with its usual silver claw.`／`Aunt Virginia glared at her. “You be quiet.”` ✓（md:10「下楼只丢下一个 "Bull"」、md:13「瞪 Gazzie 一句 "You be quiet"」逐字；词表无该行，但块层未误引）。
16. `:102`→`:105` 离场：`had finished dressing for the day instead of checking on me. Unperturbed, buoyant even, she stepped around Harrison and me… strolled to the front door. She didn’t bother explaining herself.`／`giving me an infuriatingly calm shrug on the way—Aunt Virginia clapped her hands. “May as well get an early start.”` ✓（F-15-8 的两处写法不同但同一件事，判定成立）。
17. `:108`→`:114` 自我科学化与逃离：`I was imagining things, hallucinating. Maybe I’d accidentally inhaled lead paint in my bedroom? Or toxic mold in the file room?`／`“Why don’t we bike to the beach?” Aunt Virginia’s tone edged on desperate, but I appreciated the attempt at cheerfulness.`／`Can’t stay in Florida without visiting the beach. I think that might be illegal. Should be, anyway.`／`I agreed quickly, eager to leave Greer House and whatever peculiarities lurked within.` ✓——md:11「幻觉、铅漆粉尘、毒霉」三件齐全，词表 `hallucinating`／`peculiarities` 两行例句逐字；**T-15-6 只补 Virginia 的语气层，勿改动 `agreed quickly` 的既有表述**。

## 不许裁决（本章内）

- **黑裙影子的身份**：:33 只给气味、负形与裙声；:51 排除了 Lena（红 polo），:33 排除了 Gazzie 与 Virginia，:36 的「闯入者」与 :87 的「噩梦」两套都被当场否掉或存疑；文本从未给出第四套。**不得写实**。
- **推她入水的那只手是谁的**：:12 `A delicate, cold hand` 在梦里，:24 她只把它与 Ida 猎 Ironheart 的传说连线；不得与本章的黑裙影子、也不得与 ch09 浴房里的 stranger 合并成同一主体（三条线索原文互不指认）。
- **ch09 浴房的「陌生倒影」与本章的「无法解释的人」是否同一桩**：:93 只说「比浴水里变形的倒影难解释」，是**难度比较**不是身份同一；不得写成同一个存在两次现身。
- **嗡鸣与茉莉的成因**（电路／老宅／嗅觉幻觉，或超自然）：:27 与 :33 均未归因，:108 她自己的科学化清单里没有这两项。
- **Lena 的出现是否与她的排班冲突**：ch05:189 提到的排班口径（周二与周日）与本章清晨并不同一日，原文从未调和时间表；不得据此判 Lena 说谎或另有身份。
- **Harrison 实际留宿频率**：只有他自己说的 `sometimes`（:63）与她的 `probably … all the time`（:72）；不得裁决他是否常住。
- **Gazzie 那句 "Bull" 指的是什么**：:96 前一句是 Virginia 的问话还是 Harrison 的解释，文本未定；:99 的 `You be quiet` 与 :102 的 `Unperturbed, buoyant even` 都不构成解释。
- **她是否真的「有本事」看见前兆**：:93 的规律句（只在怪事之前听到嗡鸣）出自她的经验归纳，样本量与「怪事」的边界本章未给；不得据此判定她的感知力是设定还是心理作用。
