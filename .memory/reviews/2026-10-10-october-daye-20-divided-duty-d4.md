# 五步审查 d 步 · 语义二审报告（A Divided Duty / October Daye #20）

- 组号：d4
- 覆盖章节：ch13–ch16
- 依据的 text/ 文件清单：text/ch13_thirteen.txt、text/ch14_fourteen.txt、text/ch15_fifteen.txt、text/ch16_sixteen.txt（另按需抽查 text/ch03_three.txt、text/ch08_eight.txt）

说明：全部块均已做「引语↔分析对应／说话人／事实断言（身份亲属·生死·唯一第一次·数字·时序·章节引用）／语法类别名」四查；引语逐字性用展平子串（re.sub(r'[^a-z0-9]','',s.lower())）核对，31/31 命中。

---

## ch13（md：ch13 thirteen.md ↔ text/ch13_thirteen.txt）

原句 1 — ✅（md:17；text:29 起逐字命中；说话人/Acacia 独白语境相符）
原句 2 — ✅（md:27；text:44；Tybalt 警告语境相符）
原句 3 — ✅（md:37；text:68；"He sobered." 在引语内，插入位置描述属实）
原句 4 — ✅（md:47；text:140；Luidaeg 对 Firstborn 真容的说明相符）
原句 5 — ✅（md:57；text:224；「血术师/万灵药」措辞校对无冲突）
原句 6 — ✅（md:67；text:383；「我们才是她的家人」独白引语相符）
原句 7 — ✅（md:77；text:446；对 Danny 说话的对象与「never about you」重点相符）
原句 8 — ✅（md:87；text:722；章末「她并不意外」推理与原文（目睹侧瞥、盘算退路）相符）

本章块数 8/8；报警 0；存疑 0

已核备注：① md:23「最后停在省略号上——话没说完」：引语内省略号实为句中停顿（text:29 该句续作 "made this place."），措辞略宽，未达报警门槛。② 导航/人物弧线抽查属实：Acacia 出树（text:74）、Tybalt「守炉火」承诺（text:395「I will be sure the fire is always lit in our hearth」）、化猫（text:452「Tybalt was feline」）、Danny 后视镜映出真脸（text:431）。

---

## ch14（md：ch14 fourteen.md ↔ text/ch14_fourteen.txt）

原句 1 — ✅（md:17；text:74 所在场景引语逐字命中；Melly 口气与禁令语境相符）
原句 2 — ✅（md:27；text:41；「九十年前」与 text:41「"Ninety years or so," she said.」相符）
原句 3 — ✅（md:37；text:74；「He knew what she was before he married her」支持对 Sylvester 知情不报的指控）
原句 4 — ✅（md:47；text:101；转述自被救孩子口供的来源描述（They told me）相符）
原句 5 — ❓存疑（md:57 块，问题在 md:63）：「为什么」将引语转述为「把'由受害者的血脉来接管施暴机器'说得像在分配一份职务」；引语原文为制造者（施暴者）的外孙女接管，同段后文亦写「制造者的外孙女」，仅此处作「受害者的血脉」——疑为笔误，且「受害者」一词存在低调辩护读法，故列存疑、不混入确定缺陷。text 对照：ch14_fourteen.txt:134 逐字「the granddaughter of the man who made them」；:113「She was born into safety, despite her grandfather!」
原句 6 — ✅（md:67；text:170；my ward / bring. Her. Home. 与 "I snapped" 均核对属实）
原句 7 — ✅（md:77；text:182；「效率词+伦理词并排修饰接刀」的分析与原文句法相符）
原句 8 — ❌【事实断言·「第一次」不成立】（md:95）md 原文逐字「也第一次把两人的分歧摆上桌面」；text 证据 ch03_three.txt:448 逐字「But I have a duty to that girl, and I won't let you hurt her.」及:451「You have a duty to me. You swore your oaths to me.」（另有:454 Toby 提出可请求解除誓言）——ch03 两人已当面把"对该女孩的承诺之责 vs 对我的誓言之责"这一分歧摆上桌面，ch14 并非第一次。

本章块数 8/8；报警 1；存疑 1

已核备注：① md:10/11/65 三处将该场景称为「书房」，text:332 原文为「into a small parlor with glass walls」（玻璃墙小客厅）；房间类别不属四查（身份亲属/生死/唯一第一次/数字/时序/章节引用）类别，未定级为报警，提请后续步骤复核。② md:65「'外孙女'勾住书房对话」的钩子偏松，但 Blind Michael—Luna—skerry 家族线（text:359「She's with her mother right now, in Blind Michael's skerry」）确贯穿后文对话。

---

## ch15（md：ch15 fifteen.md ↔ text/ch15_fifteen.txt）

