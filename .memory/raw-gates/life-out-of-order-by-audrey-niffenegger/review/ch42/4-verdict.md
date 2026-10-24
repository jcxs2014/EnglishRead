# ch42 embodiment — 判定表（R5，复核版）

- 原文 396 行 / 精读 131 行（mtime 2026-10-25 01:06:34）；`2-machine.json` **rc=0**（verdict=ok，8 块 / 8 段引语全逐字，segment_miss 0、empty_quote 0、struct_bad 0、keyword_bad 0、cjk_low 0、hole 0；nav 5 条、H1 `42. Embodiment`；words 2908；本书 71 章中位 6、硬上限 10）
- 报数四组：**逐字 8/8 通 · 对应 8/8 通 · 形态 通（H1／nav 5／子项四件齐／块数 8≤10）· 断言 漏 提示 5＋跳过 1 · 编 提示 1 · 错 提示 3 · 阻断 0**

## 一、本轮改判说明（必读）

上一版 `4-verdict.md`（00:56）的 **E1（1 月 14 日叙述者写成阿尔芭）与 E2（把下楼的贝克写成「母亲」）两条阻断，在当前 md 已修复**：

- `grep -nE '一月十二日由' "ch42 embodiment.md"` → `:15`「仍是双声部：**一月十二日由阿尔芭记，一月十四日与五月五日由贝克讲**」，退出码 0
- `grep -nE '贝克承认自己苛刻' …` → `:12`「**贝克**承认自己苛刻，下楼去向她那个孤独的「怪物女儿」赔不是——克莱尔当时在楼上」，退出码 0

⇒ 当前版本这两条**不再成立**，本轮不计阻断。修复方向正确，且未牵动 `:14` 人物弧线与块 8 中文（已逐条复核一致）。

## 二、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：8 块引语 | 机器层 8/8 `ok:true`；抽查 `:110` "Afterward, as we are panting entangled on the narrow sofa, I look over Carl's shoulder and see that the green light on the monitor is glowing."（md `:39`）、`:396` "I suddenly feel ashamed… I go downstairs to make amends to my lonely monster-daughter."（md `:89`） | 与原文同形（含弯引号、省略号） | 通 |
| 对应：8 块中文是否在讲该引语 | 逐块追问主语/受事：块 1「她请卡尔来」＝Alba 邀约；块 2「卡尔去厨房、她回房、回来人不见」＝两人各自动作，主语未串；块 3「她越过肩膀看见绿灯」＝Alba 看、Carl 作遮挡物；块 4「贝克开博物馆门」＝Beck；块 5「贝克说办不到」＝Beck 对 Isadora；块 6「她删房间／贝克隔离她」＝Isadora 毁、Beck 罚；块 7「贝克下楼见两个阿尔芭」＝Beck；块 8「贝克听见克莱尔、自己下楼」＝Beck | 八块均在讲本句，无一块跑去讲全书主旨或作者生平 | 通 |
| 形态 | `2-machine.json` form：h1 `42. Embodiment`、h1_shape_ok true、nav_count 5、subitems_modal 四件（中文理解/关键词/为什么这样写/读者视角提示）、blocks 8 | 与本书主流形态一致 | 通 |
| E5 `:11`／`:131`「卡尔**误入**地下室」 | `:79` "I just want to see, I won't touch anything. What's so secret, Alba?"；同段 "Carl has strong urbex tendencies. He loves being where he isn't supposed to be."；门是两人忘锁 `:66` "Lucinda and I must have forgotten to close up when she left earlier" | 卡尔是主动探看；「误入」偏软。但「不是阿尔芭带他下去」这一方向正确 | 提示 |
| E3 `:13`「先被说不像人，再被说不像成年人」 | `:173` "I don't look sufficiently human to be romantic?"（**她自己问的**）；`:177` "You don't look old enough to inspire thoughts of romance… You look like a child. It's a category error."（先否定**年龄**）；`:181` "You look like a Barbie-doll version of Lucinda"（加龄后） | 顺序倒置；「被说」与「自问」混淆 | 提示 |
| E4 `:12`「亲密被屏幕另一头看见」 | `:110` "…I see that the green light on the monitor is glowing. I try not to panic. What has Isadora seen?"；`:344` "She's seen him. They didn't meet each other." | 原文只给绿灯＝醒着，「看见」始终是阿尔芭的疑问；后文「见过他」指看见 Carl 本人 | 提示（改「可能被看见」） |
| F1 `:13`「被造出的孩子索要**身体**与爱」 | `:246` "I need the actual person. Boyfriends are human?"；`:256` "I could be out there, with the boyfriend, who is human?" | 她要的是「真人／到外面去」，无「身体」一词 | 提示（措辞外推） |
| L1 养老院失火的因由未收 | `:23` "…because the one they were living in caught fire"；md `grep -c '失火'` → 0，退出码 1 | 因果被压成「养老院的事」，不误读 | 提示 |
| L2 次日晨「Would you still love me if I didn't look like this?」整场未收 | `:124` "Would you still love me if I didn't look like this?"；`:132` "'You never know.'"；md 无对应（`grep -cE '剃|刮胡子'` → 0，退出码 1） | 对 Carl 身份最重的暗示未进 md；本章转折不在此 | 提示（导航补一句即可） |
| L3 「就我们两个」的邀约取舍未收 | `:42` "should we invite nick and nadia?"；`:45` "nope, just us" | 未收 | 提示 |
| L4 「怕自己消失烧掉房子」未收 | `:53` "I don't like to cook by myself in case I vanish and burn down the house" | 未收 | 提示 |
| L5 停战手段「告诉她未来」与 Beck 知情时点未收 | `:299` "She's telling Isadora her future."；`:344` "She's seen him. They didn't meet each other. He doesn't know about her."；md `grep -c '未来'` → 0，退出码 1 | 转折已在导航「谈成停战」，机制缺席 | 提示 |
| L6 年龄锚（Alba 17、Carl 17）未收 | `:18` "Saturday, January 12, 2019 (Alba is 17)"；`:225` "He is seventeen, the same age as Alba." | 年龄非缺陷 | 跳过 |
| 词汇表 13 条例句 | `:60` spontaneity·belatedly／`:260` cyberspace／`:273` capitulate·bottle／`:396` juxtaposed·blanket／`:59` miniature·bottle／`:79` stealthy／`:118` scheming／`:105` surrender／`:124` cheek／`:54` table | 13 条全部逐字命中（`/usr/bin/grep -nE` 逐词定位，退出码均 0；机器层未报 vocab 类 issue） | 已核实 |

