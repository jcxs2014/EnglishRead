# ch09 对账（R3）

> R1 素读：`review/ch09/1-suread.json`（facts 8，锚点 8/8 命中 text/，start-end 一致）
> R2 机器层：`review/ch09/2-machine.json`（chapter.sh --json，verdict=ok；块 10 / 引语 10 / segments 11 / segment_miss 0）
> R4 人判：`review/ch09/4-verdict.md`（10/10 块逐块核对）

## 漏（R1 有、md 无）
- 无。R1 8 条（跳进 Henry 死坑、Ruby 拔匕首、Litheo 报价三万 nox、换白光验人、拔眼蘑菇、酸池拽出、Voidling 八 nox 门费、旅店喊 Jade）全部由导航或块覆盖。

## 编（md 有、原文无）
- 无。Ruby、Litheo、Voidling、fiend-infection check、thirty thousand nox 均可回原文命中。

## 错（两边都有但不一致）
- 错 1【提示级】导航「跌进酸池溶化」与原文不符：`text/ch09_chapter_nine.txt:149`「Litheo’s trying to climb out of an acid pool, but his hands slip on the rocks as the flesh sloughs off his fingers.」——他是自己冲进酸池边缘后爬不出，不是「跌进去」；`:153` 是 Ruby 把他拽出来的（Ruby 自己双手被酸灼伤）。正文十块无冲突，错在导航层。

## 结论
R3 三单：漏 0、编 0、错 1。漏 0、编 0、错 1（导航层措辞，提示级）；已列入修复指令。
