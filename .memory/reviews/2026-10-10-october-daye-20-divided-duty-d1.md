# 五步审查 d 步 · 语义二审 · 组 d1（October Daye #20 / A Divided Duty）

- **组号**：d1（覆盖 ch01–ch04）
- **覆盖章节**：`ch01 one.md` / `ch02 two.md` / `ch03 three.md` / `ch04 four.md`
- **依据的 text/ 文件清单**：`text/ch01_one.txt` / `text/ch02_two.txt` / `text/ch03_three.txt` / `text/ch04_four.txt`（书目录 `notes/books/novels/october-daye-20-divided-duty-by-seanan-mcguire/`，md 与 text 按章号对应）

**核对方法**：逐块四查（① 引语↔分析对应·防截短；② 说话人 200 字符窗口；③ 事实断言/数字/时序/章节引用；④ 语法·语言学断言）。"逐字"判据＝展平子串（`re.sub(r'[^a-z0-9]','',s.lower())`）对**本章** `text/` 全文；关键词锚定判据＝该英文词在本块引语（展平）内可寻；四章 md 内无 `chNN` 式跨章引用（仅"本章/后文/上一段"式表述，逐条核过）。**ch01–ch04 共 29 块：29/29 条引语逐字命中本章 text，关键词 29 块全锚定。**

---

## ch01 one.md（6 块）

- 原句 1 — ✅ 逐字（text/ch01_one.txt:40）；"两个 According to""Especially me 单独成句"与引语一致；undulating wail 在引语内。
- 原句 2 — ✅ 逐字（text:49）；说话人＝October（"I said"）；分析所述 Tybalt 的咕哝＋脸朝下倒回（text:52）属实；Sleep 为无宾语命令式，语法断言属实。
- 原句 3 — ✅ 逐字（text:94）；说话人＝叙述者本人（自报家门）；between / root 均在引语内；"非人从个人属性升级为家庭属性"与句面一致。
- 原句 4 — ✅ 逐字（text:118）；Gillian＝"my daughter"（引语自带）；"前面刚写'从来不敢想象的未来'"有出处（text:91）；being taught 被动语态判断属实。
- 原句 5 — ✅ 逐字（text:169）；"三天后到期 / 上限四个月"与引语一致；"女王还要两天才开庭""Raysel 父母几乎站到家门口"有出处（text:172）。
- 原句 6 — ✅ 逐字（text:289）；说话人＝Tybalt（"he said"，回应 text:286 "Ready to face the night?"）；"face the night"在上一句（text:286）；"章首她独自走向哭声"（text:43）属实。

本章块数 6/6；报警 0；存疑 0。

## ch02 two.md（7 块）

- 原句 1 — ✅ 逐字（text/ch02_two.txt:17）；FAE—MOST FAE—ARE 全大写属实；"昼行例外 Jazz""已出炉的松饼"有出处（text:17 同段）。
- 原句 2 — ✅ 逐字（text:38）；说话人＝May（"countered May"）；Auntie May→kitten 称呼分层属实；centuries 在引语内。
- 原句 3 — ✅ 逐字（text:140）；说话人＝Chelsea（text:134 起同一轮对话，前句 "Raysel's terrified," she said）；内层条文 only if / shall return 与"谁求的（Duchess Lorden）谁批的（Queen Windermere）"均在引语内。
- 原句 4 — ✅ 逐字（text:176）；说话人＝Chelsea；"narrowed my eyes→举手→Messenger! Do not shoot!"邻接顺序与 text 一致；Tybalt 低吼＋"我强迫自己慢慢点头"（text:179）属实。
- 原句 5 — ✅ 逐字（text:164）；亲属链核对：Acacia＝Luna 之母（text:158）、Raysel＝Acacia 外孙女（引语 "her granddaughter"）；"Except."（text:161 段末）属实。
- 原句 6 — ✅ 逐字（text:221）；说话人层为 October 内视转述（"I don't think either of us had realized"，text:221）；do/wouldn't 镜像判断属实。
- 原句 7 — ✅ 逐字（text:275）；说话人＝October（自问）；"上一句是 This shouldn't take too long"（text:272）属实；will/learn 时态判断属实。

本章块数 7/7；报警 0；存疑 0。

## ch03 three.md（8 块）

- 原句 1 — ✅ 逐字（text/ch03_three.txt:26）；Oberon's antler / the sea witch 在引语内；"借来就没还"的外套有出处（text:26 "a loan … become permanent"）。
- 原句 2 — ✅ 逐字（text:83）；"通篇只用代词指他"属实（him×3）；指代对象＝Sylvester（text:80 段 "He chose my mother's secrets over my well-being"）。
- 原句 3 — ✅ 逐字（text:203）；"her"＝Luna（上段 text:200 "This was Luna's handiwork"）；同一朵花叠三个女人（Luna/Titania/Evening）与句面一致；"Roses, rich red garden roses"同位语属实。
- 原句 4 — ❓存疑（引语本身逐字✅，text:278；说话人＝Melly✅）。存疑点：md:55 读者视角提示「被一句"Please."磨开了口」的时序与原文相反——text 中 "Melly, come on. Please."（ch03_three.txt:269）出现在 Melly 拒绝「不是我该讲的事」（:272）**之前**；拒绝之后真正紧接着的是再叫一声 "Melly."（:275），随后她才开口（:278）。md 原文逐字「她说这"不是我该讲的事"，被一句"Please."磨开了口」；text 证据 ch03_three.txt:272「It doesn't feel as if it's my place to tell the Duke's business, if he hasn't chosen to disclose it.」/ :275「"Melly."」/ :278「"His Grace is arranging a celebration of his only daughter's return…"。或因压缩表述所致，故列存疑不列确定缺陷。
- 原句 5 — ✅ 逐字（text:317）；说话人＝Sylvester；"My lady has asked me""三天""今晚开始"均在引语内。
- 原句 6 — ✅ 逐字（text:353）；说话人＝October；两个 if、that's abuse、直呼其名 Sylvester（非爵衔）属实；"对方不反驳、转去自述孤独"有出处（text:356 "Who else do I have?"）。
- 原句 7 — ✅ 逐字（text:365）；说话人＝Sylvester；alone 三次计数属实（条件句/宣告/自我诊断）；"声音低下去＋低头看手"在引语内。
- 原句 8 — ✅ 逐字（text:454）；说话人＝October；"Yes, I do"接下法理、"要求解除"为程序内反抗、收尾两个否定句（not… / Neither…）均与句面一致。

