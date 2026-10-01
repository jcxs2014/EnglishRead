# 《Only a Monster》独立五步审查 — 缺陷清单与整改记录

- 书籍：`notes/books/novels/only-a-monster-by-vanessa-len/`（25 章精读 + 3 篇总览）
- 触发：用户主动发起「独立进行五步审查」（`AGENTS.md:236`「五步审查由用户主动发起」/ `:240`「用户在同一会话内要求时，本实例直接执行」）
- 执行依据：`AGENTS.md` 第 10 条 + `docs/新书启动模板.md:700-704` a–e 五小标题、`:707-710` 审查自身四条纪律、`:722-729` 开工前材料三样
- 口径：a–e 全部完整执行，不降级；同会话盲区只在结论部分标注

---

## a. 第 3 条提交门禁全量重跑（不信报告数字）

原始逐行输出：`/tmp/oam_a_gate.txt`（首跑）、`/tmp/oam_gate2.txt`（整改后复跑）。
命令：`bash scripts/gate.sh notes/books/novels/only-a-monster-by-vanessa-len` → **EXIT=0**（完整 lane，目录内有 epub）。

语料层复验（规则 1a）：
`python3 scripts/verify_corpus.py "$B" --expect 25 --expect-source "epub spine 实测：25 个 <h*> 章节标题 + 页内 TOC"`
→ `P0-0 语料验收: PASS（FAIL 0 / WARN 1）`。WARN 1 = 未给 `--anchors`，按 `AGENTS.md:118`「单 POV 长篇小说跑 ①④ 即可」属预期。

**a 步结论：门禁全绿，无内容缺陷**（但门禁本身暴露了 3 个盲区，见「工具盲区」一节）。

---

## b. 逐章归属

`check_chapter_quotes.py` 逐章实跑：**25 章全部命中本章 text**（ch06 / ch21 / ch25 各 5/5 +「另有 1 条短引语未校验」，已人工 grep 兜底）。
`verify_quotes` 块覆盖对账：`✅ 块覆盖对账：25 个文件，每块都进了 verify_quotes 校验`。

**b 步结论：无跨章错配，无遗漏块。**

---

## c. 结构扫描

| 检查 | 结果 |
| --- | --- |
| `check_struct_indep.py`（独立实现） | `独立结构扫描：25 个 md，缺陷 0 处` |
| `audit_structure` | `❌ 结构缺陷 0 ｜ ⚠️ 提示 0 ｜ 🔀 映射不一致 0` |
| ⑬ 空段扫描 | `0 处` |
| 25 章「一句话总结」字数 | 100–200 中文字，越界 **0** 处 |
| `corruption_scan.py` | `FAIL 0 处（U+FFFD / 双句号）` |

**c 步结论：无结构缺陷。**

---

## d. 语义二审

机械子项（**必须用三个独立实现**，`docs/新书启动模板.md:703`）：

| 脚本 | 结果 |
| --- | --- |
| `check_struct_indep.py` | 缺陷 0 处 |
| `check_xref_indep.py` | `chNN 引用 232 处：英文证据报警 0 处 ／ 中文式待人判 232 处` |
| `check_analysis_indep.py` | `抽出分析层英文片段 163 条 ✅ 全部片段在全书 text/ 逐字命中` |

> 这三个是**第二实现**（与 `audit_structure` / `check_crossref` / `sweep_analysis_inline` 不是同一把尺子），此前只验过 1 本书。

语义层交给三个子代理分章审，**每条我都回查原文后才动手**：

### d1. ch18–ch25（子代理 ffae5778）— 阻断型 4 / 提示型 7，**全部属实并已改**

