# 第 7 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md`（成品，140 行，7 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch07_chapter_7.txt`（原文，28 行 / 27 个非空行，3,300 字符，8 个正文自然段）
- 机器层：`bash scripts/chapter.sh "…/ch07 chapter 7.md" --json` → **退出码 0**，`verdict: ok`（详见 `2-machine.json`）
- 流程：R1 素读（`1-suread.json`，先读原文后开 md）→ R2 机器层 → R3 本单 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号
- 复核重跑：机器层复跑写临时文件 `/tmp/dshreview/m07.json`，**未覆盖** `2-machine.json`；复跑退出码 0、7 个引语字符位（139 / 418 / 742 / 1367 / 2466 / 2705 / 2999）与存档一致

---

## 一、漏（L）

### L1｜Brisa 醒来时说的那句「I’m thirsty」未进 md｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:24`）：

> "I’m thirsty."

**原文侧**（`text/ch07_chapter_7.txt:21`，紧邻上文）：

> "Brisa, are you OK? Did you hurt yourself?" Diana could tell that although her eyes were open, she was fast asleep. Unsettled, she helped her lie back in bed and covered her with the duvet. It was then that Brisa truly woke up.

**md 侧**：`ch07 chapter 7.md` 全文无对应内容。

取证命令：
```
/usr/bin/grep -c 'thirsty' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 0；退出码 1
```

**影响**：原文里这段是「女儿先像被关掉一样瘫软、被放回床上、真正醒来后第一句是要水」——醒来即索水，说明她这一夜身体状态正常，异状只出现在睡着之前的站立姿势那一段。md 把「她睡着了／睡着后的一切」写全了，唯独没有这个醒来后的收束动作，读者少一个「她回来了」的信号。

**修法**：`md:19` 之前的叙述缺一段；可在块 4（`md:55-63`）的中文理解里补一句「她把女儿放回床上盖好被子，女儿这才真正醒来，第一句话是要水」，并注明 `:21` 的 "It was then that Brisa truly woke up."。

### L2｜「Get in bed / Do you have to go to the bathroom?」这两句 Diana 的台词未进 md｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:9`）：

> "Honey, what’s going on? Get in bed." Brisa didn’t answer. "Do you have to go to the bathroom?"

**md 侧**：`ch07 chapter 7.md` 全文未出现这两句台词。

取证命令：
```
/usr/bin/grep -cE 'Get in bed|bathroom' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 0；退出码 1
```

**影响**：原文里 Diana 的第一反应是把它当普通起夜处理（「你怎么了，去睡吧」「你是不是要去洗手间」），Brisa 一声不吭，这个「普通解释失效」的两拍是塌陷前的铺垫。md 从「母亲伸手想把她转过来」直接进入瘫软，跳过了这一拍，于是母亲显得一上来就按超自然处理，弱化了原文那种「先按常识解释」的质地。

**修法**：块 3（`md:43-51`）中文理解补一句：母亲先按「孩子是不是要起夜」处理，问了两句都没得到回答。

### L3｜露营睡袋与「她已翻身趴下」这一动作未进 md｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:27`）：

> She took one of the kids' camp sleeping bags from the closet, stretched it out on the little mat, and reached up with one hand to hold Brisa's; her daughter had now rolled onto her stomach.

**md 侧**：`ch07 chapter 7.md` 全文未出现「睡袋」「露营」「趴下／翻身」。

取证命令：
```
/usr/bin/grep -cE 'camp sleeping|sleeping bag|rolled onto|stomach' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 0；退出码 1
```

**影响**：原文里母亲铺睡袋、握住女儿的手、女儿在这段时间里自己翻成了趴姿——正是这个姿势变化让第二次触摸摸到「不像背也不像胸的东西」。缺了铺垫，md 块 5 的触感异变就少一环因果；块 5（`md:67-75`）现在读起来像突然发生的。

**修法**：块 4 读者视角提示（`md:63`）已经写了「这些步骤在本章还会再来一次」，可在此处落实：块 5 的「为什么这样写」补上「她铺开睡袋、握住女儿的手，女儿自己翻成趴姿，这才有了第二次触摸」。

