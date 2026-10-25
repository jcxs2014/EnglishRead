# ch01 R4 逐块对应 + R5 判定

**R2**：2-machine.json verdict=ok（12 块 12 段，segment_miss 0，counts 全 0，words 2922 target [5,9]——12 块超建议区间为 T1 已记的提示型）。

**R4 逐块（施事/归属抽核 4 块）**：
- 块1（绕远路）：中文=她为躲学生绕路——主语 Maggie ✓，与引语一致。
- 块4（the other rune）：中文=他点破第二枚符文+擦发动作——施事「他」✓（原文 He raised a hand）。
- 块9（Maggie was lost）：中文=她沉沦/记忆焦虑——「她 hoped she never forgot」受事是她自己的记忆 ✓。
- 块12（I can't）：中文=篝火熄灭/天亮刻度+拒绝——「做不到的究竟是摘面具还是爱上」标注为悬念而非事实 ✓。

**R5 判定表**：
| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 块数 12 超本章建议 5–9 | 2-machine.json block_target [5,9] | 对话密集章按事件弧切，T1 已记 | 提示 |
| 年龄 35/33 未入 md | /usr/bin/grep -c '三十五\|33' = 0 | 非转折，未引不阻断 | 提示 |
| 引语逐字/对应/形态 | 2-machine.json verdict ok, segment_miss 0 | 通过 | — |