| # | md | 缺陷 | 原文证据 |
| --- | --- | --- | --- |
| 1 | `ch19 eighteen.md:75` | `‘Oh, but you could, I suppose?’` 安到 Tom 头上 | `text/ch19_eighteen.txt:442` 无说话人标记，夹在 Tom 的 `:439` 与 `:445` 之间 ⇒ 只能是 Joan |
| 2 | `ch20 nineteen.md:73` | 「不是好人」的**老板娘** | `text/ch20_nineteen.txt:337` `Dorothy Hunt is not a good person` ⇒「不是好人」是 Joan 的 gran，不是 innkeeper；innkeeper 在 `ch15:553/:559` 是 he/him，性别也错 |
| 3 | `ch24 twenty-three.md:13` | 「Joan 说『他也许多久前就该尽他的责任』」 | `I should have done my duty a long time ago` 是 **Nick** 说的（源头 `ch23:415`，ch24 `:22` 是 Joan 的闪回） |
| 4 | `ch25 epilogue.md:65` | 两处「他哥哥」 | Tom 是 Jamie 的**表兄**（`ch22:64` `vouch for my cousin`） |
| 5 | `ch20 nineteen.md:63/:65/:112` | 「六族」「六大家族」 | `ch20:265` 实为 **11 个家族、7 个方位**（`Olivers and Alis in the west… And the Nightingales … ‘Anywhere they please.’`） |
| 6 | `ch21 twenty.md:53` | 「前三个否定句都用完成时」 | `ch21:394` 只有前两句是否定句，第三句 `Someone had done this to him` 非否定句 |
| 7 | `ch21 twenty.md:63` | 「最后三个问句」 | 落在 1922 前的内心问句只有 **2 个**（`ch21:418`） |
| 8 | `ch22 twenty-one.md:45` | 「belonged 用的是过去完成式」 | 实为**一般过去时**（虚拟条件句） |
| 9 | `ch25 epilogue.md:31/:33` | 「全章最短的一句」「五个词」 | `ch25:220` 有单词句 `Footsteps.`；`No one else did.` 是 **4 个词** |

### d2. ch01–ch08（子代理 7bd268fc）— 阻断型 5 / 提示型 5

| # | md | 缺陷 | 原文证据 |
| --- | --- | --- | --- |
| 1 | `ch06 five.md:73` | 「**两天前** Ruth 在厨房里说过的话」 | `text/ch04_three.txt:286` `Two years ago, she'd arrived at Gran's place for the summer` + `:295` `‘They hate us and we hate them,’ Ruth had said` ⇒ **两年前**、在 ch04 |
| 2 | `ch06 five.md:53` | 「作者让**死亡**以『那里空了』的方式进入」 | `ch06:355` 只写 `She was gone.`；`ch25:76,97,121,124` Ruth 仍在场 |
| 3 | `ch06 five.md:75` | 「家人刚刚**全部死**在这栋房子里」 | 同上：Ruth 是消失不是死（Gran 确实死在房里，`ch06:270`） |
| 4 | `ch08 seven.md:51` | 关键词 `painstakingly（费力地 painstakingly shifted）` 括号内重复粘进原文 | `ch08:328` `She took time, then painstakingly shifted and squeezed` |
| 5 | `ch03 two.md:31` | 关键词 `that meant that meant（那就意味着）` 重复 | `ch03:46` 只出现一次 |
| 6 | `ch05 four.md:10` | 「徒手夺剑反杀**两人**」 | `ch05:298` `Had Nick just killed three men?`（挟持者二人 + Lucien） |
| 7 | `ch02 one.md:49` | 前半「不知所措」、后半「一样健谈」自相矛盾 | `ch02:28,34` Bertie 是理直气壮地争辩 |
| 8 | `ch07 six.md:12` | 「心理上的『跳跃尝试』」 | ch07 无跳跃场景，`Jump!` 在 ch08 `text/ch08_seven.txt:385–421`；ch07 的转折是 `:447` `To leave this time, they'd have to steal time from humans.` |
| 9 | `ch07 six.md:63` | 「**两个**对半短语」 | 引语从第二个对半短语起截（`ch07:311` `Half-human, half-monster.` 在引语外） |
| 10 | `ch06 five.md:100` | 词汇 `hands on her knees` 例句只截了段首句，不含该短语 | `ch06:382` 短语在同段下一句 |

**子代理报为假红、我复核后不采纳的 2 条**：
- `ch01 prologue.md:96` `expectant` 例句把原文逗号改成句号（`ch01:67`）—— 截句排版，保留。
- `ch07 six.md:65`「接在 Aaron 说她 new-car smell 之后 / 她没有反驳，只是先承认自己不懂」—— **原文 `ch07:310` 正是 `‘And you . . . you stink of new-car smell,’ Aaron said.`，紧接着 `:311-313` 就是自我描述，子代理判错，此处原文正确不动。**

### d3. ch09–ch17（子代理 86eaffc5）— 阻断型 11 / 提示型 11

