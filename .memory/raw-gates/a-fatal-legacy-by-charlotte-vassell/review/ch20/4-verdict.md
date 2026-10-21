# 4-verdict · ch20 独立审查判定表

- 审查范围：**仅 ch20**（`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch20 callie agrees to meet eulalia.md`）
- 权威源：`text/ch20_20.txt`（已与 epub `OPS/s032-Chapter-020.xhtml` 逐段比对，起止完整、无并章）
- 读取顺序守则：**先素读（只读 text/ch20_20.txt）→ 落盘 `1-suread.json` → 才开 md**（R1 已完成，见同目录 1-suread.json；15 条事件的字符区间经脚本逐条回验，锚点越界 0）
- ⚠️ **本目录原有一次未完成的前次审查**（只有 `1-suread.json` + `2-machine.json`，无 3-diff/4-correspondence/4-verdict）。本次**独立重做**了 R1（盲读）与 R2（重跑），前次的 `1-suread.json` 保留为 `1-suread.prev-run.json` 供对照——两份盲读在事件划分与关键结论上**一致**（互相印证，不构成自我豁免）
- 落盘纪律：只写本目录；**未改动书目录任何 md**；**未执行 git add / commit**
- 覆盖声明：**其余 53 章本次只有机器层结论，本次未做人判**，不得记作「通过」

---

## 一、四组数（只报这四组）

| 组 | 数 | 明细 |
|---|---|---|
| **逐字** | **28 / 28 全中，0 例外** | 6 个引语块全部为原文**连续子串**（自建脚本 `txt.find` + 连续性断言，6/6，区间见 3-diff §5）；词汇表 22 条例句逐条命中（22/22）。机器层：`chapter.sh` 退出码 0、`segment_miss 0`、`quote ok 6/6` |
| **对应** | **6 / 6 块成立** | 逐块判定见 `4-correspondence.md`：6 块的中文都在讲各自引语；**密度 6/6 达标**（每块有「为什么这样写」的机制层，无只复述字面的块）；**引语选短 1 处**（原句 2 首句讲了引语外的 setup 句 L53）→ 提示；**施事/归属反转 0 处**（3 问逐块核过） |
| **形态** | **0 阻断 / 1 提示偏离** | 见下节 §三 |
| **断言** | **25 条核查：5 阻断 / 6 提示 / 14 成立** | 见下节 §二 |

**阻断型条数：5**（A9–A13）。

---

## 二、断言判定表（| 断言 | 证据（章:区间） | 结论 | 档位 |）

