# Bird of a Thousand Stories（Kiyash Monsef）精读规格

> 本文件是**本批次写作的唯一事实源**。子代理写任何一章前必须读它。
> 事实全部来自 epub 实测（spine 逐件 + NCX 46 条 + LoC 版权页），**不是书名/作者印象**。

## 书与体裁

- 书名：Bird of a Thousand Stories ／ Kiyash Monsef ／ 2025 ／ Simon & Schuster **Books for Young Readers**
- LoC 版权页权威信号：`LCGFT: Fantasy fiction. **Novels**.`；`Audience: Preteens | Ages 10 and up | Grades 4–6`
- 体裁：**长篇奇幻／魔幻现实主义（YA）** ⇒ 逐章精读**精简格式** + **总览三篇**（非短篇合集，总览强制）

## 决定精读格式的三条依据

1. LoC 版权页写 **Novels**（不是 short stories collection）⇒ 不走短篇合集格式，但**要总览三篇**
2. 全书 40 件 = 26 编号章 + 14 插叙，**两条叙事线** ⇒ 导航必须写「本件属哪条线」
3. 同代作品 `astarion-by-t-kingfisher`（同为 fantasy 长篇、同为精简格式）ch01 已入库 ⇒ **格式照它写**

## 双线结构（**最易写错的结构性事实**）

- **A 线＝书内编号章**：标题形如 `Chapter One:` … `Chapter Twenty-Six:`，共 **26** 章，第一人称（Marjan 当下线）
- **B 线＝民间故事插叙**：标题**不**以 `Chapter` 开头，共 **14** 篇

⚠️ **B 线的 14 篇里只有 6 篇标题是 `THE BIRD OF A THOUSAND STORIES`**，另外 8 篇各有自己的民间故事题名
（`The Great Family and the Tiny Dragon` / `The Lamb in the Garden` / `The Turtledove and the Wind` /
`The Winged Horse of Kashan` / `A Fire in the Desert` / `The Old Name of the Bear` /
`The Forest That Returned` / `Boitatá`）。
⇒ **判定归属看标题是否以 `Chapter` 开头，不看它是不是「千鸟」**。这是本批次最容易搞错的结构性事实。

### ⚠️ B 线内部人称不统一（2026-10-02 实测，本文件此前写错）

我最初把 B 线整体写成「第三人称全知/说书人」——**这是错的**，已按 `text/` 逐篇实测修正。
写「视角」栏前必须按下表，**不要套用统一口径**：

| 人称 | 篇目 |
|---|---|
| **第一人称亲历**（`I` 明显多于三人称） | ch09（I=42）· ch16（22）· ch18（28）· ch27（18）· **ch40（109，全书收束）** |
| 第三人称全知/说书人 | ch01 · ch03 · ch05 · ch08 · ch22 · ch24 · ch28 · ch34 · ch38 |

⚠️ **ch40 是全书收束却是第一人称**（`I` 出现 109 次）——按第三人称写必错。
⚠️ **ch27 开头仍有说书人报幕**（`THERE IS A TERRIBLE PART TO THIS STORY.`），但正文是亲历者自述。
**判据：先 `grep -c '\bI\b'` 与 `head -6` 读本章实况，再写视角栏。**

⚠️ 同理，**A 线各章出现的人名也不一致**：ch25 的 `Marjan` 实测为 **0**（只有 `Mar`），
`Zorro` 在 ch25/ch26 为 0。⇒ **导航与分析层里出现具体人名前，先 `grep` 本章确认**。

## 章号映射表（`text/` 件号 → 书内章号/线别/标题）