| # | md | 缺陷 | 原文证据 |
| --- | --- | --- | --- |
| 1 | `ch10 nine.md:13` | 「Aaron 的家族因此在人类里开了**早餐店**」 | `breakfast shop/bakery/greengrocer/teashop` 全目录 **0 命中**；`breakfast` 的命中全是 `ch11:133/:142` 的 breakfast table |
| 2 | `ch10 nine.md:13` | 「Victor 的手腕…此后二十年他『一次也没回过**牛津**』」 | `Victor` 仅 `ch10:553` 一句；`Oxford` 全书仅 `ch12:436` `His accent was Oxford.`。美人鱼纹身本身是真的（`ch10:466`、`ch06:376`），但那是 Holland House 花园里死去的年轻 Oliver，Joan 还没来得及开口门就被冷风撞开（`ch10:478`） |
| 3 | `ch10 nine.md:33` | 「证据是**他的**家族昨晚刚被灭门」 | `ch10:43` `Aaron's own family had shown her that`；被灭门的是 `ch10:325` 的 Hunts＝Joan 家族 |
| 4 | `ch10 nine.md:43` | 「Aaron 开着早餐店」 | 同 #1 |
| 5 | `ch11 ten.md:25` | 「本章后面会以完全不同的力度回来——抓住手腕…这双手既摸过头发，也握过刀」 | `ch11_ten.txt` 全文 `wrist` **0 命中**；真实场景在 `ch14:13`（Nick 双手扣住 Joan 双腕）+ `ch14:163`（掏出刀） |
| 6 | `ch12 eleven.md:45` | 「Aaron 现身换装，却被 **Joan** 评成『剪裁不对』」 | `ch12:241` `‘The cut was wrong.’ The voice was Aaron's.` ——是 Aaron 评 Joan 的 T 恤，Joan 只问了「哪里不对」 |
| 7 | `ch12 eleven.md:53` | 「『认出族裔』是 **Oliver 的权力**，不是 Liu 的」 | `ch12:550` `Most monsters are recorded in the Liu family records` + `:553` `the Liu family power. Perfect memory.` |
| 8 | `ch14 thirteen.md:10` | 「本章结束时，两人仍然互相握着手」 | `ch14:181` `Nick's hand tightened for a moment over Joan's wrists. Then he released her, slowly. He stood, knife ready` |
| 9 | `ch14 thirteen.md:25` | 「前一章 **Aaron 抓住她手腕**」 | `ch13_twelve.txt` 全文 `wrist` **0 命中**；Aaron 在该章只有 `ch13:84` `Aaron took Joan's elbow` |
| 10 | `ch15 fourteen.md:43` | 「她的对手 Aaron **马上**用 blasphemy 回击」 | `ch15:112` Aaron 说 blasphemy **在前**，`:115` Ruth 的 `How's that for blasphemy?` 是回应 |
| 11 | `ch16 fifteen.md:65` | 「Aaron 全程保持 careless 的姿态，**一个字都没有反驳**」 | `ch16:508-509` `‘Our new heir?’ … ‘I had no idea the pool was so shallow.’` |
| 12 | `ch16 fifteen.md:73` | 凭空造词「**Tomcat**」 | `grep -rn Tomcat text/` **0 命中**；推柜壁的是 Tom（`ch16:574/:577`）。**我在子代理回报前已独立扫出并修掉**，子代理独立复现了同一条 |

提示型 11 条（全部已改）：`ch09 eight.md:55`「上一章」实为同章 · `ch10 nine.md:63`「上一章」错＋`resistance`(`ch10:565`) 与 `it corrects itself`(`ch10:547`) 顺序颠倒 · `ch11 ten.md:65`「Aaron 自己打翻茶杯」实为放下杯子、手微抖(`ch11:301`) · `ch12 eleven.md:65` 后续情节不存在 · `ch13 twelve.md:65`「章鱼状纹章」实为 chimera（`ch13:172` 狮子头鹰爪、`ch12:712`） · `ch14 thirteen.md:45` `The humans they stole from.` 是 Nick 自己抛出(`ch14:76`)，非对 Joan 质疑的回答 · `ch14 thirteen.md:65` 两处 new Nick(`ch14:118/:139`) 都是叙述者 · `ch17 sixteen.md:23`+`:126`「墨水没有干透／墨迹未干」虚构（全章无 wet/dry），总结里重复一次 · `ch17 sixteen.md:53`「先用 `a while` 铺垫」实为 `somewhere`(`ch17:230`)，引错词会削弱 somewhere→somewhen 双关 · `ch17 sixteen.md:73`「Joan 自己也不知道」与 `ch17:487` `I did that, she thought. And I did this.` 矛盾 · `ch17 sixteen.md:13`「力量**第一次**自己跑出来」实为第二次（金链那次在 `ch13:148`）。