### L4｜叫不醒 Carlos 与「她认定女儿在梦游」这个说法未进 md 的正文分析｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:27`）：

> She tried to wake Carlos up to tell him what had happened, to say that now she was absolutely sure Brisa had been sleepwalking, but rousing that man was basically impossible.

**原文侧**（`text/ch07_chapter_7.txt:27`，下文）：

> She was still feeling worked up, and angry, if unfairly, that Carlos was out through the whole thing.

**md 侧**：`ch07 chapter 7.md` 里 "sleepwalking" 只出现在词汇表例句（`md:123`），正文分析未写；Carlos 全章只在 `md:123` 出现一次。

取证命令：
```
/usr/bin/grep -nE 'sleepwalking|Carlos' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ md:123 一处（词汇例句），md:123 一处 Carlos；退出码 0
```

**影响**：`md:13` 的「梦游这一老套解释被兑现又被抽走」把梦游当作叙述者的断言，但原文里「女儿是在梦游」是 **Diana 自己**下的判断（"now she was absolutely sure Brisa had been sleepwalking"），且她叫不醒丈夫、独自处理这一夜，也正因如此才只能去拿耳机。这一层没有写进正文，读者看不到「梦游」这个解释的来源和它的可疑之处。

**修法**：`md:13` 与块 4（`md:55-63`）各补一句：梦游是母亲自己下的结论（她叫不醒丈夫、整夜独自守着），而她连说出口的机会都没有。

---

## 二、编（fabricated）

**无。**

核对范围：`md:11-15`（导航 5 条）、`md:19-99`（7 个引语块的中文理解／为什么这样写／读者视角提示，共 21 段分析）、`md:103-136`（20 条词汇）、`md:140`（一句话总结）逐句回查 `text/ch07_chapter_7.txt` 全文 8 个正文自然段。未发现原文没有的情节、关系、数字或杜撰场景。

逐项说明：
- 导航 `md:11`「母亲一碰她整个人就软了下去」——`text:12`「Brisa collapsed」；「摸到的身体既不像背也不像胸」——`text:27`「it felt nothing like her back or even her chest」；「开灯却一切正常」——`text:27`「She was in an uncomfortable position, but not an unnatural one」；「戴着耳机守了她一整夜」——`text:27`「proceeded to lie awake all night right next to Brisa」。
- 导航 `md:14`「她先是数女儿有没有呼吸」——`text:27`「placed her hand on her daughter's back to make sure she was breathing normally」。
- 导航 `md:15`「先听见屋里有动静，再借手机手电看轮廓，最后靠手掌确认」——`text:6`「Diana heard something in Brisa's room…phone flashlight on」→ `text:27` 触摸。
- 块 1（`md:19`）的中文理解、块 3（`md:43`）、块 5（`md:67`）、块 6（`md:79`）、块 7（`md:91`）的事实性陈述均能在 `text:6/12/27/27/27` 找到出处。
- 词汇 20 条例句：自写脚本逐条核对，全部是原文逐字子串（`rows checked=20 not_verbatim=0`）。
- 原文本章**没有阿拉伯数字、没有任何日期字样**（`/usr/bin/grep -nE '[0-9]' text/ch07_chapter_7.txt` 只命中第 1 行的章号 `7`），md 未出现任何数字断言。

---

## 三、错（E）

### E1｜`md:11`「摸到的身体既不像背也不像胸」把触感顺序说反了｜档：阻断

**原文侧**（`text/ch07_chapter_7.txt:27`）：

> Her stomach then clenched as soon as she realized she didn't know quite what she was touching. It had the warmth of Brisa, but it felt nothing like her back or even her chest.

**md 侧**（`ch07 chapter 7.md:11`）：

> 深夜的儿童房里，Brisa 面朝窗户站着，母亲一碰她整个人就软了下去；摸到的身体既不像背也不像胸，开灯却一切正常，母亲就这样戴着耳机守了她一整夜。

