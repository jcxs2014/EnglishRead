# ch01 R3 三张单（漏 / 编 / 错）

- 书：Don't Leave Her Alone by Desiree de Fez
- 章：ch01（md `ch01 chapter 1.md`；原文 `text/ch01_chapter_1.txt`）
- 依据：`docs/rules/审查表.md` R3／`docs/rules/生产-审查对照.md`（先跑机器探针再动眼睛／每个探针须能被阴性对照证伪／成片同类报警先假定工具口径错了）
- 输入：`review/ch01/1-suread.json`（8 条 fact）＋ `review/ch01/2-machine.json`（verdict ok，6/6 引语命中）
- **md 版本指纹**（另一 agent 正在改写导航／一句话总结／句子结构，本报告行号只对该指纹有效）：
  `md5 = e3cb5bff8e140d30fc6d91a70be5ea12`，mtime `2026-10-21 13:05:45`，共 133 行。
- 机器层先跑（全部只读）：`scripts/chapter.sh` EXIT 0 ｜ `check_vocab.py` ch01 无 WARN ｜ `quotes.py blocks` EXIT 0 ｜ `structure.py order` ch01 不在不可判定名单 ｜ `analysis.py inline` ch01 无报警行 ｜ `check_chinese_layer.py` ch01 不在阻断/提示名单 ｜ 自建 flat 逐字比对 6/6 整串命中。

**三张单计数（去重后）：漏 0 条 ／ 编 2 条 ／ 错 3 条**（其中 2 条「编」与「错」同源，**阻断型缺陷实为 2 项**：`粉色脚趾`、`校庆`）；**⚠️ 需人判 3 条**（怪物跨章对照、Brisa 感受"唯一"的作用域、「罢演」用词）。提示型 1 条（中文层英文残留，兼工具口径盲区）。

## 0. 素读事实逐条对照表

| 素读事实 | md 落点（行号） | 判定 |
|---|---|---|
| ① [6,717] 学龄前班扮天使；Brisa 背圣诞诗找妈妈 → 表演变 playback → 决定不再找 | :20（原句 1 引语逐字）· :22 中文理解 · :30 读者视角提示 | ✅ 一致 |
| ② [723,1287] Diana 做好一切准备；**伴侣整天在马德里，所以由一位同学的妈妈代接儿子** | :32（原句 2 引语逐字）· :34 中文理解 · :38 句子结构 · :10 导航 | ✅ 一致（用户已明示此点核实过，未作任何"修正"） |
| ③ [1664,3071] 走到 Balmes 一半开始心跳、复盘拔插头、确信有温控又推翻、转身折返、打 Carlos 电话未接、含泪快步折回 | :44（原句 3 引语逐字）· :46 中文理解 · :50 句子结构 · :52 为什么这样写 · :54 读者视角提示 | ✅ 一致（:46 残留英文 `hurried`，另见「单子②·补」） |
| ④ [3074,3591] 撞见 Brisa 同学家长、假装发短信避眼神 | :56（原句 4 引语逐字）· :58 中文理解 · :62 句子结构 · :64 为什么这样写 · :66 读者视角提示 | ✅ 概括（内容对应原文；但 :58 的「校庆」是误译、:66 的「恐惧」标签与同块 :64「而非"恐惧"」互斥 ⇒ 见「单子②/③」） |
| ⑤ [3594,4432] 到楼下、盼有东西起火、进门后一切正常、直发器没有温控 | :68（原句 5 引语逐字）· :70 中文理解 · :74 句子结构 · :76 为什么这样写 · :78 读者视角提示 | ✅ 一致 |
| ⑥ [4438,4500] 迟到、脚趾磨破 | :80（原句 6 引语逐字）· :82 中文理解 | ✅ 概括（:82「脚趾磨破」= 原文 `her pinkie toes raw`；但 :16 把「小趾」写成「粉色脚趾」，见「单子②」） |
| ⑦ [4503,5393] 助教评判迟到、听见 Brisa 哼的歌、手机录视频被无视、没有保姆只有妈妈们 | :80 · :82 · :86 句子结构 · :88 为什么这样写 | ✅ 一致 |
| ⑧ [5394,6307] 诗后唱改编 Taylor Swift 歌、Diana 独坐最后一排、Brisa 是唯一不唱歌的孩子、抱臂把金冠当面具、像蒙着闪粉纸带的极小罪犯 | :80 · :82 · :86 · :88 · :90 | ✅ 一致（:10/:14/:133 的「罢演」是概括性用词，非逐字 ⇒ 见「单子③」需人判条） |

