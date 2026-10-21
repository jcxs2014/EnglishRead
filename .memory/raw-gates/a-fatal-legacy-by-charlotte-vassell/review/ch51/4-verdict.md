# 4-verdict · ch51 判定表

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch51 caius runs in the park.md`
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch51_51.txt`
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch51/`
- 读取顺序（铁律已守）：R1 只读 `text/ch51_51.txt` → 落盘 `1-suread.json` → 才开 md → R2 机器层 → R3/R4 人判
- 档位：**阻断**（与原文不符/缺失，必须改）／**提示**（措辞可商榷，记录不建议改）／**假红**（工具判错）／**跳过**（没查）

---

## 0. 覆盖声明

| 章 | 覆盖层 | 说明 |
|---|---|---|
| **ch51** | **全层（R1+R2+R3+R4+R5）** | 本次唯一审查对象，四组数均出自本章 |
| ch50 / ch52 | **仅取 text 片段作旁证** | 只为核 X3（骸骨之手与隧道是否同一线）读了 `text/ch50:157`、`text/ch52:212/221`；**未做独立审查**，不得记为"通过" |
| 本书其余 51 章 | **只有机器层**（`scripts/check_vocab.py` 全书口径已跑，**未对 ch51 报任何告警**；其余章的告警与本次结论无关） | 未做人判，**不等于通过** |

---

## 1. 四组数（只报这四组）

| 组 | 分子/分母 | 数字 | 备注 |
|---|---|---|---|
| **逐字** | 引语段数命中 / 引语段数 | **6 / 6 ✅** | `chapter.sh --json`：`segment_miss 0`、`empty_quote 0`，退出码 0；本审查另逐条复核：6 条引语均为源文件**精确子串**（最长 362 字符），**无省略号缝合、无跨话轮拼接**；词汇表 24/24 例句亦为精确子串 |
| **对应** | 讲这句引语的块 / 总块数 | **6 / 6**（0 不对应 · 0 引语选短 · 0 密度不足） | 块级全部对应；但**导航/总结层有 2 处把引语读错**（X1 施事归属、X2 否定域）——按对照表 §⑥ 归入本组（"错的只是中文那层怎么读引语"） |
| **形态** | 偏离项 / 形态项 | **0 偏离 / 4 项全对** | H1 ✓ 导航项数 ✓ 子项集 ✓ 块数 ✓（明细见 §4） |
| **断言** | 事实断言核对 | **共核 16 条：阻断 3 · 提示 9 · 通过 4** | 阻断 3 条全在"事实断言/归属"层（X1/X2/X3）；详见 §2 |

**阻断型条数：3**（X1、X2、X3）

---

## 2. 判定表

| # | 断言 | 证据（章:区间，逐字） | 结论 | 档位 |
|---|---|---|---|---|
| X1 | md `md:122`"**马特带来的**「两代人都封过修道院地下」"、md `md:15`"**马特的转述里套着艾利的话**" | 源 `text/ch51:41` "Matt caught him up to speed and **Caius told him** what Cecil/DJ Sonikk had told him in the waiting area."；`:44` "**'Andy brought Isolde to the station. He stopped me after I'd finished with her to talk about your ancestors.'**"；`:50` "'**He** essentially said that two different generations hundreds of years apart had both decided to seal up what was under the priory…'"；`:56` "'**He** didn't say, but Robbie just got a call from forensics at the site…'"；`:59` "'**I knew it.**' Caius took out his phone to call his dad…" | 说话人是**凯厄斯**（对马特转述艾利的话），马特是**听者**（`:47`"'My ancestors?'"、`:77`、`:125`"'Are you quitting?'"）。md 把转述方向写反；且 md 自相矛盾（`md:11` 写的是"**艾利转述的**…"＝方向正确） | **阻断** |
| X2 | md `md:14`"马特**拿**凯厄斯的小腿肚当漫长难熬日子的调剂" | 源 `text/ch51:29` "'Fine. **I won't use** your skinny calves **as a little light relief** on a long hard day.'" | 原文是马特声明**不拿**小腿肚当调剂（否定域是玩笑成立的前提）；md 去掉否定＝把"拒绝"写成"惯例"。md 块 2（`md:31`"他**就不拿**…"）译法正确 ⇒ 内部矛盾 | **阻断** |
| X3 | md `md:77`"骸骨之手…与前面那条「被封住的东西」是**两条并行的线**；这一章只让它们擦肩而过" | 源 `text/ch51:80` "…a skeletal human hand that had been locked in a basement for a hundred-odd years, **so I'm guessing as it's an old priory that the tunnel probably leads to a crypt and a load of dead nuns.**"；旁证 `text/ch52:212` "watched as the little robot shone a light on **the crypt**. It was cavernous. **Skeletal remains were piled high**"；`text/ch50:157` "They knocked the priory down, you know. Left the **crypt** and basement levels only." | 原文**在同一句里已把两者串联**（"so I'm guessing…"），下一章证实隧道直通墓室与骸骨堆。md 判它们"并行、只擦肩而过"与原文相悖；md 块 6（`md:75`"并排在同一口气里"）自相矛盾 | **阻断** |
| X4 | md `md:61`"除非是**珠宝之类超过一定价值的东西**"、md `md:13`"超过一定价值的**珠宝**归女王" | 源 `text/ch51:74` "unless it's **a jewel or something over a certain value**, and then it becomes the queen's." | 原文是**两个并列条件**（是珠宝 **或** 超值 → 女王）；md 把阈值只挂到"珠宝"上，等于说"不够贵的珠宝仍归 Beauchamps 家"。（`md:11`"够贵的归女王"正确） | 提示 |
| X5 | md `md:13`"凯厄斯的继任者提到…骸骨之手，**于是推测**隧道通向墓室与一群死修女" | 源 `text/ch51:80` "**'No idea, but Caius's replacement called yesterday about…'**"＋"so **I'm guessing**… the tunnel probably leads to a crypt and a load of dead nuns." | 报告者是继任者，**推测者是马库斯**（"I'm guessing"）；md 块 6（`md:71`"**他猜**…"）正确，导航箭头链主语滑移 | 提示 |
| X6 | md `md:15`"身体在公园里**一圈圈**"、md `md:11`"**两人边走边**把案子捋了一遍" | 源 `text/ch51:26` "He was nailing his **kettlebell squats**."；`:23` "'I've missed your little running outfits,' Matt said, **walking around him**." | 原地做壶铃深蹲的是凯厄斯，"绕着他走"的是马特；md 的比喻易读成凯厄斯绕圈跑。（`md:12`"马特边走边说"**正确**） | 提示 |
| X7 | md `md:122`"在**跑完这一圈**的当口，把**搬家的事定了下来**"、md `md:11`"**顺手把搬家的事定了下来**" | 源 `text/ch51:20` "He'd **popped out** for a light jog"；"**They'd be going** from a one-bed flat…to a whole house"；`:116` "'**We're moving house.**'" | ① 原文此刻在做壶铃深蹲，无"跑完一圈"节点；② 搬家是**章首已定**的计划，本章只是**宣布** | 提示 |
| X8 | md `md:27`"搬家和**办案**都得在这条期限之前跑完" | 源 `text/ch51:20` "she had her work cut out **getting the place** to her exacting standards before the baby was born" | "before the baby was born"只修饰**收拾新家**，原文未给案情设限 | 提示 |
| X9 | md `md:25`"脑子里**暂时只有家务**"、md `md:15`"脑子却在原地**反复咀嚼**案子的下一步" | 源 `text/ch51:20–59` 全程无凯厄斯内心描写；唯一的认知反应是 `:59`"'I knew it.'"，"下一步"对应 `:59`"he'd need him to **pull off the next stage**" | 内心状态属外推；"反复咀嚼"强度修饰，原文只有一次认知反应 | 提示 |
| L1 | md 精读层未收"卡莉因 Eulalia 出现而脆弱"这一拍 | 源 `text/ch51:32` "'Callie’s being a bit funny about work following me home. Now everything has sunk in, **Eulalia turning up like that has made her feel vulnerable.**'"；`:35` "'I get that, especially with **her history**.'" | 全章唯一推进卡莉线的拍，仅以 vocab 例句（`vulnerable`）出现；6 块选样可接受，未写取舍理由 ⇒ 不判阻断，记提示 | 提示 |
| L2 | md 分析层未收"父亲**先打来**"＋开免提把马特拉进来 | 源 `text/ch51:59` "Caius took out his phone to call his dad – he’d need him to pull off the next stage – **but his father was calling him instead.** … I'm putting you on **speakerphone**." | 导航"马库斯的电话插进来"已部分覆盖；`speakerphone` 在词汇表 | 提示 |
| L3 | md 无"机器人/明天上午 10 点到工地" | 源 `text/ch51:92` "He's asking me to come down to the site **tomorrow at 10 a.m.** They're going to use **a little robot with a camera**." | 选块取舍，未写取舍理由；不判阻断 | 提示 |
| L4 | md 未收"马库斯在书房找眼镜" | 源 `text/ch51:92` "I'm in the study and I've had an email. **Where are my damn glasses.**" | 纯喜剧细节；不阻断 | 提示 |
| ④专项 | md `md:14`"末了**仍说自己还没做完警察这份工**" | 源 `text/ch51:128` "'**No, not yet. I'm not quite finished with the police yet.** The commute will be only an hour.'" | md 与原文一致；md 全文**未**出现"他已决定不做警察/去做别的"的表述（取证见 §5）⇒ **通过** | 通过 |
| ③专项 | md `md:61`"**马库斯说**，据他的法律顾问讲…归他们…归女王" | 源 `text/ch51:62` "'I do. Matt, how are you doing?' **Marcus** asked."；`:68` "'What a case,' **Marcus** said."；`:74` "'Well **according to my legal bloke**, technically the Beauchamps own the land, so anything down that tunnel is **ours** unless it's a jewel or something over a certain value, and then it becomes **the queen's**.'" | 说话人＝Marcus ✓；原话系**转述其法律顾问** ✓；归属方向（Beauchamps 家→女王）✓ ⇒ **通过** | 通过 |
| ①专项 | md `md:21`"凯厄斯穿着一条短裤**出门轻跑**；卡莉**留在家里**，坐在沙发上翻网上家居" | 源 `text/ch51:20` "**He'd popped out for a light jog** while Callie rested at home. **He'd left her sitting on the sofa browsing the internet for home decor.**" | md 未写成"正在跑"，也未编成"刚跑完"；卡莉在家的状态与活动 ✓ ⇒ **通过**（但 `md:15`/`md:122` 的"一圈圈/跑完这一圈"另见 X6/X7） | 通过 |
| ②专项 | md 未编造"他在路上想起某一步推理" | 源 `text/ch51` **无任何"路上/跑步时回想推理"的描写**；最接近的是 `:59`"'I knew it.' Caius took out his phone to call his dad – **he'd need him to pull off the next stage**" | md 没有虚构这一步 ✓；但把"家里只有家务"与"反复咀嚼"当成他的内心状态 ⇒ 另记 X9（提示） | 通过（附 X9） |

---

## 3. 本章专属判据 · 四项特别核的结论

| 特别核 | 问什么 | 结论 | 依据 |
|---|---|---|---|
| ① | 公园/跑步的**时间点**（原文是「刚跑完」还是「正在跑」）与卡莉在家的状态 | **通过**（md 主体正确）＋2 处措辞提示 | 原文：`text/ch51:20` "He'd **popped out for a light jog**"（完成时：已出门轻跑）＋`:26` "He was nailing his **kettlebell squats**"（此刻原地做深蹲，**既非"正在跑"也非"刚跑完"**）；卡莉 `:20` 在家沙发上刷家居网页，`:32` 因 Eulalia 出现而觉得脆弱。md `md:21` 两项都对；`md:15`"身体在公园里一圈圈"、`:122`"跑完这一圈"提示级（X6/X7） |
| ② | 他在路上想起的**那一步推理**是什么、md 写的与原文一致吗 | **md 未编造**（通过）；但把"脑子只有家务/反复咀嚼"当内心状态 ⇒ 提示 X9 | 原文无"路上回想推理"；最近的是 `:59`"'I knew it.' … he’d need him to **pull off the next stage**"（把父亲拉进来推进下一步）。md 块 3 把这步写成"案子从「谁动了手」推到「祖辈藏了什么」"（`md:45`），是**对引语内容的概括**，非凭空捏造 |
| ③ | 「隧道底下归 Beauchamps 家、够贵的归女王」——**说话人与原话** | **通过**（说话人＝马库斯；系转述其法律顾问；方向正确）＋1 处条件窄化提示 X4 | 见 §2 的 ③专项行 |
| ④ | 本章是不是把结局走向（不 police、去做别的）写成**既定事实** | **通过**（没有） | 源 `text/ch51:128` "'No, not yet. I'm not quite finished with the police yet.'"；md `md:14`"末了**仍**说自己还没做完警察这份工"；md 全文无"已决定不做警察/改行"表述（取证见 §5） |

---

## 4. 形态组（对照本书众数 / profile）

| 形态项 | 本章实况 | 本书众数 / profile | 偏离 | 理由 |
|---|---|---|---|---|
| **H1** | `# 51. A Park Near the Police Station` | `h1_shape_ok: true`；本书体例 `# NN. 标题` | 无 | 与源标题 `text/ch51:17` "A Park Near the Police Station" 一致 |
| **导航项** | 5 项（一句话概括／视角／线索结构／人物弧线／叙事手法） | `nav_count: 5`，`nav_counts: [5]`，`nav_missing: []` | 无 | 项数与项名与本书众数一致 |
| **子项集** | 中文理解／关键词／为什么这样写／读者视角提示 | `profile: mystery-thriller`，`profile_subitems` 同上；可选「句子结构」未用 | 无 | 可选项未用不构成偏离 |
| **块数** | 6 块 | `block_median: 7.0`，`block_range: [5, 10]` | 无 | 6 落在本书区间 [5,10] 内（比众数少 1，不出区间）⇒ 属正常浮动，无需写理由 |

