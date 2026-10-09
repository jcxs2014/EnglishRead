# ne-g9 交付报告（ch21 / ch22 / ch23 Epilogue）

生成时间：2026-10-10 · lane：完整 lane（library/ 有 epub；本组按 brief 只跑 ne_strict 自检，全书级门禁由主会话执行）

## 交付文件与自检

| 文件 | 块数 | ne_strict | 写前断言（frag in src + 块内段相邻） |
|---|---|---|---|
| `$BOOK/ch21 watch us.md` | 7（中章 5–8 ✓） | FAIL 0 / WARN 0 | 77 条全过（/tmp/ne_g9_frags21.txt） |
| `$BOOK/ch22 the last coherent thing.md` | 8（中章 5–8 ✓） | FAIL 0 / WARN 0 | 131 条全过（/tmp/ne_g9_frags22.txt） |
| `$BOOK/ch23 hello wylla.md` | 4（短章 3–6 ✓） | FAIL 0 / WARN 0 | 64 条全过（/tmp/ne_g9_frags23.txt） |

词表全部走 `vocab_candidates.py --ch N --tiers` 粘贴做减法，例句逐字回验在各自 text/；释义纯中文；专名行（VisorForge/Subsidiary/LYREBIRD/Directory）未收词表。三文件 corruption 标记（U+FFFD/双句号）为 0。keyphrase：watch us / the last coherent thing / hello wylla（当前目录无重名；他组在制品未读，若总门禁撞名由主会话裁决改名）。

## 跨章指涉核证（当场 grep，行号为 text/ 文件行）

- ch21→ch20：`The world went white.` = ch20:93（末段）；Rahn/Sira 在场与“你致歉道谢催动手” = ch20:78。
- ch21→ch22：孢子程序酝酿句 = ch22:132；下章首句坠落 = ch22:15（md 内以中文转述，不嵌他章英文原句）。
- ch22→ch21：`I jumped.` = ch21:144（md 内中文转述）。
- ch22→ch01：`Do you want it? Come and get it, scavenger.` = ch01:298，邀约消息段 = ch01:283；GIRS 抹除成幽灵段 = ch01:259。全书检索 `Come and get it` 仅 ch01:298 + ch22:90 两处；`Sorry I didn’t tell you` 仅 ch22:153；`Orkit` 仅 ch22:69（正文未展开事件）。
- ch22 B2“三方同段名单此前无”：逐段比对 ch01–ch21，无一行同列 Subsidiar*/Syndicate/Thorned（工具级复核过，非目测）。
- ch23→ch22：`I stripped the GIRS, nullified every entry` = ch22:171；`In every feed…` = ch22:183。
- ch23→ch01：`breath catching` 共享体感写法 = ch01:39；开篇两词匿名宣告 = ch01:15。
- 人名规则核查：三章 md 使用的全部专名均在本章 text/ 逐字存在（程序化比对通过）。

## 结局与悬置点：原文写了什么 / 没写什么（供总览层，总览不许越界断言）

**原文明确写了的：**
- ch21：RABBIT 死亡是直陈（`RABBIT was dead.` ch21:105）；本章末“我”背 you 跳进竖井（ch21:144）。
- ch22：Aliers 死亡有直陈——`taking her final breaths`（ch22:93）、`The line cut out.`（ch22:99）、`Aliers’s death had opened`（ch22:132）。飞船撞入 VisorForge Solutions server room（ch22:111）。Four 载体濒死、LYREBIRD 被 Prime 捏碎、`That version of me vanished.`（ch22:78–81）。“我”成为 every mask、剥掉 GIRS 注销每条记录（ch22:168–171）。末句 `But the last coherent thing I ever thought was: Wylla.`（ch22:186）——**原文只写了“连贯性在此终止”**。
- ch23：时间锚 `It’s been nearly seven months.`（ch23:51）；Wylla 在 Gamma sector 边缘小行星独居务农、`LYREBIRD PRIME, which sometimes powers on`（ch23:51）；广播确认旧记录体系崩毁（ch23:27–45）；她对空喊 `“Sable?”`（ch23:60）并得到回应 `“Hey.”`／`“Hello, Wylla.”`（ch23:69/78），末句 `There you are. I’ve missed you.`（ch23:81）。两人关系原文措辞：`Two women in love.`（ch23:66）。

