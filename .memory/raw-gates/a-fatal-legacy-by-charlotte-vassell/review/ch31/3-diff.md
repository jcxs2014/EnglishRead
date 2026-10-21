# 3-diff.md · ch31 · 《A Fatal Legacy》

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch31 a second body is found at priory square.md`
> 唯一权威源：`text/ch31_31.txt`（md5 `ad8aa838b3253c3214c5d5af6c74c5bc`，9053 字符）
> R1 素读已先于开 md 完成（见 `1-suread.json`）。本文件按 **漏 / 编 / 错** 三张单子登记，每条附两侧原文。
> 跨章取证仅用于**核对本章事实**（`text/` 语料与兄弟章 md 的既有约定），未读任何他章精读正文。

---

## 一、漏（素读有、md 无）

### 漏 1 · 未出版的回忆录（Jimmy 的 memoir）——md 全文未出现
- **md 侧**：全文检索无「回忆录 / memoir / 手稿」相关表述（词汇表里 `memoir` 词条的例句引了原文，但**正文分析完全没提这件事**）。
- **原文侧**：`text/ch31_31.txt:110`
  > ‘It looks like Jimmy wrote a memoir,’ Matt said, putting the papers back down.
  `text/ch31_31.txt:112-116`
  > ‘Another book. What a literary neighbourhood.’ / ‘It might sell now he’s dead.’
- **为什么重要**：`text/ch33_33.txt:23` 把它变成正式线索——Caius 回顾「Digby was planning on writing a book, **Jimmy had penned an unpublished memoir** and Benedict had written one controversial banger…」；`text/ch33_33.txt:51` 另有「‘And the memoir?’」。
- **档位**：**提示**（本章内不构成转折，故不判阻断；但属线索层遗漏，写入与否由写作方定。）

### 漏 2 · 后门「关着但没锁、可伸手开锁」——md 未提
- **md 侧**：导航「线索结构」列了意外现场 / 无监控后巷 / 摄像头朝内 / PO Box 关联，**无「后门未锁」**；7 个引语块亦未收录这段。
- **原文侧**：`text/ch31_31.txt:50`
  > He inspected the back gate which was undamaged and closed but unlocked. ‘Not much security on the gate. You could pop your arm over and open the lock. Or he might have just left it open. Took the bins out and forgot to lock it.’
- **为什么重要**：这是本章唯一直接解释「外人如何进出而不被看见」的**具体机制**；`text/ch37_37.txt:95` 后续把「有人在找地下室」与这段对上。
- **档位**：**提示**（属线索层遗漏，未构成事实错误）。

---

## 二、编（md 有、原文无）

### 编 1 ·【阻断】现场「围观的人对『又来一次』没有表现出任何意外」——原文本章无任何围观人群
- **md 侧**（块 3「为什么这样写」）：
  > 正是这种例行感制造压迫：同一座广场，第二次走同一条流程，**围在场边的人对「又来一次」没有表现出任何意外**。
- **原文侧**：`text/ch31_31.txt` 全章**没有围观者、没有邻居在场、没有人群**：到场者只有 Caius、Matt、Barry、法医技术员两人（`text/ch31_31.txt:41`）。
  取证命令（显式文件路径、`/usr/bin/grep`、不接管道、退出码另取）：
  ```
  $ cd .../text && /usr/bin/grep -inE 'crowd|onlooker|bystander|neighbou?r|resident|passer-?by|pedestrian' ch31_31.txt
  113:‘Another book. What a literary neighbourhood.’
  exit=0
  ```
  ⇒ 唯一命中是 line 113 的 **neighbourhood（街区，双关）**，即「多文学的邻里」那句玩笑；**没有任何居民、邻居、人群在场**。
  另（本章专属判据里的「警车」）：
  ```
  $ /usr/bin/grep -inE 'police car|siren|ambulance|flashing light|blue light|van' ch31_31.txt
  exit=1   # 零命中
  ```
  ⇒ ch31 语料里**确实没有警车／警灯／救护车**；这些元素在下一章 `text/ch32_32.txt:86`（"The police are outside again. There were loads of flashing lights."）才有。
- **旁证（疑为跨章串入）**：这样的场面在**下一章**才有——`text/ch32_32.txt:20`
  > Eulalia was standing at her bedroom window on the second floor, watching the police carry another body out the front of one of the neighbouring houses.
  `text/ch32_32.txt:86`
  > ‘On the square. The police are outside again. There were loads of flashing lights.’
- **档位**：**阻断**（编造了本章不存在的人物群；本章专属判据所列的「警车、围观的人」在 ch31 语料中确实不存在）。

### 编 2 ·【阻断】把 Barry 写成「法医技师」，与原文角色不符且 md 自相矛盾
- **md 侧**（块 3「中文理解」）：
  > **法医技师巴里**从蹲着查看广场上最新发现的那具尸体的地方站起来，问凯厄斯：「你们办的这是什么案子？」**一名技师**正在擦拭（取样）死者的 T 恤，**另一名**在拍摄周围环境。
- **原文侧**：`text/ch31_31.txt:41`
  > ‘What is this case you’re working on?’ **Barry** asked, getting up from crouching over the latest body found in the square. **A forensic technician** was swabbing the corpse’s T-shirt as another took pictures of the surrounding area.
  —— 原文里 Barry 与「一名法医技术员」是**两个人**。
- **全书定位**：`text/ch02_2.txt:101`
  > **Barry, the team’s favourite medical examiner**, was zipping up the body bag.
  `text/ch02_2.txt:128`
  > …and with that the body was removed by **two forensic technicians**.
  —— Barry 是**验尸官（medical examiner）**，与技术员分列。
- **md 内部问题**：同句里先把 Barry 叫「技师」，紧接着又另列「一名技师」「另一名」，读者无法判断擦 T 恤的技师是不是 Barry。
- **档位**：**阻断**（角色/施事归属错配，属机器四探针抓不到的一类）。

### 编 3 ·【阻断】「整个广场家家有摄像头」+「每个人都确信自己是安全的」——原文是「Quite a few of the houses」
- **md 侧**（块 5「为什么这样写」）：
  > **整个广场家家有摄像头**，于是**每个人都确信自己是安全的**；……**广场上家家户户的眼睛**加在一起，也看不见那条巷子。
  同类表述另见导航「一句话概括」：
  > …看到**每户人家的摄像头**都只对着自己的院门…
  以及「一句话总结」：
  > 看到**每户人家的摄像头**都只对着自己的院门、而唯一贯通的后巷谁也看不见…
- **原文侧**：`text/ch31_31.txt:68`
  > ‘**Quite a few of the houses have cameras** but they’re all within the gardens and pointed at their gates. No one has a visual of the alley.’
  —— 原文是「**不少**房子有摄像头」（`they're all` 只约束已存在的那批摄像头），**不是家家都有**；「每个人都确信自己是安全的」原文无据。
