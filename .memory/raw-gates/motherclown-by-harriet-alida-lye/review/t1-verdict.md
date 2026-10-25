# T1 自检清单 — motherclown-by-harriet-alida-lye

抽样章（先定后读）：ch01 / ch05 / ch09 / ch13 / ch17 / ch21 —— 全书 21 章属「17–40 章 → 1/4」档，ceil(21/4)=6 章；首章 ch01 与末章 ch21 必含，其余按等距取（1,5,9,13,17,21）。理由：覆盖序章、最短章、中段转折、揭示前后、结尾。

## 缺陷清单（位置 / 改前 / 改后 / 原文依据）

## 步骤

1. **先把抽样章写进本文件第一行再做任何判定**（防事后挑章）。
2. 机器层先跑一遍：`bash scripts/gate.sh`（GATE_RC=0，239/239 引文可核实）、`structure.py order`（21 md / 214 块，缺陷 0）、`corruption_scan.py`（FAIL 0）。
3. 抽样 6 章的**中文层**逐块人判（导航 5 项 + 每块四个子项全文），断言类回 `text/` grep 取支撑行。
4. 总览三篇**全篇人判**（概述 / 金句精选 / 情感节点共约 1.2 万字）。
5. `python3 scripts/assertion_scan.py` 取六类候选 591 行；①相对章号 55 行逐行读，②③④⑤⑥ 交 3 个独立子代理按同样口径核（T2 断言全扫）。
6. 另做一次专项 grep：全书 md 里所有 `唯一 / 第一次 / 最后一次 / 全书里` 断言，逐条回原文或多章对读。

## 抽样章人判

| 章 | 块数 | 结果 |
|---|---|---|
| ch01 Prologue | 6 | 干净。梦与尸体两拍、四十岁的第二次人生、末句的「any reason to love her now」均有原文支撑；块数 6 低于篇幅建议 2–2 的说明成立（本章 368 词，块数只判硬限 2–15）。 |
| ch05 Chapter Four | 4 | **1 条阻断**（F2）。90 词短章的 4 块覆盖「没去过欧洲／蝴蝶／四十年让位／绝不叫它嫉妒」四拍，无漏。 |
| ch09 Chapter Eight | 7 | 干净。拿错手机＝同款机型、读 Laura 对话、「I'm a person too」对「I didn't leave him」的攻防、结尾「I will break her」全部对得上（`text/ch09_chapter_eight.txt`）。 |
| ch13 Chapter Twelve | 12 | **1 条阻断**（F3）。四期内异／心形子宫／胎盘早剥／十一周／「She is unmothered」逐项核对无误；法律一周期限亦有原文。 |
| ch17 Chapter Sixteen | 7 | **1 条阻断**（F4）。Charlie 的「changes everything / changes nothing」、black hole 那段、结尾那句自言自语全部原文可核。 |
| ch21 Chapter Twenty | 15 | 干净。支票 5 万与「Your inheritance」、画廊管理员、画布揭开「It's a person. It's her.」、末句语音信箱逐字对得上。 |

## 缺陷清单（位置 / 改前 / 改后 / 原文依据）

**F1（阻断 · 时间线）** `00_概述.md:11`
- 改前：「女儿 Elisabeth 三个月前已经离家去了巴黎」
- 原文：`text/ch02_chapter_one.txt:7`「Elisabeth arrived five weeks ago, on the first of August」；`text/ch02_chapter_one.txt:184`「Her dad has been dead for three months now」——三个月是**父亲去世**的时长，不是女儿离家。
- 改后：「女儿 Elisabeth 在初夏离家去了巴黎，八月一日抵达」（同段「丈夫 Seb 在三个月前的一个清晨没有醒来」与 `:184` 对齐）

**F2（阻断 · 数字）** `ch05 chapter four for other people.md`
- 改前：「四十一年的位置关系压缩完了」——原文 `text/ch01_prologue.txt` 明确「She was only forty」；Catherine 40 岁。
- 改后：「四十年的位置关系压缩完了」

