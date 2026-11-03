# ch18 对账（R3）

> R1 素读：`review/ch18/1-suread.json`（facts 8，锚点 8/8 命中 text/，start-end 一致）
> R2 机器层：`review/ch18/2-machine.json`（chapter.sh --json，verdict=ok；块 10 / 引语 10 / segments 11 / segment_miss 0）
> R4 人判：`review/ch18/4-verdict.md`（10/10 块逐块核对）

## 漏（R1 有、md 无）
- 无。R1 8 条（手写留言、绿玻璃叶形盘至少一万五 nox、Jade 的声音在脑里、Flint 感染发烧、自述被迫自卫杀 Jade、刻「F + P」、父亲的老鹰纹身、摘表与罗盘）全部由导航或块覆盖。

## 编（md 有、原文无）
- 无。Obscuris、fifteen thousand nox、cellulitis、blood poisoning、two hundred hours 均可回原文命中。

## 错（两边都有但不一致）
- 错 1【提示级】块 8 中文理解与总结未出现父亲的名字：原文 `text/ch18_chapter_eighteen.txt:105-106`「With you every second, / Love, Sapphire and Petra」——表背刻着母亲 **Sapphire** 与 Petra 的名字；`/usr/bin/grep -rn "Sapphire" text/` 全书仅此一处命中，md 全书 0 命中。md `:104` 中文理解只写「我把那块表放进口袋，和罗盘放在一起」，`:174` 总结写「刻着母亲和自己名字的表」未点出母亲名。属**未写**而非写错，判提示级（可选补写）。

## 结论
R3 三单：漏 0、编 0、错 1。漏 0、编 0、错 1（表背刻字未译，提示级可选补写）。已列入修复指令。
