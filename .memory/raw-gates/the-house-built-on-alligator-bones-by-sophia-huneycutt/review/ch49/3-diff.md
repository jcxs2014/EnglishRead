# ch49（Epilogue）R3/R4 对账

| # | 型 | 位置（md） | 现象 | 原文依据（逐字） |
|---|---|---|---|---|
| F1 | 阻断·漏 | 全章无位置 | 尾声除「拆房／续脉」两问外还处理了 Ironheart 一条账（它是否也算在协议之内、以及人还能不与它沟通），md 完全没落（`Ironheart` 0／`agreement` 0／`commune` 0） | text/ch49_epilogue.txt:39 `There’s also Ironheart to consider… Was that part of our agreement?… One doesn’t commune with Ironheart, at least not anymore.` |
| F2 | 阻断·对应（因果错位） | :11 「情感弧线位置」 | 把「笑意在嘴唇上铺开」的因由写成「因为 Ida 会恨看到 Greer House 被夷平」；原文 that 指「遗体的罐子被风雨赶出去、与鳄鱼骨混在一处」，「Greer House 被夷平」是以 `too` 追加的第二条理由 | text/ch49_epilogue.txt:36（`…evicted them…to mingle with the alligator bones` 之后接 `…and what if Greer House was demolished too`，笑意随该句铺开） |
| F3 | 提示 | 全章无位置 | 「这是五年来第一本这么黑的速写本……像 Uncle Leon 的」未落位（`五年来` 0／`油画` 0） | text/ch49_epilogue.txt:12 `This is the first sketchbook I’ve done in five years that’s this dark… like Uncle Leon’s` |

```
$ /usr/bin/grep -nE 'Ironheart|agreement|commune' "ch49 dart decides on demolition and a daughter.md"; echo rc=$?
rc=1
```
