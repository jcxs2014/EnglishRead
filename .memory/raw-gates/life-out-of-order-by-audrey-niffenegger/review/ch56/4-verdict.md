# ch56 Parrots Do Love —— R5 判定

- 章：ch56（`text/ch56_parrots_do_love.txt`，64 行 / **319 词**；抬头 `:18` 2041-08-31，Beck 65、Isadora 32）
- md：`ch56 parrots do love.md`，79 行，**3 块**（短章下限 3，达标）
- 机器层：`bash scripts/chapter.sh` → **rc=0**，verdict=ok；3 引语全逐字；empty_quote=0；struct_bad=0；block_target=[2,2]

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| **章题句「parrots do love」全篇零落地**（导航只说「一句暗语」，总结只译「做野兽」） | `text/ch56_parrots_do_love.txt:24-25` "It’s urgent. Tell her it’s time to be a Wild Thing. Tell her parrots do love."；`:39` "“Oliver sent us a message. He says it’s time for you to be a Wild Thing, and that parrots do love. Do you understand?”" | 漏（章题＋暗语＋复述三重缺失；3 块已在下限，不适用块满降档） | **阻断** |
| **方向反了**：「她被放出「间隙」」——原文是 release **into** | `:24` "release Isadora into the Interstices as soon as possible" | 错（into＝放进；同篇导航另一条写作「释放进」，自相矛盾） | **阻断** |
| 「It’s urgent.」未译 | `:24` "It’s urgent." | 漏（总结只剩「尽快」） | 提示 |
| 长椅丢了 Will 与 Lyra | `:34` "She’s sitting on Will and Lyra’s bench in the Oxford Botanic Garden." | 漏（互文被抹平） | 提示 |
| 「She has learned well. It’s finally time.」未见 | `:51` "She has learned well. It’s finally time." | 漏（只在分析里意译） | 提示 |
| 「亲手断开」与原文动作相反 | `:60` "I connect the cable, and a moment later, she’s gone." | 错（接 vs 断；隐喻可通、事实不可） | 提示 |
| 「她提到他也许认不出她」 | `:51` "“But you may not recognize me.”" | 正确 | 跳过 |
| 数字（2041-08-31 / 65 / 32） | `:18` "Saturday, August 31, 2041 (Beck is 65, Isadora is 32)" | 正确 | 跳过 |
| 蓝裙、赤脚、宽檐帽、阴天 | `:34` "She’s wearing a blue dress, and her feet are bare. … a wide-brimmed sun hat on her lap." | 正确 | 跳过 |
| 最后一句自问 | `:64` "What have I done." | 正确 | 跳过 |

## 报数（四组）

| 组 | 数 | 说明 |
|---|---|---|
| 逐字 | 3/3 ✅ | segment_miss=0；人工 grep 三条块首全部命中 |
| 对应 | 3/3 ✅ | 逐块中文与引语一致（原句 2 的「帽子搁在膝上没戴」与原文 "on her lap" 相符） |
| 形态 | 3 块＝短章下限；子项四件齐；导航 5 条 | 通过 |
| 断言 | 阻断 2 · 提示 4 · 跳过 4 | 见上表 |

## 判词

ch56 **2 阻断**。319 词的短章，3 块把「信—屏幕—飞吻」三段收得很紧，逐字与对应全对，分析里「她被分成借来的部分和自己的部分」一句尤其准。两处硬伤都在边角、却都伤到本章的骨：①章题「parrots do love」在正文里消失了——信里两句话，md 只留下「做野兽」，把「鹦鹉也会爱」这句暗语吞了；而 Isadora 正是靠这句话得到「爱」的许可。②Tropes 条把「放进间隙」写成「放出间隙」，方向相反，且与同篇导航自相矛盾。两处都只需改一句话。

## 已核实为正确（防下一轮误修）

命令：`/usr/bin/grep -nE "release Isadora into the Interstices|parrots do love|Will and Lyra|wide-brimmed|give you a kiss|connect the cable" text/ch56_parrots_do_love.txt`，命中 `:24 / :25 / :34 / :39 / :51 / :60`，**退出码 0**。

- 原句 1 ＝ `:24` "I find a sealed envelope with my name written on it in Alba’s familiar, extravagant handwriting. I slit it open. It says, Oliver wants you to release Isadora into the Interstices as soon as possible."（md 截到 "as soon as possible" 为止，合法）
- 原句 2 ＝ `:34` "It’s an overcast day in the garden, but Isadora has a wide-brimmed sun hat on her lap. “Good morning, Beck.” She gazes out of the screen at me with Lucinda’s sweet expression, but her voice is weary."
- 原句 3 ＝ `:51` "I will give you a kiss!” She kisses her fingers, turns her hand to me in the most natural way. Her face is alight with expectation."
- 「释放进间隙」＝ `:24` "release Isadora into the Interstices" → **方向为 into，凡写「放出间隙 / 离开间隙」皆错，勿改回**
- 「parrots do love」＝ `:25` "Tell her parrots do love."；`:39` "and that parrots do love" → **章题原句，必须落地，勿删**
- 「Will and Lyra’s bench」＝ `:34` "She’s sitting on Will and Lyra’s bench in the Oxford Botanic Garden." → 正确，勿简化成「花园长椅」
- 「Lucinda’s sweet expression」＝ `:34` "with Lucinda’s sweet expression" → 神情借自 Lucinda，勿改成 Isadora 自己的表情
- 「What have I done.」＝ `:64` → 正确
