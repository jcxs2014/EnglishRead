# 五步审查 d 步 · 语义二审 · 组 d2（October Daye #20 / A Divided Duty）

- **组号**：d2（覆盖 ch05–ch08）
- **覆盖章节**：`ch05 five.md` / `ch06 six.md` / `ch07 seven.md` / `ch08 eight.md`
- **依据的 text/ 文件清单**：`text/ch05_five.txt` / `text/ch06_six.txt` / `text/ch07_seven.txt` / `text/ch08_eight.txt`（书目录 `notes/books/novels/october-daye-20-divided-duty-by-seanan-mcguire/`，md 与 text 按章号对应）

**核对方法**：逐块四查（① 引语↔分析对应·防截短；② 说话人（±200 字符窗口）；③ 事实断言/数字/时序/章节引用；④ 语法·语言学断言）。"逐字"判据＝展平子串（`re.sub(r'[^a-z0-9]','',s.lower())`）对**本章** `text/` 全文命中；四章 md 内无 `chNN` 式跨章引用（均为"本章/后文"式表述，逐条核过）。**ch05–ch08 共 32 块：32/32 条引语逐字命中本章 text；报告行内"存疑"均附 md 逐字与 text 证据。**

---

## ch05 five.md（8 块）

- 原句 1 — ❓存疑：『读者视角提示』称"这个对照"（提问者的热望／当事人的谨慎）「在本章后半（她想起 Bridget 的请求时）会再次出现」——但 ch05 中 Bridget 的实写仅开场一带（本人即提问者，text:17–53）与 text:260「I could sort of see Bridget’s position」（立场）两处，全章并无与"请求"对应的文本落点，后半也未见该对照再现；或系对该处"立场"的转写失准。引语本身逐字✅（text:23）、说话人＝October✅。md 原文逐字「而这个对照在本章后半（她想起 Bridget 的请求时）会再次出现」；text 证据 `text/ch05_five.txt:260`「I could sort of see Bridget’s position, though.」
- 原句 2 — ✅ 逐字（text:143）；说话人＝Simon（text:140 "You sound proud of that." 后接本句，md 所称"对方"即 October）；"my darling girl"＝August、golden eyes 认亲（text:137）核对无误。
- 原句 3 — ✅ 逐字（text:212）；说话人＝Tybalt；提示的 "sobered" 有出处（text:209 "from the way he sobered"）；must 宣言体、gilded cushion/rafters 对置与句面一致。
- 原句 4 — ✅ 逐字（text:224）；叙述者内省（非对白）；"同一判断说两遍、第二遍时间状语前置"属实；主系表收束属实。
- 原句 5 — ✅ 逐字（text:446）；说话人＝October，回应 Raysel "You promise?"（text:443）；誓词无条件句、血/心对句与 cut grass and copper 均在引语内。
- 原句 6 — ✅ 逐字（text:494）；说话人＝October，对 Raysel（同段 "But here's the thing, Raysel"）；loved（过去时）/you've become（现在完成）/As long as 条件句，语法断言属实。
- 原句 7 — ✅ 逐字（text:503）；"这一声抢在递出孩子之前"成立：Toby「Here, take her」（text:500）→ 门口声音（text:503），最终未交至 Raysel 手中；登场者名字延迟至 text:509 才点破，属实。
- 原句 8 — ✅ 逐字（text:575）；"全章以一行独立短句收尾（More fool me.）"属实（text:578 为全章末行）；foolishly/would 均在引语内。

本章块数 8/8；报警 0；存疑 1。

## ch06 six.md（8 块）

