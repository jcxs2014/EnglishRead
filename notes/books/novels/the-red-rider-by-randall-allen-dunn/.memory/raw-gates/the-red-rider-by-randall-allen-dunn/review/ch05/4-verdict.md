# ch05 4-verdict（T3 深审 · 边审边改）

R1：review/ch05/1-suread.json（8 条，子代理盲读，自检 PASS）。
R2：review/ch05/2-machine.json（chapter.sh --json verdict=ok，rc=0；9 块逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 三条军令 | Step/Keep silent/Shoot 在引语 | 军令无主语争议；"他不会容忍" 分析与 "He would brook no disobedience"（text 同章）一致 | 对应 |
| 2 | 兔子课 | afraid to shoot/shove your fear aside/only a rabbit 在引语 | "Papa 的核心课" —— said 主语 Papa（text 邻域）✓；you=Helena ✓ | 对应 |
| 3 | 撕裙自裹 | eyes bulge/wrapped the cotton strip/hint of Papa's smile 在引语 | I=她 gathered leaves/pressed/wrapped ✓；Papa's eyes bulge 施事 Papa ✓。注：中文理解首句"撕下裙摆"动作在引语前一段（"I tore a strip from its bottom."），分析层全部锚在引语内——S2 边缘，判提示不修 | 对应（附注） |
| 4 | 小鹿怜悯课 | carcass/final breaths/wonder and pity 在引语 | We=父女（两人狩猎）；"They rushed"中文用"他们"指父女二人，语境无歧义 ✓；相邻段 "Then shoved all pity aside." / "It was meat." 以逐字英文入分析 ✓ | 对应 |
| 5 | 扼喉 | iron manacle/one mighty arm/choking 在引语 | fist 主语 Grenault's、受事 my throat ✓；"一只巨臂撑身体、另一只掐喉"= one mighty arm...the other choking ✓ | 对应 |
| 6 | 三连降格 | nothing at all/a frightened little girl/run out of tricks 在引语 | he said=Grenault ✓ | 对应 |
| 7 | 处刑宣判 | suffocate/string you up like a piece of meat/slowly 在引语 | he=施刑者、you=她，方向与原文一致 ✓ | 对应 |
| 8 | 改口放人 | troublesome animal/Nothing to worry about/I'll handle it 在引语 | he said=Grenault ✓；楼下喊话者=镇民（text 邻域）✓ | 对应 |
| 9 | 颤栗收尾 | forced my eyes shut/still trembling/grip 在引语 | I=她 ✓ | 对应 |

跨章引用核章号：
- 原句1 分析无跨章；原句5 提示 "No hesitation."（text/ch05_5.txt 逐字，同章现在线）✓。
- **原句7 分析原写"呼应第 3 章小鹿"——阻断**：取证 `/usr/bin/grep -rn "It was meat" text/` 仅 `text/ch05_5.txt:344` 命中，ch03 计数 0（exit 1）⇒ 改"本章狩猎课闪回"。已修，chapter.sh rc=0。
- 原句3 提示新增 "I stopped the bleeding."——text 中该句跨 PDF 断行（"I stopped"+"the bleeding."分行），拼接形式由门禁空白归一化命中（rc=0）；`/usr/bin/grep -c "I stopped the bleeding" text/ch05_5.txt` 单行口径计 0（exit 1）属断行假查无，取证已留档。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| "It was meat." 章号错指 ch03 | grep 全 text 仅 ch05_5.txt:344 命中 | 改"本章狩猎课闪回" | **阻断→当场修** |
| "I stopped the bleeding" 战争格言未入 md | text/ch05_5.txt（跨行拼接） | 补入原句3 提示 | 提示→当场修 |
| 拖鞋课/扣扳机句/Well done 未入块 | 转折层已由块2/块4 覆盖 | 不修 | 提示（依据：同场景铺垫与手段层，转折与心理层全收） |
| 中文理解首句"撕裙"超出引语半句 | 撕裙在引语前一段（text 逐字） | 不修 | 提示（分析层全部锚在引语内，事实由 R1 取证） |

## 修复动作（边审边改）

1. 原句7 分析章号改"本章狩猎课闪回里那句"；2. 原句3 提示补格言句。修后 chapter.sh rc=0 ×2，pathspec 提交。

## 已核实为正确

- 原句5 提示 "No hesitation."（text/ch05_5.txt："I kept my face hard and pulled back on the lever. No hesitation."）——她在狙击前默念童年口令的写法有原文支撑。
- 原句4 分析引用的 "Then shoved all pity aside." 与 "It was meat." 均为 text/ch05_5.txt 相邻完整段逐字复制（341/344 行邻域），非拼接。
- 原句8 中文"把'她'降格成'动物'"——原文 "Just dealing with a troublesome animal" 中 animal 指她本人（Grenault 对楼下镇民的掩饰），方向无反转。
