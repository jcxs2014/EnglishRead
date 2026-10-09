# 五步审查：Mazywood（Tananarive Due）

- 审查方与执行方：**同一会话**（用户 2026-10-09 发起，要求「输出缺陷清单并完成整改」）
- 对象：`notes/books/mystery-thriller/mazywood-by-tananarive-due/`（40 章 + 总览三篇 = 43 md，text/ 40 件，完整 lane）
- 整改 commit：`c25913aa5`（e 步总览 48 处）· `8dd5d8cbc`（批 A/B 29）· `623edf748`（批 C/D 24）· `d43d7b9f9`（批 E 16）· `e4c9de0e0`（批 F 9）· `1ef938ca8`（批 G 7）
- 落盘合计：**阻断型 133 处**（章节侧 85 ＋ 总览侧 48），每批后 `corruption_scan` FAIL 0
- 收口复跑（`.memory/raw-gates/mazywood-by-tananarive-due/2026-10-09-review-closeout.txt`）：gate.sh **正门结论 0 条阻断型** · verify_quotes **299/299（100%，干净 41/41）** · 逐章归属 **275/275 全部命中本章** · sweep_full **本章命中 275／跨章 0／拼接 0／查无 0** · vocab **702 词条 FAIL 0 / WARN 39** · entities 0 · corruption FAIL 0 · check_anchor 凭空 0／松散 0 · audit_structure 缺陷 0／提示 0／🔀 0 · check_quote_blocks ✅ · 空段扫描 0 · 总览引语 **54/54** · check_overview_full 跨章多重 0／H1 错配 0 · check_xref_chapter 0／0／0

## a. 第 3 条门禁全量重跑（不采信写作期贴过的数字）

本机逐条重跑并复现：verify_quotes 299/299（含 `--full` 整串取证 0）、check_vocab FAIL 0（WARN 39 全部为「基础档疑含超纲词」长度 ≥9 启发式，**提示型**）、check_entities 0 未知实体、corruption_scan FAIL 0、sweep_full 275/275 零跨章零拼接、check_short_quotes 短引语 0 条（主门禁已全覆盖）。**0 阻断 / 39 提示（接受）/ 0 假红。**

## b. 逐章归属（换检查路径：单文件模式 → `--book-dir` 全书模式 + sweep_full 整串口径）

40 个 md 全部 X/X in 本章 text（8/8、7/7、6/6），零跨章搬句。⚠️ 本步的「换实现」= 不复用写作期的逐章 grep，而是同时跑 `check_chapter_quotes`（对 text/）与 `sweep_full`（整串 flat 对 epub），后者专抓前 60 字符指纹失明的中段篡改——两把尺子结果一致。

## c. 结构扫描（第二实现 + audit_structure 双跑）

audit_structure：结构缺陷 0／提示 0／🔀 映射不一致 0；主流子项自推断为「中文理解·为什么这样写·关键词·读者视角提示」，引语块众数 7（全部落在 3–8 配额内）。check_quote_blocks：275 块前缀完整、编号连续无撞车、无孤儿分析、无自查泄漏。check_block_keywords：阻断 0／提示 0。空段扫描 0。**本步 0 缺陷。**

## d. 语义二审（7 个只读子代理分组并行：ch01–05 / 06–12 / 13–18 / 19–24 / 25–30 / 31–35 / 36–40）

七组报告合计**阻断型 78 条**（17＋10＋14＋9＋7＋10＋11），另有引语截短与词表例句补全若干；落盘 **85 处**（差额＝同一报警在章内的联动改写，以及第 9 条 a／a2 要求的引语·例句补全）。

**审查过程自身的三条纪律在本步的落地**：
1. **报警先读行复核**——三条子代理报警经回源推翻（撤案，未改内容）：
   - ch01:76「女王行礼」——text/ch01:101 确有该动作，报警前提不成立；
   - ch03:76「ch01 后院幕布」——text/ch01:181/193/211 有 sheet/curtain，跨章指认正确；
   - ch17:52「上一章 Imani 掀开苫布」——text/ch16:67 确有此事，相对章号指对。
   另推翻组 4 存疑项 #21 的前提（ch01 md 写的是七岁，并非 15 岁）。
2. **一次改 10+ 处同类前先改 1 条验证判据**——每批脚本 dry-run 断言「锚点命中数 == 1」，命中 0 即整批不写盘（首批因把锚点写成直引号而整批 MISS，本库 md 正文用**弯引号**，改按文件真实字节后通过）。
3. **修完先 commit 再投毒**——每批落盘后 `corruption_scan` 复跑（FAIL 0），再 pathspec 提交。

**⚠️ 本轮一条新的过程教训（要记进工具坑）**：后台子代理的 `.output` 文件全部 0 B，旧会话 transcript 只剩聚合数字，导致批 F 三条报警（ch31:30／ch32:88／ch34:64）的**原始理由丢失**。处置＝不凭记忆补理由，改为**自己从 text/ 重新取证定性**后再决定改法；这一条比「报告丢失」更值得记——丢了材料仍可重取，凭印象重述会造假。

## e. 总览层事实核对（引语池 + 说话人窗口 + 数字断言逐条回源）

三篇总览（00_概述 / 00_金句精选 / 00_情感节点）**落盘整改 48 处**。引语层由 `verify_overview_quotes`（54/54）与 `check_overview_full`（跨章多重 0／H1 错配 0）覆盖，**但行内英文与中文事件断言无门禁**，全部按第 9 条 d 逐条 grep 全书：
- **说话人与归属**：警告许愿规矩的人＝同学 Priscilla Stephens（text/ch01:34、ch30:215），三篇都写成「大人」→ 订正；
- **跨线年份推算**（本书红线：只认章节抬头的时间标注，不换算年份）：「半个世纪之后」→「切回今天线」；
- **原文未写的通道**：「用一个眼神答了『是』」→「答了那个不必说出口的字」（text/ch05:332-335 只写不必说出口，随后独立一行 Yes.）；
- **物体数量**：「一箱完好的水」→「十几瓶完好」（text/ch37:158 half-empty package… at least a dozen… intact）；
- **时序**：枪响在女儿反复喊停**之后**（text/ch38:295/332/371 → :380）；
- **结局与伤势**：Tasha 的脚伤到露骨、只是没被咬（text/ch35:263、ch40:25），「毫发未失」撤回；
- **建造年代**：Mazywood 兴建早于 1943（text/ch24:418），「八年后建起」撤回；
- 明细见下方「批 O1／批 O2」。

