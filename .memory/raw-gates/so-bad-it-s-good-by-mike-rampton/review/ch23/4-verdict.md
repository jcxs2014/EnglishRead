# ch23 Unlovably Bad Family and Relationship Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 网球选手 | :15 | 是：love=零分 | love ✅ | 别约会＝你 ✅ | 通过 |
| 2 in-laws/outlaws | :20 | 是：wanted 双义 | outlaws / wanted ✅ | 被通缉＝亡命徒 ✅ | 通过 |
| 3 公路标志 | :25 | 是：signs 双义 | signs ✅ | 约会＝我 ✅ | 通过 |
| 4 公主与奥地利 | :37 | 是：联姻巩固王国 | Austria ✅ | 嫁＝女友 ✅ | 通过 |
| 5 火烈鸟 | :42 | 是：put my foot down | foot down ✅ | 学＝我 ✅ | 通过 |
| 6 口红与固体胶 | :69 | 是：递错东西 | glue stick ✅ | 递＝我 ✅ | 通过 |
| 7 邋遢孩子 | :20 | 是：Attire/a tyre | attire ✅ | 骑＝孩子 ✅ | 通过 |
| 8 香料架标签 | :127 | 是：thyme time/cumin coming | thyme / cumin ✅ | 换＝我 ✅ | 通过 |
| 9 折叠梯 | :94 | 是：step+ladder 拆词 | stepladder ✅ | 有＝我 ✅ | 通过 |
| 10 拖延 | :204 | 是：Just you wait | procrastinate ✅ | 说＝我 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 38 条（原写"约 35"） | 40 段 − 2 标题 | 改后正确 | 提示已修 |
| 629 词 | `len(text.split())`=629 | 正确 | 通过 |
| 字符数 3,599（md 写"约 3,600"） | `len(text)` | 正确 | 通过 |
| 五十年假牙 | `:204` 前后 | 正确 | 通过 |

## 已核实为正确

- 原句 7 的 `attire` 谐音：`:20` 原文 `…a scruffy kid on a bike and a smartly dressed kid on a tricycle? Attire`（a tyre 的听岔），md 写作"穿着"，双关在「中文理解」里给出。
- 原句 8 的 cumin/coming：`:127` 原文 `…but cumin`（coming），md 译"'百里香'快来了"保留 thyme/cumin 两个食材词。
- 原句 10 的 `Just you wait…`（`:204`）以省略号结尾，md 引语照抄并保留省略号，机器校验通过。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
