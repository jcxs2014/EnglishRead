# 4-verdict · ch08 the golden city（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：chapter.sh --json rc=0。R3：漏 1（轻微，提示不修）/ 编 0 / 错 0。

## 逐块判定（12 块）

| 块 | 断言 | 证据（text/ch08_chapter_8.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 corset | 施事：求助系带＝她；施助＝Dendron（后文） | "She was incapable of putting it on without help." | 对应 | ✅ |
| 原句2 Seine | 「夜/梦同素材」＝她的自评 | "the stuff of both her nightmares and her dreams" | 对应 | ✅ |
| 原句3 beggar | 施事：拍车乞讨+嘲弄＝乞丐；鞭击＝车夫；躲＝她 | "You’re a big one, aren’t you!”... he lashed the end of the reins over the man’s head" | 对应 | ✅ |
| 原句4 Eiffel | 「既轻浮又严肃」＝她读塔；希望不拆＝她 | "There was something both frivolous and serious about it." | 对应 | ✅ |
| 原句5 claim | 施事：站直/抬下巴/认领空间＝她；踉跄围观＝旁人 | "She had a right to be there, she wanted to be there, and she would claim her space" | 对应 | ✅ |
| 原句6 droll | 说话人＝买手；Emile→Edouard 纠正＝Beauclerc（上下文） | "“Yes, he was a droll fellow, with a saucy imagination." | 对应 | ✅ |
| 原句7 speech | 说话人＝Odette；对象＝买手 | "Within these jeweled halls you house the dreams of your customers" | 对应 | ✅ |
| 原句8 creed | 说话人＝Beauclerc（we are manufacturers） | "We are not people of fashion; we are manufacturers." | 对应 | ✅ |
| 原句9 Finally alive | 说话人＝Odette；体感（脸热掌麻）＝原文 | "I am feeling. I feel alive. Finally alive.” Her face was hot, her palms tingling." | 对应 | ✅ |
| 原句10 company | 「lively company」出自买手之口＝转述存疑对象 | "He kept such lively company, didn’t he?" | 对应 | ✅ |
| 原句11 coat | 施事：持衣比量＝Feld 遗孀；接衣愣住＝Merry | "Madame Feld leaned in and held it against him, checking for size." | 对应 | ✅ |
| 原句12 secret scars | 施事：怀疑对象＝父亲；提问者＝她 | "Would he have had wounds since that night that only the undertaker had seen?" | 对应 | ✅ |

## 修复

无阻断。

## 已核实为正确

- 原句4 「plans to take it down」＝原文逐字（"She had read that there were plans to take it down"）——埃菲尔铁塔去留为史实级细节，转述无误。
- 原句6 买手把亡者叫成 "poor Emile"、Beauclerc 纠正 "Edouard"——人名对照与 md 一致；md 分析「叫错死者名字」属实。
- 原句8 「feed the beast」未入精读块，但 md nav「他必须讨好买家」的表述与该句同源（未引无冲突）。
- 词汇表 splayed 例句 "stood stridently confident on massive, splayed legs"——原文逐字。

已核实为正确（R5.5 固定节）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
