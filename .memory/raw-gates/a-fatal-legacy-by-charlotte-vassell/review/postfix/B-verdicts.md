# B-verdicts.md · 增量复核任务 B · 三份判定表复读（ch31 / ch43 / ch48）

- 复读对象：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/{ch31,ch43,ch48}/4-verdict.md`
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/`
  —— **本次增量期间 text/ 未被改动**：`git log --oneline -- "$B/text/"` 输出为空（该目录从未单独提交）。
- 判据（§二）：行号漂移（同一句挪了几行）**不算缺陷**；指向变成别的内容才算。
- 档位：**通过**＝指向仍正确；**提示**＝只记；**阻断**＝必须改；**跳过/未核**＝给不出证据。

## 汇总

| 判定表 | 抽条 | 指向仍正确 | 漂移（不算缺陷） | 结论失效 | 档位 |
|---|---|---|---|---|---|
| ch31 `4-verdict.md` | 3 | 3 | 0 | 0 | 通过 3 |
| ch43 `4-verdict.md` | 3 | 3 | 0 | 0 | 通过 3 |
| ch48 `4-verdict.md` | 3 | 3 | 0 | 0 | 通过 3 |
| **合计** | **9** | **9** | **0** | **0** | **通过 9** |

---

## 一 · ch31 `4-verdict.md`

### B31-1 · 抽 A3（摄像头「家家有」放大）——判定表标 **阻断**

- 判定表原文：「md：「整个广场家家有摄像头」「每个人都确信自己是安全的」「每户人家的摄像头」（块 5＋导航两句）｜ `text/ch31_31.txt:68`「Quite a few of the houses have cameras but they’re all within the gardens and pointed at their gates」｜ 原文是「**不少**房子有摄像头」，非家家」
- 命令：`sed -n '68p' "$B/text/ch31_31.txt"`
- 原文逐字：

```
‘No.’ Caius opened the gate and popped into the alleyway. A high wall ran alongside the other side, blocking the squat two-storey houses behind from overlooking it. He walked down it as Matt followed. He stopped at the end of the path and looked out onto the main road. Buses were stopping and starting as they swallowed and vomited passengers, brave cyclists with and without helmets flying in between. ‘Quite a few of the houses have cameras but they’re all within the gardens and pointed at their gates. No one has a visual of the alley. Makes sense. You don’t want to apply for planning permission, and all any would care about was someone breaking into their own house.’
```

- 现仍指向同一句：`Quite a few of the houses have cameras but they’re all within the gardens and pointed at their gates.` ✔ **指向仍正确**。
- 顺带核 md 现值（阻断项是否已落地）：
  - `ch31 a second body is found at priory square.md:11`「广场上**不少房子**装了摄像头却只对着自己的院门」
  - `:13`「一批只对着自家院门的摄像头」
  - `:49`「广场上**不少人家**装了摄像头，但全都在自家花园里、对准自家的院门」
  - ⇒ 三处均已改为「不少」，**A3 阻断项在 md 侧已落地**（`grep -n '家家有摄像头\|每户人家的摄像头' ch31*.md` → 无命中）。
- 档位：**通过**

### B31-2 · 抽 A4（「巧合被顶了回去」）——判定表标为「最要紧的一条」 **阻断**

- 判定表原文：「A4（阻断）：md 把 `text/ch31_31.txt:74` 里**主语不同、并列共存**的两句（Caius 的 PO Box 关联「cannot be a coincidence」＋ 两起入室「could be a coincidence」）写成「后者被前者顶了回去」… ⇒ 全章主旨目前建立在一个原文不支持的转折上」
- 命令：`sed -n '74p' "$B/text/ch31_31.txt"`
- 原文逐字：

```
‘I don’t know. Digby and Scott were definitely killed by the same person. Had to be. The PO Box connection cannot be a coincidence.’ They walked back into Jimmy’s garden. ‘These two break-ins could be a coincidence. The murder happens at the same time someone else is targeting the area.’
```