**子代理主动撤回的假红 1 条**：`ch15 fourteen.md:104`「Ying Liu hadn't been the first person interested in the necklace.」它一度判为查无，复核命中 `ch15:148`，撤回并提醒不要改。**这正是「自省不构成防线、真正的防线是回查动作」（`docs/新书启动模板.md:707-710`）的现场演示。**

**子代理判为可争议/不报 4 条**（我认同）：`ch12 eleven.md:12/:121`「睡衣上的争吵」实为早餐桌旁 · `ch15 fourteen.md:33`「Aaron 家的生活守则」是 Joan 内心概括且 md 已用「或」限定 · `ch16 fifteen.md:10`「河里捡来的假 chop」「十万年前的雪」对应 `ch16:190`/`:590` 属合理概括 · `ch10 nine.md:10` 是导航段意译式概述、不冒充逐字引语（但那句本身**是编造的**，已由我在 e 步独立修掉）。

### d 步机械子项顺带抓到的阻断型

| md | 缺陷 | 证据 |
| --- | --- | --- |
| `ch22 twenty-one.md:73` | 分析层写 `before he could protest`——既是英文改写冒充逐字，又是主语错配 | `text/ch22_twenty_one.txt:433` `‘I know,’ he said before Joan could protest.` |

---

## e. 总览层事实核对

### e1. 自建覆盖脚本（补门禁盲区）

主脚本 `verify_overview_quotes.py` 在本书只验了 `00_金句精选.md` 的 25 条；`00_概述.md` 与 `00_情感节点.md` 因引语写在 `> ` 行而**一条未验**（⑭ 报「➖ 无引语行」）。

自建 `.tmp_spot/e_overview_qcheck.py` 补齐：
- 解析 `^> ` 引语行 + `00_金句精选.md` 的 `① ` 编号行（排除「呼应关系」里的纯中文引导句）；
- 比对端 **import `scripts/verify_quotes.py` 复用其 `flat_alpha()` 与 `epub_flat_text()`**（不自写展平口径）；
- 三档判据：`✅ 标注章逐字` / `⚠️ 标注与实章不符` / `❌ 全书查无`；非 ✅ 一律进待人判清单。

覆盖 **概述 35 + 情感节点 27 + 金句 61 = 123 条**，干净书 123/123 全绿、待人判 0。

**投毒自证**（`docs/新书启动模板.md:710`「大面积同类报警先读行再改」）：向 `/tmp/poison` 注入 3 处已知缺陷（概述 ch01→ch09 章号错、凭空引语、金句 ① ch01→ch05 章号错）⇒ **3/3 全抓**。

> 投毒过程中先踩了一个**我自己检查器的假阴性**：旧判据只在「能在标注章找到」时升级为 ✅，找不到时退回「全书命中」也判 ✅ ⇒ 章号标错放行。修正为三档后重跑，投毒 3/3、干净书 0。

### e2. 内容缺陷（全部已改）

