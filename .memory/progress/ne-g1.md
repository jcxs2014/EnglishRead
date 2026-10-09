# ne-g1 交付报告（ch02 / ch03）

组前缀 ne-g1 · 书：Null Entity by Seth Haddon · 书目录 `notes/books/novels/null-entity-by-seth-haddon`

## 逐章交付

| 章 | 文件 | 章字数 | 引语块数 | ne_strict 结果 | 词表行数（高/进/基） |
|---|---|---|---|---|---|
| ch02 | `ch02 desire outweighed the risk.md` | 19,169（>10K → 8 块档） | 8 | `=== ne_strict: ch02 desire outweighed the risk.md \| 块 8 \| FAIL 0 \| WARN 0 ===` | 12 / 14 / 6（共 32） |
| ch03 | `ch03 i woke to fire.md` | 18,595（>10K → 8 块档） | 8 | `=== ne_strict: ch03 i woke to fire.md \| 块 8 \| FAIL 0 \| WARN 0 ===` | 18 / 20 / 7（共 45） |

覆盖度（`src.find` 求各块首段字符偏移 / 章总字数，由 `/tmp/ne_g1_check2.py` 打印）：

- ch02 块 1–8 起始 0.1% / 2.0% / 5.3% / 13.9% / 38.7% / 66.1% / 75.5% / 93.4%（前中末三段均有）。
- ch03 块 1–8 起始 0.1% / 1.8% / 5.0% / 17.5% / 40.3% / 52.2% / 66.1% / 95.9%。

引语与分析层英文全部在动笔前经 `/tmp/ne_g1_check2.py` 做 `assert frag in src`（对各自 `text/` 逐字，非 flat 近似），输出 `ALL PASS`；多段引语一律先断言两段之间 `gap.strip()==''`（原文相邻自然段）才允许并入同一块；引语无省略号、末尾均落句读边界。词表行 100% 来自 `vocab_candidates.py --ch N --tiers`（脚本回查：ch02 32 行、ch03 45 行，均无「不在候选表」项，分档与脚本档位一致）。

自检（收尾复跑）：分析层英文片段回扫 `non-verbatim=[]` 两章皆空；`ne_strict` 两章 FAIL 0 / WARN 0。

## 块位与原文行号（供审校反查）

- ch02：块1 = 15+18；块2 = 21+24；块3 = 30；块4 = 45+48+51；块5 = 111+114+117+120；块6 = 220+223+226+229；块7 = 259+262+265；块8 = 325+328。
- ch03：块1 = 15+18+21+24；块2 = 27+30+33；块3 = 39+42+45+48；块4 = 93+96+99+102+105；块5 = 186+189+192；块6 = 228+231；块7 = 306+309+312；块8 = 444+447。

## 跨章指涉（当场 grep 的行号）

ch02 md 内：

- 「邀约的两个坐标在 ch01 末尾的讯息里已给出（Facility 34X、GTM-11）」= ch01:287。
- 「you 在 ch01:187 已经低声用过这个名字」= ch01:187（`“Sable,” you murmured.`）；ch02 内 Sable 三次 = ch02:117 / 265 / 274（grep 计数）。
- 「被回忆起来的消息板旧话」= ch02:72（`Am I better than you, Specter?`）；同一绰号的最早出处 = ch01:120、ch01:128、ch01:199。
- 「Subsidiary Four 在本章末首次正面登场」= ch02:313（`We’d never stood face-to-face with Four before`）；Four 索取身份的两问 = ch02:313、ch02:319；其授权声明 = ch02:331。
- 「本章后段两度回报」= 破门 ch02:304、种子 ch02:337；章末三事 = ch02:340/343 → 346 → 358（末行经 `tail` 核对为 ch02:358）。
- 「稍后被 tipped up 的 beak 与那道 seam of metal and flesh」= ch02:133（ch01 无 `beak`/`metal and flesh`/`LYREBIRD`，grep 无命中，故「第一次有可触碰的表面」成立）。
- 「对 Edenic Order 从修道式想象滑向 What if I'm wrong?」= ch02:75、ch02:78。
- 「legally 一词本章只出现这一次」= grep `legally` ch02 仅 1 命中（ch02:325）；`bastard` ch02 仅 1 命中（同处），ch03 的 `bastards` 属另一人（ch03:75）。
- 「名字 Sable Alzian 在本章只出现一处」= grep `Alzian` ch02 仅 ch02:265。

ch03 md 内：

