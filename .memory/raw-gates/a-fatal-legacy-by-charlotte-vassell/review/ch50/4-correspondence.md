# 4-correspondence.md · 第 50 章逐块对应人判（R4）

- 方法：对每一块只问一句——**这段中文是不是在讲这句引语？** 再问固定三问：① 每个动词的主语是谁 ② 受事/宾语是谁 ③ 涉及「谁的 / 谁欠谁 / 谁问的」时回原文核对 `by / to / from / of`。
- 不看子项标题先作答，再对照标题复核；判定档：对应成立 / 对应失真（阻断）/ 密度不足 / 讲引语之外（引语选短）/ 不对应（讲主旨或生平）。
- 原文区间写法同 `3-diff.md`（原始文件字符偏移）。

---

## 分析单元总表

| 单元 | 原文位置 | 对应 | 施事/受事核对 | 密度 | 备注 |
|---|---|---|---|---|---|
| 原句 1 | `:66` `[1689,1731]` | ✓ | ✓ | ✓ | 否认落点分析正确 |
| 原句 2 | `:78` `[1869,1930]` | ✗ 失真 | ✗ | ✓ | D2（阻断） |
| 原句 3 | `:96` `[2536,2940]` | ✓ | ✓ | ✓ | 本章最关键块，转述准确 |
| 原句 4 | `:99` `[2943,3103]` | ✓ | ✓ | ✓ | 「本章没给答案」核对成立 |
| 原句 5 | `:112` `[3227,3278]` | ✓ | ✓ | ✓ | D6（提示，绝对化） |
| 原句 6 | `:145` `[4394,4655]` | ✓ | ✓ | ✓ | D3（阻断，归属）、D5（提示） |
| 导航 1 一句话概括 | — | ✓ | ✗ | ✓ | D4（地点）、D9（多走一步） |
| 导航 2 视角 | — | ✓ | ✗ | ✓ | **D1（阻断，涨红的脸）** |
| 导航 3 线索结构 | — | ✓ | ✓ | ✓ | L1、L2（漏） |
| 导航 4 人物弧线 | — | ✓ | ✓ | ✓ | D9（提示） |
| 导航 5 叙事手法 | — | ✓ | ✓ | ✓ | D7（提示）、F1（MONDAY 为真） |

**对应组结果：11 个分析单元，对应成立 8，对应失真 3（全部为施事/归属/否认对象类）。**

---

## 逐块详判

### 原句 1 — `‘What? I don’t have an account like that.’`（`:66`）

- **是不是在讲这句引语**：是。中文理解（`Matt 刚说完“我们认为他们是顺着你的粉丝小说账号找到你的”，Isolde 的第一反应是反问「什么？」，接着否认：「我根本没有那样的账号。」`）逐项对得上：Matt 在 `:57` 说 `We think that they follow you on your fanfic account.`，Isolde `:60` `‘My what?’ Isolde looked confused.`，`:66` 是她否认账号。
- **三问**：① 主语＝Isolde（说话人）✓；② 受事＝`an account like that`，否认的是**账号是否存在** ✓；③ 归属——分析说 `这层否认在几分钟后被笔记本电脑上的登录状态顶了回来` → 原文 `:87` `‘You’re still logged in.’ He spun the laptop around.` ✓ 方向正确（是 Matt 用她的笔记本推翻，不是她自认）。
- **密度**：有「为什么这样写」（落点差异、争取到的对话方向），非字面复述 ✓。
- **判**：对应成立。

### 原句 2 — `‘I do not write dirty stories for strangers on the internet.’`（`:78`）—— **对应失真（阻断）**

- **是不是在讲这句引语**：中文理解本身对得上（Matt `:75` 说 `There’s no need to be embarrassed—`，Isolde 顶回）。但「为什么这样写」里的一句**把引语读反了**：
  > `而“给陌生人写”这个结构……**等于承认那个账号存在、只是不归她管**。`
- **三问**：① 主语＝Isolde ✓；② 受事＝`dirty stories for strangers`，这句**只否认「写」这个动作**；③ 归属——「承认账号存在」这个动作在原文里发生在**之后**（`:87` Matt 用她仍登录的笔记本），在 `:66`/`:72` 她恰恰两次否认账号存在（`I don’t have an account like that.` / `Absolutely not.`）。
- **额外**：md 自身原句 1 分析已写明她第一次否认落点在「这个账号存不存在」，并说该否认「几分钟后被登录状态顶了回来」——**同一份 md 的两块分析互相打架**。
- **密度**：其余部分（`dirty` 是道德判断、她谈到别人那件事用的词是 `seduce and murder a man`）密度足够 ✓。
- **判**：对应失真（阻断）→ D2。**这一条正是本章专属判据 ① 的落点：她否认的对象是「那些故事是不是我写的」，在原句 2 这个时点上她还没有承认账号存在。**

