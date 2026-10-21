# 3-diff.md · ch23《Eulalia's House》三张单子

> 审查方：独立审查员（本次会话）
> 语料：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch23_23.txt`（14267 字符 / 465 行）
> md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch23 eulalia watches the footage again.md`
> 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch23/`
> 读取顺序：**先素读原文落盘 1-suread.json，再开 md**（R1 已完成，见 1-suread.json）

---

## 一、漏（素读有、md 无）

### L1 ·【阻断（并入 E1 一并修）】Eulalia「刻意隐瞒」的实据——关掉标签页这件事，md 全篇没有

- 原文 `text/ch23_23.txt:410`：
  > `‘I’m not obsessed, see.’ Eulalia closed the tab. ‘I’m going to read instead.’`
- 原文 `text/ch23_23.txt:443`：
  > `‘Let’s just have quality us time.’ Mel looked at her sister picking over her lunch, reading some brain rot story on her laptop.`
- md 现状：全篇**没有任何一处**提到「她把录像关掉」这个动作。录像在原文里是一个**被刻意关掉、换成别的东西**的物件，而 md 的写法把录像写成「她从头到尾都在看」（见 E1）。
- 判据依据：本章专属判据「她从录像里读出了什么、又刻意隐瞒了什么」——「关掉标签页」正是隐瞒的物证，缺失即漏；且其缺失直接生成了 E1 的错。

### L2 ·【提示】录像里 Callie 的那句「I rather wish it was.」（与「Chivalry isn’t dead.」构成录像自身的反讽）

- 原文 `text/ch23_23.txt:112`：`Chivalry isn’t dead.`
- 原文 `text/ch23_23.txt:125`：`You know, right now I rather wish it was.`
- md 现状：导航「线索结构」只列了 `Chivalry isn’t dead`，**没有**记录紧接着的否定句；9 个引语块里也没有引用 `I rather wish it was`。结果：md 呈现的录像底色只剩「骑士精神」的正面，抹掉了录像本身的喜剧底色（女帽匠祝酒的男人被一拳打倒后，她说「我倒希望骑士精神已经死了」），也抹掉了欧拉莉亚读到的其实是「一份不可信的浪漫范本」这一层。
- 不判阻断的理由：md 在 block 2 的「为什么这样写」里写到了「拒绝一个醉醺醺的求婚者」，录像内容有部分覆盖；且本章 9 块不必覆盖每一句。

### L3 ·【提示】地下室真正落地的两件事：梅尔自己开口唱、以及「我们能发财了」

- 原文 `text/ch23_23.txt:373`：`Sonikk played the track and Mel began to sing.`
- 原文 `text/ch23_23.txt:376`：`‘Fuck me, this is good. We’re all going to be so rich,’ Sonikk said, listening back to Mel nailing the vocals in one perfectly haunting take.`
- 原文 `text/ch23_23.txt:316`：`‘No one would care if you were.’ … ‘a nascent proclivity for bisexuality would make you a much more interesting person. Might be worth pretending you are in the next round of interviews anyway. We can get you a PR girlfriend for a few weeks.’`
- md 现状：md 在导航「叙事手法」里以「谁在唱歌」一笔带过，但**没有任何一处**把「这段录音里真正开口唱的是梅尔」写成事实；`‘We’re all going to be so rich’` 与「PR 女友」这两处也没进任何引语块。
- 不判阻断的理由：本书 `ch42 mel is the voice and eulalia is the face`（章名）表明「梅尔才是声音」这条秘密在 ch42 正式展开；本章不重复展开不构成缺失。但**本章自己**把它写成了叙述里未点破的暗线时，读者会缺少落点——建议在 block 7 或导航「一句话概括」里补一句可核对的事实（梅尔在录音棚里唱，Sonikk 听到的是她的声音）。

---

## 二、编（md 有、原文无）

**本栏 0 条。** 依据（取证三件套）：

```
$ python3 脚本对 md 的 9 块引语按 “…” 拆段独立取证，逐段在 text/ch23_23.txt 中定位
  → 10/10 段逐字命中（block 3 的两段同在 text/ch23_23.txt:151，其中 “…” 是作者自己的省略号，非拼接）
