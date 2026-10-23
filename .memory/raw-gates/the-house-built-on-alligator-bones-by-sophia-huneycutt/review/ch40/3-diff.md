# ch40（Chapter Thirty-Nine）R3/R4 差异与取证

## 探针

| 探针 | 结果 |
|---|---|
| v40（词表例句逐字） | 20 行，flagged 0 |
| ap40（直撇号＋backtick span） | ASCII 撇号 0，span MISS 0 |
| in40（非块内嵌英文） | 未命中 2，均为模板（`Chapter Thirty-Nine`／`Tropes`） |

## 定点取证（/usr/bin/grep，text/ch40_chapter_thirty_nine.txt）

- L9 lockbox on his dresser；L12 crowbar 撬开；L21 证据清单（fireman's report／pink highlighter／accelerants／two identical accounting books／Brian Yelton, Mayor／promotion to chief／George R. 两张手写便条／Publix parking lot／confirming egg totals）；L24 原句2 全句。
- L42 "He was friends with your uncle, Leon. Best friends." —— 导航「Leon 最好的朋友」。
- L66 "She did it. She killed him."；L84 "rewarding me for good behavior"＋"wanted me to argue with Harrison"；L87 "I reined in my fury."
- L90 "Tell me everything."；L123 封口费段（money to stay quiet／hated himself／grown up together／summer job…spy on her）；L126 "Spy." This was getting more and more ridiculous.
- L138 "six summers ago…beach ball…"；L159 "tried ruining property, tried sending a message with the knives…" —— 毁财产＋用刀传话；L165 "worried you'd be like her"。
- L174 honest by nature／spin lie after lie；L177 "I refused to let my anger die."
- L180 "That's over."；L192 "You should hear it from family."；L195 "He wasn't even my boyfriend, or my lover. Or a friend."
- L201 "Ask Ginny," … "Gazzie's dangerous."
- L204 "Why would I listen to you? Or her?"
- L216 Gazzie directly under Ida's portrait／water rippling／skirt billowing；L222 "It was eight in the evening but dark as midnight…Hurricane Flora"；L228 "Where the hell do you think you're going?"

## 查无声明（命令+输出+退出码）

- `/usr/bin/grep -n "best friend" text/ch40_chapter_thirty_nine.txt` → 无输出 rc=1——复数为 "Best friends."（L42），非缺陷。
- `/usr/bin/grep -n -i "knife" text/ch40_chapter_thirty_nine.txt`（首轮）→ 无输出 rc=1——原文 L159 为复数 "the knives"，非缺陷。