- 现仍指向同一句：两句仍**并存**、仍主语不同（`The PO Box connection cannot be a coincidence.` ／ `These two break-ins could be a coincidence.`）✔ **指向仍正确**。
- 顺带核 md 现值（阻断项是否已落地）：
  - `ch31 …md:11`「于是他给出**两个并列的判断**：PO Box 的关联不可能是巧合，而这两起入室盗窃可以算巧合」
  - `:116`「于是他**同时说出两个判断**：PO Box 的关联不可能是巧合；而这两起入室盗窃也许只是撞车」
  - ⇒ 已无「顶了回去／不再是巧合」写法，**A4 阻断项已落地**。
- 判定表 §四·3 的护栏（「块 6 写对了，不要反向改成互相推翻」）现仍成立：md 块 6 仍写「could（松动）／cannot（钉子）」两句并存。
- 档位：**通过**

### B31-3 · 抽 §四·1 护栏（死因的谨慎表述）

- 判定表原文：「md「法医初判为滑倒撞上铁栏杆的意外」**正确**。原文 `text/ch31_31.txt:47`：「This one looks like an accident. The poor guy simply hit his head on the iron railing after slipping on the crumbling stone steps. …」——**原文本身就没确诊死因**，md 用「初判」是恰当的」
- 命令：`sed -n '47p' "$B/text/ch31_31.txt"`
- 原文逐字：

```
‘This one looks like an accident. The poor guy simply hit his head on the iron railing after slipping on the crumbling stone steps.’ Barry pointed to the middle step which had split in half and then to Jimmy’s left trainer which was covered in dust the same colour. ‘I’ll obviously be a little more thorough than that in my report, but there’s no evidence of foul play.’
```

- 现仍指向同一句（`This one looks like an accident.` 起）✔ **指向仍正确**；同句仍含 `there’s no evidence of foul play` ⇒ 「原文没确诊死因」这一结论**仍成立**。
- 顺带核 md 现值：`ch31 …md:11`「法医**说像是**滑倒撞上铁栏杆的意外」、`:116`「法医**初判为**滑倒撞上铁栏杆的意外」——措辞仍与「未确诊」相符，**护栏未被违反**。
- 档位：**通过**

### ch31 附加核验（另抽 5 条引用，同属本表，仍为只读）

| 引用 | 命令 | 现指向（原文逐字要点） | 结论 |
|---|---|---|---|
| `text/ch31_31.txt:44`（A5） | `sed -n '44p'` | `‘I don’t know, mate.’ Caius was beginning to wonder if he’d got it all wrong somewhere. ‘But I wouldn’t want to live on this square. I’d be worried I would be next.’` | 仍同句。md 现值 `:42`「我绝不会想住在这座广场上——我会担心下一个就是我」、`:44`「他担心的正是自己——『下一个就是我』」，**A5 阻断项已落地**（不再是「他替的不是自己，是住户」） |
| `text/ch02_2.txt:101`（A2） | `sed -n '101p'` | `Barry, the team’s favourite medical examiner, was zipping up the body bag. ‘Morning, morning, morning.’` | 仍同句。md 现值 `:12`「夹着马特的插话与**验尸官**巴里的判断」、`:35`「**验尸官**巴里从蹲着查看…一名法医技术员正在擦拭…另一名在拍摄」，两者已分列，**A2 阻断项已落地** |
| `text/ch01_1.txt:17`（§四·4 护栏） | `sed -n '17p'` | `The Horatio Combe Institute, Priory Square, Camden` | 仍同句，「同一广场第二具尸体」护栏仍成立 |
| `text/ch33_33.txt:243`（§四·4 护栏） | `sed -n '243p'` | `…he highlighted Digby’s and Jimmy’s houses in red and Benedict’s in orange.` | 仍同句 |
| `text/ch37_37.txt:95`（A8 后文佐证） | `sed -n '95p'` | `…There was a partial print on the door to the basement which has been sealed up for decades…` | 仍同句，仍是「后文有人在找地下室」的佐证 |

### ch31 · §四「已核实为正确」护栏 8 条复核

