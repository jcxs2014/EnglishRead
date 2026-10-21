# R3 对账 + R4 逐块对应 · 第 13 章

- 书：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/`
- 唯一真值：`text/ch13_chapter_13.txt`（23,547 字符 / 4,154 词 / 210 行 / 70 段；Alba 视角；平安夜 Splau 商场二楼）
- 受审稿：`ch13 chapter 13.md`（132 行，7 个引语块）——下文写作 **md:行号**
- 规则：`docs/rules/审查表.md` §R3/R4；`docs/rules/生产-审查对照.md` S1–S5 + ⑥施事/归属反转 + 章型加权（cliffhanger → 重 S2 归属）
- 本轮只出指令，不改稿。
- 机器层：`bash scripts/chapter.sh "…/ch13 chapter 13.md" --json` → **退出码 0**（`2-machine.json`，verdict "ok"；7/7 引语逐字命中、segment_miss=0、struct_bad=0、keyword_bad=0、cjk_low=0、issues 空）。

---

## 专题 A · 原句 1 结尾 "her" 指谁（独立取证；本章最重的归属问题）

**原文逐字（text/ch13_chapter_13.txt:6，字符区间 [498,598)）**

> She did it without using her hands; instead, she stepped on each heel with the toes of her other foot, **the way her kids took their shoes off** when they got home, **knowing full well how much it bothered her**.

**判定：her = Alba 自己（她＝那三个孩子的妈妈），不是 Alba 的母亲。** 起草稿 md:21「她明知道这个脱法最招母亲的气」＝**施事/归属反转**（S3 第 ⑥ 类）。

**证据链（四条，全部回原文整句，不靠命中行）**

1. **同段的 her 已指 Alba**：「were hurting her」（指她自己的鞋硌脚）——同句里 "her" 已在指 Alba；若末句的 "her" 改指母亲，等于在同一句里无标记地换指代。
2. **"her kids" 的所指在本章唯一**：本章 ch13:12「Those robes had become her winter uniform—her children’s, too」与 ch13:201「as she did with her kids when the public restrooms went dark」两处 "her kids" 均指 Alba 的三个孩子；本章里另一个女性指代只有 "the girl"（ch13:6、ch13:18），她没有孩子。因此「the way **her kids** took their shoes off」的 her 只能是 Alba。
3. **反身规则**：分词 "knowing full well…" 的局部主语是 "her kids"（孩子们），不是主句的 she；挂在主句 she（Alba）身上才该写 "bothered herself"。原文写 "her"，正说明它是第三人的"她"＝Alba 作为"妈妈"这个角色。
4. **语义**：孩子们用踩鞋跟的方式脱鞋，动机就是气妈妈；"knowing full well how much it bothered her" ＝孩子们明知这最招**他们妈妈**生气。Alba 此刻正照着孩子们当年的方式做——所以末句的 "her" 指 Alba 自己（"招她生气"＝招 Alba 生气），与"她学孩子"的动作构成同一件事的两面。

**反向读法（her = 母亲/Carmen）需要凭空引入**：它要求 "her kids" 改指 Alba 母亲的孩子（＝Alba 自己和兄弟姐妹），与本章 "her kids" 的既有指向冲突，且本章从未出现 Carmen 与其孩子的关系陈述 ⇒ 不能成立。

**md 侧还错了一层**：md:21「**她**明知道这个脱法最招**母亲**的气」——把「知道」的主语从"孩子们"移到了 Alba，把「被气的人」从 Alba 移到了 Alba 的母亲。两处都反了。

**修法建议（不唯一）**：改后中文＝「她不用手，而是用另一只脚的脚趾去踩自己的鞋跟，就像她的孩子们回家脱鞋那样——孩子们明知道这最招妈妈的她生气。」；或「……正是孩子们当年用来气她的那招。」

---

## R3 · 单子 A：漏（素读有、md 无）

### L1【阻断】章末的尖叫与剪影整段缺席，且情感弧线与原文末句冲突
- **md 侧**：md:11 一句话概括止于「给自己买了一双芭蕾平底鞋」；md:12 情感弧线「最后是主动抱住对方、却抱到对方在怀里消失；……**恐惧因此在章末转成落空**」；md:132 一句话总结同样止于芭蕾平底鞋。全 md 无结尾的尖叫、无剪影、无「谁在那儿」。
- **text 侧**（text/ch13_chapter_13.txt:207、:210）：
  > 207: She heard a scream that seemed suspended in time.
  > 210: She left Claire's and looked in both directions. The scream was coming from her right. She walked toward it. The screaming stopped, but she saw silhouettes. Who were they? What was stirring there?
- **为什么阻断**：本章型是 cliffhanger/恐怖高潮，章末钩子就是本章的收束点；md 把结尾写成「转成落空」，与原文最后一句（「Who were they? What was stirring there?」）**直接冲突**（原文不是落空，是新的悬念）。md 内 "scream|尖叫" 仅命中 md:85「恐怖在这里没有尖叫」（讲原句 7 的断裂）与 md:101 词汇例句，**均与结尾这声尖叫无关**。
- **修法建议**：在导航「情感弧线位置」末尾与一句话总结末尾补一拍——尖叫从右边来、走近后停住、只剩剪影与「谁在那儿／那边在搅动什么」；并把「恐惧因此在章末转成落空」改成「恐惧没有落空，而是被换成一声悬在时间里的尖叫」。引语可从 ch13:207 起补一个句级块（13 词，§3 下限 30 词 ⇒ 需与 ch13:210 连成 2 句共约 40 词）。

### L2【提示】拍掌让圣诞灯重新亮起、沿血迹与脚印下楼，未覆盖
- **md 侧**：全 md 无「拍掌/掌声/灯亮/重新亮/clap」（grep exit=1），无「血迹/脚印/血径」（grep exit=1）。
- **text 侧**（text/ch13_chapter_13.txt:201、:204）：
  > 201: She lifted her arms and clapped at the sky, as she did with her kids when the public restrooms went dark, and the Christmas lights came back on. … When she looked around, she was alone.
  > 204: … a trail of blood where the woman and the children had once walked … blurred at points by tiny footprints …
- **为什么是提示不是阻断**：这两处是氛围/收束细节，不是本章的关键转折（关键转折＝结尾尖叫，见 L1）；且「抱到女人裂成两半、灯灭」已在 md 中。
- **修法建议**：在原句 7 的「读者视角提示」或一句话总结里补一句「她朝天拍掌，圣诞灯重新亮起，她一个人站着，脚下的血迹旁多出细小的脚印」。

### L3【提示】巨型婴儿的体重与「像成人一样走路」、队伍人数，未覆盖
- **md 侧**：全 md 无「磅/pound/thirteen/十四/体重」（grep exit=1）；巨型婴儿只写了脸与眼睛（md:51），未写体重与走路；队伍人数无。
- **text 侧**（text/ch13_chapter_13.txt:18、:27）：
  > 18: … a creature like the others … **those thirteen- or fourteen-pound babies who end up in the Guinness World Records books, except it was walking like an adult** …
  > 27: … **about fifteen of them**.
- **为什么是提示不是阻断**：md 没有写出与原文冲突的数字（是"没写"，不是"写错"）；但本章最恐怖的形体（13–14 磅、像成人一样走路）只交付了脸，属于覆盖不全。
- **修法建议**：把原句 4 的引语向前扩到 "a creature like the others" 那句（注意 §3 每块 ≤70 词 ⇒ 需另起一块），或在原句 4 的「中文理解」里补一句「她像那些十三四磅、进了吉尼斯世界纪录书的巨婴一样走路——像个成年人」；队伍人数可并入导航的「一队沾血的婴儿」。

---

## R3 · 单子 B：编（md 有、原文无）

### C1【阻断】「买打折时节的婚纱」——原文里没有"打折"这层
- **md 侧**（md:65，原句 5 为什么这样写）：「作者把婚礼这件最私人的东西降级成道具，还先给两件日常衣服（连锁快时尚的睡袍、**买打折时节的婚纱**）……」
- **text 侧**（text/ch13_chapter_13.txt:63）：
  > The woman's dress was her dress from **Rosa Clará**. Her white crepe dress—now stiff and stained—with its sweetheart neckline, covered in sequins that looked like the scales on a mermaid's tail.
- **为什么阻断**：原文给的婚纱是自家那件 Rosa Clará 白色绉纱婚纱（带鱼鳞亮片），没有任何"打折时买"的性质；「打折婚纱」是凭空来的情节属性。且同一句里「两件日常衣服」与前半句「把婚礼这件最私人的东西降级成道具」**自相矛盾**（婚礼服装不能既是"最私人的"又被降级成"日常衣服"）。
- **取证**：`/usr/bin/grep -n -o -E ".{0,40}Rosa Clar.{0,60}" text/ch13_chapter_13.txt` → `63: The woman’s dress was her dress from Rosa Clará. Her white crepe dress—now stiff and stained—with its`；exit=0。
- **修法建议**：改为「还先给两件日常/旧衣服（连锁快时尚的睡袍、她自己那件 Rosa Clará 白色绉纱婚纱）」，并把「两件日常衣服」改成「两件被降级的旧衣」之类与前半句不冲突的说法。

### C2【阻断】「给自己买了一双芭蕾平底鞋」——原文没有购买动作
- **md 侧**：md:11「Alba 独自留在空商场，**给自己买了一双芭蕾平底鞋**」；md:132「……**买了一双芭蕾平底鞋**。」
- **text 侧**（text/ch13_chapter_13.txt:204）：
  > … She passed Claire's and went in. … she **found the ballet flats** … she chose **the most understated pair—even they were encrusted with silver studs** … She sat on the floor and put them on.
  > （动作链＝找到→挑→坐下穿上，**没有买**；鞋型"芭蕾平底鞋"✔，细节"最不张扬的一双、连鞋面都镶着银色铆钉"在 md 里缺失）
- **为什么阻断**：md 把"挑+穿上"写成了"买"，凭空造出一个购物动作（与本章"商场无人、店铺关门"的场景也冲突）。全书侧同样查无：ch13 与 ch14 均无 bought/pay/purchase/cash/register/receipt。
- **取证**：`/usr/bin/grep -n -iE "bought|pay|purchase|cash|register|receipt" text/ch13_chapter_13.txt text/ch14_chapter_14.txt` → 无输出；exit=1。（ch14 开篇仍是"穿着走"：`her ballet flats twinkled`，`Alba pulled the box from a coat pocket`。）
- **修法建议**：md:11 与 md:132 改为「给自己挑了一双芭蕾平底鞋」「……最后坐在地上试穿那双最不张扬、镶着银色铆钉的芭蕾平底鞋」；鞋的细节（银铆钉）建议补进原句 7 之后的总结句。

### C3【阻断】「在一座熄了灯、没有人影的商场里」——原文相反
- **md 侧**（md:65，原句 5 为什么这样写）：「……**在一座熄了灯、没有人影的商场里**，她除了衣服没有别的线索。」
- **text 侧**：
  > text/ch13_chapter_13.txt:204：The **Christmas lights were on, as were the lights in the stores she usually went to**. The stores she had never or rarely set foot in were closed and dark.
  > text/ch13_chapter_13.txt:9：It was nighttime but there was no roof, so the light from the street was filtering in.
- **为什么阻断**："没人影"✔，"熄了灯"✘——商场亮着圣诞灯和常去店铺的灯（而且灯光是本章的机制：ch13:201 拍掌把灯拍回来）。场景状态与原文冲突，且这句出现在原句 5 的论证里（用"黑暗"来解释她只能靠衣服认人），论证前提本身就错。
- **取证**：`/usr/bin/grep -n -o -E "The Christmas lights were on, as were the lights in the stores she usually went to" text/ch13_chapter_13.txt` → `204:…`；exit=0。
- **修法建议**：改为「在一座亮着圣诞灯、却空无一人的商场里」。

---

## R3 · 单子 C：错（两边都有但不一致）

### W1【阻断】原句 1：末句 "her" 的归属被反转（详见「专题 A」）
- **md 侧**（md:21）：「就像孩子们回家脱鞋那样——**她明知道这个脱法最招母亲的气**。」
- **text 侧**（text/ch13_chapter_13.txt:6，区间 [498,598)）：「… the way her kids took their shoes off when they got home, knowing full well how much it bothered her.」
- **为什么阻断**：主语（谁在"知道"）与受事（谁被气）两处都与原文相反；这是 S3 第 ⑥ 类施事/归属反转，四道机器探针（引语逐字/中文/关键词/形态）全绿，只有 R4 第三问能抓。
- **修法建议**：见专题 A。

### W2【阻断】原句 4：「队伍里别的婴儿**都是**秃的」——原文是"有些"
- **md 侧**（md:51）：「**队伍里别的婴儿都是秃的**，只有它不是。」
- **text 侧**（text/ch13_chapter_13.txt:18）：
  > **Some** of the babies in the line were bald, but not this one.
- **为什么阻断**：数量词被绝对化（Some→都）；且与本块 md:55「再把秃头这个常规从它身上排除」**自相矛盾**（"常规"要成立也得是"多数秃头"）。md:55 的「把不寻常集中到它一个」同样预设了"其余全秃"。
- **取证**：`/usr/bin/grep -n -o -E "Some of the babies in the line were bald, but not this one" text/ch13_chapter_13.txt` → `18:…`；exit=0。
- **修法建议**：md:51 改为「队伍里有些婴儿是秃的，只有它不是」；md:55 相应改为「再把秃头这个常规从它身上排除」时不再暗示其余全秃。

### W3【阻断】导航「叙事手法」：交付顺序反了
- **md 侧**（md:15）：「视觉总是迟到半步：**先看见一条长得没边的拖尾，再看见托着它的四只沾血小手，最后才看清那是个披着睡袍的女人**」
- **text 侧**：
  > text/ch13_chapter_13.txt:12：She **saw a woman**, her back to her, emerge from under the bridge. … a very long train sticking out from under her robe … It looked like an evening gown.
  > text/ch13_chapter_13.txt:15：It went on and on and on, then she saw the fabric lift timidly and caught sight of the hands that were holding it. Four tiny hands…
- **为什么阻断**：原文里"披着睡袍的女人"是**第一个**被看见的（ch13:12，同段才见拖尾），"四只沾血的小手"是**第二个**（ch13:15）。md 把顺序写成拖尾→小手→女人，与原文的时序相反。
- **修法建议**：改为「先看见一个背对她的披袍女人和一条长得没边的拖尾，再看见托着拖尾的四只沾血小手，最后才看清那队伍是什么」。

### W4【提示】原句 5：「一直挡着主角的视线」vs 原文「distracted her」
- **md 侧**（md:61）：「那条拖尾先前被对方像缠绷带一样绕在一条手臂上，**一直挡着主角的视线**，直到此刻才看清」
- **text 侧**（text/ch13_chapter_13.txt:63）：「The long train, which the woman had coiled around one arm like a sinister bandage, **had distracted her** up till this moment.」
- **为什么是提示**：原文是"分心/看得出神"，md 改成"物理遮挡视线"；主结论（婚纱是 Alba 的）不受影响，属措辞层。
- **修法建议**：改为「一直让主角看得出神，直到此刻才看清」。

### W5【提示】原句 4 读者视角提示与本块引语、为什么这样写互相矛盾
- **md 侧**（md:57）：「这一段最狠的不是脸，是「几乎分不开」：**她看得出那里有东西在看**，只是看不出它是怎么看的。」
- **text 侧**（text/ch13_chapter_13.txt:18）：「And this one was swollen, with eyes that looked like a boxer's after a fight: two straight lines you could barely separate.」
- **为什么是提示**：引语与 md:55 都写"眼睛被肿得看不见"，md:57 反过来说"她看得出那里有东西在看"。属提示层自相矛盾（阅读提示层），不改会与同块其余两句打架。
- **修法建议**：改为「最狠的不是脸，是「几乎分不开」——那里明明有眼睛，却已经分不出眼睛是怎么看的」。

### W6【提示】原句 7 / 一句话总结：「触手」没点明是谁的
- **md 侧**（md:81）：「**那几根银亮的触手**也挤了进来；……勒紧**那个女人的腰**」；md:132「抱到对方**被触手挤成两半**」。
- **text 侧**：触手是 **Alba 自己腹中**的：text/ch13_chapter_13.txt:21「the tentacles strangled her from within」（her＝Alba）；:162「the tentacles shot upward **from her belly**」；:180「the tentacles hadn't gone back inside **her body**」；:204「the tentacles coiled back inside **of her**」。
- **为什么是提示不是阻断**：md 没有把触手安到别人身上（没写反），只是没写归属；但读者极易误以为触手属于那个女人，从而把"拥抱变成凶器"的机制读反。
- **修法建议**：md:81 改为「**Alba 自己腹中伸出的**那几根银亮触手」；md:132 改为「被**从自己肚子里伸出的**触手挤成两半」。

### W7【提示】原句 6：「橱窗镜」vs 原文 "shop mirrors"
- **md 侧**（md:71）：「……以及**在橱窗镜子里看看自己**的那个念头。」
- **text 侧**（text/ch13_chapter_13.txt:156）：「her desire to look at herself in **shop mirrors**」（商场里的试衣镜）。
- **为什么是提示**：镜子的类型被换成了橱窗镜（原文指商场店铺里的镜子）。
- **修法建议**：改为「在商场试衣镜里看看自己」。

---

## R4 · 逐块对应与固定三问

判据（审查表 R4）：不看子项标题，只回答「这段中文是不是在讲这句引语」；三问＝①每个动词的主语是谁 ②受事/宾语是谁 ③「谁的/谁欠谁/谁问的」回原文看 by/to/from/of 定方向。

| 块 | 引语落点 | 中文理解 | 关键词 | 为什么这样写 | 读者视角提示 | 三问（主语/受事/归属方向） | 对应结论 |
|---|---|---|---|---|---|---|---|
| 原句1 | text:6 [233,599) | ✔ 在引语内 | ✔ 3 个短语全在引语内 | ✘ 引用了**引语外**的两句（"楼下那只脏白球鞋和装手柄的盒子"＝[7,229)） | ✘ 同上 | ① 脱鞋动作主语＝Alba ✔；② 受事＝她自己的帆布鞋 ✔；③ "her kids"＝Alba 的三个孩子 ✔，末句 her 归属 ✘（W1） | **不通过（S2①截短）**；因引语已 69 词（§3 上限 70 词），扩引语会破硬线 ⇒ 档位取提示，修法是改写分析或另选自足引语 |
| 原句2 | text:12 [2140,2363) | ✔ | ✔ a metallic quality / an old tape player / rustling and footsteps 全在引语内 | ✔（"声音劈成两层"在引语内可查） | ✔ | ① 主语＝laughter / the sounds ✔；② 无宾语；③ 无归属 | 通过 |
| 原句3 | text:15 [4172,4358) | ✔ | ✔ the fabric lift timidly / Four tiny hands / Stained with blood 全在引语内 | ✔（长度→角度→尺寸→血，句内可查） | ✔（明确标注"回到上一段"，属读者引导，不判截短） | ① 主语＝she（Alba）看见；② 受事＝fabric / the hands ✔；③ 无归属 | 通过 |
| 原句4 | text:18 [7221,7487) | ✔（量词错 W2） | ✔ an old man's face / a clump of thick black hair / eyes that looked like a boxer's after a fight 全在引语内 | ✔（三句逐级排除，句内可查） | ✘ 与引语及本块冲突（W5） | ① 主语＝The child＝队尾那只巨型婴儿 ✔；② 受事＝its eyes ✔；③ "in the line" ✔ | 通过（提示级瑕疵另计） |
| 原句5 | text:63 [12438,12717) | ✔（"挡着视线" W4） | ✔ a Primark robe / beneath it was her wedding dress / coiled around one arm like a sinister bandage 全在引语内 | ✘ 含原文无的断言（C1「买打折时节的婚纱」）与冲突断言（C3「熄了灯」） | ✔ | ① 主语＝The woman＝Alba 的镜像 ✔；② 受事＝her wedding dress＝**Alba 自己的** ✔；③ 归属方向＝"Alba's wedding dress" ✔ 正确 | **不通过（C1/C3）** |
| 原句6 | text:156 [15505,15852) | ✔ | ✔ to confirm she was still around / covered in monstrous babies / to reclaim what was hers 全在引语内 | ✔（"三个还不够"是标明出处的上下文引用，ch13:93 附近，不判截短） | ✔ | ① 主语＝she（Alba）；② 受事＝her time/body/privacy/eyes/desire ✔；③ "most of all, Carmen" → md「尤其是母亲」✔（Carmen 确为 Alba 的母亲，见 ch13:147 "like your mom" 与 ch13:156） | 通过 |
| 原句7 | text:198 [20412,20602) | ✔ 动作链 join→squeeze×3→split 逐动作对上 | ✔ joined in the embrace / squeezed and squeezed / split in half 全在引语内 | ✔（引语内） | ✔（"紧接的下一句"标注清楚：snap/灯灭/消失＝text:198 后半） | ① 主语＝the silvery appendages＝**Alba 腹中的触手**（md 未点明，W6）；② 受事＝the woman's waist＝那个女人 ✔；③ 归属方向未写反 ✔ | 通过（提示级瑕疵另计） |
| 导航＋一句话总结 | text:6/12/63/198/204/207/210 | ✘ | — | ✘（顺序反 W3） | ✘（漏 L1） | ①"被挤成两半"的施事未指明（W6）；② 婚纱归属 ✔；③ 结尾尖叫未收录（L1） | **不通过（L1/C2/C3/W3）** |

### R4 形态核对（跨步骤·形态）
- H1＝`# 13. Chapter 13`：与本书 ch00–ch17 全部 `# NN. Chapter N` 同形 ✔（本书既有 17 章已生产的章一致）。
- 导航 5 项 ✔（与本书众数一致，机器 form 段 nav_count=5 / nav_count_ok=true）。
- 子项集＝中文理解 / 关键词 / 为什么这样写 / 读者视角提示 ✔（本书 ch00–ch13、ch16、ch17 各章同形；profile_optional=句子结构，本章未加，无理由但属可选）。
- 块数 7 ✔（本书中位 7，范围 5–8）。
- frontmatter：`状态: 未读` / `modified: "2026-10-21"` / `source_text: ch13` ✔ 与 ch12/ch16 逐字同形。
- **结论：形态通过（无阻断项）。**

