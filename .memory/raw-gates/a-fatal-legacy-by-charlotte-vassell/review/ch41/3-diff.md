# 3-diff.md · ch41 三张单子（漏 / 编 / 错）

> 审查方：独立审查员（只审 ch41）。原文＝`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch41_41.txt`（唯一权威源，6221 字符）。
> md＝`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch41 margot bourne is questioned.md`。
> 档位：**阻断**＝与原文不符/缺失，必须改；**提示**＝措辞正当或轻度越界，不判红但建议改。
> 本章 md **不得**由审查方改动（本轮只落盘 `.memory/raw-gates/.../review/ch41/`）。

---

## 〇 待核问题（作业方给的四个点）— 逐条回答

| # | 待核问题 | 结论 | 依据 |
|---|---|---|---|
| ① | 本章问询的对象是谁、身份怎么被说出来的 | **问询对象＝Margot Bourne（玛戈特·伯恩），身份由「Companies House 登记董事」+「住在隔壁」+「艾米此前已与她接触过」三条说出**。md 写对了 | 原文 `text/ch41_41.txt:38`、`:44`、`:47`；md `:11`/`:13`/`:21`/`:24` |
| ② | 问询里提到的那些关于「Isolde」的资料，md 说的来源和原文是否一致 | **一致**。原文里 Isolde 的资料全部出自**艾米的独立查证**（Google 旧闻、Twitter、领英、Instagram 私密账号、粉丝小说论坛），**不在玛戈特的问询笔录里**；md 的来源归属（艾米在网上查、帖子是伊索尔德自己写的）逐项对得上 | 原文 `:127`、`:133`、`:145`；md `:13`、`:49`、`:52` |
| ③ | 问询笔录里出现的公司/机构名与数字，是否与原文逐字相符 | **本章原文根本没有出现任何公司名**（只有 Companies House、DC Noakes、the Institute 这几个机构/称谓），md 也**没有编造公司名**，更没有把 PCQV 或唱片公司牵扯进来 → **无此缺陷**。数字侧：「不到房产中介建议价的三分之一」✓（`:44`）、DC Noakes ✓（`:90`）、2011 ✓（`:127`）逐字相符 | 原文 `:38`/`:44`/`:63`/`:90`/`:127`；md `:13`/`:28`/`:35` |
| ④ | 「博物馆的两位登记董事」在原文里的准确表述，md 有没有改写 | **md 没有把它改写成「博物馆」**（md 全文 0 次「博物馆/Institute/研究所」）。原文表述是「这家**公司**的两名**登记董事**是杰拉德·伯恩先生和玛戈特·伯恩夫人，他们住在隔壁」——**登记**修饰的是公司董事，**不是博物馆董事**。md `:21` 写「这家公司的两名登记董事是杰拉德·伯恩先生和玛戈特·伯恩夫人」✓ 正确 | 原文 `:38`；md `:21`；取证命令见 §四 |

---

## 一、漏单（素读有、md 无）

### L1 · 【阻断】章末最后一句结论未进 md，且 md 反以相反方向的单向结论收束
- **原文**（`text/ch41_41.txt:154`，字符 6176–6220，全章最后一句）：
  > ‘So the killer could be one of her readers.’
- **md 侧**：全章无任何字段收在这句上。最接近的两处是
  - 导航「一句话概括」`:11`：「…以及一批**只有源头者才可能写出的细节**。」
  - 导航「人物弧线」`:14`：「…把"谁在模仿伊索尔德"的问题倒过来变成"**伊索尔德自己就是源头**"。」
  - 「一句话总结」`:107`：「…发现她写下的正是当年"假伊索尔德"讲给迪吉的那批细节。」
