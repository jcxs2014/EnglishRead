# ch25 判定表

机器层 rc=0，4 块（该章目标区间 3–5）。人判结论：**漏 0 · 编 0 · 错 2 · 提示 8**（表内 8 行，无阻断）。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| md 导航写「再回到阳光下的红酒与大笑」，但酒是在室内喝的，原文也没有「大笑」 | `text/ch25_a_murmuration.txt:71`「She comes in, sets the tray on a little table next to me, uncorks the wine and pours each of us a glass.」；`:76`「sitting together here in Clare’s bright little office, sipping cold white wine」；户外仅 `:134`「We walk to our cars together.」；情绪词是 `:123`「smile shyly」、`:143`「a big smile」 | 场景与情绪词错位 | 提示 |
| md 导航写「冷气、蜡与漆的气味」，原文的气味是香与万寿菊 | `:50`「It smells marvelous and reminds me of incense and marigolds, though there is a slightly caustic edge to the scent.」 | 由物件反推气味，非原文 | 提示 |
| Beck 的贵格会身份没进正文块/导航/总结，只被词汇表收了例句 | `:76`「As a Quaker, I have always found quiet very restorative; I crave it.」；md `/usr/bin/grep -nE "Quaker"` → 仅 `ch25 a murmuration.md:66`（词汇表行），`rc=0` | 人物身份与全章「安静」价值判断的依据缺位 | 提示 |
| 视角从 Clare 换成 Beck（全章第一人称＝Beck）没有被点明 | `:23`「Beck: Clare has invited me to visit her studio.」；md `:15` 仅写「第一人称现在时」，`:27` 只写「视角属于一个客人」 | 读者可能误读成 Clare 自述 | 提示 |
| 块 4 起点太晚，接吻的触发链被整段切掉；`blackness/Blackness` 双关也消失 | `:119`「“Hmm. Speaking as someone whose Blackness is on display all the time, are you sure you want to do that?” I mean it as a joke but Clare turns bright red…I reach over and take her hand. …I feel strange, as though I’ve just seen my soul in a mirror.」；md `grep -nE "soul in a mirror"` → `rc=1`；`grep -nE "Blackness"` → `rc=1` | 引语选短（R4 的「为什么」被删） | 提示 |
| 手机看真实鸟群、以及「flocking behavior／maybe a hawk」的解释没进任何块 | `:84-85`「She retrieves her phone…a swarm of black specks rise up from the trees, forming a diffuse, dark cloud that coalesces into an oval, then a cone, a mushroom…」；`:94`「Probably there is a predator, maybe a hawk. There’s a whole scientific discipline, flocking behavior, that tries to explain it」；md `grep -nE "flocking"` → `rc=1` | 现实参照与作者解释缺位 | 提示 |
| md 声明「抬头先给出日期与三人的年纪」，正文却没有这些数 | `:18`「Saturday, April 17, 2010 (Clare is 38, Beck is 34, Alba is 8)」；md 全文无 `2010` / `April 17` / `38` / `34` / `8` | 自指缺陷：说了有、实际没有 | 提示 |
| 末句「and this is how we begin」未引 | `:143`「…until she calls and this is how we begin.」；md `grep -nE "how we begin"` → `rc=1`；总结只到「她开始等一个电话」 | 点题句丢失 | 提示 |

**报数（四组）**

- 逐字：4 块 / 4 段引语全部在 `text/ch25_a_murmuration.txt` 命中（机器 `segment_miss=0`；我另手核 `:23`、`:42`、`:103`、`:119` 四处起止一致）→ **逐字 0 缺陷**
- 对应：4 块中 3 块完全对应；块 4 引语本身对应、但起点太晚（触发链缺失）→ **对应 0 阻断 / 1 提示**
- 形态：H1 `25. A Murmuration` ✓；导航 5 项 ✓；子项齐（中文理解/关键词/为什么这样写/读者视角提示）✓；4 块在目标区间 3–5 内 ✓；CJK 最低 43（原句 3）→ **形态 0 缺陷**（唯 P2 视角未说明属内容层）
- 断言：md 对原文的事实性断言逐条可核，无凭空情节 → **断言 0 编造**；2 条场景/气味描述与原文不符（上面第 1、2 行）

## 已核实为正确（防下一轮误修）

| 看着可疑的写法 | 原文 | 核实结果 |
|---|---|---|
| 「由车库改成的工作室」 | `:23`「a garage-like building that’s been converted into a studio」 | 原文是「像车库的附属建筑被改成工作室」，未明说原是车库。美式独立后院建筑作此推断不离谱，**不算编，可不改**；若要更贴字面可写「后院一间像车库的屋子」 |
| 「反转『表白』：先动手的是被邀的那一个，说『我找到同伴』的也是她」 | `:119`「I reach over and take her hand」「I feel I have found my heart’s companion」 | 全对：先伸手与说「找到同伴」的都是 Beck（被邀者）。别把「她」改成 Clare |
| 「鸟群在两人四周缓缓盘旋成漩涡」 | `:42`「The whole flock of birds begins to move around us, very slowly…we are at the center of a rising vortex」 | 漩涡/中心/极慢三个要素都在，准确 |
| 「她要的不是让人平静，而是把心里的黑拿出来给人看」 | `:114`「I wasn’t trying to make people feel calm. I wanted to take my blackness and externalize it—I wanted to put it where other people could see it.」 | 释义正确（`blackness` 此处＝她心里的黑，与 Beck 的大写 `Blackness` 不是同一层意思） |
| 「成百上千只鸟…靠细铁丝吊着」 | `:42`「There are hundreds, maybe thousands of them…hanging from thin wires; puppets.」 | 数词与「傀儡/铁丝」均成立 |
| 「佩斯利沙发、颜料罐、像化学实验室或女巫的厨房」 | `:50`「a paisley covered sofa…jars of pigment…remind me of a chemistry lab or a witch’s kitchen」 | 逐项对得上 |
| 「年龄：Alba is 8」 | `:18`「(Clare is 38, Beck is 34, Alba is 8)」 | 8 岁成立；md 只是没写出来（P5） |
