# ch03 4-verdict（T3 深审 · 边审边改）

R1：review/ch03/1-suread.json（8 条，子代理盲读，8/8 自检 PASS）。
R2：review/ch03/2-machine.json（chapter.sh --json verdict=ok，rc=0；9 块 10 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 装"饶命"离场 | ordered my nerves/spared his life/allowing him to leave 在引语 | "Making it appear that I had spared his life" 施事是她（第一人称 I）——中文"演出一副'是我饶了他一命'的样子"✓ | 对应 |
| 2 | 地下堡垒 | blessed/retreat/underground fortress 在引语 | 两个 "My" 开头同位语（实数 2，T1 已校正）✓ | 对应 |
| 3 | 三道爪痕 | triple claw marks/slash/distorted nose 在引语 | tore/carved/slanted/cut 四个暴力动词（started 非暴力不计）✓ | 对应 |
| 4 | 镇民仰望 | gaped/standing taller/revered 在引语 | they=gaped 的施事=镇民 ✓；"almost revered" 的半格保留在中文（"近乎受人尊崇"）✓ | 对应 |
| 5 | Celia 授名 | staring down her nose/Helena Basque/dresses like a man 在引语 | "she said"=Celia ✓；her redheaded friend tittered 是另一施事，md 未混淆 ✓ | 对应 |
| 6 | Pierre 银箭 | dipped all the tips in silver/a trace/scrap some metal 在引语 | 中文保留 Pierre 第一人称（我淬银/我谎报）✓；Papa=他父亲，被瞒者 ✓ | 对应 |
| 7 | Lisette 揭示 | Madame Lisette Leóne/targeting 在引语 | targeting 的施事是 Grenault、受事是 Lisette ✓（ch01 "For Lisette" 链条）；ch01 指认经 T1 校正 ✓ | 对应 |
| 8 | Frayne 通牒 | stay here/bringing them to our doorstep 在引语 | "he said"=Frayne（text 邻域 Monsieur Leóne 发言）✓；"you"=Helena ✓ | 对应 |
| 9 | 恐惧经济学+誓言 | frightened/a luxury I couldn't afford/destroy Grenault 在引语 | "I was frightened"=她 ✓；"before he destroyed me" 方向（他毁她）✓ | 对应 |

跨章引用核章号：原句1"上一章 Better to bluff"=ch02 原句5 ✓；原句7"ch01 里 Lisette 首次被 Devereaux 报名"✓（text/ch01_1.txt "For Lisette."）。
数字回原文：22 支="Twenty-two this time."；九年前="being locked out nine years ago"；several years（Frayne 质问）在 text ✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| "Someone has to." 立场宣言未进 md | text/ch03_3.txt: "I clenched my jaw. “Someone has to.”" 逐字 | 补入原句8 读者视角提示 | 提示→当场修 |
| Pierre 自幼相识关系未入 md | text: "We had known each other since childhood" | 导航与原句6 分析已立供给者关系 | 提示（不修，依据：关系层已覆盖，句子属背景铺陈） |

## 修复动作（边审边改）

- 原句8 读者视角提示追加 "Someone has to."（text 逐字）与誓言的同源关系。
- 修后 chapter.sh rc=0、gate.sh 退出码 0，pathspec 提交。

## 已核实为正确

- "两个 My"：引语内恰为 "My safe retreat…" 与 "My own private underground fortress." 两处——T1 校正后数字与引语一致。
- "记了九年"：7 岁狼袭（ch04）→ 16 岁（ch01 "sixteen-year-old"），与 ch07 "nine years ago" 自洽。
- 原句7 硬揭示两句在 text/ch03_3.txt 为相邻完整段，md 以 … 相接合法（fragments 逐片段命中）。