**影响**：**「一碰就软」与「摸到的身体不像背也不像胸」在原文里是前后两件事，中间隔着一次真正的触摸失败**：第一次触碰（`text:12`）是把女儿转过来时她瘫软；第二次触摸（`text:27`）是母亲伸手安抚、摸到「不像背也不像胸」的形状。md 把两件事并成一句「一碰她整个人就软了下去；摸到的身体既不像背也不像胸」，读起来像同一场触碰里的两个现象。原文的恐怖恰恰在于：第一次触碰是「瘫软」（像被关掉），第二次触碰才摸到「形状不对」——两次触碰的结论不同，md 并成一次就抹掉了这一层递进，块 5（`md:67-75`）也就失去了「第二次触摸」的定位。

**修法**：拆成两句——「母亲伸手想把她转过来，女儿却一下子瘫了下去」与「后来第二次伸手安抚，摸到的身体既不像背也不像胸」。现成的中文表述见 `md:45`（块 3 中文理解：「母亲伸手想把她转过来，女儿却一下子瘫了下去」）与 `md:69`（块 5 中文理解：「她伸手去安抚女儿，手一碰，胃就抽紧了……那是女儿身上的温度，可既不像背，也不像胸」），把这两句并进 `md:11` 即可。

### E2｜`md:15`「全章几乎是一个长段落」与原文的段落结构不符｜档：提示

**原文侧**（`text/ch07_chapter_7.txt`，段落结构实测）：正文共 8 个自然段——`:6`（入房见女儿立于窗前）、`:9`（两句台词）、`:12`（转身时瘫软）、`:15`（跪地询问）、`:18`（站起但听不进话）、`:21`（放回床上盖被子、真正醒来）、`:24`（"I'm thirsty."）、`:27`（末段 1,896 字符：厨房取水、确认呼吸、叫不醒 Carlos、睡袋、第二次触摸、开灯、耳机守夜）。
**md 侧**（`ch07 chapter 7.md:15`）：

> 全章几乎是一个长段落，感官逐级失灵：先听见屋里有动静，再借手机手电看轮廓，最后靠手掌确认——看见的还能被灯光推翻，摸到的却推翻不了。

**影响**：「几乎是一个长段落」会被读成「全章由一个长段构成」，而原文的最后一段（`:27`）虽然长，前面还有 7 个短段（其中 4 段是纯对白或极短的动作段）。这句是关于行文节奏的判断，写成「全章几乎是一个长段落」与原文段落分布对不上。

**修法**：改为「全章最后一段拉得极长，感官在那一段里逐级失灵」——原文的长段在末段（`:27`，1,896 字符，占本章大半），前七段都很短。

### E3｜`md:11`「母亲一碰她整个人就软了下去」与块 3 的「女儿不是昏过去，是被关掉了」之间，漏掉了「她站起来却像睡着」这一拍｜档：提示

**原文侧**（`text/ch07_chapter_7.txt:18`）：

> Brisa got back on her feet and looked at her worried mother, but she didn’t seem to comprehend her words.

**原文侧**（`text/ch07_chapter_7.txt:21`）：

> Diana could tell that although her eyes were open, she was fast asleep.

**md 侧**：`md:45`、`md:49` 写了「被关掉」；`md:108` 词汇例句引了 `:18` 那句，但正文分析没有写「她被扶起来后站在那里，眼睛睁着却像在睡觉」这一状态。

**影响**：原文里 Brisa 的异常不是一次性的「瘫软」，而是「站起来之后人是醒着的壳子」——`:18` 听不进话、`:21` 眼睛睁着却已经睡着。这一层是「她不是普通的睡梦状态」的关键证据；md 只保留「被关掉」这个比喻，读者拿不到「睁着眼睡着」这一更怪的事实。

**修法**：块 3（`md:43-51`）中文理解补一句：她被扶起来后重新站着，望着母亲却像没听懂话，眼睛睁着，人已经在睡。

### E4｜`md:87`「开灯之后的那份『正常』」与原文的限定语有出入｜档：提示

**原文侧**（`text/ch07_chapter_7.txt:27`）：

> She looked at Brisa again. She was in an uncomfortable position, but not an unnatural one, nothing like what she'd seen.

**md 侧**（`ch07 chapter 7.md:87`）：

> **读者视角提示**：开灯之后的那份「正常」，是这一夜最精密的安慰；把它记下来，后面再回来看这段。

