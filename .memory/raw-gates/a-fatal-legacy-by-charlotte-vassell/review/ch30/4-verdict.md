# 4-verdict · ch30《The Police Station》判定表

- 审查员：独立审查（只负责 ch30）
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch30_30.txt`（4,735 字符，83 行）
- 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch30 scott left a trail of coffee cups.md`
- 机器层：`bash scripts/chapter.sh "<md>" --json` → **退出码 0**（2-machine.json），quotes 6/6 逐字命中，segment_miss 0，struct_bad 0，keyword_bad 0，cjk_low 0
- 词汇层：`python3 scripts/check_vocab.py "<书目录>"` → FAIL 0；**ch30 无 WARN**（WARN 26 条全在其他章）；另独立核对 22 条例句，**22/22 在 text/ch30_30.txt 中逐字命中**

---

## 一、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 导航「人物弧线」：「**马特**……一句『附议』接住『凯厄斯的午餐是不是很色』」 | md:14 ↔ `text/ch30_30.txt:74`（字符 4123–4317）**‘Put a quid in the tin,’ Matt said, gesturing to the ‘bad joke jar’ on his desk.** 与 `text/ch30_30.txt:77`（字符 4320–4646）**‘Seconded. A new round of “Is Caius’s Lunch Wanky?” resumes on Monday too.’ Caius’s desk phone rang. He nodded along. ‘Absolutely. Send the details over to my DS…’ He put the phone down and looked at Matt.**（`text/ch30_30.txt:80` 4649–4712 才轮到 Matt 开口） | 「Seconded（附议）」的说话人是**凯厄斯**（同一段引语后紧接“Caius’s desk phone rang. He nodded along.”，答话用 “my DS”，挂断后“looked at Matt”，随后 Matt 才发问）；附议对象是马特刚投的那枚硬币，马特不可能附议自己。**md 把凯厄斯的台词记到马特名下** | **阻断** |
| A2 | 「十三袋垃圾」 | md:21 / md:25 / md:116 ↔ `text/ch30_30.txt:20`（41–511）`thirteen bin bags full of rubbish` | 与原文逐字一致（13 = thirteen） | 通过 |
| A3 | 「光第一袋就数出十六次尝试」 | md:21 / md:25 ↔ `text/ch30_30.txt:20`（41–511）`they’d counted sixteen attempts in the first bag alone` | 一致（16 = sixteen） | 通过 |
| A4 | 斯科特每班给出的杯子数量 | `text/ch30_30.txt:41`（1413–1496）`‘Yep, he was giving out exactly thirty cups per shift and recording the responses.’`；md 全篇 `/usr/bin/grep -n -oE "三十\|thirty" "<md>"` → 无命中（退出码 1） | md **没有写**这个数字（原文三个数量只承载了 13 袋 / 16 次；「三十杯/班」缺失） | 提示 |
| A5 | 「能与迪吉遇害现场残留指纹对上的完整指纹」 | md:21 ↔ `text/ch30_30.txt:20`（41–511）`finding a full print that matched the partials left at the site of Digby’s murder` | 归属方向正确：partials 是**迪吉现场留下的**，非「迪吉留下的」 | 通过 |
| A6 | 「写着斯科特地址的杯子」（优先搜） | md:61 / md:65 ↔ `text/ch30_30.txt:62`（3112–3273）`‘Amy, get forensics to prioritise the search for a cup with Scott’s address on,’ Caius said, closing the lid on Scott’s laptop.` | 一致，且主语方向正确（下令者＝凯厄斯，被指派者＝艾米，地址归属＝斯科特） | 通过 |
| A7 | 「马特桌上那罐『坏笑话』」 | md:15 ↔ `text/ch30_30.txt:74`（4123–4317）`gesturing to the ‘bad joke jar’ on his desk`（his = Matt） | 一致（注意与 A1 相邻但不是同一句，**勿连坐修改**） | 通过 |
| A8 | 「两桩命案在『都发生在第一次约会』上并到一起」 | md:11 / md:71 / md:120 ↔ `text/ch30_30.txt:68`（3447–3928）`Have a look though, and for men murdered on a first date too. That’s what Digby and Scott have in common.` | 一致 | 通过 |
| A9 | 「迪吉精心策划、斯科特机会性」 | md:71 ↔ `text/ch30_30.txt:68`（3447–3928）`‘Digby’s death had been planned out meticulously whereas Scott’s was opportunistic.’` | 一致 | 通过 |
| A10 | 马特追问「专门猎捕脆弱男人的连环杀手」 | md:14 ↔ `text/ch30_30.txt:59`（2962–3109）`‘By “something”, do you mean a spree killer on the hunt for vulnerable men?’ Matt asked.` | 一致（说话人＝马特） | 通过 |
| A11 | 艾米「回应少得可怜」 | md:14 / md:41 ↔ `text/ch30_30.txt:44`（1499–1623）`‘Which were few and far between?’ Amy said.` | 一致（原文为反问句，md 作引语式转述，不影响事实） | 通过 |
| A12 | 「杯子正躺在警局的物证袋里」 | md:57 ↔ `text/ch30_30.txt:20`（41–511）只写警方在翻检 `the crumpled napkins and soggy paper cups`，**无「物证袋 / evidence bag」字样** | 原文未写的场景细节（合理想象，非情节/关系/数字凭空出现） | 提示 |
| A13 | 「艾米翻杯子与记录」 | md:12 ↔ `text/ch30_30.txt:20`（41–511）翻检者原文为复数 `They were now poring over`；艾米的具体动作是派 uniform、说 `they’d counted sixteen attempts` | 概略归属，未与原文冲突 | 跳过 |
| A14 | 「在分部『A THURSDAY IN MAY』里」 | md:11；取证 `/usr/bin/grep -ril "thursday in may" text/` → 无输出，退出码 1；`/usr/bin/grep -rhoE "^[A-Z][A-Z ]{6,}$" text/` → 无输出（全书提取件内无分部标题行） | 语料内不可核（该说法来自原书结构，非本章提取件） | 跳过 |
| A15 | 原句 3 的「把回应写成数据」 | md:45 ↔ 引语 `text/ch30_30.txt:44`（1499–1623）只有 `write-up of his ‘experiment’` 与 `the outcome`；字面锚点 `recording the responses`（`:41`，1413–1496）、`graphs of his findings`（`:47`，1626–1694）在引语之外 | 分析覆盖的原文大于引语 → 引语选短（方向与数据均未错） | 提示 |
| A16 | 引语英文逐字（6 块，含省略号分段独立取证） | 2-machine.json `quotes` 全部 `ok: true`，`segment_miss 0`；`pos` 依次 25 / 490 / 1436 / 2069 / 2991 / 3447，与 `text/ch30_30.txt` 各行区间一一对应 | 6/6 逐字成立 | 通过 |
| A17 | 词汇例句（22 条）逐字 | 独立脚本比对 `text/ch30_30.txt`：**22/22 命中**（含截断例句 `‘Digby’s death had been planned out meticulously whereas Scott’s was opportunistic.`） | 全部成立 | 通过 |