- **判定**：原文把这一章收在「凶手可能是她的读者之一」这个**开放假设**上（这是本章的转向点，也是后文 ch43「the forum stories are read」、ch48/ch52 揭示「凶手是读了她的论坛帖的人」的方向）；md 把它换成了「伊索尔德＝源头」的**必然结论**，并把原句丢掉。属「关键转折未出现」＋「结论被单向化」，判 **阻断**。
- **取证命令**（证明 md 内 0 命中）：
  ```
  /usr/bin/grep -nE '读者之一|她的读者|one of her readers|可能是凶手|凶手可能' \
     "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch41 margot bourne is questioned.md"
    → 0 行输出；退出码 1
  /usr/bin/grep -n 'one of her readers' \
     "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch41_41.txt"
    → 154:‘So the killer could be one of her readers.’；退出码 0
  ```
- **建议改法**：补一条覆盖原句 154 的引语块（或把末句并入原句 5/6 的分析），并在「人物弧线」里把「伊索尔德自己就是源头」降格为**被艾米的材料提示、但被马特的末句否定的可能**，两向并置。

### L2 · 【提示】艾米查证线的细节被压到两项
- **原文**（`:127`）给出六项线索：Dorchester 2011 诗歌比赛、Google 旧闻、Twitter（无私人生活）、领英（空白）、**东哈姆小学离职（几个月前）**、**Instagram 私密 + 带数字的用户名（她受审时告诉了凯厄斯）**。
- **md 侧**：导航「线索结构」`:13` 只写「伊索尔德的**领英**与**诗歌比赛旧闻**」两项。
- **判定**：非关键转折，且 md 在「读者视角提示」`:52` 补了「她的用户名、发帖时间、所在的论坛」；**不判阻断**，记提示。

### L3 · 【提示】查证段的可核查彩蛋未收录
- **原文**（`:139`）：`I found a whole series of kinky stories about Richard Nixon. Waterplaygate.` ／ Dramione＝Draco and Hermione from Harry Potter ／ `I understand from Fi some of them are spectacularly good`。
- **md 侧**：全章未提 Waterplaygate、Dramione、Fi（`spectacularly` 的例句收录了 Fi 那句，但正文分析未用）。
- **判定**：属可选取舍，**不判阻断**，记提示。

---

## 二、编单（md 有、原文无）

### C1 · 【提示】导航「人物弧线」引号内的「我记得这位警探」原文无对应语
- **md 侧**（`:14`）：「玛戈特从"**我记得这位警探**"到在关键问题上改口要律师…」
- **原文对应处**（`text/ch41_41.txt:60`，玛戈特视角）：
  > ‘Margot, please,’ she interrupted. She liked this policeman too. Less than the other one, he was a dish, but still.
- **判定**：原文只说「**她喜欢这个警探**（不如喜欢另一个，他很帅）」，**没有「我记得」**；md 用引号把一句原文不存在的话挂成人物的定场语。同句后半「改口要律师」也偏——她从头到尾**没有否认**自己报过低价（`:66` ‘Yes, why?’／`:81` ‘There’s nothing wrong with going in low on an opening gambit.’），是**拒答并要求律师**，不是改口。
- **档位**：**提示**（属改写过头，不是凭空情节；若按原文引号读则会被当成引语，边界擦到编单，故记在编单内）。

---

## 三、错单（两边都有但不一致）

### X1 · 【阻断】把「艾米材料所示的方向」写成必然结论（必要性过强＋方向单向化）
- **原文**（`:145`）：
  > She mentioned a couple of the things that "fake Isolde" told Digby in that post, but she has been writing stories where she’s clearly using bits of info from her life. Including all of the remaining details that were told to Digby.
  紧接着 `:154` 是马特的收束假设：`‘So the killer could be one of her readers.’`——**原文从未断言「伊索尔德＝源头」**，也从未断言「知道全部细节的人只可能是写出这些细节的人」。
- **md 侧**三处单向化：
  - `:11`「以及一批**只有源头者才可能写出的细节**」
  - `:14`「把"谁在模仿伊索尔德"的问题倒过来变成"**伊索尔德自己就是源头**"」
  - `:51`「**知道全部细节的人，只可能是写出这些细节的人**」