- **档位**：**阻断**（事实断言与原文不符，且 md 的论证（「家家有 ⇒ 户户放心 ⇒ 所以巷子是盲区」）建立在这个被夸大的断言上）。

### 编 4 ·【阻断】编造「办案者意识到这不再是巧合的那一刻」——原文的两句是并列而非互相推翻
- **md 侧**（导航「一句话概括」）：
  > 于是「两起入室盗窃可以算巧合」被「PO Box 的关联不可能是巧合」**顶了回去**——**从这一刻起，同一个地点本身成了案件**。
  「一句话总结」：
  > 于是「PO Box 的关联不可能是巧合」这句话，把「两起入室盗窃也许只是撞车」**顶成了**「有人正在针对这一带」——压力不再来自某一个人，而来自这个地点本身。
- **原文侧**：`text/ch31_31.txt:74`
  > ‘I don’t know. Digby and Scott were definitely killed by the same person. Had to be. **The PO Box connection cannot be a coincidence.**’ They walked back into Jimmy’s garden. ‘**These two break-ins could be a coincidence.** The murder happens at the same time someone else is targeting the area.’
  —— 两句**主语不同**（前句＝Digby 与 Scott 之死的 PO Box 关联；后句＝这两起入室盗窃），且**都是 Caius 最终保留的立场**：入室盗窃「可以」是巧合，谋杀**不是**巧合（它与「有人正在针对这一带」同时发生）。原文**没有**「顶回/推翻」这一动作，也**没有**「意识到不再是巧合」的时刻。
