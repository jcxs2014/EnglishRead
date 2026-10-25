# ch02 R4 逐块对应 + R5 判定

**R2**：verdict=ok（12 块，counts 全 0，words 3879 target [7,12]——12 落在区间内）。

**R4 施事抽核 4 块**：
- 块5（pall slime）：中文=她认出淤泥令学生退后——施事 Maggie ✓（原文 "That is pall slime," she said）。
- 块8（Diadhan 封门）：中文=她画符文诵咒封门——施事 Maggie ✓（原文 she placed her palm）。
- 块9（three p.m. session）：中文=他的辩解自证事故归属——推断句注明「must mean」逻辑，与原文同句 ✓。
- 块12（same careful strokes）：中文=她认出封印笔法出自同一只手——受事符文、施事 Taliesin ✓。

**R5 判定表**：
| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 疏散路线/人数未入 md | /usr/bin/grep -o '42\|南梯' = 0 命中 | 过程性事实非转折 | 提示 |
| 块9 归属推断 | text/ch02「that must mean the pall formed in his lab」逐字 | 推断有原文句支撑 | — |
| 引语逐字/对应/形态 | 2-machine.json verdict ok | 通过 | — |
