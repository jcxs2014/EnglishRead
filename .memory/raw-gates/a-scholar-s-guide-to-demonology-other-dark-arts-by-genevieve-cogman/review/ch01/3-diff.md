# ch01 R3 对账（漏 / 编 / 错）

语料：`text/ch01_chap1.txt`（2520 字符，37 行，书信体，无叙述段）
素读：`1-suread.json`（7 条事实，7/7 偏移命中）
md：`ch01 prologue.md`（4 块）

## 漏（素读有、md 无）

| 素读事实 | 原文 | 判定 |
|---|---|---|
| 信头地址「Grayne’s School for Girls / North Yorkshire Moors / Yorkshire」 | `text/ch01_chap1.txt:1-7` | **已覆盖**（`ch01 prologue.md:21` 叙事手法写作「北约克郡荒原、约克郡」） |
| 日期 `10th October 2003` | `:10` | **已覆盖**（`:21`） |
| 落款 `Harriet Jagerson` + `Headmistress of Grayne’s School for Girls` | `:34-37` | **已覆盖**（`:10` 写「校长哈丽雅特·贾杰森」） |
| 「若你有这些品质，你在这里会顺利」= 招聘标准清单（positive will to succeed / cheery disposition / willingness to enjoy a joke / understanding of girls / wish to encourage their aspirations） | `:22` | **部分覆盖**：`ch01 prologue.md:17` 只概括为「若你有这些品质，你在这里会顺利」，未点出五项具体品质。**判提示**（不阻断：概括未失实，且这五项在信中确实是并列清单，逐项罗列会淹没段落） |
| 「I’m looking for」= 校长自陈在挑选 | `:22` | **已覆盖**（`:17`「招聘标准」） |

**取舍说明**：本章是纯书信，没有叙事事件；素读 7 条中 6 条（写信人/日期/夸格式/点缺漏/维基/旧生）在 md 中均有对应，1 条（五项品质清单）概括处理，已记录为提示。

## 编（md 有、原文无）

| md 断言 | 位置 | 原文核对 | 档位 |
|---|---|---|---|
| 「后面每出现一次现代事物（维基百科、电邮、外卖），都会与这句形成对照」 | `:31` | 维基百科、电邮都只出现在**本章信里**（`:16` email / `:25` Wikipedia），不是「后面」；全书 `takeaway|delivery|pizza` 只命中 `text/ch15_chapter_fourteen.txt:280` 一处，与「每出现一次…都会对照」不成比例。命令：`/usr/bin/grep -c -i -E "takeaway\|delivery\|pizza" text/*.txt` → 仅 ch15 = 1，其余 0 | **阻断**（无据的全书断言，已改写） |
| 「而开头提到的材料缺失（文书材料与推荐信）正是「苍白管束者」那一类的典型特征」 | `:55` | 原文 `:19` 只写 `certain deficiencies in your paperwork and references`，**从未**把缺材料与「pallid disciplinarian」联系；校长判断芬的依据在 `:22` 明写为 `Your letter speaks of a lifelong interest in Latin…If that is the case, you will fit in here admirably` | **阻断**（因果错置，已改写） |
| 「而芬小姐自己也不知道缺的是哪一项」 | `:45` | 全章只有信件，无芬的任何反应；`/usr/bin/grep -c "Fen" text/ch01_chap1.txt` = 1（仅称呼行 `:13`），无芬的言行 | **提示**（对人物心理的无据推断，已改写为对文本留白的说明） |

## 错（两边都有、但不一致）

| md 写法 | 原文 | 差在哪 | 档位 |
|---|---|---|---|
| 「暗示学校不在维基百科上」 | `:25` `I fear we do not feature on Wikipedia, or other modern sources of information.` | 原文是**明说**（I fear we do not…），不是暗示；同文件 `:99` 已按「自陈」写，两处口径不一 | **提示**（已改为「自陈…等现代资料里」） |
| 「贾杰森——全章唯一出场者」 | 全章无任何场景，只有一封信；贾杰森没有「出场」，只有落款 | 用词与文本形态不符（书信体无出场人物） | **提示**（已改为「唯一发声者」） |
| 块 4 引语从 `Some consider this to be maidenly modesty` 起 | `:25` 前一句是 `many of our alumnae choose not to boast of their antecedents.` | 引语里的 `this` 指代**块外**前一句；中文理解必须写出「许多校友选择不夸耀自己的先辈」才讲得通 ⇒ 分析覆盖的原文比引语长 | **阻断**（截短，已把引语起点前移到 `many of our alumnae choose not to boast of their antecedents.`） |

## 小结

阻断 3（1 编 + 1 编-因果 + 1 截短），提示 3。全部已修，`chapter.sh` 复跑 rc=0。
