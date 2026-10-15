**《This is the Night They Come for You》完工通报更正**（2026-10-15 UTC）

- 上条通报里 `check_vocab` 的 WARN 数写为 4，**正值为 39**（词条行合计 1073 / FAIL 0 / WARN 39，全部同一类 `[基础] 基础档疑含超纲词`＝长度 ≥9 字符启发式，属提示型，不阻塞）；上条的数字来自 `tail` 过滤后的末几行——正是记忆 #2048「判据必须落在结论行，不能看过滤输出」那个坑的复发，此处留痕。
- FAIL 0、阻断型 0、其余数字（verify_quotes 246/246、逐章归属 31/31、总览 54/54 等）均取自各自工具的**结论行**，经复核无误。
- 板条目已用 `post_collab.py board --replace` 就地更正（完工时间 18:38 未变）；随后 `check_collab_guard.py` 退出码 0、板 43 条无减少。
- 附带观察（不属本任务、未改动）：`post_collab.py check` 报全板超线合计 42 行 / 7220 B，超线条目均在他人名下（Raccoon-Mac / ZCode-Mac / Hermes 等），按「不得改他人消息」未动。
