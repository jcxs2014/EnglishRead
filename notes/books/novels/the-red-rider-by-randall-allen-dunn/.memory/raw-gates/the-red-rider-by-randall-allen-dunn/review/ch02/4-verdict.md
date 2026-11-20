# ch02 4-verdict（T3 深审 · 边审边改）

R1：review/ch02/1-suread.json（8 条，子代理盲读，锚点自检 8/8）。
R2：review/ch02/2-machine.json（chapter.sh --json verdict=ok，rc=0；6 块 8 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | "Leaving so soon?"+七英尺 → 中文逐句对应 | mocked/enormous/galloped/assessment 均在引语 | 主语 Grenault 伸手抓、她 gasped 回望——与原文 "grabbing for me as we galloped"（我=她）一致；"realizing my previous assessment" 施事是她 ✓ | 对应 |
| 2 | Lycanum 变身 | Lycanum/transform/uncorking/vials 在引语 | 他们（狼群）喝药、uncorking 主语是 they ✓；"must be one" 的 one=大个子，中文理解未误指 | 对应 |
| 3 | 跃马设饵 | stirrups/leaped/tumbling/flapping red cloak 在引语 | "她把双脚抽出马镫""狼群越过山头追 Crimson 与斗篷"——原文主语 I 与 wolves 一致 ✓ | 对应 |
| 4 | 首杀 Thayer | straight at his head/in an instant/guttural 在引语 | "她抬手直瞄""群狼中响起哀嚎"——原文 I fired / one of them cried ✓；省略号两段各自独立取证（fragments 123/123）✓ | 对应 |
| 5 | 空弩虚张 | predicament/reload/bluff 在引语 | "Grenault 察觉她的困境、冲下山来吞掉她"——原文 he realized...to devour me ✓；中文"最好还是虚张声势"= Better to bluff ✓ | 对应 |
| 6 | 缓退与对视 | slowly turned to depart/slow retreat/scrutinize 在引语 | "他那迟缓的撤退""他还在打量她"——原文 His slow retreat / he continued to scrutinize ✓；"仿佛早就知道她杀不了他"= As if he knew I couldn't kill him ✓ | 对应 |

跨章引用核章号：块1 分析"第 1 章酒馆里的目测"——ch01 text 有 "Could he actually be seven feet tall?"（text/ch01_1.txt），指认正确。
第一次/唯一/数字回原文：块4 提示"五箭对六狼"= "Five bolts, and six of them."（text/ch02_2.txt 逐字）✓；导航"七狼围猎"= "All seven of the wolves" ✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 连环杀 Gregor/Robillet 名字未进 md | text/ch02_2.txt: "Gregor!" / "Robillet …" 两处哀嚎逐字 | 补入原句4 读者视角提示 | 提示→当场修（S1 覆盖） |
| 狼群数量/距离细节未入引语 | 块数配额与转折覆盖权衡；导航已计"七狼" | 不修 | 提示（依据：转折层全覆盖，铺陈细节由导航计数兜底） |
| 金句 ③/㉓ 引语"跨标签拼接"⚠️（overview full） | verify_fragments_indep.py：123 片段 0 MISS、拼接未标省略号 0 | 工具口径提示；省略号两侧原词、每片段独立命中 | 提示（不修，依据：审查表 S2 ③ 允许 … 标省略，机器全绿旁证） |

## 修复动作（边审边改）

- ch02 md 原句4 读者视角提示追加 Gregor/Robillet 两声哀嚎点名（text 逐字 "Gregor!" / "Robillet …"）。
- 修后 chapter.sh rc=0、gate.sh 退出码 0，pathspec 提交。

## 已核实为正确

- "previous assessment" 指她在 ch01 对身高的目测——ch01 text "Could he actually be seven feet tall?"（text/ch01_1.txt:86 邻域）成立，非编造。
- "五箭六狼"顺序：原文先 "I only had five bolts left" 后 "Five bolts, and six of them."，md 提示语序与原文一致。
- 原句6 "As if he knew I couldn't kill him." 为独立完整段（text/ch02_2.txt 末段），多段省略号拼接合法（fragments 独立取证命中）。
