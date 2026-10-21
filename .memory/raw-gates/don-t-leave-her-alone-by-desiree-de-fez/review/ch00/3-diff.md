# ch00 三张单子（漏 / 编 / 错）

> 复核轮 2026-10-21 ｜ 对照对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch00 prologue.md`
> 证据基准：`text/ch00_prologue.txt`（1,958 字符，6 个自然段）｜机器层：`2-machine.json`（verdict=ok，7/7 引语逐字命中，位置 31<313<585<771<1219<1608<1873）

## 原文要点（供对账，左＝原文逐字，右＝md 说法）

| 原文（text/ch00_prologue.txt） | md 说法 | 判定 |
|---|---|---|
| P2 "She came to in the dark, sprawled across the floor. The light returned in phases, as if someone were rhythmically flipping the switches, and soon the whole store was lit up. The brightness was like a kick to the face. She lay back down, closed her eyes, and stayed that way awhile." | 块1 引语＝前 2 句；导航 人物弧线「闭眼躺回」 | ✅ 对应 |
| P3 "An image arose in her mind: the last time she’d been here, with Brigitte, trying on plastic tiaras. … her little voice begging to buy half the store … was replaced by an unpleasant ringing." | 块2 引语＝整段 | ✅ 对应 |
| P4 "rows of tutus splattered with red, red-stained butterfly wings and plush earmuffs." | 块3 引语＝P4 前 2 句 | ✅ 对应（"被血染红"是对 red-stained 的合理推论，同段下一句即 "dried blood"） |
| P4 "The wings she and Brigitte would try on for selfies, the bear-shaped backpacks, the pom-pom antennae, all covered in a now-stiff crust of dried blood. The sight of it, in her daughter’s favorite store, where Brigitte mistook cheap jewelry for the real thing, hurt. It hurt more than anything else, more than whatever fate this was." | 块4 引语＝P4 第 3–4 句 | ✅ 对应（P4 末句 "It hurt more than anything else…" 未入引语，见「漏」） |
| P5 "Her head was pounding. She almost touched it but stopped herself, afraid it wouldn’t be there, or not entirely there. She caught her reflection in one of those mirrors where girls admired their ballet slippers. Her head was there, but her hair was matted, and her face was a big, dark smudge. … She counted nine hoops, all different sizes, five in one ear and four in the other. They appeared to be silver, but she wasn’t sure, since everything was scabbed over, brown and black. The appointment she couldn’t remember must have been long, unhygienic, and cruel." | 块5 引语＝P5 第 3–4 句；块6 引语＝P5 末 3 句 | ✅ 对应 |
| P6 "Then, hearing someone humming, she turned and saw the girl." | 块7 引语＝全段 | ✅ 对应 |

## 漏（原文明写、md 未收；**不阻断**）

| # | 原文证据 | md 现状 | 建议 |
|---|---|---|---|
| 漏1 | P2 "The brightness was like a kick to the face."（像被踹了一脚） | 块1 未收此句，也未在分析中提「亮度像挨一脚」 | 可并入块1 引语或分析；不改也不算错 |
| 漏2 | P2 末 "She lay back down, closed her eyes, and stayed that way awhile." | 导航 人物弧线提了「闭眼躺回」，但未进引语 | 同漏1 |
| 漏3 | P4 末 "It hurt more than anything else, more than whatever fate this was." | 未入引语；导航 情感弧线位置 概括为「灾难已经发生」 | 可并入块4 引语（块4 现 44 词，加此句约 57 词仍在 30–70 区间） |

## 编（md 说了、原文没有）

| # | md 断言 | 原文对照 | 判定 |
|---|---|---|---|
| 编1 | 导航 一句话概括：「她**认不出自己的脸**」 | P5 "She caught her reflection … **Her head was there**, but her hair was matted, and her face was a big, dark smudge." —— 她照了镜子、确认「头还在」，是**认得自己但脸糊成一片污迹**，不是「认不出」 | ❌ 错（见判定表 V2，提示级） |
| 编2 | 导航 情感弧线位置：「灾难已经发生（血、穿孔、**失忆**）」 | 原文只有 "The appointment she **couldn’t remember**" —— 记不起的是那一场预约，不是「失忆」 | ❌ 措辞失准（提示级） |
| 编3 | 一句话总结：「**记不起自己做过什么**的女人」 | 同上：她只记不起那场预约 | ❌ 措辞失准（提示级） |
| 编4 | 块2 读者视角提示：「却是**后面所有血污的来源地**」 | 原文 P4 只能证明这间店是**这一屋血污**的现场；全书另有 Diana 腰间伤口（ch08）、Alba 与母亲的腹部伤口（ch14/15），与此店无因果关系 | ❌ 跨章断言过宽（提示级） |
| 编5 | 块4 读者视角提示：「后文**她自己的眼光会再次出问题**」 | 原文本段只写 Brigitte 把廉价首饰当真货；「后文眼光出问题」无出处，且「她」指代不明（Brigitte？叙述者？） | ❌ 不可核断言（提示级） |
| 编6 | 导航 Tropes 兑现/反转：给书名造中文译名「**别把她一个人留着**」 | 本站书名以英文登记（`notes/books/index.md:36` = "Don't Leave Her Alone"），本书总览 `00_概述.md` 标题亦用英文原名；md 内另一处中文译名与全站/本书不一致 | ❌ 一致性（提示级） |

## 错（引用/理解与原文冲突）

- 无「错」级内容：7 块引语全部逐字命中原文且位置递增；块5「为什么这样写」引用的 "She almost touched it …" 同在 P5，属同段内自洽回指。
- 块4 中文理解把 "The wings she and Brigitte would try on for selfies, the bear-shaped backpacks, the pom-pom antennae" 读成三件都用于自拍；原文语法上 "for selfies" 只挂在 wings 上（背��、触角是并列项）。程度极轻，列提示级（V7）。

## 机器层与人工层的差

- 机器层（bookform/chapter.sh）全绿：7/7 逐字、子项齐备、导航 5 项、中文层密度 100%、夹杂 0%。
- 人工层抓到 6 条机器看不见的**内容层措辞/归属**问题（编1–编6）——与 ch02 块4「作者 vs 她」同类，**四道机器探针全绿而人判可抓**，是本周第 ③ 类（施事/归属）的复现。
