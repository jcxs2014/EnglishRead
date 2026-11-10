# ch02 R3 对账（素读 10 事件 × md 11 块）

R1 来源：review/ch02/1-suread.json（子代理盲读 text/ch02_two.txt，10 条，锚点 10/10 独立复验命中）。

## 单子一：漏（素读有、md 无）

| 素读事件 | md 覆盖位置 | 定性 |
|---|---|---|
| [2] 红色铁板如巨鲸、吊车超百米、希腊船主矿石船 | 词汇表 ore carrier 例句 + 块 3 中文「三百米长的巨船」（触发物） | 覆盖，非漏 |
| [3] 八分钟骑行、二十层楼高断面 | 块 3 上下文（触发物）+ 词汇例句 | 词汇层覆盖，非漏 |
| [4] 棕发男工骚扰戏（Maybe I'll take Miu） | 词汇表 husky/swarming 例句 + 块 5 中文「上一段棕发男人问她」 | 覆盖，非漏 |
| [7] 下班、道歉邮件、吸烟亭、马形剪影 | 块 9（剪影）+ 词汇表 meticulously 例句（道歉邮件） | 覆盖，非漏 |
| [9] 工会办公室 12 叠、红旗、周三五 17:00–18:30 | 块 11 上下文「工会办公室的这个位置」 | 覆盖，非漏 |

结论：**漏 = 0**。

## 单子二：编（md 有、原文无）

- 块 2 中文「一年到头晒不黑」：由 every day + unusually pale 推理的评析，非事实断言——提示级以下，不判。
- 导航「Ushio……记不住账目细节」：原文为 "completely dependent on you when it comes to all things money-related" + 连收据都要她处理——「记不住」是「依赖」的引申转述，方向正确，评析从宽记提示。**编 = 0**（无凭空情节/关系/数字）。

## 单子三：错（两边都有但不一致）

- **阻断 1（S2 引语选短）**：块 4 中文「于是松了口气，认定不会触怒上帝」——两个动作（concluded with relief / invoke the wrath of God）在段 33 后半句，原引语止于 plastic models，中文覆盖了引语之外的原文。取证：/usr/bin/grep -c "concluded with relief" text/ch02_two.txt → 命中 1；退出码 0。
- 数字核对：二十五年入社 ✓（素读[10] 同源段）、约 800 名会员 × 2,000 日元 ✓、54,220 收据 ✓、0-9-2-3 密码 ✓、约 20 沃 × 100 万日元 ✓——全部在引语或词汇例句内逐字。
- **错（施事/因果/数字/时序）= 0**（阻断 1 属 S2 选短，已在单子二外单列）。

## 处置

- 块 4 扩引语至段 33 全两句（+concluded with relief, it was un-likely that we would invoke the wrath of God.），关键词同步补 2 个；chapter.sh 复验 rc=0、查无 0；commit 9ba437e69。