**影响**：原文的措辞是双重否定：「姿势不舒服，但不是不自然的那种，**完全不像她刚才看到的那个**」。原文并没有说开灯后「一切正常」——原文说的是「开灯后看到的姿势不自然吗？不，它不自然得恰到好处，但它跟我刚才看见的不一样」。md 的「正常」与 `md:11` 的「开灯却一切正常」把这个双重否定压成了「正常」，恰好抹掉了「跟刚才不一样」这层——也就是原文里真正吓人的地方（不是它变正常了，是它变成了另一个东西）。

**修法**：`md:87` 与 `md:11` 改写为「开灯后看到的并不是刚才那副模样——它只是个不舒服但谈不上反常的姿势，可那已经不是她黑暗中摸到的那个东西了」。

---

## 四、交叉说明（支撑链）

1. **梦游归属链**（支持 L4、E1）：`text/ch07:27`「now she was absolutely sure Brisa had been sleepwalking, but rousing that man was basically impossible」——「梦游」是 **Diana 的判断**，「叫不醒」的对象是 **Carlos**；同段下文「angry, if unfairly, that Carlos was out through the whole thing」。全章别处再无 "sleepwalking"（取证：`/usr/bin/grep -rn "sleepwalking" text/` → exit=0，命中 `text/ch06_chapter_6.txt:12` 与 `text/ch07_chapter_7.txt:27` 两处）。⇒ md 正文必须把「梦游」写成母亲的结论，不能写成叙述者/作者的事实判定。
2. **两次触碰链**（支持 E1、E3）：`text:12`（转身时瘫软）→ `text:18`（站起来但听不进）→ `text:21`（睁眼却睡着、被放回床上、真正醒来）→ `text:24`（要水）→ `text:27`（第二次触摸摸到不像背/胸的形状 → 看到膝盖脚尖朝上 → 开灯 → 耳机守夜）。md 的七块分别落在 `:6 / :6 / :12 / :27 / :27 / :27 / :27`，因此块 4 之后的中段（`:18`、`:21`、`:24`）在 md 里整段没有对应分析。
3. **跨章一致性**：`text/ch06_chapter_6.txt:12` 已有 "approach Brisa like a sleepwalking explorer"，说明「梦游」是 Diana 长期的解读框架而非本章新造的修辞；`ch07` md 无跨章事件指认，无需跨章核对。

---

## 五、修后复核

本单只出指令，**未改动任何 md 文件；git 未执行任何操作**。

修后应达成的状态：

| 项 | 期望 |
|---|---|
| L1 / L2 / L3 / L4 四条漏 | 在 `md:11-15` 或对应块的中文理解里补齐对应事实（引号内的原文逐字建议照抄 `:9`、`:21`、`:24`、`:27`） |
| E1 拆分两次触碰 | `md:11` 拆成「转过来时瘫软」＋「第二次触摸摸到形状不对」两句 |
| E2 段落结构 | `md:15` 改为「最后一段拉得极长」 |
| E3 睁眼睡着 | 块 3（`md:43`）中文理解补一句 |
| E4 开灯后的「正常」 | `md:87`、`md:11` 改为「跟黑暗中看到的不是同一副模样」 |

复核命令（修完后应全部 exit=1，因为这些字符串在修稿中已被替换或删除）：

```
/usr/bin/grep -cE 'Get in bed|bathroom' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
/usr/bin/grep -cE 'camp sleeping|sleeping bag|rolled onto' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
/usr/bin/grep -c 'thirsty' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
/usr/bin/grep -c '全章几乎是一个长段落' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
```

机器层期望：`bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md" --json` 退出码 **0**，`counts.struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`、`quote_long 0`、`segment_miss 0`；`form.h1_shape_ok true`、`nav_count 5`、`blocks 7`。

---

## 六、复核轮次二（2026-10-21 23:35，md 已按本单修过后复核）

