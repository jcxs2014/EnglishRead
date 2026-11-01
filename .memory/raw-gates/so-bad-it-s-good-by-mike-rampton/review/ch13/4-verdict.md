# ch13 Hauntingly Terrible Spooky Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 骷髅不打闹 | :15 | 是：guts 双义 | guts ✅ | 打＝骷髅 ✅ | 通过 |
| 2 鬼屋住客 | :25 | 是：反转＝说者自己是鬼 | housemates / haunted ✅ | 住＝我 ✅ | 通过 |
| 3 德古拉 | :37 | 是：neck-romancer≈necromancer | neck-romancer ✅ | 咬＝德古拉 ✅ | 通过 |
| 4 恶魔的墓地 | :79 | 是：evil 的反写 | demons / ghouls ✅ | 找＝人 ✅ | 通过 |
| 5 狼人 | :84 | 是：拖长嚎叫拼写 | werewolf ✅ | 变身＝我 ✅ | 通过 |
| 6 幽灵鸡 | :94 | 是：poultrygeist | poultrygeist ✅ | 叫＝鸡 ✅ | 通过 |
| 7 吸血鬼写信 | :99 | 是：Tomb it may concern | Tomb it may concern ✅ | 写＝吸血鬼 ✅ | 通过 |
| 8 与死神打牌 | :174 | 是：scythe/sigh 谐音 | scythe ✅ | 挑战＝你 ✅ | 通过 |
| 9 蝙蝠出门 | :195 | 是：血从哪来 | lamp post ✅ | 吸血＝蝙蝠 ✅ | 通过 |
| 10 灯柱答案 | :195 | 是：看不见即证据 | lamp post ✅ | 撞＝蝙蝠 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 35 条（原写"约三十"） | 37 段 − 2 标题 | 改后正确 | 提示已修 |
| 400 年 | `:25` | 正确 | 通过 |
| 钟敲十三下 | `:174` 前段 | 正确 | 通过 |
| 字符数 3,206（原写 3,100） | `len(text)` | 改后正确 | 提示已修 |
| 蝙蝠段约九倍于中位条目（原写十倍） | 101 词 vs 中位 11 词 | 改后正确 | 提示已修 |

## 已核实为正确

- 原句 2 的"我才是鬼"是原文自带的转折（`:25` 末句 `…there are no ghosts here. I’ve been here for 400 years.` 一类表述），非 md 加戏。
- 原句 7 的 Tomb it may concern：`:99` 原文逐字，md「表达方式」点明 To whom it may concern 的替换。
- 原句 9/10 的拆分：`:195` 是一段长叙事，md 按句界劈成两块（T1 时因 >100 词触发 ⚠️ 而拆），两块引语各自逐字。

## 结论

阻断 0 / 提示 3（均已修）/ 假红 0。