## 缺陷簇（按出现频次排序，全部为阻断型）

| 簇 | 典型形态 | 落盘处数（约） |
|---|---|---|
| 1. 章内时序写反 | 「在前两段已经铺完」实为本段之后；「先答 A 再问 B」次序颠倒 | 14 |
| 2. 相对章号指错 | 「上一章／下一章／前一章」指向梦境章、对方 POV 章或本章自己的后文 | 12 |
| 3. 无出处断言（词形全书查无） | Gram／Lafayette Players／抽烟／faith／seven years／漂亮小戏子 | 8 |
| 4. 长幼与人物关系反转 | Imani 与 Sharise 姐妹身份对调（Sharise 是姐姐） | 5 |
| 5. 说话人／主语错配 | 「她的疤」实为他的；「与 Johnny 一侧的并置」实为女儿们一侧 | 6 |
| 6. 时段与场景断言 | 「夜里」追迹实为一早／上午；客厅实为餐厅 | 5 |
| 7. 计数断言失准 | 三项→四项、两次→一次、三个 while→两个 while 与两处分词、一句→两遍 | 7 |
| 8. 悬置项被裁决 | ch27 把 not his ghost or hallucination 当成全书对幻象的定性 | 2 |
| 9. 引语截短（同段连续后半未取） | ch29 原句 5／ch30 原句 3 补全 | 2 |
| 10. 词表例句截掉句首 | ch05 三例（hypnotized／cooing／blanket） | 3 |
| 11. 唯一性／归属断言 | 「唯一一次触及上帝」（本章另有三处）；cassette 的购买者 | 2 |
| 12. 总览层事实与年份换算 | 见 e 步八类 | 48（总览侧） |

## 提示型与假红型（只记不改 / 未改工具）

- **提示型（接受，不改）**：check_vocab WARN 39（≥9 字符启发式）；`sweep_analysis_inline` ⚠️ 跨章 6 条——逐条回源**归属全部正确**（ch04:30 已明写 ch05、ch24:16「上一章」＝ch23、ch26:64 已明写 ch28、ch34:66「此前章节」＝ch19、ch40:16「上一章」＝ch39、ch34:64 hot comb 旧事＝ch15:178），属章标题式合法交叉引用。
- **假红型**：本轮 gate.sh 18 项未出现假红报警，**未修改任何门禁脚本**；一次性整改脚本全部存于 gitignored 的 `scripts/attic/`（断言式行级替换，不进门禁、不作结论依据）。

## 逐条清单（133 处，按批次；依据列给出取证出处）

> 表内为**主要归入该簇**的处数；一条报警常联动章内多处改写，故各行之和 ≠ 章节侧总数 85。

### 批 A/B（ch01–ch12，29 处）

- **ch01 the wishing pool.md:24** text/ch01:22 "during her seven years of life"
  - 旧：因为和她七生里跟着家人巡演走过的那些城市相比
  - 新：因为和她七年人生里跟着家人巡演走过的那些城市相比
- **ch01 the wishing pool.md:54** 双胞胎/十岁差/accident 在 text/ch01:128，不是「下一段」
  - 旧：下一段才交代双胞胎姐姐、十岁的年龄差
  - 新：本章后半才交代双胞胎姐姐、十岁的年龄差
- **ch01 the wishing pool.md:112** text/ch01:37 两次放弃：一次家务、一次天黑
  - 旧：而本章开头她正因为"太黑了"放弃过两次进林
  - 新：而本章开头她两次寻池未成，一次是因为该去做家务、一次是因为天要黑了
- **ch02 the first screen test.md:16** text/ch01:259 她答了"don't belong to nobody… found him on the road"
  - 旧：Daddy 压低嗓门追问这只狗是谁的、从哪儿来的，她没有答出来历
  - 新：Daddy 压低嗓门追问这只狗是谁的、从哪儿来的，她只答不归任何人、是路上捡的
- **ch02 the first screen test.md:28** text/ch02:167 灯后有人低声惊呼
  - 旧：于是上一章那种“狗听得懂人”的奇迹在本章被降级成日常背景，没人再觉得奇怪。
  - 新：上一章那种“狗听得懂人”的奇迹在本章并没有被当成日常——摄影机后就有人低声惊呼（How’s that damn dog know what ‘action’ means?），只有 Mazelle 觉得理所当然。
- **ch02 the first screen test.md:64** 儿童误读在 text/ch02:88，被析句在 :106，顺序相反
  - 旧：和紧接其后的儿童误读（Whose feet
  - 新：和本章前段那处儿童误读（Whose feet
- **ch03 the velvet curtain.md:14** "Gram" 在 text/ch03 出现 0 次
  - 旧：被提及者：Mr. Lorenzo、Gram、Sunshine Sammy
  - 新：被提及者：Mr. Lorenzo、Sunshine Sammy
- **ch04 we love you mazy.md:14** "Lafayette Players" 在 text/ch04 出现 0 次
  - 旧：Al Jolson 与 The Jazz Singer、Lafayette Players
  - 新：Al Jolson 与 The Jazz Singer
- **ch04 we love you mazy.md:30** 「比上周更多」是本章自己的措辞；ch05 的场景是布景外候着的家长们（text/ch05:28）
  - 旧：与 ch05 片场外那群「比上周更多」的家长形成同一套成名日常
  - 新：与 ch05 那群候在布景外的家长（the cast and the mothers as they huddled near him outside of the set）形成同一套成名日常
- **ch04 we love you mazy.md:102** 全章是办公室的一天，无夜（text/ch04 末段仍在门厅）
  - 旧：这一夜之后，她的名字、口音、头发与裙子都已不再归她所有
  - 新：这一天之后，她的名字、口音、头发与裙子都已不再归她所有
- **ch05 scout worst day.md:40** “My real name is Mazelle” 在 text/ch05:109，位于本块引语（:112）之前一段
  - 旧：作者把这场反抗写得极小：一句“My real name is Mazelle”，没有动作、没有哭闹。
  - 新：作者把这场反抗写得极小：只有块前一行那句 “My real name is Mazelle,” she heard herself say.，没有动作、没有哭闹。
- **ch05 scout worst day.md:66** 这一夜的余生交代在 ch05 自己的末尾几段（text/ch05:465–471）
  - 旧：本章她不但掀开了，还答了话；下一章起她余生都要在这一夜上面过日子。
  - 新：本章她不但掀开了，还答了话；而本章最后几段已经把这夜的账一路记到了她的余生。
