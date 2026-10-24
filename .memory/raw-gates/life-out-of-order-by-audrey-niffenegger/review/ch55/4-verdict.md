# ch55 Lucky Day —— R5 判定

- 章：ch55（`text/ch55_lucky_day.txt`，139 行 / 1109 词；抬头 `:18` 1981-05-14，Alba 27、Oliver 26）
- md：`ch55 lucky day.md`，91 行，**4 块**
- 机器层：`bash scripts/chapter.sh` → **rc=0**，verdict=ok；4 引语全逐字；empty_quote=0；struct_bad=0；block_target=[2,3]

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 人物弧线：「阿尔芭……备好衣服」——衣服是未来的他们备的 | `text/ch55_lucky_day.txt:63` "There’s a red dress hanging in her closet, just the right shade. We marvel at our future selves who have provided for us like xiǎo jīnglíng, anticipating all our needs." | 错（归属：备衣者＝未来的他们；同篇一句话总结写对，前后矛盾） | **阻断** |
| 婚礼誓词/交换戒指/宣布为夫妻无块，仅在词汇例句 | `:110` "We exchange rings. The judge pronounces us husband and wife. We kiss, briefly, but enthusiastically." | 漏（仪式落点；总结有「由一位中国女法官主持」） | 提示 |
| 唐人街婚宴细节未进块 | `:117` "the proprietor kept bringing extra dishes and strangers kept toasting us and it was the most delightful meal I’ve ever had" | 漏（情节在总结里） | 提示 |
| 「走廊不长」原文无 | `:63` "I wander down the hall from the bathroom to my own room." | 编（解释性补白，建议删） | 提示 |
| 指示清单是他笔迹 | `:55` "“I have instructions. A list. In your handwriting.”" | 正确 | 跳过 |
| 五月不吉、带四不好 | `:92` "“May is a terrible month to be married,” I tell her. “And dates with the number four are no good.”" | 正确 | 跳过 |
| 母亲九岁、父亲十七岁、他父母未出生 | `:110` "Alba’s mother is nine years old and her father is seventeen. My parents aren’t born yet." | 正确 | 跳过 |
| 红＝中国新人色、好运兴旺 | `:63` "I show her the suit and explain about red, the color for brides and grooms in China. “It means good luck, prosperity,” I tell her." | 正确 | 跳过 |
| 白天 Oliver / 夜里 Alba 双第一人称 | `:23` "Oliver: I arrive in the back garden of the Yellow House early in the morning."；`:117` "Alba: The evening of our wedding…" | 正确 | 跳过 |
| 机器层六项 | counts 全 0（quote_long/segment_miss/struct_bad/empty_quote/keyword_bad/cjk_low） | 形态通过 | 跳过 |

## 报数（四组）

| 组 | 数 | 说明 |
|---|---|---|
| 逐字 | 4/4 ✅ | 机器 segment_miss=0；人工 `/usr/bin/grep -nE` 复核 4 条块首全部命中 |
| 对应 | 4/4 ✅ | 逐块中文均讲对应引语，无错位 |
| 形态 | 4 块、子项四件齐、导航 5 条、无空引号 | 通过 |
| 断言 | 阻断 1 · 提示 3 · 假红 1 · 跳过 5 | 见上表 |

## 判词

ch55 **1 阻断**。四块的选句很准（床上的光、红西装、市政厅的算术、鸡与蛋），逐字与对应全对；唯一的硬伤在导航的人物弧线里：把「备好衣服」算成阿尔芭的功劳，而原文把这份体贴明确归给「未来的我们」（`:63`）。同篇的一句话总结反倒写对了，可见是笔误级别的归属滑落——但它是本章「谁在安排这一切」的核心，且与总结自相矛盾，须改。建议把「备好衣服」改为「发现衣服已备好」。

## 已核实为正确（防下一轮误修）

命令：`/usr/bin/grep -nE "I insert myself between the sheets|It would be unlucky to wear white|Alba waits, uncomprehending|It’s a chicken/egg problem|provided for us like|In your handwriting" text/ch55_lucky_day.txt`，命中 `:24 / :55 / :63 / :110 / :130`，**退出码 0**。

- 原句 1 ＝ `:24` "I insert myself between the sheets and Alba opens her eyes without quite waking. I stroke her arm. She turns onto her back and we lie there for a while as the sun angles over the houses and under the train tracks, into our room, onto the bed, so that our legs are warmer than our stomachs under the sheet."
- 原句 2 ＝ `:63` "It would be unlucky to wear white or black, colors of mourning, to our wedding. I wander down the hall from the bathroom to my own room. When I open the door I see red: there is a red suit laid out on the bed."
- 原句 3 ＝ `:110` "Alba waits, uncomprehending, while we talk about distance, and immigration. I do a little mental math: Alba’s mother is nine years old and her father is seventeen. My parents aren’t born yet."
- 原句 4 ＝ `:130` "“It’s a chicken/egg problem. Our marriage comes first, chronologically, but I was younger when I married Zach, and I am still married to him. Come to think of it, Zach and I had trouble getting a marriage license."
- 「指示清单是他的笔迹」＝ `:55` "“Shh,” Alba whispers. “I have instructions. A list. In your handwriting.”" → **正确，勿改**
- 「红＝中国新人色／好运兴旺」＝ `:63` "I show her the suit and explain about red, the color for brides and grooms in China. “It means good luck, prosperity,” I tell her." → **正确，勿改**
- 「未来的他们像小精灵备下一切」＝ `:63` "We marvel at our future selves who have provided for us like xiǎo jīnglíng, anticipating all our needs." → **原文明写「未来的他们」，凡把备衣功劳归给 Alba 的写法都要改，归给 future selves 的写法正确**
- 「露水脚印」＝ `:23` "My feet leave dark prints in the dew on the grass." → 正确
- 「白人金发？否——本章无此设定」：ch55 无此句，勿据 ch58 补写。
