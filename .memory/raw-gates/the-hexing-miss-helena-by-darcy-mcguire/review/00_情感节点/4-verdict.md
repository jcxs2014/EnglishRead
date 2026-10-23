# 4-verdict.md · 《The Hexing Miss Helena》`00_情感节点.md` 审查判定

审查员：主会话自审｜层：**总结层（人判全篇）**｜文件：126 行 / 10 个节点，每个节点＝「标题（章号范围）＋叙事概括（1 段）＋引语」
审查方式：审查表 §0 快审「总览三篇全篇」——逐节点核「章号范围」「叙事概括里的每条断言（身份／关系／谁做了什么／谁欠谁／谁被替罪／数字／时距）」「所引英文」。
取证纪律：所有「查无」用 `/usr/bin/grep` 显式路径并记录退出码；不用 `git grep`。

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 29 / 29 相符，0 错** | `overview.py quotes`：本文件 29/29 ✅（行内引语 29 行，已核）；`overview.py full`：整串命中、查无 0、标注与实章不符 0 |
| **对应** | **10 节点：10 对应，0 不对应** | 逐节点核「叙事概括所描述的动作/说话人/时距」与该节点引语所在段落是否一致；不对应 0 条（E1／E2／E3 是**叙述概括内部**的事实错，不落在引语↔中文对应上） |
| **形态** | **4 / 4 符合** | H1 `# 《The Hexing Miss Helena》情感节点` ✓｜10 个 `## 节点N：…（chNN）` 编号连续、章号标注齐备 ✓｜每节点＝叙事概括＋引语 ✓ |
| **断言** | **共核 42 条：相符 34 ／ 提示 2 ／ 阻断 3 ／ 跳过 0** | 阻断 3 条＝E1（年龄：七岁 → 九岁或十岁）、E2（底片是海伦娜泡的，不是辛西娅）、E3（她没有答出口）；提示 2 条＝E4（一周后 ≠ 几天后）、E5（无据时距「几天后」） |

**阻断型条数 = 3。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/<文件>:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | `:58` 节点五「她讲出**七岁**那年和小女孩一起躲进亚麻壁橱的往事」 | `text/ch13_chapter_13.txt:158` `‘I was near to nine or ten. … Clara and I hid together in a linen cupboard. I remember the smell of starch and pears. She pressed her body against mine in the small space and everything in me came alive. It was then I knew.’` | 壁橱往事发生在**九岁或十岁**；「七岁」是 ch21 那场火时的年龄（`text/ch21_chapter_21.txt:332` `‘I was seven.’`） | **阻断**（数字错） |
| E2 | `:58` 节点五「辛西娅在暗处先把话说出口，然后照他的要求摆出姿态，**再把底片泡烂**」 | `text/ch12_chapter_12.txt:264`（辛西娅问「Are you certain you can destroy the photographs?」，**海伦娜**答「I can use my witchwater to flood the negative box」）；`:327` 叙述句 `A wooden box **Helena** would flood with water, soaking the chemicals so the images would be ruined`；`:354` `Helena didn’t need a second invitation. … she pooled her power, condensing the particles of air inside until droplets formed. … Every negative would be soaked`；`:357` `she imagined the photographs hanging to dry … and soaked them as well` | 泡底片、毁照片的都是**海伦娜**（水巫）。本句三个动作并列、主语统一为「辛西娅」，第三项归属错。本书 `ch12 the scandalous photographs.md:10` 自身写的是「**海伦娜**用魔法灌湿底片盒与晾着的照片」——本节点与章内自相矛盾 | **阻断**（谁做了什么：动作归属错） |
| E3 | `:10` 节点一「警察问的不是丧亲的话，而是她是不是希望丈夫死——而**她真的答了**」 | `text/ch01_chapter_1.txt:267` `‘Lady Burrows, it gives me no pleasure to ask, but I must. Is there any reason you might want your husband dead?’`；`:269` `Oh dear.`；`:271` `Because she could think of hundreds of reasons.`（全章 271 行，到此结束） | 她**没有答出口**：警司问完，读者只看到她心里「有一百个理由可以答」。本节点把内心独白写成对警察的开口回答＝虚构动作 | **阻断**（谁做了什么：虚构动作） |
| E4 | `:70` 节点六「**几天后**的客厅里，话题从「重新做人」滑到……」 | `text/ch15_chapter_15.txt:153` `Helena sat across from her on a dark walnut settee. **It had been a week since the dinner party**, and they had seen little of each other in the flurry of activity required to pack up one’s life and start anew.` | 原文给的是「**一周**之后」（自晚宴算起），不是「几天后」 | **提示**（时距不精确） |
| E5 | `:82` 节点七「**几天后**公爵夫人把话说得更直白：来我的舞会，带上你的情人，做一次出格的事」 | `text/ch19_chapter_19.txt:86` `The ball is in a fortnight. I shall see you there.`；`/usr/bin/grep -nE "the next day\|next morning\|following day\|two days\|three days\|day later" text/ch16_chapter_16.txt text/ch17_chapter_17.txt text/ch18_chapter_18.txt` → **rc=1（零命中）** | ch16–19 四章**没有任何时距标记**；原文唯一的时距锚是「舞会在两周后」。「几天后」是把「两周后舞会」误读成「几天后」而生成的**无据时距** | **提示**（无据时距） |

