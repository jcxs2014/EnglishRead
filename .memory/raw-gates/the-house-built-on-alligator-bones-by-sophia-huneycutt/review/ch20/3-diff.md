# ch20（书内 Chapter Nineteen）R3/R4 对账

| # | 型 | 位置（md） | 现象 | 原文依据（逐字） |
|---|---|---|---|---|
| C1 | 阻断·漏 | 全章无位置 | 本章埋着母亲档案的第二处谎：Gazzie 说 Caroline 读的是 UNF、从家里通勤，而叙述者一直以为她在 Savannah 上大学——md 全无（`UNF` 0／`Jacksonville` 0／`大学` 0／`Savannah` 0） | text/ch20_chapter_nineteen.txt:354–360 `Went to UNF in Jacksonville. Commuted from here.` |
| C2 | 阻断·漏 | 全章无位置 | 「两人可信圈」（Harrison 与 Nova 之外无人可信的那句界定）未落位，导致本章「先盯住 Joe」的决定少了前提 | text/ch20_chapter_nineteen.txt:291 `...two-person circle of trust...` |
| C3 | 提示 | 一句话总结（:108）隐现 | 摄像头断电的具体口径（只有剥皮房附近那几台、恰在她离开去吃午饭五分钟后）只在总结层以「关掉监控」出现，缺「哪几台／多久」这两格可核信息 | text/ch20_chapter_nineteen.txt:240–246 `Just the ones around the skinning room. About five minutes after you left for lunch.` |
| C4 | 提示·范围歧义 | :36 「读者视角提示」 | 「原文没有说 Ida 究竟做过什么」——「原文」指本章还是全书有歧义（Ida 的事迹在 ch10 由 Gazzie 给出整版；本章确实没有） | 建议限定为「本章没有说」 |

```
$ cd text && for w in UNF Jacksonville Savannah 摄像头; do printf "%s: " "$w"; /usr/bin/grep -lw "$w" *.txt | tr '\n' ' '; done
UNF: ch20_chapter_nineteen.txt
Jacksonville: ch02 ch04 ch08 ch20 ch26 ch45
Savannah: ch02 ch04 ch06 ch08 ch10 ch13 ch16 ch18 ch20 ch22 ch24 ch28 ch32 ch38
```
