# ch11 三张单子（漏 / 编 / 错）

> 审查方：独立审查员（只负责 ch11）
> 原文（唯一权威源）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch11_11.txt`
> 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch11 matt and amy sort digbys papers.md`
> 区间基准：`text/ch11_11.txt:<行号>`；字符区间为**原文字符偏移 [start,end)**（Python 读全文，0 起算）；md 侧给 `md:<行号>`
> 引语逐字已用独立字节级复核（8/8 全串命中，含弯引号）；词汇例句 29/29 命中本章。详见 `4-verdict.md`
> 零命中取证日志：`5-evidence.txt`（命令 + 输出 + 退出码）

---

## 一、漏（原文有、md 无）

### L1 ★阻断 —— 动机线的两个数全缺，且 `md:13` 导航承诺的这条线在正文没有落地

**原文侧（逐字）**

- `text/ch11_11.txt:73` `Matt, who had taken charge of the institutional pile of paperwork, was reading through a glossy booklet when Caius came back into the incident room.`
- `text/ch11_11.txt:74` `‘Digby had the property valued last week.’`
- `text/ch11_11.txt:76` `‘Two million pounds. Imagine what it’ll be worth once they put electricity in,’ Caius said.`
- `text/ch11_11.txt:82` `‘That’s a pretty good motive if Digby isn’t the only person who has a share of the property,’ Matt said.`
- `text/ch11_11.txt:196` `‘It’s just the two of us now. My aunt had been on the board until she died three years ago.`
- `text/ch11_11.txt:198` `… I kept telling Digby that he could use his part to go and have adventures of his own.’`

**md 侧**

- `md:13` 导航·线索结构明写：`房产估值与共有份额（动机）· …` —— **这条线被声明为本章线索结构**。
- 但 8 个引语块中**没有一块**落在估值/共有份额上；`md:123` 一句话总结也不提估值。
- 两个数在 md 中零命中：
  ```
  $ /usr/bin/grep -cE '两百万|百万英镑|million' "ch11 matt and amy sort digbys papers.md"
  0
  退出码: 1
  $ /usr/bin/grep -cE '受托人只剩|就剩我们|就剩我们俩' "ch11 matt and amy sort digbys papers.md"
  0
  退出码: 1
  ```
- 需要说清的部分（避免把整条动机线都算成漏）：动机线**并非全无**——`md:114`（`share | 份额；共有权的一份`）与 `md:115`（`property | 房产；产业`）的例句正是 `text:82` 那句 Matt 的话，动机线的**引子**在词汇表里在场；缺的是把这条线**钉死**的两件事：估值数字（`text:76`）与受托人只剩两人（`text:196`）。

**结论**：`md:13` 向读者承诺「房产估值与共有份额（动机）」这条线索，正文却既没有对应引语块，也没有数字；读者按导航去找会落空。这不是「精读不必覆盖每一拍」的取舍——是**同一文件内导航与正文不一致**。且这两个数是全书动机主轴（谁继承研究所）在**全书语料中唯一的落点**（见下方跨文件观察）。**阻断**（补法：把 `text:73-82` 与 `text:196-198` 立成块，或把 `md:13` 该项删掉并写明取舍）。

> **跨文件观察（不属本章 md 的缺陷，供总览章审查员复核）**
> 全书语料中，这两个数**只出现在 ch11**：
> ```
> $ /usr/bin/grep -nE 'Two million|two million' text/*.txt
> text/ch11_11.txt:76:‘Two million pounds. Imagine what it’ll be worth once they put electricity in,’ Caius said.
> 退出码: 0
> $ /usr/bin/grep -nE 'two of us' text/*.txt
> text/ch11_11.txt:196:‘It’s just the two of us now. My aunt had been on the board until she died three years ago. …
> 退出码: 0
> ```
> 但 `00_概述.md:14`、`00_情感节点.md:46`、`00_金句精选.md:82` 把「上周刚估过两百万英镑」「就剩我们俩了」记在**白板章（ch09）**名下；ch09 原文里只有 `text/ch09_9.txt:65` `I doubt he had a couple of million in the bank`（**否定式**，且指个人存款）与 `:74-75` `‘It’s worth a bomb.’ … ‘I wonder who inherits the Institute with Digby gone?’` —— 白板章只**提出问题**，答案（估值与受托人名单）在 ch11。**本审查章无权改总览文件，此条只报给总览章审查员。**