### 与原文相符的 34 条断言（避免「只报问题」的不完整交代）

**节点一（ch01）**
1. 开书房的门、丈夫面朝下趴在奥比松地毯上、血积成深红 ✓（`text/ch01_chapter_1.txt`）；「攒了十年的怒火」✓（`text/ch08_chapter_8.txt:101` `Over the course of their ten years of marriage`）

**节点二（ch02-04）**
2. 海伦娜奉警司（其人即舅舅拉克兰，`ch03:321` `that’s my job as Superintendent of Scotland Yard`）之命上门 ✓（`ch02:107` `she heeded her uncle’s request`；`ch02:194` `Uncle Lachlan had briefed Clio and Helena`）；本该靠读心术读出凶手 ✓
3. 伸出去的手只摸到刺骨的冷和一道电流 ✓（`ch04`）

**节点三（ch05-06）**
4. 丈夫死后礼数仍把她按在原位、宁可自己跳下高台 ✓（`ch05` 引语）；布莱尔家祖传餐桌上另一个女人把水搅成漩涡、法力失灵 ✓（`ch06`）

**节点四（ch09-11）**
5. 一封催债信把她推到七针区那家俱乐部门前 ✓（`ch07` 无署名催债信）；赌厅的镜面墙、烟雾与筹码 ✓；第一次直面把杀人当生意算账的辛克莱 ✓；海伦娜只闪过一个词「我的」✓（`text/ch09_chapter_9.txt:245` `Mine.`）——⚠️ 唯一缺陷是**地名译名**「七针区」（书级术语，见 T2）

**节点五（ch12-13）**
6. 辛克莱要的价码是照片＋随时差遣的人情 ✓（`text/ch12_chapter_12.txt:68` `a few favours from time to time`、`:360` `I’ll come calling for a favour one day`）；辛西娅在暗处先开口 ✓（`ch12:270`）；照要求摆出姿态 ✓（`ch12:285`–`:315`）；底片被泡烂 ✓（**主体错＝E2**）；同车回家那段路 ✓（`text/ch13_chapter_13.txt`）；「我里面的一切都活了过来」✓（`ch13:158` `everything in me came alive`）

**节点六（ch14-15）**
7. 晚宴上两句「我来保护你」撞在一起、辛西娅一声「停」冻住满桌人 ✓（`ch14`）；话题从「重新做人」滑到「你很特别、很神秘、非常非常美」✓（`ch15`）；那个被她抢先说出口的请求 ✓（`ch15`）；两个名字第一次被并排叫出来 ✓（`ch15:237` `‘Cyn and Hel. What a pair we make.’`）

