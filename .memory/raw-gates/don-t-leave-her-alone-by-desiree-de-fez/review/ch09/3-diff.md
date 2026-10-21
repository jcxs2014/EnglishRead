# ch09 人工审查 · R3 对账 + R4 逐块对应

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch09 chapter 9.md`（106 行）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch09_chapter_9.txt`（21 行 / 474 字符 / `wc -w` = 78 词 / 6 个自然段）
- R1 素读：`review/ch09/1-suread.json`（已先于 md 完成）
- R2 机器层：`review/ch09/2-machine.json`（`bash scripts/chapter.sh … --json`，**EXIT=0**）
- 审查人：DSH-Mac

---

## 0. 原文分段与字符区间（唯一真值）

| 段 | text 行 | 区间 | 逐字内容 | 类型 |
|---|---|---|---|---|
| P1 | 1 | [0,1) | `9` | 章号行 |
| P2 | 6 | [6,283) | `One of Diana’s back pockets started to vibrate. She stopped examining herself and picked up, unconcerned that her hand was covered in blood. She said, “Hello,” listened, didn’t respond. “I have to call you back,” she said, almost to herself, sliding the iPhone into her pocket.` | 叙述＋内嵌引语 |
| P3 | 9 | [286,309) | `“They can’t find Alba.”` | 纯对白·未标说话人 |
| P4 | 12 | [312,369) | `“What?” Carlos asked, still covering Diana with the coat.` | 对白＋**标名说话人** Carlos |
| P5 | 15 | [372,395) | `“They can’t find Alba.”` | 纯对白·未标说话人（与 P3 逐字相同） |
| P6 | 18 | [398,438) | `“What do you mean they can’t find Alba?”` | 纯对白·未标说话人 |
| P7 | 21 | [441,473) | `“Mom just said Alba is missing.”` | 纯对白·未标说话人 |

`wc -w` = 78；自然段 6（P2–P7）；纯对白段 4（P3/P5/P6/P7）；含叙述段 2（P2/P4）。

---

## 1. R2 机器层（原始结果）

```
EXIT=0
counts: blocks=5  segments=5  segment_miss=0  struct_bad=0  empty_quote=0  keyword_bad=0  cjk_low=0
form:   h1="09. Chapter 9"(h1_shape_ok)  nav_count=5(ok)  subitems_modal=[中文理解,关键词,为什么这样写,读者视角提示]
        block_median=7.0  block_range=[5,8]  profile=novels  baseline=book
issues: { "struct": [], "empty_quote": [], "keyword": [], "cjk": [], "quote_long": [] }
```

**机器层盲区（本章实测）**：`2-machine.json` 的 `quotes[1].text` 回显的是**原文侧**的 `…she said, almost to herself, sliding the iPhone `，说明 chapter.sh 对引语只比 52 字符指纹／或只回显语料侧文本，短引语的**尾部**不被逐字覆盖。故机器 EXIT=0 不能代替逐字判定，本轮另跑整串比对（见 §2）。

**自跑整串逐字比对（比机器层更严）**：

```
原句1: OK 逐字命中 text[6:146]   len=140
原句2: OK 逐字命中 text[147:283] len=136
原句3: OK 逐字命中 text[312:369] len=57
原句4: OK 逐字命中 text[398:438] len=40
原句5: OK 逐字命中 text[441:473] len=32
⇒ 5/5 块整串逐字命中，0 处逐字缺陷。
```

**词汇例句逐字核对**：11/11 条全部是原文的连续逐字片段（`unconcerned / examining / listened / respond / covering / sliding / pocket / blood / coat / missing`），无生造词条、无跨标签拼接。

---

## 2. R3 三张单子

### 2.1 漏单（关键事件未出现在 md）

**无漏项。** 原文 6 个自然段的事件全部有对应：手机震动/接听/“Hello,”/不回应/“I have to call you back,”/滑进口袋 → 原句 1＋2；Carlos 问 “What?” 并用外套盖住她 → 原句 3；「They can’t find Alba.」出现两次 → 原句 3 分析（「原样说了两遍」）；追问「什么意思」→ 原句 4；末句转述母亲 → 原句 5；章型/弧线/手法 → 导航 5 项。

留白项按 R3 规则（md 写明取舍理由即不算漏）：原文对来电者、对 P3/P5/P6/P7 的说话人均不点名；md 在 **md:39** 写明「电话是谁打来的？读到后面再回头对答案」，未把留白补成事实 ⇒ 不判。

### 2.2 编单（md 有、原文无）

