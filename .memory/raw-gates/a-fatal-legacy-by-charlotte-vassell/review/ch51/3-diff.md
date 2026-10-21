# 3-diff · ch51 三张单子（漏 / 编 / 错）

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch51 caius runs in the park.md`
- 唯一权威源：`text/ch51_51.txt`（4311 字符，行号见下）
- 读取顺序：R1 素读（只读 text）→ 落盘 `1-suread.json` → 才开 md；R2 机器层 `chapter.sh --json` 退出码 0（6/6 引语逐字 ✅）
- 本文件只收**机器查不了**的五类：漏 / 编 / 错 / 说话人 / 施事归属 / 事实断言
- 档位：**阻断**（与原文不符或缺失）／**提示**（措辞可商榷，记录不建议改）／**假红**／**跳过**

---

## 一、漏单（素读有、md 无）

| # | 素读内容（原文逐字） | md 状况 | 档位 | 说明 |
|---|---|---|---|---|
| L1 | `text/ch51:32` "‘Callie’s being a bit funny about work following me home. Now everything has sunk in, Eulalia turning up like that has made her feel vulnerable.’" ／ `text/ch51:35` "‘I get that, especially with her history.’" | 精读分析层**未收**此拍；仅在词汇表以例句形式出现（`vulnerable` 条） | 提示 | 这是全章唯一推进卡莉线的拍（Eulalia 出现→她觉得脆弱→Caius「尤其是考虑到她的过去」）。6 块选样可取样，不构成阻断；但它与 L113 "‘She’s fine,’ Caius said quickly"（他对父亲报「她没事」，说得很快）构成的张力未被写 |
| L2 | `text/ch51:59` "Caius took out his phone to call his dad – he’d need him to pull off the next stage – but his father was calling him instead." ／ "'I'm putting you on speakerphone. Matt’s here but not here, if you know what I mean.'" | 分析层未收「**父亲先打来**」这个反转与「开免提把马特拉进来」；导航只写"随后马库斯的电话插进来" | 提示 | 导航已部分覆盖（电话是插入的），且 `speakerphone` 进了词汇表；缺的是"他正要打、父亲却先打来"这一节点 |
| L3 | `text/ch51:92` "He's asking me to come down to the site tomorrow at 10 a.m. They're going to use a little robot with a camera." | 精读层与导航均**无「机器人/带摄像头」「明天上午 10 点」**（全文 grep「机器人」= 0） | 提示 | 导航与人物弧线只到"说自己会到现场""临时加进来的学者"。属选块取舍，不阻断 |
| L4 | `text/ch51:92` "Where are my damn glasses." ／ `text/ch51:80` "Marcus took a breath." | 眼镜的喜剧节拍未收（Marcus 在书房找眼镜） | 提示 | 纯喜剧细节，md 别处已用"吸了一口气"做了同类功能；不阻断 |

> 漏单无阻断型条目。理由：4 条均为**选块取舍**或**已被 md 别处部分覆盖**，且 md 写明了块数（6 块）这一取舍形态。

---

## 二、编单（md 有、原文无）

| # | md 原文 | 原文对照 | 档位 |
|---|---|---|---|
| C1 | 导航·叙事手法（md:15）"身体在公园里一圈圈" | `text/ch51:20` 只写 "He'd popped out for a light jog"；`text/ch51:26` "He was nailing his kettlebell squats."（他在**原地做壶铃深蹲**）；"绕着走"的是马特——`text/ch51:23` "'I've missed your little running outfits,' Matt said, **walking around him**." | 提示（并入错单 X6） |
| C2 | 原句1·为什么这样写（md:25）"作者让凯厄斯先跑出门、**脑子里暂时只有家务**" | 原文全章**未写凯厄斯此刻的内心**（`text/ch51:20` 只有外部动作与居家安排） | 提示（并入错单 X9） |

> 编单无独立阻断型条目；两条编的内容已并入错单作提示处理。

---

## 三、错单（两边都有但不一致）

### X1 ★阻断·施事归属反转｜信息流向写反：艾利的话是**凯厄斯**转述给马特，不是马特带来的

**md 侧**（两处，互相打架）：

1. `md:122` 一句话总结："**马特带来的**「两代人都封过修道院地下」、法医发现的隧道、以及「隧道底下的东西归 Beauchamps 家」这一句……"
2. `md:15` 导航·叙事手法："全章几乎全靠对话推进，**马特的转述里套着艾利的话**，马库斯的话里又套着法律顾问的话，层层转述把传闻磨得越来越像事实"

**原文侧**（`text/ch51:41–59`，说话人＝凯厄斯，接收者＝马特）：

- `text/ch51:41` "Matt caught him up to speed and **Caius told him** what Cecil/DJ Sonikk had told him in the waiting area."
- `text/ch51:44` "**'Andy brought Isolde to the station. He stopped me after I'd finished with her to talk about your ancestors.'**"（说话人＝Caius；"He stopped **me**"＝艾利对凯厄斯讲）
- `text/ch51:50` "'**He** essentially said that two different generations hundreds of years apart had both decided to seal up what was under the priory. That at some point **your family** knew what was down there but hid it.'"（"your family"＝艾利对凯厄斯说）
- `text/ch51:56` "'**He** didn't say, but Robbie just got a call from forensics at the site. They've discovered a tunnel.'"（仍是凯厄斯在讲）
- `text/ch51:59` "'**I knew it.**' Caius took out his phone to call his dad…"（说话人＝Caius，自"我早就知道"起为证）

**结论**：马特在本章是**听者**（`text/ch51:47` "'My ancestors?'"、`text/ch51:77` 他反问"你觉得下面是什么？有传闻吗？"、`text/ch51:125` "'Are you quitting?'"），不是艾利那番话的转述者。md 的「马特带来的」与「马特的转述里套着艾利的话」把转述方向写反了。
**注意 md 自相矛盾**：`md:11` 导航·一句话概括写的是"**艾利转述的**两代人封住修道院地下的旧事"（这一处方向正确），与 `md:15`、`md:122` 冲突。⇒ 属笔误而非另有依据。
**修法**：`md:122` →"**凯厄斯带来的**「两代人都封过修道院地下」"；`md:15` →"**凯厄斯的转述里套着艾利的话**（说给马特听）"。
**档位**：阻断（机器四道探针全绿也抓不到——引语逐字对、中文是中文、关键词成立、形态正常；错的只是"谁的转述"）

---

### X2 ★阻断·否定域反转｜马特明说**不会**拿小腿肚当调剂，md 写成会

**md 侧**（`md:14` 导航·人物弧线）：

> "**马特拿凯厄斯的小腿肚当漫长难熬日子的调剂**，话说到一半就把工作带进了这场对话"

**原文侧**（`text/ch51:29`）：

> "'Fine. **I won't use** your skinny calves **as a little light relief** on a long hard day.'"

**结论**：原文是马特**声明不用**（"I won't use…"）——这正是这句玩笑成立的前提（他拿"我不拿你的小腿肚当调剂"来逗人）。md 的 `md:14` 去掉否定，写成"马特拿…当调剂"，把**拒绝**写成**惯例**。md 自己的块 2（`md:31`）翻译是对的："马特说，那好吧，**他就不拿**凯厄斯那两条偏瘦的小腿肚，当成漫长难熬的一天里的一点轻松调剂了" ⇒ md 内部自相矛盾。
**修法**：`md:14` →"马特**扬言**要拿凯厄斯的小腿肚当调剂、却又说**不会**拿"（或"马特拿**不拿**小腿肚当调剂来打趣"）。
**档位**：阻断（否定域反转＝本库已知成因类，机器查不到）

---

### X3 ★阻断·事实断言｜"骸骨之手"与"被封住的东西"不是两条并行的线

**md 侧**（`md:77` 原句6·读者视角提示）：

> "骸骨之手被锁在地下室一百多年，与前面那条「被封住的东西」是**两条并行的线**；这一章只让它们擦肩而过。"

**原文侧**（`text/ch51:80`，**同一句里已经把两者串起来**）：

> "'No idea, but Caius's replacement called yesterday about a skeletal human hand that had been locked in a basement for a hundred-odd years, **so I'm guessing as it's an old priory that the tunnel probably leads to a crypt and a load of dead nuns.**'"

**旁证（跨章）**：`text/ch52:212` "watched as the little robot shone a light on **the crypt**. It was cavernous. **Skeletal remains were piled high**"（机器人下隧道→墓室→骸骨堆）；`text/ch50:157` "They knocked the priory down, you know. Left the **crypt** and basement levels only."（研究所即被拆的修道院遗存，地下室与墓室同址）。

**结论**：原文用 "so I'm guessing…" 把"骸骨之手"直接接到"隧道通向墓室"上；下一章即证实隧道直通墓室与骸骨。md 判它们"是两条并行的线、只擦肩而过"，与本章同句的串联关系及下一章事实都相反。md 自己的块 6（`md:75`）也写明"把确凿的消息（骸骨之手、地下室、一百多年）和随口的猜测（墓室、死修女）并排在同一口气里" ⇒ 内部不一致。
**修法**：`md:77` →"骸骨之手来自**另一条**地下室线索，本章只把它**摆到隧道边上**（'so I'm guessing…'），两者是不是同一条线，章内没有点破"。
**档位**：阻断（断言与原文相悖；证据已按 R5 附逐字）

---

### X4 提示·条件窄化｜产权例外的两个条件被并成一个

**md 侧**：`md:61`（原句5·中文理解）"除非是**珠宝之类超过一定价值的东西**，那就变成女王的"；`md:13`（导航·线索结构）"超过一定价值的**珠宝**归女王"。

**原文侧**（`text/ch51:74`）：

> "unless it's **a jewel** or **something over a certain value**, and then it becomes the queen's."

**结论**：原文是**两个并列条件**（是珠宝 **或** 超过一定价值 → 归女王）；md 的写法把阈值只挂在"珠宝"上，等于说"不够贵的珠宝仍归 Beauchamps 家"。`md:11` 导航的简写"够贵的归女王"反而更贴近原文。
**修法**：改为"除非**是珠宝、或者价值超过一定数额**"（"珠宝之类"里的"之类"可留，但要把"或"补上）。
**档位**：提示（法律条件被窄化，但读者可还原；且 `md:11` 已有正确简写）

---

### X5 提示·主语滑移｜"推测隧道通向墓室"的人是**马库斯**，不是继任者

**md 侧**：`md:13`（导航·线索结构）"凯厄斯的继任者提到地下室里锁了一百多年的骸骨之手，**于是推测**隧道通向墓室与一群死修女"。

**原文侧**（`text/ch51:80`）：继任者只报告了骸骨之手；"I'm guessing… the tunnel probably leads to a crypt and a load of dead nuns" 出自**马库斯**（"Your mum doesn't like this business" 同为马库斯）。

**结论**：md 块 6（`md:71`）译对了（"**他**猜那条隧道多半通向…"），但导航的箭头链把"推测"的主语挂到了继任者身上。
**修法**：`md:13` →"…骸骨之手，**马库斯据此猜**隧道通向墓室与一群死修女"。
**档位**：提示

---

### X6 提示·场景细节｜原文此刻是**壶铃深蹲**，"绕着走"的是马特

**md 侧**：`md:15` "身体在公园里一圈圈"；`md:11` "两人**边走边**把案子捋了一遍"；`md:12` "**马特边走边说**"。

**原文侧**：`text/ch51:26` "He was nailing his **kettlebell squats**."；`text/ch51:23` "'I've missed your little running outfits,' Matt said, **walking around him**."；`text/ch51:20` "He'd popped out for a light jog"。

**结论**：① 场景里在原地做壶铃深蹲的是凯厄斯，"绕着他走"的是马特 ⇒ md 的"身体在公园里一圈圈"容易被读成凯厄斯绕圈跑；② "两人边走边把案子捋了一遍"不符（凯厄斯没在走）；③ "马特边走边说"本身**对**（`text/ch51:23` 明写 walking around him）。
**修法**：`md:15` →"身体在公园里练着"；`md:11` →"马特绕着他打趣，两人把案子捋了一遍"。
**档位**：提示（比喻层，非硬事实）

---

### X7 提示·时点｜原文没有"跑完一圈"这个节点，搬家也不是本章定下来的

**md 侧**：`md:122` "而他自己也在**跑完这一圈**的当口，把**搬家的事定了下来**"；`md:11` "凯厄斯也**顺手把搬家的事定了下来**"。

**原文侧**：`text/ch51:20` "He'd **popped out** for a light jog"（轻跑已完成，此刻在公园做深蹲）；`text/ch51:20` "**They'd be going** from a one-bed flat…to a whole house"＋"she had her work cut out getting the place to her exacting standards before the baby was born"（搬家是**章首就已定的计划**）；`text/ch51:116` "'**We're moving house.**'"（本章只是**宣布**）。

**结论**：① 原文无"跑完一圈"这一时点（他此刻在做壶铃深蹲，见 X6）；② 搬家决定早于本章，本章是告知马特，不是"定下来"。
**修法**：`md:122` →"而他自己也在**这一趟跑完的当口**，把**搬家的事告诉了马特**"；`md:11` →"凯厄斯也**顺手把搬家的事说了出来**"。
**档位**：提示（两处同源改法）

---

### X8 提示·期限外扩｜"孩子出生"这条期限，原文只约束卡莉收拾新家

**md 侧**：`md:27`（原句1·读者视角提示）"搬家和**办案**都得在这条期限之前跑完"。

**原文侧**：`text/ch51:20` "she had her work cut out getting the place to her exacting standards **before the baby was born**"（before the baby was born 修饰的是**收拾新家**这件事，全句没有给案情设限）。

**结论**：md 给案情加了一条原文没有的期限。
**修法**：`md:27` →"搬家和办案在他身上**同时**进行，但原文只把期限给了收拾新家这件事"。
**档位**：提示

---

### X9 提示·内心戏外推｜原文没写凯厄斯跑出门时在想什么

**md 侧**：`md:25`（原句1·为什么这样写）"作者让凯厄斯先跑出门、**脑子里暂时只有家务**"；`md:15` "脑子却在原地**反复咀嚼案子的下一步**"。

**原文侧**：`text/ch51:20–59` 全程**无凯厄斯的内心描写**（外部动作＋对话）；"案子的下一步"在原文里的对应物是 `text/ch51:59` "he'd need him to **pull off the next stage**"（拉父亲来推进下一步）与 `text/ch51:59` "'I knew it.'"。

**结论**：① "脑子里暂时只有家务"是把外部居家安排读成内心状态；② "反复咀嚼"是强度修饰，原文只有一次 "I knew it." 的认知反应。
**修法**：`md:25` →"（至少表面上）他跑出门时手上只有家务那摊事"；`md:15` →"脑子却被**卷进了案子的下一步**"。
**档位**：提示

---

## 四、已核对**正确**（防误修，本节所列不得以"读着不对"为由改动）

| 项 | md 写法 | 原文逐字（出处） |
|---|---|---|
| 产权说的**说话人** | `md:61` "**马库斯说**，据他的法律顾问讲" | `text/ch51:74` "**Marcus** said." 段内 "'Well **according to my legal bloke**, technically the Beauchamps own the land…"（`text/ch51:62` 明确 "Marcus asked."、`:68` "'What a case,' **Marcus** said."；说话人＝Marcus，原话系转述其法律顾问 → md 归因正确） |
| 'Your mum doesn't like this business' 的**说话人** | `md:71` "他吸了一口气，又说：你妈妈不喜欢这种事" | `text/ch51:80` "Marcus took a breath. '**Your mum** doesn't like this business.'"（＝Marcus，md 正确） |
| 骸骨之手的**来源** | `md:71` "**凯厄斯的继任者**昨天打来电话" | `text/ch51:80` "**Caius's replacement** called yesterday about a skeletal human hand…"（md 正确，不是凯厄斯自己发现的） |
| "大概/我在猜"归属 | `md:71` "**他猜**那条隧道多半通向…" | `text/ch51:80` "so **I'm guessing** as it's an old priory that the tunnel probably leads to a crypt and a load of dead nuns."（说话人＝Marcus） |
| 是否已决定不做警察 | `md:14` "末了**仍说自己还没做完警察这份工**" | `text/ch51:128` "'**No, not yet. I'm not quite finished with the police yet.**'"（原文是"还没有"，md 未写成既定事实 ⇒ 通过） |
| 卡莉在家做什么 | `md:21` "卡莉留在家里，坐在沙发上翻网上家居" | `text/ch51:20` "**He'd left her sitting on the sofa browsing the internet for home decor.**"（原文明确她**在**家沙发上 ⇒ 通过） |
| 跑步的时间点 | `md:21` "凯厄斯穿着一条短裤**出门轻跑**" | `text/ch51:20` "**He'd popped out for a light jog**"（完成时＝已出门；md 未写成"正在跑"，亦未编成"刚跑完" ⇒ 通过） |
| 隧道是**法医**发现的 | `md:55` "他们发现了一条隧道"、`md:51` "罗比刚接到现场法医打来的电话" | `text/ch51:56` "Robbie just got a call **from forensics at the site**. **They've discovered a tunnel.**"（"刚"＝just ✅） |
| 章号/标题 | `md:7` "# 51. A Park Near the Police Station" | `text/ch51:17` "A Park Near the Police Station"（✅） |
| 分部标记 | `md:11` "分部「MONDAY」" | 本书分部标签为体例（ch42「SATURDAY」、ch53「TUESDAY」、ch54「SIX WEEKS LATER」），`text/ch51` 正文不含分部行；任务书给定 MONDAY，未见反证 ⇒ 跳过（未核全书 epub） |

---

## 五、机器层小结（R2，`2-machine.json`）

- `verdict: ok`，`chapter.sh` 退出码 **0**
- 引语逐字 **6/6 ✅**（本审查另行逐条复核：6 条引语均为 `text/ch51_51.txt` 的精确子串，最长 362 字符，无省略号缝合、无跨话轮拼接）
- 块数 6 · 段数 6 · `segment_miss 0` · `struct_bad 0` · `empty_quote 0` · `keyword_bad 0` · `cjk_low 0`
- 中文字符占比：中文理解 0.78–0.93 ｜ 为什么这样写 0.69–0.90 ｜ 读者视角提示 0.60–0.90；关键词行按体例为词项（占比 0）
- 词汇表 24 条，**24/24 例句均为本章原文精确子串**（逐条 `in src` 判定）；`scripts/check_vocab.py`（全书口径）**未对 ch51 报任何告警**
- ⇒ 机器全绿，**不能**推出本章无缺陷：X1／X2／X3 三条阻断型全部落在机器读不到的那一层（施事归属、否定域、断言）