- **判定**：原文是**双向未定**（细节同源，但马特当场把凶手方向指向「她的读者」）；md 取单边并写成必然（「只可能」「只有…才」）。「只可能／只有…才」是原文没有的必要性断言。判 **阻断**（与 L1 同一轴，可一次修完）。

### X2 · 【提示】导航「一句话概括」与「一句话总结」把「联络地址是邮政信箱」写成「以邮政信箱注册」
- **原文**（`:38`）：`‘Yes, on Companies House. Interestingly, the contact address is a PO Box.’`——**注册发生在 Companies House，邮政信箱是「联络地址（contact address）」**。
- **md 侧**：
  - `:11`「一家**用邮政信箱（PO Box）注册**的公司」
  - `:107`「一家**以邮政信箱注册**、董事就住在隔壁的公司」
  - 但同一文件的「线索结构」`:13` 写的是**准确**的：「Companies House 上**联络地址为邮政信箱**的公司与两名登记董事」⇒ **同一文件内自相矛盾**。
- **判定**：主语（注册 vs 联络地址）被拉错，属性挂错对象。事实主干（PO Box、两名董事、住在隔壁）正确 ⇒ 记 **提示**（建议把两处改为「联络地址是邮政信箱的公司」）。

### X3 · 【提示】原句 2「为什么这样写」把**估价单的功能**写成「坐实」
- **原文**（`:44`）：`I’m guessing she didn’t tell Amy that she’d offered Digby less than a third of what the estate agent had advised. Matt remembered the estimate they had found early amongst Digby’s papers from his office.`
  —— 估价单＝**房产中介建议价**这个基准；「她报了不到三分之一」始终是**马特的猜测**，原文没有任何「坐实」。
- **md 侧**（`:30`）：「紧接着又让现成的估价单**把它坐实**——推断是猜的，物证却是真的。」
- **判定**：把物证（一份早先在迪吉文件里找到的估价单）的作用从「提供比较基准」放大成「证实猜测成立」，属**功能归属写反**（物证没有证实报价数额，只提供了参照价）。记 **提示**。

### X4 · 【提示】原句 2 的分析越出引语边界
- 引语块只取 `:44` 的**第一句**；md 的「为什么这样写」`:30` 与「读者视角提示」`:31` 的主要对象是**引语之外紧接的下一句**（估价单那句）。
- 按 R4「讲的是引语之外的上下文 → 引语选短」：本块**仍以引语内句为主**（“我猜”的对冲是引语内的），属轻度越界，不判阻断；**建议**把估价单那句补进引语（`:44` 两句连着取），或把分析重心移回引语内。

### X5 · 【提示】原句 4「为什么这样写」把「nasty men」直接等同于警察
- **原文**（`:93`）：`No, Halloumi. The nasty men aren’t attacking Mummy. I want a solicitor.`——原文**未指明**「the nasty men」是谁。
- **md 侧**（`:44`）：「当事人却转向一只狗说话，还**顺手把警察称作"坏男人"**」。
- **判定**：语境（正在问询的两名男警探）下推断合理，但**原文未作此等同**，属归属越权断言。记 **提示**（建议加限定，如「显然指的是屋里这两位」）。

### X6 · 【提示】原句 6「中文理解」中「作者」与「说话人」混指
- **md 侧**（`:56`）：「艾米说伊索尔德对中世纪骑士这类东西有点执念，**作者自己先打了个折扣**，"大概是名实相合那回事"。」
- **原文**（`:151`）：`Isolde’s got a thing, probably nominative determinism, about medieval knights and shit.`——打折扣的 “probably” 出自**艾米之口**。
- **判定**：本书 md 惯例里「作者」＝小说作者（`ch39`/`ch43` 均此用法），同一块内又用「说话人」指艾米，读者会误读为「作者=艾米」。属表述含混，记 **提示**（建议改成「艾米先打了个折扣」或明写「作者把这层折扣写进了艾米的话里」）。

