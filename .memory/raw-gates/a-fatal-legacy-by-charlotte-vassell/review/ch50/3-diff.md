# 3-diff.md · 《A Fatal Legacy》第 50 章对账（漏 / 编 / 错）

- 审查对象：`/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch50 isolde is questioned about the stories.md`
- 权威原文：`.../text/ch50_50.txt`（172 行 / 6280 字节）
- 字符区间约定：`[start, end)`，起点为该行首个非空白字符在全文 UTF-8 码点中的偏移（与 `scripts/chapter.sh` 内部压缩空白后的 pos 不同，本文件一律用原始文件偏移）
- 交叉核对用：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/library/A Fatal Legacy (Charlotte Vassell) (z-library.sk, 1lib.sk, z-lib.sk).epub` → `OPS/s067-Chapter-050.xhtml`（除换行外与 `text/ch50_50.txt` 逐行相同 ⇒ **语料边界无问题**）
- R1 素读已完成并落盘（`1-suread.json`），本文件在 R1 之后写

---

## 一、漏（素读有、md 无）

### L1｜本章开头的「Forensics 在 Institute 找到真隧道 / Robbie 即刻赶往 Institute」全章零覆盖 —— 提示

- 原文（`text/ch50_50.txt:23`，区间 `[128, 372]`）：
  > `‘Robbie Eastley.’ He listened carefully to the forensics person on the other end. He grimaced as he ended the call. ‘I’ve got to go to the Institute, Matt. That nutter wasn’t talking about metaphorical tunnels. Forensics have bloody found one.’`
- 原文（`:26`，`[375, 447]`）：`‘What? Really? I’d give Caius’s dad a call in that case. It’s his land.’`
- 原文（`:32`，`[525, 568]`）：`Matt shrugged. ‘I’ll speak to Isolde then.’`
- md 侧：全文检索 `Robbie` 命中 1 次、`Institute` 命中 **0** 次、`forens` 命中 **0** 次；命中的一次 `Robbie` 在词汇表例句 `Robbie’s phone rang just as he and Matt were about to collect Isolde from reception.`（`:112`），**不在任何分析里**。
- 说明：这是本章唯一一处「案件推进」实锤（隐喻隧道被证实为真隧道），也是 Matt 得以单独问 Isolde 的前提（Robbie 去 Institute ⇒ Matt 接手问话）。md 的导航「线索结构」四条线、一句话概括、人物弧线均未提及。
- 初判：**提示**（md 精读体例为引语驱动，6 块覆盖不到全部节拍；但导航层宜交代这一拍，不影响正确性）

### L2｜Andy 那段「科普」的后半段（十六世纪封地道 / 拆修道院 / 老 Horatio / precedence）无引语块、也无分析 —— 提示

- 原文（`text/ch50_50.txt:157`，区间 `[4800, 5508]`，本章最长的一段台词）：
  > `‘Well.’ Andy moved closer to Matt. ‘When the current houses were built in the Victorian era and the priory was exposed for the first time in three hundred years, the Beauchamps already knew what was down there. They chose to seal it up again, like their ancestors had in the sixteenth century. They knocked the priory down, you know. Left the crypt and basement levels only. Whether your colleague and his family have an idea now is a different question. I appreciate that there has been a change in precedence. I wouldn’t be surprised if old Horatio knocked through. He was a Boy’s Own psychopath, after all. He wouldn’t have been able to help himself if he thought there was something valuable underneath.’`
- md 侧：全文检索 `Horatio` 命中 **0** 次；`十六` **0** 次；`维多利亚` 1 次（词汇表例句）；`crypt` 2 次（均为词汇表例句与分析里的英文原文）。原句 6 的引语止于 `:145` 的 `Did you know that?`，其「为什么这样写」与「读者视角提示」也停在 `:145`。
- 说明：`:157` 这段是本章对 Beauchamp 家族最重的一击（祖先二次封死地道、拆掉修道院只留 crypt 与 basement、老 Horatio 可能打通），md 的导航「线索结构」只写了 `Hertfordshire 住宅里的 priest holes、Priory Square 的修道院遗址`，**该段未被任何一层覆盖**。
- 初判：**提示**（漏覆盖，非错写）

---

## 二、编（md 有、原文无）

### F1｜「分部 MONDAY」——按唯一权威源查无，但经 epub 交叉核实为真 ⇒ **假红（语料口径）**，非 md 缺陷

- 权威源检索：`/usr/bin/grep -c -w "MONDAY" text/*.txt` → **无任何文件命中**（退出码 1）；`/usr/bin/grep -o -i -E '\b(monday|…|sunday)\b' text/*.txt` → 命中的全是散文里的小写/首字母大写星期词（ch05/ch06/ch13/ch30/ch35/ch36…），**ch50_50.txt 内无任何星期标记**。
- 报警复核（先假定语料口径错，再判 md 错）：解包 epub 后 →
  - `OPS/s064-Part-010.xhtml` 正文首个标题就是 **`MONDAY`**；
  - `OPS/TOC.xhtml` 的目录结构为 `… SATURDAY 41…47 / MONDAY 48 / 49 / 50 / 51 / TUESDAY 52 / 53 / SIX WEEKS LATER 54`；
  - `OPS/s067-Chapter-050.xhtml` 即本书第 50 章，落在 Part-010（MONDAY）之下。
- 结论：**md 的「分部 MONDAY」正确**；查无的原因是 `text/` 提取件丢弃了 epub 的 Part 标题层（语料口径问题），不是 md 编造。→ 档位 **假红**；并入 R5.5「已核实为正确」。
- 本书真正的「编」条目：**0 条**。

---

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序 / 地点 / 归属）

### D1｜「涨红的脸」被挂到 Isolde 身上，原文里涨红的是 Matt —— **阻断**

- md 侧（导航「视角」）：
  > `Isolde 的内心全部靠台词与动作传达（瞪眼、**涨红的脸**、跛着走、掉泪）`
- 原文（`text/ch50_50.txt:57`，区间 `[1364, 1624]`）：
  > `‘About that …’ **Matt started to blush.** He thought she was far too hot to be sat at home writing things like salad sex. Surely, girls like her were just out there getting laid rather than just imagining it.`
- 说明：这是施事反转——同一句里涨红的是提问者 Matt，且原文紧接着写的是他对 Isolde 的**物化式内心判断**。md 把「脸红」记到被问者 Isolde 名下后，导航里那句「Isolde 的内心全部靠台词与动作传达」就变成了一条错误陈述。
- 附带：「瞪眼」对 `Her large green eyes were full of earnestness`（`:48`）/ `Isolde stared at her homepage on the site`（`:90`）尚可，「涨红的脸」不可。
- 初判：**阻断**（施事/归属反转；四道机器探针全绿也抓不到这一类）

### D2｜原句 2 分析把 Isolde 的否认读成「承认那个账号存在」—— 与原文当场事实相反，且与 md 自己的原句 1 分析打架 —— **阻断**

- md 侧（原句 2「为什么这样写」）：
  > `而“给陌生人写”这个结构，则把写作这件事和她本人的实名生活切开，**等于承认那个账号存在、只是不归她管**。`
- 原文（`text/ch50_50.txt:66`，`[1689, 1731]`）：`‘What? I don’t have an account like that.’`
- 原文（`text/ch50_50.txt:72`，`[1789, 1827]`）：`‘Absolutely not.’ Isolde was offended.`
- 原文（`text/ch50_50.txt:78`，`[1869, 1930]`，即原句 2 本身）：`‘I do not write dirty stories for strangers on the internet.’`
- 原文（`text/ch50_50.txt:87`，`[2138, 2419]`）：`‘You’re still logged in.’ He spun the laptop around.` —— **账号存在是在原句 2 之后、由 Matt 用她仍登录的笔记本推翻的**。
- 说明：原句 2 发生的那一刻，她 6 行前刚说过「我根本没有那样的账号」，此刻仍在否认；这句只否认「写」这个动作。md 却把它读成「默认账号存在、只是不归她管」——把**否认读成了让步**。
- 内部矛盾：md 自己的原句 1 分析写的是 `她第一次否认落点……在“这个账号存不存在”……可它在几分钟后被笔记本电脑上的登录状态顶了回来`——**同一份 md 里，原句 1 说她在否认账号存在，原句 2 说她承认账号存在**。
- 初判：**阻断**（对应失真 / 施事归属反转；正是本章专属判据 ①「她否认的具体对象是什么」）

### D3｜原句 6「读者视角提示」把 Beauchamp 家说成 Andy 的「自己家族」，且说 Andy「被问到」—— **阻断**

- md 侧（原句 6「读者视角提示」）：
  > `Andy 说这番话的语气不像闲聊，更像在试对方知道多少——**被问到自己家族与地下的关系时**，他笑着把话头从房子转到了广场。`
- 原文（`text/ch50_50.txt:142`，`[4248, 4391]`）：`‘No, it was a conflict of interest. He just discovered that **his family** own the leaseholds in the area where the crimes have been concentrated.’`（his = DI Caius Beauchamp）
- 原文（`text/ch50_50.txt:145`，`[4394, 4655]`）：`‘I see. … ‘**Their house** in Hertfordshire has lots of priest holes. It’s an interesting site. And Priory Square has a fascinating history. Did you know that?’` —— **Andy 是主动说**，Matt 只在 `:148` 回了 `‘No, I didn’t,’`；触发追问的是 Matt 的 `‘Yes?’`（`:154`）。
- 原文（`text/ch50_50.txt:151`，`[4733, 4788]`）：`‘**Your colleague’s ancestors …**’ Andy sagely drifted off.` —— 家族是 **Matt 同僚 Beauchamp 的祖先**，与 Andy 无关。
- 说明：两个方向都错了：**谁的家族**（Beauchamp 家 ≠ Andy 家）、**谁问谁**（Andy 主动抛出，Matt 从未就「家族与地下」向他发问）。
- 初判：**阻断**（归属 / 受事方向）

### D4｜「警局门口」—— Andy 说话地点是警局内的接待处 —— 提示

- md 侧三处：
  1. 导航「一句话概括」：`而她的前男友 Andy **在警局门口**随口讲的一段地理知识`
  2. 原句 6「为什么这样写」：`前男友**在警局门口**的一段家常闲话`
  3. 一句话总结：`她的前男友 Andy **在警局门口**随口说起的 priest holes 和 Priory Square`
- 原文（`text/ch50_50.txt:115`，`[3281, 3411]`）：`He walked her back to **reception**. Andy, her ex, was waiting for her.` —— 接待处在楼内；整段对话发生在楼内（`:118`–`:163`），`:166` 才 `He returned to his desk in the incident room`。
- 初判：**提示**（三处重复的地点失准，不影响情节）

### D5｜原句 6「Matt 的全部回应只有一句」—— 原文里 Matt 有三次回应 —— 提示

- md 侧（原句 6「为什么这样写」）：`Matt 的**全部回应**只有一句“No, I didn’t”，以及一句没头没尾的“他不明白 Andy 为什么看起来这么高兴”。`
- 原文：`:148` `‘No, I didn’t,’ Matt replied. He wasn’t sure why Andy looked so pleased.`；`:154` `‘Yes?’`；`:160` `‘Oh.’`
- 说明：且 `‘Yes?’` 正是引出 Andy 那整段十六世纪「科普」的触发点，原句 6 的分析把它当作不存在。
- 初判：**提示**（「全部」过硬）

### D6｜原句 5「violated 是这一章里她对自己的唯一定位词——她描述的不是『身份被冒用』」—— 提示

- md 侧（原句 5「为什么这样写」）：`**violated 是这一章里她对自己的唯一定位词**——她描述的不是“身份被冒用”，而是“被侵犯”。`
- 原文（`text/ch50_50.txt:54`，`[1052, 1361]`）：`‘Thank God. I’ve been petrified all week. It’s so grim. **Stealing parts of my life** to seduce and murder a man. …’` —— 她自己用的正是「人生被窃取」即身份被冒用的说法。
- 内部矛盾：md 自己的原句 2 分析写 `她谈到别人用她的身份做的那种事时用的词是“seduce and murder a man”`，与原句 5 的「她描述的不是身份被冒用」直接冲突。
- 初判：**提示**（绝对化措辞 + 与原文、与自家原文冲突）

### D7｜导航「叙事手法」里的第二处空白「我没听懂那番话」对不上原文；「下一次再看录像时才结算」在下一章未兑现 —— 提示

- md 侧（导航「叙事手法」）：`而“我没回答那个问题”与“**我没听懂那番话**”这两处空白，都被留到**下一次再看录像时**才结算。`
- 原文（`text/ch50_50.txt:163`，`[5519, 5647]`）：`Andy’s mouth quivered. **He wanted to ask Matt something else but backed off it.** ‘Anyway, I best drive Princess Isolde back home.’` —— 原文的空白是 **Andy 有话没问出口**，不是「某人没听懂那番话」；而 Matt 听懂了（叙述把 Andy 的话整段转述出来）。
- 跨章核验（下一章原文）：`/usr/bin/grep -n -i -E "where were you|alibi|Stratford|those dates|school" text/ch51_51.txt` → **零命中，退出码 1**（whereabouts 之问在下一章未答）；`/usr/bin/grep -n -i -E "number 35|footage|Amy" text/ch51_51.txt` → 仅 `:92` 命中 Marcus 说 `They're going to use a little robot with a camera`（site 上的机器人摄像），**35 号监控录像与 Amy 的扫描程序在下一章都没有结算**。
- 初判：**提示**（表述与原文不对应；跨章断言在前一章未兑现）

### D8｜「正是在上课中间」对 `in the middle of a school day` —— 提示

- md 侧（原句 3「中文理解」）：`文章发布的那天她正在上班——**正是在上课中间**，她在 Stratford 的一所学校代课`
- 原文（`text/ch50_50.txt:96`，`[2536, 2940]`）：`‘… That’s right in the middle of **a school day**. I was substituting in a school in Stratford. …’`
- 说明：`a school day` = 一个上学日/在校日的中段，「上课中间」易读成「一节课上到一半」。
- 初判：**提示**（措辞）

### D9｜导航「人物弧线」把 Isolde 的说法写成「用我的名字写」—— 比原文多走一步 —— 提示

- md 侧（导航「人物弧线」）：`Isolde 从“我是身份被冒用的受害者”一路滑到“**有人在用我的名字写色情故事**”`
- 原文（`text/ch50_50.txt:121`，`[3473, 3630]`）：`‘I need a strong drink,’ Isolde said, shaking her head as if to hold back the tears that had been forming. ‘**Someone’s writing dirty stories about me online.**’`
- 说明：她的原话是「about me」（关于我），不是「用我的名字」；本 md 没有把「冒名者是谁」写成事实（✓ 判据 ④ 满足），但「用我的名字」这一层比原文多走一步（原文只到「有人用她的账号发布、她说『这些我没写过』」）。
- 初判：**提示**

### D10｜词汇档位注水：`psychopath` 进 ⭐⭐⭐ —— 提示

- md 侧：`psychopath | 精神变态者 | He was a Boy’s Own psychopath, after all.`（⭐⭐⭐ 高级）
- 说明：`psychopath` 是日常高频词，与「metaphorical / leaseholds / priest holes / Victorian era / precedence」同列偏注水；`crypt`（兼有「密码」义）亦偏高级。
- 初判：**提示**（档位注水，S4 第 ③ 类）

---

## 四、对账小结

| 单子 | 条数 | 阻断 | 提示 | 假红 |
|---|---|---|---|---|
| 漏 | 2（L1、L2） | 0 | 2 | 0 |
| 编 | 1（F1） | 0 | 0 | 1 |
| 错 | 10（D1–D10） | 3（D1、D2、D3） | 7 | 0 |
| **合计** | **13** | **3** | **9** | **1** |

机器层（`2-machine.json`）：退出码 0，`verdict: ok`，6 块引语逐字全中、0 个省略号缝合、形态四项与本书众数一致、词汇例句 27/27 原文各命中 1 次 —— **机器全绿，但人判查出 3 条阻断型**，全部落在机器结构上查不了的「施事/归属/否认对象」三类。