### L2 ★提示 —— 第三封信（某学者来信，约两周前）缺失

**原文侧** `text/ch11_11.txt:132` `‘Oh and there was a letter from some academic asking to set up a meeting. That was from two weeks ago.’`

**md 侧** 无。`md:13` 只列「两封机构信」，`md:123` 只说「一封…一封…」。这封信是本章唯一带日期（两周前）的信、也是唯一指向外部学术机构的线索（可能与会面对象有关）；漏掉它，「两封未署名未署日期的信」的对读少了一个反差坐标。

```
$ /usr/bin/grep -cE '学者|学术|求会面|约见' "ch11 matt and amy sort digbys papers.md"
0
退出码: 1
```

**提示**（补一句即可，不阻断）。

### L3 ★提示 —— 其余零散转折未进块：想关停研究所 / 没有遗嘱 / 恋人线 / Nathan 与住址簿

**原文侧（逐字）**

- `text/ch11_11.txt:172` `‘Digby had written to say that he had a plan for the Institute. I think he wanted to wind it down.’`
- `text/ch11_11.txt:199-202` `‘If you don’t mind me asking, were you aware whether or not Digby had made a will?’` / `‘Not that I know of. He was young.’`
- `text/ch11_11.txt:235` `‘He hadn’t told you he’d met anyone recently?’` … `text/ch11_11.txt:241` `‘We think so.’`
- `text/ch11_11.txt:214` `‘No. Nathan’s a nice boy. Yes, Nathan was his best friend.’` … `text/ch11_11.txt:220` `‘I’m sure Digby will have an address book.’`

**md 侧** 无。取证（`5-evidence.txt` E4/E5/E6）：`Nathan|内森|住址簿|地址簿` → 0（退出码 1）；`关停|收掉|解散|停掉|wind it down` → 0（退出码 1）；`没有遗嘱|未立遗嘱|没立遗嘱|没遗嘱` → 0（退出码 1）。`md:119` 词汇表只引了遗嘱那句**提问**，答案「没有遗嘱」未写。

**提示**（`:172` 是两封信的动机前提，最值得进块；其余可选）。

---

## 二、编（md 有、原文无）

### C1 ★提示 —— 「冰箱贴」：把明信片说成冰箱磁贴，且与同块中文理解自相矛盾

**原文侧**

- `text/ch11_11.txt:85` `… remembering the postcard sent from Goa on the fridge.`
- 卡片实物（他章印证）：`text/ch04_4.txt:56` `Caius wandered over to the fridge. Inspecting a postcard of a Goan beach clinging to the front of it, he took it down.`（同处 `Mum x.` 见 `:56` 句尾）

**md 侧**

- `md:37` `**为什么这样写**：这封私人信件的证据形态是一张冰箱贴——…`
- 同块 `md:35` 自己写的是 `…他想起那张从 Goa 寄出、贴在迪吉冰箱上的明信片。`；`md:123` 也写「一张贴在冰箱上的明信片」。

**结论**：`冰箱贴`（＝冰箱磁贴）与原文的 postcard 不是同一件东西；md 在**同一块内**用了两个不同的物名。属物名失准，一字可改；该块论证主体（私人信件的物理位置＝家的那一摞）不受影响。**提示**（建议改「明信片」）。

### C2 ★提示 —— 「把藏品整体出手」把「其余藏品」说成全部

**原文侧** `text/ch11_11.txt:126` `‘There was another letter kept in the same folder, offering the rest of the collection to the Royal Geographical Society,’`

**md 侧**

- `md:58` `…一封要求归还人骨，一封要把藏品整体出手——被并排塞在一处…`
- 同块 `md:56` 自己写的是 `…愿意把其余藏品交给皇家地理学会…`；`md:13` 导航也写「剩余藏品」。

**结论**：`the rest of the collection`＝**其余**藏品；`整体出手` 抹掉了「七具人头骨走归还线、其余走出手线」这组互补关系（三处口径两对一）。**提示**（措辞，改「其余」）。

### C3 ★提示 —— 「当众」

**原文侧** `text/ch11_11.txt:145-166` 是一对一问询室内的对话（芬内拉与凯厄斯）；`:63` 另有家属联络警员接手，`:145` 之后场景仅二人。

**md 侧** `md:14` `芬内拉从"以为只是个旧宅"走到当众把"harm"改口成"murder"`。

