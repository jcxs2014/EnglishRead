# ch08 判定表（R5）· A Fatal Legacy

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch08 callie opens the neon pink box.md`
> 唯一权威源：`text/ch08_8.txt`（4568 字符，43 行）
> 审查员：独立审查（先素读 `1-suread.json`，后开 md；机器层 `2-machine.json` 退出码 0）
> 档位四选一：**阻断 / 提示 / 假红 / 跳过**

---

## 一、四组数（只报这四组）

| 组 | 分子/分母 | 结果 | 说明 |
|---|---|---|---|
| **逐字** | 6 引语块 / 6 片段 | **6/6 ✅ 命中** | 机器层 `chapter.sh --json`：「引语块 6，片段 6，查无 0」。独立复核（自写 Python，逐条 `str.find`）：6 条引语在 `text/ch08_8.txt` 中**全部命中且为单段连续区间**，无省略号、无跨段缝合。6 条引语在**原始 txt** 的区间＝[58,327]、[645,903]、[1697,1881]、[2301,2546]、[3207,3385]、[4440,4565]（注：`2-machine.json` 里的 `pos` 41/626/1671/2266/3161/4384 是**归一化后**（`lib.text.norm`：去引号、压空白）的偏移，两者口径不同，均已复核对上）。词汇表 19 条例句亦逐条命中本章（0 miss）。 |
| **对应** | 6 块 | **4 块成立 / 2 块阻断**（块 4、块 6） | 0 块密度不足、0 块讲全书主旨/作者生平；1 块引语选短（块 2，提示级）。详见 `4-correspondence.md`。 |
| **形态** | H1 / 导航 / 子项集 / 块数 | **✅ 全部合规，0 偏离** | H1＝`8. Caius and Callie’s Flat, Tufnell Park`（与 `text/ch08_8.txt:17` 的小标题逐字一致，且用本书通行的 `# NN. 标题` 形态）；导航 5 项＝本书众数 5（54/54 章同名同序：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法）；子项集＝`中文理解 / 关键词 / 为什么这样写 / 读者视角提示`，与 `docs/rules/genre-profiles.json` 的 mystery-thriller profile 一致；块数 6＝本书中位 7.0（范围 5–10），**在众数范围内，无需理由**。 |
| **断言** | 逐条核 | **5 条与原文不符（阻断）、10 条措辞/指代（提示）、3 条通过** | 全部带 `text/chNN:行` 与原文逐字，见下表。另有 **5 条「已核实为正确」** 护栏（第五节）。 |

