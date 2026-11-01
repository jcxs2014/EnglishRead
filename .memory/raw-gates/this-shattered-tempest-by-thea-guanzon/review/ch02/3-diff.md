# ch02 对账（R2 + R3）

- 精读 md：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch02 the figure behind the glass.md`
- 原文：`text/ch02_chapter_two.txt`（`char_total` = 21090）
- 素读底稿：`review/ch02/1-suread.json`（events 8 / relations 5 / numbers 6，19/19 命中）
- 机器层：`review/ch02/2-machine.json`（verdict ok）

## R2 对账

| 项 | 机器判定 | 人工对账 |
|---|---|---|
| 引语长度/句数 | 原 11 块全部 30–70 词 | 一致 |
| 逐字 | 查无 0 | 一致 |
| 形态 | H1 / 导航 5 项 / 4 子项 / 三档表 / 总结 全绿 | 一致 |
| 块数 | 修前 11（建议 7–11） | 修后 13，见「提示 T1」 |

## R3 三张单子

### 漏（素读有、md 无 → 阻断）

| # | 素读事件 | md 处置 |
|---|---|---|
| L1 | 奥莉尔自认「内纳瓦伦数千年来第一个雷击者」，父母把秘密带进坟墓 | **阻断**：原文 `text/ch02_chapter_two.txt:84`，修前 md 只在「一句话总结」提过一句、无引语块 → 已补**原句 5**（34 词，`“The first Thunderstruck born to the Dominion in thousands of years,”…their graves.`） |
| L2 | 她把整杯茶泼在塔拉辛脸上 | **阻断**：原文 `:108` `Oryal hurled the contents of her teacup at Talasyn.` 修前 md 无 → 已在原句 5 的读者视角提示中显式标注（「同一场景后文，她把整杯茶泼在塔拉辛脸上——那一泼是她第一次用动作代替回答」），标注了位置，不冒充引语 |
| L3 | 塔拉辛猜到计划：杀她 → 无继承人 → 围攻都城、另立女王 | **阻断**：原文 `:207`，修前 md 无 → 已补**原句 11**（51 词，`“Let me guess,”…on the Dragon Throne.”`） |

### 编（md 有、原文无 → 阻断）

无。逐块核对后，中文理解里的人名/动作/关系均可指回本块引语；块 2「一面是藤编屋顶与炉灶、一面挂着鹿头与长矛」已取证：`:39` `the walls plastered with stag heads on plaques and mounted spears`、`:?` `Sunrise sifted through the gaps of the rattan-vine ceiling`。

### 错（两边不一致 → 阻断）

| # | 位置 | 修前 | 判定 | 取证 |
|---|---|---|---|---|
| C1 | 原句 1 中文理解 | 「**以太海**的蔚蓝潮水」 | 阻断（术语漂移） | 术语表 `Eversea → 越海`；已改「越海」 |
| C2 | 原句 10 中文理解 | 「**凯萨瑟**在那里的政治立足点」 | 阻断（术语漂移） | 术语表 `Kesathese → 凯萨斯的`，md 其余 55 章用「凯萨斯」；已改 |
| C3 | 原句 6 读者视角提示 | 「她**后悔**的是父亲的死，不是自己的手」 | 提示（推断写成事实） | 引语只有 `because I was angry and grieving`，未出现 regret；已改为「她哀悼的是父亲的死，而不是自己那双手做过的事」 |

## 提示（不判红）

| # | 问题 | 处置 |
|---|---|---|
| T1 | 补齐两处缺口后块数 13，`chapter.sh` 打 `⚠️ 块数 13 偏离本书常见区间 4–12` | 记一行不改：13 在硬限 2–15 内，且补齐的是素读确认的两处真缺口；本书最高章块数为 13，不构成形态异常 |
| T2 | 关键词行原 4 条 / 整行 ≥7 词（`⚠️ 关键词整句 11 处`） | 已收紧为 3 条两词短语（`26e3efd2b`），复跑 0 ⚠️ |

## 修复后复跑

- `bash scripts/chapter.sh "<ch02 md>"` → `rc=0`，`引语块 13，片段 13，查无 0`，五项人工判据全 0，唯一告警为上述块数提示
- `bash scripts/gate.sh "<书目录>"` → `rc=0`，正门结论 0 条阻断型