---

## 二、四组数（只报这四组）

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **6/6 引语 + 22/22 词汇例句 + 3/3 已写出的数字（13 袋 / 16 次 / 1 枚地址杯）全部逐字成立；错 0** | 机器层 `segment_miss 0`、人工复核一致 |
| **对应** | **6 块：5 块对应 + 1 块对应偏弱（原句 3，引语选短）；不对应 0（无「讲全书主旨/作者生平」块）；施事/归属反转 0（块内）** | 详见 4-correspondence.md；块外的说话人错误见断言组 A1 |
| **形态** | **H1 `30. The Police Station` ✓｜导航 5 项（一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法）✓ 与本书众数同｜子项集 4 项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）✓｜块数 6** | **与本书众数无偏离**（`bookform.py`：本书 54 章，H1 写法 54/54 为「N.」；导航众数 5 项；子项众数 4 项；每章块数中位 7、范围 5–10 ⇒ 6 在区间内；profile mystery-thriller 块数 3–10 ⇒ 合规）**→ 无偏离，不需理由行** |
| **断言** | **逐条核对 17 条：通过 11、提示 3、跳过 2、阻断 1** | 阻断 1 条＝A1（说话人）；提示＝A4（漏「三十杯/班」）、A12（编「物证袋」）、A15（引语选短）；跳过＝A13、A14（语料内不可核） |

**阻断型条数：1**（A1）

**最要紧的一条**：**导航「人物弧线」把凯厄斯的台词「Seconded.（附议）」记到马特名下**（md:14）。原文该段说话人由紧邻叙述句锁死——`text/ch30_30.txt:77` 的引语之后是 “Caius’s desk phone rang. He nodded along.”，答话用 “my DS”，挂断后 “He put the phone down and looked at Matt.”，再往后 `text/ch30_30.txt:80` 才是 Matt 开口；而 “Seconded” 附议的又是马特刚投进罐里的那枚硬币，马特无从附议自己。四道机器探针（引语逐字 / 中文是中文 / 关键词成立 / 形态正常）全绿也照样漏掉这一条，只能靠 R4 的「谁说的」问句抓出。