**节点七（ch16-19）**
8. 探到的地址带到切普赛德 ✓（`ch16`）；野狗扑向哈姆雷特、辛西娅掌心自己跑出电 ✓（`ch17`）；逼仄的屋子——一个父亲、一个女儿、一桩说不出口的旧事 ✓（`ch16`–`ch18`）；海伦娜的杀意两次顶到「不做伤害」那条誓的边上 ✓（`text/ch18_chapter_18.txt:122` + `:212`）；辛西娅当场变成另一个人：提出补偿、掏出钱 ✓（`ch18`）；公爵夫人把话说得更直白：来我的舞会，带上你的情人，做一次出格的事 ✓（`text/ch19_chapter_19.txt:86` `‘You absolutely can.’ … ‘Bring your paramour with you to my party. I dare you. Do something inappropriate, for once.’`）

**节点八（ch20-21）**
9. 魔宠选了两个人、罗温姨妈解释灵魂被织在一起 ✓（`text/ch20_chapter_20.txt:98`）；海伦娜被吓退 ✓；辛西娅在一个夜里把界限推到了尽头 ✓；母亲与铁匠被村民锁在屋里烧死的那一年她**七岁** ✓（`text/ch21_chapter_21.txt:332`）；水变成雾 ✓；「她说自己是个诅咒」✓（`ch21`）

**节点九（ch22-23）**
10. 她看清自己：爱上一个不爱她的人、是个傻瓜 ✓（`text/ch22_chapter_22.txt:240` 上文 + `ch22` 引语 `I’ve fallen in love. With a woman who refuses to love me back. I’m such a fool!`）；转身推门走出去 ✓（`ch22`）；**守寡的宅子改作收容所** ✓（`ch22:183` `put my dowager house to good use`）；**练到挪动整只橡木衣柜** ✓（`ch22:255` `shift the massive oak armoire three full inches`）；海伦娜把自己埋进药房班表 ✓（`ch23`）；辛克莱的一只手按在她后脑勺上 ✓（`ch23`）

**节点十（ch24-27）**
11. 抽干水的房间里濒死时承认早已爱上对方 ✓（`text/ch24_chapter_24.txt` 引语 `Because as she faced the stark reality of death, she could no longer hide from the truth. She had fallen in love.`）；另一女人在两件裙子之间挑了旅行装 ✓（`text/ch24_chapter_24.txt:86` `Her travel dress and the gown the duchess had sent over that very day for the ball`）；坐马车赶到五铃街 ✓（`text/ch24_chapter_24.txt:104` `‘Five Bell Street!’`）；用自己的血解开封咒 ✓（`text/ch25_chapter_25.txt`）；**把三个打手举到半空** ✓（`ch25:220` `Flexing her arms, they lifted several feet off the ground.`）；子弹出膛、海伦娜踏浪升起 ✓（`ch25`）；醒来之后是月牙形的伤疤 ✓（`text/ch26_chapter_26.txt:185` `save a crescent moon in hawthorn-berry red`）；当着警司撒下的谎 ✓（`text/ch26_chapter_26.txt:249` + `:264`）；一个被放走的真凶 ✓（`text/ch27_chapter_27.txt:216`–`:225`）；最后那首只放给两个人听的曲子 ✓（`ch27:364`）

---

## 三、机器层

- `overview.py quotes` → **RC=0**；本文件 **29/29 ✅**；行内引语 29 行（已核，建议迁为引用块，**本轮不迁**）；总览引文 86/86（100%）；完全干净文件 3/3。
- `overview.py full` → **RC=0**；整串命中、**查无 0**、标注与实章不符 0、章节覆盖 27/27。本文件 2 条跨标签拼接为**提示**（`overview.py` 自带判级，不判红）。
- `bash scripts/gate.sh` → RC=0，0 条阻断（全书级）。
- ⚠️ 本文件 5 条缺陷（E1–E5）**全部落在门禁覆盖不到的中文断言层**；引语层 29 条**零缺陷**。