**机器层与人工层的关系**：6 条引语经 flat 归一后**整串**命中本章原文，且独立切分实测句数 6 / 8 / 20 / 2 / 9 / 19 与 md:26/:38/:50/:62/:74/:86 的自述**全部吻合**；本章**没有**被 md 略过的实质段落（唯一"未覆盖"是页码 `1` 与首句粘连的切分伪影）。⇒ 本次问题**不在引语层**，全在**中文层的改写与措辞**。

---

## 单子① 漏（素读有、md 完全没有）

| 素读事实 | md 落点（行号） | 判定 |
|---|---|---|
| — | — | **0 条** |

自证：8 条 fact 的每一个成分均在 md 有落点（逐条见表 0），且引语覆盖全章句子。**无"覆盖不足（漏）"型缺口**。
注：下列项曾疑似漏，经核为**已覆盖**，记此备查：
- 原文 :12 `She left the house early` → md:34「她提早出门」✔
- 原文 :12 `She'd even finished the following week's assignments, something she hadn't managed since she'd gone freelance all those years ago` → md:34「甚至完成下周的约稿，这是她多年前自由职业以来从未做到的」✔
- 原文 :6 `to symbolize purity` → md:22「一切应是无瑕的白以象征纯洁」✔
- 原文 :15 `She felt the weight of her makeup, the pins and needles on her face, the sweat soaking through her thermal T-shirt` → md:46 ✔
- 原文 :21 `Everything had been checked, and checked again, an hour earlier` → md:78 ✔
- 原文 :30 `the exact same shot in miniature, multiplied by one hundred` → md:82「被缩小一百倍的同一画面」✔

**与 md 自述冲突的项不在本单**，一律进「单子②／单子③」。

---

## 单子② 编（md 写了原文里没有的内容）

> ⚠️ **计读法**：下面第 1、2 条在「单子③ 错」里也各出现一次——**同一处缺陷的两个视角**：「编」＝原文没有这个内容；「错」＝这个内容与原文/与 md 自述矛盾。**去重后阻断型缺陷仍是 2 项**（粉色脚趾、校庆），不是 4 项。

| 素读事实／md 断言 | md 落点（行号） | 判定 |
|---|---|---|
| 导航「用**粉色脚趾**被新靴子磨破这类细节，把焦虑具象化」——原文从未写脚趾是粉色，只写 `her pinkie toes raw`（小趾磨破），全章颜色词仅 `white / golden / beige` | :16 | ❌ **编（阻断型）** ＋ 与 md 自述冲突 |
| 「**校庆**演出」／「比她先到**校庆**」——原文只有 `school play`（学校演出，实为圣诞演出）与 `Christmas play`，全书 `anniversary` 零命中 | :34、:38、:58 | ❌ **编（阻断型）** ＋ 与 md 自述冲突（详见「单子③」同项） |
| 补：中文层残留英文单词（`onstage` / `hurried` / `likely` / `partly` / `fear of judgment` / `em dash`）——非"编造内容"，属英文残留未中文化 | :10、:46、:54、:66 | ❌ 编（不适用）／**提示型**（工具口径问题，见 4-verdict.md「机器层结果与假红判定」） |

### 证据（逐字回原文核对）

**编·粉色脚趾**
- 原文 `text/ch01_chapter_1.txt:15` 逐字结尾：`…her too-tight new boots destroying her pinkie toes.`
- 原文 `text/ch01_chapter_1.txt:27` 逐字：`Diana arrived at the Christmas play late, her pinkie toes raw.`
- 取证命令：`grep -rnoiE '\bpink[a-z]*\b' text/ch01_chapter_1.txt` → 命中 2 处（:15、:27），**均为 `pinkie`**，无任何颜色词。
- 阴性对照：`grep -rnoiE '\b(pink|red|blue|green|black|white|gold|golden|beige)\b' text/ch01_chapter_1.txt` → 仅 `white`(:6)、`golden`(:6)、`beige`(:6)、`golden`(:30)，**无 `pink`**。
- md 自述冲突（同文件内！）：`:52`「与后文 "pinkie toes raw" 呼应」、`:88`「"toes soft and perfect" 与 "pinkie toes raw" 的对照」——md 自己引的是 `pinkie toes raw`，却在 `:16` 写成"粉色脚趾"。⇒ 判**编**（原文没有的修饰），且**与 md 自述冲突**。

