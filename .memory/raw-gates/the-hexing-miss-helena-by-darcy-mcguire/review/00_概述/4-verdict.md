# 4-verdict.md · 《The Hexing Miss Helena》`00_概述.md` 审查判定

审查员：主会话自审｜层：**总结层（人判全篇）**｜文件：72 行 / 11 段梗概 + 3 个主题 + 4 条人物弧光
审查方式：按审查表 §0 快审「总结层 全读」——六类逐句过（身份 / 关系 / 谁做了什么 / 谁欠谁 / 谁被替罪 / 数字），每条回 `text/` 找到支撑行；不许用「读起来对不对」代替清单。
取证纪律：所有「查无」用 `/usr/bin/grep` 显式路径并记录退出码；未使用 `git grep`（`text/` 被 `.gitignore` 排除，其退出码 1 与「真查无」不可区分）。

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 22 / 22 相符，0 错** | `overview.py quotes`：本文件 22/22 ✅；`overview.py full`：整串命中 22、查无 0、标注与实章不符 0 |
| **对应** | **0 块中文理解型引语块（概述用行内引语体）**；行内英文逐字 29 行全部命中 | 概述层不承担「块级中文理解」对应检查；对应类检查落在 `00_金句精选.md` / `00_情感节点.md` 与章内 |
| **形态** | **3 / 3 符合** | H1 `# 《The Hexing Miss Helena》概述` ✓｜三个一级小节（全书梗概 / 三个主题 / 人物弧光）齐备 ✓｜人物弧光 4 人（辛西娅 / 海伦娜 / 希金斯太太 / 哈姆雷特）各带起点/转折/落点 ✓ |
| **断言** | **共核 51 条：相符 45 ／ 提示 5 ／ 阻断 1 ／ 跳过 0** | 阻断 1 条＝O1（底片是海伦娜泡烂的，概述写成辛西娅）；提示 5 条＝O2（指代含混）＋O3（假设语气被写成承认）＋O4／O5（书级术语） |

