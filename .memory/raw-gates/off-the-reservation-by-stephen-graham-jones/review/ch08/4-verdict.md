# ch08 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，9 块 9 引语，issues 全空（**注意：机器层对引语头部多余引号不敏感**——见阻断 B）。
R4 人判：9/9 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块4 中文「Mooch Pease」被 T1 误删为「Mooch」 | text/ch08:95「**Mooch Pease, just fifteen**, had fallen in love hard enough」 | T1 取证错误（grep 输出截断致假查无），应恢复 Pease | **阻断**（撤销 T1 误修） |
| 块8 引语头部 `""“` 多一个直引号（同类 11 行：ch08:59、ch09:35/95/101、ch10:29、ch11:23、ch12:29/53、ch13:23/59、ch14:35） | git show 4aec2b2b5^ 对照；text/ch08:212 原文以 `“` 开头、段尾无闭引号 | 统一 `**原句 N:** ""` → `**原句 N:** "` | **阻断**（格式） |
| 块8 读者视角引「keep living, it's what he would want for you」疑似编造 | 首查 `/usr/bin/grep -rn "keep living" text/` → 0 命中（**小写假查无**）；变体 `/usr/bin/grep -rin "…he would want…"` → text/ch08:215「**Keep living. It's what he would want for you.**」 | 有据；首次零命中系大小写词形不一致 | 假红（疑似，实正确） |
| 素读#5 Trace 死状细节未入块 | 素读 anchor 命中 True | 非关键转折 | 提示（不修） |

取证命令记录：
- `/usr/bin/grep -n "Pease" text/*.txt` → text/ch08:95（本次全文长度输出，确认 Pease 在行内偏移 300+ 处，T1 时被 cut -c1-160 截断漏看）；退出码 0
- `/usr/bin/grep -rn "keep living" text/` → 0 命中、退出码 1；`/usr/bin/grep -rin "keep on living\|he would want\|…" text/*.txt` → text/ch08:215、text/ch10:89；退出码 0

## 已核实为正确

- 块8 读者视角「Keep living. It's what he would want for you.」——text/ch08:215 原文逐字（Mooch 对 Leech Lake 男孩的话）。**后续任何人不得以「全书查无 keep living」为由删除**——小写 grep 会假查无。
- 块4 引语「Mooch Pease, just fifteen」逐字保留在引语内（T1 只误改了中文理解层，引语未动）。
- 块2「brainer'd」谐音梗、块9「Con/Conrad 同人」均与素读一致。

**结论：阻断 2（T1 误修恢复 + 11 行引号格式）、假红转正确 1、提示 1（不修）。**