本章块数 8/8；报警 0；存疑 1。

## ch04 four.md（8 块）

- 原句 1 — ✅ 逐字（text/ch04_four.txt:17）；说话人层为 October 旁观转述；"站姿落差"（lounging→ramrod straight）、"她真的扑上去"（text:47 Luna launched herself at him）属实。
- 原句 2 — ✅ 逐字（text:71）；说话人＝Luna；"出现在她扑人被闪开、自己撞上墙之后"成立（text:47→:71）；"十四年囚禁"有出处（text:80 "For fourteen years, I'd been imprisoned…"）。
- 原句 3 — ✅ 逐字（text:92）；指代核对：'she's right when she says I chose Faerie over her' 的 she＝**Gillian**（text:92 前句 "the only way Gillian was ever going to let me be a part of her life … her justified anger"），md 分析归 Gillian 正确；"对 Luna 说"（引语呼语 "I lost everything, Luna"）属实。
- 原句 4 — ✅ 逐字（text:158）；说话人＝Sylvester；"同一个名字喊两次、第一次是警告"有出处（text:149 "…said Sylvester warningly"）；"用'位置'划线、I want her here 押上自身意志"与句面一致。
- 原句 5 — ✅ 逐字（text:185）；说话人＝Luna（离场前）；knives and arrows / mother-love / recover from this wound 均在引语内。
- 原句 6 — ✅ 逐字（text:215）；说话人＝Sylvester；"互为镜像"属实（前场 "You have no right to deny her place" text:158 ↔ 此处 "I have no right to claim him as my brother"）；"声音闷在两只手里"在引语内。
- 原句 7 — ✅ 逐字（text:353）；说话人＝Simon；"one of Dean's friends"＝Chelsea 链条核对无误（text:257 Chelsea 会开 Saltmist 传送门 / text:278 正是她受托前去）；nursery 细节在引语内。
- 原句 8 — ✅ 逐字（text:455）；说话人＝Etienne；账户顺序（her/you/Sylvester/女王）与引语一致；"no fair way of refusing it"在引语内。

本章存疑（2 条，均在非引语层，引语与说话人全部✅）：

- 原句 3（读者视角提示，md:45）— ❓存疑：「也对书房里那个一直沉默的人」把 Sylvester 说成"书房里"——该场对峙发生在书房**门外走廊**，Sylvester 立于门外（text:116 "Behind her, Sylvester looked absolutely stricken"；text:197 之后 "go into your study" 才进屋；本章导航亦自述场景为"走廊—书房"）。"他在场且未插话"的实质正确，仅位置表述与原文不符，列存疑。
- 导航层（人物弧线，md:12）— ❓存疑：「Sylvester：从墙边沉默的丈夫」——"墙边"在 ch04 text 只归于 Tybalt（text:17 "Tybalt was standing near one wall"）、撞墙的是 Luna（text:47 "letting her slam into the wall"）；Sylvester 的位置全章未描写。列存疑（导航层）。

本章块数 8/8；报警 0；存疑 2。

---

## 本组汇总（ch01–ch04）

- 覆盖：4 章 / **29 块，29/29 完成四查**并逐块出证。
- 引语逐字：**29/29**（展平子串对本章 text；无跨章、无截短、无拼接——19 字至 443 字各长度均整串命中）。
- 关键词锚定：29 块全过（每块 2–3 个英文关键词均可在本块引语中寻得）。
- 说话人：29 块逐条开窗核对，全部归属正确（October / Tybalt / May / Chelsea / Melly / Sylvester / Luna / Simon / Etienne）。
- 事实断言与章节引用：身份关系（Raysel＝Sylvester 之女、Acacia＝Luna 之母、Simon＝Sylvester 孪生兄弟、Chelsea＝Etienne 之女等）、数字（三天/四个月/两天/十四年/alone 三次/centuries）、时序（第 271 行 Accusation 在撞墙之后等）逐条回 text 取证，未发现无出处断言之确定项；四章无 chNN 式跨章引用。
- 语法断言：无宾语命令式（Sleep）、被动语态（being taught / was taught）、分词短语（rooting…）、条件句结构（only if / 两个 if）、时态（will 指将来 / learn）逐条核对属实。
- **报警 0；存疑 3**（ch03:1 条——Melly 被"磨开"的时序；ch04:2 条——"书房里"、"墙边"两处位置表述）。存疑 3 条均附行号与逐字证据，未混入确定缺陷，留待审查方定性。
- 审查局限（如实标注）：本代理无写作上下文、单轮逐块核对；未核 md 中文行文与索引类元数据；`00_*.md` 总览不在本组口径。
