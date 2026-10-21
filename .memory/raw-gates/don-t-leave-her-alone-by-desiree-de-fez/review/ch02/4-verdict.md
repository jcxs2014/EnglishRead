# 第 2 章 R4 判定单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch02 chapter 2.md`（成品，156 行，8 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch02_chapter_2.txt`（原文，483 行）
- 机器层：`review/ch02/2-machine.json`（已存在、未覆盖）——`verdict: ok`；8 块全 `ok=true`；`issues` 仅 `keyword_long` 8 条（块 1–8），非阻断
- 流程：R1 素读（`review/ch02/1-suread.json`）→ R2 机器层 → R3 差异单（`review/ch02/3-diff.md`）→ R4 逐块＋固定三问
- 行号约定：`text/ch02_chapter_2.txt:NNN`＝原文行号；`md:NNN`＝成品 md 行号
- 取证口径：全部用显式路径 `/usr/bin/grep`（`text/` 被 `.gitignore` 忽略，`git grep` 对它永远查无），短词用 `-w`，交替匹配用 `-E`；词数按空格切分实测

---

## 一、四组数

| 组 | 结论 |
|---|---|
| 逐字 | 8/8 块引语整串逐字命中原文（`segment_miss=0`）；引语正文一字未动 |
| 对应 | 8 块 × 4 字段 ＝ 32 个对应点，＋导航 5 条、＋一句话总结 1 条；结果：**阻断 2、提示 5、漏 7**，全部落在导航／中文理解／为什么这样写／读者视角提示层 |
| 形态 | H1 `02. Chapter 2` ✅；导航 5 项 ✅；子项 4 项齐备 ✅；块数 8（本书中位 7.5、范围 5–8）✅；`## 本章词汇` 三档齐 ✅；一句话总结 1 条 ✅ |
| 断言 | 逐条回原文取证：**编造 0**；阻断 2（W1／W2，已修）；提示 5（W3–W7，已修）；漏 7（L1–L7，已补）；假红 2（keyword_long、块数建议） |

---

