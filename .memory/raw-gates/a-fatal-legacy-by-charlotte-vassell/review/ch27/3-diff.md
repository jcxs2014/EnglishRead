# 3-diff.md · 第 27 章《A Fatal Legacy》三张单子

审：独立审查员（只负责 ch27）
原文唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch27_27.txt`（17,033 字符，54 行非空段）
md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch27 callie has dinner with eulalia.md`（17,979 字节，10 个引语块）
字符区间为 Python 字符索引（0 起，`text/ch27_27.txt` 全文）；行号为 `text/ch27_27.txt` 行号。

**计数**：本单共列 **9 条阻断型**（漏 2：L1、L2；编/错/说话人/数字 7：C1、C2、C3、C4、C5、C6、X1），分布在 md 的 **11 处**（C1 与 C4 各含 2 处）；**提示 8 条**（L3、L4、L5、C7、C8、C9、X2、X3）。逐条判定与档位见 `4-verdict.md`。

**本章专属判据的三项硬证据（先立，后判）**

| 判据 | 原文逐字 | 区间 |
|---|---|---|
| 餐桌旁几个人 | `‘Table for two, please.’` → `A waiter seated them to the side near the bar.` | char 4516–4540 / 4543–4588（line 71 / 74） |
| 倒酒是谁做的 | `Callie poured them each a glass of water from the tiny jug on the table.` | char 8028–8068（line 140） |
| Mel 是否在场 | 全章 8 处 “Mel” 全部出现在**对话里**（Eulalia 或 Callie 转述），无一处是 Mel 本人的动作 | 行 137,143,158,161,164,176,179,227（`/usr/bin/grep -n "Mel" text/ch27_27.txt` → 8 行，退出码 0） |

---

## 一、漏（素读有、md 无）

### L1 ·【阻断】Julian of Norwich／中世纪情绪板这条主线在 md 中完全缺席（含结尾的收束）

md 的导航「线索结构」自陈三层：表层餐桌寒暄 / 中层 Mel / 里层 Eulalia 对「被打断」的敏感 —— **没有中世纪—修女这条线**；正文 10 个引语块也没有一个引它。这条线不是闲笔：它在本章出现三次，是全书主线的伏笔与回收。

原文三处逐字：

- （a）char 1415–1790（line 56）`‘I’m getting there with the mood boards. It’s all very thirteenth century. … I read this article about this poet called Marie de France. … There’s a theory she was an abbess. … When I was thirteen I seriously considered becoming a nun. It only lasted a week …’`
- （b）char 2282–2313（line 62）`It was about Julian of Norwich. Eulalia had mentioned her by name so she thought she should gain a basic grasp of her life …`
- （c）char 15808–16016（line 284–287）`‘I was listening to a thing about Julian of Norwich today. …’ / ‘Julian! I love Julian! Did you know that there was a mystic nun who was burnt at the stake not too far from here?’`

跨章证据（这条线是全书主干，不是本章闲笔）：`text/ch12_12.txt:134`（Eulalia 本人就是 Julian 的粉丝：`I’m a fan of Julian of Norwich … Batshit-crazy nuns.`）；`text/ch36_36.txt:221`（Callie 的提案板原文点名 `Marie de France … Isolde … Julian of Norwich: ‘All shall be well …’`）——**ch12 → ch27 → ch36 是同一条线，md 在 ch27 处把它整段剪掉了，且未写任何取舍理由**。

md 侧：本文件全文检索 “Julian / Norwich / 修女 / 情绪板 / mood board / Marie” —— 0 命中。

取证命令：

```
/usr/bin/grep -c "Julian" "notes/…/ch27 callie has dinner with eulalia.md"   → 0（退出码 1）
/usr/bin/grep -c "Norwich" 同上                                              → 0
/usr/bin/grep -c "Marie de France" 同上                                       → 0
/usr/bin/grep -c "修女" 同上                                                  → 0
/usr/bin/grep -c "nun" 同上                                                   → 0
/usr/bin/grep -rn "Julian" notes/…/text/ | wc -l                             → 5（ch12:134、ch27:62、ch27:284、ch27:287、ch36:221）
```