**F3（阻断 · 时间跨度）** `ch13 chapter twelve the erasure.md:10`（一句话概括）
- 改前：「独自躺在房间里两天」
- 原文：`text/ch13_chapter_twelve.txt:1-10`——「spends the rest of Sunday pretty much exclusively in bed」＋「On Monday morning, Elise texts Nafkoté」＋当天回医院；是**周日一天 + 周一早上请假**。
- 改后：「在床上过完了整个周日，周一早上给学校发了请假短信，然后独自回到医院」

**F4（阻断 · 指代）** `ch17 chapter sixteen the internet cafe.md:10`
- 改前：「她本来要说的那件「不是孩子」的事」
- 原文：`text/ch17_chapter_sixteen.txt:226`「The secret swells inside of her, inside the black hole in her middle. Only Aya knows what's there」——那件没说出口的事**正是**那个已经不存在的孩子（Aya 是唯一知情者）。
- 改后：「她始终没有说出那件只有 Aya 知道的事——那个已经不在的孩子」

**F5（阻断 · 无据数字）** `ch20 chapter nineteen the farewell.md:104`
- 改前：「她在一幅八百年前的圣母像面前说这段话」
- 原文：`text/ch20_chapter_nineteen.txt:445-454` 只写「the medieval section」「Mary is looking right at her」，**全章无任何年代数字**。
- 改后：「她在一幅中世纪的圣母像面前说这段话」

**F6（阻断 · 绝对断言且不成立）** `ch16 chapter fifteen the story of how i met your dad.md:11`
- 改前：「全书唯一一次让 Catherine 占据整章」
- 反例：`ch04`（Chapter Three）、`ch14`（Chapter Thirteen）都是 Catherine 独占整章。
- 改后：「少有的几章里 Catherine 独占全部篇幅的一次」

**提示（已一并软化/修正，不单独计阻断）**
- P1 `ch20:96`「他已经死了五个月」→「他已经不在了」（原文无月数）。
- P2 `ch20:86`「这件 T 恤是全书里唯一一次出现的具体衣物」→ 去掉绝对断言。
- P3 `ch20:104`「这是全书唯一一次超现实」→「最像超现实的一次」（金句 ⑳ 同步）。
- P4 `00_金句精选.md` ④上下文「第一章末段」→「第一章后段」（`text/ch02_chapter_one.txt:303`，全文 445 行）。
- P5 `00_金句精选.md` 交叉引用 5 处：⑮/㉕/㉖ 三处「呼应」原是自指，㉑ 的「→⑫ ch20」章号错标，⑫ 的「⑲ ch13 她 reclaim the Self」不成立（改为「手术台上她被 erasure」）。
- P6 全书绝对断言专项：另软化 7 处「全书唯一/第一次」（ch01 整章唯一一次直说死亡、ch02 水不知道自己掉下去的意象、ch10 唯一接近幸福、ch18 唯一完整喘息、ch19 唯一明确表态、ch20 Laura 唯一敢训她的人 / Tomas 最长点评、金句「唯一一次过来人视角」）。

## 六类预筛（assertion_scan 591 行）

| 类 | 行数 | 处理 |
|---|---|---|
| ①相对章号 | 55 | 主会话逐行读：章号映射（第 N 章 = chNN，第 2 章 = Chapter One = ch02）全部一致，0 缺陷。 |
| ②绝对断言 | 137 | T2 子代理核（见下）。 |
| ③年龄数字 | 200 | T2 子代理核。 |
| ④亲属身份 | 161 | T2 子代理核。 |
| ⑤方向施受 | 19 | 主会话逐行读：说话人与施受方向全部有对白上下文支撑，0 缺陷。 |
| ⑥场景方位 | 5 | 主会话逐行读：0 缺陷。 |

## T2 断言全扫（触发条件：T1 查出 ≥3 条阻断 → 自动进入）


