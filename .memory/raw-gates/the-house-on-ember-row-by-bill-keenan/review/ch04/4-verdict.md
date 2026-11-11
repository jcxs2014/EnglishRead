# ch04 R4 逐块判定表

| 块 | 引语↔中文理解↔关键词↔为什么这样写 | 施事三问 | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 报馆危机对应（piece/bones/finished） | need 主语=we（Gordon）✓；find 主语=we ✓ | 对应 | 通过 |
| 2 | 三无现场+干预假设对应（disappeared/suspects/docks） | disappeared 主语=It（案）✓；found 否定主语=they ✓；throw 主语=people ✓；wanted 主语=someone ✓ | 对应 | 通过 |
| 3 | 档案腔对应（official record/Cade Jensen/End of story） | says 主语=record ✓；ruled 受事=Cade Jensen 死因 ✓ | 对应 | 通过 |
| 4 | 三件事判词对应（disappear too fast/all three/pursued） | disappear 主语=that（案子）✓；pursued 主语=no one ✓ | 对应 | 通过 |
| 5 | 章末收束对应（let it go/stuck/why） | walked 主语=I ✓；stuck 主语=the way ✓；wanted 主语=I ✓ | 对应 | 通过 |

## 断言类核查

- 「Gordon 三十六岁」：原文 "At thirty-six, his hair had already started its swift retreat"（text/ch04:20）✓。
- 「官方版本被压成一行档案体（姓名—职业—死因）」：原文 "Cade Jensen, real estate developer, suicide."（text/ch04:82）✓。
- 「Eloise 首次被提及」：取证 `/usr/bin/grep -c 'Eloise' text/ch01*.txt text/ch02*.txt text/ch03*.txt` → 0/0/0；text/ch04:140 "Hey, I'm the picture of health. Eloise says so." 首现 ✓。
- 词表 14 条例句逐字核对：MISS 0。

## 已核实为正确

- 「quinn 说每个故事无非三件事」：原文 "Quinn, every story is about one of three things—" / "Power, money, or revenge"（text/ch04:195-198）✓（md 块 4 引语取后半，说话人=Gordon 补刀正确）。
- 「a story with bones 用身体意象定义好新闻」：原文逐字（text/ch04:48）✓。

**ch04 结论：阻断 0 / 提示 0 / 假红 0 / 跳过 0。**
