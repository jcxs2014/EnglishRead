# The Moon Papers · 组 H 完工报告（ch20 / ch21，Part Two 开局的两个 Voice 节）

## 每章交付

| 章 | 文件 | 引语块数 | check_chapter_quotes 原始末行 | 词表条数（高/进/基） |
|---|---|---|---|---|
| ch20 | `notes/books/novels/the-moon-papers-by-emmalea-russo/ch20 voice the guy who wanted my life.md` | 3 | `ch20 voice the guy who wanted my life.md: 3/3 in ch20 text` | 0 / 4 / 5（高级档候选集为 0，按"某档不足留空"未补） |
| ch21 | `notes/books/novels/the-moon-papers-by-emmalea-russo/ch21 voice thick as thieves.md` | 4 | `ch21 voice thick as thieves.md: 4/4 in ch21 text` | 7 / 7 / 5 |

- 注入：两章均 `inject_by_para.py` 按句首前缀 + `+N` 连取（两章 text 各只有一个正文段，无法按自然段分块，故每块为段内连续整句，零手打、零省略号拼接）。
- 词表：`build_vocab_section.py --glosses <json>` 产出（ch20 高级 0/进阶 4/基础 5；ch21 高级 7/进阶 7/基础 5，均"3 项硬断言全过"）。
- 结构自检：`corruption_scan` 风格自查 U+FFFD 两文件均 0；`check_quote_blocks.py` 全目录 ✅（前缀完整·编号连续·无孤儿·无泄漏）；`sweep_analysis_inline.py` 全目录跑完，**ch20/ch21 零报警**（报警均落其他组文件）。

## 已 grep 取证的断言

1. **ch20"本章唯一姓名 = Vesta"**：`grep -oE '\b[A-Z][a-z]{2,}\b' ch20_voice.txt | sort -u` 人名类只有 Vesta（其余为句首大写词与节题 Voice）→ 关键人物行按"全章无名字"写 this guy 与妻子。
2. **ch20 上章回顾**：hiss / rabbit / Dean / Vesta / hung up 五要素在 `ch19_east.txt` 尾部 grep 全命中（计数 5 行）。
3. **ch21 实习生身份与老板性别**：`come back to intern in this space`、`a few nights ago` 逐字命中；老板用 `he`（`he and Vesta are thick as thieves`）⇒ 中文理解里老板译"他"，说话者本人性别不明 ⇒ 全文改用"说话者"避免她/他。

## 因查不到/不敢跨章而删改的断言

1. **"说话者是一个男人"（ch20）**：text 只有 "My wife"，未给说话者性别 → 导航与分析全部改"未具名说话者"。
2. **"本章 Vesta = ch19/ch01 的 Vesta"、"My boss = Lars Arden"（ch21）**：本章未用一句挑明 → 只写"名字相同/两处指称并置，本章未挑明"，由读者自行判断；"老板与 Vesta 是终身夫妻"明确标注为说话者的传闻口径（Husband and wife for life.）。
3. **"唯一一条亲属锚点 / 全章唯一的世界观发言 / 最恨这家人"（草稿措辞）**：属最高级断言且不严格成立（"And I had a father" 也提及父亲）→ 已全部软化为可证表述。

## 可疑但无法判定（留给主会话）

- ch20 "It seems to get everyone." 的 "get" 指什么（死？某种波及？）本章完全不交代——我按"普遍疫病"意象译成"好像落到每个人头上"，若后文（ch22 Vesta 节等）有指涉，总览层可能要回填。
- ch20 末句 "My mother should be here any minute. Her name is Vesta."——若 Vesta 即 ch01/ch19 的 Vesta Furio，则本说话者是 Vesta 的孩子（且已婚、丧妻）；本章无法确认，未写。
- ch21 理论段提到 Binky Stratford 与"绑架"话题，本章只出现在那一句长句里；总览引用时注意别把该句当事件陈述（它是说话者的反讽论证）。
- 两章 text 均含两次节题行 "Voice"（行 1 与行 10），非正文，未引作原句——与提取规范一致，仅备忘。
