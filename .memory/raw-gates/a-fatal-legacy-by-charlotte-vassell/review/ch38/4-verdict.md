# 4-verdict · A Fatal Legacy ch38 独立审查判定

- 审查员：独立审查实例（本轮为**异实例**审查，非自审自批；未参与本章写作）
- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch38 a skeletal hand is found in the institute basement.md`
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch38_38.txt`（13,543 字符）
- 读取顺序：**R1 素读（只读 text/ch38_38.txt，未看任何 md）→ 落盘 1-suread.json → 才开 md**（`1-suread.json` 已记录 8 条「谁做了什么」+ 人物关系 + 数字逐字）
- 配套产物：`1-suread.json` / `2-machine.json` / `3-diff.md` / `4-correspondence.md` / 本文件
- 纪律：机器能判的先跑（`chapter.sh --json` → exit 0）；人只处理漏／对应／说话人／施事归属／事实断言；报警先读行再定性；不改书目录任何 md、不 git add/commit；只写本落盘目录

---

## 一、四组数

| 组 | 分子／分母 | 明细 |
|---|---|---|
| **逐字** | **9/9** | 9 块引语逐字命中本章原文（机器 `chapter.sh --json` 9/9 `ok`，`segment_miss=0`；我另用 `str.find` 独立定位 9/9）。词汇表 27 条例句逐字取自本章原文（`check_vocab.py` 对本书 exit 0、ch38 零告警）。**0 处省略号拼接**（本章引语无 `…` 缝合） |
| **对应** | **9/9**（5 完全对应 + 4 部分对应） | 0 不对应、0 密度不足、0 说话人错配；1 处引语尾部（第 6 块末句）未被分析 |
| **形态** | **4/4** | H1 / 导航项名与项数 / 子项集 / 块数——见下节 §三 |
| **断言** | **审计 21 条**：阻断 2 · 提示 12 · 假红 2 · 跳过 0 · 成立 5 | 阻断 2 条见 §二；成立项与「假红」见 §四、§五 |

