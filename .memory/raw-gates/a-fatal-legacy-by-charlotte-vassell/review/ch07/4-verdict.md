# ch07 判定表（R5）

> 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch07_7.txt`（已与 epub `OPS/s017-Chapter-007.xhtml` 交叉核对）
> 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch07 cctv shows a willow lookalike.md`
> 档位：**阻断**（与原文不符/缺失）｜**提示**（措辞正当，可改可不改）｜**假红**（工具判错）｜**跳过**（没查）
> 覆盖声明：**本报告只覆盖第 7 章**（独立审查单元，委托书指定）。本书其余 53 章、总览三篇（`00_概述.md`／`00_情感节点.md`／`00_金句精选.md`）**未审**——不得据此推断全书结论。

---

## 一、四组数（只报这四组）

| 组 | 总数 | 通过 | 有问题 | 明细 |
|---|---|---|---|---|
| **逐字** | 引语 9 条 + 词汇例句 28 条 = **37** | **37** | **0** | 9 条引语全部原样连续命中原文（机器 `2-machine.json` 全部 `ok:true` + 人工复核）；28 条例句每条 `grep -F` 在 `text/ch07_7.txt` 命中 1 次，无一条取自他章。**0 条问题** |
| **对应** | 块 **9** | **9** | **0（对应层面）** | 每块中文都在讲它自己的引语；无「引语选短」/「讲全书主旨」/「只复述字面无为什么」。**但 9 块中有 2 块在施事或对象上错位**（原句4、5），按分组计入「断言」组 |
| **形态** | 4 项（H1 / 导航项 / 子项集 / 块数） | **4** | **0** | 见下节「形态组」 |
| **断言** | 逐条核对（人物 / 数字 / 时序 / 归属 / 措辞） | — | **阻断 5 · 提示 6** | 阻断 5：错1 三个身影、错2 叙述句变台词、错3/编1 走路姿势+静止剪影、编2 走动路线、漏A 在场证明缺失。提示 6：漏B Tom 支线、漏C 恶作剧伏笔未兑现、漏D/E/F、错4 颜色落点、错5 锁定/打算、错6 指代含混。详见 `3-diff.md` 与下表 |

**阻断型条数：5**（另有 0 条假红、0 条跳过）

---

## 二、形态组（H1 / 导航项 / 子项集 / 块数）

| 项 | 现场实测 | 本书众数 / profile | 结论 |
|---|---|---|---|
| **H1** | `# 7. The Police Station` | 书内 54 章**全部**为 `# <章号>. <标题>`；`text/ch07_7.txt:17` 即 “The Police Station” | **无偏离**。⚠️ 注意：ch05 / ch49 / ch50 的 H1 也叫 “The Police Station”（同名场景多章共用），**不是重名错误**，勿“修正” |
| **导航项** | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 本书 54/54 章**完全同一组 5 项**（`nav_count: 5`，`nav_count_ok: true`）；profile 允许 5 项 | **无偏离**。profile 的第 2 项名为「情感弧线位置」，本书实作「视角」——**全书一致**，非本章问题 |
| **子项集** | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | profile `mystery-thriller` 规定子项 4 项一致；本书 391 个块**全部**用这 4 项 | **无偏离** |
| **块数** | **9 块** | 本书中位 **7**（区间 5–10，分布：5×5、6×19、7×10、8×5、**9×8**、10×7）；profile 区间 3–10 | **无偏离**。9 块落在 profile 区间内，且本书有 8 章同为 9 块，非孤例。**不构成需要写理由的偏离** |

> 形态组结论：**形态 4/4 通过，0 偏离**。（`chapter.sh` 的 form 段亦全绿：`h1_shape_ok: true`、`nav_count_ok: true`、`nav_missing: []`、`subitems_modal` 与 profile 完全一致。）

---

## 三、判定表（断言 | 证据（章:区间） | 结论 | 档位）

