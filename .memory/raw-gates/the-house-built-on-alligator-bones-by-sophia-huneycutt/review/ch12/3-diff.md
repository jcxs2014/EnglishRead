# ch12（书内 Chapter Eleven）深审 R3/R4 三张单子

素读基线：`review/ch12/1-suread.json`（82 条事实／0 MISS，只读 `text/ch12_chapter_eleven.txt`，写完才开 md）
机器层：`review/ch12/2-machine.json` → verdict `ok`（blocks 4 ∈ target [2,4]；segments 4／MISS 0；words 1154；struct_bad 0）
直撇号探针：`/tmp/apos.txt` 未列 ch12 ⇒ 0 站
词表：16 行例句展平逐字 **0 MISS**

## 🟥 阻断（7）

### C-12-1 形态误称：「无起伏的单音节对白」
- md:14：**「Nova 用无起伏的单音节对白与 Princess Diana’s ghost 的荒诞假设完成低温喜剧化」**
- 原文逐字：`text/ch12_chapter_eleven.txt:81` — `She answered in single-word sentences. Yes. No.`（**单词**，不是单音节）；而同章 Nova 的台词多为完整长句：`:87` `“Everything behind that door is off-limits… It’s locked, as are the other doors to that side of the building.”`、`:126` `“Regulations weren’t as tight back then. Not in Florida, anyway…”`、`:135` `“Yeah. It’s a lot, even with so much missing…”`
- 判定：`single-word sentences` 只覆盖 :81 那两处 Yes／No；把它升级成「单音节对白」并当作 Nova 全章的说话方式，既错在语言单位（word≠syllable），也错在范围。md:10 自己写的「Nova 单词作答」才是准确口径。⇒ 内部还自相矛盾（md:10 vs md:14）。改法：「Nova 的 Yes／No 式单词作答与毫无起伏的转述」。

### C-12-2 依据叙述者推断作结构结论，且与本章互斥
- md:12：**「反转在发落者的位置：把 Dart 支开的不是 Gazzie 而是雇员 Harrison，说明农场真正的运转握在中层手里，祖母亲的注意力只是最后一道章。」**
- 原文逐字：`:66` — `Of course. He’d suggested a task that would keep me away from her.`（这是 **Dart 的推断**，句首 `Of course.` 正是她的即时归因）；`:63` — `“You will be helping me. Harrison pointed out we’ve neglected our files long enough.”`；`:69` — `“Show her,” Gazzie commanded Nova.`；`:93` — `“Gazzie’s orders.”`；`:147` — `Don’t leave this building. Your grandmother doesn’t want people wandering.`
- 判定：「不是 Gazzie 而是 Harrison」在本章内部即被 :63/:69/:93/:147 四句顶回——指派由 Gazzie 说出并命令执行，禁令直接归给 Gazzie；而 md:38–md:44 分析的原句 :141 本身就是「Gazzie 在放话」。**「农场真正的运转握在中层手里」是全书权力结构的判断，不能由本章一处的叙述者推断承担。**改法：「反转在归因的方向：Dart 把支开自己的责任算到 Harrison 头上（:66 是她的推断），而本章的命令、锁与禁令仍全部署在 Gazzie 名下——两套归因同章并存，未被调和」。

### C-12-3 与同章证据直接相抵：「Gazzie 反而不在规则链里」
- md:34：**「这条规矩的出处用 "Virginia said" 转述，档案室的实际行政命令出自 Virginia，Gazzie 反而不在规则链里。」**
- 反证逐字：`:93` — `“Gazzie’s orders.”`；`:147` — `“One more thing: Don’t leave this building. Your grandmother doesn’t want people wandering.”`；另 `:126` Nova 的转述还带两层对冲：`Or so she said. I wasn’t around then.`
- 判定：本章的规则链恰恰以 Gazzie 为终点（锁门、禁走），Virginia 只在「留档年限」这一条上以 hearsay 出现；md 还把 Nova 的「她是这么说的／我那时不在场」这层不可靠标记丢掉。改法：删去「Gazzie 反而不在规则链里」，改为「唯有关于保留年限的那一条，Nova 用 `Virginia said` 转述，并自补 `Or so she said. I wasn’t around then.`」。