**阻断型合计 2 条**（另 12 条提示、1 条假红、0 条跳过）。

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（章:区间／逐字） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 一句话总结：「他在乡间看房时发现，**儿子**和未出世的孩子已经在等着入住一间空房间」 | md L124；原文 `text/ch38_38.txt:283` — `He supposed that this would be the nursery.`；`:204` — `He looked down at the rug, imaging a toddler crawling across it`；`:56` — `‘I can’t imagine losing your son, your brother and well, your husband all in a week.’`（本章唯一的 son＝Tabs 亡故的儿子）；`text/ch28_28.txt` — `‘Callie’s pregnant, it’s too early to say anything…’` | **凭空实体**：全书无「儿子」这个角色，且「儿子和未出世的孩子」并列与「只有一间婴儿房／一个未出世的孩子」自相矛盾。疑为「妻子」之误 | **阻断** |
| A2 | 导航「一句话概括」：「他自己却带着卡莉去乡间看房，**把另一个“等人来坐”的房间布置了起来**」 | md L11；原文 `text/ch38_38.txt:235` — `‘Because it’s my estate. Honestly, Caius.’ … ‘The plumbing and electrics have just been done. The plasterers are coming in a week or two. The kitchen will be sorted soon. You just need to pick out the cabinets.’`；`:289` — `‘once the kitchen is fitted it’ll be all yours. If you want it.’`；`:295` — `It was a done deal.`；`:283` — `He supposed that this would be the nursery.` | **施事写反**：把房子收拾好的（施事）是**马库斯**，凯厄斯只是在心里把空房间**定成**婴儿房；且与 md 自己的第 8 块（「把“我给儿子安排房子”演成…」）自相矛盾 | **阻断** |
| A3 | 导航「线索结构」：「**被翻出来的**「疟疾年日记」」 | `text/ch38_38.txt:165` — `‘Keep going through the malaria-year diary.’`；`text/ch33_33.txt` — `‘I started with the malaria year…’` | 实为「继续翻」，本章之前已开卷；新旧颠倒 | 提示 |
| A4 | 导航「视角」：「中段落在**卡莉的家庭线**」 | 场景结构：`:20`–`:97` 面包店（卡莉与 Tabs，家/友线在 `:50`、`:65`、`:92`，属 Tabs 家人）；`:105`–`:210` 公寓（案情线）；`:220`–`:298` Meadowview（父子） | 位置／归属含混：真正的家庭线在**首段**且是 Tabs 的家人线；中段是案情线 | 提示 |
| A5 | 导航「叙事手法」：「三段式（**咖啡馆**闲谈／…）」 | `:17` — `The Purple Toad Bakery`；`:189` — `‘The Purple Toad.’`；`:192` — `‘Yeah, I went there with Tabs.’` | 场景标签错，应作「面包店闲谈」（本章标题场景） | 提示 |
| A6 | 导航「视角」：「读者听到的“怪事”始终是**他转述过的版本**」 | `:150`、`:156` 为艾米直接引语；`:180` — `‘Everything all right?’`；`:183` — `‘Yeah,’ Caius said, staring at her.`（凯厄斯并未向卡莉转述这只手） | 措辞不准：读者听到的是艾米原话 | 提示 |
| A7 | 第 7 块「中文理解」：「塞满了他**从前几世的人与爱**」 | `:204` — `Like it was cramped with the **memories** of his previous lives, and loves.` | 漏译 `memories`（原文塞满的是记忆） | 提示 |
| A8 | 第 6 块引语第三句 `‘Not as stunning as you.’` | `:195` 全文；md L54 引语含该句，L56「中文理解」未涉及 | 引语与分析不对齐：要么补分析，要么摘掉该句 | 提示 |
| A9 | 第 1 块「为什么这样写」：「地下室于是从**堆东西的地方**变成了…而**安排这一切的人并不在场**」 | `:150` 全文（无「堆东西」，无「安排者」） | 解读外推；且与 md 同块读者视角提示／导航「本章没有交代布置者与观众」口径不一 | 提示 |
| A10 | 第 2 块「读者视角提示」：「发现物证与处理物证的人是两拨人——这解释了为什么“为什么现在才被翻出来”…没人能回答」 | `:150`、`:156` 全文（未说谁发现的手） | 推理跳跃；真正的「为什么现在」在 ch37（ Robbie 接手后开封地下室），不在 ch38 | 提示 |
| A11 | 第 4 块「为什么这样写」：「说明抄的人本就**认识当事人**」 | `:171` — `‘Why did they copy her life story and not just make something up? It feels really personal.’` | 原文只给「很私人」，未给「认识当事人」 | 提示 |
| A12 | 第 4／9 块跨块对位（照抄人生 ↔ 摆上仪式桌；空房间 ↔ 摆好的降神会桌） | `:150` 与 `:171`（原文并列，从不连接）；md 已用「读者难免…」「对照着读一遍」框定 | 解读成立，须保持「读者联想」框定，不可升级为「同一人所为」 | 提示 |
| A13 | 导航「人物弧线」：「最后**自己动手承认**“我们该搬走了”」 | `:207` — `‘We need to move, don’t we?’` | 病句（应为「自己开口」），内容对 | 提示 |
| A14 | 第 7 块「审判官」花园精灵 | `:204` — `the bright red hat of the judgy gnome`；本书 `text/ch15_15.txt` — `The sales assistant tried not to be judgy` | 译法偏字面（judgy＝爱评判的） | 提示 |
| A15 | 导航「线索结构」：「本章没有交代**布置者与观众**，只留下“被布置”这个动作本身」 | `:150` — `It was on a table set up for a seance.`（原文确无布置者／观众／时间） | **成立**——md 在本章专属判据上处理正确：没有编造布置者、也没有断言手的身份 | 成立（列入 §五 防误修） |
| A16 | 导航「一句话概括」：「在分部「**FRIDAY**」里」 | epub `OPS/package.opf` spine：Part-008 `FRIDAY`(p.225) 含 ch36–ch40；ch38 起页 243、标题 `The Purple Toad Bakery` | **成立**——md 正确；任务书给的「THURSDAY」为任务书口径错 | 假红（不计 md 缺陷） |
| A17 | 词汇表分档（⭐⭐⭐ 含 `wide-brimmed`、`plasterers`） | `python3 scripts/check_vocab.py "<书目录>"` → exit 0；`grep ch38` → 退出码 1（该章零告警）；本书同档既有 `plasterwork`(ch34)、`forensics`(ch39) | 分档符合本书实践，工具判红不成立 | 假红 |
| A18 | 说话人（1、2、5＝Amy；3、4＝Caius；8＝Marcus） | `:150`、`:156`、`:171`、`:10440`、`:7285` | 全部正确，0 处错配 | 成立 |
| A19 | 「两桩案子」的对比关系（旧凶手已死 vs 现行凶手仍在外面） | `:165` — `…that killer is probably long gone, whereas whoever killed Digby and Scott, possibly Jimmy too, is walking around out there.` | `whereas` 对比方向未写反 | 成立 |
| A20 | 「PCQV 与唱片公司是两个实体」 | 本章 md 仅有词汇例句引原文 `working for PCQV now`（`:132`），**未把 PCQV 说成唱片公司**（重塑项目主顾＝Eulalia）；无混同 | 成立 | 成立 |
| A21 | 「Singh / 手的主人是某人」类身份断言 | 全文零处断言手的身份；Caius 明写留作悬案 `:165` | 成立 | 成立 |