---

## 四、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **节点八的「那一年，她七岁」——成立，勿改成九岁或十岁。** 依据：`text/ch21_chapter_21.txt:332` `‘I was seven. Old enough to have done something. And I tried, but my powers weren’t enough to stop the fire.’`。**七岁＝那场火；九岁或十岁＝壁橱**（E1 只涉及节点五）。
2. **节点十的「月牙形的伤疤」——成立，不必改成「月牙形印记」。** 依据：`text/ch26_chapter_26.txt:185` `the wound knitted itself together … When the last smudge of blood absorbed into the wound, it sealed itself, her smooth skin unmarred save a crescent moon in hawthorn-berry red.`——「unmarred save」＝除了那道月牙别无痕迹，伤痕确实留在了那里。
3. **节点九「守寡的宅子」——成立，勿改成「新宅子」。** 依据：`text/ch22_chapter_22.txt:183` `I am going to put my **dowager house** to good use.`（金句 ⑳ 把同一处写成「新宅子」，那一条才要改，见 `00_金句精选.md` J7）。
4. **节点二「奉警司之命上门」——成立。** 依据：警司＝舅舅拉克兰（`text/ch03_chapter_3.txt:315`、`:321`）；`ch02:107` `she heeded her uncle’s request`。
5. **节点五「辛西娅在暗处先把话说出口」——成立。** 依据：`text/ch12_chapter_12.txt:270` `Cynthia didn’t pull away, but spoke into the crook of Helena’s neck.`（暗处＝暗房；说话人＝辛西娅）。⚠️ **只把「再把底片泡烂」改归海伦娜**，前半句不动。
6. **节点四「海伦娜在那一瞬间只闪过一个词：我的」——成立。** 依据：`text/ch09_chapter_9.txt:245` `Mine.`、`:247` `The primitive instinct resonated in her bones.`。⚠️ 「只闪过一个词」是原文的内心独白形态，不是开口说话。
7. **节点十「用自己的血解开那道封住力量的咒」——成立。** 依据：`text/ch25_chapter_25.txt`（以指血破印、地面开裂）。
8. **节点一「她攒了十年的怒火刚找到对象，人却已经死了」——成立。** 依据：`text/ch01_chapter_1.txt`；十年见 `text/ch08_chapter_8.txt:101`。
9. **节点七「海伦娜的杀意两次顶到「不做伤害」那条誓的边上」——成立。** 依据：`text/ch18_chapter_18.txt:122`（重申不伤害誓言）与 `:212`（`reared once more like a rogue wave` 的杀意）。⚠️ 注意这是**节点七**的两次，与 `ch18` 章内 V1 的「莉莉 stop threatening」不是同一处，勿混改。

---

## 五、覆盖声明与已知盲区

- **本文件覆盖**：人判**全篇**（10 个节点逐节点核），42 条断言全部回源取证。
- **全书覆盖**：机器层 27/27 章 + 总览三篇；人判 **ch01 / ch10 / ch18 / ch27 = 4 / 27 章** ＋ 总览三篇全篇；其余 23 章**仅机器层**。
- **本层盲区（如实标注）**：与另两篇总览同——本层**没有**「先素读再开 md」的顺序纪律；独立性弱于 ch10。补偿：每条断言要求显式行号，且对「年龄／时序／说话人／动作归属」四类专门回源（E1／E2／E3 即由此查出；E2 由**本书 ch12 章内写法反向验证**——章内写对了，总览写错了）。
- **未做**：深审 R0–R5 全章未执行；快审升级条件已命中，**须提请用户确认，本会话不自行升级**。