**阻断型条数：5**（3-diff 记 5 条阻断：L1、L2、C1、W1、W2；W1 的三个 md 落点算 1 条根因）

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 导航「一句话概括」：「她按对方邮件给的时间地点动身，**去赴一场由别人安排好的会面**」；「一句话总结」：「临出门，她按那封只有时间地点的邮件走出门」；块 6 读者视角提示：「**这趟出门**不是去认识一个人，而是去扮演一个早已熟悉对方作品的人」 | `text/ch08_8.txt:42`（区间 [4133,4184]）："She was off to **brunch with her old neighbour Innogen**." ／ `text/ch08_8.txt:39`（区间 [3207,3385]）：邮件只给 "a where and when"，会面尚未发生（`text/ch12_12.txt:17` "Tate Britain" 才是会面现场） | 本章结尾的出门是**去老邻居 Innogen 那儿吃早午餐**；与欧拉莉亚的会面是**下一章的事**。md 把它改写成「去赴会面」，并据此推出「这趟出门是去扮演一个熟悉对方作品的人」。**三个落点同一根因**（`md:11`、`md:13`、`md:77`、`md:123`） | **阻断** |
| 2 | 块 4 读者视角提示：「这正是下一句「完全不知道她在说什么」的根因：**卡莉听不懂**的不是词，是这套把一切都拉平的逻辑」 | `text/ch08_8.txt:34`（区间 [3032,3068]）："**I have no idea what any of that meant** but Eulalia is the most disturbingly beautiful woman I have ever seen. You're going to go feral when you finally get to see her too." ／ 框文首句 `text/ch08_8.txt:28`（区间 [1887,2249]）："…**When I asked** how her burgeoning stardom felt…" ／ `text/ch08_8.txt:23`（区间 [1813,1880]）："Callie laughed as she read **her** most recent interview **in the Observer**" ／ `text/ch12_12.txt:20`："She still had **no idea what Eulalia bloody looked like**." | 框文第一人称是**《观察家报》的采访者**，不是卡莉（卡莉是**读者**：read … in the Observer；且本章她还没见过欧拉莉亚，不可能说「I've ever seen」）。md 把那句反应安到卡莉头上 = 施事/归属反转。另称它是「下一句」也不准：中间隔着欧拉莉亚那段话的其余约 485 字符 | **阻断** |
| 3 | 导航「人物弧线」：「从捡起箱子时那一瞬「它.From哪儿来的」的**隐约警觉**，到认出它不过是自己的旧订阅」 | `text/ch08_8.txt:20`（区间 [58,326]）："Callie picked up a small cardboard box from the floor in the hallway. It had been shoved up against the wall behind the front door. **The neon-pink box was from** an online female hygiene subscription service that she'd signed up for and meant to cancel but kept forgetting." | 原文里她**立刻**认出是自己订的订阅，全程无起疑、无「它从哪儿来」的念头。且与 md 自己的块 1「为什么这样写」自相矛盾（那里写的是「这层悬疑感就被**她自己拆掉**」）。凭空加主角内心动作 = 编 | **阻断** |
| 4 | md 全章无「经期迟到一周／怀孕」这条线（导航自称「**四样东西串起这一章**」，人物弧线、一句话总结也全无） | `text/ch08_8.txt:20`（区间 [1298,1569]）："She hated to admit it but **Caius had been right, she was bloody due**. Any day now. Actually, probably yesterday. She’d been so tense over her television appearance that she’d probably skipped it. She looked at the calendar on her phone. **She was late by a week.** It must have been the stress of Chelsea." | 关键转折未进 md，且 md 无取舍理由。md 侧取证：`/usr/bin/grep -nE "怀孕\|例假\|生理期\|月经\|晚了一周\|迟到\|宝宝\|Caius\|凯厄斯" "ch08 callie opens the neon pink box.md"` → 唯一命中是 H1 里的 `Caius`（md:7），正文 0 命中；退出码 0。该线是本书 ch15／ch27／ch28 的伏笔 | **阻断** |
| 5 | md 全章无「出门去吃早午餐／Innogen」这条线（正文分析、导航、总结皆无） | `text/ch08_8.txt:42`（区间 [4133,4184]）："She was off to **brunch with her old neighbour Innogen**. Innogen’s mother had been an actress and had insisted on giving her the correct form of the name and not the printer’s mistake in the First Folio." | 同样只出现在词汇表例句（md:115–116），分析层零覆盖。md 侧取证：`/usr/bin/grep -nE "brunch\|Innogen\|早午餐\|英诺根" "ch08 callie opens the neon pink box.md"` → 命中 md:115、md:116 两行词汇表；退出码 0。本章最后一个动作被抽掉，整章收尾失真 | **阻断** |
| 6 | 块 2「为什么这样写」：「慈善之所以成立，是因为对彼得来说**这笔买卖划算**」 | 原文在**引语外**：`text/ch08_8.txt:20`（区间 [905,975]）"**She suspected that** that was because it could be **societally advantageous** for the old git now that he'd lost his footing after stepping down from Parliament and his acrimonious divorce."（本块引语止于 [903]） | ① 分析依据在引语外 ⇒ 引语选短（退回创建卡 §2 ①；解法＝把引语延到 [975]，或把分析改写为只谈引语内的 "hadn't taken much convincing"）；② 原文是**卡莉的怀疑**，md 写成客观因果断言 | 提示 |
| 7 | 块 1「为什么这样写」：「箱子**不是被送来的**，是被推进来、抵在墙角的」 | `text/ch08_8.txt:20`（区间 [329,417]）："For a small fee **they sent her a package in the post** every month of organic cotton tampons"；同句前文 "It had been **shoved up against the wall** behind the front door"（被动，无施事） | 原文明写是**寄来的**；md 自己的块 1 读者视角提示也写「只是一份被忘掉的**月度订阅**」——同一块内自相矛盾。措辞层（未污染情节），可改 | 提示 |
| 8 | 导航「线索结构」把出门的妆造算成「为**赴约**做的一整套功课（…镜子前的口红）」 | `text/ch08_8.txt:42`（区间 [4033,4085]）："Taking out a soft matte lipstick in a warm rosy shade, she applied it in the mirror in the hallway." | 原文未把口红与赴欧拉莉亚的会面挂钩（她出门是去早午餐）。与 #1 同根，单独记一条以便改时不漏 | 提示 |
| 9 | 块 3 读者视角提示：「这声笑标出她此刻的位置：她在门外，**是写稿的那个人**」 | `text/ch08_8.txt:23`（区间 [1813,1880]）："Callie laughed as she read her most recent interview in the Observer" | 主语连读成「卡莉＝写稿的人」就与原文（她是读者）、也与 md 自己的块 3 中文理解（「卡莉**读到**…」）冲突。指代含混，宜改写为「写稿的是《观察家报》那位」 | 提示 |
| 10 | 块 4「为什么这样写」：「**作者把它原样引出来，不加一句评语**」；且全段以「**名气**」为拆解对象 | `text/ch08_8.txt:31`（区间 [2255,2300]）："‘**Fame? What is fame? Am I famous? Am I a star?** I don’t have my own gravitational pull. …"；`text/ch08_8.txt:34`（区间 [3032,3068]）："I have no idea what any of that meant…" | ①「名气」主题落在本块引语（[2301,2546]）**之外**；② 紧接其后**确有**一句评语，md 说「不加一句评语」与原文相抵。两处都在块 4 内部，提示级 | 提示 |
| 11 | 块 5 读者视角提示：「对方给的**这两条**，卡莉一条不落地照办：**连欧拉莉亚巡演戴过哪些头套都查了个遍**，地铁上还准备把对方的新专辑听熟」 | 邮件要的两条在 `text/ch08_8.txt:39`（区间 [3322,3384]）："All they asked her to bring was **her sketch pad and an open mind**"；头套在 [3417,3495]、专辑在 [4440,4527]，**都在本块引语（止于 3385）之外**，也不是邮件要的那两条 | 指代错位 + 例证跨块。提示级 | 提示 |
| 12 | 块 2 读者视角提示：「这二十条卫生巾与上一段那只粉盒子**是同一件事**」 | `text/ch08_8.txt:20`（区间 [740,769]）："all she was doing was **sending them twenty tampons a month**"（寄给那批女工的）vs 区间 [268,326]（她**收到**的月度订阅） | 收的 ≠ 寄的，是同一订阅机制的两端而非同一件东西。措辞级 | 提示 |
| 13 | 导航「一句话概括」末段：「查清她巡演戴过的头套」 | `text/ch08_8.txt:39`（区间 [3417,3495]）："She’d also found a blog where a superfan had detailed **all of the heads that Eulalia had worn on her last tour**" | 「查清」略强（她只是读了一个粉丝博客的汇总），但不涉事实错误 | 提示 |
| 13b | 导航「视角」：「场景是 Tufnell Park 这套公寓里的**一个上午**——**门厅、书桌、玄关**」 | `text/ch08_8.txt:42`（区间 [4133,4184]）唯一时段锚点 "She was off to **brunch**"（brunch 跨正午）；区间 [1574,1640] "sat down at her **laptop**"、区间 [3866,3915] "got up from the **table**"（是桌子非书桌）；区间 [4033,4085] "applied it in the mirror in the **hallway**"（仍在走廊非玄关） | 场景措辞三处微偏；「门厅」✓、「一个人也没有」✓ 属实（框文是纸面文字，非出场人物）。不涉情节 | 提示 |
| 14 | 词汇表：19 条例句全部逐字取自本章；「printer」释义作「印刷所；印刷工」 | 逐条 `str.find` 复核：19/19 命中，0 miss；`python3 scripts/check_vocab.py "<书目录>"` → `--- FAIL (0) ---`、该章 0 条 WARN（全书 26 条 WARN 全在别的章） | 词汇层无缺陷 | 跳过（通过） |
| 15 | 章节专属判据「她已经开始按对方给的方式准备自己」 | `md:27`（块 1 读者视角提示）："真正被安排好的是另一件事——欧拉莉亚那边给了她一个时间和一个地点，要她带上速写本和一颗开放的心。**她已经开始按对方给的方式准备自己。**" ／ `md:67`（块 5 读者视角提示）："**她在按对方给的方式准备自己。**" | 判据要求的两处「读者视角提示」都点到了，**满足** | 跳过（通过） |
| 16 | 判据前提「粉盒里是一张专辑」「她把它当成一次被安排的接触」 | `text/ch08_8.txt:20`（区间 [190,417]）：盒内是 "a package in the post every month of **organic cotton tampons**"；Callie 立刻认出是**自己忘了退订**的订阅，md 也写成「那其实是一份她忘了退订的卫生巾订阅」（`md:11`） | **判据前提本身与原文不符**（盒里是卫生巾，不是专辑；她也不把它当「被安排的接触」）。md 在这点上**忠于原文**，不判缺陷。专辑是另一件事——《Burn Bright》，她在地铁上循环听（区间 [4440,4527]） | 跳过（前提不成立） |
| 17 | 「分部 A SUNDAY IN MAY」 | `/usr/bin/grep -rIn "A SUNDAY IN MAY" text/` → 0 命中，退出码 1；epub `OPS/toc.ncx` 展平后分部名为 `A FRIDAY IN MAY / SATURDAY / SUNDAY / MONDAY / TUESDAY / WEDNESDAY / THURSDAY / FRIDAY / SATURDAY / MONDAY / TUESDAY / SIX WEEKS LATER`，ch08 落在 **`SUNDAY`** 这一分部（Part-003，其后依次是 ch08/09/10，再进 MONDAY） | 「A SUNDAY IN MAY」在原文与 epub 里**都不存在**（epub 写的是 `SUNDAY`）。但这不影响本章：md 与本书 ch01–ch12 一致地**不在导航里写分部名**（`/usr/bin/grep -l "分部" *.md` → 26/54 章有，ch01–ch12 除 ch02 外均无；ch02 的「星期六」是叙事日不是分部名）。故 md 缺分部名**不构成形态偏离** | 跳过（前提不成立／无偏离） |
| 18 | 机器层结果 | `bash scripts/chapter.sh "…/ch08 callie opens the neon pink box.md" --json` → 退出码 **0**，`verdict: ok`，引语查无 0、块结构/中文密度/形态三段全绿 | 机器层四道探针对本章**无告警**——本章的 5 条阻断全部落在机器结构上查不了的五类（漏 / 对应 / 说话人 / 施事归属 / 事实断言），与 `docs/rules/生产-审查对照.md` 预期一致 | 跳过（工具正常） |