- 受审 md 版本：`ch07 chapter 7.md` = 11758 字节 / 140 行 / md5 `c6d3c343fcaad849af1d24ba8e017f60`，对应 commit `6f02ca802`（21:40:08，「ch07 复核修复（两次触摸合并为一处/开灯后落差/段落形态）」）。
- 机器层复跑：`bash scripts/chapter.sh "…/ch07 chapter 7.md" --json` → 退出码 **0**，`verdict: ok`；`counts`：`struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`、`quote_long 0`、`template 0`、`hole 0`、`block_count 0`、`segments 7`、`segment_miss 0`；`form`：`h1_shape_ok true`、`nav_count 5`、`nav_count_ok true`、`blocks 7`、`block_median 7.5`、`block_range [5,8]`、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示、`profile novels`、`baseline book`；引语字符位 [139, 418, 742, 1367, 2466, 2705, 2999] 与存档 `2-machine.json` 一致（复跑输出写临时文件，未覆盖存档）。
- 逐字复跑：自写脚本 `check_md_quotes.py`（ch07）→ 原句块 7 条全部命中，词汇例句 MISS 数 = 0。

### 本轮已销账（6 项）

| 原编号 | 状态 | 复核证据 |
|---|---|---|
| E1（阻断） | **已修** | `md:11` 现文：「母亲伸手想把她转过来，她却一下子瘫了下去；后来母亲再伸手去安抚，手一碰，胃就抽紧了——摸到的身体既不像背也不像胸，开灯之后看到的东西又和刚才完全不同」——两次触碰已拆成两句，与 `text/ch07:12`「When she tried to turn her around by the shoulders, Brisa collapsed.」＋`text/ch07:27`「it felt nothing like her back or even her chest」一一对应。 |
| E2 | **已修** | `md:15` 现文「正文段落不长却连成一条单向的下坠」；段落实测：8 个正文自然段、正文 3272 字符，末段 `:27` 占 1895 字符＝**57.9%**，前七段合计 20.0%＋2.9%＋6.7%＋2.0%＋3.2%＋6.9%＋0.4%。 |
| E4 | **已修** | `md:87` 现文「开灯之后看到的东西和她以为看到的完全不一样，这份落差是这一夜最精密的安慰」；`md:11` 同口径改为「开灯之后看到的东西又和刚才完全不同」。 |
| E3 | **部分修** | `md:11` 已含「后来母亲再伸手去安抚，手一碰，胃就抽紧了」；但「她站起来却像睡着」这一拍仍未写（见下方 L5）。 |
| L4 | **部分修** | `md:13` 现文已写「**母亲认定**女儿是在梦游」——归属已标（符合 `text/ch07:27`「now she was absolutely sure Brisa had been sleepwalking」）；但「叫不醒 Carlos」仍未进正文（见 L6）。 |
| L1 / L2 / L3 | **未修** | 见下方 L1–L3。 |

### 本轮新增／仍未修（提示级，均无原文逐字冲突）

#### L1｜Brisa 醒来后那句「I'm thirsty.」仍未进 md｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:24`）：

> "I'm thirsty."

**原文侧**（`text/ch07_chapter_7.txt:21`）：

> Unsettled, she helped her lie back in bed and covered her with the duvet. It was then that Brisa truly woke up.

**md 侧**：`/usr/bin/grep -cE "thirsty|Get in bed|bathroom|camp sleeping|sleeping bag|rolled onto" "…/ch07 chapter 7.md"` → **0；退出码 1**。

**影响**：母亲把女儿放回床上盖好被子之后，女儿才真正醒来，第一句是要水——这是这一夜唯一的「她回来了」的信号。md 的七个块停在 `:6/6/12/27/27/27/27`，`:18`–`:24` 这一整段（站起来却听不进话 → 睁眼睡着 → 放回床上 → 醒来要水）没有对应分析。

**修法**：块 4（`md:55-63`）「中文理解」补一句：她把女儿放回床上盖好被子，女儿这才真正醒来，第一句话是要水（`:21`「It was then that Brisa truly woke up.」＋`:24`「"I'm thirsty."」）。

#### L2｜Diana 的两句台词仍未进 md｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:9`）：

> "Honey, what's going on? Get in bed." Brisa didn't answer. "Do you have to go to the bathroom?"

**影响**：原文里母亲的第一个反应是把这一切当普通起夜处理，两句都没得到回答；这拍「先按常识解释」的铺垫在 md 里缺失，读者直接看到「女儿瘫软」，少了常识失效的那一步。

