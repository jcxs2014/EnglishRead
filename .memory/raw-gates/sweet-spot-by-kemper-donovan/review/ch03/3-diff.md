# ch03 三单对账（R3）

素读基准：`1-suread.json`（facts 8 / relations 6 / numbers 19）；晶体：`ch03 engaged and hired.md`（15 块，已达本书块数硬顶）。

## 漏
- **F4「Denny 抢白说自己已订婚」未成块**。原句 7 的引语从「This response spilled out of me…」起，`I'm engaged` 这句只在导航与一句话总结里以转述出现。
  - 原文：`text/ch03_chapter_3.txt:70` `“I’m engaged,” he blurted out.`
  - 判定：**漏**（本章关键动作句未成引语），提示型；**且不可补块**——本章已 15 块，插入即触「块数 2–15」硬顶。
- **F8「周五晚在 Sweet Spot 撒骨灰」未成块**：该信息只在导航与总结里转述，未引原句。
  - 原文见 `text/ch03_chapter_3.txt` 关于 Friday night / Sweet Spot 的对话段。
  - 判定：**漏**（同上，块数已满），提示型。

## 编
- 无。`2-machine.json`：15/15 块引语逐字命中（片段全部 ok）。
- 附核：原句 7 中文理解引的「哇，太好了，恭喜」并非编造——原文 `text/ch03_chapter_3.txt` 作 `“Oh wow! That’s amazing, congratulations!”`（小写，首次 grep 大小写敏感故未命中）。

## 错
- **「妹妹」应作「姐姐」**：原句 5 中文理解原写「二十五年前她还在少女时期，妹妹自杀身亡」。
  - md 侧：`ch03 engaged and hired.md:60`
  - 原文侧：`text/ch03_chapter_33.txt:100` `I was two years younger and always in her shadow`（Cassie 比她大两岁）⇒ Cassie 是**姐姐**；本书 ch33 引语亦作 `her big sister`。
  - 判定：**错（亲属关系）**，已改。属 S5 类。

## 数字复核（对 `numbers` 19 条）
- `twenty-five years ago` / `eighteen` / `twenty years ago` / `fourteen years old` / `three months` / `Wednesday` / `Friday night` 均与 md 表述一致。
- 「不到两天」＝周三到周五，算术成立。