---

## 三、形态组（4/4 通过）

| 项 | 本书众数／profile | ch38 实测 | 结论 |
|---|---|---|---|
| H1 | `N.`（54/54 章） | `# 38. The Purple Toad Bakery` | ✓ 同形（章号 + 书中场景标题） |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | `## 本章导航` 下 5 项，**项名逐字相同** | ✓ |
| 子项集 | 4 项：中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | 每块 4 项，**无缺项无多项**（`chapter.sh` `struct_bad=0`） | ✓ |
| 块数 | 本书中位 7，范围 5–10；profile `mystery-thriller` 允许 3–10 | 9 块 | ✓ 在众数范围内（5–10），且 `chapter.sh` 形态段 `blocks=9 / block_median=7.0 / block_range=[5,10] / nav_count=5 / nav_count_ok=true / h1_shape_ok=true`。**无须写偏离理由**（若仍需一行：9 块高于中位 7，是因为本章三场景两条线并行，块数仍在本书区间内） |
| 章内骨架顺序 | `## 本章导航` → `## 精读` → `## 本章词汇` → `## 一句话总结` | 同形 | ✓ |

---

## 四、零命中断言自证（R5-补：命令 + 输出 + 退出码）

```
$ /usr/bin/grep -n -i -E "\bson\b|\bsonny\b|\bdaughter\b|\bchild\b|\bchildren\b" \
      notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch38_38.txt
56:  'I can't imagine losing your son, your brother and well, your husband all in a week.'
204: ... His mum loved children. Callie wouldn't be stuck in the flat on her own with a newborn while he chased down drug dealers.
退出码 0（命中 2 行；本章唯一的 son 属 Tabs，无 daughter，无 Callie&Caius 的儿子）

$ /usr/bin/grep -c -i -E "\bperform|\bstag|\bspectator|\baudience|\btheatre" \
      notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch38_38.txt
0
退出码 1（真零命中：ch38 无 perform/stage/spectator/audience/theatre 一类词；
          放宽到 theatr* 时只命中 ':41 Tabs theatrically sniffed'，与降神会桌子无关）

$ python3 - <<'PY'   # 全书 54 章扫 son/daughter 所属
… 输出 8 处命中：ch02 Rawiri 的儿子、ch08 无关、ch11 Fenella 的儿子(Digby)、ch28 证人的儿子、
  ch38 Tabs 的儿子、ch43 无关、ch52 Marcus 的儿子(=Caius)、xx_characters Caius 是 Marcus 之子
  ——无一处是 Callie 与 Caius 的儿子
退出码 0

$ python3 scripts/check_vocab.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
退出码 0（全书 WARN 若干，均在别章；grep "ch38" 无命中 → 本章零告警）

$ bash scripts/chapter.sh "<书目录>/ch38 a skeletal hand is found in the institute basement" --json
退出码 0，verdict=ok，quotes 9/9 ok，counts={blocks:9, segments:9, segment_miss:0, struct_bad:0,
empty_quote:0, keyword_bad:0, cjk_low:0}
```