| # | md 侧（逐字） | text 侧（逐字） | 判定 |
|---|---|---|---|
| C1 | md:49「紧接着**丈夫**用一个字的疑问打断」 | text:12 `“What?” Carlos asked, still covering Diana with the coat.`；全书英文一律称 Diana 的伴侣为 **partner**：`text/ch01_chapter_1.txt:12` `Her partner was going to be in Madrid all day`；`text/ch05_chapter_5.txt:540` `his partner’s family`；`text/ch10_chapter_10.txt:12` `his partner sliced down the middle`；`text/ch10_chapter_10.txt:894` `his partner and his mother-in-law`。`grep -nw husband` 全书命中处（ch02:1、ch05:4、ch10:3、ch14:1）均为 Juan／Carmen 的亡夫／bingo 女人们的丈夫 | **提示**：「丈夫」是原文未使用的关系断言；但 `text/ch10_chapter_10.txt:879` `Carlos raised his voice to his mother-in-law` 保留了已婚读法，故不判阻断，建议改「伴侣」 |
| C2 | md:49「**电话那头**那句「他们找不到 Alba 了」**在整通电话里**原样说了两遍」 | text:6 末句 `“I have to call you back,” she said, almost to herself, sliding the iPhone into her pocket.`（电话在 P2 结束）＋ text:9 / text:15 `“They can’t find Alba.”` | **阻断**：原文未显示这两句出自电话；P2 明写她说完就把手机滑进口袋。md 自身 md:37 又写「为什么**被挂断**」——与 md:49 自相矛盾 |
| C3 | md:57「**她**追问，这句话到底什么意思。」 | text:18 `“What do you mean they can’t find Alba?”`（未标说话人） | **阻断**：说话人错配。P6 的受事是 P3/P5 的说话人，而该说话人是 Diana（见 §3 归属链），故问话人是现场另一人 Carlos。md 把「被问的人」当成「问话人」 |
| C4 | md:69「**对方**说，妈妈刚说 Alba 不见了。」 | text:21 `“Mom just said Alba is missing.”`（未标说话人） | **阻断**：说话人错配。P7 是对 P6 的回答，说话人是 Diana、对象是 Carlos；`Mom`＝Diana 的母亲 Carmen（`text/ch08_chapter_8.txt:102` `My mom.`）。md 把「听的人」当成「说的人」 |
| C5 | md:11「接起来只有一句「他们找不到 Alba 了」」；md:12「恐惧第一次不在她身上，而在**电话那头**」；md:14「**Carlos 全程只有一个「什么？」**，衬出她才是唯一听懂的人」；md:106「只用**一轮电话问答**就把恐慌…」 | text:12 `“What?” Carlos asked, still covering Diana with the coat.`＋text:18 `“What do you mean they can’t find Alba?”` | **阻断**：C2–C4 的下游复述。Carlos 在本章有**两**句台词（text:12、text:18），md 断言他全程只有一句 |

### 2.3 错单（两边都有但不一致）

| # | md 侧（逐字） | text 侧（逐字）/ 实测 | 判定 |
|---|---|---|---|
| E1 | md:14「被一句**五个词**的短句拽成惊惶的追问者」 | text:9 / text:15 `“They can’t find Alba.”` → `printf "They can't find Alba.\n" \| wc -w` = **4** | **提示**：按标准分词为 4 词；若把 `can’t` 拆成 can+not 才得 5，属计数口径歧义（非情节事实错），建议改「四个词」。（若该短句指末句 `“Mom just said Alba is missing.”` 则是 6 词，两种所指都不是 5） |
| E2 | md:15「全章只有六个自然段，其中**一半**是纯对白」 | 实测：自然段 6 ✓，纯对白段 **4**（P3/P5/P6/P7），含叙述段 2（P2/P4）⇒ 2/3 | **提示**：「六个自然段」✓；「一半」应为「四段／三分之二」 |
| E3 | md:25「偏偏她的**语气还很不耐烦**」 | text:6 `unconcerned that her hand was covered in blood`＝漠不关心／毫不在意（非「不耐烦」）；且与本块自己的中文理解 md:21「一点也不为那手上的血担心」矛盾 | **提示**：措辞与其余表述不一致 |
| E4 | md:61「语法上是一个规整的**反问**」 | text:18 `“What do you mean they can’t find Alba?”`＝信息询问句（要求解释），非反问句 | **提示**：术语用词不准 |

---

## 3. R4 逐块对应（每块的子项是不是在讲这一句引语）