**阻断型条数 = 1。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/<文件>:行`） | 结论 | 档位 |
|---|---|---|---|---|
| O1 | `:18` 「**她**当场毁掉了底片，也把自己交到了这个人手里」（上句主语为辛西娅） | `text/ch12_chapter_12.txt:354` `Helena didn’t need a second invitation. She took Cynthia’s hand, and they hurried to the door. Looking behind her at the box, she pooled her power, condensing the particles of air inside until droplets formed. … Every negative would be soaked; the images … were irrevocably ruined.`；`:357` `With a flick of her gaze, she imagined the photographs hanging to dry in the makeshift darkroom and soaked them as well`；`:264`（辛西娅问「Are you certain you can destroy the photographs?」，**海伦娜**答「I can use my witchwater to flood the negative box」）；`:327` 叙述句 `A wooden box **Helena** would flood with water` | 泡底片与毁照片的都是**海伦娜**（水巫），不是辛西娅。本书自己的 `ch12 the scandalous photographs.md:10` 写的就是「**海伦娜**用魔法灌湿底片盒与晾着的照片」——概述与章内自相矛盾 | **阻断**（谁做了什么：动作归属错） |
| O2 | `:18` 「再加上一根随时能勒住**她**叔叔的绳」 | `text/ch12_chapter_12.txt:68` `As long as you grant me a few favours from time to time. Like putting a leash on that dog you call an uncle, **Miss Blair**. I grow weary of ’im sniffing around my territory.`；`:162` `You ’ave no options. And neither will your uncle. Soon.`；`:360` `Take a message to your uncle, **Miss Blair**.` | 这句是辛克莱对**海伦娜**（Miss Blair）说的，勒住的是拉克兰舅舅（`text/ch03_chapter_3.txt:315` `Uncle Lachlan`；`:321` `that’s my job as Superintendent of Scotland Yard`）。概述句中「她」紧接「辛西娅给出的回答」，读作辛西娅的叔叔＝歧义；建议明确 | **提示**（指代含混） |
| O3 | `:10` 「**十年里她唯一敢承认的**那点快意，就藏在这句里」 | `text/ch01_chapter_1.txt` 全章 271 行，末两行 `:269` `Oh dear.`、`:271` `Because she could think of hundreds of reasons.`；概述所引为叙述者句 `If she did feel a breath of liberation at his demise, it was only because …` | 原文是叙述者的**假设语气**（If she did feel），不是辛西娅的「承认」；「敢承认」把条件句坐实为自陈 | **提示**（语气确认化；同一簇见 `00_金句精选.md` J4、`00_情感节点.md` E3） |
| O4 | `:12` 「休伯特生前欠下**七针区**那位“魔鬼”的债」 | `text/ch07_chapter_7.txt:360` `He lost me in the Seven Dials.`；`text/ch08_chapter_8.txt:41` `‘The Devil of Seven Dials. Damien Sinclair.’`；`text/ch26_chapter_26.txt:247` `a housekeeper from Seven Dials had murdered a marquess from Mayfair` | 同一地名全书两译：本书主流作「七铃区」（`ch23:10/100/151`、`ch24:53/190`、`ch25:23`、`ch26:89` 共 7 处），本行与 `00_情感节点.md:46` 作「七针区」 | **提示**（书级术语统一） |
| O5 | `:44` 「辛西娅·布尔洛斯（**肯特米尔**侯爵夫人）」 | `text/ch01_chapter_1.txt:137` `Superintendent Lachlan MacDougal`（舅舅全名）；头衔见 `text/ch10_chapter_10.txt:140` `I am the Marchioness of Kentmore.`、`text/ch27_chapter_27.txt:231` `My last act as Marchioness of Kentmore` | 同一头衔两种译名：本书主流作「肯特莫尔」（`ch02:10`、`ch11:20`、`ch27:10`），本行与 `ch10:11` 作「肯特米尔」 | **提示**（书级术语统一） |

### 与原文相符的 45 条断言（避免「只报问题」的不完整交代）

**A. 全书梗概 11 段**
1. `:10` 尸体面朝下趴在奥比松地毯、血积成深红 ✓（`ch01`）；警司拉克兰·麦克杜格尔当场在书房 ✓（`ch01:137` 全名、`ch03:321` 警司）；「攒了十年的怒火」✓（`text/ch08_chapter_8.txt:101` `Over the course of their ten years of marriage`）；问的是「你会不会希望你丈夫死」✓（`ch01:267`）
2. `:12` 债主是辛克莱、催债信措辞狠 ✓（`ch07` 无署名催债信）；引语 ch11 ✓；**真凶是家里端茶倒水的女管家** ✓（`text/ch26_chapter_26.txt:247` `a housekeeper from Seven Dials had murdered a marquess from Mayfair`）
3. `:14` 「奉警司之命上门」✓——**该警司就是她们的舅舅拉克兰**（`ch02:107` `she heeded her uncle’s request`；`ch02:83` 克莱奥本被派去问鬼；`ch02:194` `Uncle Lachlan had briefed Clio and Helena`）；引语 ch04 ✓
4. `:16` ch05 引语 ✓；「守寡第一夜」✓
5. `:18` 辛克莱要的是照片＋随时差遣的人情 ✓（`ch12:68` `a few favours from time to time`、`:360` `I’ll come calling for a favour one day`）；「辛西娅给出的回答是「我唯一怕的是自己的欲望」」✓——**该句说话人确为辛西娅**（`ch12:270` `Cynthia didn’t pull away, but spoke into the crook of Helena’s neck. ‘I don’t find your attraction to women twisted in the slightest…’ She stepped back. Helena ached at the loss of her warmth.`）
6. `:20` 地址由希金斯太太给 ✓（`ch16:62` 引语）；狗扑哈姆雷特、辛西娅掌心放电 ✓（`ch17` 引语）；「在此之前她以为自己只是个被封住力量的普通人」✓（`ch25` 血咒解封前）
7. `:22` 哈姆雷特选两个女主人、灵魂交织 ✓（`ch20:98` 引语）
8. `:24` 「海伦娜**七岁**那年，母亲与铁匠被村民锁在屋里烧死」✓（`text/ch21_chapter_21.txt:332` `‘I was seven. Old enough to have done something. And I tried, but my powers weren’t enough to stop the fire.’`）
9. `:26` ch22 引语 ✓；**守寡的宅子改作收容所** ✓（`text/ch22_chapter_22.txt:183` `I am going to put my dowager house to good use. I am turning it into a home for women in need.`）；**练到挪动整只橡木衣柜** ✓（`ch22:255` `she was able to shift the massive oak armoire three full inches`）
10. `:28` ch23 引语 ✓；**三个打手举到半空** ✓（`text/ch25_chapter_25.txt:220` `One man had his hand on his gun, another’s eyes were bulging … The third man’s mouth was open on a silent scream. Flexing her arms, they lifted several feet off the ground.`）
11. `:30` **当着警司的面撒谎** ✓（`text/ch26_chapter_26.txt:249` `‘Hubert killed himself.’` → `:261`–`:264` `‘That is the truth, Superintendent MacDougal. He tried to murder me, but he didn’t murder my husband.’`）；ch27 誓词 ✓

**B. 三个主题 3 条**
12. `:34` 不伤害誓言 ✓（`ch18:122`）；母亲为留住铁匠做爱情药水、并破了布莱尔女巫的誓 ✓（`text/ch21_chapter_21.txt:278` `…those love spells violated the oath she made. The oath of all the Blair witches. To do no harm.`）；**海伦娜另立私人誓言永不坠入爱河** ✓（`text/ch16_chapter_16.txt:176` `Helena made another oath. A private promise to never fall in love with another.`）
13. `:36` ch03 空读心 ✓；「说出欲望／母亲的火／我是诅咒／新的誓词」✓（`ch12`／`ch21`／`ch22`／`ch27`）
14. `:39`–`:40` ch22、ch27 两处引语 ✓

**C. 人物弧光 4 人 × 起点/转向/最低点/落点**
15. `:46`–`:49` 辛西娅 起点 ch01 ✓／转向 ch05 ✓／最低点 ch22 ✓／落点 ch27 ✓
16. `:54`–`:57` 海伦娜 起点 ch02 ✓／转向 ch18 ✓／最低点 ch24 ✓／落点 ch27 ✓
17. `:62`–`:64` 希金斯太太 起点 ch16 ✓（`‘It was my doing that got Lily here in the first place.’`）／中段 ch26 ✓（`ch26:311` `She caught him strangling one of the poor girls…`）／落点 ch27 ✓；`:65`「她杀人不为利，只为让那个掐住女仆脖子的手停下来」✓（`ch26` 同一事件）
18. `:69`–`:71` 哈姆雷特 起点 ch02 ✓／转折 ch20 ✓／落点 ch27 ✓；`:72`「起手他只属于海伦娜一个人……结尾处他仍在放哨」✓（`ch02` 归属 + `ch27:364` `as Hamlet stood sentinel`）

**D. 数字与专名**
19. `:10` 十年 ✓｜`:24` 七岁 ✓｜`:26` 橡木衣柜 ✓｜`:28` 三个打手 ✓｜`:44` 侯爵夫人 ✓｜`:54` 克莱奥是她的表亲 ✓（`ch02:83` `Clio was a firewitch…`；`ch03:315` `this is my sister` 指向克莱奥与托马斯是兄妹）

---

## 三、机器层

- `python3 scripts/overview.py quotes "<书目录>"` → **RC=0**；`00_概述.md` 行内引语 29 行（已核，建议迁为 `> "…"（chNN）` 引用块）；引语块 **22/22 ✅**；总览引文 **86/86 可核实（100%）**；完全干净文件 3/3；已核覆盖 3/3 篇。
- `python3 scripts/overview.py full "<书目录>" "<epub>"` → **RC=0**；整串命中 **99**｜🔶 拼接 **7**｜❌ 查无 **0**；章节标签对 99、标注与实章不符 **0**；章节覆盖 **27/27 章，未被任何总览引语提到 0 章**。本文件 2 条跨标签拼接为**提示**（`overview.py` 自带判级，不判红）。
- `bash scripts/gate.sh "<书目录>"` → **RC=0，0 条阻断**（全书级，结论见 `2-machine.json`）。
- ⚠️ **总览层的中文事件断言没有任何门禁覆盖**——`gate.sh` / `overview.py` 只核引语逐字与标签，核不了「谁做了什么／几岁／第几章」。本文件 5 条缺陷全部来自人判，**门禁全绿 ≠ 本层干净**。

---

## 四、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「警司拉克兰·麦克杜格尔」——成立，不要拆名也不要改名。** 依据：`text/ch01_chapter_1.txt:137` `Superintendent Lachlan MacDougal`；`text/ch03_chapter_3.txt:315` `Uncle Lachlan`；`:321` `that’s my job as Superintendent of Scotland Yard`。**拉克兰·麦克杜格尔是同一个人**：既是海伦娜／克莱奥／托马斯的舅舅，也是苏格兰场警司。
2. **「布莱尔家的海伦娜奉警司之命上门」——成立，不要改成「奉舅舅之命」。** 依据：`ch02:107` `she heeded her uncle’s request`；`ch02:194` `Uncle Lachlan had briefed Clio and Helena the moment they arrived.`。原文的「请求者」就是那位警司舅舅；本层与 `00_情感节点.md` 节点二写法与原文一致。
3. **「辛西娅给出的回答是「我唯一怕的是自己的欲望」」——成立，勿因「通常这类话出自海伦娜」而改成海伦娜。** 依据：`text/ch12_chapter_12.txt:270` `Cynthia didn’t pull away, but spoke into the crook of Helena’s neck. ‘I don’t find your attraction to women twisted in the slightest. And the only desires I fear are my own. I’ve never wanted anyone the way I want you.’ She stepped back. Helena ached at the loss of her warmth.`——**说话人是辛西娅**（她把话说到海伦娜颈窝里，随后是她退开、海伦娜失落）。同一段英文在 `00_金句精选.md` ⑦（`:73`）也出现，那一处**未指名说话人**，同样不构成错误。
4. **「海伦娜七岁那年，母亲与铁匠被村民锁在屋里烧死」——成立。** 依据：`text/ch21_chapter_21.txt:332` `‘I was seven. …’`。⚠️ **七岁是「那场火」时的年龄，不是「亚麻壁橱」时的年龄**（壁橱是九岁或十岁，见 `00_金句精选.md` J1／`00_情感节点.md` E1）。
5. **「真凶不是流窜在外的陌生人——她一直在这个家里，端茶倒水」——成立。** 依据：`text/ch26_chapter_26.txt:247` `a housekeeper from Seven Dials had murdered a marquess from Mayfair`。
6. **「把三个打手举到了半空」——成立，不必改成「三人」。** 依据：`text/ch25_chapter_25.txt:220`（一、二、三三人分述，`Flexing her arms, they lifted several feet off the ground.`）。
7. **「她把守寡的宅子改成收容需要帮助的女人的地方」——成立。** 依据：`text/ch22_chapter_22.txt:183` `put my dowager house to good use`；`:201` 公爵夫人支持。注意原文是 **dowager house（守寡宅）**，不是「新宅子」。
8. **「把力量练到能挪动一整只橡木衣柜」——成立。** 依据：`text/ch22_chapter_22.txt:255` `shift the massive oak armoire three full inches`。
9. **「当着警司的面撒了一个谎，把真凶从绞架上护了下来」——成立。** 依据：`text/ch26_chapter_26.txt:249` + `:261`–`:264`（辛西娅当面向 MacDougal 说休伯特是自杀）；放走希金斯太太见 `text/ch27_chapter_27.txt:216`–`:225`。
10. **「海伦娜自己又加了一道更重的誓——永远不要爱上任何人」——成立。** 依据：`text/ch16_chapter_16.txt:176` `A private promise to never fall in love with another.`；`:180` 附近 `text/ch20_chapter_20.txt:98` `Her promise to never fall in love.`；`text/ch26_chapter_26.txt:44` `Breaking her oath to never fall in love had nearly destroyed Helena.`
11. **「那晚她攒了十年的怒火刚找到对象，人却已经死了」——成立。** 依据：`text/ch01_chapter_1.txt`（尸体与怒火的叙述）；十年见 `text/ch08_chapter_8.txt:101`。
12. **本文件行内引语体（29 行）不判红。** `overview.py quotes` 明示「已核，但建议迁为 `> "…"（chNN）` 引用块」——是体裁建议，不是缺陷；**不要在本轮为了迁体裁而重排本文件**（会动到 22 处已核引语）。

---

## 五、覆盖声明与已知盲区

- **本文件覆盖**：人判**全篇**（72 行 / 11 段梗概 + 3 主题 + 4 人物弧光），六类逐句过，51 条断言全部回源取证。
- **全书覆盖**：机器层 27/27 章 + 总览三篇；人判 **ch01 / ch10 / ch18 / ch27 = 4 / 27 章** ＋ 总览三篇全篇；其余 23 章**仅机器层**。
- **本层盲区（如实标注）**：总览三篇**没有**章内那套「先素读 text/ 再开 md」的顺序纪律——它们的形态就是「先读 md 再回源核」，故**独立性弱于** ch10（ch10 的 `text/` 写作期未读过）。补偿手段：本层每条断言都要求**显式行号证据**，且对「人物/动作归属」「年龄」「时序」三类专门回源复核（O1 即由此查出）。
- **未做**：深审 R0–R5 全章未执行；快审升级条件已命中（见总指令文件首段），**须提请用户确认，本会话不自行升级**。