| 护栏 | 现是否仍成立 | 证据（命令 + 原文） |
|---|---|---|
| 1. 死因谨慎表述（「初判」） | **成立** | `sed -n '47p' text/ch31_31.txt` → 原文仍含 `there’s no evidence of foul play`；md `:11`/`:116` 仍写「说像是／初判为」 |
| 2. 死者身份（前电视主持人吉米·琼斯） | **成立** | `sed -n '23p'` → `‘Jimmy Jones, forty-eight years old. You may well remember him from mid-two-thousands late-night panel shows.’`；`sed -n '125p'` → `Besides, Jimmy Jones would’ve been on big money at the BBC then. He did a travel show, right? … And that late-night game show.`（md 未写年龄，不算漏） |
| 3. 块 6「一松一钉」写法对，A4 只改导航不改块 6 | **成立** | `sed -n '74p'` 两句仍在；md 块 6 未被改成「互相推翻」 |
| 4. 「同一广场第二具尸体」成立 | **成立** | `sed -n '17p' text/ch01_1.txt` → `The Horatio Combe Institute, Priory Square, Camden`；`sed -n '243p' text/ch33_33.txt` → `highlighted Digby’s and Jimmy’s houses in red` |
| 5. H1 `# 31. Priory Square` 不得改 | **成立** | `sed -n '17p' text/ch31_31.txt` → `Priory Square`；md H1 现仍为 `31. Priory Square` |
| 6. 译名「迪吉」（Digby） | **成立** | `grep -ro '迪吉' "$B"/*.md \| wc -l` → 160 处，未被改动 |
| 7. 块 7 引语截取方式（连续无 `…` 拼接） | **成立** | `sed -n '101p'` → `…“Fake Isolde” is clever; this doesn’t feel clever…`；md 块 7 引语仍为连续子串 |
| 8. 词汇表 29 条例句全部逐字命中 | **成立** | 现 md 词表例句行数 = 29；本次任务 A 逐条整串核验未见不命中 |

---

## 二 · ch43 `4-verdict.md`

### B43-1 · 抽阻断型（导航称 Amy 与 Matt「自己亲手办过的案子」，判定表记「阻断 → 已改」）

- 判定表原文：「导航·一句话概括与一句话总结都称…是 Amy 与 Matt「自己亲手办过的案子」｜ `text/ch43_43.txt` L80 `‘I remember that case, it was one of the first ones **he** worked on as a DS.’`；L86 `‘**Caius** worked on both of these.’`｜ **与原文不符**：办这些案子的是凯厄斯」
- 命令：`sed -n '80p;86p' "$B/text/ch43_43.txt"`
- 原文逐字：

```
‘Yep. A youngling butchered by a troll, left in a sacred well. The nymphs wept for her. He brought the troll to justice.’ Matt looked up at her. ‘I remember that case, it was one of the first ones he worked on as a DS.’

‘Caius worked on both of these. That poor kid whose dad … Her Barbies were all lined up on the side of the bath.’
```

- 现仍指向同一句（`he worked on as a DS` ／ `Caius worked on both of these.`）✔ **指向仍正确**。
- 顺带核 md 现值（阻断项是否已落地）：
  - `ch43 the forum stories are read.md:11` 现为「认出了**凯厄斯本人、凯厄斯亲办过的旧案**和卡莉自己的生意」
  - `grep -n '自己亲手办过' "$B/ch43 the forum stories are read.md"` → **无命中**
  - ⇒ 判定表所述「两行均改」**确已落地**。
- 档位：**通过**

### B43-2 · 抽提示型 6（「被月桂遮住的艳妇」）

- 判定表原文：「导航·一句话概括「被月桂遮住的艳妇」：原文 `Neath a laurel`（在月桂之下），非「被遮住」。」
- 命令：`grep -n 'Neath a laurel' "$B/text/ch43_43.txt"`
- 原文逐字（`text/ch43_43.txt:83`）：

```
Amy stood over his shoulder. ‘’Neath a laurel, the gaudy lady spoke not truth. Days sat in a temple of lustful delight. Misadventure, her dark knight an ignoble lover. He loved all over town.’ She looked at Matt. ‘Clemmie O’Hara, found dead under a bush after having an affair with her boss in that dodgy art gallery.’
```

