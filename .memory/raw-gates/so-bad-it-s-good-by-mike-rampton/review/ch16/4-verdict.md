# ch16 Maths and Science Jokes That Just Don't Add Up 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 冰人 | :14 | 是：ice guy | ice guy / 0 degrees ✅ | 遇见＝我 ✅ | 通过 |
| 2 中子进酒吧 | :19 | 是：No charge | neutron / charge ✅ | 请＝酒保 ✅ | 通过 |
| 3 原子 make up | :24 | 是：构成/编造 | make up ✅ | 不信＝科学家 ✅ | 通过 |
| 4 光子轻装 | :36 | 是：travelling light | travelling light ✅ | 说＝光子 ✅ | 通过 |
| 5 丢电子 | :41 | 是：positive 双义 | positive ✅ | 问＝朋友 ✅ | 通过 |
| 6 薛定谔通缉 | :51 | 是：dead and alive | wanted / alive ✅ | 通缉＝警方 ✅ | 通过 |
| 7 平行线 | :56 | 是：never meet | parallel ✅ | 说＝作者 ✅ | 通过 |
| 8 猎户座腰带 | :63 | 是：waist/waste | waist of space ✅ | 说＝作者 ✅ | 通过 |
| 9 二进制 10 类人 | :68 | 是：10=2 | 10 types ✅ | 说＝作者 ✅ | 通过 |
| 10 Oct 31=Dec 25 | :238 | 是：八进制 31=25 | Oct / Dec ✅ | 混淆＝程序员 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 43 条（38+5，原写"约 34"） | 47 段 − 2 标题 − 2 抬头 | 改后正确 | 提示已修 |
| 712 词 | `len(text.split())`=712 | 正确 | 通过 |
| 字符数 4,126（md 写"约 4,100"） | `len(text)` | 正确 | 通过 |
| 5 条天才小节 | 段 42–46 | 正确 | 通过 |

## 已核实为正确

- 原句 2 的 No charge：`:19` 原文酒保台词，md 保留"不收费/不带电"双解，未写成"免费喝酒"。
- 原句 5 的 positive：`:41` 原文 `‘I’m positive’`，md 未把电荷正负说反。
- 原句 6 的 wanted dead and alive：`:51` 原文逐字（通缉令 "dead or alive" 的改写）。
- T1 时删掉的 `superposition` 词条仍不在本章词表内（全书查无），已核实。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