| 件号 | 线别 | 书内章号 | 英文标题 | text/ 文件 |
|---|---|---|---|---|
| ch01 | B 插叙 | 无（卷首） | THE BIRD OF A THOUSAND STORIES | ch01_the_bird_of_a_thousand_stories.txt |
| ch02 | A 编号 | Chapter One | The Other Thing My Dad Left Me | ch02_chapter_one_the_other_thing_my_dad_left_.txt |
| ch03 | B 插叙 | 无 | The Great Family and the Tiny Dragon | ch03_the_great_family_and_the_tiny_dragon.txt |
| ch04 | A 编号 | Chapter Two | Is. Tan. Bul. | ch04_chapter_two_is_tan_bul.txt |
| ch05 | B 插叙 | 无 | The Lamb in the Garden | ch05_the_lamb_in_the_garden.txt |
| ch06 | A 编号 | Chapter Three | Foreign Objects | ch06_chapter_three_foreign_objects.txt |
| ch07 | A 编号 | Chapter Four | The Man Who Sold Rugs | ch07_chapter_four_the_man_who_sold_rugs.txt |
| ch08 | B 插叙 | 无 | The Bird of a Thousand Stories | ch08_the_bird_of_a_thousand_stories.txt |
| ch09 | B 插叙 | 无 | The Turtledove and the Wind | ch09_the_turtledove_and_the_wind.txt |
| ch10 | A 编号 | Chapter Five | Nothing Is Simple | ch10_chapter_five_nothing_is_simple.txt |
| ch11 | A 编号 | Chapter Six | The Phalarope | ch11_chapter_six_the_phalarope.txt |
| ch12 | A 编号 | Chapter Seven | Shuck | ch12_chapter_seven_shuck.txt |
| ch13 | A 编号 | Chapter Eight | Home Sooner | ch13_chapter_eight_home_sooner.txt |
| ch14 | A 编号 | Chapter Nine | My Orphans | ch14_chapter_nine_my_orphans.txt |
| ch15 | A 编号 | Chapter Ten | Other Factors | ch15_chapter_ten_other_factors.txt |
| ch16 | B 插叙 | 无 | The Winged Horse of Kashan | ch16_the_winged_horse_of_kashan.txt |
| ch17 | A 编号 | Chapter Eleven | Out of Wishes | ch17_chapter_eleven_out_of_wishes.txt |
| ch18 | B 插叙 | 无 | A Fire in the Desert | ch18_a_fire_in_the_desert.txt |
| ch19 | A 编号 | Chapter Twelve | A Posy of Alkaloids | ch19_chapter_twelve_a_posy_of_alkaloids.txt |
| ch20 | A 编号 | Chapter Thirteen | All the Water in the World | ch20_chapter_thirteen_all_the_water_in_the_wo.txt |
| ch21 | A 编号 | Chapter Fourteen | Hello, and Also Goodbye | ch21_chapter_fourteen_hello_and_also_goodbye.txt |
| ch22 | B 插叙 | 无 | The Old Name of the Bear | ch22_the_old_name_of_the_bear.txt |
| ch23 | A 编号 | Chapter Fifteen | Things That Need Repair | ch23_chapter_fifteen_things_that_need_repair.txt |
| ch24 | B 插叙 | 无 | The Bird of a Thousand Stories | ch24_the_bird_of_a_thousand_stories.txt |
| ch25 | A 编号 | Chapter Sixteen | Centro | ch25_chapter_sixteen_centro.txt |
| ch26 | A 编号 | Chapter Seventeen | We’re Here About the Bird | ch26_chapter_seventeen_we_re_here_about_the_b.txt |
| ch27 | B 插叙 | 无 | The Forest That Returned | ch27_the_forest_that_returned.txt |
| ch28 | B 插叙 | 无 | Boitatá | ch28_boitat.txt |
| ch29 | A 编号 | Chapter Eighteen | Am I Safe | ch29_chapter_eighteen_am_i_safe.txt |
| ch30 | A 编号 | Chapter Nineteen | Everything’s a Mess | ch30_chapter_nineteen_everything_s_a_mess.txt |
| ch31 | A 编号 | Chapter Twenty | A Never-Ending Ellipsis | ch31_chapter_twenty_a_never_ending_ellipsis.txt |
| ch32 | A 编号 | Chapter Twenty-One | A Princess Trapped in a Castle | ch32_chapter_twenty_one_a_princess_trapped_in.txt |
| ch33 | A 编号 | Chapter Twenty-Two | Sacred Treasures | ch33_chapter_twenty_two_sacred_treasures.txt |
| ch34 | B 插叙 | 无 | The Bird of a Thousand Stories | ch34_the_bird_of_a_thousand_stories.txt |
| ch35 | A 编号 | Chapter Twenty-Three | Behind and Between | ch35_chapter_twenty_three_behind_and_between.txt |
| ch36 | A 编号 | Chapter Twenty-Four | The Castle of Come-and-Never-Go | ch36_chapter_twenty_four_the_castle_of_come_a.txt |
| ch37 | A 编号 | Chapter Twenty-Five | The Thing with Feathers | ch37_chapter_twenty_five_the_thing_with_feath.txt |
| ch38 | B 插叙 | 无 | The Bird of a Thousand Stories | ch38_the_bird_of_a_thousand_stories.txt |
| ch39 | A 编号 | Chapter Twenty-Six | Horaltic | ch39_chapter_twenty_six_horaltic.txt |
| ch40 | B 插叙 | 无（全书收束） | The Bird of a Thousand Stories | ch40_the_bird_of_a_thousand_stories.txt |

