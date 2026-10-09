# ne-g8 交付报告（Null Entity ch19 + ch20）

生成时间：2026-10-09 · 组前缀 ne-g8 · 完整 lane（epub 在 library/，本章口径按 text/ 逐字断言）

## 交付文件
- `$BOOK/ch19 the parliamentary coup.md` —— 8 块（ch19 原文 10,804 字符，>10K 长章配额 8 ✓）
- `$BOOK/ch20 the world went white.md` —— 5 块（ch20 原文 3,537 字符，短章 3–5 配额 ✓）

## 自检结果（ne_strict.py --book，交付时点原样输出）
```
=== ne_strict: ch19 the parliamentary coup.md | 块 8 | FAIL 0 | WARN 0 ===
=== ne_strict: ch20 the world went white.md | 块 5 | FAIL 0 | WARN 0 ===
```
另跑写前断言脚本 `/tmp/ne_g8_precheck.py`（27+18 条引语、212+88 条分析层英文片段逐一 `frag in src`）：**ALL PASS**。
断言过程中抓出并删除了 5 条我自己拼出来的假片段（如 `Systems, functions, and organs`、`Prime's voice was in the commlink`——均不在两章 text/ 里，未落入 md）。

## 「全书最短章」断言的可复现取证（任务要求）
`wc -c notes/books/novels/null-entity-by-seth-haddon/text/ch*.txt | sort -n`：
- ch20=3607（字符数 3537）为 **编号章 ch01–ch22 中最小**，次小 ch13=5146、再次 ch21=5204。
- ch23_epilogue=2899 更小，但按事实底座它是 Epilogue、不是章。
- md 中的措辞已限定为「正文各章（第一章至第二十二章）最短的一章」，导航与总结各一处。

## 跨章指涉（当场 grep，text/ 行号）
ch19 md 内：
- 「That Syndicate squad...we overheard」指涉的旁听 → ch17_chapter_17.txt:123（`A Syndicate squad of ten soldiers...`）、:135（`...join the arena demonstration`）。md 只写「we overheard it」不补叙，未引用他章英文。
- 首块「cut off from its location」的场景承接 → ch18_chapter_18.txt:126（`I had been partitioned off...no longer tell Prime's location`）。md 正文用中文表述，未贴 ch18 原句。
- 「We'd seen the announcement on GTM-11 / you'd stalled RABBIT's update」（ch19:243 原文自带）→ 强制更新公告 ch02:45；推掉 RABBIT 更新 ch04:155。md 未展开此指涉，仅备查。
- 「Vick's ousting on GTM-11」（ch19:219）→ ch03:180–195（Four 驱逐 Vick 现场）、ch09:213（`Governor Vick, ousted`）。md 未展开。
- 孢子分辨句（ch19:33）→ 与 ch18:144（Prime 检出 `Biological spores have been detected...`）同链；md 未展开。
ch20 md 内：
- 视窗二次接管指涉 → ch19:114（`your face blooming across the glass`）、ch19:120（Wood 收编）。
- 「Do it now」的两个候选所指 → ch19:36（Aliers 毁灭令）、ch19:72（引爆方案）。
- LION 是 Wood 脸上面具的出处 → ch18:75（`his LION mask`）；ch20 md 分析层只用中文写「面具」，未用他章英文片段（「LION mask」不在 ch20 text/，已按规则回避）。

## 短引语备案（<20 字符裸短句，均已逐字回源）
- ch19:15 `“Wylla?”`（作为 3 段块的首段，块内其余为长段）
- ch19:258 `It was Prime.`（3 词收章句，块内其余为长段）
- ch20:15 `Prime closed the distance.`；ch20:93 `The world went white.`（同为多段块组成部分）

## 不敢下判断的清单（总览层需用）
1. ch19 首句「Wylla?」的唤者未标——ch18:132 末章有「我」同款喊话，但本章不承接，md 明确写「别替文本补这个空」。
2. 「build you into a daemon / dragged your wiped ID from the void」的技术原理文本未解释（本章只对 RABBIT 的感知原理明写 `I never found out`），md 只写机制不写原理。
3. ch20 「Mrs. Alzian」与「LYREBIRD PRIME PROTOTYPE is in your body」的所指（这是谁的称呼、Four 躯壳与该名的关系）文本零注释——md 明写「本章不下判」，总览**不要**替它定身份。
4. ch20 「Do it now」的宾语未明写（毁灭 Directory 或引爆方案，两个候选都留了行号），md 拒绝裁决。
5. Fyster 与「我」的关系（亡夫）**只存在于 ch01**，ch19 内 Fyster 仅 1 次（:99）且无关系交代——ch19 md 未写「亡夫」，总览引用时须标 ch01 出处。
6. 「Thorned Root」在两章里均无定义（队伍名？编号？），md 按原文角色使用，未加注释。
7. ch20 结尾「The world went white.」的成因（爆炸/枪/被擒）文本未写，md 保持留白。
8. ch19:114 视窗为何播出你未戴面具的脸（Aliers 的故意还是意外）文本未说明；md 只写「计划撞上目标、结果失控」。
9. 「I＝LYREBIRD、you＝Wylla」全局推断：ch19 有 Wylla/Sotain/LYREBIRD 字样（各 6/2/7 次），ch20 **无 Wylla/Sotain**（名字出现次数 0）——ch20 md 全程只用「你」，未落名。

## git 与边界
未做任何 git 写操作；只写了上述两个 md、本报告与 /tmp/ne_g8_* 临时件。ch18/ch21 他组在制品未读未改。