- **ch05 scout worst day.md:96** 
  - 旧：也许是全新的，也也许和她当年在 Gracetown
  - 新：也许是全新的，也许和她当年在 Gracetown
- **ch05 scout worst day.md:122** 词表三条例句被截掉句首
  - 旧：| In a once-upon-a-time voice that hypnotized them all, Mr. |
  - 新：| In a once-upon-a-time voice that hypnotized them all, Mr. Sharpe gathered the kids to tell them the story they would act out. |
- **ch05 scout worst day.md:125** 
  - 旧：| Wu, who held Danny in the shade of an awning, cooing
  - 新：| Everyone flocked to them except Mrs. Wu, who held Danny in the shade of an awning, cooing
- **ch05 scout worst day.md:137** 
  - 旧：| blanket | 毯子 | Sharpe held up a small blanket. |
  - 新：| blanket | 毯子 | Mr. Sharpe held up a small blanket. |
- **ch06 discovered your grandmother.md:14** Johnny 是编导演，非童星；童星是 Mazelle（text/ch06:37 卖出第一个剧本／:291 Misery Swamp 出自学业之后）
  - 旧：偏头痛遗传自母亲，童星出身，Frat House Haunting 四部的编导演
  - 新：偏头痛遗传自母亲，Frat House Haunting 四部的编导演
- **ch06 discovered your grandmother.md:30** his mother = Sadie，ch01–ch05 那个女孩是他祖母（text/ch06:321 his grandmother’s name／ch07:19 Sadie）
  - 旧：下一段就会交代 his mother——他遗传的是那个女人，也就是 ch01–ch05 里那个女孩。
  - 新：下一段就会交代 his mother——他遗传自母亲这一边；而 ch01–ch05 里那个女孩是他母亲的母亲，也就是他的祖母。
- **ch06 discovered your grandmother.md:100** 她争的是名不是姓（text/ch05:109 My real name is Mazelle. Not Mazy.）
  - 旧：而且她当着大人说过自己不姓 Mazy
  - 新：而且她当着大人说过 Mazy 只是艺名、她叫 Mazelle
- **ch07 a calm eye.md:11** Florida 是二十年前母亲车祸的联想（text/ch07:16），当天是从 LDR 的会面驾车回家
  - 旧：Johnny 从佛罗里达返程，当天傍晚回到 Baldwin Hills 的家中
  - 新：Johnny 从 LDR 那场会面驾车回家（途中闪回的是二十年前 Florida Highway Patrol 通知母亲车祸），当天傍晚回到 Baldwin Hills 的家中
- **ch07 a calm eye.md:76** text/ch07:136 不知情的是两个女儿
  - 旧：三个人的不知情保护了一个人
  - 新：两个女儿的不知情保护了一个人
- **ch07 a calm eye.md:90** 运动用品店的插叙在本章（text/ch07:164），且不是五金店
  - 旧：紧接着下一章轮到女儿们在五金店里谈论圣诞节
  - 新：而本章后文已经先给过女儿们的版本——她们吵着要滑雪服，Sharise 开车带 Imani 去了运动用品店
- **ch08 evil genie.md:28** 全大写四项（text/ch08:16 SNOWBOARD. HELMET. GOGGLES. SKI MASK.）
  - 旧：全大写的三项像喊出来的
  - 新：全大写的四项像喊出来的
- **ch08 evil genie.md:76** 抽烟在 ch08 查无（text/ch08:112 只把 headaches 列为「他们不对劲」的证据之一）
  - 旧：（红眼是孕吐与失眠、"头痛"是抽烟与血压、行程是家族史）
  - 新：（红眼是孕吐与失眠、"头痛"是她数给父母的另一桩毛病、行程另有隐情）
- **ch10 running in white.md:66** ch09 是现实中的模型（text/ch09:162），ch10 才是梦
  - 旧：本书让同一件衣服在两个梦里分别吓到两个人
  - 新：本书让同一件衣服在现实与梦境里分别吓到两个人
- **ch11 left behind.md:11** 「几分钟车程」在 ch11 查无（text/ch09:16 私路离镇十五分钟、text/ch11:94 离 McCloud 二十分钟）
  - 旧：山脚小镇公路旁的 Gas N Go 便利店与它的停车场，离私路入口只有几分钟车程
  - 新：山脚小镇公路旁的 Gas N Go 便利店与它的停车场；上山那条私路仍在更北的地方
- **ch11 left behind.md:78** 周五是 ch09、周六是 ch11；上一章 ch10 是梦
  - 旧：把这条信息与上一章对上，是读者按题注（周五与周六）自己做的推断
  - 新：把这条信息与 ch09 对上，是读者按题注（周五与周六）自己做的推断
- **ch11 left behind.md:88** 本章已答改名者与她为何改（text/ch11:203 She named it after her character）
  - 旧：是全章留下的第一个真正的谜：谁改的名、什么时候改的，本章不答
  - 新：是全章留下的第一个真正的谜：她为什么要为这个角色名改掉自己的名字，本章不答
- **ch12 the white jeep.md:102** 梦在 ch10，上一章是 ch11
  - 旧：这件镶毛边的红袍与上一章梦里坐在门廊台阶上的祖母
  - 新：这件镶毛边的红袍与 ch10 梦里坐在门廊台阶上的祖母

### 批 C/D（ch13–ch24，24 处）

- **ch14 a frozen nightmare.md:52** text/ch14:148 的自圆其说在本章后文；ch15 是 Johnny 屋内线
  - 旧：这个时间差正是下一章她能自圆其说的凭据
  - 新：这个时间差正是本章后文她能自圆其说的凭据
- **ch15 the punishment room.md:30** 袍子的回想在 text/ch13:155（章中），ch14 全章无 robe
  - 旧：上一章末尾 Tasha 才想起 Mazelle 的袍子
  - 新：ch13 章中 Tasha 才想起 Mazelle 的袍子
- **ch15 the punishment room.md:40** 「为何此处是家庭秘密」的疑问在 text/ch13:152
  - 旧：同时替上一章 Tasha 的疑问
  - 新：同时替 ch13 里 Tasha 的疑问
- **ch15 the punishment room.md:64** 事发时 Johnny 十三岁，本章讲述时他六十；具体年数不换算，删数
  - 旧：时态把三十年前的夜里拉回当下
  - 新：时态把当年的那片夜拉回当下