### C-12-4 施事归错人：「Dart 的自嘲式归因（我一抬头它就变本加厉）」
- md:24：**「它既是 Dart 的自嘲式归因（我一抬头它就变本加厉），又像在给房子留一个「有反应」的接口」**
- 原文逐字：`:27` — `Gazzie tilted her face toward the ceiling, redirecting my attention. I followed her line of sight to a crack about ten inches long… Within seconds, it was a steady stream, as though her attention had made it worse.`
- 判定：叙述者是 I，`as though **her** attention had made it worse` 的 her 只能回指 Gazzie（先仰头、且水落在她脚边的那位）；md 的括注把这份「看一眼就让事情恶化」归给 Dart 自己，方向相反。md:20 的中文理解保留代词未落实（「她的注视」）✓，问题只出在这一句括注。改法：「既像 Dart 替 Gazzie 记下一笔自嘲（她一抬头，漏势就变本加厉）」。

### C-12-5 承重信息缺失：Virginia 逼 Gazzie 开始记账的那二十年
- md 全篇（:10／:12／:34 三处涉及 Nova 转述）都停在「2009 年以前的文件可以扔」。
- 原文逐字：`text/ch12_chapter_eleven.txt:126` — `“Regulations weren’t as tight back then. Not in Florida, anyway. Virginia made Gazzie start tracking paperwork regularly in the last two decades, when they acquired the two satellite farms. Or so she said. I wasn’t around then.”`
- 判定：`Virginia made Gazzie start tracking paperwork regularly` 是本章唯一具体交代「Virginia 对 Gazzie 行使过什么权力」的一条，直接接上 ch08:192 留下的 `Virginia must hold some kind of power over her, but I didn’t know what it could stem from`；`when they acquired the two satellite farms` 还与 ch08:132「三场合计」对上。md 一处未收。取证：`/usr/bin/grep -nE "分场|satellite|二十年" "ch12 dart sent to digitize files.md"` → 0 命中。改法：md:10 或 md:34 补一句「近二十年开始 regular 记账是 Virginia 逼的，时点在买下两座分场之际——而 Nova 立刻自补「她是这么说的，我那时不在场」」。

### C-12-6 承重信息缺失：Ida 画像的笑变明显了
- md 只在词表 `pronounced`／`gaze` 两行的例句里出现（:79/:89），导航与精读全无。
- 原文逐字：`:78` — `Averting my gaze, I studied Ida’s portrait on the wall. Again, her hair’s exquisite detailing drew me in, each strand seemingly painted one by one. Since the last time I’d seen her, the smile on her lips seemed more pronounced.`
- 判定：这是本书「画像／雕像会动」线索库里的关键一级（`Again` 与 `Since the last time` 明确把它接到 ch06 与 ch08 的两幅／一次细读上），也是 Dart 在等待 Nova 涂润唇膏时的主动逃避动作——本章悬疑装置的一部分。按「整块信息单元缺失」判阻断。改法：md:10 或 md:12 补一句「等 Nova 的当口她去盯墙上的 Ida，认定距上次以来**笑得更明显**（Again／Since the last time 把这三眼看串成一条）」。

### C-12-7 跨章全称预言：「后面 Gazzie 每多给一分信任，都会牵动这条交换是否兑现」
- md:56（block 4 读者视角提示）
- 判定：「每…都会」是对后 37 章的普遍预言，本次深审尚未跑到，无取证。同段的「记住这个等式（有用＝可被坦白）」有 :156 凭据 ✓，可留。改法：「本章她把这条交换摆在 :156；后文 Gazzie 若给出信任，先回这一句对表」。

## 🟡 提示（7）

