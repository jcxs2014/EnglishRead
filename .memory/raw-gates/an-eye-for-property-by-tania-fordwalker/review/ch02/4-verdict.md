# ch02 · R4/R5 判定表

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 画家揭示（签名=她名字）章内零覆盖 | text/ch02: The signature on the top painting is your name. | 阻断（修复前）→ 已修复：补原句3（无框油画+You are an artist），后续块重编号 | 阻断→已修 |
| 原句1 …接（sentimentality 段→While the house 段） | text/ch02 相邻两段 | 两段各自连续、verify_fragments_indep 76 段 MISS 0 | 假红排除 |

R2：chapter.sh --json rc=0（2-machine.json 在同目录）；R1 素读 8 条锚点 8/8 命中。

## 已核实为正确
- text/ch02 相邻两段（原句1 …接（sentimentality 段→While the house 段））
- 引语逐字：本章全部引语块 verify_fragments_indep 逐段命中（MISS 0）。