- **ch15 the punishment room.md:76** text/ch15:97 在本段引语内，:100 的追问在其后，全书仅此一处提问
  - 旧：Tasha 在前面问过"first blood"是什么意思，这段就是回答，作者因此
  - 新：Johnny 在本段先说出 drew first blood，Tasha 的追问（What do you mean… ‘first blood’?）紧随本段之后，作者因此
- **ch15 the punishment room.md:100** text/ch15:202 那句禁令就在本块引语内，不在前一章
  - 旧：让成年人第二次以"压低消息"的方式出场，与前一章"别把这事再对别人说"呼应。
  - 新：让成年人第二次以"压低消息"的方式出场——同段里他先被告知 not to repeat his story to anyone else，随后又听到那句 chasin’ 之后的劝告，两道禁令叠在一处。
- **ch16 the meat graveyard.md:16** text/ch15:157/160 疤在 Johnny 自己手臂上
  - 旧：把她的疤与自己那句
  - 新：把他的疤与自己那句
- **ch17 the cure all along.md:28** 惩罚房无窗（text/ch15:52），临终房是有百叶窗的主卧（text/ch17:16/22/95）
  - 旧：同一个 room 在上章还是"惩罚房"，现在成了"临终房"与婚床所在。三个空间名互相覆盖
  - 新：无窗的窄小惩罚房（ch15）与放了病床、有百叶窗的主卧（本章）本是相邻的两间房，却在叙述里被并置成同一层记忆。两个空间名互相覆盖
- **ch17 the cure all along.md:52** text/ch13:37 走廊替 Mazelle 抱不平；ch16 是 Imani 视角无此内容
  - 旧：满足的正是上一章她替 Mazelle 抱的那些不平
  - 新：满足的正是 ch13 走廊上她替 Mazelle 抱的那些不平
- **ch18 the thing under the snow.md:78** 落汽油交代在 text/ch16:46/55，ch17 无汽油
  - 旧：都在赎上一章她落下的那两桶汽油
  - 新：都在赎 ch16 交代她落下的那两桶汽油
- **ch19 the severed hand.md:66** text/ch19:103 早于本块引语（text/ch19:179）已交出"白毛"一句
  - 旧：这是他第一次交出"长相"
  - 新：这一段才补全躯干、口鼻与牙齿——本章稍早他只交出过一句白毛（White fur, like camouflage in the snow）
- **ch20 hunting on their own.md:64** snake/bat 此前只是叙述比喻（ch15:202 snakelike、ch15:31 like a bat’s wings），非 Johnny 的候选
  - 旧：否定排比把 Johnny 此前给过的每个候选答案（fox-thing、bear、snake、bat）逐一划掉
  - 新：否定排比把 Johnny 此前给过的候选答案（mountain lion、bear、fox 或 possum 大小的东西）逐一划掉，而 snake 与 bat 此前只以叙述旧比喻出现过（ch15 写那身子 undulating snakelike、写袍袖 like a bat’s wings），此刻第一次被当成候选
- **ch22 jump for joy.md:40** text/ch22:344 from the dining room
  - 旧：后文他的低音在客厅里唱 Jump for Joy 的新抒情曲
  - 新：后文他的低音从餐厅那边传来，唱 Jump for Joy 的新抒情曲
- **ch22 jump for joy.md:54** text/ch22:61/362/425 单独成行，:133 嵌在段末
  - 旧：在本章单独成行地反复响起（Richard 的得意之后、Lorenzo 出现之后、她笑说"这辈子最好的一天"之后、Sharpe 醉话之后）
  - 新：在本章三次单独成行地响起（Richard 的得意之后、她笑说"这辈子最好的一天"之后、Sharpe 醉话之后），另有一次嵌在段落末尾（…lingering baby face. Be careful what you wish.）
- **ch22 jump for joy.md:12** 
  - 旧：靠单独成行的 Be careful what you wish. 反复回环来缝合
  - 新：靠单独成行三次的 Be careful what you wish. 反复回环来缝合
- **ch22 jump for joy.md:84** text/ch22:407 与 :413 同一句问了两遍
  - 旧：Sharpe 醉着打来，只问了一句"你签了吗"
  - 新：Sharpe 醉着打来，连着两遍问"你签了吗"（“Did you sign it?”…“Just tell me—did you sign it?”）
- **ch22 jump for joy.md:76** text/ch22:94 该句出自叙述对 "Passport to Georgia" 歌词的听感，非 Lorenzo 的推销词（:260–272）
  - 旧：而 Lorenzo 的推销词恰好把这份相认坐实：Negroes fleeing racial violence in the South sang about moving to cities 的处境
  - 新：而把这份相认坐实的是叙述本身——Negroes fleeing racial violence in the South sang about moving to cities 出自她对 "Passport to Georgia" 歌词的听感，不是 Lorenzo 的推销词；其处境
- **ch23 closed eyes.md:60** text/ch23:350 全章 "she hadn’t noticed" 仅此一处；:347 那句在引语块前一段
  - 旧：她说"你醉得不轻，先生"，故意用"先生"去扎他残存的清醒。
  - 新：她说"你醉得不轻，先生"（这句在引语块前一段），故意用"先生"去扎他残存的清醒。
- **ch23 closed eyes.md:60** 
  - 旧：他又靠近了一步——她已经第二次没察觉他在移动——现在他只剩一把椅子的距离。
  - 新：他又靠近了一步——她没察觉他在移动（全章这一处 hadn’t noticed）——现在他只剩一把椅子的距离。
- **ch23 closed eyes.md:64** 
  - 旧：作者的预警技术也在这里：连续两处写她"没察觉"（He’d been moving toward her again and she hadn’t noticed；前文 she felt a practiced tug on her dress’s zipper 之前，叙述已写过她站在椅后 keeping the chair between them），叙述者的眼睛比角色更早看见危险。
  - 新：作者的预警技术也在这里：叙述只写了一次她"没察觉"（He’d been moving toward her again and she hadn’t noticed），而她其实早有位置感——她站在椅后 keeping the chair between them，用椅子隔开两人；她看见了距离，没看见意图。叙述者的眼睛比角色更早把危险摆出来。