## 三、已核实为正确（防下一轮误修）

1. **叙述者归属**：`:15`「一月十二日由阿尔芭记，一月十四日与五月五日由贝克讲」＝原文 `:23` 段首 "Alba:"、`:146` "Beck: Clare and I get home later than we'd planned…"。**不得再改回「十四日由阿尔芭记」。**
2. **下楼赔不是的是贝克**：`:396` "I suddenly feel ashamed of myself for being so harsh with Isadora. I can hear Clare stirring upstairs, but instead of waiting for her I go downstairs to make amends to my lonely monster-daughter."；Clare 本章未发一言。**不得改成「母亲下楼」。**
3. **绿灯＝Isadora 醒着**：`:93` "The little green light that indicates Isadora's awake is not lit, to my relief."——块 3 注「灯的含义在章内早处交代过」成立。
4. **停战是年长 Alba 谈成的**：`:294` "I hear her say, 'Isadora! Shut the fuck up for a minute! Listen!'"；`:370` "Detente. Isadora will behave herself."——md `:11` 正确。
5. **「贝克嘴上说不知道、心里明白自己不会做」有原文**：`:260` "I don't know how to make that happen." ＋同段 "I don't add that I wouldn't do it, even if I knew how."（第一人称内心）——md `:131` 成立，勿删。
6. **镜像房间细节**：`:152` "…wearing a black dress with skinny straps, high heels and dark red lipstick, holding a wineglass that's half full of pale yellow liquid."——「半杯」「暗红」「细吊带」均未写错。
7. **「她要的是真的」是年长 Alba 说的**：`:326` "She wants the real thing. Her emotions are real, she feels real to herself and she doesn't want a synthetic love. Would you?"——md 未错挂给贝克。
8. **年长 Alba 年龄外貌**：`:277` "The extra Alba is in her late fifties or early sixties."；`:278` "Her hair is waist-length and completely white"——md `:81` 一致。
9. **块 3「越过肩膀」的方向**：`:110` "I look over Carl's shoulder and see that the green light on the monitor is glowing."——她背对屏幕、只能看见灯，md `:45` 的说法成立。
10. **机器层 rc=0 是真通过**：`bash scripts/chapter.sh "…/ch42 embodiment.md" --json` 退出码 0，counts 全零，非「无法判定」。