- 现仍指向同一句 ✔ **指向仍正确**；`Neath a laurel, the gaudy lady spoke not truth.` 确在 `text/ch43_43.txt:83`。
- md 现值 `ch43 …md:11` 仍写「被月桂遮住的艳妇」——判定表把它归为**提示型（只记不改）**，故仍保留**不算失效**；md `:61` 的中文理解已按原文写「月桂之下艳妇所言非真」，与原文一致。
- 档位：**通过**

### B43-3 · 抽提示型 2（「一直沉默滑动的 Matt」）

- 判定表原文：「原句 6 为什么这样写「一直沉默滑动的 Matt」：Matt 前文一直在出声朗读与评点，原文只说 `continued scrolling`。」
- 命令：`grep -n 'continued scrolling' "$B/text/ch43_43.txt"`
- 原文逐字（`text/ch43_43.txt:104`）：

```
Matt continued scrolling. ‘The writer has put themselves into an erotically charged love triangle.’
```

- 现仍指向同一句 ✔ **指向仍正确**（原文仍只写 `Matt continued scrolling.`，未标他沉默）。
- 档位：**通过**

### ch43 附加核验（另抽 2 条）

| 引用 | 命令 | 现指向 | 结论 |
|---|---|---|---|
| `text/ch43_43.txt:92`（阻断型证据行） | `sed -n '92p'` | `‘And referenced here. This story is all about Caius and Callie. There’s a bit here about a buxom fair maiden with enchanted fingers who is celebrated for making garments for princesses. That’s Callie’s hats. She’s got a very fancy clientele. Caius said that most of her sales for the year come from Ascot…’` | 仍同句；阻断型证据链（含「给公主裁衣的丰满少女＝卡莉的生意」「Ascot」两处提示项的原文出处）**未失效** |
| `text/ch43_43.txt:17`（场景标题 / H1） | `sed -n '17p'` | `The Police Station` | H1 `# 43. The Police Station` 仍对应原文场景标题，判定表「形态 0 偏离」仍成立 |

---

## 三 · ch48 `4-verdict.md`

### B48-1 · 抽阻断型（街边对话不是结尾，判定表记「阻断 → 已改」）

- 判定表原文：「导航·视角称「最后由 Matt 与 Caius 在街边单独对话收束」；导航·叙事手法称「最后收在街边一段只有两个人的低声交代上」｜ `text/ch48_48.txt` 第 4 个 `* * *`（@10457）之后的第 5 段（@11409–16432）：Amy 回到威洛手抄的 Horatio Combe 疟疾年日记 → holy lady → Alice de Burge → `knocked through a basement wall and into any subterranean ruins` → `Isolde and Andy sit down at 9.37 p.m. They don't move until 1.01 a.m.` → Robbie 的红鲱鱼质问 → Amy 的行动清单 → `‘Let's do both.'`」
- 命令（复现分段偏移）：
  `python3 -c "import re;s=open('$B/text/ch48_48.txt',encoding='utf-8').read();print([m.start() for m in re.finditer(r'\*\s*\*\s*\*',s)])"`
- 输出：`[5110, 9089, 10457, 11409]` ⇒ 4 个分隔符，与判定表所述「第 4 个 `* * *` @10457」**一致** ✔
- 命令：`sed -n '286p;292p;316p' "$B/text/ch48_48.txt"`
- 原文逐字（段 5 内的三处关键锚点）：

```
Matt forwarded the email to Robbie with the link. ‘Is it possible that someone knocked through a basement wall and into any subterranean ruins? I mean, it sounds crazy.’

Matt checked his phone. Caius had forwarded him an email from his account at his family’s property company. Matt read it again. Caius did know who the killer was. He got up the CCTV from Whipps Cross A&E. Caius had requested it a while ago but there hadn’t been a need to watch it before. ‘Isolde and Andy sit down at 9.37 p.m. They don’t move until 1.01 a.m.’

‘Let’s do both,’ Robbie said, nodding to himself. He might spot something indeed. ‘Amy, when’s this Willow girl coming in again? Make sure she actually knows Jen and that Jen wasn’t stalking her too like she was Caius and his girlfriend.’
```

