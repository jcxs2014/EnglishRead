# R3 对账 · ch23

- 素读：review/ch23/1-suread.json（盲读子代理产出）；生产素读 production/ch23-facts.txt 对照。
- R1 盲读对照：子代理 fact4（Ben 窃药+雇守卫）与 t#4 对应 ✓；fact6（Suppose I don’t send you back/1938）与 t#6 对应 ✓；fact8（冷手钩子）与 t#9 对应 ✓。
- 三单结论：漏 0（转折点/结尾钩子均已入块）；编 0（无凭空情节）；错 1（见下）。

| 档 | 位置 | 问题 | 证据 | 修复方向 |
|---|---|---|---|---|
| 阻断 | ch23 t#8 RD | 「这些稿纸在结尾章会成为关键物证（她写给谁的？）」——原书结局（ch25–27）无稿纸回收：ch26 的 papers 是 Ben 信封文件，ch27 是信件；该伏笔在原书中悬置，md 断言与原书结局不符 | /usr/bin/grep -c "pages|paper" text/ch25=0、ch26=2（sheaf of papers=Ben 文件）、ch27=1（a paper=信纸）——均非 ch23 稿纸 | 改为「这些稿纸随她留下（原书未再回收）——伏笔悬置本身是留白的一部分」 |
