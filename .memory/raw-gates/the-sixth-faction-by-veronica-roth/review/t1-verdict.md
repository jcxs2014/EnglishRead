# T1 自检结论（同会话自检，非异会话审查）

抽样章号（62 章 >40 ⇒ 1/5=12.4 向上取整 13 章；首章、末章必含，其余等距）：**ch01 / ch06 / ch11 / ch16 / ch21 / ch26 / ch32 / ch37 / ch42 / ch47 / ch52 / ch57 / ch62**。等距步长 62÷13≈4.8，取 1,6,11,16,21,26,32,37,42,47,52,57,62。抽样前先把这串章号写进本行。

## 一、抽样章人判

- **ch21 `ch21 everyone is bigger than you.md`**｜一句话概括「被**还没出院**的 Christina 撞见」→ 改「被**刚出院**的 Christina 撞见」｜原文 ch21："the bandage askew on her head … she just got out of the hospital."（她刚出院，不是还没出院）｜阻断（事实错）｜已改，chapter.sh rc=0。
- **ch47 `ch47 the hemlock bargain.md`**｜一句话总结「最后只留下**三个词**：I did it.」→「最后只留下**一句**：I did it.」｜原文 ch47 末句 "But I did it."（四词；同章导航「最后一句只有四个词」写对，总结与之口径不一）｜提示（措辞/计数口径）｜已改，chapter.sh rc=0。
- 其余 11 章（ch01/06/11/16/26/32/37/42/52/57/62）：导航 5 项、块内四子项、一句话总结逐条对原文，未发现事实错；抽查点均命中——ch01 "once every three months"（镜子）、ch06 "ninety"＋"shards of glass"＋侧门（emergency door）、ch11 "STAY LATE"＋donation center 折衣、ch16 Gretchen 开柜＋Boots 在场、ch26 "cocaptain"＋carousel＋"missing an entire crate full of guns"、ch32 "I didn't encounter any Divergent initiates last year"、ch37 "record time"＋枪打偏中肩、ch42 "10E"＋"Them before I"＋"you can call me Tobias"、ch52 半队 south/半队 north、ch57 "flames turn briefly blue"、ch62 "And I feel the wind."。
- 抽样章缺陷密度 = 2 ÷ 13 = **0.15 < 0.2**（可停）；但**全 T1 累计阻断 5 条**（抽样章 2 + 总览三篇 3），已达「≥3 条阻断 ⇒ 自动进 T2 全扫」的触发线 ⇒ **本 T1 结论：进 T2**，T2 为 62 章全扫（结论另见 review/t2-verdict.md）。

## 二、总览三篇全篇人判

- **00_金句精选.md ⑯**｜「全书**唯一**一次由 Four 自己承认『Tobias Eaton』还活着」→「全书**第一次**由 Four 自己在心里承认」｜反例 ch46："『No, my father coached me pretty thoroughly,』Tobias says…"（他自己用这个名字自称）｜阻断（绝对断言不成立）｜已在模板改并重生成。
- **00_概述.md**｜「Four 替 Peter 收拾残局、替 Eric 遮掩，也在 Candor 总部的那场大火里第一次明白…」→「在 Eric 眼皮底下藏档案，后来在医院里听母亲亲口讲 Candor 总部那场火」｜原文 ch29 Four 在病房："I want to think my mom isn't someone who would burn a building just to kill one man."（他不在火场）｜阻断（场景错配）｜已改。
- **00_概述.md**｜「那年只有 Abnegation 不办转派」→「那年没有人转入 Abnegation」｜原文 ch08："I've been told there are no transfers to Abnegation this year"（Caleb→Erudite、Felicity→Dauntless 是转出）｜阻断（事实错）｜已改。
- **00_情感节点.md 节点五**｜「遇见**独眼的 Christina**」→「遇见 Gretchen、Jove 和十三岁的 Mae」｜原文 ch15 中庭一幕无 Christina｜提示（人物错置）｜已改。
- **00_情感节点.md 节点十**｜「**五个人**赶上火车」→「一行人赶上火车」｜原文 ch62 无人数｜提示｜已改。
- **00_情感节点.md 节点六**｜「那是全书**唯一一次**她不靠说话制止一场流血」→「那一下没有一句台词」｜全书级绝对断言无据｜提示｜已改。
- **00_金句精选.md ⑮/⑨/㉒ 交叉引用**｜③→「⑮ 当武器」、⑨→「㉒ 母亲付代价」、㉒→「㉓/㉕」三处编号指错｜改指 ⑨、⑩、㉔/㉕｜阻断（交叉引用漂移）｜已改。
- 查重：三篇各自 Counter 计引语文本，dups 全 0（27 / 25 / 22 条）。

## 三、机器预筛与回灌

- `python3 scripts/assertion_scan.py "<书目录>"`：① 相对章号 33 行、② 绝对断言 255 行、③ 年龄数字 534 行、⑥ 场景方位 32 行（全读）；⑤ 方向施受 60 行、④ 亲属身份 220 行（各抽 20 行）；原始输出见 `t1-candidates.txt`。
- 改过的词回灌总览：`grep -n "还没出院\|三个词\|五个人\|唯一一次由 Four" 00_*.md` ⇒ 0 命中；改后的表述已在概述/金句/节点落定。
- 抽样章 suread 复用：13 章 `/tmp/sf-chNN-facts.txt` 重跑 `suread.py`，逐条 ✅、退出码 0；另抽 3 条事实回源（ch26 少一箱枪、ch42 10E、ch62 罗盘）。
- 复跑 `bash scripts/chapter.sh`（ch21/ch47 改后）rc=0；`bash scripts/gate.sh "<书目录>"` 正门结论 0 条阻断型、rc=0（⑭ 总览引文 80/80 可核实；⑳ 整书体检全 0）。
