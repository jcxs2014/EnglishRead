# ch39（书内 Chapter Thirty-Eight）R3/R4 对账

| # | 型 | 位置（md） | 现象 | 原文依据（逐字） |
|---|---|---|---|---|
| E1 | 阻断·对应（译文语病＋分析同误） | :20 「中文理解」／:24 「为什么这样写」 | 译成「没有门**自行动**上」并推论为「门关不上」；原文是否定「门自己关上」这件事**没有发生**，用来证明 Ida 不在看——md 把「没发生」写成了「关不上」，方向相反，且中文句子不通 | text/ch39_chapter_thirty_eight.txt:9 `No doors closed on their own, no one muttered; Ida’s focus was elsewhere.` |
| E2 | 阻断·断言（清点不全） | :13 「人物弧线」 | 「Harrison 在本章只交出两样：一把撬棒、一句安抚」——原文他交出的是梯子**和**撬棒，另还有放风、把她拉起、帮她把脚从地板里弄出、检查脚踝 | text/ch39_chapter_thirty_eight.txt:75 `a ladder and a crowbar`；:162、:171（拉起／处理脚踝） |
| E3 | 阻断·漏 | 全章无位置 | 她自我开解清单里明确有一条「Gazzie 未经她同意就启动了改名程序」，是本章「关系」这条代价的具体凭据，md 全无（`改名`／`名字`／`name` 0 命中） | text/ch39_chapter_thirty_eight.txt:12 `she’d started the process of changing my name without my consent`（回收 text/ch38:201） |
| E4 | 提示 | 全章无位置 | `She’s holding court`（对 Gazzie 办公室场面的定性）未落位 | text/ch39_chapter_thirty_eight.txt:81 |

```
$ /usr/bin/grep -nE '改名|名字|name' "ch39 lockbox hidden in the greer house attic.md"; echo rc=$?
rc=1
```