- 现仍指向同一句 ✔ **指向仍正确**：段 5（`@11409` 之后）仍依次含 `knocked through a basement wall and into any subterranean ruins`、`Isolde and Andy sit down at 9.37 p.m. They don’t move until 1.01 a.m.`、`‘Let’s do both,’ Robbie said`。
- 顺带核 md 现值（阻断项是否已落地）：
  - `ch48 the case is rebuilt on the board.md:11` 视角现为「Matt 与 Caius 在街边单独对话**之后**，镜头转回 Amy——她重新翻起威洛手抄的日志抄本…末了落在 Robbie 一句「那就两样都做」上」
  - `:15` 叙事手法现为「街边那段只有两个人的低声交代是插叙的**最后一下**；镜头**随后**转回 Amy 手里的日志抄本」
  - ⇒ 判定表所述「已改」**确已落地**。
- 档位：**通过**

### B48-2 · 抽 `4-correspondence.md` 块 8 对应范围 `@13599–13720`

- 对账表原文：「8 | Matt 转发邮件＋地下室墙与地下遗迹（@13599–13720）| 对应 | 「由提出者自己先贬一句『听起来很疯狂』」对应 `I mean, it sounds crazy.`；「把楼上的世界和地下的世界接上」对应 `knocked through a basement wall and into any subterranean ruins` ✓」
- 命令：`python3 -c "s=open('$B/text/ch48_48.txt',encoding='utf-8').read();print(repr(s[13599:13720]))"`
- 原文逐字：

```
forwarded the email to Robbie with the link. ‘Is it possible that someone knocked through a basement wall and into any su
```

- 现仍指向同一句 ✔ **指向仍正确**，**偏移未漂移**（区间仍落在 Matt 转发邮件→地下室墙→`I mean, it sounds crazy.` 这一段内）。
- 档位：**通过**

### B48-3 · 抽 `4-correspondence.md` 块 10 对应范围 `@14670–14800`

- 对账表原文：「10 | Amy：把真 Isolde 排除到超越合理怀疑（@14670–14800）| 对应 | 查笔记本／搜查令搜住处／传唤问本人三项动作逐项对上；「不是证明她有罪，而是排除」对应 `We should eliminate her beyond any reasonable doubt` ✓」
- 命令：`python3 -c "s=open('$B/text/ch48_48.txt',encoding='utf-8').read();print(repr(s[14670:14800]))"`
- 原文逐字：

```
d Keisha Jones who she was out running with in Walthamstow. Keisha helped her home at approximately 6.30 p.m. There is time unacco
```

- 现仍指向同一句 ✔ **指向仍正确**，**偏移未漂移**（区间仍落在「Isolde 不在场证明」那段，`Keisha Jones … Walthamstow … 6.30 p.m.`）。
- 交叉确认该块所依赖的 `We should eliminate her beyond any reasonable doubt` 仍在原位：
  `python3 -c "s=open('$B/text/ch48_48.txt',encoding='utf-8').read();print(s.find('We should eliminate her beyond any reasonable doubt'))"` → `15233`（md 原句 10 引语起于 `@15130`）✔
- 档位：**通过**

### ch48 附加核验（另抽 3 条）

| 引用 | 命令 | 现指向 | 结论 |
|---|---|---|---|
| `@2226–2412`（块 1） | `s[2226:2412]` | `That’s interesting,’ Robbie said, going up to the whiteboards that Amy was tracking the case on. He flipped one over and began writing on the back. ‘All right, tell me what I’m missing.’` | 仍同句，偏移未漂移 |
| `@13990–14120`（块 9） | `s[13990:14120]` | `…t checked his phone. Caius had forwarded him an email from his account at his family’s property company. Matt read it again. Caius` | 仍同句，偏移未漂移；`It all ties up perfectly` 现在 `@14533`（md 原句 9 引语起于 `@14351`）✔ |
| `@12501–12680`（块 7） | `s[12501:12680]` | `Alice de Burge? The nun who was burnt for heresy during the Reformation. The one with the blob statue in the middle of the square. His little cult is “feeding” off the ancient sit` | 仍同句，偏移未漂移 |

### ch48 · 提示项 2 复核（「日志里那个小教派」→「Horatio Combe 那个小教派」）