### L2 ·【阻断】饭桌上真正的「主戏」之一：Callie 对甲方关系的关键判断（她预期被晾着）被漏掉

原文 char 3248–3569（line 62）：

> `Eulalia was already waiting for her outside. Callie wasn’t expecting that. She’d expected to be kept waiting, to be told that she was the lowly freelancer whose time wasn’t important. Callie wasn’t one for such power play and it seemed Eulalia wasn’t either. That was probably why her sister dealt with the business side.`

md 侧：「Callie 期望被晾着／她是低阶外包／Eulalia 的姐姐管生意」——md 中 0 命中（`/usr/bin/grep -c "kept waiting" "notes/…/ch27 callie has dinner with eulalia.md"` → 0，退出码 1）。这条判断正是 md 导航「人物弧线：Callie 从以为这是一次普通的甲方饭局，到看出自己正处在一个三人权力结构里」的前提；前提没进 md，后半句悬空。

### L3 ·【提示】「Callie 脑中闪过 Eulalia 会走到迎面来的车前」的幻象被漏掉

原文 char 12828–12904（line 209）：`… she was gripped by a vision of Eulalia stepping in front of an oncoming car.`

md 侧 0 命中。md 的原句 10「为什么这样写」只提到「对方掏出现金付账、不等找零就走了」，把同一段里更刺眼的一笔丢了（同时紧接的 `Eulalia was standing on the pavement, emptily staring at the traffic` 也是铺垫）。

### L4 ·【提示】孕吐（nausea）只进了导航，正文块未收

原文 char 2530 段内 `… between frenzied mood board sessions – when the nausea allowed.`（line 62）与 char 16120–16144（line 296）`Callie nodded; the nausea was returning.`。md 仅在导航写「可能怀孕的帽匠 Callie」，正文无。

### L5 ·【提示】两人桌这一决定性证据没有被引语或中文引用（只被「倒了两杯不是三杯」间接代偿）

原文 char 4516–4540（line 71）`‘Table for two, please.’`。md 全篇没有出现这句原文，也没有在中文里转述「订的是两人桌」；只有原句 7 的读者视角提示说「注意她倒了两杯，不是三杯——Mel 在这顿饭里连一只杯子都没有」。**结论对，但缺原文锚点**；本章专属判据要求的正是这句证据。

---

## 二、编（md 有、原文无 / 与原文不符）

### C1 ·【阻断】把「酒」的决定权交给 Mel —— 施事／归属反转，且 md 自相矛盾

md 两处：

- 导航「人物弧线」：`Mel 全程不出场，却决定了这顿饭能喝什么、能听什么、能长什么样。`
- 原句 6「读者视角提示」：`把 Mel 记下来：本章她一次都没出现，却决定了酒、专辑、头套和面包。`

原文：

- 酒（char 6458–6497，line 119）：`Eulalia tried to order a carafe of wine but Callie said her dermatologist had told her to stop drinking for the sake of her complexion, so Eulalia had had to settle for a solo glass of Valpolicella while Callie daintily refrained and ordered a Limonata.` —— **挡酒的是 Callie，不是 Mel**；Mel 在这一段连一个字都没出现。
- Mel 真正握着开关的三件事，原文逐字：专辑 `‘I don’t think Mel would like that.’`（char 7977–8010, line 137）；头套 `‘Mel is now saying that the label’s plan is for me to perform in them when live but when I’m doing photoshoots and interviews it’ll be my face.’`（char 9358–9437, line 161）；面包 `‘Mel says I can’t eat bread. I’ve got to bring the receipt back with me.’`（char 10426–10454, line 176）。

md 自相矛盾：同一篇 md 的导航「一句话概括」写的是 `Mel 手里握着专辑、头套和面包三种开关`（**三项，无酒**），原句 5 的分析也正确地把挡酒归给 Callie（`Callie 用一个半真半假的健康理由替她挡掉`）。⇒ 「酒」是孤例错项。

### C2 ·【阻断】「里面是玻璃做的一样脆」那句的说话人写成 Callie，实为 Eulalia

md 导航「叙事手法」：`作者用 Callie 的挑剔视角与吐槽给每个场景降温；她不写推理，只写认物——一杯水、一篮面包、一次挥手中指；而她对男人的那句评价（里面是玻璃做的一样脆），和她自己刚刚起步的那段关系形成反讽。`