## 二、判定表

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| 1 | W1｜`md:109`「引语里的最后一句只有**四个词**」 | `text:483`「They could find no solace.」——按空格实测 **5 词**（They / could / find / no / solace.） | 与原文不符，已改回「五个词」 | **阻断（已修）** |
| 2 | W2｜`md:75`（块 5 读者视角提示）「本章后面她抱着孩子追店员时，注意力**再次**收缩」 | 全章收缩仅 `text:249` 一处（`grep -c "shed all objects and life"` → 1），且原句 5 引的就是这一段；`text:219` 的水母是**电视屏幕**画面（"a swarm of jellyfish on the screen at her back"） | 与原文不符，已改「全章只有这一次收缩，就发生在这一段里」 | **阻断（已修）** |
| 3 | W3｜`md:109`「三个解释来源（医生、教练、家人）」 | `text:483`「None of the explanations from pediatricians, gymnastics coaches, Carmen, Carlos, or Juan convinced them.」＝**五个**来源 | 数字错，已改「五个解释来源（儿科医生、体操教练，外加 Carmen、Carlos、Juan 三位家人）」 | 提示（已修） |
| 4 | W4｜`md:61`（块 4 为什么这样写）「接着**他**抽出其中一条」 | 同块 `md:57` 的「她」＝Diana（数癖好的人）；作者是女性，「他」在同块无指代对象 | 归属不清，已改「接着从清单里挑出其中一条」 | 提示（已修） |
| 5 | W5｜`md:109`「最后一句」 | 同块 `md:111`「本章最后一句」＝`text:483` 末句 "at the exact same time."；同块两个「最后一句」指向不同句子 | 指代含混，已改「引语里的最后一句」 | 提示（已修） |
| 6 | W6｜`md:12`「恐惧线则借血**正式登场**」 | 与总览「节点六：恐惧越过家门（ch06-ch07）」的起点冲突；ch01 同类措辞已改为「都还没成形」 | 与总览口径冲突，已改「恐惧线则开始渗血」 | 提示（已修） |
| 7 | W7｜`md:12`「承第一章那种「**非做不可**」的焦虑」 | 「非做不可」出自 ch16，ch01 无此措辞（`grep "非做不可" ch01 chapter 1.md` → 0） | 出处错，已改「承第一章那种停不下来的焦虑」 | 提示（已修） |
| 8 | L1｜本章没有任何时间锚点 | `text:36`「on a Wednesday at seven a.m.」、`text:9`「It was seven thirty a.m.」、`text:132`「only three days until Christmas」、`text:48` Carmen 75 岁、`text:129` Alba 37 岁 | 漏，已补 `md:11`「周三清早，距圣诞节还有三天，Carmen 七十五岁、Alba 三十七岁」 | 提示（已修） |
| 9 | L2｜每天接送的日程与「小公社」 | `text:117`「the infinitely more reasonable option」；`text:126` 学校在 Westfield La Maquinista；`text:342` 提到的 Esplugues 线路；五人「little commune」 | 漏，已补 `md:45`（Esplugues、半小时路程、一段公交、五人小公社） | 提示（已修） |
| 10 | L3｜Alba 没有工作、自己的事一直被推后 | `text:129`「The supposed demands of motherhood always meant postponing whatever had to do with her exclusively.」「Only her older sister, Diana, insisted she go to a specialist and sent her a dermatologist’s number several times.」 | 漏，已补 `md:21`（无工作、眼皮鳞状、皮肤科号码） | 提示（已修） |
| 11 | L4｜二十三个癖好是谁数的、为什么数 | `text:132`（Diana 在父亲葬礼守夜上数母系女人的癖好） | 漏，已补 `md:57` | 提示（已修） |
| 12 | L5｜Brigitte 体操馆那一整场 | `text:471`「The neckline of her leotard, white with silver trim, was soaked with blood」；「three meters of beige carpet」；`text:474`「why she looked like a little serial killer」；两个 trainer | 漏，已补 `md:105`（平衡木、白色滚边连体衣、三米米色地毯、两个教练、「像个小连环杀手」） | 提示（已修） |
| 13 | L6｜误按录像键与视频自己播放 | `text:480`「she didn’t realize that she had hit record and was taking a video」「The video she had just taken started playing on its own」 | 漏，已补 `md:93`（塑料尺三十厘米、误按录像键、视频自播） | 提示（已修） |
| 14 | L7｜Alba「跨门两次」的强迫 | `text:132`「compulsion to cross through a door or an archway twice」 | 漏，已补 `md:69` | 提示（已修） |
| 15 | 机器层 `keyword_long` 8 条 | 块 1–8 的关键词为整句照抄 | 判据是「选词」不是「改事实」，非缺陷 | 假红 |
| 16 | 机器层块数建议 13–15 | 本书形态约束：块数范围 5–8、中位 7.5（`python3 scripts/bookform.py` 首行） | 按本书形态约束，不按单章篇幅建议 | 假红 |

---

## 三、收口复核（逐块三问：主语／受事／归属，8 块 × 3 问 ＝ 24 问，全部回原文有出处）

