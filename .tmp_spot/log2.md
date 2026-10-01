【工具变更】--full 全库复核：17 条真误引 + 4 条假红

**背景**：给 `scripts/gate.sh` 的 ① `verify_quotes` 加 `--full`（见本会话同日板条目）后，趁改动跑了一次全库扫描，想知道「52 字符指纹盲区」在历史上放过多少东西。

**扫描**（97 本有 epub 的书，逐本 `--full`，解析口径 `--full 整串取证 N`）⇒ **7 本非零**。⚠️ 首轮用 `grep -oP` 解析全数报 `grep: invalid option -- P`（macOS BSD grep 无 `-P`），输出「0 本非零」是**假结果**；改用 `sed -n 's/.*整串取证 \([0-9][0-9]*\).*/\1/p'` 后才拿到真数。

**复核方法（关键）**：不能直接拿 `--full` 的数字下结论——取证里混着**合规的 `…` 省略号拼接**（AGENTS 允许，省略号两侧须为原词）。复核脚本 `.tmp_spot/spot3.py` **直接 import `scripts/verify_quotes.py`，复用它自己的 `flat_alpha()`（NFKD + 先剥 `\n`/`\t`）与 `epub_flat_text()`（剥标签 + `html.unescape`）**，只多一步「按 `…`/`...`/`. . .` 切段逐段查」。
踩坑记录：自己重写 epub 展平时**漏了 `html.unescape`**，导致 `&#8217;` 之类实体把数字 `8217` 混进 flat 串，误报了一大批假缺陷；第一版 `spot.py` 还**没处理省略号**、且拿不足长度的尾段去比对，又误报 10+ 条。**两次假红都出在「自己另写一份口径」上**——复核必须复用被检工具的实现。

**逐条定位脚本** `.tmp_spot/diff.py`：把展平后的 md 引语与原文同位逐字符比，打印首个分歧点。

**阻断型 17 条（真缺陷；常规门禁 100% 全绿也放行）**：
| 书 slug | 条数 | 常规门禁 |
|---|---|---|
| `nine-perfect-strangers-by-liane-moriarty` | 10 | 1503/1503 **100%** |
| `society-of-lies-by-lauren-ling-brown` | 2 | 440/440 **100%** |
| `lucy-by-the-sea-by-elizabeth-strout` | 3（另 3 条已在常规门禁判 ❌） | 66/69 96% |
| `the-green-road-by-anne-enright` | 1 | 129/129 **100%** |
| `tomorrow-in-the-battle-think-on-me-by-javier-marias` | 1 | 65/65 **100%** |

逐条文件行号（`md:行`）：
- nine-perfect-strangers：`ch11 Frances.md:168`、`ch16 Jessica.md:98`、`ch21 Carmel.md:48`、`ch21 Carmel.md:58`、`ch23 Frances.md:238`、`ch23 Frances.md:378`、`ch25 Masha.md:108`、`ch26 Napoleon.md:278`、`ch31 Lars.md:128`、`ch61 Napoleon.md:78`
- society-of-lies：`ch12 chapter eleven maya.md:39`、`ch21 chapter twenty naomi.md:32`
- lucy-by-the-sea：`ch06 chapter one.md:42`、`ch07 chapter two.md:42`、`ch09 chapter four.md:62`（另 3 条常规门禁已判 ❌：`ch05:62`、`ch09:22`、`ch10:32`）
- the-green-road：`ch07 dublin.md:32`
- tomorrow-in-the-battle：`ch10 chapter ten.md:40`

形态举例（已逐字对照原文）：
- `ch16 Jessica.md:98` md：`…quite intellectual and spiritual, thought Jessica, which was good…`；原文：`…spiritual, she thought, which was good…`（动词在前，语法不成立 ⇒ 凭印象改写）
- `lucy ch09 chapter four.md:22` md：`…It's like some seizure is taking place…`；原文：`…It's like William put his fork down. It's like some seizure is taking place…`（**整句被静默删掉**）
- `the-green-road ch07 dublin.md:32` md：`open so you go sometimes`；原文：`open so there you go, sometimes`（词级损坏）
- `nine-perfect-strangers ch11 Frances.md:168` 首个分歧在展平后第 94 字符（引语的 **90%** 处）——指纹只覆盖前 52 字符，这条几乎整段都在盲区里。

**假红型 4 条（工具报警但内容没问题）**：
- `the-glass-girl-by-kathleen-glasgow` 3 条（`ch13 day_two.md:87` 等）、`see-you-yesterday-by-rachel-lynn-solomon` 1 条——逐段复核后**查无 0**，是合规的 `…` 拼接。
- ⚠️ see-you-yesterday 那条的取证片段尾部出现过 `...nightmarech08`，看着像章节标签粘进引语正文，**实为 `_strip_trailing_annot` 只剥尾部标注、该标注在引语中段**导致的取证展示怪相，不是内容缺陷。**初看很容易误判成真缺陷**。
- **结论：`--full` 不可整类接退出码**（会把这两本书误红），与本会话先前的判断一致。

**合规处置**：这 7 本都不是本会话产出，按 `AGENTS.md` 第 7 条**只出核对报告、未改动任何他人文件**；按完成报告硬要求，**原始逐行输出进本日志，协作板只留聚合数字 + 结论 + 一行指引**。板上用《书名》而非目录 slug，以免 `post_collab verify --book <slug>` 把这些书的条目数从 1 变成 2（本会话复核确认本书仍为「板：1 条 ✅」）。

**临时脚本**（工作区内，已随本次 commit）：`.tmp_spot/spot2.py`（分段复核，NFKC 版，保留作对照）、`.tmp_spot/spot3.py`（分段复核，复用工具口径，正解）、`.tmp_spot/diff.py`（首个分歧点定位）、`.tmp_spot/board2.md`（板正文）。