- **T-12-1** md:26「这漏水发生在办公室**正中央**」：原文只给 :27 仰头见天花板裂缝、水落在 Gazzie 脚边，位置是办公室入口一带（:9/:12 前台附近）；「正中央」是造出来的坐标。
- **T-12-2** md:36「Nova 说这些时毫无起伏（She spoke without inflection）」：该引语出自 :57，描写的是她反问 `“Really?”` 那一刻；档案室里的平板另有其词——:114 `“These are the files,” Nova droned`。建议改引 droned，或标注原所指。
- **T-12-3** md:11「全章的波澜都被压在「收集证据」这层理智下面」：全称。:24 `Before I could repress the urge, I narrowed my eyes at him`、:48 `Suck-up. I rolled my eyes`、:141 `Heat spread across my cheeks` 三处都是当场外泄、并未被理智压住。
- **T-12-4** md:10／md:93「上农场的第一天」：本章只写 `the next morning`（:9），"第一天" 的凭据在 ch11:132 `“You’ll start tomorrow.”`；建议在导航注明是次日的第一个班次，以免与 ch08 的参观日混。
- **T-12-5** md:24「水、藻、裂缝在这里都是有意志的原告」：藻类在本章只以 `like the algae`（:39）一笔带过，实体在 ch08；三者并列是拔高，且「原告」暗含「有意志」的裁决——本章 Dart 的措辞是 `Nature just seemed intent on`（seemed＝她自己的读法）。
- **T-12-6** 轻漏：:150 `The unnamed incident from a few days before must have happened outside; I’d overheard Nova mentioning something out back.`（她对新信息的唯一一次主动追问被 :153 切断）与 :84 `A thin goateed man in a bright green tee passed by the window. Another employee.`（新增一名员工，是否与 ch08:156 喂料者为同一人原文未写）。
- **T-12-7** md:10「加工区一侧的门**全部**上锁」宜照原文限定：:87 是「那扇门锁着，那一侧的其他门也锁」，且加工区本身是 `Presumably`（:84）——她只是推测那就是参观时示意过的加工区。

## ⬜ 判为假红／不报警（8）

- **F-12-1** md:24「水量按时间单位三级升级…三个刻度」✓ 三档全在引语内（a bead／then another／steady stream）。
- **F-12-2** md:34「"even with so much missing" 是本句唯一一处泄露」✓ 限定在三句之内成立；「缺了什么、谁弄缺的」本章确未解释。
- **F-12-3** md:44「连最不在乎这份工的人都读懂了」✓ :81 `She wasn’t invested in Greer Fine Alligators` ＋ :129。
- **F-12-4** md:44 对 `festering for years, if not decades` 的引用与「缺了一大块」的组合 ✓ :111／:135。
- **F-12-5** md:54「转述的话、偷听的只言片语、门锁、规章」与 :156 四单项一一对应；`There’ve been accidents in the past` 逐字 ✓ :105。
- **F-12-6** md:13「她再次把自我价值登记成一桩待兑换的交易」✓ 有 ch09:111（redeem myself）作旧账，非凭空。
- **F-12-7** md:46「对照本章开头——Gazzie 在车旁等她、一句怨言没有——同一天的两个证据指向相反结论，叙述者没有调和它们」✓ :9／:141，且「同一天」与本章 `the next morning` 一致。
- **F-12-8** 词表 16 行例句全部为原文逐字子串（0 MISS）；`bonding session` 一行把本章与 ch10 夜谈相接 ✓（时间线：ch10 谈话＝ch11 早餐当天清晨，:54 `After the way she’d opened up yesterday` 与之自洽）。

## 逐块对应（R4）

- block1（:27）关键词 crack／bead／steady stream／attention ✓ 全在引语；中文理解逐句对应，代词「她」未被落实 ✓（错在 md:24 的括注，见 C-12-4）。
- block2（:135）关键词 missing／consolation／throw out／dig back ✓；「2009 年以前」与「十年」两个数字逐字回源 ✓；`IRS` 译「国税局」✓。
- block3（:141）关键词 isolating／worthless／message／picked up on ✓；`You’re not one of us` 译「你不是一员」✓；中文理解未把这句写成 Gazzie 的台词（原文是 Dart 读出的「message」）✓。
- block4（:156）关键词 settled／overheard／locked doors／usefulness ✓；中文理解把 `in her office` 的所属悬着（「她办公室里的话」）✓ —— 原文未写明是农场办公室还是宅内办公室，不裁决。
- 本章无 cliffhanger（收在 :162 `Resigned, I pulled out the first file.`），md 未误称悬念 ✓。
