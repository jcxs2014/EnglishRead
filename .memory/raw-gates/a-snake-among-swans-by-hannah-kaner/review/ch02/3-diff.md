# ch02 R3 对账（素读 8 条 ↔ md 11 块）

R1 素读：`1-suread.json`（8 条，intervals_ok 8/8）

## 漏（素读有、md 无）→ 已修

1. **fact 4 的「五天」半句**：md 块 5 只写手足受刑的样子，没写「I spent five days wishing for their deaths」，也没写放箭、派刺客两次失败。
   → 已补进块 5 的 `读者视角提示`。证据：`text/ch02_chapter_two_tilde.txt`「I spent five days wishing for their deaths. We tried to reach them with arrows … we tried to send assassins in the night, but they were caught and killed.」
2. **fact 7 的「银女王六年无音 / Torcros 自封商路」**：全章 0 处提及（`grep -c 银女王/六年` = 0）。
   → 已补进块 7 的 `读者视角提示`。证据：「the silver queen will send ships from the east」与母亲的追问段。
3. **fact 8 的「石根嵌荆棘 + 林语」**：md 只写戒指遇毒变色，`grep -c 荆棘` = 0。
   → 已补进块 11 的 `为什么这样写`。证据：「It was a thorn, set in the ring, at the base of the stone.」＋「Blood in blood, dark hawthorn, with my touch is poison drawn.」

## 编（md 有、原文无）

- 引语：机器层 0 编造。分析句抽查：「咒语式的一节献词」「橘红的花」「a crown of nettle」对应「a crown of nettle woven at his brow」✅；「轮蛇旗是她亲手降下」对应「Our flag of the wheeled snake, she lowered herself」✅。
- 块 6 分析原写「蛇的图腾在这里**第一次**低头」→ 已在前一轮改成「随这面旗一起落到地上，是母亲亲手放的」（本轮复核：现状无「第一次」）。⇒ 编 0。

## 错（主语/因果/数字/时序）

- 块 1「玫瑰总让我想起 Sanafin」→ 原文 `the roses had always reminded me of Sanafin` 同段 ✅。
- 块 3「她死后的第二天就整块消失」→ 原文 `in the day after her death I realised that the memory was gone` ✅。
- 块 6「末代国王」→ 原文 `the last king of Ardwen`（原文用 king，虽指 Rivani）✅。
- 时序：packing（fact 1）→ 禁令（2）→ 开城（3）→ 受刑（4）→ 质问（5）→ 生子要求（6）→ 银女王（7）→ 戒指（8）——md 块序 1→2→3→4→5→6→7→8→9→10→11 与原文一致 ✅。

## 小结

阻断 3（均为漏）→ **已全部修复**（3 处分析补写，未动引语、未改块序）；提示 0。
修后 `chapter.sh` rc=0（引语 11 块 / 片段 13 / 查无 0）。