- **块 1**（`md:19`–`md:29`）：主语＝Alba（"Alba planned her summers in January"）；受事＝一年的日子与三趟采购（机票、AliExpress 装饰、圣诞采购）；归属＝「只有姐姐 Diana 坚持让她去看专科」＝**Diana 主动**（`text:129`「Only her older sister, Diana, insisted she go to a specialist」），「她自己没有工作」＝Alba 一侧 ✔
- **块 2**（`md:31`–`md:41`）：主语＝Alba（踢飞玩具车）；受事＝墙（"crashed against the wall"）；归属＝「这不是意外」＝Alba 的判断（"It wasn’t an accident."）✔
- **块 3**（`md:43`–`md:53`）：被描写主体＝祖母（"The grandmother always a bodily extension of the mother"）；喻体＝多触手水母；归属＝「同一个生命体／不断繁殖」＝作者判断（`text:33`–`text:36`），「每天要跑好几趟…五人小公社」＝`text:117` 的日程事实 ✔
- **块 4**（`md:55`–`md:65`）：主语＝**Diana**（"She had counted twenty-three obvious manias"，`md:57` 已点明）；受事＝二十三个癖好；归属＝清单数于父亲葬礼守夜＝**Diana 所数**（`text:132`）✔
- **块 5**（`md:67`–`md:77`）：主语＝Alba；受事＝所穿行的空间（"shed all objects and life"）；归属＝「跨门两次的强迫」＝Alba 本人（`text:132`），「母亲一直知道」＝`text:132` ✔
- **块 6**（`md:79`–`md:89`）：主语＝Alba（"Alba said"）；施事＝「那两个寡妇里的一个——那个斜眼的」（老妇）；受事＝从鼻子里滴下的血与围巾；归属＝「她给我下了咒」＝**Alba 自己的说法**（`text:342` 的 the widows 是约七十岁的老妇，与 Carmen 75 岁不可混）✔
- **块 7**（`md:91`–`md:101`）：主语＝Diana（"Once she had freed Brisa of it"）；受事＝从掌心长到肘部的血块；归属＝量尺、误按录像、视频自播＝**Diana 亲手做的流程**（`text:480`）✔
- **块 8**（`md:103`–`md:113`）：主语＝两位母亲并列（"Diana and Alba both barely slept that night"）；受事＝内疚与血块（"the guilt seeped through their insides"）；归属＝「五个解释来源」＝文本列举（`text:483`），「她们找不到任何安慰」＝文本结论（"They could find no solace."）✔

---

## 四、已核实为正确（防误修清单）

1. `md:51`「水母本章后段还会以另一种方式再出现一次」——`text:219`「Carmen turned for a second and saw a swarm of jellyfish on the screen at her back」成立（是**电视屏幕画面**，不是注意力收缩），不得改。
2. `md:11` 结尾把时间拨回一个月前——`text:468`「About a month ago, the girls’ noses had both bled dramatically, in different places and situations but at the same time.」成立。
3. 称呼链：**Juan ＝ Alba 的丈夫**、**Carlos ＝ Diana 的伴侣**（`text:126`、`text:483`）；「your sister」在 Carlos 口中＝**Alba**（`text:513`，与 `text:549`「six years older than Alba」互证）。
4. Alba 有三个孩子；「七个」与「九个」岁分别为长女与次女（`text:117`）。
5. **Brigitte 是 Brisa 的表姐**（`text:477`「her cousin」）；**Tomás 是 Brisa 的哥哥**（`text:480`「Tomás’s plastic ruler」）。
6. 手柄是给**长子**换的（`text:126`「a couple of Switch controllers for her eldest」），不是给 Brisa。
7. the widows 是**约七十岁的老妇**（`text:342`「They looked to be around seventy」），与 **Carmen 75 岁**不可混。
8. 本章＝**12 月 22 日周三**；Alba 生日 12/23（`text:165`「Tomorrow is my birthday.」）；平安夜 12/24（`text:171`「Christmas Eve? Are you out of your mind?」）。
9. `md:57` 的「她」＝**Diana**（数癖好的人），不是 Alba。
10. 词汇表三档例句全部逐字命中本章 `text/`（自跑比对：18 章 × 三档 × 例句，非逐字 0、缺档 0）。
11. 8 个引语块逐字且位置递增；**引语正文一字未动**——本轮 2 条阻断与 5 条提示全部落在导航／中文理解／为什么这样写／读者视角提示层。
12. `md:105`「阿爾巴跳下看台追过去…把手里那瓶水一口气喝光」＝`text:474`「She sat down next to Brigitte and drank the entire bottle of water she was still holding in one go.」成立。

---

## 五、复核命令（期望退出码）

```bash
cd ~/Documents/Works/EnglishRead
# 旧措辞应查无（期望 exit 1）
/usr/bin/grep -nE "四个词|再次收缩|三个解释来源|接着他抽出|正式登场|非做不可" \
  "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch02 chapter 2.md"
# 本章收缩只有一次（期望输出 1 行）
/usr/bin/grep -c "shed all objects and life" \
  "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch02_chapter_2.txt"
# 机器层（期望退出码 0）
bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch02 chapter 2.md"
# 整书门禁（期望退出码 0、「0 条阻断型」）
bash scripts/gate.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/"
```