**结论**：无公众在场；「当众」把私密问询写成公开场面。**提示**。

### C4 ★提示 —— 「地点始终是警局的案情室」

**原文侧** `text/ch11_11.txt:73` `…when Caius came back into the incident room.` —— 说明他此前不在案情室（道歉与首轮问询在另一间房，`:60-63`）；`:63` `Caius left the room, signalling for the family liaison officer to take over.`

**md 侧** `md:12` `…地点始终是警局的案情室。`

**结论**：`始终` 不成立；章节小标题 `The Police Station`（`text:17`）说的是警局，不是案情室。**提示**。

### C5 ★提示 —— 《Our Apologia》三种译名并存

**原文侧** `text/ch11_11.txt:190` `He called it “Our Apologia”.`

**md 侧**

- `md:13` `…计划写成的自白书《Our Apologia》…`
- `md:70` `《Our Apologia》（我们的自辩书）`
- `md:83` `| Apologia | 辩白书；自辩（尤指对自身过错的公开检讨） | He called it “Our Apologia”. |`
- 跨文件：`00_概述.md:44` 用「自辩书」；`ch13 …md:85` 用「自辩书（拟议书名）」。

**结论**：同一书名在 ch11 一章内出现「自白书 / 我们的自辩书 / 辩白书；自辩」三种译法；「自白」＝坦白，与 apologia（为自己申辩/致歉书）语义不合。**提示**（统一为「自辩书／辩白书」其一）。

### C6 ★提示 —— 词汇条「toi moko」的释义系外部补入

**原文侧** `text/ch11_11.txt:99` `I am writing to you with regard to the repatriation of human remains within the Horatio Combe Institute.` / `:102` `…seven toi moko or mokomokai from New Zealand.` —— 本章**未给词义**，只作名词使用。

**md 侧** `md:82` `| toi moko | 毛利人对待敌人遗骨的方式，此处指人头骨 | … |`

**结论**：释义属书外补入，且「对待遗骨的方式」与词义不合——`toi moko`／`mokomokai` 是**纹饰人头**本身，他章口径 `text/ch02_2.txt:285` `the mokomokai were preserved as a way to honour their ancestors by showcasing their tattoos`（纹样）与 `ch39 …md`「缩头」可参。**提示**（附注：`md:42`「毛利人头骨」与全书口径 `ch38:117`「骸骨之手」、`ch39:75`「缩头与 mokomokai」、`00_概述.md:14`「七具新西兰人头骨」一致，**不是缺陷，不必动**）。

---

## 三、错（两边都有但不一致）

### W1 ★阻断 —— 原句 6 的「读者视角提示」把「同一个文件夹」拆成两摞互相渗透：与原文冲突，且与本章自家上句自相矛盾

**原文侧（逐字）** `text/ch11_11.txt:126` `‘There was another letter kept in the same folder, offering the rest of the collection to the Royal Geographical Society,’ Amy said, scanning the other letter. ‘Also unsigned and undated.’`
（另 `text:120` `‘It hasn’t been dated, or signed yet,’ Amy said, looking the letter over.`）

**md 侧**

- `md:59` `**读者视角提示**：这层模糊正是本章的关键：一摞"机构文件"里混进了死者的私人决定，而"私人信件"里又装着整个馆的处置方案。`
- 同块 `md:58` 自己却写 `…被并排塞在一处，私人决定与机构事务的界线就在这一摞里被抹平了。`

**结论**：原文是**一个文件夹里的两封信**（一封致部里的遣返函、一封致皇家地理学会的出手函，**都是机构信**，都未署名未署日期）；本章唯一那封私人信件是 `text:85` 冰箱上的明信片，卡片实物见 `text/ch04_4.txt:56`，它**不在任何文件夹里**，更不含「馆的处置方案」。md 的 `md:59` 描述成「机构文件一摞」与「私人信件一摞」互相渗透——既与 `text:126` 的 `the same folder` 冲突，也与**本章自家 `md:58`（并排塞在一处）自相矛盾**。本章专属判据问的正是「私人信件与馆藏文件的分界在哪一摞被翻出来时开始模糊」，md 在这一句上把答案说反了。**阻断**。

### W2 ★阻断 —— 原句 3 的「他母亲」：紧跟「凯厄斯说」，中文默认绑定成凯厄斯的母亲

**原文侧（逐字）** `text/ch11_11.txt:85` `‘His mum wrote to him saying they’d talk about the future of the Institute when she got back,’ Caius said, remembering the postcard sent from Goa on the fridge.`

