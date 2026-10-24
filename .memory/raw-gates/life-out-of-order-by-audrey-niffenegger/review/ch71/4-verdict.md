# ch71 判定表（The Vanished World）

- 覆盖：深审人判全块（10/10）+ 四件套齐全；素读 10 条（`1-suread.json`，含字符区间）
- 机器层：`bash scripts/chapter.sh "…/ch71 the vanished world.md" --json` → **rc=0**，块数 10，引语段 10/10 命中（33/38/59/32/31/48/31/49/36/37 词，pos 640/2871/12160/14652/18912/20934/21998/22403/23925/24437），查无 0，空引号 0，struct_bad 0，关键词异常 0，中文密度低 0，nav 5（5 项齐），H1 `71. The Vanished World` 形态正确，`block_target [9,15]`；`block_hint` 提示「10 块高于本书常见区间 3–9」——本书 71 章最高即 10、中位 6，本章是终章，块数与任务表配额 ch71=10 一致 ⇒ **此提示不构成阻断**
- 报数：**逐字 0 · 对应 0 · 形态 0 · 断言 1 阻断 + 提示 8**（提示含 6 条提示级漏：三瓶啤酒／鹦鹉与新动物／Steinway／再来一次／饼干／黄房子，另有抬头年龄与「岸上」措辞各 1 条）

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 开篇：梦见回到上海童年的卧室，母亲在隔壁唱《两只老虎》；醒来枕上有小而圆的湿点，不知是记忆还是梦 | text/ch71:23 `Oliver: I wake from a particularly vivid dream. I was small again, I was back in my old bedroom in Shanghai, in my narrow bed. In the next room my mother was singing:`；歌词 :30–58 `两只老虎 Two little tigers … 一只没有眼睛 One has no eyes … 一只没有尾巴 One has no tail … 真奇怪 How strange`；:64 `I find small, round wet spots on my pillow. I am not sure if this was a memory, or merely a dream.` | **整段不在场**：`/usr/bin/grep -cE "两只老虎\|上海\|母亲" "ch71 the vanished world.md"` → `0`，**退出码 1**；`/usr/bin/grep -nE "焗豆\|湿点\|枕"` → 无输出，**退出码 1**。这是全书唯一一次出场的奥利弗的母亲、全书唯一一次出现的《两只老虎》（缺眼睛、缺尾巴的儿歌＝一个残缺世界的隐喻）、也是终章第一句情绪来源（湿点是泪还是屋顶渗水，作者故意不判）；第 11 行直接从「淹水的伦敦醒来」起笔，等于把这一章的开场镜头剪掉了 | **阻断**（首选：在导航第 11 行前补一句梦与湿点，块数仍守 10；若允许多一块，可用 text:64 的 `London is quiet.` 之前另起一块「原句 0」） |
| 抬头日期与「应该 69、实际 91」的来由 | text/ch71:18 `Friday, June 13, 2098 (Oliver should be 69, but has spent so much time in the past that he is actually 91)` | md 只写「91 岁」，未落日期、也未解释 69→91 的差额（正是全书机制） | 提示 |
| 三瓶啤酒＝顺路去接阿尔芭 | text/ch71:241 `“Why three beers?”`；:245 `“We’re going to collect Alba on our way.”` | `三瓶` 零命中（rc=1）；第 152 行只留「带上啤酒」 | 提示 |
| 伊莎多拉：鹦鹉多了、有叫不出名字的新动物、也许让它们自己命名 | text/ch71:435 `“Oliver, there are so many parrots now. There are new animals, too, I don’t have names for them.”`；:444 `“Or maybe I will let them name themselves.”` | `鹦鹉` 零命中（rc=1）。「世界在愈合」的最硬证据（新物种）与命名权交接都缺 | 提示 |
| 管风琴管子被偷光、她特意留一架 Steinway Model B | text/ch71:457 `“the organ is ruined. People stole all the metal pipes. There is a piano for you. I keep it specially.” … a Steinway Model B, hidden behind the stage.` | `Steinway\|斯坦威` 无输出（rc=1）；第 13 行只有「音色出乎意料好的钢琴」 | 提示 |
| 「你还会再来一次吗」「当然。会。嗯，大部分吧」 | text/ch71:523 `“Would you do it again?”`；:527 `“Of course. Yes, I would. Well, most of it, anyway.”` | `再来一次` 无输出（rc=1）。终章里他对自己一生的唯一总评缺失 | 提示 |
| 留着一包巧克力消化饼干「一直等着这一天」 | text/ch71:513 `I’ve got plenty of water and a packet of chocolate digestive biscuits I’ve been saving. I’ve been looking forward to this, it will be an adventure.` | `饼干` 零命中（rc=1） | 提示 |
| 不出门，「除了黄房子」 | text/ch71:299 `“I don’t go out, except to the Yellow House, of course. … witness to the vanished world.”` | `黄房子` 零命中（rc=1）；第 152 行只抓了后半句「躲进过去」 | 提示 |
| 「阿尔芭从岸上消失」 | text/ch71:501 `We are helping my older self get settled in the boat when Alba says, “Oliver!” and vanishes.` | 她消失在**船边**（帮老人安顿时），不在岸上；第 14 行措辞略松，事实层无误 | 提示 |
| 零命中类断言（四处） | ① `/usr/bin/grep -cE "两只老虎\|上海\|母亲" "ch71 the vanished world.md"` → `0`，退出码 **1**；② `-cE "三瓶\|黄房子\|鹦鹉\|饼干"` → `0`，退出码 **1**；③ `-nE "Steinway\|斯坦威\|再来一次"` → 无输出，退出码 **1**；④ `-nE "焗豆\|湿点\|枕"` → 无输出，退出码 **1** | 见上 | — |