「她」全链指向 Callie（「作者用 Callie 的视角…她不写推理」；末句「她自己刚刚起步的那段关系」= Callie 与 Caius 这段刚开始的关系）。

原文 char 6173–6394（line 110–116）：

> `‘No, Mr Polo. They’re easy to break. All bravado but their insides are fragile. Like they’re made of glass.’`
> `‘I don’t doubt that you’ve broken a few hearts in your time.’ Callie picked up the menu.`
> `‘A few skulls too.’`

⇒ 「made of glass」是 **Eulalia** 对 Callie 说的（回敬 Callie 说她男友是「paramour」的讥讽，针对「Mr Polo」这类男人）；Callie 的相邻台词只有 `I don’t doubt that you’ve broken a few hearts in your time.`。说话人反了。

### C3 ·【阻断】一句话总结把 Mel 写成「在旁边」——与原文（Mel 全程不在场）不符且自相矛盾

md 一句话总结：`那位从未露面的 Mel 在旁边握着专辑、头套和面包的开关`

同一句前半句说「从未露面」，后半句说「在旁边」，自相矛盾；且字面把 Mel 放到餐桌旁——原文是两人桌（`‘Table for two, please.’`，char 4516–4540；`A waiter seated them to the side near the bar.`，char 4543–4588），Mel 无任何在场描写（见上表 8 处 grep）。

### C4 ·【阻断】断言 Callie「编」了皮肤科医生的理由——原文无据

md 两处：

- 原句 2「为什么这样写」：`… 还临时编了一套皮肤病学的理由把酒挡掉。`
- 原句 5「为什么这样写」：`Callie 用一个半真半假的健康理由替她挡掉`

原文 char 6458–6497（line 119）只写 Callie **说了**这句话：`Callie said her dermatologist had told her to stop drinking for the sake of her complexion`，**没有说这是编的，也没有说半真半假**。

取证（按 R5-补「零命中必须自证」三件套）：

```
/usr/bin/grep -rn "dermatolog" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/
→ 仅 1 处命中：text/ch27_27.txt:119（就是 Callie 说这句本身）
退出码 0
```

⇒ 全书 54 章没有任何旁证支持「编造／半真半假」；md 断言的是原文没写的人物动机（把一条未定性的健康理由写成了刻意欺骗）。

### C5 ·【阻断】原句 7「桌上剩下的液体只有 Callie 亲手倒的水」——与原文不符

md 原句 7「为什么这样写」：`酒被挡掉之后，桌上剩下的液体只有 Callie 亲手倒的水`

原文（line 119 + line 140）：挡掉的只是 **carafe（整壶）**，桌上仍有 **一杯 Valpolicella**（Eulalia 的）和 **一杯 Limonata**（Callie 的），随后还有 **两杯 limoncello**（char 11369–11412, line 197）。⇒ 「剩下的液体只有水」与原文不符；md 自己的原句 5 还写着「桌上只剩一杯酒」，前后打架。

### C6 ·【阻断】原句 8 把 Callie 的口头反问说成「沉默」

md 原句 8「为什么这样写」：`作者用她接下来说的那句「我本来以为」后面的沉默，表明她的工作正被另一个人的意志推着走。`

原文 char 9210–9330（line 158）：`‘I thought that was the plan?’ Callie was confused. Eulalia had said as much on their first meeting and Mel’s very clear brief had left them out.` —— **是出声的反问 + 叙述层的 confused，全段没有「沉默」**。作者用来表现 Callie 被推着走的装置是「Callie was confused」与随后的 `She’d have to pull something out of nowhere`，不是沉默。

### C7 ·【提示】导航「视角」里的「她数着对方说话的停顿」——原文无此细节

md 导航「视角」：`… 后半段是她在餐厅里的观察与判断，她数着对方说话的停顿，猜 Mel 的意图 …`

原文 char 3323–16698 全段（line 62–320）：没有任何 Callie「数停顿」的描写；Callie 对 Mel 意图的猜测在 char 7013–7070（line 125，`Callie assumed that Eulalia didn’t like her new producer.`）与 char 9210 附近，属「猜测」成立，「数停顿」属添加的细节。