`His` 指**迪吉**：上一句 `text:82` 谈的正是 `Digby isn’t the only person who has a share of the property`；卡片实物 `text/ch04_4.txt:56` 落款 `Mum x.`、内容 `Let’s talk about the Institute when I get back on 27th.`；`text:196` 芬内拉自述 `It’s just the two of us now`（董事会只剩她与迪吉两人），`text:172` 她转述迪吉的打算。

**md 侧** `md:35` `**中文理解**：凯厄斯说，他母亲写信告诉迪吉，等她回来两人要谈研究所的未来；他想起那张从 Goa 寄出、贴在迪吉冰箱上的明信片。`

**结论**：`他母亲` 的先行词在中文里默认绑定最近的主语「凯厄斯」，读成「**凯厄斯的母亲**写信告诉迪吉」——凭空造出一段书中不存在的母子关系；而后文「两人要谈研究所的未来」又只能指迪吉与**他的**母亲（芬内拉），句子内部即不自洽。这正是 R4 固定追问③「谁的」归属问题：机器四道探针（引语逐字✓、中文是中文✓、关键词✓、形态✓）全绿也照样漏。**阻断**（改为「迪吉的母亲」/「芬内拉」）。

### W3 ★提示 —— 原句 5 的「早已办妥的馆藏文件」

**原文侧** `text/ch11_11.txt:120` `‘It hasn’t been dated, or signed yet,’ Amy said, looking the letter over.` / `text:126` `…‘Also unsigned and undated.’` —— 同一文件夹里那封同样未署名、未署日期。

**md 侧** `md:51` `**为什么这样写**：…但它已经躺在死者的文件里，和那些早已办妥的馆藏文件摞在一起。`

**结论**：「早已办妥」是原文没有的状态描述，且与同文件夹那封同样未署名未署日期的事实相冲。**提示**。

### W4 ★提示 —— 原句 8 的「几十年」

**原文侧** `text/ch11_11.txt:178` `‘It gave me the creeps.’ … ‘It’s a mausoleum. My father was curator before Digby took over.’` / `:180` `…Digby had graduated the summer before and was at a loss because of the recession so he took it on.` —— 本章只给了祖父/父亲任 curator 与迪吉毕业后接手，**没有给年代跨度**。

**md 侧** `md:72` `…把这个家里几十年来的遮遮掩掩说成了一次具体的动作…`

**结论**：「几十年」是本章未给的量度（书外推断）。**提示**。

### W5 ★提示 —— 原句 5 的分析用了引语外的下一句（引语边界外扩）

**原文侧** `text/ch11_11.txt:120`（本块引语只到这一行）→ `text/ch11_11.txt:123` `‘He was waiting to speak to his mum,’ Caius said.`

**md 侧** `md:51` `…凯厄斯随即判断这封信是在等母亲回来后才发：写不动笔的理由不在信里，而在信外的那个人身上。`

**结论**：分析里「凯厄斯随即判断…」的判断依据在引语之外（`text:123`）。属 R4 第一档「引语选短」，但该块分析主体仍落在引语内（无日期/无签名的含义），密度不减。**提示**（把 `text:123` 并入引语即可）。

### W6 ★提示 —— 原句 5 的「翻来覆去看了看」

**原文侧** `text/ch11_11.txt:120` `Amy said, **looking the letter over**.`

**md 侧** `md:49` `**中文理解**：艾米把那封信翻来覆去看了看，说：…`

**结论**：原文是「把信端详一遍」，「翻来覆去」暗示反复翻动，动作被加重。**提示**（措辞）。

---

## 四、三张单子小结

| 单子 | 阻断 | 提示 | 条目 |
|---|---|---|---|
| 漏 | 1（L1 动机线两个数 + `md:13` 导航承诺未落地） | 2（L2 第三封信；L3 关停/遗嘱/恋人/Nathan） | 3 |
| 编 | 0 | 6（C1 冰箱贴；C2 整体出手；C3 当众；C4 始终在案情室；C5 三种译名；C6 toi moko 释义） | 6 |
| 错 | 2（W1 两摞 vs 同一个文件夹；W2 他母亲归属） | 4（W3 早已办妥；W4 几十年；W5 引语边界外扩；W6 翻来覆去） | 6 |

**阻断合计 3 条**（L1、W1、W2）。