- **ch23 closed eyes.md:76** text/ch23:356 结束该段，解拉链在 :371–374，相隔两段；文中无"越过椅背"
  - 旧：声音裂开的那一秒与他的手越过椅背的那一秒被排在同一段里，这就是本章的道德结构。
  - 新：他的承认（His voice cracked.）与随后伸手解她背后拉链的那一段被排在紧邻的两段里，这就是本章的道德结构。
- **ch23 closed eyes.md:100** text/ch23:444/459 车程前半她说过两句；"没说"在广播之后（:468→:471）
  - 旧：也不用 Mazelle 忏悔——她确实一个字没说（She and Sharpe didn’t speak for the rest of the drive.）
  - 新：也不用 Mazelle 忏悔——广播响起之后的后半程她一个字没说（She and Sharpe didn’t speak for the rest of the drive.；此前她只丢给 Sharpe 两句自保的话）
- **ch23 closed eyes.md:141** text/ch23:468 只有一句警告，且为章末前一行
  - 旧：最后把全部判决交给收音机里另一个女人的两句警告。
  - 新：最后把全部判决交给收音机里另一个女人的一句警告。
- **ch24 play it again.md:100** ch24 无"司机在楼下"（text/ch24:136 只写 driver parked 后开门）
  - 旧：没有车（司机在楼下）、没有合约
  - 新：没有一辆能替她离开的车、没有合约

### 批 E（ch25–ch30，16 处）

- **ch26 no happy ending.md:13** text/ch26:118 that morning／text/ch27:311 barely nine thirty
  - 旧：Imani 带着 Sharise 与一支 Winchester 在夜里追 the Beast 的踪迹
  - 新：Imani 带着 Sharise 与一支 Winchester 一早就追进 the Beast 的踪迹
- **ch26 no happy ending.md:132** 
  - 旧：Imani 带着 Sharise 与一支 Winchester 追进夜里 the Beast 的踪迹
  - 新：Imani 带着 Sharise 与一支 Winchester 追进上午的雪光里，一路追着 the Beast 的踪迹
- **ch26 no happy ending.md:14** Sharise 是姐姐：text/ch06:225 十八岁／ch27:458 her older sister／ch35:28 his older daughter
  - 旧：Imani（持枪、执意追踪的姐姐）、Sharise（一路哭泣、主张回去求助的妹妹）
  - 新：Imani（持枪、执意追踪的妹妹）、Sharise（一路哭泣、主张回去求助的姐姐）
- **ch26 no happy ending.md:54** 
  - 旧：本章让被 Imani 视作"只会哭"的妹妹承担了几次关键观察
  - 新：本章让被 Imani 视作"只会哭"的姐姐承担了几次关键观察
- **ch26 no happy ending.md:64** 
  - 旧：作者让她把这套推理讲给妹妹听
  - 新：作者让她把这套推理讲给姐姐听
- **ch26 no happy ending.md:64** "faith" 在 text/ch28:329，ch26 全章无该词
  - 旧：（呼应章末 Imani 靠"faith"这个名字撑着）
  - 新：（呼应 ch28 里那句 It was about faith, like the way she knew Mom was still alive）
- **ch27 tree well.md:14** text/ch27:43 那句修饰的是「生前最后一次与真的叔叔说话」，不是给幻象定性；悬置项不裁决
  - 旧：只在 Johnny 脑内／幻象里出声，本章文本明确写 "not his ghost or hallucination or whatever the fuck"
  - 新：本章起在 Johnny 身边出声；原文那句 not his ghost or hallucination or whatever the fuck 修饰的是他与「真的」叔叔最后一次交谈，并未裁定此后这些是幻象——全书悬置项，不裁决
- **ch28 miracle tree.md:90** text/ch28:404 (A Beasthole, technically.) 是叙述插注；Imani 十三岁（ch06:225），text/ch28:122 只写别人猜她 eleven or twelve
  - 旧：（本章自造词、作者让 12 岁的 Imani 造出来）
  - 新：（本章自造词，出自叙述者的插注而非 Imani 的台词；Imani 十三岁，只是常被人猜成 eleven or twelve）
- **ch28 miracle tree.md:98** 关键词须在块内引语（text/ch28:461）；in your head 出自下一段 Sharise 的问话（:464）
  - 旧：**关键词**：clear and calm、smiling、in your head
  - 新：**关键词**：clear and calm、smiling、heard her voice
- **ch28 miracle tree.md:100** 
  - 旧：整个 Q&A 的节奏是「姐姐的确认+妹妹的温柔」
  - 新：整个 Q&A 的节奏是「姐姐的轻声追问＋妹妹的点头」
- **ch29 the waving hand.md:100** 药品递进（Tylenol :314／Aspirin :317／blood thinner :371）都在本块（:311）之后
  - 旧：的层层递进（他要的是"抗凝"，指向心脏）在前两段已经铺完
  - 新：的层层递进（他要的是"抗凝"，指向心脏）要到本段之后才逐层铺开
- **ch29 the waving hand.md:102** 
  - 旧：他此前低声说 I had some help… from Uncle Ricky 时
  - 新：他随后低声说 I had some help… from Uncle Ricky（本章后文）时
- **ch29 the waving hand.md:70** 引语截短：同段后半在 text/ch29:169
  - 旧：carefully loaded five tarnished rounds from the old cardboard box.
  - 新：carefully loaded five tarnished rounds from the old cardboard box. The cardboard had frayed, so a few of the sharp-tipped cylindrical rounds rolled loose in his pocket. He counted twelve total. Twelve chances.
- **ch30 wish scout back.md** 引语截短：同段后半在 text/ch30:83
  - 旧：If you touch the water, the wish won’t come true—and there might be hell to pay.

  - 新：If you touch the water, the wish won’t come true—and there might be hell to pay. The Wishing Pool is mostly dried up, except during the summer. That’s the best time to get your wish.

- **ch30 wish scout back.md:78** 筋斗属于 Mazelle 自己（text/ch05:438 Her backflips and somersaults and splits）；Scout 的行礼与舞步在 ch01/ch02
  - 旧：读者会拿 1926 年那只毛茸茸、会翻筋斗的 Scout 来比对这个形体
  - 新：读者会拿 1926 年那只毛茸茸、会向她鞠躬并跟着她舞步打转的 Scout 来比对这个形体（翻筋斗与劈叉是 Mazelle 自己的技艺，text/ch05 交代过）
- **ch30 wish scout back.md:90** ch30 无 "seven years"（该词在 ch31:34，指回来之后的七年）；原文只到 but then Scout went away.
  - 旧：本章对 Scout 那七年去了哪里始终沉默
  - 新：本章对 Scout 离开的那些年的去向始终沉默