### 原句 3 — `‘I didn’t.’ She clicked on the last story. ‘Two things: firstly, I’m an English lead – the grammar is appalling. Secondly, I was at work when this was published. …’`（`:96`）

- **是不是在讲这句引语**：是，且是本章转述最准的一块。逐项核对中文理解：
  | md 中文 | 原文 |
  |---|---|
  | 她是一名英语语言教学 lead | `firstly, I’m an English lead` |
  | 那些文章的语法糟透了 | `the grammar is appalling` |
  | 文章发布的那天她正在上班 | `Secondly, I was at work when this was published` |
  | 正是在上课中间（提示，见 D8） | `That’s right in the middle of a school day` |
  | 她在 Stratford 的一所学校代课 | `I was substituting in a school in Stratford` |
  | 笔记本放在家里 | `I didn’t have my laptop, it was at home` |
  | 上班从不带自己的设备 | `I never use my own devices when I’m at work` |
  | 连手机都关机 | `I even turn my phone off` |
  | 「我这样会给人树立什么榜样？」 | `What sort of example would I be setting?` |
- **三问**：① 主语＝Isolde（她点开故事、给出两条理由）✓；② 受事＝`the last story`／那些故事 ✓；③ 归属——`I’m an English lead` 是**她本人的身份陈述**（她另在 `:84` 说 `apply for English language teaching jobs in Italy`，与「英语教学」身份一致，md 的「英语语言教学 lead」不与原文冲突；也没有把 `lead` 误读成「铅」）。
- **密度**：「为什么这样写」给出了理由排序（先文风后行踪 = 越需要核查的越往后）、身份筑墙、师德落点，有「为什么」✓。
- **判**：对应成立。**本章专属判据 ②（反驳理由是否被准确转述）在此块通过。**
- **附**：此块也证明 md **没有**把「嫌疑」写成「事实」——她的话只到「这些我没写过」「我在别处」，md 如实写成「否认」，未写「真正的 Isolde 自己也在写同人小说」⇒ 判据 ① 的红线未被触碰。

### 原句 4 — `Matt nodded, and turned the laptop back round to face him. He went back to the dashboard and the summary of the stories posted. ‘Where were you on these dates?’`（`:99`）

- **是不是在讲这句引语**：是。中文理解逐项对上：Matt 点头、把笔记本转回、退回后台看作品列表、问「这些日期你人在哪里」。
- **三问**：① 主语＝Matt（问话人）✓；② 受事＝`the dashboard and the summary of the stories posted`（他去看的东西）✓；③ 「谁问的」＝Matt ✓——md 没有把这一问算到 Robbie 头上。
- **对应核验（md 的强断言逐条回原文）**：
  - `可这一问之后紧跟一个分节符` → 原文 `:104` 即 `* * *` ✓
  - `本章没有给出她的回答` → `:104`–`:109` 之间无 Isolde 台词 ✓
  - `她人已经走出大楼了` → `:109` `Matt escorted her out of the building.` ✓
  - `她此前只交代过“最新那一篇发布当天”在哪儿` → `:96` 她点开 last story 后说 `I was at work when this was published` ✓（「this」= 她刚点开的那篇）
- **密度**：✓ 有「为什么」（问句层级从身份抬到行踪；后台日期清单才是可逐条对照的东西）。
- **判**：对应成立。

### 原句 5 — `‘I feel so violated.’ She turned to Matt. ‘Why me?’`（`:112`）

- **是不是在讲这句引语**：是。中文理解「走进电梯时她转过身对 Matt 说」对上 `:109` `They entered the lift.` → `:112` `She turned to Matt.` → `:115` `he said as the lift door opened.`（两人在电梯里，对话发生在进电梯之后、门开之前；「走进电梯时」属可接受的简化）。
- **三问**：① 主语＝Isolde ✓；② 受事＝`I feel so violated`（她对自己处境的判断）✓；③ 归属——`她描述的不是“身份被冒用”，而是“被侵犯”` ✗ **与原文 `:54` 冲突**：她自己也说过 `Stealing parts of my life to seduce and murder a man.`（身份被窃取的说法）。且 md 自家原句 2 已承认她对那件事用的是「身份」一词 ⇒ 自相矛盾（→ D6，提示）。
- **密度**：`violated` 作为自我定位词、三步同向的应对结构 ✓。
- **判**：对应成立（附一条绝对化措辞的提示）。

### 原句 6 — `‘I see. It’s probably hard for them to keep track of all their property.’ Andy nodded, quickly smiling to himself. ‘Their house in Hertfordshire has lots of priest holes. It’s an interesting site. And Priory Square has a fascinating history. Did you know that?’`（`:145`）