- 医护所问的「你的广播」→ ch01:72（`Our counter-ad carried the contract…`），覆盖范围 → ch01:51（sector-wide drop, thirteen stations and three planets）、ch01:104。
- 「the Specter 这个绰号消息板上已用」→ ch01:120、ch01:128；「缺失本身就是警报」→ ch01:259。
- 叙述者认出的「设施里那个女声」→ ch02:277（该行英文 `rough with fatigue` 属 ch02，故 ch03 md 内只作中文转述，未引英文）。
- 「上一章那段录像：LYREBIRD 被戴到活人头上、腔体里一片空」→ ch02:259–268（`hollow cavity` 在 ch02:268）；本章对应 = ch03:306。
- 「Vick 这个名字在 ch04 又被 you 提起」→ ch04:33（`And then there was Vick. You’d drawn the same conclusion…`）。
- 「Four 当众报出过她的名字」→ ch03:279；「两次循环播放」→ ch03:420 与 ch03:447（grep `replayed` 仅此两处）。
- 「替两人挡下爆炸」→ ch03:60；「断指收进口袋」→ ch03:350，开门 → ch03:429。
- 「医护用 they/them」→ ch03:222、228、231、246、273（分析层已改用以避免中文「他」误置性别）。
- 「你本章并非无台词」→ ch03:369、387、429、432；末声 `Wylla!` = ch03:459，末行 = ch03:462（`tail` 核对）。

## 页码 bleed / 形近规避

- ch02:72 论坛串尾 `If you can keep up …` 带粘连省略号，未入引语，仅在分析层以行号引用；同句的 `Am I better than you, Specter?` 已入分析层（逐字命中 ch02:72）。
- ch03:339 `“You can’t … have her—!”` 内含省略号，未引；分析层用 ch03:342/345/348 的动作事实替代。另外 ch03:237（`If they take HelixCare next …`）、ch03:279（`“Where…?”`）、ch03:291（`punishable…`）均带粘连省略号，未入引语块。
- 章名关键词均来自本章原文首行级语句（ch02 `Desire outweighed the risk` ch02:18；ch03 `I woke to fire` ch03:15），未取自他章。

## 不敢下判断的清单（总览层需用）

1. **I ＝ LYREBIRD 的物理关系仍未裁决**：ch02:30（裸肤贴表面）、ch02:133（beak 与 metal and flesh 的缝）、ch02:262（`the horror of my own, a vessel I had never truly controlled`）三处方向不同——「桌上之物」与「自身之体」并存，本组未择一定论。
2. **谁引爆了 Facility 34X**：ch02:358 只写 `Behind us, the facility exploded.`；ch03:27 提供两个未择一的原因（`Whether from the blast or the Subsidiary’s dart`），ch03:84 把它定性为 Order sabotage，ch03:414 行星广播改口 `suspected act of ecoterrorism`。文本没有权威答案，md 内一律只复述来源。
3. **医护之死**：ch03:294 只有 `the shot and the answering thud`，开枪者未被点名（语境强烈指向 Four，但未写明），md 未写成「Four 杀了医护」。
4. **断指数目不一致**：ch03:63 写这台 Subsidiary 自伤后 `Two fingers and part of an arm were gone`，而 ch03:345 被打掉的是 `three fingers hit the grime`（同一台机器同一批手指，本章内两个数不同）；开枪—掉落—收指三句依次在 ch03:342/345/348/350，开门在 ch03:429 只写 `the severed fingers` 未计数量。md 未强行调和，涉及该处一律写作「断指」不带数。
5. **`Fyster’s airlock`（ch03:429）无本章前指**：grep ch01/ch02 的 text/，`airlock` 无命中，指涉对象不明（疑指 ch01 的 Fyster 船事件，但书中未在本章前写过气闸），md 未作解释。
6. **Wylla 是否对 Four 自报过身份**：ch03:279 Four 猜出 `Most likely Wylla Sotain`，ch03:234 的 `Yes.` 只对医护说；她是否曾对 Four 口头承认，前六章无文本证据。
7. **孢子是否永久**：ch03:390 治愈大腿、ch03:408 `The spores have compromised RABBIT`，一好一坏同时发生；后续代价书中本组未写，md 未断言「治好了」。
8. **Ray 之死归因**：ch03:75 只有哀悼者的指控（`Their machine—it killed Ray!`）与 ch03:78 `her howl made the truth plain`（叙述者承认这是情绪判断），Subsidiary 是否真的杀了 Ray 未被文本确认，md 写为「她认定」。
9. **`Edenic Order Thorned Root` 与 ch02:75「被荆棘根缠住的树苗徽记」的关系**：符号已在本组两章出现，但该分支与 Order 主体是否决裂、指挥链如何，书中未交代，md 只并列证据不下结论。
10. **年份线**：ch02:181 终端日志 `Corporate Year 338`、ch02:238 录像角标 `Corporate Year 339`（`Which was this year.`）；两值差一年与「录像拍摄于别处（Martial Syndicate territory?）」同段出现，本组未据此推断时间线。

## 其他

- 未执行任何 git 写操作；只写了上述两个 md 与本报告；临时脚本为 `/tmp/ne_g1_check.py`、`/tmp/ne_g1_check2.py`。
- 名字门（规则⑥）执行结果：ch02 首次出现 `LYREBIRD`（ch02:30）、`Sable Alzian`（ch02:265）、`Subsidiary Four` 正面登场（ch02:313）；ch03 首次出现 `Governor Elric Vick`（ch03:180）、`Marek Cintel`（ch03:126）、`Ray`（ch03:39）。`Parallax`／`HoloProp`／`Pell` 不在 ch03 正文，故 ch03 md 未用其锚定；`spores` 不在 ch02 正文，故 ch02 md 未提前使用。
- 五步审查：未做（待用户发起）。