- 原句 1 — ✅ 逐字（text:17）；"同一个 pomp and circumstance 稍后在正厅从 Quentin 低声吐槽中响起"属实（text:347）；May 留守为本章开场交代，"另一位缺席者"＝Simon 有出处（text:257 "someone needed to stay home with the babies"）。
- 原句 2 — ✅ 逐字（text:116）；sentinels / unknowable danger / the kingdoms we acknowledge now 均在引语内；千年尺度收束与口语化自评属实。
- 原句 3 — ✅ 逐字（text:182）；说话人＝Eion（引语自带 said Eion）；放开手→看向队伍→询问同行者三动作顺序属实；"今晚把门的人"有出处（text:173 "I stand guard"）。
- 原句 4 — ✅ 逐字（text:209）；说话人＝Raysel（whispered Raysel）；"心里的下一句话"有出处（text:215「This whole thing was verging on invasion of privacy, and it wasn’t cute.」）；"没人向刻工提供细节"有出处（text:212 "none of the people who’d been there … had provided the details for that carving"）。
- 原句 5 — ✅ 逐字（text:380）；说话人＝Dianda；被动式串（was pulled/had been placed/were lost）属实；"她儿子的手"与原文用词相合（text:467「She cut off my son’s finger」/「I care about my kid’s hand」）。
- 原句 6 — ✅ 逐字（text:440）；说话人＝Raysel；"父亲抬头的动作"属实（text:443 "he did lift his head and look at Raysel"）；term of service / getting better 交替出现属实。
- 原句 7 — ❓存疑：『为什么这样写』把 Luna 报出 Blind Michael 之名这一手的"风险"写成"新听众未必愿意为旧魔头的名字动容"；但该处新听众的反应恰是全场最响的抽气（text:416 "gasped most loudly"），叙述真正点名的 "first mistake"（text:428）是随后提醒听众 Acacia 是 Titania 之女（"Reminding them that Acacia was her daughter"），并非这个名号本身。引语本身逐字✅（text:413）、说话人＝Luna✅、bowed…looked up 两动作✅。md 原文逐字「作者随后还借 October 的叙述点出这一手有多冒险：对新来的听众而言，Blind Michael 仍停留在“儿童故事”的层面——咒语的受害者未必愿意为一个旧魔头的名字动容」；text 证据 `text/ch06_six.txt:416`「A gasp ran through the room, coming most loudly from the newcomers.」、`:428`「That might have been Luna’s first mistake. … Reminding them that Acacia was her daughter was very close to calling Blind Michael a monster.」
- 原句 8 — ✅ 逐字（text:491）；说话人＝Patrick（text:485 "said Patrick"）；"全场转头"（text:485）、"手搭儿子肩"、自证顺序（from the land→our husband）均属实。

本章块数 8/8；报警 0；存疑 1。

## ch07 seven.md（8 块）

- 原句 1 — ✅ 逐字（text:17）；"门没锁"的最小事件＋两界时间差（人界白天/Summerlands 入夜）均在引语内；"跟随 Lilac 的路线一路向下"属实（text:116 点名 Lilac、text:140 "leading me down the balcony to the first winding stair"）。
- 原句 2 — ✅ 逐字（text:41）；说话人＝October（对小仙子）；封价（last offer）＋"自己去找"的软硬两手均在引语内；"前几轮还价压成极短段落"有出处（text:29 宴会一、text:35 "The next two banquets."）；"账本后面再走一笔"＝允带 Lilac 探亲（text:131）。
- 原句 3 — ✅ 逐字（text:95）；破折号定义澄清（"the title is about magical power, not political position"）确在句内；制度句现在时（manage）、退位句完成时（had effectively stepped down）与 without facing challenges 收尾均属实。
- 原句 4 — ✅ 逐字（text:215）；说话人＝October（承 Nolan 追问，text:212）；"just that: stories"与 justify punishing 属实；tearing itself apart 身体化收束属实；"解谜链第一环"与后文桌上湿痕呼应（text:566、text:572）。
- 原句 5 — ✅ 逐字（text:233）；说话人＝October（承 Nolan，text:230）；Easier to … than to … 对偶与 easy target / stones to throw 均在引语内。
- 原句 6 — ✅ 逐字（text:281）；叙述者视角；"标点缺席"属实（引语串内无逗号/句号/问号，仅空格与句尾省略号）；babbled、clinging to my arms 及"旁观者反应在前、私人崩溃在后"的顺序均属实。
- 原句 7 — ❓存疑：『为什么这样写』称"先给最朴素的答案（wine），破折号后接一句自省式的推理"——英文原文此处为逗号连接（"What you're tasting is wine," I said. "And what it is, is that …"），并无破折号；破折号仅见于 md 自己的中译（「至于它是什么——」）。引语本身逐字✅（text:605）、说话人＝October✅、两个落锤短句（Luna was here. Luna took Raysel.）与公文语域（notify Queen Windermere / abducted / outside the authority of the Mists）✅。md 原文逐字「先给最朴素的答案（wine），破折号后接一句自省式的推理」；text 证据 `text/ch07_seven.txt:605`「"What you're tasting is wine," I said. "And what it is, is that we didn't double-check to make sure Luna would still bleed in a way we could recognize after she lost her Kitsune skin.」
- 原句 8 — ✅ 逐字（text:611）；说话人＝October；最短宣言（无从句、have to）属实；"把会客厅许的承诺翻译成行程"有出处（text:461「"You promise?"」→ text:464「"I promise," I said … Promises matter … breaking a promise can come with magical consequences.」）。