| # | 位置 | 缺陷 | 证据 |
| --- | --- | --- | --- |
| 1 | `00_概述.md:92` | 「Ruth **死在窗口**」 | `ch06:355` `She was gone.`；`ch25:76` 起仍在场 |
| 2 | `00_情感节点.md:19` | 同上 | 同上 |
| 3 | `00_金句精选.md:126` | 「表姐死在窗口」 | 同上 |
| 4 | `ch06 five.md:10/:11` | 「Gran 与 Ruth **相继死**在眼前」 | 同上 |
| 5 | `00_概述.md:10` | 开场场景错：写「**十六岁那年**」与动作链倒置；且写 Mr Solt 想买花却是现成花店 | `ch02:46` 只有 ch02 写十六岁；原文 `There hasn't been a florist here for years.`，动作链是「撑住→被推开→才抓住肩膀」 |
| 6 | `00_概述.md:36` | **凭空中文台词**「你要习惯一群怪物当你在的社会」 | `grep -iE "get used\|used to\|society"` 在 ch10 与全库**零命中**；真正依据只有 `ch10:115` `A culture.` |
| 7 | `ch10 nine.md:10` | 同上（同一处编造的第二份拷贝），同句「一门生意」也是编造的（`business` 在 ch10 零命中） | 同上 |
| 8 | `00_概述.md:41` | 「Court 的 gala 只开两晚，一夜几百年」 | `ch15:436` `Last time the gate opened was centuries ago. And it won’t open again for another century.` ⇒ **门**百年一开，**gala** 两晚后举行，两件事不能混 |
| 9 | `00_概述.md:49` | 「**越过**完全冻结的泰晤士河，**走下通往地窖的阶梯**」 | `cellar\|basement\|underground` 在 ch17/18/19 全零命中；冻结的河是在套间**望见**（`ch18:31/:67`） |
| 10 | `00_概述.md:56` | 「那本岛的禁令」表述崩坏 | `ch03:187` |
| 11 | `00_金句精选.md:223` | 「ch17，**王宫地窖前**」 | 地窖不存在；实际是 Whitehall 宫内守卫换班前（`ch17:220-222`） |
| 12 | `00_金句精选.md:99` | 「ch18 **他重复这句时**」 | `Real monsters look like me and you` 只在 `ch01:25` 出现一次，ch18 从未重复 |
| 13 | `00_金句精选.md` ⑨⑯⑰⑱⑲ | 5 条 `**中文**` 只译了引语前半段 | 逐条补全到引语末尾 |
| 14 | `00_金句精选.md:139` | 「四种答案互不相同」 | 该 bullet 只列了 Gran / Nick / Ruth 三条 |
| 15 | `00_情感节点.md:55` | `## 节点6：真相（ch20–ch22）` 内含一条 ch19 引语 | 改为 `（ch19–ch22）` |

### e3. 已核验**通过**的关键断言（抽样，附证据）

- Dorothy Hunt ＝ Gran 本名（`ch10:451`）；Ruth 是表姐（`ch02:46/:61`）；Nick 家「Eight of us in a two-bedroom flat」；Ravencroft Market（`ch10:208` + `ch11:91/103/106`）；Tom 是前 Court Guard（`ch19:394`）；Aaron 是 Edmund 最小的儿子且本应继位却被剔出（`ch12:193`）；Marie Oliver（`ch06:304`）；邮递员连提包消失（`ch10:592` `vanished, bag and all`）；Nick 抢项链（`ch14:124-157`）；吊坠是钥匙（`ch12:745` `‘You have a key.’`）；铭文不属于十二家族（`ch13:181`）；**1922 次重启**（`ch21:418`）；Holland House 一夜被炸二十二次（`ch25:178/:334`）——概述「二十二次」与主题三「一千九百二十二次」两处都对。
- **「吹茶杯抹平茶面」属实**（`ch12:85` `She leaned over and blew across her mug. The tea in it shivered and then stilled.`）；**「地下室里两个人贴身扭打」属实**（`ch23:52` `This was the basement of Holland House.`）。
- 跨书污染自检：`Solt` / `Bao Bao` / `Mtawali` / `Liu stories` / `King's Reach` / `vanessa len` 全书唯一；`Elsie` / `Bertie` / `Conrad` / `Ying` / `Rose` 虽见于他书但均为常见人名、且本书语境自洽（非污染证据）。md 中 `\b[A-Z][a-z]{2,12}\b` 候选 281 个，`text/` 查无仅 2 个（`Prologue` 章名、`Tomcat` epub 元数据）。

---

## 工具盲区（本轮审查最有价值的产出）

| # | 盲区 | 表现 | 建议 |
| --- | --- | --- | --- |
| 1 | **中文引号台词零覆盖** | `ch10 nine.md:10` 与 `00_概述.md:36` 的凭空中文台词 `「你要习惯一群怪物当你在的社会」`，所有英文引语门禁（①②⑤⑥⑭⑮）**结构上无法覆盖** | 对 md 里的 `「…」` 与纯中文 `"…"` 片段做抽样回查，或加一条「中文台词须带原文定位」的门禁 |
| 2 | **`verify_overview_quotes` 不解析 `> ` 形态，且不验 (chNN) 标注** | 概述 / 情感节点两篇一条未验；金句集 25/25 ✅ 但**章号全错也照样 ✅** | 扩 `> ` 行解析 + 把标注章纳入判定 |
| 3 | **散文断言行不在任何门禁内** | 「六族 vs 十一个家族」「两天前 vs 两年前」「他哥哥 vs 表兄」「早餐店」「牛津」「Tomcat」全部漏过 | 门禁之外保留 d 步语义二审（本轮执行方式：三个子代理分章 + 我逐条回查原文） |
| 4 | **中文散文里的英文专名零覆盖** | `check_anchor` 只查英文词形，`Tomcat` 藏在中文句子里照样放行 | 补一步专名扫描：对 md 抽 `\b[A-Z][a-z]{2,12}\b` 候选，逐个回 `text/` 查（本轮对 ch09–ch17 跑：候选 157，查无 1＝`Tomcat`） |