**编·校庆**
- 原文 `text/ch01_chapter_1.txt:12` 逐字：`…or missed a school play just to hole up and finish reviewing some absurd movie, or rush off to interview a barely relevant public figure.`
- 原文 `text/ch01_chapter_1.txt:18` 逐字：`…who all had left home with just enough time but would seemingly still beat her to the school play.`
- 原文 `text/ch01_chapter_1.txt:27` 逐字：`Diana arrived at the Christmas play late, her pinkie toes raw.`
- 取证命令：`/usr/bin/grep -cE 'anniversary|anniversar' *.txt`（在 `text/` 内，显式路径）→ **exit 1，18 章全 0**；`/usr/bin/grep -noE 'school play|Christmas play' ch01_chapter_1.txt` → 命中 :12（×2）、:18、:27、:30（exit 0）。
- 阴性对照（证明探针本身有效，不是口径错）：同一 `-E` 交替模式 `Christmas play|school play` 在 ch01 命中 4 行、其余 17 章 0（`/usr/bin/grep -rcE 'Christmas play|school play' text/*.txt`）⇒ 探针能命中真实存在的词形，**「anniversary」零命中是真的零命中**，原文不存在周年庆语义。
- md 自述冲突：`:34` 同一句内前半写「女儿的**圣诞演出**」「先看演出」，后半写「错过**校庆演出**」；`:58`「比她先到**校庆**」；`:82`「Diana 迟到抵达**圣诞演出**」；`:133`「圣诞演出」。全章自相矛盾。
- 全书一致性：`grep -rn '校庆' --include='*.md' .` → **仅 ch01:34、:38、:58**；其余 17 章一律用「演出／圣诞演出」。

---

## 单子③ 错（md 写了但与原文矛盾）

| md 断言 | md 落点（行号） | 判定 |
|---|---|---|
| 「错过**校庆**演出」「比她先到**校庆**」——原文事件是 `school play`（学校演出）且为 `Christmas play`（圣诞演出），无"周年庆" | :34、:38、:58 | ❌ **错（阻断型）**（同时属「单子②」：原文没有的概念） |
| 「em dash 后的 "she couldn't stand …" 是本章**唯一一次** Diana 表达对他人反应的**恐惧**」——原文全章无 `fear` 字样；且同一引语块的 `:64` 写着「作者把 Diana 的痛苦写成"羞辱"**而非"恐惧"**」，**同块两行标签互斥** | :66（对照 :64） | ❌ **错（提示型）**——"恐惧"是对 `couldn't stand` 的可辩护解读、**不与原文直接矛盾**（原文本章本就无 fear 表述）；真问题在 **md 自述冲突**（:64 vs :66）＋"唯一一次"计数断言不成立。判提示型而非阻断型（无原文逐字可证其与原文矛盾）＋⚠️ 需人判 |
| 「用**粉色脚趾**被新靴子磨破」——原文只有 `pinkie toes`（小趾），无颜色 | :16 | ❌ **错（阻断型）**（同时属「单子②」） |
| 「她**不是被怪物追杀**」——ch01 与序章均无 `monster`，全书主题线在 ch02:120 / ch05:441 / ch06:6 / ch13:18 | :88（与 :12 呼应） | ⚠️ 需人判（全书主题修辞，非本章编造） |
| 「是本章**唯一一次**直接写出 Brisa 的感受，此前都是外在行为」——原文 :6 `Failing to see her mom in the crowd, she decided to stop looking.` 已是 Brisa 的内心决定 | :88（对照 :30） | ⚠️ 需人判（"唯一"在块内成立、全章不成立） |
| 「Brisa … **罢演**」——原文只写 `her acting out had made her the star of the Christmas play: The only child not singing`，未写"拒绝演出" | :10、:14、:133 | ⚠️ 需人判（属概括，不判错） |
| 导航「伴侣整天在马德里、**帮不上忙的**」 | :10 | ✅ 一致（原文 :12 `Her partner was going to be in Madrid all day`；用户明示已核实，不动） |