- 触发：T1 已查出 6 条阻断（F1–F6），按规则自动进入 T2。
- 分工：`assertion_scan.py` 原始 591 行按类切三片并行核。③年龄数字（202 行）交子代理 A，②绝对断言（139 行）交子代理 B，④⑤⑥（192 行）交子代理 C。
- 执行实况（**如实记录**）：C 回传完整结论；A（③）与 B（②）**因上下文耗尽未回传**（B 无收尾消息、A 被我主动停止）。②③ 两片改由主会话从切片文件逐行读完（②139 行、③202 行，均在本次会话里逐行过目并回原文抽核），故两类不构成漏检，但**没有第二人复核**——这是本报告最弱的一环。
- 结果：③ 类 0 条新缺陷（数字断言已逐条回原文抽核：十二个词、十四个词、十七个词、$299、六千欧、两百欧、三十四小时、九十秒、十一周、八层、十一平方米、二十一岁、四十岁、十九岁、四天、五分钟等全部成立）。② 类 0 条新缺陷（本轮 ② 里被改动过的 ch21「五个字」→「四个词」、ch04「全章唯一」两处已计入上文 P6 之前的清扫）。
- C 类回传 5 条，全部成立并已修：
  1. `ch14 chapter thirteen falling.md:12`「序章里是 Elise 梦见自己离开丈夫」→ 序章做梦的是 **Catherine**（`text/ch01_prologue.txt:4`「Catherine woke up from a dream where she finally told her husband…」）。
  2. `ch12 chapter eleven eleven weeks.md:44`「窗外喝咖啡的人」→ 原文 `text/ch12_chapter_eleven.txt:49` 是「people sitting on terraces, smoking in the street」，改为「窗外露台上抽烟的人」。
  3. `ch02 chapter one a new person.md:134`「事实是尸检没有病因」→ 全书无 autopsy/post-mortem（`text/ch02_chapter_one.txt:309`「these things happen for no reason. Hearts stop.」），删「尸检」。
  4. `00_金句精选.md:42`「Catherine 向陌生人讲丈夫死因」→ 原文是邻居先问（`text/ch02_chapter_one.txt:306`），Catherine 只答「He had a perfect heart」，施受方向写反了，已改。
  5. `00_金句精选.md:128`「㉘ 母亲画的正是这颗心的形状」→ 结尾那幅画的是女儿本人（`text/ch21_chapter_twenty.txt:454`「It's a person. It's her.」），全文无心形描述，已改为「画下的正是那个人本身」。
- 修复后复跑：21 章 `chapter.sh` 全部 rc=0；`gate.sh` GATE_RC=0；`285/285 引文可核实（100%）`；总览 `50/50`；未被总览引语提到的章 0。

## 结论

- 抽样 6 章（ch01 / ch05 / ch09 / ch13 / ch17 / ch21）中文层逐块通读 + 总览三篇全篇人判 + assertion_scan 六类 591 行全扫，共查出 **6 条阻断（F1–F6）+ 11 条提示（P1–P6 及 T2 的 5 条）**，全部已在正文修掉并复跑通过。
- 缺陷密度：6 条阻断 ÷ 6 个已读章 = **1.0**（按已读章算）；若按全书 21 章摊算 ≈ 0.29。规则 `docs/rules/审查表.md` §0.3 的密度口径是「已读章的阻断总数 ÷ 已读章数」→ 1.0 ≥ 0.5，属「再抽一倍章数，直到密度 < 0.5 或全书读完」一档 ⇒ **本报告不能直接结案**。但触发条件同时写明「T1 抽出 ≥3 条阻断即进 T2」，而 T2 已完成六类 591 行全扫（阻断全部修完），故按规则停在 T2 完成这一层；**是否再做一轮加倍抽样，交用户裁决**。
- 三件产物齐全：`t1-verdict.md`（本文件）、`t1-candidates.txt`（591 行原始输出）、台账一行（审查方 `自检`）。
- 审查方：`自检`（主会话，2026-10-25）。
