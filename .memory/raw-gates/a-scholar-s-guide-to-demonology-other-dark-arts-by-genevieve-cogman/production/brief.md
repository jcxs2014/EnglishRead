# 派工指令书 · a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman

> 写给子代理的唯一一份给料。派工人＝主会话。子代理**不碰 git**。

## 0. 必读（按顺序，别读别的）

1. `docs/rules/创建卡.md` **全文**（约 8 KB，写作规则与一章骨架）
2. `python3 scripts/bookform.py "notes/books/novels/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman" --contract`（本书契约：判红 8 项 + 骨架 + 导航项名）
3. 你负责的章的 `text/chNN_*.txt` **全文**（不许只读开头）
4. 参照成品形态（第一、二章已定稿）：`notes/books/novels/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman/ch01 prologue.md`

**不给也不要找**：`docs/rules/审查表.md`、`docs/实测档案/`、门禁脚本源码。

## 1. 本书已勘定的形态与事实

- 体裁 `novels`：导航 **5 项**，项名固定为
  `一句话概括` / `情感弧线位置` / `Tropes 兑现/反转` / `人物弧线` / `叙事手法`；
  精读块 **4 子项**：`中文理解` / `关键词` / `为什么这样写` / `读者视角提示`。
- **H1 形态**：`# <两位文件号>. <该章 text 首行抬头的大小写形式>`
  - ch01 `# 01. Prologue`（text 首行是校名，章抬头取书里实际形态，见成品）
  - ch02 `# 02. Chapter One` … ch27 `# 27. Chapter Twenty-Six`
  - ⚠️ **文件号比原文章号大 1**（ch02 文件 = 原书 CHAPTER ONE）。
    **导航与正文里不要用「Chapter N」「第 N 章」指代别章**——必然指错。
    要回溯只能用「此前」这种不带章号的写法，或干脆不写。
- **文件名**：`ch<NN> <keyplot>.md`，**唯一分隔符是单个空格**，去标点，小写（英文词用空格分隔，不加下划线、不加连字符）。
- **frontmatter**：`状态: 未读` + `modified: "2026-10-31"`（逐字照 ch01 抄）。
- **章节顺序固定**：`## 本章导航` → `## 精读` → `## 本章词汇`（三档表）→ `## 一句话总结`。
- 已知人物（写他们时只能复述本章原文的说法，别自己补关系）：Philomela “Phil” Fen（主角，第一人称「I」视角）、
  Harriet Jagerson（校长，全书被学生叫「the Head」）、Margot Hamilton（教师）、Mrs Vaughan（教师）、
  Dr Tregennis、Miss Day、Miss Grending、Anne Bredon（对手）、Hamish Alastor（黑猫，原名 Alastor 是恶魔之名）、Jane、Faith、Melandric 等。
- ⚠️ **注意校长姓名的两种拼法**：书信落款是 `Harriet Jagerson`，但正文中学生把校长叫 `Jaggers`。写校长时按本章原文的拼法复制，不要混用。

## 2. 硬约束（违反即退回）

- **`…` 只能在同一个自然段内跳过内容；跨自然段一律拆成独立引语块。**
  引语是**句级**：每块 **1–3 句、30–70 词**；>100 词会被 `chapter.sh` 打 ⚠️，看到就按原文句界拆。
- **块数**：`chapter.sh` 会打印「本章 N 词，建议 a–b 块」，**以该命令实际打印的区间为准**（硬限 2–15）。
  ⚠️ 注意：区间是按词数算出来的，与本文件里的估算可能差 2 块——**以现场输出为准**，别照抄估算值。
  ⚠️ 写完先跑一次 `chapter.sh` 看实际建议区间，超了就合并块（把相邻两块并成一块），不要硬塞新块。
- **块的 `原句 N` 编号必须连续且不重复**（1,2,3…N），删块后要重排编号。
- **不凭记忆引原文**：每条英文先 `grep -F` 落笔；弯撇号 `’`、破折号 `—`、省略号照原样复制。
  最佳做法：用脚本从 `text/` 里**按字符区间切片**取出引语原文（不要手打）。
- **每章先交素读清单再动笔**（顺序不可反）：
  `python3 scripts/suread.py "notes/books/novels/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman" chNN "<facts.txt>"`
  5–8 条「谁做了什么」，每条挂一段**原文逐字锚点**（格式：`原文片段 || 事实描述`），
  必须全部命中（≥5 条）才继续写。
- **词表用脚本，例句不许手打**：
  `python3 scripts/vocab_candidates.py "notes/books/novels/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman" --ch chNN --tiers`
  从输出里**只做减法**挑词条，例句原样粘贴，只填「释义」一栏；
  **三档是分类不是配额**（某档不足就少放甚至留空，不许为凑满从记忆里补）。
- **不写模板套话**（「本句描写了场景与人物的反应」「把 X 重新定义 as Y」等），
  不写「N 个词／N 次／倒数第二段／独立成段／全章唯一／先于」这类不可核的计数与排版断言。
- **跨章指认禁令**：不写「上一章」「前几章」「第 N 章提到」。确需回溯，只写「此前」并保证不指认具体内容。
  子代理看不到别的章，写了指认就是凭空。
- **分析层里的英文证据**必须整段从本章原文复制，不许改写、不许造词。
- **关键词**只从本块引语里挑（不许写中文理解的中译英），单个关键词不超过 8 个词。
- **「读者视角提示」写读者的实感**（会怎么想、会在哪一刻不安），不许写成作者意图说明。

## 3. 每章交付流程

1. `ls notes/books/novels/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman/text/ | grep chNN` 找到语料文件名；
2. 通读本章 text 全文 → 写 facts.txt（放 `.memory/raw-gates/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman/production/chNN-facts.txt`）→ 跑 `suread.py`，全命中才继续；
3. 落引语（脚本切片）→ 写 4 子项 → 词表（脚本粘贴）→ 导航 + 一句话总结 → frontmatter；
4. `bash scripts/chapter.sh "notes/books/novels/a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman/<章 md 绝对路径>"`，
   把尾部输出与退出码抄进回执；rc≠0 就改到 rc=0；
5. **不要 `git add`／`commit`／`push`**。

## 4. 回执（六项，少一项退回）

1. 文件路径 + 字节数；
2. 每块引语的前 6 个词；
3. 事实清单（谁做了什么 / 数字 / 时间），每条能回到原文；
4. 最没把握的一处，明写「哪句是推断、哪句是原文」；
5. `suread.py` 的「锚点命中 N/N」一行；
6. `chapter.sh` 原始输出尾部 + 退出码。