**形态组结论：0 偏离。**

---

## 5. 取证三件套（凡"零命中/查无"类断言必须自证）

```
CMD: /usr/bin/grep -cE '辞职|离职|不干了|quit' "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch51 caius runs in the park.md"
     → OUT=2, EXIT=0
     （两行均为假阳性命中：md:86 是词汇例句原文 'Are you quitting?'；md:103 是 "quite frankly" 中的 "quit"
       ⇒ md 全文**没有**"他已决定不做警察/改行"的断言）

CMD: /usr/bin/grep -cE '机器人|robot' "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch51 caius runs in the park.md"
     → OUT=0, EXIT=1   （EXIT=1 = 无匹配 ⇒ L3「机器人/带摄像头」确未出现在 md）

CMD: /usr/bin/grep -c '警察' "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch51 caius runs in the park.md"
     → OUT=1, EXIT=0
CMD: /usr/bin/grep -n '警察' 同上文件
     → md:14 "- **人物弧线**：…末了仍说自己还没做完警察这份工。"   EXIT=0
       （"警察"全文仅 1 次且语境正确 ⇒ ④专项"未把结局走向写成既定事实"成立）

CMD: /usr/bin/grep -n '辞职|离职|不干了|quit' 同上文件
     → md:86 / md:103（见上）   EXIT=0
```
说明：取证一律用**显式文件路径 + `/usr/bin/grep`**（不用 `git grep`／rg 默认 ignore 规则），模式用 `-E`；本文件所有"查无"类断言均附命令、输出与退出码。