### C8 ·【提示】原句 2 中文理解把「试图自杀」译成「自我了断」

md 原句 2 中文理解：`… 对方用隐喻、身体和情感三种方式唱着自我了断 …`

原文 char 2530–2620（line 62）：`She sang about trying to kill herself metaphorically, physically and emotionally.` ——「trying to」是「试图」，「自我了断」读起来是已完成的自我了结。属译法偏重，不改结论。

### C9 ·【提示】原句 9 把 Callie 的推测说成「作者点破」

md 原句 9「读者视角提示」：`注意她为什么会为这样一件小事动怒：作者在本章里点破，这一次代表的是此前所有那些打断，不是这一件。`

原文 char 13500 附近（line 218）：`She didn’t think Eulalia’s behaviour was really about the limoncello or the pass the guy made, but more that his interruption represented all the ones that had come before it.` —— 主体是 `She didn’t think`，即 **Callie 的推测**，不是叙述者/作者的断语。

---

## 三、错（两边都有但不一致）

### X1 ·【阻断】原句 3「三次提问」与原文问号数不符

md 原句 3「为什么这样写」：`一句话里塞进三种餐厅、三次提问和两个比喻`

原文 char 3629–3955（line 68）整句：`‘Cal. How are you? Do you fancy Italian? Or Korean barbecue, maybe? There’s a sushi place across the road that might be better? What do you think? Are you a sushi person? You look like a sushi person but then you also look like a Botticelli painting. You’re sort of pearly, aren’t you? Did you pop out of a clam fully formed?’`

- 「三种餐厅」✓：Italian / Korean barbecue / sushi。
- 「三次提问」✗：该句共 **8 个问号**（`How are you?` / `Do you fancy Italian?` / `maybe?` / `better?` / `What do you think?` / `Are you a sushi person?` / `aren’t you?` / `Did you pop out of a clam fully formed?`）—— 脚本复核 `s[3629:3955].count('?')` = **8**。
- 「两个比喻」可辩：Botticelli painting、pearly 两个明喻成立，clam 那句可算俏皮话。

⇒ 数字与原文不符（R3「错」的「数字」档）。修法：「三次提问」改为「一串提问」即可。


### X2 ·【提示】原句 1 与原句 9 的中文理解含引语之外的上下文（引语选短）

- 原句 1 中文理解首句 `Caius 打电话来预告自己要晚归` —— 出自引语**前一句**（char 106–134, line 23：`‘I’m going to be back late,’ Caius said over video.`）。
- 原句 9 中文理解首句 `侍者送来两杯 limoncello，说是吧台那边那位男士请的` —— 出自引语**前一句**（char 11369–11412, line 197）。
- 原句 6 中文理解首句 `Callie 问能不能先听一听那张专辑` —— Callie 的问句在引语之前（char 7496–7600, line 134：`‘Would it be possible to hear the album? It might help me with my process.’`）。

三处都是「引语选短」型（S2 失误①）：分析覆盖的原文比引语长，但主体内容都在引语内，判提示。

### X3 ·【提示】原句 2 漏掉同一段的前半（Julian 播客）

原句 2 的引语从 `Now that she’d met Eulalia she couldn’t bear to listen to her music.` 起（char 2530），而同一自然段的**前半**（`It was about Julian of Norwich…`，char 2282 起）未被引也未被述。属 S2 截短，与 L1 同源。

---

## 四、机器层与本单的关系

`bash scripts/chapter.sh "…/ch27 callie has dinner with eulalia" --json` → **退出码 0**，`verdict: ok`，10/10 引语逐字命中、10 块结构与子项齐全、CJK 密度全部达标、形态全部合规。

⇒ 上列 9 处阻断型缺陷（漏 2：L1、L2；编/错/说话人/数字 7：C1、C2、C3、C4、C5、C6、X1）与全部提示项，**没有一条能被机器层抓出**：它们分别属于「覆盖」「施事归属」「说话人」「人物动机断言」「数字计数」五类，机器只验「引语逐字 + 中文是中文 + 关键词 + 形态」。这与 `docs/rules/审查表.md` §0.5「不许用机器全绿推出缺陷都在摘要层」一致。