| # | 断言 | 证据（章:区间 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md:49「把**三个身影**一起对着铁栏杆比」 | 原文 `text/ch07_7.txt:140`「comparing **both figures** to the iron railings.」＋ `:137`「the one that Tiny Simm had taken of Amy from the same place」＋ `:76`「‘Five foot two.’」 | 与栏杆比的是**两个影像**（录像里那人 + 同地点拍的 Amy）；Willow 身高是她自报，从未参与栏杆比对 | **阻断** |
| A2 | md:42「**说了句**“她很娇小”」 | 原文 `:73`「He took out the screenshot he’d made of the recording and then he looked at her. **She was diminutive.** ‘Willow, how tall are you?’」 | `She was diminutive.` 是叙述句（无引号），Caius 此处唯一台词是 `‘Willow, how tall are you?’`；md 同块 `:44`「他先**目测**再发问」亦自相矛盾 | **阻断** |
| A3 | md:13／:24／:129「**连走路姿势都读不出来**」「**录像留下的是一幅静止剪影**」 | 零命中取证：`/usr/bin/grep -inE "gait\|stride\|posture\|walk(ed\|ing\|s)? (like\|style\|habit)" …/text/ch07_7.txt` → **无输出，退出码 1**；`/usr/bin/grep -inw "walk\|walks\|walked\|walking" …/text/ch07_7.txt` → 退出码 0，仅 3 处且全为方向义（`:20` `:259` `:265`）；epub 正则计数 gait→0/stride→0/posture→0/walk→3；全书 `text/*.txt` 中 gait/stride 只命中 `ch52_52.txt:233`「hitting his stride」（无关章）。原文反证 `:20`「**The quality wasn’t bad**… could at least see the general outline… Their height, **build**, anything particular they might have been wearing **or carrying** would all be ascertainable.」「He’d seen Willow **come and go** as she described.」「screenshotting anyone **walking towards** the Horatio Combe Institute」 | 原文**从未**把走路姿势列为证据的一维，也未断言读不出；“**静止剪影**”与原文三处事实相反（画质不差、画面里有人在走动、还能分辨走向）。md 把一条推断当作原文给出的证据上限，并重复 3 次（含「一句话总结」）——**本章承重结论，必须改**。附：同源口径不一致，md:13 写“这三样”漏掉**携带物**（原文 `:20` “wearing **or carrying**”），而 md:24 自己写对了 | **阻断** |
| A4 | md:11「逐项比对身高、衣着与**走动路线**」 | 零命中取证：`/usr/bin/grep -n "route\|path\|walked the same\|same route" …/text/ch07_7.txt` → 无输出，退出码 1。原文实际比对项：行踪 `:43`–`:58`、衣着 `:61`–`:70`、身高 `:73`–`:94`、网络身份与粉丝 `:97`–`:124`；唯一与走动相关的推理是**目击者视角** `:277`「if you glanced across from the square you might reasonably dismiss them as Willow putting in a late shift」 | md 虚构了一次不存在的调查动作，并顶替掉了真实存在且承重的“行踪核对”（见 A5） | **阻断** |
| A5 | md 全文缺 **Willow 的不在场证明**（“她周五傍晚不在伦敦/不在场”） | 原文 `:43`「‘Willow, where were you Friday evening at around 6.30 p.m.?’」`:52`「‘No, at my parents’ house in Harpenden.’」`:58`「My entire extended family and about thirty of my parents’ closest friends. My dad retired on Friday. We had a big party at the cricket club… I caught the train from St Pancras mid-afternoon… My mum dropped me off at the station before eight o’clock on Saturday morning.」；md 侧全文检索 `Harpenden` 仅命中词汇例句 `:122`，正文零叙述 | 全章**唯一**能证明“录像里那人不是 Willow 本人”的客观材料未被写出来，读者无法复核 md「一句话概括」里“有人借了 Willow 的外形闯进研究所”这一结论 | **阻断** |
| A6 | md 全文缺 **Tom（前男友）假说及其证伪** | 原文 `:158`「‘Willow’s boyfriend? Weirdly jealous… It doesn’t stack, does it?’」`:195`「‘Ex. I have dumped him since.’… ‘Tom’s a marine biologist.’」`:201`「‘Penzance probably. He’s been in Cornwall for the last eight months with his tutor tracking basking sharks. Nowhere near London.’」；md 侧只留下取自该段的词汇例句 `:95` megafauna、`:107` basking sharks（“词条在、事件不在”） | 本章第二个假说（跟踪者/前男友雇人假扮）整段缺失，只留半条推理链 | 提示 |
| A7 | md:59「这个‘恶作剧’的说法很快就会被证据推翻——**注意它是怎么没的**」承诺的兑现段缺失 | 原文 `:152`「It’s a lot of effort for a prank. Setting up a PO Box and corresponding with Digby by letter for weeks. Caius had given the letters from Isolde that he’d found yesterday to forensics to fingerprint and to test the envelopes for saliva.」；md 全文 `PO Box`=0、`forensic`=0 | md 自己设的伏笔在本章内没有兑现，读者等不到答案 | 提示 |
| A8 | md:38「形似到能混，但**细节对不上**」 | 原文 `:67`「You had a red one yesterday, but this one is orange.」→ `:70`「I have **six of this specific cardigan, in different colours**, and twenty-two others. Practically one for each day of the month.」；同块 md:37 已写对「靠颜色分辨身份本身就不牢靠」 | 块内两处口径相反；且漏掉原文当场给出的答案 | 提示 |
| A9 | md:129「**锁定了一个**…身影」「**并打算把罪名栽到她头上**」 | 原文 `:271`「Isolde dressed up as the person who they likely knew would find the body.」（只是 Amy 的提问 + Caius 的「Maybe?」）`:274`「‘Is it personal then? Are they taunting Willow?’」`:277`「‘I’m not sure.’… ‘**Maybe they thought they were in disguise and hadn’t thought that far ahead.**」；与 md 自身 `:79`「却证明不了身份」`:80`「身份也建立不起来」冲突 | ① “锁定” 与本章主旨及 md 自身口径打架；② “打算”把悬置假说写成既定意图，原文明说“我不确定/也许他们自以为伪装成功” | 提示 |
| A10 | md:13「**被盯上的调查对象**最终被暂时当作那个以 Isolde 之名与迪吉通信的人」 | 原文 `:256`「Amy tacked the blurry screenshot onto the incident board and wrote ‘**Isolde?**’ above it in marker.」`:295`「staring at **the figure who they had to assume was Isolde for now**」 | 被临时认定为 Isolde 的是**录像里那个身影**（板上写的还是带问号的 “Isolde?”）；md 主语读起来像指 Willow | 提示 |
| A11 | md 缺 **Digby 生前情绪突变 / 口哨 / “有某种存在”** | 原文 `:225`「he was suddenly all loosey-goosey. He was whistling when I saw him last… for a moment, I thought it was, you know, **a presence**.」；md 只在词汇表留 `loosey-goosey` 例句 `:96` | 本章唯一凶兆线未进正文 | 提示 |
| A12 | md 缺 **潜在目击者（Māori 抗议者 / 对街女孩）** | 原文 `:219`「There’s this girl who lives across the way who talks to me about romance stories in the square at lunch」`:222`「‘Apart from the Māori protestors,’ Amy said.」 | 正是“目击证据不可靠”层的另一半，未进正文 | 提示 |

