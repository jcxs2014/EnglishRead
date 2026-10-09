# mp-L 交付报告（The Moon Papers · 组 L · ch36）

## 完工条目（数字均来自命令输出）

- 文件：`notes/books/novels/the-moon-papers-by-emmalea-russo/ch36 lars extraordinary departures.md`
- 引语块数：8（`grep -c '^> \*\*原句'` = 8；全部由 `inject_by_para.py` 带 `*` 整段注入，零手打）
- `check_chapter_quotes.py 36 "<md>"` 原始最后一行：`ch36 lars extraordinary departures.md: 8/8 in ch36 text`
- 词表：21 条 = 高级 9 / 进阶 8 / 基础 4（`build_vocab_section.py --glosses` 输出：`已写入 …: 高级 9 / 进阶 8 / 基础 4（共 21 条，3 项硬断言全过）`，词头全部取自 `vocab_candidates.py --ch 36` 候选集）
- 损坏自查：`grep -n $'\uFFFD'` 无输出；`check_quote_blocks.py` 对全书报 `✅ 前缀完整 · 编号连续无撞车 · 无孤儿分析 · 无自查泄漏`
- `sweep_analysis_inline.py` 对 ch36：2 条 ⚠️（导航「上章回顾」引 ch35 原句，跨章属有意为之）＋2 条 🟠 提示型（同一行内两个各自逐字的行内片段被扫描器拼成一条，如 `a spy balloon forever in the sky`＋`everything would add up`；均为假红，未改）

## 已实际读取的行区间

- `text/ch36_lars.txt`（wc -l = 975）：1–250、251–500、501–750、751–975，读到文件真实末尾（末段＝讣告段 L975）
- `text/ch35_chloe.txt`（56 行）：全文读完（上章回顾的依据）
- `.memory/progress/mp-writer-brief.md`、`ch01 west the secret phone.md`：两份均完整读到文件末尾

## 已 grep 取证的断言

1. 「下一段唯一一次自疑（"What if he was wrong?"）」——`grep -c` 本章命中 **1** 次。
2. 「同车乘客共七人」——L93 `who totaled seven`；L969 另有一处 `totaled`（指 CCC 网图两张），故 Q3 措辞已把「全章唯一一次点数」降为「一段罕见的冷静点数」，避免跨段最高级。
3. 「十年前到访 CCC」——L972 `arrived at the CCC ten years prior`；导航「end of summer 发射倒计时」——L433 `Moon2 will launch at the end of summer`；「Danish Morton 取消 RSVP」——L779-782。
4. 上章回顾两句引语逐字取自 ch35 L24 / L40。

## 因查不到/有歧义而删掉的断言

1. 「也是下一章的发动机」——ch37 未读，删（章末提示只留「全章最大空档」）。
2. Q7 中文理解里的「**昨夜**临睡前」——`the night prior`（L972）指哪一夜有歧义（可指昨夜，亦可指十年前到访前夜），改为不锚定具体日期的「临睡前那种昏沉而澄明的当口」。
3. Q4 读者提示原拟引用 ch01「还没充气的月亮」做跨章互文——跨章推断不写（§4.2/§4.8），改为只在本章内取证的光线句 `until the sun began to set`。

## 可疑但无法判定点（留主会话）

1. **说话人边界**：访谈体（L330-451）里 Lars 的回答以 `La:` 起行，我在 Q5 分析中把它当「Lars 自己的话」——按发言人行成立，但整段访谈是否被叙述层反讽（记者按语已判 `fringe beliefs misguided and conspiratorial`）留待总览层裁决。
2. **Dean Konig 讣告与 ch01 的 Dean** 是否同一人，全书视角下可能是核心悬念；本章 text 只给一份讣告，md 未作同一性断言。
3. Q3 引语段末尾 `mors immatura`（L93）为拉丁短语，`check_chapter_quotes` 扁平化口径下无碍，但词表未收（候选集无此词头），如总览要用需另行取证。

## git

未执行任何 git 命令（按指令书 §0）。
