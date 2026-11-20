# ch11 4-verdict（T3 深审）

R1：review/ch11/1-suread.json（8 条，子代理盲读，自检全 PASS）。
R2：review/ch11/2-machine.json（chapter.sh --json verdict=ok，rc=0；8 块 10 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 抢时间救人 | before Grenault found Pierre/silver-tipped bolts/he would kill him 在引语 | 杀意施事=Grenault、受事=Pierre ✓；"concluded" 推理动词中文"一旦断定" ✓ | 对应 |
| 2 | 八英尺持炉栅 | eight-foot height/a large plate of metal/slash at 在引语 | Grenault 立于她与桌案之间 ✓；挥爪目标=Leóne 的脸 ✓ | 对应 |
| 3 | 倒数如丧钟 | blood surged/short gasps/a death knell 在引语 | "His countdown of my remaining bolts" 施事=Grenault、受物=她的余弹 ✓ | 对应 |
| 4 | 织针反击 | knitting needles/lunging at his back/shocking savagery 在引语 | 施刺者=Madame Leóne、受击者=Grenault 背 ✓；"Run, Helena!" 喊话方向（她→Helena）✓ | 对应 |
| 5 | 一记反手 | backhanded/sending her flying/unconscious 在引语 | Grenault 反手、Leóne 受击撞柱 ✓ | 对应 |
| 6 | 倒数清零 | deflected it easily/None/steady my breathing 在引语 | he=Grenault 挡箭 ✓；"I stood…"=她 ✓；两段 text 相邻完整段 ✓ | 对应 |
| 7 | 缴械对视 | felt naked/stand my ground/the last monstrous face 在引语 | "his hideous yellow eyes"=Grenault ✓ | 对应 |
| 8 | 钉墙宣判 | ramming me against it/drove his claws a little deeper/It's over 在引语 | 他撞她、爪入肉 ✓；"It's over, little Helena." 说话人=Grenault ✓ | 对应 |

跨章引用核章号：块6 提示引 "Weapons are all around you"（Francois 语）——text/ch06_6.txt "Weapons are all around you, if you look." ✓ 章号 ch06 正确；块8 提示 "little Helena" 降格称谓链（ch01 "little girl"→ch05 "Mademoiselle"→ch11）✓。
数字回原文：十箭=Nine→None 倒数合计（text/ch11_11.txt 九、八、六、五、四、三、一、none 各报数逐字在案）；两根织针="two large knitting needles" ✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 烧铺子威胁/prize-Prime 重复威胁/银缸冷与夺弩动作 未入块 | ch05 原句7 已全量详写处刑方案；块7 "naked" 承接缴械 | 不修 | 提示×3（依据：重复威胁不再整段复收，转折层全收） |

无修复动作。chapter.sh rc=0。

## 已核实为正确

- 一句话总结"挡尽十箭"——倒数 Nine（首箭后余 9）至 None（末箭余 0）合计恰 10 支，与 repeating crossbow 十发设定（ch09 text）自洽。
- 块4 分析"缝纫工具对狼王的'不对称反击'"——knitting needles 为 text 逐字，武器系谱评论有锚。
- 块8 引语以 … 接 "It's over, little Helena."（独立完整段，text/ch11_11.txt 末段）——多段合法，fragments 独立取证命中。
