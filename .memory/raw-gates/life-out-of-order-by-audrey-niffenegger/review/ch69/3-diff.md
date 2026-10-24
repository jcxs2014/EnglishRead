# ch69 R3 对账（素读 13 条 vs md）

- 原文：`text/ch69_a_murmuration.txt`（236 行 / 2314 词），四段署名：`Beck:`（:23）→ `Alba:`（:118）→ `Beck:`（:123）→ `Alba:`（:188）
- 精读：`ch69 a murmuration.md`（6 块 / 112 行）
- 素读：`1-suread.json`（13 条）；机器：`2-machine.json`（rc=0，6 块，6 段全命中 44/37/55/37/36/51 词，pos 85/3171/4521/9652/10868/11273，nav 5，子项 4）

## 漏（素读有、md 无）

1. **「另一个阿尔芭」——九岁的她自己出现、与她拥抱、说「你怎么这么久才到」——全章零字** —— 档：**阻断**
   - text/ch69:214 `In the abrupt silence I hear footsteps. A child hesitates in the doorway. It’s my nine-year-old self, from that first day when I played for Isadora. Other Alba runs to me and I embrace her. She says, “What took you so long to get here?”`
   - text/ch69:224 `Other Alba is holding my violin, watching me expectantly. I will be my own muse, now.`
   - md 侧零命中：`/usr/bin/grep -cE "九岁|另一个|童年|小女孩" "ch69 a murmuration.md"` 四项全为 0，退出码 **1**（无匹配）。
   - 影响：块 5（原句 5 `I will be my own muse, now.`）在原文里紧接 `Other Alba is holding my violin, watching me expectantly`——那是「自己做自己的缪斯」的对位（她要向童年的自己要一支琴）。md 第 12 行写「直到群鸟与乐谱把情绪推到最亮」，第 11/112 行从「群鸟穿身」直接跳到「坐进堆满乐谱的房间」，中间这个**登场的人物与她的台词**整段丢失，导致块 5 的中文理解（第 61 行「从今往后她做自己的缪斯」）失去来处。

2. **Jasper 提到「你的 Isadora」与「我们的女儿」** —— 档：**提示**
   - text/ch69:99 `“Your Isadora—she’s delightful. She comes here sometimes, to let me know how you are. I like to imagine that our daughter would have been just like Isadora.”`；text/ch69:104 `I embrace him. “That was the idea,” I say. “But she’s exceeded my original plan.”`
   - md 侧：`伊莎多拉`／`Isadora` 各 0 命中。这是本章唯一交代 Isadora 来历（女儿已不在、Isadora 是照她做的）的地方，也是 Jasper 与 Beck 之间真正的和解内容。

3. **黄房子里的实物遗物未收** —— 档：**提示**
   - text/ch69:194-195 `Oliver’s piano, his cigarette lighter, our little cache of opera and symphony tickets, a leather jacket that Zach gave me for my birthday in 2026… a pan of Beck’s vegan lasagna and three lemon bars in a Tupperware container I recognize as my mother’s.`
   - md 侧：只保留「柠檬条入口即化」（第 13 行），Oliver 的钢琴、Zach 2026 年的皮夹克、母亲的保鲜盒、「咬下去味道全对却像气泡化掉」这组物件全无（`千层面` / `皮夹克` / `Oliver` 均 0 命中）。

4. **世界状态与身体的几处硬信息未收** —— 档：**提示**
   - text/ch69:37 `I have lived here for fifty-five years.`；text/ch69:24 `there aren’t any taxis now`；text/ch69:37 `The bioware implant makes me dizzy when I move too abruptly.`；text/ch69:155 `Just leave the servers on. I left instructions, they’re on my desk.`；text/ch69:200 浴室 `three toothbrushes sit side by side in the glass`
   - md 侧：`五十五` / `服务器` / `牙刷` 各 0 命中（`bioware` 只出现在第 99 行词汇例句）。这组信息合起来才是「2065 年 + 她早已把自己搬进机器」的实证。

## 编（md 有、原文无）

- 无严格意义的凭空新事。两处轻度越界已列在「错」与「其他」：①「死在沙发旁」（第 14 行）——原文只说身体蜷在地板上（text:236），沙发是她**死后**被安放的地方，且沙发位于书桌旁（text:37 `I have positioned the sofa near my desk`）；②第 15 行「两个视角轮换报告同一场会面」——Alba 的第二段（text:188-236）是**独自**穿湖、进黄房子、见自己，不是「同一场会面」。

## 错（两边都有但不一致）

1. **「说再见的人是贝克」——说再见的其实是阿尔芭** —— 档：**阻断**（低危，三字可修）
   - text/ch69:168 `Alba hugs me. “Goodbye, Beck,” she says. “Thank you, for everything.”`
   - md 侧（第 13 行）：`反转「告别」：说再见的人是贝克，真正走开的却是她。`——前半句主语反了；且后半句的「她」若指贝克，两句合起来自相矛盾（说再见的是贝克、走开的也是贝克）。
   - 成立写法：「说再见的是阿尔芭，真正走开的却是贝克」。

## 其他（留档，未判阻断）

- 抬头未落地：`text/ch69:18` `Saturday, September 26, 2065 (Alba is 64, Beck is 89)`；md 全篇无日期、无 64/89（按 ch66/ch68 同一口径记为提示，见 4-verdict）。
- 贝克在此章**性别正确**：md 通篇用「她」（第 21/31/41/51/61/71/112 行），`他` 只用于 Jasper（第 35/37/112 行）——与 ch67/ch68 的类级缺陷不同章，修 ch67/ch68 时**不要**连带改这里。