> 阻断型 **5** 条：A1（三个身影）、A2（叙述句变台词）、A3（走路姿势/静止剪影）、A4（走动路线）、A5（在场证明缺失）。
> **最要紧的一条＝A3**：它同时出现在「线索结构」「读者视角提示」「一句话总结」三处，是全章的中心论断，而它在原文里零命中（grep 退出码 1 已自证）；且原文在同一段里给出了三处反证（画质不差、能看到人走动、能分辨走向），使 md 的“静止剪影/读不出走路姿势”不只是无据，而且**与原文相反**。这一条直接决定本章“目击证据不可靠”写得对不对——按原文口径，录像那一层能证明“有人朝研究所走去、能辨出身高体格与穿戴携带物”，不能证明的是**身份**，而不是“走路姿势”。

---

## 四、已核实为正确（防误修护栏：以下不得以“读着不对”为由改动）

| md 写法 | 原文逐字 | 位置 |
|---|---|---|
| 9 条引语全文 | 见 `3-diff.md`「四、已核实为正确」逐条对照表（每条均原样连续命中） | md:19/26/33/40/47/54/61/68/75 |
| 28 条词汇例句 | 每条 `grep -F` 在 `text/ch07_7.txt` 命中 **1** 次 | md:88–125 |
| `# 7. The Police Station` | `text/ch07_7.txt:17` “The Police Station”；ch05/ch49/ch50 同名——**不是重名错误** | md:7 |
| “画质不差，只是离得太远”“穿着或带着什么显眼的东西” | `:20`「The quality wasn’t bad, it was just from so far away.」「anything particular they might have been wearing or carrying」 | md:21 |
| “深色宽松牛仔裤”“深色头发剪成齐耳短发”“整体看上去和实习生 Willow 极为相似” | `:30`「a pair of dark, baggy jeans. Her dark hair was cropped into a bob. She looked remarkably like Willow Bell, the intern.」 | md:28 |
| “Amy 比 Willow 高几英寸，而录像里那个人又比 Amy 高几英寸”（后半句） | `:140`「You’re a couple of inches taller than Willow and this person is a couple of inches taller than you」 | md:49 后半 |
| “拿栏杆当尺子”“只给差异不给绝对值” | `:140`「comparing both figures to the iron railings」（只给 “a couple of inches”） | md:51–52 |
| “另外十个人”“案发前两小时”“已经不再优先” | `:265`「screenshots of ten other people who walked past in the two hours before Digby’s death that aren’t a priority any more」 | md:70、:73 |
| “深色齐耳短发和一件宽大开衫”“把对方当成 Willow 在加晚班”“从广场对面扫一眼的人完全可能…” | `:277`「they would probably just see a dark bob and giant cardigan… if you glanced across from the square you might reasonably dismiss them as Willow putting in a late shift」 | md:77 |
| “靠颜色分辨身份本身就不牢靠” | `:70`「six of this specific cardigan, in different colours… one for each day of the month」 | md:37 |
| “以 Isolde 之名与迪吉通信的人”“暂时当作” | `:152`「the letters from Isolde that he’d found yesterday」「corresponding with Digby by letter for weeks」＋ `:295`「had to assume was Isolde for now」 | md:13 |
| 全部数字（6 点半 / 五英尺二 / 五英尺五 / 十个人 / 两小时 / 三十人） | `:30` `:58` `:76` `:91` `:265` | md 全文 |

