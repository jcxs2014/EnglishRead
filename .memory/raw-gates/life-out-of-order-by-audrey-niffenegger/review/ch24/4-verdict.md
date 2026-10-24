# ch24 判定表

机器层 rc=0，8 块。人判结论：**漏 5 · 编 0 · 错 2 · 提示 8**（表内 10 行，其中阻断 2 行）；其中阻断 2 条（L1 漏、E1 错），其余 8 条均为提示级。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| Isadora 自发说「You make my heart sing」、以及「Consciousness?」/「No. But something less random than usual.」整段没有进任何块，也没进导航/总结 | `text/ch24_to_bring_the_moonlight_into_a_chamber.txt:356`「Out of nowhere comes a voice: “You make my heart sing.”」；`:366`「“Consciousness?” I ask.」；`:370`「“No. But something less random than usual. I need to figure out what.”」；md 侧 `/usr/bin/grep -nE "heart sing"` 与 `"Consciousness"` 均 `rc=1`（零命中） | 漏：本章收尾钩子整体缺失 | **阻断** |
| 原句 7 引语截短，导致「为什么这样写」的结论被原文下一句否证 | md 引语止于「…the outside world.」；原文 `text/…ch24…txt:351` 紧接「I feel the weight of my sadness shift—it still hangs over me, but I can begin to look forward and imagine my life after Henry’s death.」；md `ch24 …md:85` 却写「她没有说悲伤结束，只说知道自己缺什么……作者选的是后一种」 | 错：截短 + 结论与原文相反 | **阻断** |
| md 没写本章日期与年龄 | 原文 `:18`「Friday, April 9, 2010 (Clare is 38, Beck is 34)」；md `grep -nE "April 9"` → `rc=1` | 体制不齐（同批 ch29 写了日期） | 提示 |
| VR 博物馆约五十行（底特律壁画→卢浮宫维米尔→V&A→Marble Palace→新奥尔良教堂→保险库→Ando Gallery）无任何块 | 原文 `:279-330`；8 个引语块无一落在此区间；导航仅「带她戴上头显逛一座收容失物的虚拟博物馆」一句 | 选点前重后轻，非「未进导航」 | 提示 |
| 本章最锋利的一句台词未引 | 原文 `:347`「“It’s the room that’s the ghost. The light you’re seeing is already six days old.”」；md `grep -nE "six days old"` → `rc=1` | 名句漏引 | 提示 |
| 头颅「不是她做的」这一层被跳过 | 原文 `:77`「“No,” Beck replies, grimacing. “I hired a grad student to make it, but I’m not too excited about the result.”」；md `grep -nE "grad student"` → `rc=1` | 细节缺，不影响主线 | 提示 |
| 原句 6 从句子中段起引，丢掉 Beck 对 Clare 的正面反驳 | 原文 `:225`「“True beauty is not elitist. I want Isadora to be able to love. To find beauty and goodness in places that humans might not.」；md 引语自第三句起 | 引语选短（R4） | 提示 |
| 原句 7 中文主语指向不明 | 原文 `:351`「when **she** sat next to me in this room」＝Beck；md `:81`「当初她在这间昏暗展厅坐到她身边时」两个「她」不可分 | R4 三问之一（主语是谁）未落实 | 提示 |
| 「三年」的归属被改写 | 原文 `:309`「I don’t want to explain that I’ve been weeping in this room for three years.」；md `:87`「也是她三年没肯回去的地方」 | 把「哭了三年」换成「三年没回去」 | 提示 |
| 原句 8 截短，丢掉 Kimy 的旁人评语 | 原文 `:379`「“You’re in a good mood,” Kimy says approvingly.」、`:387`「“It’s about time,” Kimy replies.」；md 该块中文止于 Clare 唱歌 | 引语选短（R4） | 提示 |

**报数（四组）**

- 逐字：引语 8 块 / 8 段，全部在 `text/` 命中（机器 `segment_miss=0`，我另抽 4 段手核一致）→ **逐字 0 缺陷**
- 对应：8 块中 5 块完全对应，3 块引语截短（原句 6、7、8），其中原句 7 的分析结论被原文否证 → **对应 1 阻断 + 2 提示**
- 形态：H1 `24. To Bring the Moonlight into a Chamber` ✓；导航 5 项齐 ✓；子项齐（中文理解/关键词/为什么这样写/读者视角提示）✓；8 块在 2–15 内 ✓；CJK 密度最低 41（原句 8）无低密度告警 ✓ → **形态 0 缺陷**
- 断言：本章 md 对原文的事实性断言（十二英尺、虹膜扫描、图灵 Child Machine、加德纳失窃维米尔、Toll House、Kimy 在场）逐条可核 → **断言 0 编造**；另 1 条分析断言错（E1）

## 已核实为正确（防下一轮误修）

| 看着可疑的写法 | 原文 | 核实结果 |
|---|---|---|
| 「半个球形铁架、约十二英尺高，几乎顶到天花板」 | `:30`「It’s a half sphere, about twelve feet high (maybe more, it nearly touches the ceiling)」 | 数字与「几乎触顶」都成立，别改 |
| 「Richard 那位意大利小提琴修复师朋友」 | `:24`「a friend of Richard’s, an Italian violin restorer who always hams it up for Alba’s benefit」 | 归属是 Richard 的朋友，方向正确 |
| 「卢浮宫侧厅里那幅失窃的维米尔」 | `:289-294`「wasn’t this the one that was stolen from the Gardner Museum?」「Yes…I put it in a little side gallery in the Louvre」 | 画＝The Concert, by Vermeer；失窃地＝加德纳；md 未写「加德纳」不算错（原文是 Clare 的问句，非旁白） |
| 「守丧三年」 | `:309`「I’ve been weeping in this room for three years」 | 三年成立；只有 E2 的「没肯回去」是改写 |
| 「图灵的孩子机器 / 给机器一个童年」 | `:206`「I’m testing Alan Turing’s Child Machine theory…I am letting Isadora ‘grow up’ like a real girl」 | 引文与转述一致 |
| 「黑天花板、成排服务器、地上一块胶带贴的 X」 | `:29-31`「the ceiling has been painted black…an X marked with silver duct tape」 | 形态描述准确 |
| 「她连朋友的名字都找不到」＋读者提示「说明 Beck 在这栋楼里还没留下多少痕迹」 | `:49`「Just a few months. I was waiting for my servers to arrive from Detroit.」 | 推断有原文支撑（搬来仅数月），不是编 |