**修法**：块 3（`md:43-51`）「中文理解」补一句：母亲先按孩子要起夜处理，问了两句都没得到回答。

#### L3｜露营睡袋与「女儿已翻身趴下」仍未进 md｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:27`）：

> She took one of the kids' camp sleeping bags from the closet, stretched it out on the little mat, and reached up with one hand to hold Brisa's; her daughter had now rolled onto her stomach.

**影响**：女儿翻身趴下是第二次触摸摸到「不像背也不像胸」的因果前提；缺了它，块 5 的触感异变显得突然。

**修法**：块 5（`md:67-75`）「为什么这样写」补一句：她铺开睡袋、握住女儿的手，女儿自己翻成趴姿，这才有了第二次触摸。

#### L5｜「她站起来却像睡着」这一拍仍未写｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:18`）：

> Brisa got back on her feet and looked at her worried mother, but she didn't seem to comprehend her words.

**原文侧**（`text/ch07_chapter_7.txt:21`）：

> Diana could tell that although her eyes were open, she was fast asleep.

**md 侧**：`/usr/bin/grep -c "听不进" "…/ch07 chapter 7.md"` → 0，退出码 1；`md:93` 里的「睁着眼」指的是母亲守夜（`text/ch07:27`「proceeded to lie awake all night」），不是这一拍。

**影响**：原文里 Brisa 的异常不是一次性的瘫软，而是「站起来之后人是醒着的壳子」——听不进话、眼睛睁着却已经睡着。这是「她不是普通睡眠状态」最硬的证据。

**修法**：块 3（`md:43-51`）「中文理解」补一句：她被扶起来后重新站着，望着母亲却像没听懂话，眼睛睁着，人已经在睡。

#### L6｜叫不醒 Carlos 这件事仍未进正文｜档：提示（漏）

**原文侧**（`text/ch07_chapter_7.txt:27`）：

> She tried to wake Carlos up to tell him what had happened, to say that now she was absolutely sure Brisa had been sleepwalking, but rousing that man was basically impossible.

**原文侧**（`text/ch07_chapter_7.txt:27`，下文）：

> She was still feeling worked up, and angry, if unfairly, that Carlos was out through the whole thing.

**md 侧**：`/usr/bin/grep -nE "sleepwalking|Carlos" "…/ch07 chapter 7.md"` → 仅 `md:123` 词汇例句一行（rousing）；正文分析里没有「叫不醒丈夫」这一事实。

**影响**：这一层决定「梦游」这个解释的可信度——它不是叙述者的判断，而是**母亲独自守了一夜的唯一解释**，而她连说出口的机会都没有（丈夫叫不醒）。md 的 `md:13` 写了「母亲认定女儿是在梦游」，读者仍看不到这个解释的处境。

**修法**：块 4（`md:55-63`）「读者视角提示」补一句：她试着叫醒丈夫告诉他实情、说她已确定女儿是在梦游，可那人根本叫不醒；这一夜她只能自己守着。

### 本轮复核命令（原样）

```
/usr/bin/grep -cE "thirsty|Get in bed|bathroom|camp sleeping|sleeping bag|rolled onto" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 0；退出码 1
/usr/bin/grep -nE "sleepwalking|Carlos" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ md:123（词汇例句 rousing）；退出码 0
/usr/bin/grep -c "听不进" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 0；退出码 1
/usr/bin/grep -n "全章几乎是一个长段落" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 无输出；退出码 1（E2 已修）
/usr/bin/grep -n "开灯之后的那份" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md"
→ 无输出；退出码 1（E4 已修）
```

### 本轮结论

- **本章无阻断**：上一轮的 E1 阻断已由 `6f02ca802` 修掉，复核通过。
- 本轮剩余 6 项（L1、L2、L3、L5、L6 ＋ E3 的残余）全部是「md 未覆盖原文事实」的**漏**（提示档），**没有一条与原文逐字冲突**。
- 剩余漏项的共同后果：`:18`–`:24` 这一整段（站起来听不进话 → 睁眼睡着 → 放回床上 → 醒来要水）以及「叫不醒 Carlos」在 md 里没有对应分析；md 的七块落在 `:6/6/12/27/27/27/27`。