- **md 内部不一致**：块 6「为什么这样写」反而写对了——「入室盗窃那一句里的『could』是松动，邮政信箱那一句里的『cannot』是钉子」——即**一松一钉共存**，并非一钉压掉一松。导航与总结的「顶了回去」与本块直接打架。
- **档位**：**阻断**（本章专属判据要求写的「不再是巧合的那一刻」在原文里并不存在；md 用一个虚构的转折承担了全章主旨）。

---

## 三、错（两边都有但不一致）

### 错 1 ·【阻断】施事反转：块 4 说 Caius 担心的是「住户 / 邻居的安危」
- **md 侧**（块 4「为什么这样写」）：
  > 而且**他替的不是自己，是住户**——「住在这里的人」才是他担心的对象。……一个连自己都在办的什么案子都说不清的人，**先想到的却是邻居的安危**。
- **原文侧**：`text/ch31_31.txt:44`
  > ‘I don’t know, mate.’ Caius was beginning to wonder if he’d got it all wrong somewhere. ‘But I wouldn’t want to live on this square. **I’d be worried I would be next.**’
  —— 主语是 **Caius 本人**（`I would be next`）。
- **md 内部矛盾**：同一块的「中文理解」「读者视角提示」写的是「我会担心**下一个就是我**」「把『下一个就是我』这句话记下来」，与「为什么这样写」直接相反。
- **档位**：**阻断**（施事/归属反转；四道机器探针全绿，只有 R4 的三问能抓到）。

### 错 2 ·【提示】块 7「那张脸」归属不明且方向易反
- **md 侧**（块 7「中文理解」）：
  > 还**让斯科特去寄**，好**避开邮局监控里的那张脸**。
- **原文侧**：`text/ch31_31.txt:101`
  > The PO Box purchased with a random card that they probably bought the details of on the dark web, **using Scott to avoid being seen on the CCTV at the Post Office**
  —— 被「避免被看见」的是**冒名者一方**；斯科特是**被利用去露面**的人（否则没这句）。md 的「那张脸」无所指，按最自然的读法会读成斯科特自己的脸 ⇒ 方向反。
- **档位**：**提示**（核心意思尚在，但指代须写明「避开的是假 Isolde 那张脸」）。

### 错 3 ·【提示】尸体落点写成「自家门前的石阶上」，原文只说「found in the square」
- **md 侧**（导航「一句话概括」/「一句话总结」）：
  > 吉米·琼斯的尸体出现在**自家门前的石阶上** / 吉米·琼斯**倒在自家门前的石阶上**。
- **原文侧**：`text/ch31_31.txt:41`
  > …crouching over **the latest body found in the square**.
  现场作业位置见 `text/ch31_31.txt:38-41`：Caius「followed the sound of activity to **the garden**」，技术员在花园一侧 swabbing 尸体 T 恤；`text/ch31_31.txt:119` 只说「met out the front while they waited for Jimmy’s body to be carried out」（从正门抬走），**全章没有任何一句把尸体落在石阶上**。「石阶」是 **Barry 的意外假说里的致伤处**（`text/ch31_31.txt:47`：hit his head on the iron railing after slipping on the crumbling stone steps），不是原文给出的尸体落点。
- **档位**：**提示**（位置越界；死因本身 md 写对了，见 `4-verdict.md` 的「已核实为正确」）。

### 错 4 ·【提示】限定词丢失：「入室者**都**从后巷进」
- **md 侧**（导航「一句话概括」）：
  > 发现**入室者都从**绕整圈的后巷进
- **原文侧**：`text/ch31_31.txt:56`
  > ‘In both incidents **it would seem they probably** entered in through the back.’
  —— 原文是双重限定（it would seem / probably），且只针对「both incidents」这两起。
- **档位**：**提示**。

### 错 5 ·【提示】块 2 把「没人看见巷子」挪成了「居民谁也没看见」
- **md 侧**（块 2「为什么这样写」）：
  > **广场上一户户人家，没有一个人看见**；而刷着直播的这一个看见了。
- **原文侧**：`text/ch31_31.txt:68`
  > ‘…**No one has a visual of the alley.**’
  —— 原文说**摄像头**看不到巷子，不是「居民没看见任何东西」；且这句在**块 5 的引语内**，不在块 2。
- **档位**：**提示**（语义漂移 + 跨块借用）。