### 证据（逐字回原文核对）

**错·校庆**（同「单子②」取证命令；核心矛盾引文）
- md:34 逐字：`…她想不起哪年圣诞节没拖延购物、没溜出家庭晚餐、没为了窝着写完某部荒诞电影的评论或冲去采访某个无足轻重的公众人物而错过校庆演出。`
- md:38 逐字：`…第七句用 when 引导的时间从句写她想不起哪年圣诞节没拖延购物、没溜出家庭晚餐、没为窝着写评论或赶去采访而错过校庆演出…`
- md:58 逐字：`…他们都"刚刚好"出门，却似乎仍会比她先到校庆。`
- 原文对应句逐字（`text/ch01_chapter_1.txt:12`）：`She couldn’t remember a Christmas when she hadn’t put off her shopping, slipped out of a family dinner, or missed a school play just to hole up and finish reviewing some absurd movie, or rush off to interview a barely relevant public figure.`
- 原文对应句逐字（`text/ch01_chapter_1.txt:18`）：`…would seemingly still beat her to the school play.`

**错·唯一一次恐惧**
- md:66 逐字：`em dash 后的 "she couldn't stand when smiling parents pointed out …" 是本章唯一一次 Diana 表达对他人反应的恐惧，显示她的焦虑 partly 是社会性焦虑（fear of judgment）。`
- md:64 逐字（同块）：`作者把 Diana 的痛苦写成"羞辱"而非"恐惧"——焦虑症的代价不仅是内心折磨，更是社会性尴尬；…`
- 原文 `text/ch01_chapter_1.txt:18` 逐字：`She pretended she was texting to avoid eye contact—she couldn’t stand when smiling parents pointed out that she was going the wrong way, though she herself had made that joke, too, when she saw someone rushing home to grab a swim bag or whatever else.`
- 取证命令：`/usr/bin/grep -cE 'fear[a-z]*' ch01_chapter_1.txt` → **exit 1，0 命中**；`/usr/bin/grep -noE 'judg[a-z]*|embarrass[a-z]*' ch01_chapter_1.txt` → 仅 :30 `judge`、:15 `embarrassed`。
- 阴性对照（证明探针有效，不是口径错）：同一模式在全书有命中——`/usr/bin/grep -cE 'fear[a-z]*' *.txt` → ch02:1、ch05:2、ch06:3、ch10:1、ch11:1、ch15:1、ch16:1（exit 0），ch01 才是真 0。
- ⚠️ 需人判点：`couldn't stand`（受不了／无法忍受）作"社会性不适"解读是可辩护的；病句在**"恐惧"这个字面标签**与**"唯一一次"这个计数断言**。

**错·粉色脚趾**：证据同「单子②」。

**需人判·怪物**
- 取证命令：`/usr/bin/grep -cE 'monster|monstru|creature' ch01_chapter_1.txt` → **exit 1，0**；`/usr/bin/grep -cE 'monster|monstru|creature' ch00_prologue.txt` → **exit 1，0**；阴性对照（同一模式全书）：ch02:1、ch05:1、ch06:1、ch13:4（exit 0）⇒ 探针有效，ch01 与序章的 0 是真 0。
- md:88 逐字：`作者把 Diana 的迟到写成社会性死亡——她不是被怪物追杀，而是被其他母亲的凝视；…`
- 判为需人判而非编造的理由：md:12「在序章的恐怖之后…恐怖不来自外力」已建立全书恐怖基调，`monster` 在 ch05:441 确有实体。⇒ 属跨章修辞，**本章范围内**为悬空对照。

