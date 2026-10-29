# ch03 判定表（R4 逐块 + R3 三单）

审查：异会话（用户点名 T3）｜素读先于读 md｜`2-machine.json` rc=0

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 块 3「fun 掀了屋顶 / 住进 world 放弃 wonder」 | `text/ch03_collapses.txt:27` `given up on wonder to live in the world` | 语义对，但中文层夹生英文，属措辞缺陷 | 提示（已改） |
| 导航「ch01 那一行的街头毒打」 | `ch01 …nights.md` 全章为同一夜 | 「那一行」无指代，属笔误 | 提示（已改） |
| 漏：Venturi 创办诊所（19 世纪） | `:30` `founded in the 19th century by Girolamo Venturi` | 背景设定，非本章转折 | 提示（不修） |
| 漏：Dal Mare 跛脚十四年 | `:39` `as injury has forced him to do for the last fourteen years` | 人物外观背景 | 提示（不修） |
| 块 1「梦里只有物理量被翻转」 | `:18` `In Dream, Porky is no less fat, but much lighter` | 原文以 no less fat 让步，读法成立 | 假红 |
| 块 2 绕口令里 s 的密度 | `:21` `“Susie’s sewing stockings for soldiers.”` | 引语逐字；s 音密集成立 | 假红 |
| 块 4「国宝」四词是价目表 | `:36` `His common sense, his simple realism, his quiet manner and extreme generosity` | 属叙述者反讽读法，非事实断言 | 假红 |
| 块 5「赤脚踩柏油路」先于本段 | `:150` `“Their feet were bare,” he remembers.`、`:165` `“But this was on asphalt!”` | 位置正确（块 5 引语在 `:183`，赤脚细节在前） | 假红 |
| 块 7「Almost like a hook. 四个词」 | `:201` `Almost like a hook.` | 四词独立成段，成立 | 假红 |

## 已核实为正确

- 块 1 引语为同段连续子串：`text/ch03_collapses.txt:18`，`“Porky” is the name…light enough to fly.` 之间无省略、无空行。
- 块 3 引语同段连续：`:27`，`They hurt each other plenty…live in the world.` 完整。
- 块 7 引语同段连续：`:198`，`It’s their fault…arched, curved, pointed.` 完整（含原文 `when, Dal Mare got angry,` 的逗号错位，逐字保留）。
- 块 8 城市旁白：`:207`，`Rome is a city so loaded with History…the love between them isn’t over yet.` 逐字。
- 块 9「四年前有了经纪人」：`:333` `four years ago having an agent made her believe she was right on the edge of success`——数字与因果正确。
- 章末让步句：`:336` `“Let’s talk about Sunday,” she concedes.`——「塌完仍接活」的读法有原文支撑。