## 逐章格式（照 `ch01 the bird of a thousand stories.md` 写，一处不差）

```
---
状态: 未读
modified: "2026-10-02"
---

# NN. <中文标题>（书内 <Chapter X | 无·插叙>）

## 本章导航        ← 6 项粗体，每项必须有正文
  **一句话概括** / **书内章号** / **视角** / **情感弧线位置** / **人物弧线** / **叙事手法**

## 精读            ← 3–8 块（配额），每块四子项，顺序固定
> **原句 1:** "<从 text/ 逐字复制>"
- **中文理解**：
- **关键词**：    ← 2–3 组，只能用本块引语里出现的词
- **为什么这样写**：
- **读者视角提示**：

## 本章词汇        ← 三档 `### ⭐⭐⭐ 高级` / `### ⭐⭐ 进阶` / `### ⭐ 基础`
| 词/短语 | 释义 | 例句 |     ← 例句逐字来自本章 text/

## 一句话总结      ← 必须有正文
```

## 写「视角」栏之前（**这一步最容易写错**）

- **B 线（插叙）人称不统一**：见上方「B 线内部人称不统一」表——
  ch09 / ch16 / ch18 / ch27 / **ch40** 是**第一人称亲历**，其余才是第三人称全知/说书人。
  ⚠️ **ch40 是全书收束却是第一人称**（`I` 出现 109 次），按第三人称写必错。
  **别套统一口径**（本文件此前就写错过一次，由 ch27 worker 报告纠正）。
- **A 线人名逐章不同**：出现 `Marjan`/`Mar`/`Malloryn`/`Zorro` 前先 `grep` 本章确认
  （实测 ch25 的 `Marjan` 为 **0**，只有 `Mar`；`Zorro` 在 ch25/ch26 为 0）。
- 判据动作：`grep -c '\bI\b' text/chNN_*.txt` ＋ `head -6 text/chNN_*.txt` ＋ `grep -c 'Marjan' text/chNN_*.txt`。

## 硬规则（违反即 precheck 报 ❌，禁止 commit）

1. **引语逐字**：`> **原句 N:**` 的内容必须是 `text/chNN_*.txt` 的**逐字连续片段**；
   省略号 `…` 每段都要各自连续（禁令 5）
   ⚠️ **一条引语只能取自一个自然段**——`…` 不能用来把**两段**的话连成一条
   （The Paris Deception 已记录：省略号两侧都合法，段落边界 flat 比对却看不见）。
   本批 ch06/ch07/ch08 各因此被抓 1–2 处。要引下一段的内容，**另起一块**。
2. **关键词只从本块引语里挑**（禁令 4）；分析层英文只能用本块引语或本章 text/ 里的词
3. **词表**：词头须是**本章原词形**（`captive` 不是 `captivity`、`grateful` 不是 `gratitude`）；
   例句逐字来自本章；**三档是分类不是配额**，某档不足就少写，不许从记忆里补（禁令 1a）
4. **导航/总结层/分析层的英文也必须能在本章 `text/` 找到**——这三层六道门禁全都不解析（AGENTS 8.1 第 4 步）
5. **禁写标注**：（未出现／未见于原文／本章未／（释义待填）／中文理解补充）一律不许出现（禁令 1a）
6. **禁不可核计数**：不写「N 个词／N 个分句／N 次」；要展示递减就写递减本身（禁令 2）
7. **禁最高级**：「唯一／全书唯一／第一次／最高级」——改成可证写法（禁令 2 第三类）
8. **禁跨章断言**：不写「前一章说…」「第 N 章里…」——本批不核对跨章，写了必错；
   只写本章内部能证的事
9. **禁造词**：任何英文词都必须在本章 `text/` 逐字存在（禁令 1）

## 提交前必跑（两条都过才可 commit）

```bash
python3 scripts/bird/precheck_bird.py "<md 路径>"     # 写作期 10 项判据，退出码 0 才可提交
python3 scripts/verify_quotes.py "<书目录>" "<epub>"  # 引语逐字（对 epub 全文）
```

**precheck 报 ❌ ⇒ 不许提交**，回原文改。⚠️ precheck 的 ⚠️（最高级断言）是提示型，逐条看过即可。