| # | 断言（md 逐字） | 证据（`text/ch20_20.txt` 行:逐字） | 结论 | 档 |
|---|---|---|---|---|
| A1 | L10/L18 「十二周扫描的老话」「多数流产发生在十二周之前」 | L26 `‘The old adage is that you wait for the twelve-week scan because most miscarriages happen earlier than that.’` | 成立 | — |
| A2 | L18 「凯厄斯钻进被窝后问"我们什么时候能告诉别人"」 | L23 `‘Anything for you.’ Caius had got in under the covers with her after he’d come home. ‘When can we tell people?’` | 成立 | — |
| A3 | L28 「她是这一章里第一个把欧拉莉亚抬上桌的人」 | L56 `‘Bits and pieces from portraits,’ Callie said, sitting up. ‘I think that a sort of Renaissance-era portrait of Eulalia could be really interesting.’`（Eulalia 全章仅此 1 次） | 成立 | — |
| A4 | L38 「凯厄斯……只给了一句：你应该去跟乔治说」 | L59 `‘You should speak to Georgie.’` | 成立 | — |
| A5 | L48/L52 「她自己降格成速写」「维特鲁威人」 | L62 `‘Yes, I thought the same, but I doubt there’s time for a full-blown portrait. I love the idea of sketches. Not Vitruvian man exactly, but something along those lines.’` | 成立 | — |
| A6 | L10/L58 「塔比莎的咖啡邀约」「把短信读了两遍」 | L130 `18.13`；L135 `Hey Callie, it’s Tabitha! … Fancy a coffee this week? Would be great to catch up X`；L140 `Callie reread the message twice.` | 成立 | — |
| A7 | L62 「作者不肯让卡莉说出真正怕的是什么，只让她把两条理由并排交出来」 | L140 `She didn’t want to be rude, Tabs was a nice girl, but she also didn’t think it was wise to get sucked into that circle. ‘I’m not sure.’` | 成立 | — |
| A8 | L68/L72 「他觉得卡莉听到亚瑟·汉普顿眼下的动向也不是什么坏事」「替她下了结论："去见她吧"」 | L149 `‘There you go,’ Caius said, whisking the eggs together and adding them to the pan. It might not be the worst thing if Callie heard the odd account of Arthur Hampton’s goings-on. ‘Meet up with her.’` | 成立 | — |
| **A9** | L12 `末尾让丈夫替妻子说一句她本该自己说的话`；L24 `这段婚姻何时能被外人知道`；L72 `并不属于这段婚姻的理由`；L74 `才读得懂这段婚姻此刻的状态` | **本章无任何夫妻表述**（`/usr/bin/grep -nEi "husband\|wife\|marri\|engage\|boyfriend" text/ch20_20.txt` → 唯一命中 L38 `community midwife`，退出码 0）。**跨章反证**：`text/ch27_27.txt:98` `‘I take it that isn’t what it’s like with your boyfriend? He is your boyfriend, you’re not engaged, right?’`；`text/ch27_27.txt:100` `‘I refer to him as my “paramour” and he refers to me as his “missus”. It’s an equal partnership.’` | **不成立**：二人是男友/女友，**未订婚未成婚**（md 4 行共 5 处把「paramour / missus」写成「丈夫 / 妻子 / 婚姻」） | **阻断** |
| **A10** | L8 `卡莉在床上告诉凯厄斯自己怀孕了` | L23 `‘When can we tell people?’`（他问的是**何时告诉别人**，说明他早已知情）；L110 `‘Well, I did accidentally knock you up so it was the very least I could do.’`（他早知）。跨章：怀孕更早已成立——`text/ch15_15.txt:198` `‘Please may I have a pregnancy test?’`；`text/ch28_28.txt:41` `‘Callie’s pregnant, it’s too early to say anything but you’re chuffed and have chosen to tell me, Matt Cheung, …’` | **不成立**：本章没有「她告知他怀孕」这一事件，且本章主题恰是「什么时候才能说出口」——被写成「已经说了」是方向性倒错 | **阻断** |
| **A11** | L32 `提议不是"要不要去见她"，而是"给她画一张什么画"——见面这件事被包装成一件有交付物的作品` | 本章**无人提出去见 Eulalia**：Eulalia 全章仅 1 次（L56，画肖像的对象）；`/usr/bin/grep -nE "meet\|Meet" text/ch20_20.txt` → 唯一命中 L149 `‘Meet up with her.’`（**指 Tabitha**），退出码 0；L59 `‘You should speak to Georgie.’`、L62 `‘… I doubt there’s time for a full-blown portrait. …’` | **不成立**：把「画像提议」重写成「一次被包装的会面提议」——被包装的**会面**在本章不存在；且与本 md 自己的 L8/L117（只说「提画像的想法」）自相矛盾 | **阻断** |
| **A12** | 文件名 `ch20 callie agrees to meet eulalia`（含同名 symlink） | L149 `‘Meet up with her.’` 的 `her`＝Tabitha；本章无「agree to meet Eulalia」；跨章：`ch12 callie meets eulalia at tate.md`、`ch27 callie has dinner with eulalia.md` | **不成立**：slug 描述了本章没有的情节，且与 ch12/ch27 撞题材 | **阻断** |
| **A13** | L42 `全章里凯厄斯处理卡莉的每一个念头都走这条路径——不表态，只换路径。` | 反例 L29 `‘I see.’`（不表态也**不转介**）；L83 `‘Yeah. Definitely not baby Max. I quite like the name Charles. It’s solid. You can shorten it to Charlie. No nonsense.’`（**表态**）；L143 `‘Go, if you want to,’ Caius said as he cracked an egg into a bowl. ‘You like her, right?’`（**表态**）；L149 `‘Meet up with her.’`（**替她拍板**） | **不成立**：全称断言被 4 处反例推翻，且与本 md 自己的原句 6（「决定由他作出」）自相矛盾 | **阻断**（一句话可修） |
| A14 | L58 `她只给出三个字——"我不确定"` | L140 末句 `‘I’m not sure.’` | 部分不成立：中文「我不确定」是**四个字**（英文原句才是三个词） | 提示 |
| A15 | L9 `第三人称限知，全程贴着卡莉` | L149 `It might not be the worst thing if Callie heard the odd account of Arthur Hampton’s goings-on.`（Caius 内心，Callie 不知；md L72 自己写「叙述在此处插进来点明」） | 部分不成立：章末存在视角切换 | 提示 |
| A16 | L12 `用一道煎蛋把时间串起来（点菜、下锅、装盘）` | L149 `whisking the eggs together and adding them to the pan.`（止于下锅） | 部分不成立：无「装盘」描写 | 提示 |
| A17 | L12 `白玫瑰与速写本是仅有的两件道具` | L53 `a whole multipack of mythical animal meat in the freezer from Costco`；L128–135 手机与 Tabitha 消息（且是全章收束的载体） | 部分不成立：「仅有的」过绝 | 提示 |
| A18 | L8 `翻着速写本里给欧拉莉亚画像的打算` | L53 `Callie’s sketchbook had slid onto the floor. He picked it up. ‘What have you been drawing?’` | 部分不成立：无「翻」的动作（是滑落—被捡起—被问） | 提示 |
| A19 | 词汇表 `Mercenary \| 唯利是图的；势利的（这里带自嘲）` | L146 `‘Yeah, she’s nice. Plus she works in fashion so she may be useful at some point. Mercenary, I know.’` | 例句逐字成立；释义「势利的」对应 snobbish，与 mercenary 不同义 | 提示 |
| A20 | L10 「取名黑名单（讨厌的人、自己逮捕过的人、切尔西那边的人）」 | L77 `‘Mostly it’s a list of names to avoid. People I hated at school, people I’ve arrested, Chelsea players, you know. The worst people in the world.’` | 成立 | — |
| A21 | L9/L11 「客厅沙发上的白玫瑰」 | L98 `A large bunch of white roses had appeared on the coffee table.`；L101 `‘Are these for me?’` | 成立 | — |
| A22 | 词汇表 `omelette / unicorn / community midwife / blood test` 等例句 | L20 / L50 / L38 / L44 | 成立（22/22 逐字） | — |
| A23 | L10 「自己逮捕过的人」→ 凯厄斯是执法者 | L77 `people I’ve arrested` | 成立 | — |
| A24 | L10/L99 侧写「抽血和称重」「社区助产士」 | L38 `‘Yeah, I’ve got an appointment with the community midwife on Thursday.’`；L44 `‘I think they just do a blood test and weigh you or something.’` | 成立 | — |

