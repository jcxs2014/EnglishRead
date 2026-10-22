# ch10（书内 Chapter Nine）R3/R4 对账

| # | 型 | 位置（md） | 现象 | 原文依据（逐字） |
|---|---|---|---|---|
| B1 | 阻断·漏 | 全章无位置 | Gazzie 当场几乎说出另一个人的名字，且原文立刻标注叙述者当时没注意——这是本章留下的最硬的一个接口，md 完全没写 | text/ch10_chapter_nine.txt:48 `...（她几乎说出另一个人的名字）`＋同段 `At the time, I didn’t notice she’d nearly said another person’s name` |
| B2 | 阻断·章内时序 | :94 「为什么这样写」 | 写「本章早前已经给过电路这条现实出口：**姨妈跟她讲过家里的用电毛病**」——本章 Aunt Virginia 那句在 :219，位于本引语块（:216）之后，不是「早前」；本章之前唯一提过电的是叙述者本人（ch09:78） | text/ch10_chapter_nine.txt:219（姨妈）／:216（本块引语）／text/ch09_chapter_eight.txt:78 `the electricity was doing that buzzing thing` |
| B3 | 阻断·章内时序 | :84 「为什么这样写」 | 写「（**前文** She told me herself）」——该句全书唯一命中在 :186，位于本块引语（:180）之后 | 唯一命中：`/usr/bin/grep -rn 'She told me herself' text/` → 仅 text/ch10_chapter_nine.txt:186 |
| B4 | 提示·唯一性 | :96 「读者视角提示」 | 「本章唯一一次超自然『显形』」——本章此前已有两次声息／形体（:60、:93），按「显形＝可感的异象」不成立；建议改「最盛的一次」 | text/ch10_chapter_nine.txt:60 与 :93（另两次异象） |

```
$ /usr/bin/grep -nE 'So did|另一个人的名字|差点说出' "ch10 gazzie tells ironheart curse.md"; echo rc=$?
rc=1        # 真查无（md 侧），text/ 侧同词命中见上
```
