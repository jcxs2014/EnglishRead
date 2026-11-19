# T1 自检判定 · pumpkin-spice-promises-by-taylor-jade

## 抽样章（31 章 >16 ≤40 → 1/4 = 8 章；首末必含；等距取）

ch01 · ch05 · ch10 · ch14 · ch20 · ch24 · ch28 · ch31（共 8 章）
- 首章 ch01 ✅ / 末章 ch31 ✅
- 中间 6 章按 1/4 间隔取：ch05(送奶路线) · ch10(会议对峙) · ch14(Yes短信) · ch20(Past病房) · ch24(吻后三天) · ch28(二十步)

## 断言扫描（assertion_scan.py）

原始输出 → `t1-candidates.txt`（649 行，六类全覆盖）。
只人读了命中行，重点核 ①相对章号（23 行）、②绝对断言（152 行）、③年龄数字（391 行）、④亲属身份（28 行）。

## 六类逐章核对结果

### 数字 / 计数

- ch01：September 1st 在 text 4 次 / md 2 次（引语 + 分析各 1）✅
- ch05：Rosie text 6 / md 8（分析和引语可重复引用）✅
- ch10：Thirty-six text 2 / md 三十六 4（分析+引语）✅；two hundred text 1 / md 两百箱 4 ✅
- ch14：seven forty-three text 1 / md 七点四十三 1 ✅；twenty minutes text 1 / md 二十分钟 1 ✅；Twenty-three text 1 / md 二十三 9（导航+引语+分析）✅
- ch28：twenty steps text 1 / md 二十步 8（标题+引语+分析）✅
- ch31：November ninth text 1 / md 11月9号 1 ✅；fiancé text 2 / md 未婚夫 1 ✅

### 亲属称谓 / 角色名

- ch10：Meme/Margaret/Evelyn 区分正确——Meme(32 次) 均指 Evelyn Rome；Margaret(9 次) 指 Margaret Jones ✅
- ch26：James/Pops 区分——text 有 James(1 次)+Pops(6 次)，md 中 James 出现在引语内引用、Pops 出现在分析内 ✅
- ch31：Millie text 1 / md 1 ✅（骑术课小女孩）
- ch30：Talbot text 1 / md 2（引语+分析各 1）✅

### 相对章号

23 行命中全部为「读者视角提示」或「为什么这样写」字段内的叙述性指引（如「下一章」「上一章」），
不涉及事实跨章指认。逐条核无一处将 A 章内容归入 B 章引语。

### 施受方向

32 行命中为 ch01-ch04 之间的叙事手法描述，核无反向施受错误。

### 场景方位

9 行命中为全局空间描述（门廊/牧场/谷仓），核无错位。

### 名单顺序

ch10 Rosie→Meme→Margaret→June 出场顺序与 text 一致 ✅

## 缺陷统计

**阻断型 0 条。**

### 提示型（不修，留档）

1. **ch03 读者视角提示「他不知道她的名字」** —— 此句是叙述性指引而非引语内容断言；不修。
2. **ch26 中文理解「本文标题级的和解」** —— 「标题级」为自创描述用语；不判阻断但下次注意措辞。
3. **ch31 词汇表 carton 例句引自 ch26 而非 ch31** —— 已在写作期修正为 ch31 的 temporary；此为写作过程中已自纠的痕迹，留档不修。
4. **ch29 敏感章引语选择** —— 性爱场景已按规程克制选句，仅收前奏与后余韵；属于约定范围而非缺陷。

### 跨章引语污染（全查 0 条）

对 8 个抽样章逐章 grep 了「上一章/下一章」的引语内容是否混入了邻章的 text/——零命中。

### 总览引语

总览三篇 144/144 引语 100% 可核实（verify_overview_quotes 已过）；总览英文段落 0 处（check_chinese_layer 已过）。

## 结论

T1 自检：抽 8/31 章，阻断 0 条，提示 4 条（均不修）。样本密度 25.8%（8/31）。
**T1 为同会话自检。** T3 深审未做（待用户发起）。
