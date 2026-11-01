# ch28 Criminally Bad Police Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 厕所被偷 | :17 | 是：nothing to go on | nothing to go on ✅ | 说＝警方 ✅ | 通过 |
| 2 车轮被偷 | :22 | 是：tirelessly | tirelessly ✅ | 说＝警方 ✅ | 通过 |
| 3 裸体营篱笆 | :35 | 是：looking into it | looking into ✅ | 说＝警方 ✅ | 通过 |
| 4 假发厂 | :40 | 是：combing | combing ✅ | 查＝警方 ✅ | 通过 |
| 5 T-rex 卖枪 | :55 | 是：small arms | small arms ✅ | 逮捕＝警方 ✅ | 通过 |
| 6 两船相撞 | :73 | 是：marooned | marooned ✅ | 撞＝两船 ✅ | 通过 |
| 7 监狱编号 | :130 | 是：只报数字、表演失败 | number ✅ | 讲＝犯人 ✅ | 通过 |
| 8 Stradivarius | :150 | 是：violins/violence | violins ✅ | 偷＝贼 ✅ | 通过 |
| 9 take a fence | :167 | 是：take offence | take a fence ✅ | 说＝你 ✅ | 通过 |
| 10 咖啡杯 mugshots | :172 | 是：mug/mugshot | mugshots ✅ | 发＝警方 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 33 条（原写"约 35"） | 35 段 − 2 标题 | 改后正确 | 提示已修 |
| 监狱故事 160 词（原写 180） | `:140` 段词数 | 改后正确 | 提示已修 |
| 782 词 | `len(text.split())`=782 | 正确 | 通过 |
| 10,000 只蜜蜂 | `:73` 附近 | 正确 | 通过 |

## 已核实为正确

- 原句 7 的编号笑话是整章唯一长段（160 词），md 未把它拆块，机器校验通过。
- 原句 5 的 T-rex `small arms`（`:55`）双关：武器／小短手，md 解释正确。
- 原句 9 的 `Nothin’, just take a fence`（`:167`）——take offence 的谐音，md 未写成"拿走栅栏"就收。

## 结论

阻断 0 / 提示 2（已修）/ 假红 0。