> 分部归属一项计入**形态组**（§三 偏离 1），不重复计入断言数。

---

## 三、形态组（与本书众数 / profile 对照）

| 项 | 本章实测 | 本书众数 / profile | 结论 |
|---|---|---|---|
| H1 | `# 20. Caius and Callie’s Flat` | 写法众数 `{'N.': 54}`（54/54 章同形）；标题逐字等于源章节内小节标题 L17 `Caius and Callie’s Flat` | 无偏离 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 众数 5 项，**同名同序**（`bookform.py`：导航项众数＝这 5 项） | 无偏离 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | profile(mystery-thriller) 4 项，一致 | 无偏离 |
| 块数 | 6 | 本书中位 7，范围 5–10（profile 3–10） | 落在范围内，**无需写偏离理由** |
| 词汇条数 | 22 | 本书中位 27.5，范围 21–30 | 落在范围内（偏低端），无偏离 |
| **偏离 1（提示）** | md 全文**无「分部」标注** | 本书 **26/54 章**在导航写明「分部「A WEDNESDAY IN MAY」」等；本章属 epub `OPS/s027-Part-005.xhtml` = `TUESDAY`（覆盖 Chapter-016…020，本章为该分部末章） | **提示**：章内星期/分部信息缺失（书内惯例未过半，属弱偏离，不阻断） |

---

## 四、R5-补 · 「零命中」类断言的自证

本报告含「本章没有 X」的断言，凡属零命中者，一律给出命令与输出（`/usr/bin/grep`，显式文件路径，**不用 git grep**）：

```
/usr/bin/grep -c "Eulalia" text/ch20_20.txt                → 1；退出码 0
/usr/bin/grep -n "Eulalia" text/ch20_20.txt                → 56:‘Bits and pieces from portraits,’ Callie said, sitting up. ‘I think that a sort of Renaissance-era portrait of Eulalia could be really interesting.’；退出码 0
/usr/bin/grep -nE "meet|Meet" text/ch20_20.txt             → 149:‘There you go,’ … ‘Meet up with her.’（唯一一处，指 Tabitha）；退出码 0
/usr/bin/grep -nE "husband|wife|marri|engage|boyfriend" text/ch20_20.txt
        → 38:‘Yeah, I’ve got an appointment with the community midwife on Thursday.’（唯一命中为 midwife，非婚姻词）；退出码 0
/usr/bin/grep -n "Georgie" text/ch20_20.txt                → 59:‘You should speak to Georgie.’；退出码 0
```
（用 `-E` 交替匹配、显式路径；`text/` 被 `.gitignore` 排除，故不用 `git grep`。）

