# ch03 T3 判定

覆盖：R1 text-only 7 事实、R2 JSON rc=0、R3 三账、R4 原句 1–7 全块逐对人判。

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 「唇毛都不许动」 | text/ch03_2_blair.txt:64 “I feel my top lip twitch with satisfaction, thinking about how wrong they were – even with the 0.5ml recently injected that shouldn’t budge at all.”；md:63 | top lip 是上唇，不是唇毛；改译 | 阻断 |
| 「下一章的会面从她迟到的那一刻开始」 | text:97 “before we’ve even had a chance to stand on the wicker doormat and ring the bell.”；下一件 text/ch04_3_cassie.txt 是 Cassie 视角 | 未迟到且下一章非 Blair 会面，删该断言 | 阻断 |
| 「后面每一条都会逐项对账」 | text:61；md:55 | 无证前瞻，建议改为开放式提示 | 提示 |

四组数：逐字 7/7；对应 7/7；形态 5 导航/4 子项/7 块；断言 2 阻断、1 提示。已按指令就地修复；chapter.sh rc=0，整书 gate EXIT=0。

## 已核实为正确
- 三个月交往、0.5ml 注射、粉色摩根石戒指、辞去酒吧夜班均在本章 text:43,64,82。
