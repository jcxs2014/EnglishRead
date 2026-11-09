# FoolSilver (Blood and Bond) — Meg Xuemei X 任务表

- 书目录：`notes/books/novels/foolsilver-by-meg-xuemei-x/`
- 体裁：novels（paranormal romance / 反后宫 why-choose），Zodiac Covenant 系列第 2 本
- 语料：38 章零偏移（ch01–ch38 = Chapter 1–38），verify_corpus PASS（FAIL 0 / WARN 0）
- POV 分布（TOC）：ch01=Drakken，ch02–07=Max，ch08=Caspian，ch09–13=Max，ch14=Nikolai，
  ch15–24=Max，ch25=Drakken，ch26–29=Max，ch30=Nikolai，ch31=Max，ch32=Aelindor，
  ch33=Max，ch34=Drakken，ch35–38=Max（章标题块第二行即 POV 名，H1 取 `# NN. Chapter N`，POV 写进导航）
- 装置件：text/xx_copyright / xx_blurb / xx_authors_note / xx_excerpt / xx_about_author（不写）
- ch38 末尾 2 行 = 下一本预告（Blood and Bond 3: Witchkeel / Releases in Oct, 2026），不算章内正文，禁引用
- U+2060 WORD JOINER 分布（重排后新编号；引语跨 ⁠— 时先查再避，或在 md 引语内补插同字符）：
  ch01,03,05,06,08,11,17,19,21,25,26,27,28,32,35 ×1；ch09,18,24,34 ×2；ch20,33 ×3
- Lokepub 广告 14 行 / 7 章已从 text/ 移除（ch01,10,14,22,25,30,35；epub HTML 内 <p style="margin:0"> div 对，ch20:456 "Read more…" 与 ch25:422 为真对话保留）
- 每章流程：素读清单(suread) → 全文精读 → 引语先行 grep -F → 四子项 → vocab_candidates 挑词 →
  导航+总结 → chapter.sh rc=0 → structure.py order → corruption_scan → commit(pathspec)
- 批次：生成批 ≈1 章/次；每批 commit 前 gate.sh；漏提交对账（书目录 + raw-gates 零输出）

| 章 | 词数 | 建议块数 | 内容概记 | commit | 完成 |
|---|---|---|---|---|---|
| ch01 | 3143 | 6–12 | 试产：Drakken POV，四继承人军营夜议+隔帐听 Max 哭 | 待验收 | |
| ch02 | 2005 | 4–8 | | | |
| ch03 | 3199 | 6–12 | | | |
| ch04 | 967 | 2–4 | | | |
| ch05 | 2954 | 6–12 | | | |
| ch06 | 1913 | 4–8 | | | |
| ch07 | 1092 | 2–4 | | | |
| ch08 | 2054 | 4–8 | Caspian POV | | |
| ch09 | 1914 | 4–8 | | | |
| ch10 | 2707 | 5–10 | | | |
| ch11 | 1049 | 2–4 | | | |
| ch12 | 1964 | 4–8 | | | |
| ch13 | 1432 | 3–6 | | | |
| ch14 | 2604 | 5–10 | Nikolai POV | | |
| ch15 | 1268 | 3–5 | | | |
| ch16 | 1611 | 3–6 | | | |
| ch17 | 1652 | 3–6 | | | |
| ch18 | 1849 | 4–7 | | | |
| ch19 | 1567 | 3–6 | | | |
| ch20 | 2707 | 5–10 | | | |
| ch21 | 1987 | 4–8 | | | |
| ch22 | 1674 | 3–7 | | | |
| ch23 | 1523 | 3–6 | | | |
| ch24 | 2501 | 5–10 | | | |
| ch25 | 3407 | 6–13 | Drakken POV | | |
| ch26 | 5082 | 10–15 | 最长章 | | |
| ch27 | 1064 | 2–4 | | | |
| ch28 | 1781 | 4–7 | | | |
| ch29 | 2080 | 4–8 | | | |
| ch30 | 1051 | 2–4 | Nikolai POV | | |
| ch31 | 471 | 2 | 最短章 | | |
| ch32 | 1786 | 4–7 | Aelindor POV | | |
| ch33 | 4476 | 9–15 | | | |
| ch34 | 2214 | 4–9 | Drakken POV | | |
| ch35 | 1572 | 3–6 | | | |
| ch36 | 2504 | 5–10 | | | |
| ch37 | 3126 | 6–12 | | | |
| ch38 | 921 | 2–4 | 末章（尾部预告行禁引） | | |

总览三篇（ch38 后）：00_概述.md / 00_金句精选.md / 00_情感节点.md
完工定义：gate.sh EXIT=0 + 总览门禁 + T1 自检三件（t1-verdict.md / t1-candidates.txt / 台账一行「自检」）
T1 抽样：>40 章不适用（38 章 → 1/4 = 10 章，首末必含）