### 批 F（ch31–ch35，9 处）

- **ch31 bad boy scout.md:30** 刻字在 text/ch31:55，门的用途在 text/ch31:118（后文）
  - 旧：而本章早前刚交代过这扇门的用途
  - 新：而这扇门的用途要到本章后文才交代
- **ch32 personally invited.md:64** text/ch32:397 那次是 Li'l Gumshoes 的梯子特技（ch05），与"七岁"无关；ch32:421 的 seven 是另一处明喻
  - 旧：她七岁时拿别人的恐惧当燃料去表演
  - 新：她当年违抗 Sharpe 夫妇演那次梯子特技、看着他们怕她摔下去
- **ch32 personally invited.md:88** 旧梦在 text/ch32:527，早于形体描写 :572；"漂亮小戏子"在 ch30 查无
  - 旧：正落在 Lorenzo 下一段马上要想起的旧梦上
  - 新：正落在 Lorenzo 前一段刚想起的那场旧梦上
- **ch32 personally invited.md:88** 
  - 旧：preened（炫耀）与 ch30 她许愿得到的"漂亮小戏子"押韵，这头东西仍然在为她表演
  - 新：preened（炫耀）这个动词把形体写成一次演出，这头东西仍然在为她表演
- **ch34 no one was there.md:13** text/ch34:91 "said aloud again"；ghost 的说法在 ch29:115 已经出现
  - 旧：第一次说出 It’s a ghost
  - 新：再次说出 It’s a ghost 并第一次不再否决它
- **ch34 no one was there.md:154** 
  - 旧：Johnny 在崖顶第二次见到 Uncle Ricky 并第一次承认它是 ghost
  - 新：Johnny 在崖顶又一次见到 Uncle Ricky 的形影，并第一次不再否决「它是 ghost」这个说法
- **ch34 no one was there.md:54** 原句 3（text/ch34:88）本身是 Johnny 一侧，与之并置的是看不见的女儿们
  - 旧：注意本段与 Johnny 一侧的并置：同一时刻他正为"要不要信自己眼睛"挣扎
  - 新：注意本段与女儿们一侧的并置：同一时刻 Johnny 正为"要不要信自己眼睛"挣扎，而崖下的两个女儿什么也没看见
- **ch34 no one was there.md:64** hot comb 在 ch34 只出现于 :97/:100，其旧事出自 ch15
  - 旧：his grandmother’s hot comb，本章上文提到的旧事
  - 新：his grandmother’s hot comb，ch15 交代的旧事
- **ch35 knew you were alive.md:52** text/ch35:55 只有两个 while，另有 watching/strategizing 两处分词
  - 旧：三个 while 层叠把"同时做四件事"写成句法上的气喘
  - 新：两个 while 与两处分词（watching…、strategizing…）层叠，把"同时做四件事"写成句法上的气喘

### 批 G（ch36–ch38，7 处）

- **ch36 look out for him.md:28** 原句 1 的分析把 cassette 的购买者写成孙子；text/ch36:19 明写 Ricky had bought her（儿子）
  - 旧：cassette 是孙子买的，标题却是他人生效的评语。
  - 新：cassette 是儿子 Ricky 买的，标题却像对她一生的评语；而她听这音乐时涌起的负罪指向外孙（本章后文写明 her grandson had been playing this group when she took his cassette player）。
- **ch36 look out for him.md** chittering 不在上一章 ch35；银圈眼睛只在本章出现
  - 旧：它们与前章林中之物的语汇高度重合
  - 新：其中 chittering 并非本章新词——ch31、ch33、ch34 已用它写林中之物的发声，而银圈眼睛（unnatural silver rim）只在本章出现过
- **ch37 beast brings water.md:13** text/ch37:112 原文是 half-empty package…at least a dozen…intact，非「一箱完好」
  - 旧：却朝她们抛来一箱完好的瓶装水
  - 新：却朝她们抛来半箱瓶装水（外包装被牙印咬烂、里面至少十几瓶完好）
- **ch37 beast brings water.md:54** 
  - 旧：chittering 在前章已是这生物的惯常发声
  - 新：chittering 在 ch31、ch33、ch34 已写为那生物的发声，上一章 ch36 里 Scout 也用同样的声音招呼病中的 Mazelle
- **ch38 the bone room.md:13** text/ch38:79 Johnny 要的是「go to the tree」；取杖/开 Jeep 是 Sharise 在 :106 自己改的主意
  - 旧：他劝 Sharise 取滑雪杖回小屋、开 Jeep 去镇上搬救兵
  - 新：他要 Sharise 回那棵树那边去，而取滑雪杖步行回去、开 Jeep 上镇搬救兵是 Sharise 自己改的主意
- **ch38 the bone room.md:28** 本章 Johnny 向上帝开口不止一次（:70/:154/:298）
  - 旧：括号句 (Thank you, God.) 是 Johnny 段落里唯一一次直接触及上帝，且以旁注形式出现，不是祷词，是事后签收。
  - 新：括号句 (Thank you, God.) 以旁注形式出现，不是祷词，是事后签收；本章他此后还要向上帝开好几回口（But, God, please let Sharise and Imani have a tomorrow. / Nothing yet, thank God. / Dear God.），唯独这一句最短。
- **ch38 the bone room.md:145** 枪响在 Imani 反复喊停之后（:295/:332/:365 → :380）
  - 旧：又在女儿冲进来喊停之前击毙了那头曾给她们送水的生物
  - 新：又在女儿冲进来一再喊停（Daddy, no!／Don’t shoot it!）之后击毙了那头曾给她们送水的生物

### 批 O1（总览三篇，38 处）

- **00_概述.md:30** O1/O2/O3 警告人＝同学 Priscilla Stephens（text/ch01:34、text/ch30:215）
  - 旧：早在七岁那年，就有大人警告过她许愿的规矩
  - 新：早在七岁那年，就有同学 Priscilla Stephens 警告过她许愿的规矩
- **.overview_templates/ov_00_概述.md.tpl:30** 
  - 旧：早在七岁那年，就有大人警告过她许愿的规矩
  - 新：早在七岁那年，就有同学 Priscilla Stephens 警告过她许愿的规矩
- **00_金句精选.md:13** 
  - 旧：脑子里过的是大人给她的这条规矩
  - 新：脑子里过的是同学 Priscilla Stephens 给她的这条规矩
