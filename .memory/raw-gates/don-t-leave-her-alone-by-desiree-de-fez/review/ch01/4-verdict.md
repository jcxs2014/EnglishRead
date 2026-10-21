# 第 1 章 R5 判定（人工审查）

## §0 覆盖声明

- **本轮人工审查只覆盖第 1 章**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch01 chapter 1.md`）。
- 抽样理由：本章是全书第 1 章，开篇即定调，且内含三处容易出错的判定点——①块 2 的引文与「同一段台词，两种读法」的解读是否对得上（诗 vs 歌）；②`md:111` 借序章作类比时，耳环／耳洞与人物归属是否准确（序章是 Alba 线）；③`md:97` 的标点指针（分号 vs 破折号）。这三处都只能靠逐字回原文裁定，适合做人工抽验。
- **其余各章（ch00、ch02–ch17）本轮只有机器层，没有人工层，不写成「通过」**（依据 `docs/rules/审查表.md:31`：「抽样章号与理由写进 `4-verdict.md` 的覆盖声明；没跑的章要写「只有机器层」，不许写成「通过」」）。第 2 章的人工层由同一子代理另出 `review/ch02/4-verdict.md`，本章结论**不外推**到第 2 章。
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch01_chapter_1.txt`（30 行 / 6,308 字符）。
- 成品 md：`ch01 chapter 1.md`（153 行；引语块 8 个；`## 本章词汇` 21 条（⭐⭐⭐ 8 / ⭐⭐ 7 / ⭐ 6）；`## 一句话总结` 1 条）。
- 流程合规：R1 素读产出已落盘（`review/ch01/1-suread.json`，**已存在且已提交，本次未覆盖、未修改**）；R2 机器层重跑 `bash scripts/chapter.sh "…/ch01 chapter 1.md" --json` → 退出码 0、`verdict: ok`，复核输出落在 `/tmp/ch01_machine_recheck.json`，**未覆盖仓库内 `review/ch01/2-machine.json`**；R3–R4 出 `review/ch01/3-diff.md`；R5 出本文件。顺序符合 `docs/rules/审查表.md:37`。
- 引用取证口径：全部用显式路径 `/usr/bin/grep`（`text/` 被 `.gitignore` 忽略，`git grep` 对它永远查无），短词用 `-w`，括号匹配用 `-E`；字符区间为原文 UTF-8 解码后的 `[start, end)`。
- 签名：DSH-Mac

---

## §1 四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | 8/8 引语块逐字一致（100%）；`## 本章词汇` 21 条例句逐字一致（21/21，`not_verbatim=0`） | `bash scripts/chapter.sh "…/ch01 chapter 1.md" --json` → 退出码 0、`verdict: ok`、8 块 `ok=true`、`empty_quote=0`、`segment_miss=0`、`quote_long=0`、`issues` 四组全空（`/tmp/ch01_machine_recheck.json`）。自写脚本把 8 块引文归一化（`’→'`、`“”→"`、`—/–→-`、空白折叠）后在原文中定位到 8 处**连续**区间（偏移 2 / 315 / 498 / 2139 / 2586 / 3061 / 3892 / 5947），无省略号拼接的碎块。词汇表 21 条（去掉 3 行表头/分隔行）例句全部是原文子串。 |
| **对应** | 8 块 × 固定三问，全部能在原文指出出处（8/8 通过） | ①动词主语：块 1「dressed up / should be」＝学龄前孩子们／制作者（`text/ch01:6`，区间 `[2,340)` 附近，「to symbolize purity」为 `[142,218)`）；块 2「scanned / recited」＝Brisa（`:6`，区间 `[319,409)`）；块 3「switching to playback / decided to stop looking」＝Brisa（`:6`，区间 `[502,716)`）；块 4「she was sure」＝Diana（`:15`，区间 `[2162,2247)`）；块 5「She wanted him」＝Diana（`:15`，区间 `[2597,2657)`）；块 6「was crossing paths」＝Diana（`:18`，区间 `[3074,3338)`）；块 7「She longed for」＝Diana（`:21`，区间 `[3907,3980)`）；块 8「she had crossed / had sunk」＝Brisa（`:30`，区间 `[6039,6222)`）。②受事／宾语：块 3「the verses they had spent weeks preparing」（`:6`，区间 `[602,650)`）；块 5「him」「the decision」（`:15`，区间 `[2597,2657)`）；块 6「the parents of Brisa's classmates」（`:18`，区间 `[3206,3338)`）；块 7「a harmless flame」（`:21`，区间 `[3907,3980)`）；块 8「the golden crown her classmates wore」（`:30`，区间 `[6039,6162)`）。③归属方向：块 4「it had a temperature gauge」＝直发夹（`:15`，区间 `[2162,2247)`）；块 5「tell her what she knew already」＝她自己（`:15`，区间 `[2597,2657)`）；块 7「averted a total catastrophe」＝她（`:21`，区间 `[3982,4072)`）；块 8「Stung by her mother's absence」＝Brisa→母亲（`:30`，区间 `[6164,6222)`）。 |
| **形态** | 4 项子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）× 8 块 = 32 个子项行，**缺 0**；引语行形态 `> **原句 N:** "…"` 8/8 合规；块数 8 ∈ [3,10]（profile novels）；导航 5 项齐全（`md:11–15`）；`## 本章词汇` 三档齐全（8/7/6）；`## 一句话总结` 有正文（`md:153`）；H1 `# 01. Chapter 1` 符合本书 `N.` 形态 | `2-machine.json`：`h1_shape_ok=true`、`nav_count=5 ok`、`subitems_modal`＝4 项、`blocks=8`、`block_median=7.0`、`block_range=[5,8]`、`profile=novels`、`baseline: book`；`counts`：`struct_bad=0`、`empty_quote=0`、`keyword_bad=0`、`cjk_low=0`、`quote_long=0`、`segments=8`、`segment_miss=0`。**形态偏离说明**：机器层在每个块都报「关键词 CJK=0」，与兄弟章同体例（`ch02 chapter 2.md:23`、`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23`、`ch05 chapter 5.md:23` 的「关键词」子项同样全是英文短语）⇒ **假红**，非本章偏离。 |
| **断言** | 16 条关键断言逐条回原文取证（16/16 有据，0 条编造） | 见 §2 判定表 A1–A16；A7、A11、A13 已由作者在审查过程中改好（记为**已修复**），A8、A9、A10、A12 判「提示」，其余通过。 |

