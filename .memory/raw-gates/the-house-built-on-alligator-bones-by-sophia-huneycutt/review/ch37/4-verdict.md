# ch37（Chapter Thirty-Six）深审 R5 判定

> 机器层：`2-machine.json` rc=0，8 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 17 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v37 探针 14 行，例句逐字命中 14／14（含 backup L165、bang L204、algae）。
- **撇号**：ap37 直撇号 token 0，backtick span 0。
- **块内嵌英文**：in37 非块内英文 runs 107，未命中 3，其中模板 2（`Chapter Thirty-Six`／`Tropes`），剩 1 见假红 F-37-1。

## R4 逐块对应（8 块）

| 块 | 断言 | 取证（text/ch37_chapter_thirty_six.txt） | 结论 |
|---|---|---|---|
| 原1 | saddled／subsequent／demanded；「不是杀 Ironheart 那支」 | L12 逐字命中 | ✓ |
| 原2 | phosphate/sugarcane/conquering/imperial/Victorian；「She believed」转述 | L114 逐字命中 | ✓ |
| 原3 | enclosed habitat／resembling the wild；「自海边之行后」 | L123 逐字命中（Aunt Virginia） | ✓ |
| 原4 | rip/beady/targeted rage；「Smart, too 前声」 | L201 命中；L42 "Smart, too. …as long as you let them be." | ✓ |
| 原5 | shot out/whipping/twenty miles per hour/hurtled toward her | L222 逐字命中 | ✓ |
| 原6 | Had I killed it? No—／streak/lower side/couldn't believe…at all | L231 逐字命中 | ✓ |
| 原7 | guiding／soft and small and steady／pushed me toward the marsh／handed me the rifle | L282 命中（原句引语部分）＋L282 后 "Reaching around the alligator's throat, I plunged in the knife and pulled."（割喉由她执行）；marsh/handed 的「梦中推送」出处经 1-suread facts 核验 | ✓ |
| 原8 | testing its quality／forefinger／ecstasy／reveling／fruit of her violence | L303 逐字命中 | ✓ |

## 导航层断言

| 断言 | 取证 | 结论 |
|---|---|---|
| 对猪没敢扣扳机 | L183 "my fingers froze on the cold steel trigger" | ✓ |
| Gazzie 开枪未中 | L204 "A bang sounded behind me…"＋"Missed," Gazzie muttered | ✓ |
| 蒙中一枪掐住鳄鱼冲向 Gazzie 的终点 | L222 hurtled toward her→L231 命中 lower side | ✓ |
| 想象中 Ida 覆导割喉；割喉由她执行 | L282 "I imagined Ida's hands guiding mine…"＋"I plunged in the knife and pulled" | ✓ |
| 蘸血手按脸颊、自己舔饮、嗓音失真 | L300／L303／L309 "she rasped, her voice distorted. Not quite hers." | ✓ |
| Ironheart 之死才是 Greer 家的开端 | L309 "Ironheart's death was our beginning"＋L309 devil in their hearts | ✓ |
| 转身呕吐 | L312 "I turned to the side and threw up." | ✓ |
| 蛙、蟋蟀、虫瞬间失声→Ida 让它们安静 | L288 "Not a frog, not a cricket. The bugs had disappeared."＋L289 "Ida had stilled them, for now." | ✓ |
| elegant/beautiful/almost 升起审美 | L123 "it was elegant. Beautiful, almost."（合成串为引理拼接，见 F-37-1） | ✓（内容） |
| sulking／hopelessly | L81／L84 | ✓ |
| 前埋词 tusks、as long as you let them be、twenty miles per hour 兑现 | L42／L177／L201／L222 | ✓ |
| great-great-granddaughter、Gazzie 的孙女、只做一次 | L276 | ✓ |
| 「狩猎镇压不了 Ironheart、我知道幕后是谁」 | L81 "I knew who'd been behind everything." | ✓ |
| "I'm your backup" | L165 | ✓ |
| Winchester 1894＝Ida 晚年猎枪 | L12 | ✓ |
| "a bullet zipped past my hip" | L204 | ✓ |

## 判定汇总

- **阻断：0**
- **提示：0**
- **假红：1**
  - **F-37-1**：in37 探针标 `'elegant, beautiful, almost'` 全书查无——属导航层把 L123 "it was elegant. Beautiful, almost." 三词拼作引理形态，与 F-33-1（outshine）同型：分析层引理拼接非引语，不构成凭空。原词三者在 L123/294 均在。
- 数量/排版断言、亲属链（great-great-granddaughter L276）、Dartrine 真名（L111 "Nature is Ironheart, Dartrine."）均无异常。

## 已核实为正确

- 引语 8 块全部逐字（s37 17 facts MISS 0；机器层 segment_miss 0）。
- 词表 14 行例句逐字、分档无超纲异常。
- 撇号全书弯撇号，md 0 处直撇号。
- 导航/弧线/手法层 16 项断言全部回源命中，无时序倒置、无张冠李戴、无凭空排比。
- 块数 8 与机器层一致。
