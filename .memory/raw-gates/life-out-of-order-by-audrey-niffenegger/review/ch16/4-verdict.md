# ch16 The Empty Bottle · R5 判定

- 机器层：`chapter.sh` **rc=0**；块数 8 / 引语 8 / segment_miss 0 / 查无 0 / 空引号 0 / 结构缺项 0 / 关键词异常 0 / 字数 1911
- 素读：`1-suread.json`（10 条 + 转折点补条；**全章 Zach 第一人称**，声部标记 `Zach:`）
- 对账：`3-diff.md`

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 谁在说话：全章 Zach 第一人称，Oliver 的台词不得归给 Zach、反之亦然 | `text/ch16:23` `Zach: Alba’s been time traveling…`；`:91` `“I’m Zach.”`；`:95` `“Oliver.”`；md 第 19 行保留 `Zach:` 前缀 | 声部正确，全章未错置（ch14 是 Alba、ch15 是 Oliver，本章是 Zach——三章三种第一人称，已逐一核对） | 跳过（核实无误） |
| 2 | 空瓶酒吧这一场的身份错位未被 md 误写成「两人相认」 | `text/ch16:154` `“No, I’ve never played in public in Chicago. My wife lives here. I come to visit her.”`；`:241-262` Zach 回家复述「我遇到一个有意思的人」、Alba 只说 `“That was nice of him,”` | md 第 11/13 行均写「对彼此一无所知」「读者比 Zach 多知道一层」，未虚构相认 | 跳过（核实无误） |
| 3 | Oliver 的三处时代错位（车库乐队/足球赛/波多黎各游行）全章查无 | `text/ch16:129` `“I thought they were meant to be confined to garages until they were ready to perform in public?”`；`:137` `“Was there a football match?”`；`:142` `the Puerto Rican Day parade is this weekend`；`/usr/bin/grep -cE "车库\|garage" "ch16 the empty bottle.md"` → `0` **rc=1**；`"波多黎各\|Puerto"` → `0` **rc=1**；`"足球"` → `0` **rc=1** | 本章唯一的「他不属于 2034 年」证据全缺 | 提示 |
| 4 | 物证细节缺：祖父的 Ronson 打火机、亮黄 Weejuns 无袜 | `text/ch16:133` `bright yellow Weejuns without socks`；`:162` `I have an old Ronson lighter that used to belong to my grandfather… he looks surprised to see it, but he knows how to use it.`；`/usr/bin/grep -cE "Weejun\|乐福鞋" md` → `0` **rc=1**；`"Ronson\|打火机"` → `0` **rc=1** | 漏两处物证 | 提示 |
| 5 | md 第 15 行观察顺序「先衣着、再口音、再国籍」 | `text/ch16:38`（衣着）→ `:43` `Then I realize that he’s Chinese…` → `:50` `a very elegant English accent` → `:91` 问名字 | 国籍与口音前后颠倒（真实次序恰是本章误会的来源） | 提示 |
| 6 | 两条「想要孩子而不能」的平行是否成立 | `text/ch16:203` `“No,” I say… “I’d like to, but we can’t.”`；`:212` `“My wife and I both have medical issues…”`；`:207` `You can’t possibly understand, I think.` | 平行成立，md 第 81/87 行判读正确 | 跳过（核实无误） |
| 7 | 本章 8 块 / 1911 字是否低于本书主流 | `2-machine.json` `block_target [3,6]`、`words 1911`；ch14 10 块/3054 字、ch15 3 块/755 字（短章） | 块数与字数在本书区间内，只是缺口集中在 L1/L2 | 提示（并入 3/4） |
| 8 | 词汇例句逐字 | 13 条全中（脚本核 0 miss）：shirtfront 38 / shoplifted 83 / incredulously 120 / chain-smoke 171 / stir-crazy 249 / newsworthy 275 / vanished 24 / crumpled 24 / sparse 29 / slouches 34 / nightstand 262 / conversations 107 / mysterious 266 | 无一处改写 | 跳过（核实无误） |

报数（四组）：

- **逐字**：0（8 条引语全中，含 `Zach:` 声部前缀；13 条词汇例句全中）
- **对应**：0（8 块全部对得上，见 3-diff 第四节）
- **形态**：0（H1 `16. The Empty Bottle`；导航 5 项齐；子项原句 1–8 齐；块序与原文一致；有「一句话总结」）
- **断言**：0 阻断 + 3 提示（漏 2 + 错 1）

## 已核实为正确（防下一轮误修）

| 看着像错 | 回原文核对 | 结论 |
|---|---|---|
| 「Zach 33、Oliver 27」——Oliver 比 Zach 小 6 岁，却与 Alba 同龄 | `text/ch16:18` `(Zach is 33, Oliver is 27)`；`text/ch15:18` `(Oliver is 27, Alba is 30, Zach is 30)` | 2031 年 Zach 30、2034 年 33；Oliver 两条线都是 27。原书抬头如此，勿按年份换算 |
| 「Alba 说 Twenty sixteen」像是笔误 | `text/ch16:245` `“Twenty sixteen,” she says.` | 原文用英文数词写法（= 2016），md 第 14 行「答一句二零一六年」译法正确，勿改成「2016 年」以外的写法 |
| 「她可能在他身边睡着时消失」像推断过头 | `text/ch16:24` `I think she might have vanished while she was asleep next to me` | 原文本身是推测语气（I think… might have），md 保留「可能」正确 |
| 「他对乐队说 People paid money to hear this?」 | `text/ch16:120` 逐字 | 有据 |
| 「他自称衣服是偷的」 | `text/ch16:83` `“I shoplifted all of it, you see, so there really is no need to worry.”` | 有据；md 第 13 行写「整套都是偷来的」准确 |
| 「他说从没在芝加哥公开演出过」 | `text/ch16:154` 逐字 | 有据；别误改成「没在芝加哥演出过」（原文限定 in public） |
| 「You can’t possibly understand」的位置 | `text/ch16:207` `I offer him another cigarette. You can’t possibly understand, I think.` | 是在 Oliver 说「我理解」之后、他自己心里补的，md 第 14 行「说完在心里补了一句」正确 |
| 「Empty Bottle」在 Ukrainian Village | `text/ch16:185` `this bar in Ukrainian Village` | 与 md 第 71 行一致 |