---

## §2 判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 8 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（8/8）；自写脚本归一化后定位到 8 处连续区间（偏移 2/315/498/2139/2586/3061/3892/5947） | 成立 | 通过 |
| A2 | `本章词汇` 21 条例句均为原文子串 | 自写脚本 `real rows: 21`、逐条 `NOT VERBATIM` 输出为空 | 成立 | 通过 |
| A3 | 块 1（`md:19-27`）对应「天使、纸板翅膀、金冠、纯白象征纯洁」 | `text/ch01:6`「The preschoolers had dressed up as angels… The idea was that everything should be immaculate white, to symbolize purity」（`[142,218)`） | 成立 | 通过 |
| A4 | 块 2（`md:31-39`）的主语是 **Brisa**，受事是「the Christmas poem」 | `text/ch01:6`「From the stage, Brisa scanned the room for her mother while she recited the Christmas poem」（区间 `[319,409)`） | 成立 | 通过 |
| A5 | 块 3（`md:43-51`）对应「表演切换成 playback、她决定不再找」 | `text/ch01:6`「She looked for her in the audience, her performance switching to playback… Failing to see her mom in the crowd, she decided to stop looking」（区间 `[502,716)`，其中「she decided to stop looking」为 `[689,716)`） | 成立 | 通过 |
| A6 | 块 4（`md:55-63`）对应「她确信直发夹有温控、会自动断电」 | `text/ch01:15`「she was sure it had a temperature gauge and turned off on its own when it got too hot」（`[2162,2247)`） | 成立 | 通过 |
| A7 | `md:51`「Brisa 在本章里**唯一一次**自己做主」 | `text/ch01:6`「she decided to stop looking」（`[652,716)`）＋ `text/ch01:30`「Stung by her mother's absence, she had sunk into the choir」（`[6164,6222)`）——:30 也是 Brisa 自己的决定；「唯一」不可核 | 不可核的绝对计数 | 提示（**已修复**：改「在台上第一次自己做主」） |
| A8 | `md:37`「观众会为这段稚气台词喝彩，母亲听见的却是自己缺席的证据——同一段台词，两种读法」 | `text/ch01:30`「After the poem, the kids launched into a loosely religious version of a Taylor Swift song. The parents laughed loudly…」＋「Diana's eyes clouded and her legs shook when, from the hallway, she heard the Christmas song」——父母喝彩在**歌**上；母亲在**走廊**听见的是歌，**诗已结束** | 归属错位（诗↔歌） | 提示 |
| A9 | `md:39`「Brisa 练了整周，而妈妈错过了整场」 | `text/ch01:21`「she had missed the start of the play」；`text/ch01:30`「Diana sat down alone in the last row」（`[5594,5630)`）＋「made a mask of the golden crown」（`[6039,6162)`）——她只错过开场，折皇冠那段她在场 | 与原文不符（措辞过头） | 提示 |
| A10 | `md:97`「破折号后那句自我辩解用 sure 开场」 | `text/ch01:21`「…she wasn't ridiculous; sure, she had missed the start of the play…」（`[3982,4072)`）；`/usr/bin/grep -c ";" text/ch01_chapter_1.txt` → 1（本章唯一分号，无破折号） | 标点指针错位 | 提示（**已修复**：改「分号后」） |
| A11 | `md:37`「真女王正站在楼下为一只插头发疯」 | `text/ch01:15`「But halfway there, her heart started pounding in her ears」（`[1664,1721)`）＋「So she hurried back up Balmes, teary-eyed, embarrassed」（`[2848,2902)`）——心慌在半路／巴莱姆街 | 地点错位 | 提示（**已修复**：改「走在去学校的路上」） |
| A12 | `md:111`「序章里……别人给她戴上的耳环，她连自己身上多了什么都不知道」 | `text/ch00:21`「ears were covered in new piercings… She counted nine hoops, all different sizes, five in one ear and four in the other」（`[1535,1628)`、`[1630,1712)`）——是**新扎的耳洞**，且她数清了九个 | 与原文不符 | 提示（**主体已修复**；残余：仍需点明序章是 Alba 线） |
| A13 | `md:12`「欲望线与恐惧线都还没露面」 | `notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/00_情感节点.md:58`「节点六：恐惧越过家门（ch06-ch07）」——恐惧线到 ch06–07 才跨出门，本章在家门内 | 用词过头 | 提示（**已修复**：改「都还没成形」） |
| A14 | `md:11`「一句话概括」与原文事件链一致 | `text/ch01:12`（计划出席）＋`:15`（半路折返）＋`:21`（无火无烟）＋`:27`「Diana arrived at the Christmas play late, her pinkie toes raw.」（`[4438,4499)`）＋`:30`（折皇冠做面具） | 成立（且「第一场演出」已改为「演出」，见 A15） | 通过 |
| A15 | `md:11` 原写「错过了女儿的**第一场**演出」 | `/usr/bin/grep -nw "first" text/ch01_chapter_1.txt` → 仅 `:30`（"or that the kids in the other year had gone first" 与 "The only child not singing"）；`text/ch01:12`「missed a school play」是往年旧例 | 凭空计数 | 提示（**已修复**：改「错过了女儿的演出」） |
| A16 | md 是否存在「原文无」的杜撰事实（编单） | 逐条核对 `md:11-15`、`md:19-111`、`md:113-149`、`md:153` 的事实性断言（人名／数字／时间／亲属关系／事件／地点／次数） | 无编造 | 通过 |