- **.overview_templates/ov_00_金句精选.md.tpl:13** 
  - 旧：脑子里过的是大人给她的这条规矩
  - 新：脑子里过的是同学 Priscilla Stephens 给她的这条规矩
- **00_情感节点.md:10** 
  - 旧：说的时候她已经知道大人给过她规矩
  - 新：说的时候她已经知道同学给过她规矩
- **.overview_templates/ov_00_情感节点.md.tpl:10** 
  - 旧：说的时候她已经知道大人给过她规矩
  - 新：说的时候她已经知道同学给过她规矩
- **00_概述.md:14** O4 「用一个眼神答了」＝原文未写的通道（text/ch05:332-335 只写不必说出口，随后单独一行 Yes.）
  - 旧：而她在楼梯口用一个眼神答了「是」
  - 新：而她在楼梯口答了那个不必说出口的字
- **.overview_templates/ov_00_概述.md.tpl:14** 
  - 旧：而她在楼梯口用一个眼神答了「是」
  - 新：而她在楼梯口答了那个不必说出口的字
- **00_金句精选.md:55** 
  - 旧：而楼梯口的她用一个眼神答了「是」
  - 新：而楼梯口的她答了那个不必说出口的字
- **.overview_templates/ov_00_金句精选.md.tpl:55** 
  - 旧：而楼梯口的她用一个眼神答了「是」
  - 新：而楼梯口的她答了那个不必说出口的字
- **00_情感节点.md:22** 
  - 旧：而她在楼梯口用一个眼神答了「是」
  - 新：而她在楼梯口答了那个不必说出口的字
- **.overview_templates/ov_00_情感节点.md.tpl:22** 
  - 旧：而她在楼梯口用一个眼神答了「是」
  - 新：而她在楼梯口答了那个不必说出口的字
- **00_概述.md:16** O5 跨线年份推算（本书只认章节抬头；半个世纪只适用 ch38:122 的 1980→今天）
  - 旧：**四、半个世纪之后，六十岁的人
  - 新：**四、切回今天线，六十岁的人
- **.overview_templates/ov_00_概述.md.tpl:16** 
  - 旧：**四、半个世纪之后，六十岁的人
  - 新：**四、切回今天线，六十岁的人
- **00_金句精选.md:36** 
  - 旧：**呼应关系**：半个世纪后，同一个公司名
  - 新：**呼应关系**：今天线上，同一个公司名
- **.overview_templates/ov_00_金句精选.md.tpl:36** 
  - 旧：**呼应关系**：半个世纪后，同一个公司名
  - 新：**呼应关系**：今天线上，同一个公司名
- **00_概述.md:18** O6 汽油桶：ch11:80 离镇／ch13:227 只见一桶／ch16:46 是 Imani 落下
  - 旧：而全家进屋之后，山下少了两桶汽油，看屋人已经离镇。
  - 新：而答应照看房子的看屋人前一天一早就离了镇。
- **.overview_templates/ov_00_概述.md.tpl:18** 
  - 旧：而全家进屋之后，山下少了两桶汽油，看屋人已经离镇。
  - 新：而答应照看房子的看屋人前一天一早就离了镇。
- **00_情感节点.md:46** 
  - 旧：两桶汽油在山下失踪
  - 新：两桶汽油在山下不见了（ch16 交代是 Imani 搬行李时落在加油站）
- **.overview_templates/ov_00_情感节点.md.tpl:46** 
  - 旧：两桶汽油在山下失踪
  - 新：两桶汽油在山下不见了（ch16 交代是 Imani 搬行李时落在加油站）
- **00_情感节点.md:94** O7 Mazywood 兴建年代：ch24:418（1943 已在建）／ch30:98、113（1950 已投入甚巨）
  - 旧：八年后她亲手建起 Mount Shasta 山脚的 Mazywood，许愿的甜头换成守秘的劳役。
  - 新：而她从战前就在 Mount Shasta 山脚一手兴建的 Mazywood，把许愿的甜头换成守秘的劳役。
- **.overview_templates/ov_00_情感节点.md.tpl:94** 
  - 旧：八年后她亲手建起 Mount Shasta 山脚的 Mazywood，许愿的甜头换成守秘的劳役。
  - 新：而她从战前就在 Mount Shasta 山脚一手兴建的 Mazywood，把许愿的甜头换成守秘的劳役。
- **00_金句精选.md:15** O8 1950 年她没有「把话说全」（text/ch30:267 明写又漏）
  - 旧：1950 年她在同一个池边把这句话补完，代价也由她自己认领。
  - 新：1950 年她在同一个池边临时起愿，照样漏了要他原样回来这一条，代价也由她自己认领。
- **.overview_templates/ov_00_金句精选.md.tpl:15** 
  - 旧：1950 年她在同一个池边把这句话补完，代价也由她自己认领。
  - 新：1950 年她在同一个池边临时起愿，照样漏了要他原样回来这一条，代价也由她自己认领。
- **00_金句精选.md:119** O9 ch35:263、ch40:25：Tasha 的脚伤到露骨，只是没被咬
  - 旧：Imani 与毫发未失的母亲会合
  - 新：Imani 与没有被咬过一口的母亲会合
- **.overview_templates/ov_00_金句精选.md.tpl:119** 
  - 旧：Imani 与毫发未失的母亲会合
  - 新：Imani 与没有被咬过一口的母亲会合
- **00_概述.md:34** O10 LDR 不是 Johnny 自己的公司（ch06:25、104：是买他剧本的那家）
  - 旧：是在自己公司的三个字母里才找回她的名字
  - 新：是在买他剧本的那家公司的三个字母里才找回她的名字
- **.overview_templates/ov_00_概述.md.tpl:34** 
  - 旧：是在自己公司的三个字母里才找回她的名字
  - 新：是在买他剧本的那家公司的三个字母里才找回她的名字
- **00_概述.md:32** O11 包装是半箱、至少十余瓶完好（text/ch37:158）
  - 旧：直到它咬破包装送来一箱完好的水
  - 新：直到它咬破包装送来十几瓶完好的水
- **.overview_templates/ov_00_概述.md.tpl:32** 
  - 旧：直到它咬破包装送来一箱完好的水
  - 新：直到它咬破包装送来十几瓶完好的水
