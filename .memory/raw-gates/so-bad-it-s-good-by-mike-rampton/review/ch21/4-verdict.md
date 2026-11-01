# ch21 The Christmas Cracker Connection 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 笑话不可省 | :15 | 是：少了笑话只剩吃饭 | underwhelming ✅ | 拉＝人 ✅ | 通过 |
| 2 表演成分 | :18 | 是：人人当一分钟明星 | performance ✅ | 演＝你 ✅ | 通过 |
| 3 起源是诗 | :21 | 是：维多利亚蹩脚诗 | romantic poetry ✅ | 装＝厂商 ✅ | 通过 |
| 4 一战后才有笑话 | :21 | 是：唱片机与更快解 | First World War ✅ | 出现＝笑话 ✅ | 通过 |
| 5 三条标准 | :25 | 是：简单、基础文字游戏 | multiple generations ✅ | 懂＝几代人 ✅ | 通过 |
| 6 ex's tinsel crisis | :25 | 是：太晦涩的反例 | tinsel ✅ | 讲＝你 ✅ | 通过 |
| 7 doing a turn | :28 | 是：1960 年代人人有段子 | doing a turn ✅ | 表演＝宾客 ✅ | 通过 |
| 8 没牙老人唱歌 | :28 | 是：cringe 之前 | social awkwardness ✅ | 唱＝老人 ✅ | 通过 |
| 9 摄像机与高标准 | :36 | 是：当众表演变可怕 | cameras ✅ | 拍＝时代 ✅ | 通过 |
| 10 elf-esteem | :39 | 是：包袱 | elf-esteem ✅ | 说＝拉炮 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 7 段正文（原写"五段"） | 9 段 − 2 标题 | 改后正确 | 提示已修 |
| 4 处完整笑话（原写"三处"） | :18 / :21 / :25 / :39 | 改后正确 | 提示已修 |
| 笑话在一战后出现 | `:21` 逐字 | 正确 | 通过 |
| 1960 年代 | `:28` 逐字 | 正确 | 通过 |
| 字符数 3,428（md 写"约 3,430"） | `len(text)` | 正确 | 通过 |

## 已核实为正确

- `:21` 的 `What do solicitors wear to work? / Lawsuits!` 是全章唯一以斜线断行的笑话，md 未把它当成正文断句错误。
- `:28` 的 `an old man with no teeth sincerely singing a lengthy song about a boat` 是作者举例，md 未写成作者亲历。
- `:39` 的 `To boost their elf-esteem` 与 md 收束一致；"第二好的圣诞 Claus"（`:36` escape clause）在 md 脉络里有对应。

## 结论

阻断 0 / 提示 2（已修）/ 假红 0。
