# ch25 对账（R1–R4）

text = `text/ch25_chapter_twenty_four.txt`（147 行，1,608 词）｜md = `ch25 aunt virginia announces moving out.md`｜块数 5（建议 3–5 ✅）｜素读事实 85 条／MISS 0｜机器层 rc=0（引语块 5／片段 5／查无 0）

## 阻断

- **[C-25-1] 漏·承重单元：Gazzie 的本名 Gertrude（全书唯一一次出现）**｜:18 `“I’m not gallivanting, Gertrude; I’m spending quality time with my girlfriend…”`
  `/usr/bin/grep -n "Gertrude" text/*.txt` ⇒ 全书仅 ch25:18 一处——Virginia 当面叫出 Gazzie 的本名，是本章（也是全书）唯一一次祖母以名字现身。md 全篇（导航五句、5 块、词表、总结）无一字登记；「人物弧线」只写冲突不写命名。
  ⇒ 在「人物弧线」或块 2 一带登记：Virginia 在争吵中当面叫出 `Gertrude`——叙述者一直只闻代号 Gazzie，本章拿到真名（全书唯一出处）。
- **[C-25-2] 漏·承重单元：Leon 线三拍全未登记**｜:63 `“You’ve driven off everyone who’s ever loved you. Or left them in a grave.”` → :66 `Was she referring to Gazzie locking him in the breeding pond, or was there more to it?` → :69 `I’ll make her let me go or die trying.`
  这是本章唯一的超自然/悬案拍点：graves 一句点名死人 → 她跳到 Leon 与 breeding pond（她的既有怀疑，`ch20:378` 罚去清 breeding pond）→ Leon 那行字原句复现（首出 `ch23:119`，`/usr/bin/grep` 确认 :69 为第二次）。md 对这三拍零登记；导航与总结只走人际关系线。
  ⇒ 至少在「叙事手法」或加一块处理： grave 句 → breeding pond 之疑 → :69 那行字的复现，并标注 :66 是疑问句（"or was there more to it?"）、不裁决。
- **[C-25-3] 逐字·撇号字形（5 处，全书同形态队列）**｜md:13 `That's`／`didn't`×2、md:14 `didn't`、md:98 `one's`
  原文全部为 U+2019（:123 `That’s what I told myself, anyway`、:114 `I didn’t wonder…`／`I didn’t note…`、:98 词表释义 `hold one's breath` 亦应作 `one’s`）。短语本身逐字正确，只改字形；属全书 15/49 章 51 处判形队列，机器层不覆盖。

## 提示

- **[P-1]**｜md:10「**摔门**开车走人」＋「**晚餐桌边**」——:75 只有 `Gazzie stomped around the side of the house`（跺脚绕到屋侧），无摔门；SUV 已走是 :114 的回望。:138 餐桌上只有柠檬水（`a glass of lemonade`），未写晚餐。
- **[P-2]**｜md:12「家里的账本**第一次**当着她的面翻开」——跨章「第一次」表述有反例风险：ch21 Gazzie 已当面交代纵火旧事。建议改「姐妹矛盾的账本第一次当面翻开」，把范围收到本章这组矛盾。
- **[P-3]**｜md:13「最后**自己承认** ‘You manipulated me’」——该句是她的控诉（:99 `“You manipulated me,” I said, voice cracking`），「承认」易读成认罪；建议「亲口说出」。
- **[P-4]**｜md:56「她还惦记着 Harrison 的**吻**」——吻未发生：ch24 止于 `leaned forward half an inch`＋被打断（ch24:336–:351）；本章 :9 也只是 `the thought of kissing me`。改「那记没落成的吻」。
- **[P-5]**｜md:102「并**承认**邀 Dart 上岛有掩人耳目的成分」——原文 :84 是 `She winced, not denying it.`（不否认）；:90 还给出「怕你不想来／怕你留不下」的另一层解释。改「没有否认」。
- **[P-6]**｜漏：:102 `I imagined my hand connecting with her face… Another ugly thought.`——她想象自己扇 Virginia 耳光并自标「又一个丑陋念头」，与她压抑冲动的既有线相接，md 未登记。
- **[P-7]**｜漏：:126 `Uncle Leon’s painting of Ida digging underneath the house`——那幅画的具象内容（Ida 在房子底下挖）未登记；与 ch23 速写本「墙是骨头」互为图证。

