# ch15 审查判定（R3 独立审查员，第三轮）

- 对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch15 callie hunts for a pregnancy test.md`
- 语料：`text/ch15_15.txt`（6955 字符 / 232 行）
- 机器层：`bash scripts/chapter.sh "<md>" --json` → **verdict ok，退出码 0**（引语逐字 segment_miss=0、struct_bad=0、empty_quote=0、keyword_bad=0、cjk_low=0）。
- ⚠️ **机器全绿不等于没缺陷**：本轮 4 条阻断中 3 条机器层结构上查不出（施事反转 / 归属写反 / 断言越界），只有逐块三问能看见。
- 分部（书里真名）：**MONDAY**（epub `OPS/TOC.xhtml`：十二分部 A FRIDAY IN MAY / SATURDAY / SUNDAY / MONDAY / TUESDAY / WEDNESDAY / THURSDAY / FRIDAY / SATURDAY / MONDAY / TUESDAY / SIX WEEKS LATER；第一个 MONDAY 覆盖 11–15 章 ⇒ ch15 ∈ MONDAY）。

---

## 一、四组数（只报这四组）

| 组 | 分母 | 阻断 | 提示 | 假红 | 跳过 | 说明 |
|---|---|---|---|---|---|---|
| **逐字** | 7 块 / 7 段引语 | 0 | 0 | 0 | 0 | 7/7 与原文逐字一致（机器 segment_miss=0 复核）；另抽查词汇表 30 行例句，30/30 逐字命中原文 |
| **对应** | 7 块 | **1** | 5 | 0 | 0 | 对应成立 7/7；阻断＝原句 6 施事写反 |
| **形态** | 4 项（H1 / 导航 / 子项 / 块数）+1 项分部标注 | 0 | 1 | 0 | 0 | 四项全部合全书众数；仅「分部 MONDAY 未标注」为提示 |
| **断言** | 全章（7 块分析 + 导航 5 项 + 一句话总结 + 词汇表） | **3** | 4 | 0 | 0 | 3 条阻断：castless 绝育断言 / 唱片公司老板 Eulalia / 货架线「只可能」 |

**合计：阻断 4 条（对应 1 + 断言 3），提示 9 条，假红 0，跳过 0。**

---

## 二、形态组明细

| 形态项 | 本章实测 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `15. Caius and Callie’s Flat` | 54/54 章均为 `NN. 标题`（ch53 同样用 `53. Caius and Callie’s Flat`）；源文行 17 小标题一致 | 无 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | **54/54 章完全同名同序，项数恒为 5** | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | profile `mystery-thriller` 的 profile_subitems 同集（optional：句子结构，未用，可选） | 无 |
| 块数 | 7 | 全书众数 7（block_median 7.0，range 5–10） | 无 |
| **分部标注** | **全章未出现 MONDAY / 任何分部名** | 24/54 章在导航里标注所属分部（如 ch13 同属 MONDAY，写「把这一章扣回分部 MONDAY 的周一」；ch22/ch24 写「本章属「WEDNESDAY」这一分部」） | **偏离（提示）**：ch15 漏标所属分部 MONDAY。理由：非全书强制（30/54 章同样不标），但同分部的前一章 ch13 已标，属可选补齐项；须用书里真名 MONDAY，不得写成 A FRIDAY IN MAY 等 |

---

## 三、断言清单

| # | 断言（md 位置与原文） | 证据（章:区间 / 行） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 原句 1 中文理解「庆祝自己「不再有生育能力」——**这个词说明他那边已经做过不可逆的处理**」；词汇表「castless｜不育的；被阉割的（**此处指做过绝育手术**）」 | `text/ch15_15.txt:20`（区间 [46,336)）：`‘Let’s celebrate me being castless. …’`——原文只给了一个玩笑词，无任何绝育叙述；全书 grep `castless` 仅此一处（`/usr/bin/grep -n -i "castless\|vasect\|steril" text/*.txt` → 仅 ch15:20，退出码 0）；反证 `text/ch53_53.txt:74`：`‘We’ve had the date for the twelve-week scan come through.’`、`text/ch54_54.txt:71`：`‘I’m very sorry, Miss Foster. There’s no heartbeat.’`（孩子是凯厄斯的，故「已做不可逆绝育」与全书冲突） | 原文无据 + 后文证否；且该断言是本块「反讽框架」（他那边越轻松、风险只在她一侧）的地基 | **阻断** |
| 2 | 导航「一句话概括」：「卡莉被**唱片公司老板 Eulalia** 的活儿逼得心力交瘀」 | `text/ch15_15.txt:53`（区间 [905,1309)）：`‘She’s basically using me to go over her record label’s head.’`——Eulalia 是被**她自己的**唱片公司管着的艺人，Callie 做的活是要**绕过唱片公司**（跨过 record label 的头）；另 `text/ch12_12.txt:170`：`‘…so that then the label will be forced to go along with what I want…’`；`text/ch23_23.txt:340`：`‘The label and PCQV are both aware…’`（唱片公司与 PCQV 是两个实体） | 归属写反：Eulalia 不是唱片公司老板，恰恰是被唱片公司压着的那一方 | **阻断** |
| 3 | 导航「线索结构」：「货架线（验孕试纸不在架上，**只可能被收银员挪到柜台后面**）」 | `text/ch15_15.txt:165`（区间 [5043,5101)）：`‘They’re probably behind the till. They get nicked a lot.’`——Caius 的**猜测**（probably / 被偷），且后文 `text/ch15_15.txt:201`（区间 [5986,6141)）：`‘Sure.’ The sales assistant took one down from the shelf, scanned it and placed it on the counter.`——验孕棒**是从货架上取下的**，并未在柜台后面 | 把猜测写成唯一事实，且与同章后文直接冲突 | **阻断** |
| 4 | 导航「视角」：「第三人称限知，**以凯厄斯的观察为主**，叙述**不时**切进卡莉的内心（她不肯说 Eulalia 长得像婴儿天使；她明知维生素与真正的问题无关）」 | 自由间接叙述几乎全在卡莉一侧：`text/ch15_15.txt:77`（区间 [2912,3306)）`‘Callie wasn’t going to describe her. She wasn’t going to say that she looked like a baby angel. Caius didn’t need to know that.’`；`:59`（区间 [1508,1628)）`Callie was kicking herself.`；`:186`（区间 [5510,5623)）`aware that the vitamins were tangential to the real question`；`:192`（区间 [5648,5713)）`She just needed to hear him say it.`；凯厄斯只一处内心：`:20`（区间 [46,336)）`He fancied one of their aubergine and San Marzano tomato ones.` | 视角中心归属写反（md 自己举的两个例子也都是卡莉的内心）；若作者原意指「外部场面」而非叙述视角，可降为提示 | **阻断**（可降为提示，按作者本意定） |
| 5 | 导航「一句话概括」：**「卡莉被唱片公司老板 Eulalia 的活儿逼得心力交瘀」**＋本章把「the TV thing」这条线完全略去 | `text/ch15_15.txt:107`（区间 [3886,4028)）：`‘I’m late. I think I was so stressed worrying about the TV thing going wrong and then it did…’`；同章 `text/ch15_15.txt:44`：`‘I thought it went well at the time…’`（Eulalia 会议「当时顺利」） | 原文里卡莉的压力源被写作「the TV thing」（一条本章未交代的另一条线），且**结果是真的砸了**；Eulalia 会议反而「当时顺利」。md 用 Eulalia 的活儿顶替了 TV thing，把两条线并成一条 | **提示**（合并两条线，未直接写反） |
| 6 | 一句话总结：「卡莉在工作的重压里**又等到一条消息**——皮下埋植避孕药三个月前就到期了，而她**偏偏是在超市找不到验孕棒时才被迫面对它**」 | `text/ch15_15.txt:119`（区间 [4142,4293)）：`Callie took her handbag from the table and fished out her purse, finding the card with details of her contraceptive implant. ‘Shit.’`；`:125`（区间 [4306,4336)）：`‘It ran out three months ago.’` | 她**没有收到任何消息**，是自己在公寓里翻卡片发现到期；发现/面对的时点是公寓，不是超市（超市才是行动点） | **提示**（时序与「消息」措辞） |
| 7 | 原句 3 中文理解：「她做过避孕——**就是皮下埋植的那一种**」 | `text/ch15_15.txt:113`（区间 [4049,4094)）：`‘Pregnant? No, I can’t be. I’m baby-proofed.’`——本句未指明避孕方式；埋植剂出现在下一轮 `text/ch15_15.txt:119`：`‘Yeah, Nexplanon.’` | 把引语外内容（下一轮的答案）前置进本块 | **提示** |
| 8 | 原句 5 为什么这样写：「连凯厄斯也只好猜试纸是不是**被收银员挪到**了柜台后面」 | `text/ch15_15.txt:165`：`‘They’re probably behind the till. They get nicked a lot.’`——nicked＝被人偷走，挪货者不是收银员 | 施事补写（与第 3 条同源，本块尚标「猜」，故为提示；导航升级成断言即为阻断） | **提示** |
| 9 | 原句 7：`**结完账往外走**`；`**二十支**「Marlboro Lights」` | `text/ch15_15.txt:231`（区间 [6876,6954)）末句；`:225`（区间 [6730,6800)）`‘You’re going to kill me,’ Caius said, tapping his card on the reader.`（仍在收银台前，原文无「往外走」）；`:213`（区间 [6297,6469)）`‘Oh, and twenty Marlboro Lights and a bottle of your strongest whisky as well, please,’`——twenty Marlboro Lights ＝ 二十包/条成品烟，非二十根 | 舞台动作原文没有；数量单位写错 | **提示** |
| 10 | 原句 2：「她解释**这一晚**自己一直紧绷着」；原句 4：「她从手袋里翻出钱包」（略去「从桌上拿起手袋」） | `text/ch15_15.txt:107`（过去时 `I think I was so stressed worrying…`，原文未锚定「这一晚」）；`text/ch15_15.txt:119`：`Callie took her handbag from the table and fished out her purse…` | 措辞/微节添加 | **提示** |
| 11 | 全章**未标注所属分部** | 同上「形态组」明细；`text/` 无分部标记，epub `OPS/TOC.xhtml` 显示 ch15 ∈ MONDAY | 漏标可选信息（24/54 章有标，同分部 ch13 有标） | **提示** |

---

## 四、对应组明细（原句 6 的阻断）

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| md 原句 6 中文理解：「**她在维生素区看到**一盒印着挺胸孕肚的金发女郎的孕期维生素，**问凯厄斯要不要买一包**」 | 原文 `text/ch15_15.txt:171`（区间 [5121,5366)）：`‘… Caius **glanced over to the adjacent vitamin aisle and spotted** a box with a toothy blonde smiling while holding her bump. ‘**Do you want a pack of those?**’`；`text/ch15_15.txt:174`（区间 [5369,5390)）：`‘Pregnancy vitamins?’`（Callie 的复述）；`text/ch15_15.txt:186`（区间 [5510,5623)）：`‘Do you want me to get the vitamins?’ Callie asked…` | **发现者与首个提问者都是 Caius**，md 双双安到 Callie 头上，并把 Caius 的 "Do you want a pack of those?" 复述成 Callie 的问句 —— 施事/归属反转（机器四探针查不出） | **阻断** |

---

## 五、待核问题（本章指定四问）的原文答案

1. **超市收银台前到底买了什么、验孕棒买到没有**：**买到了**。`text:198` Callie 放下维生素、店员扫描；`text:201` 店员从**货架**取下一盒验孕棒、扫描、放到柜台，Callie「slipped **both items** into her bag」（both ＝ 维生素 + 验孕棒）。**安全套没成交**（`text:204` Caius 要了，`text:210` 他自己收回："Never mind… The horse has bolted."）；**香烟与威士忌也没买**（`text:213` Callie 要了，`text:219` 店员转身去拿时她改口 "I'm only joking"）。⇒ md 只在块 7 提了荒唐加单，未提「验孕棒确实买到」；无错。
2. **避孕怎么说、数字是否逐字**：原话 `text:113` `‘Pregnant? No, I can’t be. I’m baby-proofed.’`；`text:116` Caius 问 `‘You’ve still got that thing in your arm?’`；`text:119` `‘Yeah, Nexplanon.’` + 翻出植入物卡片 + `‘Shit.’`；`text:125` `‘It ran out three months ago.’` ⇒「**three months ago**」逐字，指**三个月前就已失效**（不是「三个月有效期」，也不是「三个月前开始用」）。md 写「埋植药三个月前就到期了」✓ 逐字相符。
3. **降格成玩笑的动作与原话**：收银台前 Callie 先 `text:198` `‘Please may I have a pregnancy test?’`，随后 `text:213` `‘Oh, and twenty Marlboro Lights and a bottle of your strongest whisky as well, please,’`（店员 `tried to not be judgy but froze at the combination`），Caius 问 `text:216` `‘What?’`，她改口 `text:219` `‘I’m only joking,’ … She took out her Nectar card hurriedly. ‘Sorry, I thought I was being funny.’` ⇒ md 块 7 抓到了「荒唐加单」，但把 twenty Marlboro Lights 写成「二十**支**」。
4. **导航与总结的概括**：
   - 与原文一致 ✓：工作线（视觉企划 / 没谈成的费用 / 待签合同，`text:53/59/65`）、身体线（Nexplanon 三个月前到期，`text:119/125`）、人物弧线（`text:44/53` → `text:113` → `text:213/219`）、卡莉的自我缩小与凯厄斯的「it'll be fine」→「炸饭团 + Amex」（`text:140` → `text:231`）。
   - 与原文冲突 ✗：导航「唱片公司老板 Eulalia」（应为：欧拉莉亚是**被自己的唱片公司**管着的艺人）、导航「只可能被收银员挪到柜台后面」（应：店员**从货架**取下）、导航「以凯厄斯的观察为主」（应：叙述中心在卡莉）、导航漏标分部 MONDAY。

---

## 六、取证命令（可复跑）

```
/usr/bin/grep -n -i "castless\|vasect\|steril\|snipped" text/*.txt
  → 仅 text/ch15_15.txt:20（退出码 0）

/usr/bin/grep -n -w -i "TV" text/ch2*.txt text/ch3*.txt
  → ch31:89、ch32:155（ch15 的 "the TV thing" 在全书没有其他落点；本书内无第二处 TV 指涉可对应）

python3 逐行核对词汇表 30 行例句 → verbatim-miss = 0
```

**未核**：全书 54 章的 md 形态一致性只做了 ch15 与全书导航项名/项数、块数众数的统计比对，未逐章人工核对文字；ch15 的「本章词汇」三档星级划分是否合全书体例未查（档位：跳过）。