---

## 五、已核实为正确（防误修，固定一节）

以下写法「读着像错」，回原文核对后**成立**，后续任何人不得以「读着不对」为由改动：

1. **导航写「在分部「FRIDAY」里」**——epub spine 实测 ch38 属 Part-008 `FRIDAY`（p.225，ch36–ch40），**正确**；改前请勿改成「THURSDAY」。
2. **导航「线索结构」写「本章没有交代布置者与观众，只留下“被布置”这个动作本身」**——原文（`:150`）确无布置者／观众／时间交代，**md 没有编造「谁布置的」**，是本章专属判据上处理最稳的一处。
3. **第 5 块「艾米答应再去查一遍伊索尔德·伯勒尔」**——说话人是 Amy（`:171` Caius 点名「Amy」后她的直接应答），**没写反**。
4. **第 3 块「那个凶手多半早就没了；此刻还在外面走动的，是杀了迪吉比和斯科特、可能还有吉米的人」**——`whereas` 的对比方向与原文一致，**两桩案子没写混**。
5. **第 9 块「马库斯正在排队那些可以推给儿子的行政事务」**——原文 `Marcus was lining up administrative tasks that he could push onto him`，**「推给儿子」方向正确**。
6. **词汇表 27 条例句全部逐字取自本章原文**，分档与本书实践一致（工具对本书 exit 0、ch38 零告警）——**不要动例句或分档**。
7. **第 8 块「把“我给儿子安排房子”演成“儿子瞒着我干的荒唐事”」**——施事（马库斯）与受事（凯厄斯）都正确；**是导航「一句话概括」写反了，不是这一块写反了**（修的时候别把对的那块改坏）。

---

## 六、本章专属判据的逐问回答

判据问：研究所地下室里摆着降神会桌子的骸骨之手；「物证被布置成一场表演」这一层——**谁布置的？布置给谁看？为什么现在才被翻出来？这只手是谁的手？谁下的命令？谁把它摆上去的？「表演」这个说法有没有被原文支持？**

**本章原文给出的全部内容只有一句**（`text/ch38_38.txt:150`）：

> `'It's got weirder. There's a skeletal hand in the basement of the Horatio Combe Institute. It was on a table set up for a seance.'`

逐问：

| 问 | 本章原文 | md 的处理 | 判定 |
|---|---|---|---|
| 这只手是谁的手 | **本章不交代**；Caius 明写留作悬案（`:165`：`I know it's tempting to try to work out who the hand could be but that killer is probably long gone`） | md **没有**给手的主人安名字 | 通过 |
| 谁下的命令 | 本章不交代 | md 不交代（导航「线索结构」明写「本章没有交代布置者与观众」） | 通过 |
| 谁把它摆上去 | 本章不交代（原文只有被动 `It was on a table set up for a seance`） | md 未安施事；第 1 块「安排这一切的人并不在场」是解读外推，已列提示 A9 | 通过（带 1 条提示） |
| 布置给谁看 | 本章不交代 | md 明写不交代 | 通过 |
| 为什么现在才被翻出来 | 本章不交代（本章只写「更怪了」与「罗比带马特下去了」） | md 第 2 块给的解释（「发现与处理是两拨人」）**推不出**，已列提示 A10 | 提示 |
| 「表演」有没有原文支持 | **零命中**（取证见 §四）——原文只有 `set up for a seance`（为降神会布置的桌子），没有 perform/stage/audience 一类词 | md 一律以「叙事手法／读者视角／对位」框定，未断言「原文写了这是一场表演」 | 通过（措辞建议保留框定） |