---

## 三、已核实为正确（防误修，后续任何人不得以「读着不对」为由改动）

1. **md:51「他其实是想证明她有多会操纵人，才要他先跳过一圈『疯狂的圈套』才肯发生关系」** — 看似把「施事」写成斯科特要求**别人**跳圈套（方向反了），实为原文的第三转述：
   `text/ch30_30.txt:53`（字符 1928–2809）`Scott was trying to prove how manipulative she was by asking him to jump through all of these “crazy hoops” before he could have sex with her.`
   —— 原文 him/he 即斯科特本人（他在论坛上以第三人称写自己让**自己**跳过圈套，以证明她有多会操控人）；md 全块「他」一律指斯科特，方向与原文一致。**不要改成「要自己跳」。**
2. **md:15「马特桌上那罐『坏笑话』」** — `text/ch30_30.txt:74`（4123–4317）`gesturing to the ‘bad joke jar’ on his desk`（his = Matt，句子主语是 Matt said）。**与 A1 相邻但不是同一句，不要连坐改成「凯厄斯桌上」。**
3. **md:61「他说，看够了」** — `text/ch30_30.txt:62`（3112–3273）`closing the lid on Scott’s laptop. He’d seen enough for one sitting.`（He = Caius）。
4. **md:12「凯厄斯翻手机与论坛帖子」** — `text/ch30_30.txt:23`（514–931）`He had Scott’s phone in front of him.`；`:35`（1062–1377）`Caius had found a host of notifications in Scott’s emails…`、`Caius scrolled down through the chat`。
5. **md:14「马特往冷笑话罐里投一枚硬币」** — `text/ch30_30.txt:74`（4123–4317）`‘Put a quid in the tin,’ Matt said`（a quid = 一英镑硬币）。
6. **md:31「发给朋友的消息多半在聊电子游戏，看上去一切正常」** — `text/ch30_30.txt:23`（514–931）`There were a few messages to friends, mostly about video games. Those were seemingly normal.`
7. **md:41「她甚至不必看斯科特那份『实验』报告，就知道结果会是什么样」** — `text/ch30_30.txt:44`（1499–1623）`She didn’t need to see Scott’s write-up of his ‘experiment’ to know the outcome.`（write-up 归属＝斯科特，方向正确）。
8. **md:71「他让同事再查一查『死在第一次约会上的男人』」** — `text/ch30_30.txt:68`（3447–3928）`Have a look though, and for men murdered on a first date too.`：施事＝凯厄斯对警局团队的祈使，非「他让同事」以外的人，归属正确。
9. **md:120 一句话总结「把斯科特那只写着号码的咖啡杯翻出来当作追查的入口」** — `text/ch30_30.txt:53`（1928–2809）`He’d written his number on “the opportunity’s” cup.`；目标杯为写着地址的那只（`:62`）。两句各自有据，未把「号码杯」与「地址杯」混为一杯。

---

## 四、覆盖声明

- 本次审查**只覆盖 ch30**（`The Police Station`）。其余 53 章（含概述三篇 `00_*.md`、总览断言层）**未审**，不得据本报告推断全书无缺陷。
- 机器层覆盖：引语逐字（6/6）、块清单、形态、中文密度（6 块最低 cjk 比例 0.81，全部达标）、词汇例句命中（22/22）、词汇门禁（FAIL 0，ch30 无 WARN）。
- 人判覆盖：R1 素读 15 条事件 + 人物关系 + 数字/日期；R3 三张单子 8 条；R4 逐块三问 6 块；R5 断言 17 条。
- 未覆盖/未核：① 分部名「A THURSDAY IN MAY」语料内不可核（A14）；② epub 口径的「词是否 A 类虚构」判定（本书无 epub，check_vocab 已明示降级，不出结论）；③ 原书分页/页眉页脚信息；④ 全书级总览断言。
- 修复建议（供写作方参考，本审查方不改 md）：A1 改 `md:14` 的「附议」归属为凯厄斯，并让「接住『凯厄斯的午餐是不是很色』」这一动作落到正确的话轮上；A4 在原句 3 的中文理解或为什么这样写里补「每班正好三十个杯子」；A12 删「物证袋」或改成「正摊在警局的桌上」；A15 把 `text/ch30_30.txt:41` 那句纳入引语或补进中文理解。