### X7 · 【提示】导航「视角」的场次计数与「叙事手法」不齐
- md `:12`：「第三人称限知，**三段切换**——警局办公室里的问询（马特、罗比、玛戈特…），以及案发室中马特与艾米对线索的复盘。」——只枚举了**两处**地点。
- md `:15`：「**两处**星号分隔线把一段推进切成**三场**」——场景数是 3（原文 `:52`、`:113` 两处 `* * *`，已核）。
- **判定**：「三段切换」与「切成三场」本身不矛盾，但导航栏只列出两组地点，读者数不出三段。记 **提示**。

### X8 · 【提示】词汇表释义：「anachronistic」第二义不对
- **原文语境**（`:32`）：`‘Out Oxford way. He was a character. He was purposefully anachronistic.’`——指迪吉写信**刻意不合时宜/用旧式做派**。
- **md 侧**（`:67`）：`anachronistic | 刻意不合时代的；**反潮流的**`——「反潮流」（counter-trend）不是 anachronistic 的义项。
- **判定**：前半义正确，后半义多余且不确。记 **提示**（建议删「反潮流的」或改为「有意用旧式做派的」）。

### X9 · 【假红/基线】词汇分档工具对本章报的 4 条「基础档疑含超纲词」不判红
- `python3 scripts/check_vocab.py "<书目录>"` 输出：`ch41 … [基础] 基础档疑含超纲词「character」/「interview」/「attacking」/「online community」`——同一模式在 ch26/33/34/39/46/50 亦命中，**全书同型**，脚本 `--- FAIL (0) ---`、退出码 0。
- **判定**：**假红（基线问题）**，不算本章缺陷，不要求改 md。
- 另：`deceased` 收在 ⭐⭐⭐ 略偏高（犯罪小说语境属常用正式词），工具未报警，**提示级**。

---

## 四、取证命令汇总（凡「查无」类断言均附命令 / 输出 / 退出码）

```
# E1 md 内无「分部/分部名」字样
/usr/bin/grep -nE '分部|SATURDAY|FRIDAY|MONDAY|FRIDAY IN MAY' \
  "…/ch41 margot bourne is questioned.md"   → 0 行输出；退出码 1

# E2 md 内无「博物馆 / Institute / 研究所 / PCQV / 唱片」
/usr/bin/grep -nE '博物馆|Institute|研究所|PCQV|唱片|label|唱片公司' \
  "…/ch41 margot bourne is questioned.md"   → 0 行输出；退出码 1

# E3 md 内无「读者之一 / one of her readers」类表述
/usr/bin/grep -nE '读者之一|她的读者|one of her readers|可能是凶手|凶手可能' \
  "…/ch41 margot bourne is questioned.md"   → 0 行输出；退出码 1

# E4 原文本章无 museum / PCQV / collector
/usr/bin/grep -inE 'museum|PCQV|collector' "…/text/ch41_41.txt"   → 0 行输出；退出码 1

# E5 原文章末句在位
/usr/bin/grep -n 'one of her readers' "…/text/ch41_41.txt"
  → 154:‘So the killer could be one of her readers.’；退出码 0

# E6 词汇例句逐字核对（自写脚本，读 text/ 原文做子串计数）
  → 26/26 例句逐字命中，且每条例句在 ch41_41.txt 中恰好命中 1 次（非 1 计数 = 0）
```
> 工具说明：按规则用 `/usr/bin/grep` + 显式路径，**不用 `git grep`/rg**（`text/` 被 `.gitignore` 排除，会造成假零命中）。

---

## 五、单子小结

| 单子 | 条数 | 其中阻断 |
|---|---|---|
| 漏 | 3（L1 阻断；L2、L3 提示） | **1** |
| 编 | 1（C1 提示） | 0 |
| 错 | 9（X1 阻断；X2–X8 提示；X9 假红） | **1** |
| **合计** | **13** | **2** |
