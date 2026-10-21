# ch24 三张单子（漏 / 编 / 错）

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch24 benedict opens his basement.md`
> 唯一权威源：`text/ch24_24.txt`（7942 字符）
> 素读底稿：`1-suread.json`（R1 已落盘后才开 md）
> 机器层：`2-machine.json`（`chapter.sh --json`，退出码 0 / verdict ok）
> 档位：阻断 / 提示 / 假红 / 跳过

---

## 一、漏（素读有、md 无）

判据：关键事件或转折未出现（除非 md 写明取舍理由）。

| 编号 | 档 | 原文（逐字 + 位置） | md 侧 | 判定 |
|---|---|---|---|---|
| L1 | 提示 | `text/ch24_24.txt:98` "Caius stared around the space. **That much paper was highly flammable.** ‘You think the wannabe burglar came down here?’" | 7 个引语块无一引用；块4（`md:40`）谈地下室与「进来的人没有翻动任何东西」、块7（`md:58`）引献辞 "we lost to the flames"，两处都没有把「纸堆极易燃」这一伏笔与火／焚书连起来 | 伏笔漏引（**非情节转折，故不判阻断**）：这是全章唯一由 Caius 说出的判断性句子，且与末段献辞的 flames 构成现成的呼应，md 未接 |
| L2 | 提示 | `text/ch24_24.txt:44` "Stacks of books clung to the wall. One wobbled as Benedict walked past and a pile of **twelve hardbacks fell in front of Caius**." | 7 块无一引用；且 `md:40` 写「墙边的书堆还堆着」 | 明写的动作（十二本精装书当场塌在 Caius 面前）漏引；另与块4 的「书堆还堆着」冲突 → 另见 X2 |
| L3 | 提示 | `text/ch24_24.txt:131` "…her mother had told her that the lady who lived here before their family did, had **performed seances down here**." | 只在 `md:47`（块5 读者视角提示）以「降神会」三字带过，无块引用；块5 引语只到五芒星 | seance 来历（1973 年买下此房的老太太转述其母的话）只作一句提示带过，未落到任一引语块 |
| L4 | 提示 | `text/ch24_24.txt:98` "‘You think the **wannabe burglar** came down here?’" / `:101` "‘**Yes, like I said**, the basement door was open. I haven’t been down here in a while.’" | md 全章称「入室者／进来的人」（`md:11,40,52,107`），从不出现「冒牌窃贼」；Benedict「我下去过（那边有一阵子没下去）」这一自认也未出现 | 措辞/细节漏：原文用带引号的「冒牌窃贼」定性与「我有一阵子没下去」的自认，两处都能加固「不是为偷」这层，md 未用 |
| L5 | 提示 | `text/ch24_24.txt:95` "He turned the light on and started down the stairs. **He was still holding his drink.**" | 7 块未引；`md` 无「他手里还端着酒」 | 细节漏（可选） |
| — | 跳过 | `text/ch24_24.txt:50`（Oxfam £1 平装书）、`:56`（装沉思）、`:62/:71`（Fuck Martin Amis）、`:113`（Henry VIII / leasehold）、`:119/:125`（疯修女 / Booker）、`:143`（三十年手稿）、`:146`（999 / 指纹）、`:152/:155`（抽屉手稿 / 麻风病人 / 印度姐妹）、`:183`（贝母 / Callie / Regent's Park） | 块1–块7 的引语与词汇例句均已覆盖 | **不判漏**（已由引语块或词汇表覆盖） |

---

## 二、编（md 有、原文无）

判据：情节／关系／数字凭空出现。

| 编号 | 档 | md 侧（逐字 + 位置） | 原文侧 | 判定 |
|---|---|---|---|---|
| C1 | 提示 | `md:107` 一句话总结 "…后门与地下室的门都敞着，**家具**、书堆、**抽屉里的手稿一样没动**——" | 全文无「家具」二字（`text/ch24_24.txt` 室内陈设为书堆、chaise longue、battered armchair、扶手椅）；也**无任何一句写「抽屉没翻」**。可支持的只有：`:143` "They didn’t steal that from me."、`:137` "‘No, not that I’ve noticed.’"（= 没丢东西）、`:152` "all those manuscripts in the drawer"（抽屉里有手稿）、`:44` 书堆仍在 | 「没人偷东西」这一层有原文依据 ✓（本章专属判据达成），但**「家具一样没动」「抽屉一样没动」是原文没有的具体化**；属推断被写成场景观察 → 提示级，建议改为「一样东西也没被拿走」或补出可核依据 |
| C2 | 提示 | `md:12` 导航·视角 "随后在地下室**抬头**看见剥落的漆下露出的五芒星" | `text/ch24_24.txt:104` "‘What’s that?’ Caius asked, **looking at a mark on the wall** revealed by a layer of paint peeling away." | 「抬头」是原文没有的动作（原文只说看墙上痕迹）→ 提示级措辞添加 |
| C3 | 提示 | `md:47` 块5 读者视角提示 "**房东**对这符号有另一套来历，把它归给前住户做过的降神会。" | `text/ch24_24.txt:131` 说话人是 **Benedict**（房主本人），"I was told by the old lady I bought the house off in 1973" | 说话人没错（Benedict 说的），错在**称谓**：Benedict 是自住房的 leasehold 持有人，**真正的地主是那位朝臣的后代**（`:113` "His descendants still own my fucking leasehold."）→「房东」用错 → 提示级（详见 X3） |
| C4 | 提示 | `md:59` 块7 读者视角提示 "碑上所献的 Alice **正是**房东口中那位被当作女巫烧死、据说能看见异象的修女。" | `text/ch24_24.txt:171` 铭牌只写 "For Alice and all the other women philosophers that we lost to the flames"；同章 `:119` "the madwoman they executed"、`:125` "some nun who had visions" —— **本章从未把 Alice 与那位修女连起来，也未说她是「philosopher」** | 断言在本章**无依据**（属编）。但**跨章可证**：`text/ch33_33.txt:283` "One of the priory’s most infamous inhabitants was **Alice de Burge**. She was a young nun … supposedly blessed with **prophetic visions** … **burnt at the stake for heresy in 1532**"；`text/ch48_48.txt:262` "‘It could be **Alice de Burge**? The nun who was burnt for heresy … **The one with the blob statue in the middle of the square**.’" ⇒ 断言本身与全书一致，只是本章内未建立 → 提示级（宜改为「也许就是」），并已列入「已核实为正确」防误修 |
| — | 跳过 | `md:46` 块5 "全案头一个画出来的符号" | 跨章断言 | 已取证成立 → 见「已核实为正确」 |

---

## 三、错（两边都有但不一致）

判据：主语、因果、数字、时序。

| 编号 | 档 | md 侧（逐字 + 位置） | 原文侧（逐字 + 位置） | 判定 |
|---|---|---|---|---|
| X1 | **阻断** | `md:11` 导航·一句话概括 "Caius 第三次按响 Benedict Carr-Ridge 城里住宅的门铃，**第四次才被放进屋**"；`md:13` 导航·线索结构 "门铃与矛头栏杆（**按到第四次才进屋**）"；`md:107` 一句话总结 "Caius 第三次上门、**第四次才进得去**的那间屋子里" | `text/ch24_24.txt:20` "For the third time Caius rang the doorbell … **He rang for a fourth time.**" → `:23` "‘What the fuck do you want?’" → `:29` "**He slammed the door shut.**" → `:32` "**Caius rang the doorbell again.**" → `:35` "He looked **through the letterbox** at Caius" → `:41` "**He swung the door open** to reveal himself … beckoning him in." | **数字/时序错**：第四次按铃**没有**让他进屋——第四次按铃后被骂并摔门，Caius **又按了一次**（第五次），经信箱口对话后 Benedict 才开门。md 三处把「第四次」与「被放进屋」绑在一起，与原文动作序列不符，且与 md 自己的块1 中文理解（`md:20` "他按响了第四遍"，正确）自相矛盾 |
| X2 | 提示 | `md:40` 块4·为什么这样写 "进来的人没有翻动任何东西——**墙边的书堆还堆着**，抽屉里的手稿原封未动"；`md:15` 导航·叙事手法 "（**书堆原样**、稿子原封、后门与地下室的门都敞着）" | `text/ch24_24.txt:44` "One wobbled as Benedict walked past and a **pile of twelve hardbacks fell in front of Caius**." | 「书堆原样／还堆着」与原文「一堆十二本精装书当场塌在 Caius 面前」有张力。原文没有说书堆是否被翻动过（塌落发生在 Benedict 自己走过时，非入侵者所为）⇒ 提示级，建议改为「墙边的书还在」或删去「原样」 |
| X3 | 提示 | `md:11,47,59` 共 3 处 "**房东**"（`md:11` 导航·一句话概括 "**房东**说夜里醒来见到一张白得像死亡的脸"；`md:47` 块5 读者视角提示；`md:59` 块7 读者视角提示 "**房东**口中那位被当作女巫烧死…的修女"） | `text/ch24_24.txt:131` "I was told by the old lady **I bought the house off** in 1973"（他买下此房）；`:113` "**His descendants still own my fucking leasehold**"（地主是朝臣后代） | 称谓与原文关系不一致：Benedict 是**自住房的租赁产权持有人**，不是出租方。同一 md 的 `md:15` 又用了「主人」，本书他章用「屋主」（`ch22:34,35`）或「房主」（`ch54:13,15`）→ 提示级，建议统一为「房主」 |
| X4 | 提示 | `md:32` 块3·中文理解 "他又睡过去，心想这回**杜松子酒大概不合身了**" | `text/ch24_24.txt:77` "I fell asleep again thinking that **unusually the gin hadn’t agreed with me**." | 语义误译："hadn't agreed with me" =「这酒（这回）不对劲／不服身」，"不合身"（尺寸不合）属直译走样 → 提示级 |
| X5 | 提示 | `md:26` 块2·中文理解 "「哦，**一位警司**。」" | `text/ch24_24.txt:38` "‘**DI** Caius Beauchamp.’"（DI = Detective Inspector） | 职级渲染与本书不一致：全书他章一律作「警探」（`ch21:11,51,52,99`、`ch34:11`、`ch37:12`、`ch41:14`、`ch46:24`、`ch52:85`、`00_概述:60`），且中文语境「警司」通常指 Superintendent → 提示级 |
| X6 | 提示 | `md:11` 导航·一句话概括 "晨起后后门大开、地下室的门也在晃，可屋里没有一样东西被拿走，**被打开的只是通往地下室的那道门**" | `text/ch24_24.txt:83` "I woke up in the morning and **my back door was wide open** … but **it was flapping about and so was the door to my basement**." | 自相矛盾：同一句里已说「后门大开」，又说「**只是**通往地下室的那道门」被打开；原文是**两扇门都开着**（后门可由「我总忘锁」解释，地下室门才是反常）→ 提示级，建议改为「唯一反常的是通往地下室的那道门」（同 md 的 `md:107` 写「后门与地下室的门都敞着」是对的） |
| X7 | 提示 | `md:28` 块2·为什么这样写 "于是警察在他眼里**先是同道**，不是麻烦" | `text/ch24_24.txt:41` "‘**I am important.** Oh **and** a detective who reads quality literature. Well, I never. I suppose you may enter.’" | 原文顺序是「先摆自己的重要地位，再提对方读不读得出好东西」；md 的「先是同道」把次序倒置 → 提示级（措辞，不影响施事归属） |

---

## 四、R2 机器层与人工层的分工核对

| 项 | 机器（`2-machine.json`） | 人工 |
|---|---|---|
| 引语逐字 | 7/7 `ok:true`；人工独立复核 7/7 在原文中**连续存在**、无 `…` 拼接 | 通过 |
| 块数 | 7（`blocks:7`） | 通过 |
| 形态 | `h1_shape_ok:true` / `nav_count:5`（`nav_counts:[5]` = 本书每章均 5）/ `subitems_modal` 4 项 = profile `mystery-thriller` 4 项 / `blocks:7` = `block_median:7.0`（`block_range:[5,10]`） | 无偏离 |
| 中文密度 | 7 块 `cjk_low:0`、`keyword_bad:0`、`struct_bad:0`、`empty_quote:0` | 通过 |
| 词汇例句 | 机器未覆盖 | 人工全量复核 27/27 例句在 `text/ch24_24.txt` 中逐字命中（`3-diff.md` 之外另记） |
| 机器查不了 | — | 漏 L1–L5、编 C1–C4、错 X1–X7 全部由人工出 |

**结论**：机器层（逐字 / 形态 / 密度）全绿，但**机器绿 ≠ 无缺陷**：本章唯一一处**阻断**（X1「第四次才被放进屋」×3 处）恰好落在机器四道探针都照不到的地方——它是导航/总结层的中文转述，不是引语，中文语法完全正确。
