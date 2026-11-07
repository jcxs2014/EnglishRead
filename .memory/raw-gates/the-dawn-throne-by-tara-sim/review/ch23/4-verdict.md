# ch23 R4 判定表（10 块逐块 · 施事三问）

| 块 | 引语↔中文对应 | 关键词在引语 | 施事三问 | 断言回源 | 结论 |
|---|---|---|---|---|---|
| 1 | ✅ 程序回顾式忏悔 | ✅ anguish/mercy | 她记得手感 ✅ | 逐字 ✅ | 正确 |
| 2 | ✅ 地理即伤史 | ✅ gash/instigated | Nyx 犁开 ✅ | 逐字 ✅；「第九章 curse in his own veins」= ch09:38 ✅ | 正确 |
| 3 | ✅ 废墟出庭 | ✅ greatness/proud | 她对 Nyx 说 ✅ | 逐字 ✅ | **阻断**：提示「对照 **Perigee 里 Phos** 的「I would rather reduce my world to cinders」」——该句是**第十五章 Deia** 的话（text/ch15:173，grep 命中 1 处、仅此一处）；Perigee 无此句（已修） |
| 4 | ✅ 剑=脊椎 | ✅ astralam/compass | 她对视 ✅ | 逐字 ✅ | 正确 |
| 5 | ✅ 屠杀=乘法 | ✅ Double/memory | Varrick 忍笑下令 ✅ | 逐字 ✅；「第十章 Pathetic」= ch10:152 ✅ | 正确 |
| 6 | ✅ 蔽称里的政变 | ✅ soft/prisoners | Varrick 转述 ✅ | 逐字 ✅ | 正确 |
| 7 | ✅ 名字=圣物 | ✅ worship/penitent | 他低唤 ✅ | 逐字 ✅ | 正确 |
| 8 | ✅ 坦白收刀 | ✅ recoil/already | 她自陈 ✅ | 逐字 ✅ | 提示「第十三章她教 Saya「Don't look」」——Don't look 在**第十七章**（text/ch17:140/146，grep ch13 退出码 1 查无；ch13 时 Saya 尚在别墅）——已修 |
| 9 | ✅ 神偷台词 | ✅ vessel/benefit | Nyx 复述 ✅ | 逐字 ✅ | 正确 |
| 10 | ✅ 死刑令悬置 | ✅ last | （判词句）✅ | **六个词**=And soon to be its last. ✅（T1 已修） | 正确 |

## 已核实为正确（防误修护栏）
- cinders 归属：/usr/bin/grep -rn "reduce my world to cinders" text/ → 命中 1（text/ch15_xv.txt:173，Deia crooned），退出码 0——归属 Deia/第十五章，勿改回 Perigee。
- Don't look 归属：/usr/bin/grep -n "Don’t look" text/ch17_xvii.txt → :140/:146 两处；ch13 同 grep 0 命中退出码 1——归属第十七章。
- 「容器清零」= 她的原话被神复述：text/ch23:335 vs :392 逐字对应，成立。