**原文没写、不许替原文下结论的（悬置清单）：**
1. **叙述者生死**：ch22 末句不能读作死亡宣告，ch23 的回应也不能读作复活证明——两侧原文都不背书（md 已按此写）。总览层禁用“Sable 死了”“Sable 复活了”两种表述。
2. **Wylla 在 ch22 反攻后的身体结局**：ch22 只写 `You chose, as you had always chosen, not to die.`（117）与“我”接管战斗；生死均未写。她在 Epilogue 活着是 ch23 的信息，**不得回写成 ch22 的结局**。
3. **Prime 的最终下场**：ch22 只写 `drove Prime mad`／`forced Prime back`／Subsidiary bodies `drop and bloom with infection`，没有一句写 Prime 被摧毁或死亡。
4. **ch01 匿名邀约者身份**：`Come and get it, scavenger` 说话者全书未揭示（仅两处出现）；不得写“是 Aliers/是叙述者/是 Order 发的”。
5. **`Funny, to die the same way twice.`（ch22:75）**：“第一次”指什么原文未解释。
6. **ch23 广播里的 “the Specter” 指谁**：原文未裁决；紧接着只说 `your lingering legacy`（48）把遗产按在 you 身上。不得断言 Specter＝叙述者或＝Wylla。
7. **`There I am, waving back at you.`（ch23:72）的性质**：实像、幻觉还是记忆成像，原文不判。
8. **七个月从何事件起算**：Epilogue 未写锚点事件；`days old` 的广播延迟与“是否还有过其他回应”亦未写明。
9. **Mrs. Alzian / Wylla / Sable / Veonya / Alzian 的对应关系**：三个登记名式称呼集中在 ch21 十几行内、ch22 出现 `Sable Alzian` 与 `Sable Veonya` 并立（114），但**婚姻/载体/名字归属关系任何一章本节选都没写明**——总览层只可罗列原文称呼，不可归并成一句身份判定。
   - **补充取证（组内跨章 grep，非本章断言，仅供主会话参考后由总览层落笔）**：`Sable-wearing-LYREBIRD` 在 ch15:60 出现一次（同章 21/36/66/102/108 行另有 Four、Sable、Wylla）；`You appeared as yourself; I as Sable-wearing-LYREBIRD.` 逐字在 ch15。另计数（大小写敏感，`grep -c`）：Sable 在 ch15 出现 3 次、ch16 4 次、ch21 2 次、ch22 1 次——“我”的名字在中段章节密集、收尾两章稀疏，这一分布是**观察不是结论**，命名归属仍需主会话裁决后才可写进总览。
   - **本组 md 未使用上述跨章取证作断言**：ch21/ch22/ch23 正文只写各自 text/ 里可数的称呼与关系。
10. **Wylla 是否重返行动**：ch23 只写 `debating whether to contact the Thorned Root`（51），选择未写。

## 我不下判断的清单（逐章汇总，同上一节编号）

ch21：9（称呼归并）、1（跳井后生死衔接不写）｜ch22：1、2、3、4、5｜ch23：1、2（回写禁令）、6、7、8、10。

## 过程注记

- ch21 B4 的 “As LP, I” 与 “As Four, I” 为原文逐字片段（两处均在本段引语内，可数），非框架豁免；全章无任何 `…`/`...` 省略号（词汇释义列的中文省略号为字典用法，非引语）。
- “本章登记名出现顺序可数”（ch21 B6）、“三拍完成”（B5）等计数断言均可在同段引语内复点复核。
- 相对章号全部当场核过（清单见上），无未核指涉。
- brief 提示的 ch22 结尾句红线已落进 md：导航、B8、悬置清单三处一致执行“只写连贯性终止，不写死亡”。