| 块 | 引语（text 区间） | 中文理解 | 关键词 | 为什么这样写 | 读者视角提示 | 三问（主语／受事／归属） |
|---|---|---|---|---|---|---|
| 原句 1 | text[6:146] | ✓ 在讲本句（查看自己、手上血、手机震动、接听、不担心） | ✓ 3/3 落本句内 | ✓ 讲本句写法；惟「不耐烦」措辞偏（E3） | ✓ 讲 unconcerned 的性质 | ①主语：One of Diana’s back pockets（物主链落到 Diana）；她 stopped examining / picked up ②受事：她自己（examining herself）、她的血（her hand was covered in blood）③归属：her hand 属 Diana；unconcerned 修饰「picked up」的态度，方向正确 |
| 原句 2 | text[147:283] | ✓ 逐项对应（“Hello,”／听／没回答／回拨／塞回口袋／几乎像自言自语） | ✓ 3/3 落本句内 | ✓ 讲「留白」与「几乎像自言自语」；「为什么被挂断」与 md:49 冲突（并入 C2） | ✓ 把「电话是谁打来的」列为悬念，与原文不点名来电者一致 | ①主语：She(Diana) ②受事：Hello／回应（didn’t respond）；almost to herself＝说给自己 ③归属：to herself 方向正确 |
| 原句 3 | text[312:369] | ✓ 在讲本句（Carlos 问「什么？」＋用外套遮住她） | ✓ 3/3 落本句内 | ✗ **半块不在讲本句**：前半把 P3/P5 的发言人写成「电话那头」且称「在整通电话里…两遍」（C2，阻断）；「丈夫」（C1，提示） | ✓ 讲 coat 动作与本章开头血手的呼应 | ①主语：Carlos（asked）②受事：外套盖住 Diana（covering Diana with the coat）③归属：covering 的方向＝Carlos→Diana，正确；still＝「还在」✓ |
| 原句 4 | text[398:438] | ✗ **说话人错配**（C3，阻断）：应为 Carlos 追问 | ✓ 2/2 落本句内 | △ 前半在讲本句（短句、问句结构），后半「对方马上给出的解释」方向随错配而反 | ✓ 讲问句里「他们」＝搜索方 | ①主语：问话人＝Carlos（非 Diana）②受事：they can’t find Alba 这一说法（被问者是 Diana）③归属：「they」＝未点名的搜索方，不是 Diana 一方 |
| 原句 5 | text[441:473] | ✗ **说话人错配**（C4，阻断）：应为 Diana 对 Carlos 说；引语内容翻译正确 | ✓ 3/3 落本句内 | △ 「转述／信息迟到」在讲本句 ✓；「她一直在追问含义」随错配而反 | ✓ 讲「危险挪到家人身上」（Alba＝Diana 的姐妹，`text/ch10_chapter_10.txt:207` `It was the same with Diana and her sister`） | ①主语：说话人＝Diana（回答 P6）②受事：Alba is missing 这一消息 ③归属：`Mom`＝Diana 的母亲 Carmen（`text/ch08_chapter_8.txt:102` `My mom.`）＝消息来源／转述者，不是本章说话人 |

### 3.1 固定三问的归属链（本章归属判定的完整证据）

1. **电话在 P2 结束** —— text:6 末 `“I have to call you back,” she said, almost to herself, sliding the iPhone into her pocket.`：她说完把手机滑进口袋 ⇒ P3–P7 不可能是通话内容。
2. **现场只有两个人** —— ch08 场景延续：text:12 的 `still covering Diana with the coat` 对应 `text/ch08_chapter_8.txt:279` Diana 说 `cover me up with the coat for a minute`；该段 kids 在草地自己玩（`text/ch08_chapter_8.txt:186` 前后），场中对话双方＝Diana 与 Carlos。
3. **P4 是原文唯一点名的说话人** —— text:12 `“What?” Carlos asked, still covering Diana with the coat.` ⇒ 对 P3 的反应者是 Carlos ⇒ **P3 的说话人＝Diana**。
4. **文体惯例：未标说话人的行按「另一方应答」交替** —— `text/ch08_chapter_8.txt:261` `“Did you do it to yourself?”` ↔ :263 `“What do you mean did I do it to myself? I didn’t do anything. Why would I do something like that?”`（未标，应为另一人）；`text/ch08_chapter_8.txt:216`（未标，Diana）→ 下一行才标 `Carlos started to sob` ⇒ 未标行＝在场另一人。
5. **P6 的受事是 P3/P5 的说话人**（＝Diana）⇒ **P6 说话人＝Carlos**（第 3 步已排除他另有台词）。
6. **P7 回答 P6** ⇒ **P7 说话人＝Diana**；`Mom`＝Diana 的母亲 Carmen（`text/ch08_chapter_8.txt:102`、`text/ch10_chapter_10.txt:210`）。

⇒ 归属链结论：**P3＝Diana、P4＝Carlos、P5＝Diana、P6＝Carlos、P7＝Diana**；来电者原文始终未点名；母亲＝消息来源（转述者），非本章说话人、也非失踪者。
⇒ md 的「电话那头说」「她追问」「对方说」「Carlos 全程只有一个『什么？』」「一轮电话问答」「接起来只有一句『他们找不到 Alba 了』」全部与之冲突（C2–C5）。

---

## 4. 形态组核对

