# ch43（Chapter Forty-Two）R3/R4 差异与取证

## 探针

| 探针 | 结果 |
|---|---|
| v43（词表例句逐字） | 14 行，flagged 0 |
| ap43（直撇号＋backtick span） | ASCII 撇号 0，span MISS 0 |
| in43（非块内嵌英文） | 未命中 2，均为模板（`Chapter Forty-Two`／`Tropes`）。首跑曾误报 61 条——派生时 text 文件名替换模式写错（源为 ch42_chapter_forty_one.txt），修正后复跑即 2。工具误用，非 md 缺陷。 |

## 阻断取证

- **C-43-1**（时间错译，先例 C-34-1 同型）：md 原句5「中文理解」写「对方沉默了**五年半**才冒出来敲诈她」——原文 text/ch43_chapter_forty_two.txt:210 "He didn't say anything for **half a decade**, then came out of the woodwork to blackmail me."。half a decade＝五年，中文多出「半」。`/usr/bin/grep -n "half a decade" text/ch43_chapter_forty_two.txt` → L210，rc=0。

## 定点取证（/usr/bin/grep，text/ch43_chapter_forty_two.txt）

- L9 full-sized portrait／no haint…only my grandmother／goosebumps；L45 about-face；L66 "I don't need forgiveness… I don't regret it."；L105 pliers and spool of thick wire。
- L120 bird-boned frame；L162 左手攥钳；L165 "He wasn't dead!"；L174 bolt gun／turn me in if he survived；L180 'Florida Woman Tries to Feed Son to Alligator.'／spare heir／Ironheart was thrilled。
- L204 "Greg wasn't an angel, either."；L207 "Greg," I repeated（Harrison 父亲）；L210 half a decade／blackmail／croaked／"I can't believe I trusted him."；L216 "For Ginny, for your mother. For you."
- L228 hightailed；L234 "run away, Dartrine, purest upholder of good. Run back to Georgia"；L249 "By going to the police."；L255 reprehensible／cause of death recorded as a heart attack。
- L276 "The weight of the pliers slamming into my forehead stunned me."；L278 pushed（years of slaughtering）；L285 vision tunneled／black frame；L288 grim determination。

## 导航断言

14 项断言全部回源命中：断电夜（L9 electricity was out）、堵住（L33/45）、拒绝原谅（L66）、钳子铁丝补围栏（L105/L120）、He wasn't dead（L165）、bolt gun（L174）、头条标题（L180）、Greg 敲诈（L204–210）、For you（L216）、报警宣言（L249）、钳子砸额（L276）、推倒（L278）、vision tunneled（L285）、grim determination（L288）。