---

## §3 收口复核（本轮三处指定疑点的独立结论）

1. **「第一场演出」是否凭空计数——是，已修复**
   - `/usr/bin/grep -nw "first" text/ch01_chapter_1.txt` → 仅 `:30`（"or that the kids in the other year had gone first" 与 "The only child not singing"），本章**没有**任何「第一场」的依据。
   - `text/ch01:12`「She couldn't remember a Christmas when she hadn't put off her shopping, slipped out of a family dinner, or missed a school play…」——这处「missed a school play」是**往年**的旧例清单，不是本章这一次。
   - 结论：`md:11` 改为「错过了女儿的演出」成立。
2. **块 2 的「同一段台词，两种读法」是否成立——不成立（提示，已修复）**
   - `text/ch01:30`「After the poem, the kids launched into a loosely religious version of a Taylor Swift song. The parents laughed loudly…」——父母喝彩在**歌**上；「After the poem」明写 Diana 进厅时**诗已结束**。
   - `text/ch01:30`「Diana's eyes clouded and her legs shook when, from the hallway, she heard the Christmas song Brisa had been humming at home for weeks.」——她从**走廊**听见的是「the Christmas song」，不是块 2 引的那首诗。
   - 结论（已修）：`md:37` 改为「同一场演出，两种读法」并点明「诗她已错过」；`md:39` 改为「错过了开场那一段诗」。两处见 commit `1fcf5c7c6`／`128ec026d`。