$ bash scripts/chapter.sh "<md>" --json   → counts.segment_miss=0, struct_bad=0, empty_quote=0, keyword_bad=0, cjk_low=0
$ 词汇表 28 条例句逐条比对原文 → 27 条命中，1 条为截断（见 E6），0 条凭空
```

md 中出现的数字/日期全部与原文一致，无凭空数字：`at least an hour and a half of peace` / `maybe two if we're lucky` / `100 per cent` / `in five years' time` / `a thousand ships` / `two junctions of the M42` / `ten minutes ago` / `Sunday` / `for a week` / `one perfectly haunting take`（均见 `text/ch23_23.txt:322 / 331 / 355 / 358 / 358 / 386 / 416 / 340 / 376`）。

---

## 三、错（两边都有但不一致）

### E1 ·【阻断】md 断言「章节结束时她仍在看同一段录像」——与原文相反

- md 原文（block 1「读者视角提示」）：
  > `留意这个 “again”——全章结束时她仍然在看同一段录像，这中间还隔着一次出门和一顿午饭。`
- md 原文（block 9「为什么这样写」）：
  > `作者让欧拉莉亚从头到尾没抬眼：这个动作说明她此刻全部心思还留在屏幕上那段录像里，姐姐在她身边说的话只被处理成一条条可以批阅的请求。`
- 原文 `text/ch23_23.txt:410`：
  > `‘I’m not obsessed, see.’ Eulalia closed the tab. ‘I’m going to read instead.’`
- 原文 `text/ch23_23.txt:443`：
  > `‘Let’s just have quality us time.’ Mel looked at her sister picking over her lunch, reading some brain rot story on her laptop.`
- 判定：录像在午餐前**已被她主动关掉**，午餐时她在看「brain rot story」。md 把它写成「仍在那段录像里」，与原文直接冲突。
- 附带伤害：这条错误正好落在本章专属判据的靶心——**「刻意隐瞒」被写反了**。原文是「被追问就关掉、换成诗集」（隐瞒），md 写成「始终在看」（不隐瞒）。同一处错误还连带 L1。
- 修法方向：block 1 的 tip 可改为「她后来把标签页关掉了」；block 9 的 why 改为「她没抬眼，因为此刻她要的是被安排好的生活，而录像已经被她换成了别的东西——姐姐不知道那部片子早就被她关掉了」。

### E2 ·【阻断】block 5 把 `‘Good.’` 判给了梅尔；按原文语序与本章一致的行文体例，这句是欧拉莉亚说的

- md 原文（block 5「中文理解」）：
  > `梅尔应了一声“好”。欧拉莉亚抬头看着姐姐，开始在房间里来回踱步，说：我只是觉得她懂我，Cal 理解我，她明白我想要做的事。`
- md 原文（block 5「为什么这样写」）：
  > `……而梅尔听得清清楚楚，却只回了一个“好”。`
- 原文 `text/ch23_23.txt:295`：`‘I like her vibe.’ Eulalia jumped up in defence of Callie’s honour.`
- 原文 `text/ch23_23.txt:298`：`‘I know you do, that’s why we’ve got her on board. She sent over the signed contract and the NDA, by the way, so you can continue to play with her without her leaking your bra size to the Mail.’`
- 原文 `text/ch23_23.txt:301`：`‘Good.’ Eulalia looked up at her sister and started pacing. ‘I just feel like she gets it. Cal understands me. She understands what I’m trying to do.’`
- 原文 `text/ch23_23.txt:304`：`‘Are you OK? You seem a bit manic.’`
- 判定依据（三条互相印证）：
  1. **语义**：紧挨 `‘Good.’` 之前的 `text/ch23_23.txt:298` 是**梅尔自己**的话（她解释为什么把 Callie 弄上船、 NDA 已签）。梅尔不可能“回应自己刚说的上一句”并说 `Good`；而欧拉莉亚正是在听到「NDA 已签、可以放心玩」之后说 `Good`，语意顺。
  2. **行文体例**（本章内三处同型）：`text/ch23_23.txt:289` `‘What?’ Eulalia asked, turning round to look at her sister.`｜`text/ch23_23.txt:295` `‘I like her vibe.’ Eulalia jumped up…`｜`text/ch23_23.txt:410` `‘I’m not obsessed, see.’ Eulalia closed the tab.`——引语在前、随后的动作属于同一说话人。`text/ch23_23.txt:301` 同型，故 `‘Good.’` 归欧拉莉亚。
  3. **话轮**：`text/ch23_23.txt:304` 是梅尔发言（`‘Are you OK? You seem a bit manic.’`），若 `‘Good.’` 是梅尔的，则梅尔连续占了两轮而欧拉莉亚只在一段里说半句，与文本的对话轮转不符。
- 附带伤害：block 5 的「为什么这样写」整段结论（「梅尔看得清清楚楚，却只回了一个『好』」）建立在错误的说话人上；且原文里梅尔对这段的回应其实是 `text/ch23_23.txt:304` 的「你看起来有点 manic」。

### E3 ·【提示】导航「人物弧线」的「让卡莉到家里吃饭」——提议属实，落点不同

- md 原文（导航·人物弧线）：
  > `……最后却主动开口要钱、答应让瑜伽老师进家、让卡莉到家里吃饭——依赖从情感挪到了物质和地盘上；`
- 原文 `text/ch23_23.txt:446`：`‘Callie’s coming over for dinner, by the way. Thought we could brainstorm or whatever.’`
- 原文 `text/ch23_23.txt:449`：`‘Here?’ Mel wasn’t keen on having her in the house. She didn’t want her poking around or trying to get her sister into the recording studio downstairs for a cheeky preview.`
- 原文 `text/ch23_23.txt:452`：`‘I thought we could go out?’`／`text/ch23_23.txt:455`：`‘Sure.’`
- 判定：欧拉莉亚确实提出了「卡莉来家里吃饭」，但结果是**改成出去吃**（`text/ch23_23.txt:452-455`），家里吃饭并未成立。导航写成既成事实（「让卡莉到家里吃饭」）与原文落点不符；建议改为「提议卡莉来家里吃饭、最后改成出去吃」。
- 另：`text/ch23_23.txt:449` 里梅尔不想让 Callie 进家，恰恰与「依赖挪到地盘上」的方向相反，导航这一句的收尾论断与原文的方向也需要一并复核。

### E4 ·【提示】block 4「为什么这样写」里「一个同行者平平常常的一句实话」与本块「读者视角提示」自相矛盾（说话人指代）

- md 原文（block 4「为什么这样写」）：
  > `……在满篇崇高与浪漫之后，一个同行者平平常常的一句实话，把话拉回地面。`
- md 原文（block 4「读者视角提示」）：
  > `注意这句是对同行者说的，不是对镜头说的宣言。`
- 原文 `text/ch23_23.txt:279`：`Callie:`
- 原文 `text/ch23_23.txt:281`：`I don’t know, Monty. It’s rough out there.`
- 判定：本块「中文理解」写的是「**卡莉**朝主持人说了一句大实话」，正确；但「为什么这样写」用「一个同行者……一句实话」，而同一块的 tip 已把「同行者」定义为**被说话的人**（＝主持人 Monty Don）。两处对「同行者」的指代不一致，导致 why 段可被读成「这句是主持人说的实话」——而原文里说这句的是卡莉。建议把 why 段的「一个同行者」改成「一个同行者**听来的**实话」或「她自己那句实话」，消除歧义。

### E5 ·【提示】block 8 的「为什么这样写」把引语之外的身世内容并入本块，且「眼前这位卡莉的男朋友」在原文无据

- md 原文（block 8「为什么这样写」）：
  > `作者让这段自白紧跟在卡莉把那位前任骂作蠢人的那句吐槽之后，读者由此听出欧拉莉亚读到的根本不是那段录像的事实，而是它的形状：一个关于风度与庄园的童话。`
- 原文 `text/ch23_23.txt:398`（本块引语所在行）：`‘I’m not obsessed. I just think she’s terribly romantic. Her boyfriend will be a knight one day. An actual knight. His family have a big house in the country.’`
- 原文 `text/ch23_23.txt:404`（身世内容所在行，引语之外）：`……His grandfather inherited this house and stuff because someone else was illegitimate. … His family are descended from a branch of the Plantagenets and therefore from Melusine.`
- 判定两处：
  1. **身世不在引语里**：「金雀花血脉」「祖父因非婚生而继承房子」出自 `text/ch23_23.txt:404`，是欧拉莉亚**另一段**台词。md 在「为什么这样写」里把它们当作本块引语的延伸来讲（另见 4-correspondence.md 第 8 块）。
  2. **「眼前这位卡莉的男朋友」的身份在原文未指明**：录像里 Callie 唯一出现过的男性是 Max（求婚者，且被她称作「my stupid ex」，`text/ch23_23.txt:151`）与被 Max 称为「The new man」的 Caius（`text/ch23_23.txt:68`）。原文从未说明 `Her boyfriend` 是谁；md 的「录像里的求婚虽然是闹剧，**眼前这位**卡莉的男朋友却……」暗示这是另一位在场者，此暗示无原文依据。建议改成「录像里那位求婚者的男朋友身世（原文未点明是谁）」或直接不点身份。

### E6 ·【提示】词汇表 `lasagne` 例句是截断引文，却以完整引号收尾

- md 原文（本章词汇·⭐ 基础）：
  > `| lasagne | 千层面 | ‘Can’t I have lasagne? Or cottage pie?’ |`
- 原文 `text/ch23_23.txt:416`：
  > `‘Chicken again. Really. I never want to see another grilled chicken fillet again. Can’t I have lasagne? Or cottage pie? A cheeseburger? What about a roast? Let’s have a roast on Sunday! We could go home? I’ve not seen Mum or Dad in ages.’`
- 判定：例句文字在原文中逐字存在，但它是**一段更长台词的中间截断**，md 把它加了起止引号写成一句完整台词（原文同段后面还接着 `A cheeseburger? What about a roast?`）。按 S4「例句是本章原句」的口径，此例应标省略号：`‘Can’t I have lasagne? Or cottage pie? …’`，或改取该段的完整句。

### E7 ·【提示】导航「叙事手法」的「妹妹的病」——原文无人下诊断

- md 原文（导航·叙事手法）：
  > `……同时把家里的秘密——谁在唱歌、妹妹的病——压在轻快的口吻底下。`
- 原文 `text/ch23_23.txt:331`（Sonikk 的**猜测**）：`He’d thought ‘Eulalia’ was going to be bratty or a cokehead, not a sweet girl who possibly had a personality disorder and her hyper-gifted, sow-faced big sis.`
- 原文 `text/ch23_23.txt:346`：`‘She’s not delicate. She’s more robust than most people you’d meet out on the street.’ Mel was making sure she took her medication, after all. Perhaps it was time for a review with her psychiatrist just to be sure the dosage was right though.`
- 判定：原文里「人格障碍」是 Sonikk 的揣测（「possibly」），全章无人确诊；md 在导航里写成既成事实「妹妹的病」。建议改为「妹妹的状态（她自己可能并不清楚的那部分）」或「姐姐替她盯着的药」。

---

## 附：本轮已核对无误（不必改，供修复方护栏）

- 9 块 10 段引语全部在原文逐字命中，块与原文行对应关系：
  | 块 | 原文行 | 块 | 原文行 |
  |---|---|---|---|
  | 1 | `text/ch23_23.txt:20` | 6 | `text/ch23_23.txt:313` |
  | 2 | `text/ch23_23.txt:37` | 7 | `text/ch23_23.txt:340` |
  | 3 | `text/ch23_23.txt:151`（两段同段，`…` 为作者自留） | 8 | `text/ch23_23.txt:398` |
  | 4 | `text/ch23_23.txt:281` | 9 | `text/ch23_23.txt:464` |
  | 5 | `text/ch23_23.txt:301` | | |
- 词汇表 28 条例句：27 条逐字命中（`isolated` 的例句是 `She seemed so isolated when he saw her.`，与 `text/ch23_23.txt:349` 一致，**不是**误写）；仅 `lasagne` 一条为截断（见 E6）。
- 原文 `text/ch23_23.txt:322`：`she left with a volume of poetry` —— 印证 md block 6 把 `a slim volume` 译作「薄薄的诗集」是对的。
- md block 5 把 `‘Good.’` 之前的 `text/ch23_23.txt:295` `‘I like her vibe.’` 归给欧拉莉亚——正确（block 6 中文理解亦然）。