## R4 逐块对应（三问）

| 块 | 这段中文是不是在讲这句引语？ | ①动词主语 | ②受事 | ③归属方向 |
|---|---|---|---|---|
| 1（原句1，pos 640，text:64） | 是（伦敦的静与「几乎所有人都不在了」） | London（quiet）；叙述者（想象他们在外面） | 不存在的人 | `Alba, Zach, Madeline` 同属「不在了的人」，第 21 行未把 Madeline 说成与他同住 |
| 2（原句2，pos 2871，text:88） | 是（他交罐头、报日期、说自己已经准备好） | 老年的他（says / smiles） | 罐头、日期 | `It’s June 13, 2098` 由**老自己**报出（不是叙述者算出来的）；`I am quite ready` 的主语是他，不是「我们」 |
| 3（原句3，pos 12160，text:277） | 是（水线以上是废墟、以南全是水） | 叙述者（can see / turn） | 水线、废墟 | `fifty meters uphill` 是水线在他的**上坡方向**五十米，不是「水位高五十米」；第 47 行「水位线在五十米外的坡上」对 |
| 4（原句4，pos 14652，text:325） | 是（水里有人游来，老自己先叫出名字） | 另一个他（says） | 游来的人 | 游来的人＝Alba（不是 Isadora）；第 63 行「另一个他先开口」对 |
| 5（原句5，pos 18912，text:413） | 是（礼拜堂后门开、女人站上舞台、全场屏息） | 那个女人（steps / 关门的人） | 门、舞台 | 「露辛达——或者伊莎多拉」是叙述者的**不确定**（原文 `It’s Lucinda—or Isadora.`），第 73 行保留了这层不确定；相貌「四十多岁、实际近九十」没有写成「她真的四十多岁」 |
| 6（原句6，pos 20934，text:471） | 是（弹安魂曲的过程与三个听者） | Alba（says）／叙述者（nod / sit / begin） | 安魂曲 | 曲为 **Madeline** 而写、她**从未见过**（`whom she never met`），第 87 行没有改成「为纪念母亲」 |
| 7（原句7，pos 21998，text:486） | 是（她说这不是终点、世界在愈合、她会要他再来） | Isadora（shakes head / says） | 奥利弗的悲观 | `You think this is the end, Oliver` 是她对**他**的判断的否定，不是「她认为这是终点」；第 93 行未反转 |
| 8（原句8，pos 22403，text:501） | 是（老自己向阿尔芭道别、她愕然） | 老年的他（turns and says） | 阿尔芭 | 「我们从不告别」的我们＝**叙述者与阿尔芭**（text:501 `We never say goodbye to each other`），不是「他与老自己」；第 99 行用「他们之间」承接前句主语，指代可读作两人，但未错置成「他与自己」 |
| 9（原句9，pos 23925，text:531） | 是（收桨漂流、等他静下来） | 叙述者（put up oars / sit still and wait） | 船桨、船 | `his gnarled hands folded in his lap` 归**老自己**；第 105 行「另一个他神色满足」对 |
| 10（原句10，pos 24437，text:535） | 是（回到厨房、蒙头睡下、未来的自己仍在漂） | 叙述者（am back / climb / pull） | 床、被单 | `In the future, I am drifting alone` 指的是**未来那个自己**（已在海上），第 117/152 行「他未来的自己仍在淹水的伦敦上方独自漂着」对，没有写成「他此刻正在海上漂」 |