3. **`md:111` 的序章类比是否成立——主体不成立，已修复；残余亦已修（已修复）**
   - `text/ch00:21`「her ears were covered in new piercings, full of earrings she'd never seen before. She counted nine hoops, all different sizes, five in one ear and four in the other.」——是**新扎的耳洞**，且她**数清了九个**（一边五个、另一边四个）；她不知道的只是「预约那天的过程」（「The appointment she couldn't remember must have been long, unhygienic, and cruel.」）。
   - `text/ch00:15`「the last time she'd been here, with Brigitte」＋ `:18`「in her daughter's favorite store, where Brigitte mistook cheap jewelry for the real thing」——序章的女人是带 **Brigitte** 的母亲（Alba 线）；`text/ch02:468`／`:477` 确认 Brisa 与 Brigitte 是表姐妹，分属两条线。
   - 结论（已修）：现写法「她自己身上多了九只从没见过的耳环，连多出来的是什么都说不清」已与原文对齐；补写「要注意那条线是另一个人的：序章醒来的女人是带着布里吉特的母亲，不是本章的戴安娜和布里斯卡」后，Brigitte 与 Brisa 不再混淆（commit `13f283033`）。

---

## §4 已核实为正确

以下写法在审查中看似有误，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **`md:27`「记住这个纯白标准。它在本章是幼儿园舞台的装饰，后面还会以更脏的样子回来」有出处**。依据：`text/ch02_chapter_2.txt:471`「The neckline of her leotard, white with silver trim, was soaked with blood.」（区间 `[35880,35955)`）——纯白被血浸透；另有 `text/ch00_prologue.txt:18`「rows of tutus splattered with red… a now-stiff crust of dried blood.」。⇒ 此前把它记为「无出处」是误判。
2. **块 6 的比较级排序译法正确**。依据：`text/ch01:18`「More humiliating than her slow but steady breakdown, than the feeling of becoming as lifeless as a dishrag, was crossing paths with the parents of Brisa's classmates…」（区间 `[3206,3338)`）——「崩溃 → 麻木 → 被顺路超过」三级排序与 md:85 一致。
3. **块 8 的「felon in a lineup」译作「列队照相里的小囚犯」正确**。依据：`text/ch01:30`「She looked like a tiny felon in a lineup, blindfolded with a band of sparkly paper.」（区间 `[6224,6306)`）。
4. **`md:14`「她没有哭闹，而是用沉默与自我遮蔽回应母亲的缺席」成立**。依据：`/usr/bin/grep -nw -iE "cry|cried|crying|wept|sobbed|tears" text/ch01_chapter_1.txt` → 退出码 1（本章**零**哭戏描写）；`:6`「she decided to stop looking」＋`:30`「crossed her arms and made a mask」＋「sunk into the choir」＝沉默与自我遮蔽。
5. **块 7 的「盼一场无害的小火」译法正确，且「什么都没发生，等于什么都没被证明」与原文同义**。依据：`text/ch01:21`「She longed for a harmless flame, something small she could easily put out, to prove to herself that she wasn't ridiculous」（区间 `[3907,3980)`）。
6. **块 5 的两样东西（确认与决定）提炼正确**。依据：`text/ch01:15`「She wanted him to pick up and tell her what she knew already… She wanted him to make the decision for her」（区间 `[2597,2657)`）。
7. **块 4 的「安慰句越长，问句越短」节奏分析有原文支撑**。依据：`text/ch01:15`「she was sure it had a temperature gauge and turned off on its own when it got too hot. But did it actually have a temperature gauge? Was she sure?」。
8. **md 未把 Carlos 写成「丈夫」，处理正确**。依据：本章原文用 `Her partner`（`:12`），全章无 `husband`；md 的 `md:145` 只在词汇例句里保留 "Her partner"。
9. **`md:15` 的「中途用一句独立成段的话当章节铰链（迟到、趾尖磨破）」与原文结构一致**。依据：`text/ch01:27`「Diana arrived at the Christmas play late, her pinkie toes raw.」——该行自成一段（区间 `[4438,4499)`），前后皆空行。
10. **`本章词汇` 21 条例句全部逐字命中原文**（自写脚本 `real rows: 21`，逐条无 `NOT VERBATIM` 输出），无需改动。
11. **机器层「关键词」子项 CJK=0 不是本章缺陷**。依据：`ch02 chapter 2.md:23`、`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23`、`ch05 chapter 5.md:23` 的「关键词」子项同样全为英文短语 ⇒ 全书体例，非形态偏离。

---

本判定只覆盖第 1 章；其余各章只有机器层，不写成「通过」。本轮**未改动任何成品 md 文件**，git 未执行任何操作（未 add / 未 commit / 未 push）；新增产物仅落在 `.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/review/ch01/`。
