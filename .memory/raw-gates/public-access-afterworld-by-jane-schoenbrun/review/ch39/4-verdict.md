# R4 逐块判定 · ch39（captain video swallows）

机层：review/ch39/2-machine.json（EXIT=0）；引语逐字 6/6、词汇 FAIL=0；修复后整书 gate EXIT=0。

| 块 | 引语↔中文理解↔关键词↔分析 | 施事三问 | 判 |
|---|---|---|---|
| 1 | a speck/cinematic universe｜墓志铭初稿 | 说话人=屏幕上的 Erin 分身（text "the Erin on the screen said"）；「童谣→悼词转调」与 ch08 原诗变形关系 ✓ | ✓正确 |
| 2 | to HBO/nefarious｜媒介时间折叠 | 说话人=Mary（未来 HBO 采访）；被评者=David（脖子淤青）——「案发当日即被撰写档案」判断 ✓ | ✓正确 |
| 3 | I get it now/I never was｜离场和解词 | 说话人=Erin（对 David 说的平静告别）；「她不是将要成为虚构，她从来就是」与 text 存在论否认一致 | ✓正确（修复后） |
| 4 | burst open/cosmic vacuum cleaner｜吞噬机械美学 | 开门者=video store 自身（门在她身后炸开）；卷走者=风/宇宙吸尘器；被卷者=Erin——「铃=开门营业」与 ch26 开业呼应 ✓ | ✓正确 |
| 5 | ripped from herself/anyone at all｜两层死亡 | 离场者=Erin（尖叫哭泣）；两问的受问对象：世界→自己——「终极问卷」与 ch78 的回答呼应 ✓ | ✓正确 |
| 6 | shared work/stray signal｜守夜编制化 | 守望者=David、等待对象=漏网的 Erin（stray signal）——「爱好变岗位」与 ch28/ch30 的 Fisch 支线互证 ✓ | ✓正确 |

跨章引用：b1（ch08）、b2（ch02）、b3（ch38——已修复）、b4（ch26）、b5（ch39 自身分身）、b6（ch28/ch30）——章号与内容全部核对正确。
数字断言：一小时（an hour later David got home）text 逐字 ✓。

## 断言 | 证据 | 结论 | 档位
- 「自我更正注释+两处查无引语」（原提示 3） | grep ch07 "not sure they're even still alive"=0；grep ch19 "I'm not really here"=0 | 错（生成残留+查无引语）| 阻断→已修复（改 ch38 同章衔接）
- 「Erin 最后两问在最后两集得到回答」 | text/ch77 "she sees you and me, all of us…alive and dead" + ch78 "We hold on to the image…" | 成立（结构预告）| 已核实为正确

## 已核实为正确
- 原句 1–6 引语逐字；词汇 9 条例句命中本章。
- 修复后 gate.sh EXIT=0，ch39 单章 rc=0 ✓。