## 已核实为正确（防下一轮误修）

1. **全章只有两处署名** —— `Oliver:` 在 text/ch71:23 与 text/ch71:76，此后至 :535 无第三处。md 未给中段补署名**正确**；不要照 ch69（四段署名）的形态改造本章。
2. **年龄 91 岁不是笔误** —— text/ch71:18 明说「应 69、实 91」，因为他在过去耗掉太多时间。不要把 91 改回 69，也不要补一句「作者算错了」。
3. **「你来了，我准备好了」是老年的他说的** —— text/ch71:88 `“I had lost track of the days, but now you’re here and I am quite ready.”`，第 11 行归属正确。
4. **露辛达与伊莎多拉是同一位的两半** —— text/ch71:422 `“Alba, I’m so glad you’ve come. I’m just Isadora now. Lucinda is gone. She was ready, and I let her go.”`：被放走的是 Lucinda，说这话的是 Isadora。第 11/14 行没有把两人对调。
5. **安魂曲的受献者是玛德琳，且阿尔芭从未见过她** —— text/ch71:471 `Alba wrote it for Madeline, whom she never met, as a gift.`；块 6 的中文理解与第 13 行都成立。
6. **「我们从不告别」的「我们」＝叙述者与阿尔芭** —— text/ch71:501 `We never say goodbye to each other; we always come and go as though we are just stepping out of the room for a moment.`；块 8 的读法正确，不要改成「他与自己从不告别」。
7. **三句告别用的是拼音，不是汉字** —— text/ch71:531 `“Wǎn’ān,”` / `“Shěntǐ bǎozhòng,”` / `“Yī lù shùn fēng.”`，原文只在此处给出英文对译 Good night / Take care / Safe travels。第 15 行写「中文『晚安／保重／一路顺风』」是**译述**，成立；若日后有人要「还原原文」，应写成带声调的拼音，**不要**改成汉字（那才是编）。
8. **结尾的两个「我」没有混淆** —— text/ch71:535 叙述者回到 2086 年 7 月的厨房（`Almost no time has passed since I left.`），未来那个自己留在 2098 年的海上。第 117/152 行区分正确。
9. **末日成因的因果链未倒置** —— text/ch71:289-290：警告无人听 → 冰化了 → 饥荒、瘟疫、战争 → 圣保罗与碎片大厦等被炸弹逐座摧毁。第 152 行「警告无人听，冰化了，饥荒、瘟疫与战争之后，高楼被炸弹逐座摧毁」顺序与施事都对。
10. **老自己不出门，唯一例外是黄房子** —— text/ch71:299。第 152 行未写成「他足不出户」（那会与「去黄房子」矛盾），只是没提这条例外；补写时不要删掉「除了黄房子」。
11. **英文引语 10 段全部逐字** —— 机器 10/10 命中，含原句 2 的嵌套卷引号（`"“I have no idea what’s in any of those tins…"`）。
12. **词汇 14 条例句逐字可查** —— filtration（text:158）、unwrinkled（93）、vegetation（205）、miraculously（400）、extracting（331）、wardrobe（93）、eyebrows（83）、guarantee（144）、pavement（200）、hospital（93）、stage（400）、adventure（513）、beloved（471）、anxiety（144），均以 `/usr/bin/grep -n -F` 复核。
13. **10 块不算超配** —— `block_target [9,15]` 内，任务表配额即 10，本书最高章也是 10（ch69）。`block_hint` 只是与「常见区间 3–9」对比的提示，**不得据此压块**；若为补漏 1 加块，11 块同样在 target 内。