---

## 复验

整改后 `bash scripts/gate.sh` **EXIT=0**，全部 lane 归零：

```
① verify_quotes        172/172（100%）；完全干净文件 26/26；--full 整串取证 0
② check_vocab          词条行 656 ｜ --- FAIL (0) ---
③ check_entities       0 个文件存在未知实体
④ corruption_scan     FAIL 0 处 ｜ 报告 0 处
⑤ sweep_full           ✅ 144 ｜ ⚠️ 跨章 0 ｜ 🔶 跨标签拼接 3（合规 … 省略）｜ ❌ 0
⑥ check_short_quotes   ✅ 3 ｜ ⚠️ 0 ｜ ❌ 0
⑦ 逐章归属              25 章全部 X/X in 本章 text
⑧ 块覆盖对账            ✅ 25 个文件，每块都进了 verify_quotes 校验
⑨ 导航/总结层英文核对    ❌ 0 ｜ ⚠️ 0
⑩ sweep_analysis_inline ✅ 逐字 859 ｜ ⚠️ 0 ｜ 🟠 0 ｜ 🟡 0 ｜ ❌ 0
⑪ audit_structure      ❌ 结构缺陷 0 ｜ ⚠️ 提示 0 ｜ 🔀 0
⑫ check_anchor         凭空造词 0 ｜ 松散关键词 0
⑬ 空段扫描              0 处
⑭ verify_overview_quotes 00_金句精选.md 25/25 ✅
⑮ check_overview_full  ❌ 查无 0 ｜ 标注与实章不符 0
```

外加本次自建：`.tmp_spot/e_overview_qcheck.py` **123 条全绿、待人判 0**；
`check_struct_indep.py` / `check_xref_indep.py` / `check_analysis_indep.py` 三个独立实现全绿（`分析层英文片段 164 条 ✅ 全部逐字命中`）。

## 缺陷总计

| 类别 | 阻断型 | 提示型 | 假红（不计入） |
| --- | --- | --- | --- |
| d1 ch18–ch25 | 4 | 9 | 4 |
| d2 ch01–ch08 | 5 | 5 | 2 |
| d3 ch09–ch17 | 11 | 11 | 5 |
| d 步机械子项 | 1 | — | — |
| e 步总览层 | 15 | — | 0 |
| **合计** | **36** | **25** | **11** |

36 条阻断型全部改完并回查原文；11 条假红（其中 1 条是子代理自己撤回的）保持原样并记录理由。

## 同会话审查的已知局限（`AGENTS.md:242` 要求仅在结论部分标注）

1. **作者即审查者**：精读 md 与原文由同一会话写出，「我当初为什么会这么写」的意图无法与错误分离——d 步能证明「这句与原文不符」，不能证明「这句的理解是作者真正想要的」。
2. **d 步用了三个子代理，但它们与我在同一会话上下文里**（subagent_fork 继承本会话已完成的轮次），不是完全冷启动的第三方；我用「子代理结论必须逐条回查原文」来对冲，但无法排除同源偏差。
3. **e 步的中文散文断言共 356 条 `"…"` + 51 条 `「…」` 片段**：本轮按「高风险模式定向扫」（时间词、计数词、亲属称谓、极值断言、专名、章号区间）覆盖，**不是逐条穷举**。已核验通过的是抽样 + 全部 `chNN` 标注引语；散文里可能仍有未被定向模式命中的失实。
4. **独立实现只验过 1 本书**（`docs/新书启动模板.md:703` 要求写清）：`check_struct_indep.py` / `check_xref_indep.py` / `check_analysis_indep.py` 的零报警，在这本书上不能外推为「对任何书都灵」。
5. **同会话内 e 步自建脚本 `.tmp_spot/e_overview_qcheck.py` 只用于本书**，未纳入 `scripts/`，也未在其他书身上验证过；其投毒自证只覆盖了 3 类已知缺陷形态。