---

## 三、形态组（按 R5 要求逐项写明）

| 项 | 本章实际 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 8. Caius and Callie’s Flat, Tufnell Park` | 54/54 章均为 `# NN. 标题`；本章小标题逐字等于 `text/ch08_8.txt:17` | 无 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 同上 5 项，54/54 章同名同序 | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | `genre-profiles.json` 的 mystery-thriller：同 4 项（＋optional「句子结构」未用） | 无 |
| 块数 | 6 | 中位 7.0，范围 5–10 | 无（在范围内，无需理由） |
| 分部名 | 未写 | 本书 26/54 章写，ch01–ch12 基本不写 | 无（本章属 ch01–ch12 段，与同段一致） |
| 词汇表位置 | `## 精读` 之后、`## 一句话总结` 之前 | 创建卡 §0.5 固定 | 无 |
| frontmatter | `状态: 未读` / `modified: "2026-10-20"` / `source_text: ch08` | 54/54 章同形 | 无 |

**形态组结论：0 偏离，不需写理由行。**

---

## 四、已核实为正确（防误修，固定一节）

以下写法**看着像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动：

1. **块 1/块 4 的引语从长句中间起、到长句中间止**（块 1 起于 "Callie picked up…"，块 4 起于 "I don’t have my own gravitational pull…" 而非 `‘Fame? What is fame?`）——`text/ch08_8.txt` 中这些就是**单段连续区间**（[58,327]、[2301,2546]），非缝合、非省略号。机器层 6/6 逐字命中佐证。**勿**为「补全成整段」而改动引语（那会引入原书没有的引文边界）。
2. **块 4 的中文理解把这段判为欧拉莉亚的话**——正确：`text/ch08_8.txt:31` 该段带单引号，是欧拉莉亚对采访的回答。**勿**因 #2（归属错）而把说话人改掉；要改的是**读者视角提示**那一行。
3. **块 3 的引语从 "Most of them were ridiculous." 起**（原文 [1697,1881]）——`text/ch08_8.txt:23` 的整段从 "Callie walked back into the living space…" 起，md 只截了后半段（前半段 "She'd been reading past interviews Eulalia had given." 未入引语），但这不构成拼接或改写。**勿**为「补全引语」而动。
4. **原文 epub 的 `OPS/s018-Chapter-008.xhtml` 在 `…Eulalia had given.` 与 `Most of them were ridiculous.` 之间带一个 `pagebreak-rw` 页码 span（"55"、"56"）**（见 epub 原始 markup：`…Eulalia had given. <span class="pagebreak-rw" epub:type="pagebreak" id="pagebreak-rw_55">55</span>Most of them were ridiculous.`）。**但提取后的 `text/ch08_8.txt` 已把该 span 剥掉**——取证：`/usr/bin/grep -nE '(^|[^0-9])55([^0-9]|$)' text/ch08_8.txt` → 0 命中，退出码 1；`56` 同。⇒ **本章语料无页码 bleed，不是缺陷**（`python3 scripts/verify_corpus.py` 的 bleed 告警指向的是 ch23，不指向 ch08）。**勿**把 epub 的页码 span 误当成本章语料污染。
5. **块 4 的 md 引语起于 `I don’t have my own gravitational pull.`（原文 [2301]），而 `‘Fame? What is fame? Am I famous? Am I a star?`（[2255,2300]）落在引语之外**——这不是错引（引语是单段连续区间，机器层 6/6 命中佐证），只是**边界选择**：分析里用的「名气」一词因此在引语外（见判定表 #10 提示）。**勿**以「引语截短」为由判定此条为错引。

---

## 五、覆盖声明与复现

- **本次只审 ch08**。本书其余 53 章 **未审**——不得据此书的其他章判「通过」。
- 机器层已跑：`bash scripts/chapter.sh "<章 md>" --json`（退出码 0，产物 `2-machine.json`）；`python3 scripts/check_vocab.py "<书目录>"`（FAIL 0）；`python3 scripts/verify_corpus.py "<书目录>"`（P0-0 PASS，3 条 WARN 分别指向「未给 --expect」「ch23 页码 bleed」「未给 --anchors」，**均不指向 ch08**）。
- 复核者可复现的命令与输出已随本文件给出（每条断言带 `text/chNN:行` + 原文逐字 + 字符区间；「零命中」类断言附原命令、输出与退出码，见 #4、#5、#16、#17）。
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch08/`（本会话只写此处；未改书目录任何 md，未执行 git add/commit）。