## 假红（核对后成立——防下一轮改坏）

- md:10「两姐妹互翻旧账」——:42 `waving off her sister with the other`，姐妹关系逐字。
- md:10「夏至派对后要搬去和 Henri 同住」——:51 逐字。
- md:10「步行五十分钟回 Greer House」——:114 `The walk to Greer House took fifty minutes` 逐字。
- md:10「只剩留在 Amelia Island 赢回 Gazzie 认可这一条路」——:135 `I had only one option: stay on Amelia Island and win her approval`。
- md:13 两句 didn’t 引文（`I didn't wonder how badly…`／`I didn't note the ease…`）——:114 逐字（字形另列 C-25-3）。
- md:13 `That's what I told myself, anyway`——:123 逐字（字形另列）。
- block2 引文逐字＝:15；读者提示「Virginia 前一句 Hire a PA…」＝:12 确在其前。
- block3 引文逐字＝:51；`The details clicked into place` 引用＝:54。
- block5 引文逐字＝:147；`I can see that`＝:144。
- md:14「‘I didn’t…’ 的排比否定句」——:114 四连 didn’t 成立（md 择二引之，未误称全量）。
- 逐字／形态层：引语块 5 条全部逐字（机器查无 0＋人工 5/5）；词表 15 行例句逐字（flag 0）；非块内嵌英文全书查无 0（仅 `Chapter Twenty-Four`／`Tropes` 模板例外）。

## 不许裁决

1. Leon 是否真被 Gazzie 锁进 breeding pond、死因为何——:66 是她的疑问（`or was there more to it?`）；Michelle／Leon／Mama 三种死法一律不裁决（书级护栏）。
2. `Or left them in a grave.` 具体指谁——:63 未点名，不得坐实。
3. Virginia 邀她上岛的动机——:84 `not denying it` 与 :90「怕你不想来」两层并存，不裁决。
4. Gazzie 一巴掌的动机——:102 `That’s why Gazzie had slapped her` 是叙述者的解读。
5. 「two separate presences or one」——:126 她自己拿不准，不裁决。
6. Harrison 是否对她有意、是否站在她这边——:123 是她的自我说服（`That’s what I told myself, anyway`）。
7. Virginia 与 Gazzie 旧账的具体事例（:117 `other instances where Aunt Virginia coerced Gazzie`）——原文未列，不裁决。
8. Gazzie 提到的 Mother 与 Ida 的裁定内容（:15 `Even Mother agreed with Ida on that`）——只有结论没有内容，不引申。

## 跨章取证表

| 本章条目 | 取证位置 | 用途 |
|---|---|---|
| Gertrude＝Gazzie 本名（全书唯一） | ch25:18（`grep "Gertrude"` 全书 1 处） | C-25-1 |
| breeding pond 与 Leon 的既有怀疑 | ch20:378（罚清 breeding pond）／ch32:144（后文口径） | C-25-2 |
| `I’ll make her let me go or die trying.` 首出 | ch23:119 | C-25-2 |
| 吻未发生 | ch24:336–:351 | P-4 |
| 纵火旧事已当面交代 | ch21（Gazzie’s arson confession） | P-2 |
| 姐妹关系 | ch25:42 | 假红 1 |

## 探针自检（本判定文件自身）

`/tmp/span25.py`：结果见 4-verdict.md；`/tmp/v25.py` 词表 15 行／flag 0；`/tmp/ap25.py` ASCII 撇号 **5 处**（md:13×3／md:14／md:98，已列 C-25-3）／反引号 span 0；`/tmp/in25.py` 内嵌英文 117 串／全书查无 2（两个模板例外）；`/tmp/s25.py` 素读 85 条／MISS 0。