- **00_情感节点.md:118** O12 枪响在喊停之后（text/ch38:295、332、371→380）
  - 旧：也在女儿冲进来喊停之前，击毙了那头曾给她们送来一箱水的生物
  - 新：也在女儿冲进来反复喊停之后，击毙了那头曾给她们送过水的生物
- **.overview_templates/ov_00_情感节点.md.tpl:118** 
  - 旧：也在女儿冲进来喊停之前，击毙了那头曾给她们送来一箱水的生物
  - 新：也在女儿冲进来反复喊停之后，击毙了那头曾给她们送过水的生物
- **00_金句精选.md:151** 
  - 旧：在女儿冲进来喊停之前击毙了那头曾给她们送水的生物
  - 新：在女儿冲进来反复喊停之后仍扣下扳机，击毙了那头曾给她们送水的生物
- **.overview_templates/ov_00_金句精选.md.tpl:151** 
  - 旧：在女儿冲进来喊停之前击毙了那头曾给她们送水的生物
  - 新：在女儿冲进来反复喊停之后仍扣下扳机，击毙了那头曾给她们送水的生物
- **00_概述.md:24** O13 ch32 的那句不是全章末句（末句是她隔着落地窗的骄傲）
  - 旧：本章末句写明，最后杀死他的不是心脏也不是 Scout
  - 新：本章收尾几行写明，最后杀死他的不是心脏也不是 Scout
- **.overview_templates/ov_00_概述.md.tpl:24** 
  - 旧：本章末句写明，最后杀死他的不是心脏也不是 Scout
  - 新：本章收尾几行写明，最后杀死他的不是心脏也不是 Scout
- **00_情感节点.md:94** 
  - 旧：本章末句写明，最后杀死他的既不是心脏也不是 Scout
  - 新：本章收尾几行写明，最后杀死他的既不是心脏也不是 Scout
- **.overview_templates/ov_00_情感节点.md.tpl:94** 
  - 旧：本章末句写明，最后杀死他的既不是心脏也不是 Scout
  - 新：本章收尾几行写明，最后杀死他的既不是心脏也不是 Scout

### 批 O2（总览三篇（二次回查），10 处）

- **00_概述.md:73** Sharise 是姐姐（text/ch06:225 十八岁／ch27:458 her older sister／ch35:28 his older daughter） ｜ 该条是 Sharise 的弧光，她扣住的是妹妹 Imani 的手
  - 旧：而她在雪里扣住的是姐姐的冷手指
  - 新：而她在雪里扣住的是妹妹的冷手指
- **.overview_templates/ov_00_概述.md.tpl:73** 
  - 旧：而她在雪里扣住的是姐姐的冷手指
  - 新：而她在雪里扣住的是妹妹的冷手指
- **00_情感节点.md:82** ch26 是白天出发（text/ch26:118 that morning；紧接 ch27:311 barely nine thirty）
  - 旧：Imani 带着 Sharise 与一支 Winchester 追进夜里 the Beast 的踪迹
  - 新：Imani 带着 Sharise 与一支 Winchester 一早就追进 the Beast 的踪迹
- **.overview_templates/ov_00_情感节点.md.tpl:82** 
  - 旧：Imani 带着 Sharise 与一支 Winchester 追进夜里 the Beast 的踪迹
  - 新：Imani 带着 Sharise 与一支 Winchester 一早就追进 the Beast 的踪迹
- **00_金句精选.md:93** 
  - 旧：Imani 带着 Sharise 与一支 Winchester 在夜里追进雪原
  - 新：Imani 带着 Sharise 与一支 Winchester 在上午的雪光里追进雪原
- **.overview_templates/ov_00_金句精选.md.tpl:93** 
  - 旧：Imani 带着 Sharise 与一支 Winchester 在夜里追进雪原
  - 新：Imani 带着 Sharise 与一支 Winchester 在上午的雪光里追进雪原
- **00_概述.md:22** ch20 的逃生发生在天亮之后（text/ch19:212 6:20 Daylight／ch20:385 a single morning）
  - 旧：**七、天不亮的一家人弃车逃生
  - 新：**七、天亮后一家人弃车逃生
- **.overview_templates/ov_00_概述.md.tpl:22** 
  - 旧：**七、天不亮的一家人弃车逃生
  - 新：**七、天亮后一家人弃车逃生
- **00_情感节点.md:70** 
  - 旧：一家人天不亮弃行李逃生
  - 新：一家人天亮后弃行李逃生
- **.overview_templates/ov_00_情感节点.md.tpl:70** 
  - 旧：一家人天不亮弃行李逃生
  - 新：一家人天亮后弃行李逃生

## 四条悬置项（整改后仍不裁决，逐条已回查）

1. **Scout 的来历与本质**——Mazelle 自己也只是猜想（路上捡的／会行礼跳舞），全书无成因解释；ch27 那句 not his ghost or hallucination 只修饰「生前最后一次交谈」，不是对幻象的裁定。
2. **ch38 击毙者／送水者／ch30 池中物是否同一**——文本从不把三者放进同一画面确认。
3. **Imani 是否真听见声音**——ch28 的 heard her voice 与 in your head 两种读法并存，(A Beasthole, technically.) 是叙述插注不是 Imani 台词。
4. **ch40 they were going home**——「home」指何处不裁决。

## 结论

**五步审查完成**：d 步 78 条阻断报警 → 章节侧落盘 85 处；e 步总览侧落盘 48 处；合计 **133 处整改全部回查原文**。收口复跑 gate.sh **0 条阻断型**，引语层（299/299 逐字、275/275 本章归属、整串 flat 零跨章零拼接）在本轮全部改动后**未变差**——引语层与整改层是两件事，本轮 133 处改动**只动分析层与导航层**，275 条引语一字未换，这是「整改不伤引语」的证据。

**同会话审查的已知盲区**（供用户判断是否另行指派异实例复核）：
1. 审查方与执行方共享写作时的语境记忆，对「当初为什么这样写」的判断可能带同一偏差；
2. d 步子代理报警的原始理由曾因 `.output` 落盘为 0 B 而丢失，三条改由主会话重新取证定性——**报警的「发现过程」不可复现，只有结论可复现**；
3. 总览层的**中文事件断言**没有任何门禁覆盖（本轮 48 处全靠人工逐条 grep），异实例若只跑门禁会全部漏过；
4. 说话人／人物／关系／结局四类已实测不可靠机械化（`check_speaker_consistency` 命中约 1/3 假阳），本轮该层为纯人判，异实例复核价值最高。