本章块数 8/8；报警 0；存疑 1。

## ch08 eight.md（8 块）

- 原句 1 — ✅ 逐字（text:20）；说话人＝October（对 Chelsea）；"排除法"结构（先正判断、后连串否定）属实；was transported / wasn't portaled / wasn't taken 被动串属实、施动者缺席属实（两个 "So …" 收口均在引语内）。
- 原句 2 — ✅ 逐字（text:44）；说话人＝October；as good as 的措辞包装属实；"当众说满、纸面撤回"由引语内 "That wasn't entirely true: we had access to Oberon." 自证，"够得着 Oberon"改案性有后续（text:44 续句 "Oberon, the King of All Faerie, had authority in Blind Michael's lands"）。
- 原句 3 — ✅ 逐字（text:122）；说话人＝Quentin；mulish 姿态与 supposed to be 的"身份即义务"读法属实；"上一拍把车钥匙抛给他、往家里打发"有出处（text:116 "tossing them gently to Quentin"、text:119 "Get the car home"）；"我找得到你的地方"有出处（text:119 "I want you to be where I can find you"）。
- 原句 4 — ✅ 逐字（text:155）；说话人＝October；两句 worry 镜像属实；Chelsea 回敬「That's low, Daye.」在 text:158，属实。
- 原句 5 — ❓存疑：『为什么这样写』称"三个名字的排列就是本句的骨架——认可的链条一环追一环"，但本句（text:296）只见 Amandine、Miranda 两个专名，叙述者以"我"出现（非名字）；"她→我→Miranda 三代人"的链条成立，而"三个名字"在本句内无落点。引语本身逐字✅（text:296）。md 原文逐字「三个名字的排列就是本句的骨架——认可的链条一环追一环」；text 证据 `text/ch08_eight.txt:296`「We grow up, but we never outgrow the people we were as children. Not really. Amandine wasn't even my mother anymore, and I was going to be chasing her approval for the rest of my life. Not for the first time, I promised myself that Miranda was never going to need to feel like this.」
- 原句 6 — ❓存疑：『为什么这样写』称"主人从抽象概念换到说话者、再换到 Raysel"，但第二处用法 "you were 'supposed' to be in that pond" 的指向是受话者 Toby（池塘＝Toby 的禁闭，text:491 "my scales during my confinement in the pond"），并非说话者本人；该句说话人为 Luidaeg（text:299 "said the Luidaeg"，至 text:317 仍是她的回合）。引语本身逐字✅（text:311）、"词换手三次"的框架✅。md 原文逐字「同一个词，主人从抽象概念换到说话者、再换到 Raysel」；text 证据 `text/ch08_eight.txt:311`「you were 'supposed' to be in that pond」。
- 原句 7 — ✅ 逐字（text:407）；说话人＝Luidaeg；"不要血/誓/路费、要'克制'"有出处（text:401 "I have all the blood I need from you … The one thing I don't have right now is your restraint."）；限定词串（the both of you / for each of you / one time）与"女儿在险境也须停手"均在引语内；"紧接着补上的例外条款"＝text:428（godchild 豁免）。
- 原句 8 — ✅ 逐字（text:500）；说话人＝Luidaeg（同句 "she said, in a distant, almost dreamy voice"）；押韵对（sun/done、right/light）与 one candle's light 收口属实；"落地后夜鸟啼叫只隔几行"属实（text:512 "an owl—or something like an owl—screeched its challenge into the night."）。

本章块数 8/8；报警 0；存疑 2。

---

## 全书汇总

- **覆盖块数**：32/32（ch05 8/8；ch06 8/8；ch07 8/8；ch08 8/8）。
- **报警**：0。
- **存疑**：5（ch05 原句1；ch06 原句7；ch07 原句7；ch08 原句5、原句6）——均为低风险表述层项，引语与证据链本身无误。
- 32 条引语全部逐字命中本章 text；未发现引语截短、说话人错挂、事实/数字/时序/章节引用错误；四章 md 均无跨章编号式引用（相关"本章/后文"表述已逐条核过）。
