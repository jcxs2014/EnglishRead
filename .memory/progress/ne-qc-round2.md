# Null Entity 二轮质检（2026-10-09 22:29 UTC）

## 一、章层门禁（23/23 章，全部重跑，不采信此前数字）

```
verify_quotes      总计 164/164 引文可核实（100%）；完全干净文件 23/23；正文章节 0 提取 0；总览 0 提取转交 0
verify_quotes --full  …… --full 整串取证 0                      （52 字符指纹盲区已关）
check_short_quotes verify_quotes 跳过（<20 flat 字符）的引语：7 条 → ✅ 命中 7｜⚠️ 别的章 0｜🔶 跨标签拼接 0｜🔧 B类 0｜❌ 查无 0
check_chapter_quotes  逐章 23 次，非满命中行 0 行（全部 numerator==denominator，无 MISS）
sweep_full         ✅ 本章命中 164｜⚠️ 跨章 0｜🔶 跨标签拼接 0｜❌ 全书查无 0
check_vocab        词条行合计 591 —— FAIL (0)
check_entities     0 个文件存在未知实体
corruption_scan    FAIL 0 处（U+FFFD / 双句号）；报告 0 处
件数               md 23 == text/ch*.txt 23；keyphrase 重复 0
```

**提示型（只记不改）**：`check_vocab` 基础档疑含超纲词 3 条 —— ch21 `caregiver`／ch21 `companion`／
ch22 `emergency lights`（词长 ≥9 启发式误报，均为文中真实词，不改）。

## 二、g5 停摆后的 ch11–13 语义复核（完成，无阻断型）

逐条取证（全部大小写无关、弯/直引号归一后对该章 `text/` 验）：

| 断言 | 落点 | 判 |
|---|---|---|
| 「六个我的表亲」 | ch11 `six of my cousins` | ✅ |
| 「我们没时间」／`That's an order`／`Veonya`／`He'll be fine` | ch11 全部逐字在 | ✅ |
| 「舱尾湿件装置＝Aliers 一开始的安排」 | ch11 末段 `this, I knew, was what she had wanted us to see` | ✅ |
| 「Aliers 第一次被写成会下令牺牲的人」 | ch01–10 grep `Aliers…order/sacrific` 仅 ch10 一句 `Aliers barked an order`（进舱），无下令牺牲 | ✅ 可核最高级成立 |
| 「上一章最后写四人从对接闸门进入货箱舱段」 | ch10 91% 处 `The four of us entered the cargo wing together`，随后即末两段湿件/六支枪 | 提示型：`最后` 指末节而非末句，措辞松散但不错 |
| ch12 `LYREBIRD MARK II PRIME`／`Sable Alzian`／线人＝`Our contact swore…`／`You're not Wylla Sotain, are you?` | 逐字在 | ✅ |
| ch13 `Renata Aliers's mind was full of thorns`／`withered under the sun of reality`／`Renata`+`General` 同章 | 逐字在 | ✅ |
| ch11–13 跨章引用形式 | `chNN` 出现 **0 次** | 该类为空 |

## 三、总览层并发碰撞（第二次同类事故，编排方责任）

- 22:23 派出的概览代理始终在跑；主会话按「代理已停摆」假定于 22:25–22:27 自写了三份
  `.overview_templates/ov_00_*.md.tpl`，随即被代理在 00:28:05–00:28:06（本地）覆盖，
  `ov_00_金句精选.md.tpl` 到 00:29:05 仍在增长 ⇒ **代理在制品期，主会话不得写同一批文件**。
- 与 ch11/ch12 那次同源：**扩范围前必须先确认原范围所有者是否已死**，而不是看它有没有落盘。
- 处置：代理三份（含主会话版 `情感节点`）快照进 `.memory/progress/ne-ov-agent/` 作恢复基线；
  磁盘上 `$BOOK/.overview_templates/` 交给代理，等其回报后再验。
- 主会话自写版的成果没有浪费：其 `build_pool` 依赖的 `{P:NN:seq}` 用法、以及
  「inline 英文片段须逐字锚定章」自查脚本口径已在本轮跑通（见下）。

## 四、总览层待办（接力点）

1. 收代理回报 → 三份 tpl **逐条验**：`{Q:NN:seq}` 是否存在于池中（`gen_overview` 会 exit 2 兜底）、
   中文事件断言只取 `ne-facts-part1/2.md` 带 `(chNN L行号)` 的行、悬置点 12＋10 条不写判词
   （尤其：叙述者生死／Wylla ch22 身体结局／Prime 下场／ch01 匿名邀约者／七个月起算点）。
2. `python3 scripts/gen_overview.py "$BOOK"` → 产出 `00_概述.md`／`00_金句精选.md`／`00_情感节点.md`。
3. 总览门禁：`verify_overview_quotes.py`／`check_overview_full.py`／`check_overview_labels.py`／
   `check_entities.py`，再手工 grep 总览层 inline 英文（**无门禁覆盖**，本轮自写版即靠此抓出
   `tightened` 一处不属于 ch11 的插入）。
4. 全书 `bash scripts/gate.sh "$BOOK"`（读条目行，不看退出码）＋ 原始输出归档
   `.memory/raw-gates/null-entity-by-seth-haddon/`。
5. `post_collab.py` 完工通报（注明「五步审查未做（待用户发起）」）＋ daily 日志，
   与章文件**分次**提交，一律 `git commit -- <pathspec>`；**禁止 push**。
6. `H1` 核对：`grep -m1 '^# ' 00_*.md` 三篇语义互不串（第 9h 条配套机检）。