- **是不是在讲这句引语**：是。中文理解逐项对上（说家族产业不好管理、自己笑了一下、Hertfordshire 宅子的 priest holes、Priory Square 的历史、「你知道吗？」）✓；`priest holes（藏人的地洞）` 的释义与原文用法相符 ✓。
- **三问**：① 主语＝Andy ✓；② 受事＝`their property`／`Their house`／`Priory Square` ✓（their = Beauchamp 家，依据 `:142` `his family own the leaseholds`）；③ **归属方向错**：
  - `被问到自己家族与地下的关系时` —— 原文里 Andy **不是被问**的：他自己抛出 `Did you know that?`（`:145`），Matt 只回 `‘No, I didn’t,’`（`:148`）与 `‘Yes?’`（`:154`）；且原文 `:151` 明写 `‘Your colleague’s ancestors …’` —— 那家族是 **Matt 同僚 Beauchamp 的祖先**，不是 Andy 的「自己家族」。
  - `Matt 的全部回应只有一句“No, I didn’t”` —— 原文 Matt 在这一段有三次回应（`:148`、`:154`、`:160`），且 `‘Yes?’` 正是引出 Andy 那整段十六世纪「科普」的触发点。
- **密度**：`把范围指向警方正在查的那片区域` 这一推论经跨章核验**成立**：epub 目录与正文显示 Priory Square 即案发区（`text/ch01_1.txt:17` `The Horatio Combe Institute, Priory Square, Camden`；`text/ch33_33.txt:274` `Priory Square had been the site of St Agnes’s Priory …`；`:286` `In the 1860s, when the houses that now form Priory Square were constructed…`；`:331` `Priory Square. It’s Beauchamp land.`）✓
- **判**：对应成立，但**含一条归属阻断**（D3）与一条绝对化提示（D5）。

---

## 导航五项复核（不计入「块」，但同为 md 的中文层）

1. **一句话概括** —— 与原文相符（`:45`–`:99` 的问话 + `:145` 的 Andy 闲话）；两处措辞问题：地点「警局门口」实为警局内接待处（`:115` `He walked her back to reception.`）→ D4；「用我的名字写色情故事」比她原话 `Someone’s writing dirty stories about me online.`（`:121`）多走一步 → D9。
2. **视角** —— `第三人称限知，主要贴着问话的 Matt` ✓（叙述者始终在 Matt 视角：`:57` 的心里话、`:148` 的 `He wasn’t sure why Andy looked so pleased.`）；`Isolde 的内心全部靠台词与动作传达` 的列举中 **`涨红的脸` 属 Matt**（`:57` `Matt started to blush.`）→ **D1（阻断）**；`瞪眼/跛着走/掉泪` ✓（`:90` `stared`、`:109` `moon boot`、`:121` `the tears that had been forming`）。
3. **线索结构** —— 四条线逐条对得上（账号仍登录 `:87`、语法与发布时间 `:96`、Stratford 代课/笔记本在家/手机关机 `:96`、35 号监控与录像扫描程序 `:166`/`:169`），但**漏了本章开头的「Forensics 找到真隧道 / Robbie 赶往 Institute」**（`:23`）与**Andy 后半段（十六世纪封地道、老 Horatio）**（`:157`）→ L1、L2。
4. **人物弧线** —— `从“我是身份被冒用的受害者”一路滑到“有人在用我的名字写色情故事”` 的时间方向 ✓（`:54` → `:121`），但末句措辞多走一步（D9）；`Matt 则在送走她之后转身去查监控` ✓（`:115` → `:166`）。
5. **叙事手法** —— `问答体推进` ✓；`中间夹一段 Matt 的心里话（他满脑子想的是 salad sex）` ✓（`:57`）；`段落末尾又塞进 Andy 的一整段“科普”` ✓（`:157`）；`分部 MONDAY` ✓ **经 epub 核验为真**（`OPS/s064-Part-010.xhtml` 标题 `MONDAY`；TOC：MONDAY 段含 48/49/50/51）——**「按唯一权威源查无」是语料口径造成的假红**；`“我没回答那个问题”与“我没听懂那番话”这两处空白` 中第二处与原文 `:163`（`He wanted to ask Matt something else but backed off it.`）不对应，`下一次再看录像时才结算` 在 `text/ch51_51.txt` 未兑现 → D7。

---

## R4 结论

- **引语选短**：0 处（6 块引语与其分析所指区间一一对应；无「分析讲的是引语之外的上下文」）。
- **讲全书主旨/作者生平**：0 处（全部 6 块都在讲本章事件）。
- **只复述字面、密度不足**：0 处（6 块的「为什么这样写」均给出写法动因）。
- **施事/归属反转**：3 条 —— D1（涨红的脸：Matt → Isolde）、D2（否认读成让步）、D3（Beauchamp 家 → Andy「自己家族」／被问方搞反）。
- **未查**：0（6 块 + 5 导航项 + 词汇表 27 条 + 跨章两处断言，全部实查）。
