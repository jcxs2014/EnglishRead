# ch01 判定表（R5）

章：`ch01 the last party.md`（155 行，10 块）
原文：`text/ch01_the_last_party.txt`（2116 行 / 14623 词）
机器：`2-machine.json` rc=0；块数 10；引语 10 段全 ok；空引号 0；子项缺 0；关键词 4 行英文全中；`block_hint` 仅提示块数 10 略高于本书中位 6（不判红）。
素读：`1-suread.json` 10 条，`quote in line` 脚本校验 10/10。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 抬头三个 Alba（21/29/47）与 Zach 22 岁全部落进 md | `text/ch01_the_last_party.txt:18`「Monday, December 26, 2022, and Tuesday, December 27, 2022 (Alba is 21, 29, and 47, Zach is 22)」。md:11 只写「一位从 2031 年旅行回来的年长 Alba」，md:15 引抬头时停在日期。另 `:1925`「I look at her more carefully and realize that she’s older than the self we were with earlier; her hair is going gray.」证明地下室是**第二个**年长版 | md 把三个 Alba 压成一个，47 岁版与 Zach 年龄全缺 | **阻断（漏）** |
| md:11「她在示威中打倒的警察一周后死在医院」 | `:1711`「Hyde Park demo—she hit a policeman with her sign when he grabbed her from behind. He died of brain hemorrhage a week ago.」原文无「医院」、无「打倒」（只是用标语牌 hit） | 细节添加 | 提示（编） |
| md:15「三段带名字的第一人称声部（Alba—Zach—Alba）交替」 | `grep -nE "^(Alba\|Zach):" text/ch01_the_last_party.txt` → 7 行：`:23`、`:194`、`:204`、`:1267`、`:1476`、`:1864`、`:1883`；`grep -c` = 7 | 声部 2 个、段落 7 段，非 3 段 | 提示（形态） |
| md:13「全屋人替她演一场正常派对」 | `:158`「The place is packed with people I don’t recognize…whiter friends」；`:159`「did we hire actors?」；`:1911`「all these sleeping people are more than asleep…the sign for a spiked drink」 | 客人是 Junior 那圈陌生人、后被下药，既不知情也不是演员 | 提示（错，范围） |
| 四处细节应补 | Zach 塔尔萨 `:586`「Tulsa. I moved to Chicago four years ago.」+ 妹妹 `:670`「Seventeen and thirteen. RaeAnn and Suellen.」；Kendrick/病名 `:877`「the doctor who first discovered time-travel genes?」；父死日期 `:698`「On New Year’s Eve. It was 2006 turning into 2007.」+ `:708`「a librarian at the Newberry Library」；五人姓名 `:1954`「Junior, Buddy, Art, Rick and Terry」 | md 均未落（导航与块内都没有） | 提示（漏，降档） |
| md:37「这把琴是家里的第三代传物」 | ch01 仅有 `:35`「my beloved Guarneri del Gesù that was my grandfather’s」；ch00 全文无 violin/Guarneri 世系句（`/usr/bin/grep -nE "violin\|Guarneri" text/ch00_life_out_of_order.txt` → 只 `:37` 泛论音乐） | 本书前两章无法证实「三代」，也不构成反证 | **未核** |

计数（只数阻断档）：漏 1 · 编 0 · 错 0；提示 4。

## 已核实为正确

以下看着可疑、回原文核对后**成立**，下一轮不要误修：

1. 日期部分照抄无误：md:15 引「Monday, December 26, 2022, and Tuesday, December 27, 2022」与 `:18` 前半逐字一致（缺的只是括号里的年龄，见上表）。
2. 宵禁时间：md:11「宵禁十点到六点」= `:104`「curfew is in effect from ten to six」。
3. 派对是最后一次：md:13「Lamont 家父母离婚、房子春天挂牌」= `:1573`「Our parents are putting it on the market in the spring. They’re getting divorced.」
4. Lucinda 十六岁：md:81「十六岁的 Lucinda」= `:1140`「She looks childlike, much younger than sixteen.」（是「看起来比十六小」，即她 16 岁，不是「不到十六」）。
5. 「你未来的自己说她会没事」：md:87 = `:1256`「She will be fine, according to your older self.」
6. 床罩掀开露裸体：md:77 = `:1470`「she peels off the yellow bedspread with a flourish and stands gloriously naked」。
7. 「说 I want you to kiss me」：md:14 = `:1859`「“I want you to kiss me,” I reply, and he does.」
8. 「黄色便笺写字再烧掉」：md:15 = `:1641`「Caralora retrieves a yellow legal pad and a ballpoint pen」+ `:1734`「Nick take the paper to the sink and set it on fire」。
9. 「Nadia 开车来」：md:11 = `:70`「climbing into Nadia’s car」。
10. 结尾「只为有个地方躲」：md:109/117 = `:2116`「I will go back just to have something to do, a place to hide.」
11. 机器层「引语逐字」10/10：`2-machine.json` 每段 `segments[].ok=true`，本书 `text/` 为本轮真值，无需再对 epub。
12. 未提「1957 Nash Ambassador」不算漏：md 通篇不写车，`:2072`「It’s a 1957 Nash Ambassador」属可选细节（若下一轮补车，型号照此，别写成别的年份）。
