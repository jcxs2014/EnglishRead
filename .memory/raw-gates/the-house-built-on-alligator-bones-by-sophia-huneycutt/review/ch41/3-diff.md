# ch41（Chapter Forty）R3/R4 差异与取证

## 探针

| 探针 | 结果 |
|---|---|
| v41（词表例句逐字） | 25 行，flagged 0 |
| ap41（直撇号＋backtick span） | ASCII 撇号 1（md L10 `Ida's`，引原文）→ C-41-1；span MISS 0 |
| in41（非块内嵌英文） | 未命中 5：模板 2（`Chapter Forty`／`Tropes`）＋`feet too hot`（→F-41-1）＋`Gazzie-Caroline`（→F-41-2） |

## 阻断取证

- **C-41-1**：md L10「tainted by Ida's blood」——`/usr/bin/grep -n "Ida’s blood" text/ch41_chapter_forty.txt` → L180 `Ida’s`（弯撇号）rc=0；md 用直撇号。

## 定点取证（/usr/bin/grep，text/ch41_chapter_forty.txt）

- L9 breath came in short bursts／negligence／that, I could forgive；L18 原句2 全句（curious glance／refused／clutching them tighter／caged snake／spin the situation）。
- L30 Cat Two；L36 four hours before Flora hits；L39 "That's so romantic."；L51 "Should you drink more, honey?"。
- L84 boot/grinding（suread）；L87 "My stomach turned."；L90 "Ida laid the entire legacy…on her back"／"to a T, no matter what they were, even when Ida was dead"。
- L93 "Uncle Leon," I said firmly；L99 "What?"；L102 one last shot；L108 "my job was to support the family. Act as peacemaker. That was my inheritance."
- L111 "My feet felt too hot all of a sudden"（→F-41-1 引理来源）；L117 less incriminating；L126 Caroline 揭发；L138 prod 拖尸；L150 "Or what?" I croaked。
- L159 "give her child a chance"；L168 "My mother didn't marry my father? They didn't get a divorce?"；L180 原句7；L183 "Tainted."；L186 wickedness；L189 "born with a devil inside. She meant Ida."
- L195 "She shouldn't have had me"；L201 "Am I?"；L222 "How could you have caused a heart attack?"；L255 marionette。
- L270 "the final key in unraveling his death"；L273 "Harrison told me to ask what Gazzie did"；L285 报纸袋掉包；L288 hurtling through Ocala／distasteful；L306 seawall；L309 raindrops like knives。

## 查无声明（命令+输出+退出码）

- `/usr/bin/grep -n "feet too hot" text/ch41_chapter_forty.txt` → 无输出 rc=1——原文 L111 "My feet felt too hot all of a sudden"（feet felt too hot），导航压缩为引理，见 F-41-1。
- `/usr/bin/grep -n "Gazzie-Caroline" text/ch41_chapter_forty.txt` → 无输出 rc=1——分析层自造连字标签，见 F-41-2。