**跨章背景（供修复方参考，不计入 ch38 缺陷）**：这只手与那张桌子是**维多利亚时代的旧物**，不是近期布置的一场戏——ch37 末尾法医开封地下室当场发现（`text/ch37_37.txt`：`'There's a crystal ball,' their voice carried back up from the depths. 'And tarot cards on the table too. And – is that a hand?'`；同章：`the basement which has been sealed up for decades`），ch39 补充（`text/ch39_39.txt`：`'There were candlesticks on a big round table and all sorts of weird markings everywhere. It was eerie. It was sealed like a creepy time capsule.'`；`'There's a hand laid out in the middle of a table set up for what appears to have been a seance.'`）。⇒ **「为什么现在才被翻出来」的答案是 ch37 的**：Robbie Eastley 接手后重开封印的地下室；**「近期有人把物证布置成一场表演给谁看」这一读法在后续章并不成立**。建议 md 的「表演／等人来坐」措辞在章内保持开放，勿暗示「近期」；这不影响本章任何一行的「与原文不符」判定（本章原文确实什么都没说）。

---

## 七、覆盖声明

- **人判覆盖**：ch38 全文（9 块引语逐块 R4 + 导航 5 字段 + 一句话总结 + 词汇表 27 条例句）；另为回答本章专属判据，**只读** `text/ch37_37.txt` 与 `text/ch39_39.txt`（原文，非 md），以及 `text/ch28_28.txt`、`text/ch33_33.txt`、`text/ch15_15.txt` 的定向片段（用于取证「儿子」「疟疾年日记」「judgy」三处断言）。
- **机器层覆盖**：ch38（`chapter.sh --json` exit 0 / `check_vocab.py` exit 0 / `bookform.py` 形态行）。
- **未查（只有机器层／未核）**：本书其余 53 章 md、三篇总览（`00_概述.md` / `00_金句精选.md` / `00_情感节点.md`）**本轮未做 R4 人判**；`00_金句精选.md` 若收录了 ch38 的引语，其**逐字与出处**本轮未核（按规则记「未核」，不写「通过」）。
- **本轮不做**：修复（未改任何书目录 md）、git 操作（未 add / 未 commit / 未 push）。

---

## 八、给修复方的最小改动清单

1. **阻断 A1**：一句话总结中的「**儿子**和未出世的孩子」→ 改为「**妻子**和未出世的孩子」（或「他和未出世的孩子」），删掉「儿子」。
2. **阻断 A2**：导航「一句话概括」中的「**他自己**…把另一个“等人来坐”的房间布置了起来」→ 把施事还给马库斯（如「父亲却把乡间老宅收拾成另一个“等人来坐”的地方」），或改为凯厄斯在**心里**把空房间定成婴儿房；改后须与第 8 块口径一致。
3. 提示 A3–A14 按 3-diff.md 逐条处置（措辞类可只改字句，不动引语与结构）。
4. 提示 A10：若要保留「为什么现在才被翻出来」，建议改为指向「地下室封印多年、这次才被打开」这一层（本章可写「封印」不可写「谁发现的」）。
5. **改完必跑** `bash scripts/chapter.sh "<书目录>/ch38 a skeletal hand is found in the institute basement" --json`（应仍为 exit 0），并回原文核 A1／A2 两处的逐字。