---

## 五、可复现命令（第三方复核用）

```bash
cd /Users/jcxs2014/Documents/Works/EnglishRead
bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch07 cctv shows a willow lookalike" --json \
  > .memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch07/2-machine.json; echo "EXIT=$?"
# → EXIT=0，verdict=ok，9/9 quotes ok:true，counts 全 0，form 全绿

python3 scripts/verify_corpus.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
# → P0-0 语料验收: PASS（FAIL 0 / WARN 3）

python3 scripts/check_vocab.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
# → FAIL (0)

/usr/bin/grep -inE "gait|stride|posture|walk(ed|ing|s)? (like|style|habit)" \
  notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch07_7.txt; echo "EXIT=$?"
# → 无输出，EXIT=1（A3 零命中自证）

/usr/bin/grep -inw "walk|walks|walked|walking" \
  notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch07_7.txt; echo "EXIT=$?"
# → 3 处方向义命中，EXIT=0

/usr/bin/grep -nE "route|path|walked the same|same route" \
  notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch07_7.txt; echo "EXIT=$?"
# → 无输出，EXIT=1（A4 零命中自证；BRE 写法 "route|path" 亦为 0 命中，两种口径一致）
```

**本报告未做的事**（供复核方知悉，避免误读“全绿”）：未改书目录任何 md、未 `git add`/`commit`、未审第 7 章以外的任何章与总览三篇、未对 `00_*.md` 做跨文件一致性核对。