| 项 | 现场实测 | 结论 |
|---|---|---|
| frontmatter | `状态: 未读` / `modified: "2026-10-21"` / `source_text: ch09` | ✓ 与同书 18 章一致 |
| H1 | `# 09. Chapter 9` | ✓ 与同书众数 `# NN. Chapter N` 一致 |
| 导航项数 | 5 | ✓ 同书众数 5 |
| 精读子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示（4 项齐） | ✓ 与众数一致 |
| 块数 | 5（众数 7，range 5–8） | ✓ 本章型（原文仅 78 词）已知例外 |
| 编号 | 1–5 连续 | ✓ |
| 块序 vs 原文顺序 | 6 → 147 → 312 → 398 → 441 | ✓ 递增，与原文顺序一致 |
| 引语形态 | 每块单段落、无 `…` 缝合、无跨话轮拼接、无一行多句 | ✓ |
| 引语长度 | 23 / 23 / 9 / 8 / 6 词 | **已知例外**：原文仅 78 词，达不到创建卡建议的 30–70 词；判据改看「逐字／单段落／块序／编号」，四项皆过 |
| 重复句处理 | 原文 text:9 与 text:15 逐字相同；md 引语层**只引一次**，另一处放在原句 3 的分析文字里复述「原样说了两遍」 | ✓ 次数复述忠实原文；非「重复块」缺陷（归属措辞问题另计 C2） |

---

## 5. 收口（cliffhanger）核对

- 末句 `“Mom just said Alba is missing.”`（text:21）在 md 中的读法：原句 5 中文理解「对方说，妈妈刚说 Alba 不见了」＋ 为什么这样写「一个严重的坏消息被包装成转述」＋ 读者视角提示「危险从 Diana 身上挪到了家人身上」＋ 一句话总结「把恐慌从 Diana 自己的身体挪到了她的家人身上」。
- ⇒ **没有读成「母亲失踪」**：「妈妈」始终是转述者/消息来源，`Alba 不见了` 才是缺失项 ✓。
- 支撑：`text/ch10_chapter_10.txt:6` `There were five of them, not six. Alba was missing.`（后续才坐实 Alba 失踪）、`text/ch10_chapter_10.txt:207` `It was the same with Diana and her sister`（Alba＝姐妹＝家人）✓。
- 唯一瑕疵：末句的说话人被写成「对方」，与归属链冲突（C4，阻断）。

---

## 6. R5-补：零命中类断言的自证（命令＋输出＋退出码）

```
$ /usr/bin/grep -c "Alba" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
… ch09=4 / ch02=55 / ch03=4 / ch04=3 / ch05=47 / ch06=4 / ch08=2 / ch10=17 …（ch00/ch01/ch07=0）

$ /usr/bin/grep -nw "husband" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
ch02:1  ch05:4  ch10:3  ch14:1        # 命中处均为 Juan／Carmen 亡夫／bingo 女人们的丈夫，无 Carlos

$ /usr/bin/grep -nw "partner" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
ch01:12  ch05:540  ch10:12  ch10:894   # Diana 的伴侣一律称 partner（Carlos）

$ /usr/bin/grep -n "mother-in-law" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
ch02/ch04/ch05/ch10×2/ch13×2/ch17      # 指 Carmen（Carlos 的 mother-in-law）

$ /usr/bin/grep -n "find Alba" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
ch09:9  ch09:15  ch09:18               # 全书只有本章三处

$ /usr/bin/grep -n "Alba is missing" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
ch09:21  ch10:6                        # 末句与后续坐实

$ /usr/bin/grep -n "pathologically obsessed" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
ch10:432                                # 支撑 md「强迫症患者」
```

（全部使用 `/usr/bin/grep` 显式路径；`text/` 被 .gitignore，不用 `git grep`。上述命令退出码均为 0＝有命中；无任何「全书查无」型断言。）

---

## 7. 全书查无类断言（带命令、输出、退出码）

- **「Carlos＝丈夫」在全书英文中查无此称谓**：
  ```
  $ /usr/bin/grep -nw "husband" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/*.txt
  （输出：ch02:1 / ch05:4 / ch10:3 / ch14:1，全部为 Juan、Carmen 亡夫、bingo 女人们的丈夫）
  退出码 0
  $ /usr/bin/grep -nw "husband" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch09_chapter_9.txt
  （无输出）
  退出码 1
  ```
- **「电话那头说了两遍」类断言无法用文本查无**（原文确实有两处同句），故以 §3.1 的归属链判定，不作查无式断言。

---

## 8. 本轮处置

- **只出指令不改稿**：未修改任何 `ch*.md` / `00_*.md`；未 `git add` / `commit` / `push`。
- 待改点（供生产侧执行，见 `4-verdict.md` 判定表）：C1–C5（1 项提示＋4 项阻断）、E1–E4（4 项提示）。
