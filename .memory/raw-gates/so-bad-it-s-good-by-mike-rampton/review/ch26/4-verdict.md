# ch26 Technology Jokes That Need a Reboot 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 remorse code | :15 | 是：remorse/morse | remorse ✅ | 写＝我 ✅ | 通过 |
| 2 rota/rotor | :20 | 是：YES WE KNOW | rotor ✅ | 命名＝俱乐部 ✅ | 通过 |
| 3 人形电脑 | :25 | 是：十分钟就睡 | human computer ✅ | 睡＝我 ✅ | 通过 |
| 4 爱尔兰 two-factor | :30 | 是：to be sure, to be sure | two-factor ✅ | 说＝爱尔兰人 ✅ | 通过 |
| 5 PayPal/papal | :40 | 是：decree | papal ✅ | 付＝人 ✅ | 通过 |
| 6 beef stew | :94 | 是：不是 stroganoff | stroganoff ✅ | 说＝人 ✅ | 通过 |
| 7 打字员丢 contacts | :109 | 是：联系人/隐形眼镜 | contacts ✅ | 丢＝打字员 ✅ | 通过 |
| 8 caps lock 帽子 | :114 | 是：锁住帽子 | caps lock ✅ | 戴＝手机 ✅ | 通过 |
| 9 site for sour ryes | :124 | 是：sight for sore eyes | sour ryes ✅ | 看＝我 ✅ | 通过 |
| 10 吸尘器 gather dirt | :149 | 是：灰尘/把柄 | dirt ✅ | 偷＝吸尘器 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 32 条 + 8 行清单（原写"约 40 条 + 七行"） | 42 段拆分 | 改后正确 | 提示已修 |
| 7 条 • 清单 | 段 13–19 | 正确 | 通过 |
| 644 词 | `len(text.split())`=644 | 正确 | 通过 |
| 字符数 3,704（md 写"约 3,700"） | `len(text)` | 正确 | 通过 |

## 已核实为正确

- 原句 2 的 `rotor`/`rota`（`:20`）：原文为 "Try To Invent A Helicopter Club" 的缩写玩笑，md 未把 rota 解释成"值班表"就收。
- 原句 10 的 `gathering dirt`（`:149`）：施事是吸尘器，md 写"比手机和电脑更阴"，与原文比较对象一致。
- 清单七条各自独立成段（`:65–` 段），md 未把整段清单拼成一块引语，符合"块不跨段"的门禁要求。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