---

## 五、已核实为正确（防误修；后续任何人不得以「读着不对」改动）

| md 位置与逐字 | 原文逐字 | 为何是对的 |
|---|---|---|
| L18 `凯厄斯钻进被窝后问"我们什么时候能告诉别人"` | L23 `Caius had got in under the covers with her after he’d come home. ‘When can we tell people?’` | 说话人、动作、顺序均对 |
| L28 `凯厄斯从地上捡起掉落的速写本，问她在画什么` | L53 `Callie’s sketchbook had slid onto the floor. He picked it up. ‘What have you been drawing?’` | `He` 的先行词是 Caius，对 |
| L28 `她是这一章里第一个把欧拉莉亚抬上桌的人` | Eulalia 全章仅 L56 一次，说话人 Callie | 对 |
| L48 `卡莉说她也想到一块儿去了` | L62 `‘Yes, I thought the same, …’`（`the same` 指 L59 的转介） | 对 |
| L72 `它把她上一句「Mercenary, I know」那句自嘲，当成了她已经想通的证据` | L146 → L149 相邻 | 「上一句」指 L146，正确 |
| L8 `凯厄斯替她拍板：去见她` | L149 `‘Meet up with her.’` | **`她`＝塔比莎**（同句前半主语是「塔比莎的咖啡邀约」）⇒ **正确，勿误改成 Eulalia** |
| L117 `卡莉先说出给欧拉莉亚画像的想法，凯厄斯把它转手给乔治，卡莉又自己把它降成几张速写` | L56 → L59 → L62 | 对 |
| L12 `用一道煎蛋把时间串起来（点菜、下锅…）` | L20/L47/L53/L149 | 「点菜—下锅」链成立（只有「装盘」无据，见 A16） |
| 词汇表 22 条例句 | 全部逐字命中 `text/ch20_20.txt` | 对（22/22） |
| 6 个引语块 | 全部原文连续子串，无 `…` 缝合、无跨话轮拼接 | 对 |

---

## 六、最要紧的一条

**A11 + A12（同源）：md 与文件名把本章写成了「要不要去见 Eulalia」的章，而原文里根本没有这个议题。**
原文（`text/ch20_20.txt`）的事实是：Eulalia 全章只出现 **1 次**（L56，Callie 说「给 Eulalia 画一幅文艺复兴式肖像会很有意思」）→ Caius 不表态、只转介（`‘You should speak to Georgie.’` L59）→ Callie 自己降格为速写（`‘… I doubt there’s time for a full-blown portrait. …’` L62）。
而本章真正被「犹豫—岔开—替谁做决定」写出来的是**另一件事**：Tabitha 的咖啡邀约（Callie `‘I’m not sure.’` L140 → Caius `‘Go, if you want to’` L143、`Callie` 自己给理由 `‘Mercenary, I know.’` L146 → Caius 拍板 `‘Meet up with her.’` L149）。
md 的**正文分析其实抓住了这条真线**（原句 5、原句 6、一句话总结 L117 全对），但两处把它拧成了 Eulalia：文件名 `callie agrees to meet eulalia`，与原句 2 的「见面这件事被包装成一件有交付物的作品」（凭空引入「去见她」这个被包装的前提）。
⇒ 修法优先级：**先改文件名 slug**（如 `ch20 callie agrees to meet tabs`）与原句 2「为什么这样写」一句（把「去见她」改回「画不画这幅画」）；**不要**因此改动已经正确的原句 5、原句 6 与一句话总结。

次要紧：A9（丈夫/妻子/婚姻，全书 ch27:98/100 明确否认）与 A10（「在床上告诉凯厄斯自己怀孕了」，本章无此事）。

---

## 七、本次跑过的命令（供第三方复核）

```bash
python3 scripts/verify_corpus.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"      # PASS（FAIL 0 / WARN 3，与 ch20 无关）
bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch20 callie agrees to meet eulalia" --json > 2-machine.json   # 退出码 0
python3 scripts/check_vocab.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"       # FAIL 0；ch20 无 WARN
python3 scripts/bookform.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"          # H1/导航/子项/块数众数
python3 - <<'PY'   # 自建：6 引语块连续子串判定 + 22 条词汇例句逐字判定 + 每章词汇条数统计 + epub ch20 逐段比对
```
