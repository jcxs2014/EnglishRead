# 3-diff.md · 《A Fatal Legacy》第 22 章对账

> 审查方：独立审查员（异实例路径）· 章：22 · 书：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell`
> 权威源：`text/ch22_22.txt`（已与 epub `OPS/s035-Chapter-022.xhtml` 逐段对账：**44 段全部逐字命中，0 段丢失 / 0 段多出**，见 4-verdict.md「语料自证」）
> 证据格式：`text/ch22_22.txt:<行>` + 该行原文逐字。
> 单子：漏 / 编 / 错。**每条附两侧原文片段**。

---

## 单子一：错（两边都有但不一致）

### 错-1【阻断·说话人/归属反转】md 说「丈夫叫 Beverley」——原文里丈夫叫 Nigel

- **md 侧**（`ch22 matt questions beverley parkin.md:23`，原句 1 · 读者视角提示）：
  > 留意屋里的称呼：妻子叫「Bev」、丈夫叫「Beverley」；门外那个「Mrs Beverley Parkin」在这套叫法之外，是另一重身份。
- **原文侧**：
  - `text/ch22_22.txt:38`（Nigel 说的）：
    > ‘What is it, Beverley?’ He stopped and looked at Matt in his shirt and tie. ‘Jehovah’s Witnesses? Or is it double glazing? No thank you, not today. I told you, Bev, just shut the door.’
  - `text/ch22_22.txt:41`（Beverley 说的）：
    > ‘No, Nigel, he’s police.’
  - `text/ch22_22.txt:110`（Nigel 说的）：
    > ‘Bev, did you leave a little piece of paper with the PIN number on it with the card?’
- **判**：原文里 **「Bev」与「Beverley」都是丈夫 Nigel 对妻子 Beverley 的称呼**（Nigel 同段里两个都用了：「What is it, Beverley?」…「I told you, Bev」）；妻子称丈夫为 **Nigel**；「Mrs Beverley Parkin」就是 Beverley 本人的正式称谓，**不是「这套叫法之外的另一重身份」**。md 把「Bev／Beverley」安到「妻子／丈夫」两栏，等于把丈夫改名成 Beverley、把妻子的正式名说成第三方身份。
- **取证**（R5-补 三件套）：
  ```
  CMD: /usr/bin/grep -inwE 'Bev|Beverley|Nigel' text/ch22_22.txt
  → 命中 20 行（含 32/38/41/47/50/53/59/65/68/71/74/83/89/95/110/113/119/122/131/134/137/143/146/149 中的相关行）
  EXIT=0
  ```
  逐行核对结果：**「Beverley」每次出现都指妻子**（Nigel 叫、Matt 叫、她自己称）；**「Nigel」每次出现都指丈夫**；**「Bev」只出现在 Nigel 的台词里**（:38 / :110 / :146）。
- **档**：**阻断**（S3 第 ④ 类「说话人错配」＋⑥ 类「归属反转」，四道机器探针全绿，只有人判能抓）

### 错-2【阻断·事实断言反了】md 说贝弗利「亲口说出」三件事——原文这三件全在她心里

- **md 侧**（md:14，导航 · 人物弧线）：
  > 贝弗利从一句「No, definitely not」的否认，走到后来**亲口说出**女儿的「another turn with her nerves」、伦敦有「better doctors」，以及那笔瞒着丈夫的钱；
- **原文侧**：
  - `text/ch22_22.txt:137`（整行只有一句是对白，其余是叙述/她心里的盘算）：
    > ‘I know.’ Beverley nodded. She thought it was for the best too for Jenny to be a bit more independent and away from them. It also meant that if Jenny had another turn with her nerves the neighbours didn’t have to see or hear of it like last time. Besides, they had better doctors down there.
  - `text/ch22_22.txt:149`：
    > ‘I’ll call later, love.’ Beverley looked at the time on her watch. ‘They’ll be busy and I don’t want to upset anyone.’ She really didn’t want to upset the little bit of ‘housekeeping’ she was sent on the sly every month without her tight husband’s knowledge, which had paid for her new highlights and a pair of new leather boots and all the other little treats that her husband had been convinced had come from the back of the wardrobe.
- **判**：三处（神经发作 / 更好的医生 / 每月那趟差事）**都不是她说出口的话，是她的内心**；`another turn with her nerves` 与 `better doctors` 只出现在叙述句里，`housekeeping` 那段更明写「without her tight husband's knowledge」——**说出口就不叫瞒着**。md 这一句自相矛盾，且与本 md 自己原句 5 的分析直接打架（原句 5 · 为什么这样写：「这些话全被压在贝弗利的心想里，**夫妇俩谁也没有说出口**」）。
- **为什么这是本章最重的错**：本章专属判据正是「**她说的和没说的**」；这条导航把「没说的」改写成「说的」，把全章的对照轴翻了过来。
- **档**：**阻断**（S5/导航层事实断言错 + 与本 md 内部不一致）

### 错-3【对应·引语选短】原句 2 的中文理解首句讲的是引语**之前**的原文

- **md 侧**（md:26，原句 2 · 中文理解）：
  > **听到「被钓鱼」几个字，贝弗利先说自己只有一个账户、只用来收账单和 Next 的促销邮件**，随即话锋一转：前些月她在 M&S Food 丢过一张卡……
- **原文侧**（`text/ch22_22.txt:95`，引语从 “Hang on, Nigel.” 起，前半句**不在引语内**）：
  > ‘Oh no. I’ve got an account but I only really use it to get my bills and emails about the Next sale,’ Beverley said. She turned to look at Nigel and furrowed her brow. **‘Hang on, Nigel. I think I dropped a card in M&S Food the other month. I had to get a new card, but perhaps I wasn’t quick enough. It was such a hassle. It can’t have been an expensive charge or I would’ve noticed and challenged it with the bank. I hadn’t noticed anything, actually.’**
- **判**：中文理解的第一句（账户 / Next 促销邮件）分析的是引语**外**的上下文 ⇒ S2 第 ① 类「截短：分析覆盖的原文比引语长」，读者无法凭引语核对这一句。引语本身逐字无误（机器 6/6 ✅）。
- **档**：**提示**（机器全绿；引语可选短也可改中文理解，属选材口径问题，不是内容错误）

### 错-4【对应·引语选短】原句 3 的中文理解末句讲的是引语**之后**的原文

- **md 侧**（md:32，原句 3 · 中文理解）：
  > …除了那姑娘惊人的平凡——她用厚重刘海和不搭颈色的浓妆遮过这张脸，**母亲年轻时应当是秀气的，这姑娘大概随了她那位面团似的父亲。**
- **原文侧**（`text/ch22_22.txt:119`，引语止于 “colour of her neck.”，加粗部分在引语之后）：
  > ‘Right,’ Matt said. He took another look around the room. There was a graduation photo of a young woman on the mantlepiece. There was nothing remarkable about it other than the girl’s spectacular plainness that she had tried to hide under a chunky fringe and a layer of caked-on make-up that didn’t match the colour of her neck. **Beverley looked like she would’ve been pretty when she was younger. Her daughter must have taken after her doughy father.**
- **判**：中文理解盖过了引语边界（引语短了）。引语逐字无误。
- **档**：**提示**（同错-3，选材口径）

---

## 单子二：编（md 有、原文无）

### 编-1【提示·陈设虚增】原句 3 说 Matt 先看「吊灯、地毯、书架」——原文没有地毯、没有书架

- **md 侧**（md:35，原句 3 · 读者视角提示）：
  > 看 Matt 的视线顺序：先看房间（**吊灯、地毯、书架**），再看到人（毕业照、女儿的相貌）；
- **原文侧**（本章原文出现的全部陈设：`text/ch22_22.txt:20`「1930s semi-detached … pleasant cul-de-sac」、`:29`「warrant card」、`:35`「a trowel in one hand and a pair of gardening shears」、`:50`「neat living room … leather sofa」、`:56`「A cheap chandelier hung from the ceiling」、`:95`「a bobble on her cardigan」、`:119`「graduation photo … on the mantlepiece」、`:83`「a commemorative plate in a cabinet」、`:122`「perched on the stairs」）
  ——**没有地毯，没有书架**。
- **取证**（R5-补 三件套，词边界匹配防 `Shrugged` 里的子串 `rug` 误命中）：
  ```
  CMD: /usr/bin/grep -inwE 'carpet|rug|bookshelf|bookcase|vanity|dresser|comb' text/ch22_22.txt
  → 无输出
  EXIT=1
  ```
  （对照：`/usr/bin/grep -cinE 'carpet|rug|bookshelf|dressing table' text/ch22_22.txt` → **1**，命中 :131 的 `Beverley **Shrugged**.` —— 纯子串误命中，正是 R5-补 说的坑；故本条以 `-w` 口径为准。）
- **判**：属**陈设细节虚增**，不是情节/关系/数字凭空出现，故按 R3「编」表的判据列（情节/关系/数字）**不判阻断，判提示**；但它是写给读者看的「原文里有什么」的陈述，应删或改（原文只有吊灯）。
- **档**：**提示**

### 编-2【提示·陈设虚增】原句 6 说秘密「藏在衣柜与梳妆台之间」——原文没有梳妆台

- **md 侧**（md:52，原句 6 · 为什么这样写）：
  > 而这一家人所有的秘密都藏在**衣柜与梳妆台**之间；
- **原文侧**（`text/ch22_22.txt:149`）：
  > …all the other little treats that her husband had been convinced had come from **the back of the wardrobe**.
  （上文取证：`grep -inwE '…|vanity|dresser|comb' text/ch22_22.txt` → 无输出，EXIT=1；本章只出现 wardrobe）
- **档**：**提示**

### 编-3【提示·身体细节虚增】导航说「那双刻意藏拙的眼睛」——原文只写刘海与不搭颈色的浓妆

- **md 侧**（md:13，导航 · 线索结构）：
  > → 壁炉架上女儿的毕业照与**那双刻意藏拙的眼睛** → …
- **原文侧**（`text/ch22_22.txt:119`）：
  > …the girl’s spectacular plainness that she had tried to hide under **a chunky fringe and a layer of caked-on make-up that didn’t match the colour of her neck**.
- **取证**：
  ```
  CMD: /usr/bin/grep -inwE 'eye|eyes' text/ch22_22.txt
  → 134:‘I thought they had plenty of money.’ Nigel stood up and took his phone out of his pocket. ‘Can’t buy a cardigan? I thought the whole idea of Jenny moving to London too was that she’d get a bit of independence while **her sister kept an eye on her**. Made sure she was OK.’
  EXIT=0
  ```
  ⇒ 全章唯一的 “eye” 是「**她姐姐盯着她**」，与「藏拙的眼睛」无关；且原句 3 的中文理解写的是刘海与浓妆，两处口径不一致。
- **档**：**提示**

---

## 单子三：漏（素读有、md 无）

### 漏-1【提示·漏】皇家婚礼 / Lady Di 那一段没有进入任何引语块

- **原文侧**（`text/ch22_22.txt:77`–`:83`）：
  > ‘I’ve not been to London since the Royal Wedding. Oh she did look lovely. I was stood right in front of Westminster Abbey. Me and my cousin camped out the night before. What a fairytale.’
  > ‘Kate Middleton?’
  > ‘Oh no, Lady Di,’ Beverley said, gesturing to a commemorative plate in a cabinet. ‘Taken too young.’
- **md 侧**：6 个引语块与 5 条导航线索**都没有覆盖这一段**（只在本章词汇表收了 commemorative 一词）。导航「线索结构」的第一环是「邮政信箱（伦敦，PO Box）」，而这段正是全章**唯一直接回答「伦敦 PO Box」**的材料（她自皇家婚礼后再没去过伦敦，且把 Kate Middleton 与 Lady Di 弄混）。
- **判**：属有信息量的对话，非「关键转折」，且词汇表已部分收录 ⇒ **提示级漏**，不判阻断。补一条引语块或在导航线索里点一句即可。
- **档**：**提示**

### 漏-2【提示·漏】Nigel 问「PIN 纸条」那一段没有进入任何引语块

- **原文侧**（`text/ch22_22.txt:110`–`:116`）：
  > ‘Bev, did you leave a little piece of paper with the PIN number on it with the card?’
  > ‘I might have done, Nigel.’
  > ‘You’ve got to be more careful.’
- **md 侧**：无任何引语块覆盖（词汇表亦未收 PIN 行）；md 叙事只把「被钓鱼」「两步验证」写进导航，而 PIN 纸条恰是本章最实的一个漏洞。
- **档**：**提示**

---

## 第二遍（引语块 4–6 · 导航 · 词汇表 · 形态）追加

### 错-5【提示·与引语相抵】原句 4 说「中间没有一句「为什么」」——引语里就有 why 句

- **md 侧**（md:41，原句 4 · 读者视角提示）：
  > 她转述得又快又急：信箱、开衫、警方兴趣，三件事一口气说完，**中间没有一句「为什么」**。
- **原文侧**（`text/ch22_22.txt:125`）：
  > ‘A PO Box? What does Jenny want with a PO Box? She said she just wanted to buy a cardigan. **And why are the police interested?’**
- **判**：三件事中的第三件本身就是 why 疑问句；「中间没有一句为什么」在字面上与引语相抵（若读作「三件事之间没有 why」，则应明说是「三件事之间」）。
- **档**：**提示**（措辞）

### 错-6【提示·与引语相抵】原句 2 说她「认下了「受害者」这个位置」——引语里她正说「我什么都没注意到」

- **md 侧**（md:28，原句 2 · 为什么这样写）：
  > 这一段等于由她自己**认下了「受害者」这个位置**，Matt 后面那句「跟银行说」才有来处。
- **原文侧**（`text/ch22_22.txt:95`）：
  > ‘It can’t have been an expensive charge or I would’ve noticed and challenged it with the bank. **I hadn’t noticed anything, actually.**’
  （另 `:71`：‘No, definitely not,’ Beverley said, mystified.）
- **判**：她的原话是**否认察觉、否认受害**；「主动翻出丢卡」＝给 Matt 一个替代解释，不等于认下受害身份。属解读过度。
- **档**：**提示**（措辞/解读）

### 错-7【提示·自相矛盾】导航「一句话概括」把「瞒着丈夫的差事」也算成她跟丈夫念叨的内容

- **md 侧**（md:11，导航 · 一句话概括）：
  > …她当场否认，转头却**跟丈夫念叨女儿要「买件开衫」，以及每月瞒着丈夫办的那趟差事**。
- **原文侧**（`text/ch22_22.txt:149`）：
  > …the little bit of ‘housekeeping’ **she was sent on the sly every month without her tight husband’s knowledge**…
- **判**：她**没有**对丈夫念叨那趟差事（瞒着丈夫＝不对他说）；md 句子把两个并列宾语都挂在「跟丈夫念叨」下，与自己的括注「瞒着丈夫」相抵。
- **档**：**提示**

### 错-8【提示·位置错】一句话总结说「没说出口的那部分……全落在她转身跟丈夫说话的那些话里」

- **md 侧**（md:103，一句话总结）：
  > 她嘴里没说的那部分——女儿的神经发作过、邻居见过、每月有一笔瞒着丈夫的秘密款——**全落在她转身跟丈夫说话的那些话里**。
- **原文侧**（`text/ch22_22.txt:137` 与 `:149`，见错-2 逐字）：
  > ‘I know.’ Beverley nodded. **She thought** it was for the best too for Jenny… the neighbours didn’t have to see or hear of it like last time. Besides, they had better doctors down there.
  > …**She really didn’t want to upset** the little bit of ‘housekeeping’ she was sent on the sly every month…
- **判**：这三样只出现在**叙述层（她的心里）**，不在她对 Nigel 说出的话里（她说出的话只有 “I know.” / “It’s no big deal.” / “I’ll call later, love.” 三句）。md 把「心想的」写成「说出的」，与错-2 同源。
- **档**：**提示**（与错-2 同类；错-2 已在导航层判阻断，此处判提示）

### 错-9【提示·措辞】原句 1 说「作者先用一个**笑声**把这次登门定成家庭喜剧」——本章没有任何笑声

- **md 侧**（md:22，原句 1 · 为什么这样写）：
  > 作者先用**一个笑声**把这次登门定成家庭喜剧：妻子的矜持与丈夫的慌手慌脚并置……
- **原文侧**（`text/ch22_22.txt:32`，本块引语全文）：
  > ‘Nigel.’ The woman demurely called once for her husband to no response and then again with operatic gusto. ‘Nigeeelllll.’
  （丈夫的「慌手慌脚」在下一段 `text/ch22_22.txt:35`：`A bald man appeared behind his wife at the door. He was flustered, his cheeks red;…`，**不在本块引语内**）
- **取证**：
  ```
  CMD: /usr/bin/grep -inE 'laugh|chuckle|giggle' text/ch22_22.txt
  → 无输出
  EXIT=1
  ```
- **判**：本块引语既没有笑声，「丈夫的慌手慌脚」也在引语之外 ⇒ 既是措辞问题也是引语选短（S2 ①）。
- **档**：**提示**

### 错-10【提示·措辞】原句 1 把「operatic gusto」译成「像歌剧里的号角」

- **md 侧**（md:20，原句 1 · 中文理解）：
  > 第二声却拉长了调子，**像歌剧里的号角一样**喊了出去。
- **原文侧**（`text/ch22_22.txt:32`）：`and then again with operatic gusto`（“用歌剧般的劲头”）。
- **取证**：
  ```
  CMD: /usr/bin/grep -inE 'bugle|horn|trumpet' text/ch22_22.txt
  → 无输出
  EXIT=1
  ```
- **判**：原文是「歌剧般的劲头」，md 换成了「号角」（另一种乐器），属比喻外加。含义方向对（夸张的、带表演感的喊），不判阻断。
- **档**：**提示**

### 错-11【提示·原文未言】导航说「Matt 开着四个小时的车到哈罗盖特」

- **md 侧**（md:11）：`Matt 开着四个小时的车到哈罗盖特`
- **原文侧**（`text/ch22_22.txt:119`）：
  > Matt handed Beverley his card and **left for the four-hour drive back to London.**
- **判**：四小时是**回程**（回伦敦）；去程时长原文未言。往返同路，可接受，但严格说是原文未给的数。
- **档**：**提示**

### 错-12【提示·排版】词汇表两条例句缺收尾引号

- **md 侧**（md:82 / md:83）：
  > `| dodgy | 可疑的；来路不明的 | ‘Of course it is, Bev, they don’t send policemen up from London for one little dodgy payment like that. |`
  > `| M&S Food | 玛莎百货旗下的自有食品品牌 | ‘Hang on, Nigel. I think I dropped a card in M&S Food the other month. |`
- **判**：例句只有开引号 `‘` 没有收引号 `’`（原文有：`…like that.’` / `…the other month.`）。**全书同类 37 行 / 17 章**（ch10/11/13/16×2/19×4/21×8/22/24×3/27×2/31/33/35/37/47×3/48×5/53/54），非本章独有 ⇒ 判为全书排版口径问题，提示档，**不在本章判阻断**。
- **取证**（自制扫描，独立实现）：
  ```
  CMD: python3 - <<'PY'   # 扫全书 ch*.md 的「## 本章词汇」表格第三列
  → 行数 1458，未配对开引号行 37，涉及 17 个文件；ch22 命中 1（'M&S Food'；'dodgy' 行因 don’t 的撇号被漏检，实为同型）
  PY
  ```
- **档**：**提示**

---

## 形态核对（本书众数，非缺陷）

| 项 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 22. Harrogate` | 「N.」写法 54/54 | 无 |
| 导航项 | 5 项（一句话概括/视角/线索结构/人物弧线/叙事手法） | 众数 5 项，**名单逐字相同** | 无 |
| 子项集 | 4 项（中文理解/关键词/为什么这样写/读者视角提示） | 众数 4 项，名单逐字相同 | 无 |
| 引语块数 | 6 | 中位 7，范围 5–10；profile 3–10 | 无（在范围内） |
| 前置元信息 | `状态: 未读` / `modified` / `source_text: ch22` | 全书 54 章一致 | 无 |

⇒ **形态组无偏离，无需写偏离理由。**

## 机器层结论（R2，`2-machine.json`）

- `verdict: ok`；退出码 **0**。
- 引语逐字：**6 块 / 6 段全部 ok=true**（每块 1 段，无 `…` 缝合）。
- 块数 6；`struct_bad 0` / `empty_quote 0` / `keyword_bad 0` / `cjk_low 0`。
- 中文密度：中文理解 36–89 字（占比 0.78–0.93）；为什么这样写 57–75 字（0.79–0.91）；读者视角提示 30–52 字（0.43–0.88）；关键词 0 字（关键词层为西文词条，工具不计 CJK，非缺项）。
- 词汇表（`scripts/check_vocab.py`）：全书 FAIL 0，**ch22 无 WARN**；本章 29 行词条例句逐字命中本章（工具口径；另见错-12 的排版缺口）。
- 语料（`scripts/verify_corpus.py`）：PASS（FAIL 0）。