### 词汇表（S4）核对
- 24 条例句逐条 `例句 in 原文` 全部 True 且**各命中 1 次**（脚本核对，0 漏）；例句均为本章原句 ✔。
- 分档：⭐⭐⭐ 8 条（gelatinous / otherworldly / convulsions / whimpering / procession / intolerable / instinctively / unbothered）＋⭐⭐ 8＋⭐ 8；未发现注水档位，⭐ 组为实义日常词（ponytail / wedding dress / affection / pain / baby / eyes / children / dark）——数量 24 条与本书其他章规模相称 ✔。
- **结论：词汇表通过（提示级）。**

---

## 附 · 零命中类断言的取证（R5-补，全部用 `/usr/bin/grep` 显式路径；`text/` 被 .gitignore，`git grep` 永远查无且退出码 1 与真查无不可区分）

```
$ /usr/bin/grep -n -iE "bought|pay|purchase|cash|register|receipt" \
    notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch13_chapter_13.txt \
    notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch14_chapter_14.txt
（无输出）                                             → exit=1   # ch13+ch14 全无购买动作
$ /usr/bin/grep -n -icE "earring" .../text/ch13_chapter_13.txt
0                                                     → exit=1   # 本章无"耳环"
$ /usr/bin/grep -n -E "磅|pound|thirteen|十四|体重" "…/ch13 chapter 13.md"
（无输出）                                             → exit=1   # md 未写体重
$ /usr/bin/grep -n -E "拍掌|掌声|灯亮|重新亮|clap" "…/ch13 chapter 13.md"
（无输出）                                             → exit=1   # md 未写拍掌/灯亮
$ /usr/bin/grep -n -E "血迹|脚印|血径" "…/ch13 chapter 13.md"
（无输出）                                             → exit=1   # md 未写血迹/脚印
$ /usr/bin/grep -n -E "scream|尖叫" "…/ch13 chapter 13.md"
85:…恐怖在这里没有尖叫…
101:| instinctively | … | The woman's adult screams got mixed up with the children's… |
                                                    → exit=0   # 仅 2 处命中，均与章末尖叫无关
$ /usr/bin/grep -n -E "买" "…/ch13 chapter 13.md"
11:…给自己买了一双芭蕾平底鞋。 / 65:…买打折时节的婚纱… / 132:…买了一双芭蕾平底鞋。
                                                    → exit=0
$ /usr/bin/grep -n -E "触手" "…/ch13 chapter 13.md"
81:…那几根银亮的触手也挤了进来… / 132:…被触手挤成两半… → exit=0   # 两处均未点明触手表属
$ /usr/bin/grep -n -o -E ".{0,40}Rosa Clar.{0,60}" .../text/ch13_chapter_13.txt
63: The woman's dress was her dress from Rosa Clará. Her white crepe dress—now stiff and stained—with its   → exit=0
$ /usr/bin/grep -n -o -E "The Christmas lights were on, as were the lights in the stores she usually went to" .../text/ch13_chapter_13.txt
204:…                                                                    → exit=0
$ /usr/bin/grep -n -o -E "Some of the babies in the line were bald, but not this one" .../text/ch13_chapter_13.txt
18:…                                                                     → exit=0
$ /usr/bin/grep -n -E "scream|screamed|screaming" .../text/ch1{4,5,6,7}_*.txt
ch16:18 …the same sound Alba had heard before, which had brought her here in the first place. / ch16:21 / ch16:24 / ch16:39 / ch16:42 / ch16:51 / ch16:54 / ch16:57   → exit=0   # 跨章旁证：ch13 结尾那声尖叫在 ch16 才有解释，本章不交代
```

> 阴性对照提醒：以上"查无"全部是 `/usr/bin/grep` 对显式文件路径的执行，退出码 0/1 已分别标注；未使用 `git grep` 或尊重 ignore 规则的 rg 系（`text/` 在 `.gitignore:132` 被排除，那类工具必然假零命中）。