### 错 6 ·【提示】块 7「作者把这一章收在一句反差上」——引语 7 不是本章末句
- **md 侧**（块 7「为什么这样写」）：
  > 作者**把这一章收在**一句反差上：……
- **原文侧**：`text/ch31_31.txt:125-137`（引语 7 之后仍有两人的怀旧闲话，直到「Mine are yet to come」收尾）；md 自己的导航「叙事手法」也写「**章末**用两人关于『从前』的怀旧闲话把气压慢慢放掉」。
- **档位**：**提示**（md 内部不一致）。

### 错 7 ·【提示】块 3「第二次」的落点其实是「又来一次」，措辞与所引句子略有错位
- **md 侧**（块 3「为什么这样写」）：
  > 巴里一句问话就把这桩案子的「**第二次**」讲了出来——最新发现的那一具，就在广场上
- **原文侧**：`text/ch31_31.txt:41`
  > ‘…the **latest** body found in the square.’
  —— 原句说的是「**最新**发现的一具」，本句本身没有「第二次」；「第二次」是作者从语料层补出来的（第一次是 Digby，尸体在同一条 Priory Square 的 Institute：`text/ch01_1.txt:17` "The Horatio Combe Institute, Priory Square, Camden"；`text/ch33_33.txt:243` "highlighted Digby’s and Jimmy’s houses in red"）。
- **档位**：**提示**（结论正确但不是本句的字面内容；写清「全书的第二具尸体在此」即可）。

---

## 四、对应类（引语截短 / 越界）——归 R4 计数，此处只登记证据

### 对 1 ·【阻断】块 2：引语选短，分析讲的是引语外的一句
- **md 侧**（块 2「中文理解」/「为什么这样写」）：
  > **有人起初确实以为那不过是节目效果**；但有一位牵挂的粉丝，是在当天早上八点发现他居然还在直播，才把电话打了进来。
  > ……作者把「围观」写成这个案子里唯一可靠的眼睛……
- **原文侧**：md 引语只到 `text/ch31_31.txt:35`
  > ‘Yeah, but one concerned fan called it in when they realised that he was still livestreaming at 8 a.m. this morning.’
  而「以为是节目效果」出自**引语外的紧邻上一句** `text/ch31_31.txt:32`
  > ‘**And everyone watching thought what? That it was a bit?**’
- **档位**：**阻断**（S2 截短；修法：把引语向上扩到 `text/ch31_31.txt:32`，两句相邻，取证方便）。

### 对 2 ·【提示】块 5：「中文理解」首句问句出自引语外
- **md 侧**（块 5「中文理解」首句）：
  > **马特问「这算不算只是有人想碰碰运气」，凯厄斯答「不是」**；……
- **原文侧**：md 引语起于 `text/ch31_31.txt:68` 的「‘No.’」；问句在**引语外的上一段** `text/ch31_31.txt:65`
  > ‘…**Do you think this is someone just trying their luck?** They’re breaking into houses in the area and accidentally stumbled on Digby after they’d searched the house. It would explain the set of partials.’
- **档位**：**提示**（问句紧邻且「答『不是』」在引语内，影响小）。

---

## 五、三张单子小结

| 单子 | 条数 | 其中阻断 | 提示 |
|---|---|---|---|
| 漏 | 2 | 0 | 2 |
| 编 | 4 | 4 | 0 |
| 错 | 7 | 1 | 6 |
| 对应（另计，见 R4） | 2 | 1 | 1 |

**阻断型合计（断言侧）＝ 5 条**（编 1、编 2、编 3、编 4、错 1）；对应侧另有 1 条阻断（对 1）。

### 逐字 / 形态组（机器层已判，无新增）
- 引语 7 条**全部逐字命中**原文（本人用 Python 独立复核 `body in src` = True，位置 pos = 36 / 1124 / 1988 / 2216 / 4142 / 4847 / 6943），**无省略号拼接、无跨章搬句、无 U+FFFD**。
- 形态：H1 `# 31. Priory Square`（与全书 54 章的「`# NN. <epub 章名>`」一致）、导航 5 项、子项 4 项（中文理解/关键词/为什么这样写/读者视角提示，与 mystery-thriller profile 一致）、块数 7（本书众数 7，区间 5–10）——**0 偏离，无需写理由**。