- 判定表原文：「原句 7「日志里那个小教派」→「Horatio Combe 那个小教派」（小改，提升可回溯性；依据 `His little cult` + 语料 `He led a group of occultists that lived in these same four houses in the square.`）」
- 命令：`grep -n '小教派' "$B/ch48 the case is rebuilt on the board.md"`
- 原文逐字（md 现值）：`:63`「Horatio Combe 那个小教派正是在“feeding”这处古遗址的能量。」
- ⇒ 小改**已落地**；词表 `:104`「| cult | 小教派；（含贬义）邪教式团体 | His little cult is “feeding” off the ancient site’s energy.’ |」亦逐字命中 `text/ch48_48.txt`。
- 档位：**通过**

---

## 四 · 只记条目（提示型，不改）

### B-提示 1 · ch31 判定表 §四·2 的行号指向有偏差（判定表自身笔误，不影响 md）

- 判定表原文：「`text/ch31_31.txt:23`「Jimmy Jones, forty-eight years old」、`:29`（BBC 旅行节目 + 深夜游戏节目 + mid-two-thousands 深夜 panel 节目）」
- 实测三处：
  - `sed -n '23p' "$B/text/ch31_31.txt"` → `‘A fan, apparently.’ … ‘Jimmy Jones, forty-eight years old. You may well remember him from mid-two-thousands late-night panel shows.’` ← 「mid-two-thousands 深夜 panel 节目」在 **:23**
  - `sed -n '29p' "$B/text/ch31_31.txt"` → `‘The one and the same. I’ll get up his Wikipedia.’ … Apparently, Jimmy is doing weird little livestreams for a handful of fans these days. Hasn’t toured in four years.’ He put his phone back in his pocket. ‘He was in the middle of a live-stream when an intruder was spotted on camera. He gave chase and never returned.’` ← **不含** BBC / 旅行节目 / 游戏节目
  - `sed -n '125p' "$B/text/ch31_31.txt"` → `… Besides, Jimmy Jones would’ve been on big money at the BBC then. He did a travel show, right? About stag dos or something. And that late-night game show. It was a bit eurotrashy. …` ← **BBC 旅行节目 + 深夜游戏节目在 :125**
- 定性：**判定表护栏条目里的行号笔误**（`:125` 的内容被写到了 `:29`）。
- **md 无缺陷**：护栏结论「前电视主持人吉米·琼斯」仍成立；md 未写年龄，也不构成「漏」。
- 建议（供书主决定，本次**未改**）：把 ch31 `4-verdict.md` §四·2 的 `:29` 改成 `:125`。
- 档位：**提示**

### B-提示 2 · ch48 判定表 §三 的「5 段 / 4 段」口径分歧（判定表自身已声明）

- 判定表 §三 已自述：「源文 `* * *` 分 5 段、街边对话为其中第 3 段插叙、其后第 5 段回到主线，本判定依此；若按「分隔符数」口径读则应为 4 段，属措辞口径差异，判提示。」
- 实测：分隔符 4 个 ⇒ 分 5 段；街边对话在**第 4 段**（`@10457–@11409`，起句 `Matt escorted Caius and Callie out of the building…`），其后第 5 段（`@11409` 起）回主线到 Amy。
- 定性：**口径差异**，判定表已自行判提示并写明依据；其「阻断 → 已改」的结论（街边对话不是结尾）**不受影响**，md 现值确已改。
- 档位：**提示**（与判定表自身判定一致）

---

## 五 · 结论

三份判定表抽读的 **9 条引用全部仍指向同一句**，**0 条漂移**（连 ch48 的字符偏移都未漂），**0 条结论失效**。

- ch43 / ch48 两份判定表记的「阻断 → 已改」，经回 md 现值核验，**修改确已落地**。
- ch31 判定表 §四 的 **8 条「已核实为正确」护栏，8 条全部仍成立**。
- 只记 **2 条提示**（判定表自身的行号笔误 / 口径差异），**均不涉及书稿 md，不需要改书**。

档位计数：**通过 9 ｜ 阻断 0 ｜ 提示 2 ｜ 假红 0 ｜ 跳过/未核 0**。
