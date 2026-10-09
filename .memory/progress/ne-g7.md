# ne-g7 交付报告（ch16 / ch17 / ch18）

组前缀：ne-g7 · 书：Null Entity (Seth Haddon) · 2026-10-09
临时脚本：/tmp/ne_g7_assert.py（写前断言：引语逐字 + 末尾句读 + 多段块相邻性 + 分析层英文片段；全过）
git 写操作：未执行任何一条（仅 ls/grep/python 只读）。

## 逐章清单

### ch16 → `ch16 infinity mirror.md`
- 块数：8（中章 9278 字符，覆盖 L15→L210 前/中/末）
- ne_strict：块 8 | FAIL 0 | WARN 0
- 省略号引语：0；<20 字符裸短引语：0
- 跨章指涉（当场核过的行号）：
  - 「Pholan's World 雪中身体闪回与 ch02 所记『你找到我』同景」→ text/ch02_chapter_2.txt:181（"just four months before you found me on Pholan's World"）
  - 「It won't be dead for long」「calling its nanobots to life」均本章内文（ch16 text:57、192）
- 不敢下判断的（留给总览）：
  1. schism 的具体史实——本章只有邀请函措辞且带 "At least, that's what VisorForge's invitation claimed" 的 hedge；和谈真伪不裁决。
  2. "three thousand strong" 是谎言还是情报未明示（Aliers 一行前 Rahn 只说另一句"which was the truth"，覆盖范围不扩）。
  3. 「我」复制成多份的实例模型（LYREBIRD PRIME／原壳／Four 体内三者关系）本章只写动作，不写本体论。
  4. LP 的物理定义不在本章。

### ch17 → `ch17 welcome home.md`
- 块数：8（中章 9024 字符，覆盖 L15→L152）
- ne_strict：块 8 | FAIL 0 | WARN 0
- 省略号引语：0；<20 字符裸短引语：0（末块 P2 "And when this was over, we'd be free." 38 字符）
- 跨章指涉（当场核过的行号）：
  - 「trials 中受试者死亡前文有记录」→ text/ch02_chapter_2.txt:244、text/ch09_chapter_9.txt:114（"every subject broke"）；另 ch03_chapter_3.txt:306 亦见 "LYREBIRD's trials"
  - 「null entity 警报反转回指第一章」→ text/ch01_chapter_1.txt:259（"That absence was its own alarm"）
  - 「no longer the mouse of BTW-02」的 BTW-02 出处 → text/ch04_chapter_4.txt:320、text/ch08_chapter_8.txt:213
  - LP 词源（Lars P. Olivier）→ text/ch01_chapter_1.txt:259；md 内仅以「伪装名」措辞带过，未扩写
- 不敢下判断的：
  1. 「你格式化 Four」发生在何时、格式化与此刻壳内运行的「我」的关系——本章不解说，md 明确标注「本章只带走一个事实」。
  2. Aliers 是否随队登舰之后的安排（本章她留守船上，后续不推断）。
  3. Fulvia 被注入 daemon 后的下场——本章只写"shot a daemon with Four's ID into her"，未写后果，md 不预测。

### ch18 → `ch18 have you been compromised.md`
- 块数：8（中章 7230 字符，覆盖 L15→L159）
- ne_strict：块 8 | FAIL 0 | WARN 0
- 省略号引语：0
- 短引语备案（<20 字符，已回源核行号）：原句 8 末段 "It is not."（13 字符）→ text/ch18_chapter_18.txt:159，系 Prime 三连问答的必要一轮，逐字无误。
- 跨章指涉（当场核过的行号）：
  - 「Why are you doing this? 与上一章叙述者心中原句逐字相同」→ text/ch17_chapter_17.txt:96（"Why are you doing this? I wanted to ask him."）
  - 「display box 即上一章要安插士兵之处」→ text/ch17_chapter_17.txt:60
  - 「arena 里的 chaff masks 上一章刚发给 Syndicate 士兵」→ text/ch17_chapter_17.txt:129
  - 「杀人与销售共用声线」的前章判词 → text/ch17_chapter_17.txt:24（md 内已按规则改用中文转述，不引他章英文）
- 不敢下判断的：
  1. "Why are you doing this?" 说话人归属：依 L39 "the pressure broke your composure" 归为「你」，原文无显式 said——md 用「你的 composure 先破，问出」表述，总览引用时注意这是上下文推断而非标注。
  2. "There were three Subsidiaries"/"They ran out" 的所指与去向——本章只两行，md 标为数目疑云，不点破。
  3. Prime「抬手」（It raised its hand, and the feed went dead.）的动作语义——本章不解释，md 明示「不解释」。
  4. "For old Earth" 是否指真实地球——文本不给，md 只写「乡愁」。
  5. Wood 与 Syndicate 拆 Federation 设备的授权关系——Curiously 一句只记录现象。

## 人名/专名合规自查
- ch16 md 出现的专名全部在本章 text/：Aliers、Rahn、Sey、Sotain、LYREBIRD、LYREBIRD PRIME、Prime、Four、Subsidiary、RABBIT、Thorned Root、Edenic Order、VisorForge、Corporate Federation、Martial Syndicate、Pholan's World、Wylla、Wylla Sotain、Sable。
- ch17：上述基础上加 Sira、Fulvia、Balis-Tarok、BTW-02、LP、EO（均本章原文）；GIRS 不在 ch17 原文，已从 md 移除（改中文「登记身份」）。
- ch18：Sira、Rahn、Sey、Aliers、Wood、Beckhan Marshall Wood、LION、Balis-Tarok、Ms.、Flee、RABBIT 均本章原文；Fulvia、LP、daemon、null entity、Sable、GIRS 不在 ch18 原文，md 全部避开（改中文或不写）；modulation 越章词亦已移除。

## 词表
三章均从 vocab_candidates.py --ch N --tiers 输出整行粘贴、只做减法填纯中文释义；剔除全书通行专名行（VisorForge/Federation/Syndicate/LYREBIRD/Subsidiary/Balis-Tarok 等）；例句为脚本原样，未手打。

## 其他备注
- 章号映射按 brief 事实底座：chNN＝书内 Chapter NN，零偏移；文件名后缀用 text/ 的 chNN_chapter_NN 对应章。
- 未读、未引用其他组在制品 md；仅读 ch01 参考章与本章/他章 text/。