原句 1 — ❌【语法类别名用错】（md:23）md 原文逐字「didn't stay away because I wanted to 用双重否定不说出'被迫'二字」；该句仅含一重否定（didn't），并非双重否定。text 证据 ch15_fifteen.txt:20 逐字「At least this time, I didn't stay away because I wanted to.」
原句 2 — ✅（md:27；text:50；Bridget「manner of the loss」段与说话人相符）
原句 3 — ✅（md:37；text:53；Chelsea 回话「gonna」与宣誓式短句分析相符）
原句 4 — ❌【事实断言·时序】（md:55）md 原文逐字「叙述者在通话结束后立刻用一段追述补上」；text 证据 ch15_fifteen.txt:224 逐字「Silences had been overthrown in the war, years and years ago…」位于引语（:221）之后、告别与挂断（:227「Talk to you later?」、:233「"Just doing my job," he said, and the line went dead.」）之前——追述发生在通话进行中，并非「通话结束后」。
原句 5 — ✅（md:57；text:251；浮雕场景与「I knew him」辨认相符）
原句 6 — ✅（md:67；text:467；Cassie「small club」悖论与会话转轴分析相符）
原句 7 — ✅（md:77；text:536；「lousy role models」对照与 Cliff 插入语分析相符）
原句 8 — ✅（md:87；text:644；「half-cocked 旧词」核实：同章 text:491（Toby 立规矩）与:494（Chelsea 转述 Quentin 反呛）两处前用属实）

本章块数 8/8；报警 2；存疑 0

已核备注：md:59「他胸前护着的 Arden 的纹章」系 "Arden's arms at his breast"（text:251）的引申译法（arms=纹章译对；「护着」为意译添加），未达报警门槛。

---

## ch16（md：ch16 sixteen.md ↔ text/ch16_sixteen.txt）

原句 1 — ❌【引语截短】（md:19 中文理解、md:23 为什么）引语自 "I am Sir October Daye" 起，但中文理解以「'嘘，'我说，接着更大声地说」开译，为什么以「先对 Chelsea 一声 'Shush'，紧接着 more loudly 把同一句话变成公告」为"音量机关"分析支点，均属引语之外且与之紧邻的内容。text 证据 ch16_sixteen.txt:26 逐字「"Shush," I said, and then, more loudly, "I am Sir October Daye. I serve your mistress as a Hero of the Realm.」
原句 2 — ✅（md:27；text:38；Tuatha 瞬移设定段与 "as I think…" 插入语断言相符）
原句 3 — ✅（md:37；text:56；「温柔地残忍」谈判句法与条件从句分析相符）
原句 4 — ✅（md:47；text:80；Eion 偏执式短句与 them 的不指名复数分析相符）
原句 5 — ❌【事实断言·亲属关系】（md:63）md 原文逐字「例证顺序也有算计：先死者之妹（时间上不可能有罪）」；引语中 Raysel 与「死者」（Eion 之兄弟）无任何兄妹关系，引语给出的理由仅为她当时尚未出生。text 证据 ch16_sixteen.txt:83 逐字「Raysel isn't 'them.' She wasn't alive yet when your brother was taken.」
原句 6 — ✅（md:67；text:107；Children's Hall 流程与「名字的温柔和机制的残酷」分析相符）
原句 7 — ❌【事实断言·数字】（md:83）md 原文逐字「而第三次呼唤不再换词、改成 know I tell you right 的担保句」；引语内 "Hear me" 呼语仅两次（weary rover→weary wanderer），"know I tell you right" 属第二次呼语的后半句，不存在"第三次呼唤"。text 证据 ch16_sixteen.txt:215 逐字「"Hear me, weary rover, and listen as you stand…" … "Hear me, weary wanderer, and know I tell you right: …"」

本章块数 7/7；报警 3；存疑 0

已核备注：① md:63 为什么兼及引语后同段续文（「比我俩都聪明的人」＝text:83「a conversation for smarter people than either one of us」；「Raysel 不该替父母的罪受罚」＝text:83「Raysel doesn't deserve to suffer for the sins of her parents」），属段级评注、未达引语截短门槛（中文理解/关键词均未出引语）。② md:12「跪地哀求」属实：text:140「He looked me dead in the eyes and dropped to his knees, beginning to babble.」③ 同一韵文在 ch08 亦出现（text/ch08_eight.txt:500、:506），呼语同为两次，无第三呼语可依。

---

## 全书汇总（本组 d4，ch13–ch16）

- 覆盖块数：31/31（ch13: 8，ch14: 8，ch15: 8，ch16: 7）
- 报警：6（ch13: 0，ch14: 1，ch15: 2，ch16: 3）
- 存疑：1（ch14 原句 5「由受害者的血脉」疑似反向）
- 报警分布：引语截短 ×1（ch16-1）；语法类别名 ×1（ch15-1 双重否定）；事实断言 ×4（ch14-8「第一次」、ch15-4 追述时序、ch16-5「死者之妹」亲属关系、ch16-7「第三次呼唤」数字）
- 质量核对：引语 31/31 展平逐字命中；说话人 31/31 与 text/ 前后文窗口核对通过；章节引用（chNN 等）无跨章引用项。
- 未覆盖项：无。