**需人判·Brisa 感受唯一性**
- 原文 `text/ch01_chapter_1.txt:6` 逐字结尾：`Failing to see her mom in the crowd, she decided to stop looking.`
- 原文 `text/ch01_chapter_1.txt:30` 逐字：`Stung by her mother’s absence, she had sunk into the choir.`
- md:88 逐字：`…母亲缺席刺痛了她，是本章唯一一次直接写出 Brisa 的感受，此前都是外在行为。`
- md:30 逐字：`Brisa "decided to stop looking" 是本章第一个主动选择…` ⇒ md 自身承认 :6 有一个 Brisa 的主动内心动作。⇒ "唯一"在**原句 6 块内**成立，在**全章范围**不成立。

---

## 未进扫描集内容（❓ 无法判定，不是「正常」）

以下内容**我没有检查**，不能据此判通过：

1. **引语字符级一致性**（标点、大小写、弯引号/破折号/省略号的逐字符比对）：我只做了 flat 归一比对（NFKC + 弯引号/破折号归一 + 空白压缩），flat 会掩盖标点级差异 ⇒ ❓ 无法判定
2. **词汇表 22 条的释义准确性**与 **⭐/⭐⭐/⭐⭐⭐ 分档合理性**（我只验了 22 条例句在原文逐字命中）⇒ ❓ 无法判定
3. **关键词 26 条（36 个英文词）是否落在其所属引语块内**——我已跑 `structure.py anchor .`：全书「凭空造词 0 处／松散关键词 0 处」，ch01 的 26 个关键词全部落在本块引语或分析正文内 ⇒ **已核，非未核**；但**关键词的"分析价值"（是否真的指向该块主题）未核** ⇒ ❓ 无法判定
4. **导航四项的读者体验质量**（可读性／与后文是否重复／是否兑现承诺）⇒ ❓ 无法判定
5. **全书跨章一致性**：我只抽查了 Carlos–Diana 关系、straightener 复现、Splau/El Prat、monster 主题线、ch03 对 ch01 的引用；**其余 16 章与 ch01 的人物/时间线/称呼一致性未检** ⇒ ❓ 无法判定
6. **整体拼写/语法/标点校对**（`scripts/corruption_scan.py` 本次未跑）⇒ ❓ 无法判定
7. **原文提取质量**（`scripts/verify_corpus.py` 本次未跑；本章 `text/` 为既有语料）⇒ ❓ 无法判定
8. **md 的未提交改动**：另一 agent 正在改写导航／一句话总结／句子结构；本报告行号只对 md5 `e3cb5bff8e140d30fc6d91a70be5ea12` 有效，对方再提交后行号会漂移 ⇒ ❓ 无法判定
9. **「校庆」应改译为「学校演出」还是「圣诞演出」**——最终中文用词属作者风格决定，我不代决 ⇒ ⚠️ 需人判
10. **「罢演」是否保留**——原文只写 `acting out` 与 `The only child not singing`；md:82 已用较克制的「唯一不唱的孩子／她的"表演"」表述，但 :10/:14/:133 用「罢演」⇒ ⚠️ 需人判
11. **总览三篇**（`00_概述.md` 等）是否含本章的同款错误（如「校庆」「粉色脚趾」）——本次**未查** ⇒ ❓ 无法判定
12. **md 尚未被另一 agent 提交前的后续改动**（若导航/一句话总结/句子结构再被改写，:10/:16/:34/:38/:58 的行号与措辞会变）⇒ ❓ 无法判定
13. **原文里 md 未选中的段落**——**本项不适用**：实测 6 条引语覆盖本章**全部正文行**（6/12/15/18/21/27/30）的全部句子，唯一"未覆盖"是页码 `1` 与首句粘连的切分伪影 ⇒ **md 没有略过任何段落**，故无"未选中段落"可漏判；但**引语的段落切分是否保持原书自然段边界**（原文每行是自然段、还是被切分器合并过）本次未核（`text/` 为既有提取件）⇒ ❓ 无法判定
14. **词汇表 22 条的星标分档与词义解释**、**关键词的"分析价值"**、**导航四项的读者体验质量**、**md 之外的本书 16 章与 ch01 的人物/时间线/称呼一致性**、**`corruption_scan.py` 与 `verify_corpus.py` 两个脚本** —— 均未跑/未核，见第 2、3、4、5、6、7 条 ⇒ ❓ 无法判定
