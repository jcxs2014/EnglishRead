# ch02 判定（R4 逐块）

块数 13（修前 11，补两块见 `3-diff.md` 的 L1/L3）。

| 块 | 引语起头 | 中文理解 ↔ 引语 | 关键词 | 为什么这样写 | 判定 |
|---|---|---|---|---|---|
| 1 | `Talasyn faded in and out` | 一致（「拍岸—退去」对应 `lapping … before receding`） | 3/3 | 「涨落」读解成立 | ❌→已修：`以太海`→**越海**（术语表口径） |
| 2 | `Then she was in a cavernous longhouse` | 一致 | 3/3 | 两个「家」对照成立 | ✅（`stag heads on plaques and mounted spears`、`rattan-vine ceiling` 均已取证） |
| 3 | `The glass seemed to thin` | 一致 | 3/3 | 「此后不再描写」可核：`grep -c -i chestnut` = 1 | ✅ |
| 4 | `Talasyn’s arms ached` | 一致 | 3/3 | 「同一个洞两次疼法」与块 10 呼应，成立 | ✅ |
| 5（新增） | `“The first Thunderstruck born…` | 一致 | 3/3 | 身份/尺度/代价三合一，成立 | ✅（补漏 L1；顺带在提示里标注 L2 泼茶） |
| 6 | `“The Zahiya-lachis doesn’t need to like you”` | 一致 | 3/3 | 「信息悬在茶盘上方」与原文动作（倒茶、喝茶）相符 | ✅ |
| 7 | `Those two men outside the antechamber` | 一致 | 3/3 | 「她不留余地给悔意」读解成立 | ❌→已修：把「她后悔的是父亲的死」软化为「她哀悼的是父亲的死」（**谁说的**：原文只有 `angry and grieving`） |
| 8 | `“My dear Lady Oryal, this is most irregular”` | 一致 | 3/3 | 「lying low / confirmation of her death」两词组确在引语内 | ✅ |
| 9 | `The heels of Ralya’s walking boots` | 一致 | 3/3 | 「bony cheek」细节成立 | ✅ |
| 10 | `She was careful to school her features` | 一致 | 3/3 | 「shard = 遗物残片」成立 | ✅ |
| 11（新增） | `“Let me guess,” she said as loftily` | 一致 | 2/2 | 「用猜来夺回话语权」成立 | ✅（补漏 L3） |
| 12 | `She would rise from what was certain` | 一致 | 3/3 | 「foothold 把婚姻说成一块地」成立 | ❌→已修：`凯萨瑟`→**凯萨斯** |
| 13 | `The gaze that she fixed on Talasyn` | 一致 | 3/3 | 「with relish」读解成立 | ✅ |

## 施事三问小结

- **谁做的 / 谁说的**：块 7 把「哀悼」写成「后悔」，属替人物加内心判断，已软化。
- **谁的**：无问题（奥莉尔、拉莉亚、吉塔布、哈南、乌尔杜佳的亲属与主从关系与原文一致）。
- 块 1 与块 12 的两处术语漂移属「译名」问题，非事实问题。

## 判定表

- 阻断 **5** 条（漏 L1/L2/L3，错 C1/C2），全部已修；C3 计提示。
- 提示 **2** 条（块数 13 偏离区间、关键词行长度），前者记一行不改，后者已改。
- 假红 **0**；跳过 **0**。

## 已核实为正确

- 13 条引语全部逐字命中（`chapter.sh` 查无 0；新增两条另用 `str.find` 复核）。
- 块 3「不再第二次描写」、块 7「只说自己愤怒与哀悼」、块 8 两个英文词组、块 10「shard」四处可指认断言已回原文取证。
- 修复后 `bash scripts/chapter.sh` rc=0；`bash scripts/gate.sh` rc=0、正门结论 0 条阻断型。
