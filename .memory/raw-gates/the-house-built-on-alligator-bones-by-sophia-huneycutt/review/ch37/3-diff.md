# ch37（Chapter Thirty-Six）R3/R4 差异与取证

## 探针

| 探针 | 结果 |
|---|---|
| v37（词表例句逐字） | 14 行，flagged 0 |
| ap37（直撇号＋backtick span） | ASCII 撇号 0，span MISS 0 |
| in37（非块内嵌英文） | 未命中 3：`Chapter Thirty-Six`（模板）、`Tropes`（模板）、`elegant, beautiful, almost`（→F-37-1） |

## 逐项取证（/usr/bin/grep，text/ch37_chapter_thirty_six.txt）

- L12 Winchester 1894／subsequent hunts／demanded that I try —— 原1 引语+关键词全中。
- L42 "Smart, too. …as long as you let them be."／tusks —— 原4「前声兑现」链成立（L177、L201 再现 tusks）。
- L81 "I knew I was sulking like a teenager… I knew who'd been behind everything." —— sulking、幕后断言。
- L84 "Do you like this?" I asked hopelessly —— hopelessly。
- L114 phosphate/sugarcane/imperial/Victorian/Very Ida —— 原2。
- L123 enclosed habitat／"it was elegant. Beautiful, almost." —— 原3＋审美断言（三词两段，合成串查无＝引理拼接）。
- L165 "I'm your backup." —— 词汇 backup 例句。
- L183 "my fingers froze on the cold steel trigger" —— 「对猪没敢扣扳机」。
- L204 "A bang sounded behind me, and a bullet zipped past my hip."＋后句 "Missed," Gazzie muttered —— 开枪者是 Gazzie 且未中，导航表述无误。
- L222 twenty miles per hour／hurtled toward her —— 原5。
- L231 "Had I killed it? No—a streak of red had formed on its lower side." —— 原6。
- L276 great-great-granddaughter／Gazzie's granddaughter／just once。
- L282 "I imagined Ida's hands guiding mine, soft and small and steady…"＋"Reaching around the alligator's throat, I plunged in the knife and pulled." —— 原7＋割喉执行者=她。
- L288 "Not a frog, not a cricket. The bugs had disappeared."＋L289 "Ida had stilled them, for now." —— 失声句号＋解读归属。
- L300／L303 placed it on my cheek／smearing it down a cheek／fruit of her violence —— 原8。
- L309 "Ironheart's death was our beginning… Greers are born with a devil in their hearts."（rasped, voice distorted, Not quite hers）。
- L312 "I turned to the side and threw up."
- L111 "Nature is Ironheart, Dartrine." —— Dartrine 为原文真名。

## 查无声明（命令+输出+退出码）

`/usr/bin/grep -n "elegant, beautiful, almost" text/ch37_chapter_thirty_six.txt` → 无输出，rc=1（合成串不存在；三词分别在 L123、L123、L294）。