---

## 6. 已核实为正确（防误修 · 固定一节）

**以下写法读着像错，回原文核对后成立；后续任何人不得以"读着不对"为由改动，除非能给出反证。**

| 项 | md 写法 | 原文逐字（出处） |
|---|---|---|
| 产权说的说话人 | `md:61`"**马库斯说**，据他的法律顾问讲" | `text/ch51:62` "'I do. Matt, how are you doing?' **Marcus** asked."；`:68` "'What a case,' **Marcus** said."；`:74` "'Well **according to my legal bloke**…'"（说话人＝Marcus，原话系转述其法律顾问 ⇒ 归因正确，**不要**改成"艾利/马特说的"） |
| 'Your mum doesn't like this business' | `md:71`"他吸了一口气，又说：你妈妈不喜欢这种事" | `text/ch51:80` "**Marcus took a breath.** '**Your mum** doesn't like this business.'"（＝Marcus） |
| 骸骨之手的来源 | `md:71`"**凯厄斯的继任者**昨天打来电话" | `text/ch51:80` "**Caius's replacement** called yesterday about a skeletal human hand…"（**不是**凯厄斯自己发现的） |
| "I'm guessing" 归属 | `md:71`"**他猜**那条隧道多半通向…" | `text/ch51:80` "so **I'm guessing** as it's an old priory that the tunnel probably leads to a crypt and a load of dead nuns."（说话人＝Marcus） |
| 块 2 的否定 | `md:31`"马特说，那好吧，**他就不拿**…" | `text/ch51:29` "'Fine. **I won't use** your skinny calves as a little light relief on a long hard day.'"（**块 2 译法正确**——错的只是 `md:14` 导航那一处，勿把块 2 一起改坏） |
| 隧道由法医发现 | `md:51`"罗比**刚**接到现场法医打来的电话：他们发现了一条隧道" | `text/ch51:56` "Robbie **just** got a call **from forensics at the site**. They'**ve discovered a tunnel**." |
| 卡莉在家的状态 | `md:21`"卡莉留在家里，坐在沙发上翻网上家居" | `text/ch51:20` "**He'd left her sitting on the sofa browsing the internet for home decor.**" |
| 跑步时点 | `md:21`"出门轻跑" | `text/ch51:20` "**He'd popped out for a light jog**"（完成时；md 未写成"正在跑"） |
| 是否已定不做警察 | `md:14`"末了**仍**说自己还没做完警察这份工" | `text/ch51:128` "'**No, not yet. I'm not quite finished with the police yet.**'" |
| 章号 / 标题 | `md:7` "# 51. A Park Near the Police Station" | `text/ch51:17` "A Park Near the Police Station" |
| 术语「墓室」 | `md:71`"通向**一间墓室**" | `text/ch51:80` "leads to **a crypt**"（crypt＝墓室/地下墓穴，md 词表已收） |
| 分部「MONDAY」 | `md:11` "分部「MONDAY」" | `text/ch51` 正文不含分部行（分部标签为全书体例：ch42「SATURDAY」、ch53「TUESDAY」、ch54「SIX WEEKS LATER」）；任务书给定 MONDAY，未见反证 ⇒ **跳过**（未核全书 epub，不作断言） |

---

## 7. 结论

- **四组数**：逐字 **6/6** ｜ 对应 **6/6**（其中导航/总结层 2 处读错引语）｜ 形态 **0 偏离** ｜ 断言 **16 条：阻断 3 · 提示 9 · 通过 4**
- **阻断型 3 条**：X1（艾利的话被写成马特带来的／马特的转述——方向写反）、X2（"I won't use" 的否定被抹掉）、X3（骸骨之手与隧道被说成两条并行线）
- **最要紧的一条 = X1**：它出现在**一句话总结**与**导航·叙事手法**两处，是本章最显眼的施事归属反转——读者会以为马特把艾利的话转述给凯厄斯；原文里马特是**听者**（`'My ancestors?'`/`'Are you quitting?'`），转述者是**凯厄斯**。md 自己的导航另有一处（`md:11`"艾利转述的…"）方向是对的，⇒ 属笔误，改两处即可，且改动不触及引语与块内分析。
- 机器层全绿（`chapter.sh` 退出码 0、6/6 逐字、词汇 24/24 命中）**不能**推出本章无缺陷：本章 3 条阻断型全部落在机器读不到的层（施事归属 / 否定域 / 断言）。
- 本次审查未改动书目录任何 md，未 `git add`／未 `git commit`。
