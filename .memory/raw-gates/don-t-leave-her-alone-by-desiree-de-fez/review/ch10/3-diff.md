# 第 10 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md`（成品，154 行，8 个引语块，22 条词汇）
- 机器层唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch10_chapter_10.txt`（原文，924 行，46,518 字符）
- 机器层：`bash scripts/chapter.sh "…/ch10 chapter 10.md" --json` → **退出码 0**，`verdict: ok`，`issues` 四组全空（详见 `2-machine.json`）
- 流程：R1 素读（`1-suread.json`，先读原文后开 md）→ R2 机器层 → R3 三张单子 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号
- 取证一律走显式路径 `/usr/bin/grep`（本书 `text/` 被 `.gitignore` 排除，`git grep` 在此目录永远查无，退出码与「真查无」不可区分）；命令、输出、退出码逐条附在各项下方

---

## 一、漏（L）

### L1｜车身上的血手印与车底那块血布——全篇未写｜档：提示（漏）

**原文侧**（`text/ch10_chapter_10.txt:147`）：

> Diana and Carlos went, and Juan gestured that they should look closely. They quickly saw that the car was blood-streaked. A handprint, the fingers spread wide, made a broken path from one side door to the trunk. The marks were unmistakable. And on the ground, sticking out beneath the car, there was something that looked like a sheet, also soaked with blood. Carlos tried to pull it out with his foot, but Juan stopped him.

**原文侧**（`text/ch10_chapter_10.txt:168`）：

> I cleaned it as well as I could, and I tried to apply pressure with a blanket we had in the back. That's what you see underneath the car.

**md 侧**：md 全文无「手印」「车底」「后备箱」「血布」。

取证命令：
```
/usr/bin/grep -cE '手印|车底|后备箱|血布' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1
```

**影响**：这一段是本章唯一的**物证**——Alba 的车里留下一个张开五指的血手印，从一侧车门拖到后备厢；车底下压着的那块「像床单一样的东西」正是 Juan 用后备厢的毯子压住 Carmen 伤口时垫的。md 只在 `md:39` 写了「肚皮上全是血块」（那是 Juan 口述），读者拿不到任何能看见的证据，Juan 讲经过那段的说服力随之下降。

**修法**：在块 2 或 `md:15` 补一句：Juan 招手让他们看车——车身溅满血，一个张开五指的血手印从一侧车门拖到后备厢；车底下露出一块像床单的东西，也浸透了血，那就是他用来给 Carmen 压住伤口的毯子。

### L2｜Juan 讲的走散经过（商场内走散、手机在他手里、MediaMarkt 手柄）——只以词汇例句形式出现，正文分析没有｜档：提示（漏）

**原文侧**（`text/ch10_chapter_10.txt:87`）：

> "She doesn’t have her phone. It happened so fast. We got separated inside. I thought she was with your mom, and your mom thought she was with me."

**原文侧**（`text/ch10_chapter_10.txt:93`）：

> "Not at all. About forty-five minutes. But when they announced the mall was closing, we split up—she had to get a few more gifts and didn’t want the kids to see. I’m convinced she went back to MediaMarkt to ask about the Switch controllers. I took Brigitte and Juanito out here and loaded up the car."

**原文侧**（`text/ch10_chapter_10.txt:111`）：

> "Because I have it."

**md 侧**：`md:11` 只写「妹妹 Alba 不在」；`md:137` 的词汇例句「I’m convinced she went back to MediaMarkt to ask about the Switch controllers.」是本章唯一一次提到 MediaMarkt。

取证命令：
```
/usr/bin/grep -c 'MediaMarkt' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 1（仅 md:137 词汇例句行）；退出码 0
/usr/bin/grep -n 'she went back to MediaMarkt' text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:93；退出码 0
```

**影响**：Juan 讲经过是全章中段的骨架（`md:15`「中段让 Juan 单向讲述那道伤口」），可 md 里读者始终不知道 Alba 究竟是怎么没的、她手机为什么在 Juan 手里（`md:114`  Carlos 追问换手机那句「Fuck, Juan. I don’t understand this thing you guys have with swapping phones.」在正文里同样没有落点）。

**修法**：块 2 的「读者视角提示」或 `md:15` 补一句：Juan 说两人是在商场里被人流冲散的，手机在他手上；闭店广播后 Alba 去买没给孩子看的礼物，他「确信」她是折回 MediaMarkt 问 Switch 手柄（`:87`、`:93`、`:111`）。

### L3｜三十年前那道仪式里「光柱、震动、深粉近乎紫」——全篇未写｜档：提示（漏）

**原文侧**（`text/ch10_chapter_10.txt:792`）：

> "Bullshit. You’re closing them because it hurts so bad, just like it’s hurting me. And I don’t know what else they did, because the bingo woman had her back to me, and I couldn’t really see. But I heard something like an axe, or like when they’re cutting meat at the butcher, and the sound of water, or whatever it was, dripping into the plastic bucket. Then I heard sobbing. And they kept singing, or praying, I couldn’t make out the words. I covered my eyes, and when I looked again, there was light shooting up from the table, over the trees and into the sky. A deep pink, almost purple. And everything started to vibrate."

**md 侧**：md 全文无「光柱」「震动」「粉」「紫」；块 7 只取到蜡烛与歌，块 8 从「三十年」起论。

取证命令：
```
/usr/bin/grep -cE '光柱|震动|粉|紫' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1
/usr/bin/grep -n 'light shooting up from the table' text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:792；退出码 0
```

**影响**：这一段是全章超自然线索的落点，也是 Diana「说不清楚」的实体内容（光柱、震动、斧劈般的声音、水滴进塑料桶）。md 的块 8（`md:105-109`）大谈「三十年」这个尺度，却没有告诉读者三十年前到底看见了什么，读者只拿到蜡烛、歌声和一句「看上去像在祈祷」。

**修法**：块 8 的「中文理解」或「读者视角提示」补一句：她能报出来的只有仪式的声音（像斧子、像肉铺切肉、水滴进塑料桶）和颜色——从桌面射起、越过树梢冲进天空的深粉近紫的光柱，以及随之而来的震动。

### L4｜Alba 的露台是营地的复制品——全篇未写｜档：提示（漏）

**原文侧**（`text/ch10_chapter_10.txt:414`）：

> "That’s ridiculous! Anyway, if you haven’t noticed, her patio is basically a replica of the campsite. She’s crammed so much stuff out there, Mom. She even has a cooler! And a deck chair, and a beach umbrella. What good is an umbrella when she already has an awning?"

**原文侧**（`text/ch10_chapter_10.txt:435`）：

> As Diana said, it was a miniature of La Tortuga. There were two beach umbrellas; an outdoor loveseat; an aboveground portable swimming pool, always set up; two folding chairs; the kids’ bikes, scooters, and roller skates; Brigitte’s Hula-Hoop; two beach coolers; a striped deck chair; the old fridge they had repurposed as a pantry… La Tortuga Ligera’s campground sat next to the Castelldefels highway, and Alba’s patio looked out over the B-20 beltway.

**md 侧**：md 全文无「复制」「露台」；块 6（`md:79-87`）直接引用了 Alba 在露台上看广告牌的段落，却没有交代这段的来源。

取证命令：
```
/usr/bin/grep -cE '复制|露台' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1
```

**影响**：原句 6 之所以能出现，是因为 Alba 每晚饭后都上露台坐着，露台本身就是营地的翻版（两把沙滩伞、便携泳池、沙滩冰箱、条纹躺椅、旧冰箱改成储藏室）。缺了这一层，块 6 只是一次广告牌异变；补上之后，读者会明白 Diana 口中「她的露台就是营地」与广告牌异变是同一件事的两端。

**修法**：块 6 的「中文理解」补一句「她的露台本来就是营地的翻版——两把沙滩伞、便携泳池、沙滩冰箱、条纹躺椅，窗外就是 B-20 环城路」，并在「读者视角提示」点出块 6 属于 Alba 视角的转述层。

### L5｜父亲夜里出现在 Diana 家里——全篇未写｜档：提示（漏）

**原文侧**（`text/ch10_chapter_10.txt:558`）：

> "Jesus, yeah. Dad." She paused. "By the way, he was at my house the other night."

**原文侧**（`text/ch10_chapter_10.txt:570`）：

> "I’m serious. I got up to go to the bathroom and realized he’d been there."

**原文侧**（`text/ch10_chapter_10.txt:576`）：

> "The bathroom smelled like it did after he’d been in there—like cigarettes."

**原文侧**（`text/ch10_chapter_10.txt:588`）：

> "At four in the morning? No way. None of our neighbors would be up that late. It was Dad. It’s not the first time, either. And it’s only on certain dates. He also came the night before I went in for my back injection."

**md 侧**：md 全文无「父亲」「爸爸」「卫生间」「烟味」。

取证命令：
```
/usr/bin/grep -cE '父亲|爸爸|卫生间|烟味' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1
/usr/bin/grep -n 'at my house the other night' text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:558；退出码 0
```

**影响**：这一段是本章第二条超自然线索（父亲已两年多未出现在人世，见 `text/ch05_chapter_5.txt:636`、`:642` 的交代），而且它就发生在 Diana 讲营地故事的前夜。md 的块 8 讲「三十年说不出口」，读者却不知道同一夜里她还撞见过另一件说不出口的事。

**修法**：块 8 的「读者视角提示」补一句：在讲这段故事之前，她刚跟母亲讲过另一件事——几天前的凌晨四点，她起夜时发现父亲来过家里，卫生间里是父亲抽完烟的味道，而且只在特定的日子出现。

### L6｜Carmen 一早断言「Alba 从来没有单独过」——全篇未写｜档：提示（漏）

**原文侧**（`text/ch10_chapter_10.txt:276`）：

> "She hasn’t been alone in years," Carmen said after a long pause.

**原文侧**（`text/ch10_chapter_10.txt:288`）：

> "That Alba is never alone."

**原文侧**（`text/ch10_chapter_10.txt:207`）：

> Diana had never met up with just Alba because Alba didn’t go anywhere alone.

**md 侧**：md 全文无「独处」「从不」「单独」；`md:154` 只写「妹妹走丢」。

取证命令：
```
/usr/bin/grep -cE '独处|从不|单独' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1
/usr/bin/grep -n 'She hasn’t been alone in years' text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:276；退出码 0
```

**影响**：这是全书「Alba 从不独处」这条线索在母亲口中的版本（`text/ch05_chapter_5.txt:513`「Your sister is never alone」是 Carlos 的版本，`text/ch14_chapter_14.txt` 是 Alba 侧）。本章里母亲主动说出这一条，读者却只能靠 `md:154` 的「妹妹走丢」自行联想。

**修法**：块 3 的「读者视角提示」补一句：母亲沉默很久后主动说出「她已经很多年没有单独待过了」，Diana 立刻坐直了——「你终于说出来了」。

---

## 二、编（C）

**无。** md 的 5 条导航（`md:11-15`）、8 个引语块的四个子项（`md:19-111`）、词汇表 22 条（`md:113-150`）、一句话总结（`md:154`）中的事实性内容逐条回原文核对，都能落到本章原文；`md:14` 的「手镜」虽与原文不符，但它对应的是原文确有的 `glasses`（`text:6`），属**用词错**而非凭空造物，故归入第三节 W1。

---

## 三、错（W）

### W1｜`md:14`「戴上手镜点数」——原文是眼镜（glasses），且与 `md:21` 自相矛盾｜档：阻断

**原文侧**（`text/ch10_chapter_10.txt:6`）：

> This image of her family—incomplete—shocked her. She took out her glasses and put them on, and pointed to every family member, counting. There were five of them, not six. Alba was missing.

**md 侧**（`ch10 chapter 10.md:14`）：

> - **人物弧线**：Diana 从戴上手镜点数、用双手做成取景框的旁观者，变成三十年后才把当日目击讲出口的人；

**md 侧**（`ch10 chapter 10.md:21`）：

> **中文理解**：她一眼看过去就愣住了：这幅全家图是残缺的。她掏出眼镜戴上，挨个指着家人点数——只有五个，不是六个。少掉的那位是妹妹。

取证命令：
```
/usr/bin/grep -nw 'mirror' text/ch10_chapter_10.txt
→ 无输出；退出码 1
/usr/bin/grep -nw 'glasses' text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:6（"She took out her glasses and put them on"）；退出码 0
/usr/bin/grep -c '手镜' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1
```

**影响**：原文里 Diana 摘下的是眼镜（glasses），中文对应的正是眼镜；`md:21` 已经正确译成「她掏出眼镜戴上」。同一份 md 的导航句写成「手镜」，既是与原文不符（原文无 mirror 一词），也是与本文自己的 `md:21` 打架——读者在导航里读到的物件和进正文后读到的物件不是同一个。

**修法**：`md:14`「戴上手镜点数」→「戴上眼镜点数」（同句的「用双手做成取景框」另见 W2）。

### W2｜`md:14`「用双手做成取景框」——原文是手搭成的遮光板（blinders）｜档：提示

**原文侧**（`text/ch10_chapter_10.txt:9`）：

> Diana made blinders with her own hands—still bloodstained—so she could concentrate on that image, so nothing would distract her and she’d not miss one detail.

**md 侧**（`ch10 chapter 10.md:14`）：

> - **人物弧线**：Diana 从戴上手镜点数、用双手做成取景框的旁观者，变成三十年后才把当日目击讲出口的人；

**影响**：「blinders」是用手在眼前搭起两侧遮住、逼自己专注的挡板；「取景框」是取景取景框，正相反的动作是「框住」，但原文强调的是「别的都不要分散我、一个细节都不许漏」。同一段原文后面确有 "The way her family was scattered across the plane she had framed with her hands"（`:9`，framed＝框住），两处叠在一起容易被译成「取景框」；但就「blinders」这个动作而言，译成「挡光板」更准。

**修法**：`md:14`「用双手做成取景框」→「用双手在眼前搭起挡光板」（若保留「框住」这层，另在块 1 的「为什么这样写」里补一句原文 "framed with her hands"）。

### W3｜`md:14`「Carlos 是把这家族病症说破的那个人」——他只是心里想通，没人听见｜档：提示

**原文侧**（`text/ch10_chapter_10.txt:204`）：

> Carlos couldn’t make sense of it, he didn’t understand why they would avoid doing something so normal. He found it bizarre that they were so close and so mutually dependent, while also completely lacking deeper knowledge about one another.

**原文侧**（`text/ch10_chapter_10.txt:162`）：

> Juan turned to Carlos, perplexed. "I tell her all that, and what, nothing? Not a single question? I can’t with these three."

**md 侧**（`ch10 chapter 10.md:14`）：

> - **人物弧线**：Diana 从戴上手镜点数、用双手做成取景框的旁观者，变成三十年后才把当日目击讲出口的人；Carmen 从草地上那团安静的身影，退回到她曾把梦想投在女儿身上的旧账；Carlos 是把这家族病症说破的那个人；Juan 从报信的人变成质问的人。

**影响**：原文里 Carlos 的这番判断是**叙述层**写他的认知（`:204`），既没有对谁说出口，也没有「说破」这个动作；当场被说破感受的反而是 Juan（「我说了这么多，一个问题都没有？」）。md:49「这一段是全章的病历」把这段写成病历本身没问题，但把它记成 Carlos「说破」会让人以为场上有过一次坦白。

**修法**：`md:14`「Carlos 是把这家族病症说破的那个人」→「Carlos 是看穿这家族病症、却没说出口的那个人」。

### W4｜`md:154`「讲完了，母亲还是不信」——原文里 Carmen 没有表示不信｜档：提示

**原文侧**（`text/ch10_chapter_10.txt:801`）：

> "Boy, you are a writer, aren’t you."

**原文侧**（`text/ch10_chapter_10.txt:807`）：

> "But you were always so scared. Why didn’t you say anything?"

**原文侧**（`text/ch10_chapter_10.txt:810`）：

> "I don’t know. How could I have explained it? I just told you, thirty years later, and still you don’t believe me. Imagine if I’d tried to tell you back then."

**md 侧**（`ch10 chapter 10.md:154`）：

> 平安夜商场关了门，妹妹走丢，她和母亲身上各自带着一道腹部伤口，谁都不肯让别人看；母亲躺在草地上玩消除游戏，女儿趁这个夜晚把三十年前隔着灌木看见的那场仪式从头讲了一遍——讲完了，母亲还是不信。

**影响**：「你不信」是 Diana 自己的说法（`:810` "still you don’t believe me"）；Carmen 的实际反应只有夸她「会写」和追问「当年为什么不说」，没有说过「我不信」。md:111 已写「从头到尾没有追问一句这到底是不是真的」，与 `md:154` 的「母亲还是不信」在同一份文件里口径不一。

**修法**：`md:154` 末句「讲完了，母亲还是不信」→「讲完了，母亲只夸她会写，追问她当年为什么不说」。

### W5｜`md:57`「可她一有了孩子」——原文里有了孩子的是 Diana 指代易被读成母亲｜档：提示

**原文侧**（`text/ch10_chapter_10.txt:210`）：

> But then the spell broke: After her first child, Diana turned into a pumpkin. To Carmen, she was no longer special: Now, she was just another mother. … Carmen had spent years encouraging her to grow, to get out, and then she had a child. That’s why she was so hard on her now, about even the smallest things. How could Diana have dared compromise her fantasy?

**md 侧**（`ch10 chapter 10.md:57`）：

> **中文理解**：母亲曾花了多年催她长大、催她走出去闯荡；可她一有了孩子，母亲就忽然变得苛刻，连最小的事都不放过。母亲给她的责难是一句问话：她怎么敢毁掉自己替她安排好的那场人生。

**影响**：原文两个「she」都指 Diana（原文在同段里点名 "After her first child, Diana turned into a pumpkin"）。md 的中文里「母亲曾花了多年催她长大……可她一有了孩子，母亲就忽然变得苛刻」——两个「她」夹着两个「母亲」，读者很容易把「她一有了孩子」读成母亲生了孩子，这会变成一处亲属/施事误读。

**修法**：`md:57` 改为「母亲曾花了多年催**她**长大、催**她**走出去闯荡；可**她**一有了孩子（原文点名是 Diana 的第一个孩子），母亲就忽然变得苛刻」——把「她」与「母亲」拆开点明。

### W6｜同章内 Juan 的中文名与西文名混用（`md:12` 写「胡安」，`md:15`／`md:137`／`md:138` 写「Juan」）｜档：提示

**md 侧**（`ch10 chapter 10.md:12`）：

> - **情感弧线位置**：全章从少了一个人的外部恐慌起步，一路滑向一种更冷的静——两个被剖开肚子的女人躺在草地上，一个玩消除游戏，一个讲三十年前的旧事；最低点其实在当下，**胡安**描述那道伤口时她母亲的平静……

**md 侧**（`ch10 chapter 10.md:15`）：

> - **叙事手法**：开场用数人头把家庭写成一份清单；中段让 **Juan** 单向讲述那道伤口；……

**同书其他章体例**：`/usr/bin/grep -c "胡安" *.md` → `ch14 chapter 14.md:12`、`ch17 chapter 17.md:6`、`00_情感节点.md:1`、`ch10 chapter 10.md:1`；`/usr/bin/grep -c "Juan" *.md` → `ch02:4`、`ch03:3`、`ch10:2`、`ch14:7`、`ch17:7`。

**影响**：「胡安」是本书 Juan 的既有中文名（ch14、ch17、情感节点表都用它），所以 `md:12` 不是错译；但同一章的 `md:15` 与词汇表却用西文「Juan」，读者要在两种写法之间自行判断是同一个人。

**修法**：本章内统一（建议随 `md:12` 用「胡安」，或随 `md:15` 用「Juan」），全书其余章维持既有体例不动。

### W7｜`md:75`「对方人回来了，心还留在那年夏天」——「人回来了」易被读成字面回营地｜档：提示

**原文侧**（`text/ch10_chapter_10.txt:384`）：

> "Mom! Don’t change the subject. I’m being serious. How is it possible that she still thinks Camp La Tortuga Ligera is the most amazing place on earth? It’s not normal for her to remember those summers as the high point of her existence. I think she’s still there."

**md 侧**（`ch10 chapter 10.md:75`）：

> **读者视角提示**：留意这句判断的对象——不是那个营地，是人；她的意思是对方人回来了，心还留在那年夏天。

**影响**：「I think she’s still there」的 there 指那年的夏天状态，不是「人回到营地」；md 后半句「心还留在那年夏天」已经说对，但前半句「人回来了」容易被读成字面意义上的归来，与 `md:69`「她断言，对方其实还留在那里」的口径也不一致。

**修法**：`md:75`「她的意思是对方人回来了，心还留在那年夏天」→「她的意思是对方人虽然在这儿，心还留在那年夏天」。

---

## 四、交叉说明

1. **称呼与亲属方向**（决定 W5 的读法）
   - `text/ch10_chapter_10.txt:210`：「After her first child, Diana turned into a pumpkin.」⇒ 有了孩子的是 **Diana**。
   - `text/ch10_chapter_10.txt:384`：Diana 对母亲说 "How is it possible that **she** still thinks Camp La Tortuga Ligera…" ⇒ 第三人称的 she ＝ **Alba**。
   - `text/ch05_chapter_5.txt:549`「who was six years older than Alba」、`text/ch02_chapter_2.txt:129`「Only her older sister, Diana…」、`text/ch17_chapter_17.txt:96`「even with six years between them」⇒ Diana 是姐姐、Alba 是妹妹；md `md:21`「少掉的那位是妹妹」正确。
   - `text/ch14_chapter_14.txt:9` 的 "younger daughter" 指 Alba。
   - 结论：md 的「妹妹 Alba」「姐姐」方向全部正确，未发现亲属方向反转。
2. **草地上躺着的两个女人**：原文 `text/ch10_chapter_10.txt:60`「Carmen, meanwhile, was stretched out on the grass several meters away.」＋ `:201`「Carlos looked for Diana and saw she was stretched out next to her mom, in the same position.」⇒ 是 **Carmen 与 Diana**，Alba 不在场；md `md:12`「两个被剖开肚子的女人躺在草地上」正确。
3. **谁在讲三十年前的事**：`text/ch10_chapter_10.txt:603`「"All right, I’ll tell you the camper story. I’m still traumatized."」＋ `:786` 的长引语是 **Diana** 在讲给 Carmen 听；md `md:11`／`md:14` 方向正确。`:801`「"Boy, you are a writer, aren’t you."」是 Carmen 的反应，`md:111`「母亲听到这一段的反应……先夸了一句她真会写」正确。
4. **「三十年」是谁说的**：`text/ch10_chapter_10.txt:327`「"Oh, come on—that was fifteen years ago, at least."」是 Carmen，`:330`「"Fifteen? More like thirty."」是 Diana ⇒ md `md:109`「三十年前没有人肯听，三十年后连听的人也不信」按 Diana 的口径成立。
5. **仪式在房车外，不在房车里**：`text/ch10_chapter_10.txt:636`「"They weren’t inside. They were sitting out in front."」＋ `:690`「They were out there sitting at that stone table on their lot…」⇒ md 未写房车内部，方向正确。
6. **目击者是 Diana**：`text/ch10_chapter_10.txt:795`「"Only you saw it?" Carmen asked…」＋ `:798`「"Yeah, that’s the weird part…」⇒ md `md:87`／`md:99` 归给 Diana，正确。
7. **「像绞肉机」属于谁**：`text/ch10_chapter_10.txt:156` 是 Juan 描述 **Carmen** 的腹部（「Like someone attacked her with an immersion blender and tried to cut her in half.」）⇒ md `md:39`「肚皮上全是血块」指的是母亲，正确；md 未把「四指宽」挪到 ch10（那是 ch08 的 Diana 伤口），无越界。
8. **报警与救护车**：`text/ch10_chapter_10.txt:168`、`:219`、`:759`、`:843`、`:849`、`:861` 反复谈 call the police / one-one-two，但本章未写警报已发出；md `md:154` 未称已报警，正确。
9. **本章 md 内的跨章指认**：md 正文无指向其他章的事件描述，唯一跨书事实是「胡安」这一中文名（见 W6）。

---

## 五、修后复核（改稿后按此复核）

1. 改 `md:14`「手镜」→「眼镜」；同句「取景框」→「挡光板」，「说破」→「看穿……却没说出口」。
2. 改 `md:57` 的两个「她」，点明有了孩子的是 Diana。
3. 改 `md:154`「母亲还是不信」→ 改为母亲的实际反应（夸她会写＋追问当年为什么不说）。
4. 改 `md:75`「对方人回来了」→「对方人虽然在这儿，心还留在那年夏天」。
5. 补 L1（血手印与车底血布）、L2（走散经过与 MediaMarkt）、L3（光柱与震动）、L4（露台是营地翻版，并点出块 6 属 Alba 视角转述层）、L5（父亲夜访）、L6（Carmen 说「她已经很多年没有单独待过了」）六处。
6. 统一本章 Juan 的中文名／西文名。
7. 复核命令（改完逐条跑，期望全部 exit=1 即无残留）：
   - `/usr/bin/grep -n '手镜' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"` → 期望无输出。
   - `/usr/bin/grep -n '取景框' "…/ch10 chapter 10.md"` → 期望无输出。
   - `/usr/bin/grep -n '母亲还是不信' "…/ch10 chapter 10.md"` → 期望无输出。
   - `/usr/bin/grep -cE '手印|车底|后备箱' "…/ch10 chapter 10.md"` → 期望 ≥1（补入 L1 后）。
   - `/usr/bin/grep -cE '光柱|震动' "…/ch10 chapter 10.md"` → 期望 ≥1（补入 L3 后）。
   - `/usr/bin/grep -cE '独处|单独' "…/ch10 chapter 10.md"` → 期望 ≥1（补入 L6 后）。

---

## 六、复核轮次二（2026-10-21 23:35，md 已按本单修过后复核）

- 受审 md 版本：`ch10 chapter 10.md` = 15676 字节 / 154 行 / md5 `ff482a9379f8144a8e63dddcb3116693`，对应 commit `d3c51a5b1`（23:14:19，「ch10 第二轮复核修复（挡光板/没说出口/她指代/走散经过/血手印/营地翻版/光柱震动/父亲夜访/独处断言/总结口径）」）；前一版 commit `33f74dfd5`（22:44:10，「胡安译名统一/三十年前为叙述者口径」）。
- 机器层复跑：`bash scripts/chapter.sh "…/ch10 chapter 10.md" --json` → 退出码 **0**，`verdict: ok`；`counts`：`struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`、`quote_long 0`、`template 0`、`hole 0`、`block_count 0`、`segments 8`、`segment_miss 0`；`form`：`h1_shape_ok true`、`nav_count 5`、`nav_count_ok true`、`blocks 8`、`block_median 7.5`、`block_range [5,8]`、`profile novels`、`baseline book`；引语字符位 [986, 8692, 13050, 15786, 20664, 25301, 39462, 41088] 与存档 `2-machine.json` 一致（复跑输出写临时文件，未覆盖存档）。
- 逐字复跑：自写脚本 `check_md_quotes.py`（ch10）→ 原句块 8 条全部命中，词汇例句 MISS 数 = 0。

### 本轮已销账（9 项）

| 原编号 | 状态 | 复核证据 |
|---|---|---|
| W1（阻断） | **已修** | `md:14` 现文「Diana 从**戴上眼镜**点数」——与 `text/ch10:6`「She took out her glasses and put them on」一致；`/usr/bin/grep -c "手镜" "…/ch10 chapter 10.md"` → 0，退出码 1。 |
| W2 | **已修** | `md:14` 现文「用双手**在眼前搭起挡光板**的旁观者」——与 `text/ch10:9`「Diana made blinders with her own hands—still bloodstained—so she could concentrate on that image」一致。 |
| W3 | **已修** | `md:14` 现文「Carlos 是**看穿**这家族病症、**却没说出口**的那个人」——与 `text/ch10:204`（叙述层认知）＋`:162`（Juan 的困惑）一致。 |
| W4 | **已修** | `md:154` 现文末句「讲完了，母亲只夸她会写，追问她当年为什么不说」——与 `text/ch10:801`「"Boy, you are a writer, aren’t you."」＋`:807`「"But you were always so scared. Why didn’t you say anything?"」一致。 |
| W5 | **已修** | `md:57` 现文「母亲曾花了多年催 **Diana** 长大、催她走出去闯荡；可 **Diana** 一有了孩子，母亲就忽然变得苛刻」——指代歧义已拆开，与 `text/ch10:210`「After her first child, Diana turned into a pumpkin」一致。 |
| W7 | **已修** | `md:75` 现文「她的意思是对方人**虽然在这儿**，心还留在那年夏天」——与 `text/ch10:384`「I think she’s still there.」一致。 |
| L1 | **已修** | `md:39` 现文「Juan 又招手让 Diana 和 Carlos 走近看车：车身溅满血，一个张开五指的血手印从一侧车门断断续续拖到后备厢；车底下露出一块像床单的东西，也浸透了血——那是他用来给母亲压住伤口的毯子」——与 `text/ch10:147`＋`:168` 一致。 |
| L2 | **已修** | `md:27` 现文「两人在商场里被人流冲散，手机在他手上；闭店广播响后 Alba 要去买没给孩子看的礼物，他「确信」她是折回 MediaMarkt 问 Switch 手柄」——与 `text/ch10:87`＋`:93`＋`:111` 一致。 |
| L3 | **已修** | `md:105` 现文补入「她能报出来的只有仪式的声音——像斧子、像肉铺切肉、水滴进塑料桶——和颜色：从桌面射起、越过树梢冲进天空的深粉近紫的光柱，以及随之而来的震动」——与 `text/ch10:792` 一致。 |
| L4 | **已修** | `md:81` 现文括注「（她那方露台本来就是营地的翻版：两把沙滩伞、便携泳池、沙滩冰箱、条纹躺椅，窗外就是 B-20 环城路。）」——与 `text/ch10:414`＋`:435` 一致。 |
| L5 | **已修** | `md:111` 现文补入「而在讲这一段之前，她刚跟母亲讲过另一件事：几天前的凌晨四点，她起夜时发现父亲来过家里，卫生间里是父亲抽完烟的味道，而且只在特定的日子出现」——与 `text/ch10:558/570/576/588` 一致。 |
| L6 | **已修** | `md:51` 现文补入「同一段对话里，母亲沉默很久后主动说出「她已经很多年没有单独待过了」，Diana 立刻坐直了：「你终于说出来了。」」——与 `text/ch10:276`＋`:282` 一致。 |

### 本轮新发现（阻断级，1 项）

#### F1｜`md:87`「读者是从 Diana 的讲述里，第二次看到那块广告牌」——本章原文里那块广告牌只出现过一次，且不在 Diana 的讲述里｜档：阻断

**原文侧**（`text/ch10_chapter_10.txt:438`，全章唯一一处广告牌，叙述层，Alba 视角）：

> Every night after dinner, Alba would go out to her patio. … And the beltway, the cars, the lights, the billboards. They hadn't updated those billboards in a long time. One was for the McDonald's drive-thru off of L'Hospitalet; the other was for a brand of sex toys. Days before Splau had swallowed her up, Alba went out to the patio, as she did every night. Her eyes traveled over the landscape, as always, but for some reason, she got stuck on the McDonald's ad. She stared at it for a long time, watched it transform. The yellow M on its red background liquefied, trickling downward and leaving behind just a white billboard with red text and a running turtle—the billboard for La Tortuga Ligera. Alba closed her eyes for a moment, and when she opened them, the ad for the campground was still there. She went inside and shut the curtains.

**md 侧**（`ch10 chapter 10.md:87`）：

> **读者视角提示**：这里她看见就回避：窗帘一拉上，回忆立刻倒回当年那个露营地的夏天。这段属于 Alba 视角的转述层——读者是从 Diana 的讲述里，第二次看到那块广告牌。

**取证命令（原样）**：
```
/usr/bin/grep -n "billboard" text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:438（唯一一处）；退出码 0
/usr/bin/grep -n "McDonald" text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:438；退出码 0
/usr/bin/grep -n "yellow M" text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:438；退出码 0
/usr/bin/sed -n '603,810p' text/ch10_chapter_10.txt > /tmp/dshreview/camper2.txt
/usr/bin/grep -niE "billboard|advert[a-z]*|McDonald" /tmp/dshreview/camper2.txt
→ 无输出；退出码 1（Diana 讲营地故事的整段 603–810 里没有广告牌）
/usr/bin/grep -nioE "billboard|advert[a-z]*|McDonald|sign[a-z]*" /tmp/dshreview/camper2.txt
→ 22:sign ／ 196:sign（分别是 :624「the sign taped to the door: Do Not Disturb. It's Bingo Night.」与 :798 的同一句），与广告牌无关
/usr/bin/grep -rn "McDonald" text/
→ text/ch10_chapter_10.txt:438（全书仅此一处）；退出码 0
/usr/bin/grep -rn "yellow M" text/
→ text/ch10_chapter_10.txt:438（全书仅此一处）；退出码 0
```

**影响**：三处对不上。① **「第二次看到」无出处**——本章原文里 McDonald's 广告牌与化开的黄色 M 各只出现一次（都在 `:438`），读者此前从未见过它，谈不上「第二次」；② **「从 Diana 的讲述里」与叙述层不符**——`:438` 是叙述者直接写 Alba 的动作（Alba 走出去、盯住广告牌、闭眼、拉开窗帘），并不是 Diana 在讲给母亲听；Diana 讲的那段是三十年前的营地仪式（`:603` 起），两者之间没有「同一块广告牌」的呼应；③ 若读者据此去找「第一次看到那块广告牌」的位置，会落到 Diana 的营地故事里，而那里根本没有广告牌（camp story 段 603–810 内 billboard / advert / McDonald 命中 0），只有房车门上「Do Not Disturb. It's Bingo Night.」那块牌子。

**修法**：`md:87` 末句改为「这段属于 Alba 视角的转述层——广告牌的异变发生在本书开篇前，读者在这里第一次看到它；母亲听到的是 Diana 讲的另一件事：那年的营地。」

### 本轮其余未修项（提示级，1 项）

#### E1｜同章内 Alba／阿尔巴、Carmen／卡门、Diana／戴安娜混用｜档：提示（体例）

**md 侧**：`md:11`、`md:19`、`md:27`、`md:79`、`md:87` 用「Alba」，`md:81` 用「阿尔巴」；`md:11`–`md:15`、`md:57`、`md:133` 用「Diana」，全书该角色在 ch01–ch13 多用 Diana、ch14–ch17 多用戴安娜；`md:12`、`md:15`、`md:27`、`md:39`、`md:51` 用「Juan」，ch14/ch17 用「胡安」；`md:11`–`md:15`、`md:39` 用「Carmen」，ch14/ch15 用「卡门」。

**取证命令**：
```
/usr/bin/grep -c "Alba" "…/ch10 chapter 10.md"   → 5
/usr/bin/grep -c "阿尔巴" "…/ch10 chapter 10.md"  → 1
/usr/bin/grep -c "Juan" "…/ch10 chapter 10.md"   → 5
/usr/bin/grep -c "胡安" "…/ch10 chapter 10.md"    → 0
/usr/bin/grep -c "卡门" "…/ch10 chapter 10.md"    → 0
```
**影响**：全书体例本身就混用（ch02/ch05/ch13/ch17 用 Carmen，ch14/ch15 用卡门；ch14/ch15/ch16/ch17 用戴安娜，其余章用 Diana），所以这不是新引入的错误；但同一章内「Alba」与「阿尔巴」并存，读者要在两种写法之间自行判断是同一个人。

**修法**：本章内统一即可（建议随 `md:11` 保留 Alba，把 `md:81` 的「阿尔巴」改成「Alba」），全书其余章维持既有体例不动。

### 本轮复核命令（原样）

```
/usr/bin/grep -c "手镜" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1（W1 已修）
/usr/bin/grep -c "取景框" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1（W2 已修）
/usr/bin/grep -c "说破" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1（W3 已修）
/usr/bin/grep -c "母亲还是不信" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 0；退出码 1（W4 已修）
/usr/bin/grep -cE "手印|车底|后备箱" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 2（md:39）；退出码 0（L1 已修）
/usr/bin/grep -cE "光柱|震动" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 1（md:105）；退出码 0（L3 已修）
/usr/bin/grep -cE "独处|单独" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 1（md:51）；退出码 0（L6 已修）
/usr/bin/grep -c "父亲" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 1（md:111）；退出码 0（L5 已修）
/usr/bin/grep -c "第二次看到那块广告牌" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ 1（md:87）；退出码 0（F1 仍在）
```

### 本轮结论

- 上一轮 W1 阻断已由 `d3c51a5b1` 修掉（`md:14`「手镜」→「眼镜」）。
- **本轮新发现 1 条阻断**：`md:87`「第二次看到那块广告牌」——本章 McDonald's 广告牌只出现一次（`:438`），且在叙述层而非 Diana 的讲述里；已附 `text/ch10_chapter_10.txt:438` 原文逐字与全部取证命令。
- 其余 1 项（E1 译名体例）为提示级。

---

## 七、复核轮次三追加（2026-10-21 23:52）：`md:154`「谁都不肯让别人看」与原文相反

### F2｜`md:154`「她和母亲身上各自带着一道腹部伤口，谁都不肯让别人看」——原文里两人先后都给对方看了伤口｜档：阻断

**md 侧**（`ch10 chapter 10.md:154`）：

> 平安夜商场关了门，妹妹走丢，她和母亲身上各自带着一道腹部伤口，谁都不肯让别人看；母亲躺在草地上玩消除游戏，女儿趁这个夜晚把当年隔着灌木看见的那场仪式从头讲了一遍——讲完了，母亲只夸她会写，追问她当年为什么不说。

**原文侧**（`text/ch10_chapter_10.txt:216`，**Diana 先给母亲看**）：

> "I don't think so. She must have just gotten sidetracked as she was leaving. She's probably on her way out now." Diana looked at her mother and now saw the bloodstains on her parka. She leaned forward so she could see better, then opened her coat and lifted her sweater. Carmen didn't resist. A wound just like hers, dark and fresh, ran across her stomach. She said nothing and covered it back up.

**原文侧**（`text/ch10_chapter_10.txt:726`，**Diana 第二次给母亲看**）：

> "My stomach. I have the same thing you do." Diana lifted her sweater to show her mother her wound.

**原文侧**（`text/ch10_chapter_10.txt:732`，**母亲也掀起衣服给 Diana 看**）：

> "It's nothing? Mom, Jesus, it looks awful. Let's see yours." She slid the parka off of her and lifted up her sweater. "It looks like it's getting worse. Maybe we should go to the hospital. Or the clinic. Is it open?"

**原文侧**（`text/ch10_chapter_10.txt:903`，**Carlos 后来要看被拒**）：

> Carlos tried to lift her sweater to check, but Diana stopped him, pushing his hand away.

**取证命令（原样）**：
```
/usr/bin/grep -nE "didn't resist|show her mother|Let me see|see yours|lifted up her sweater" text/ch10_chapter_10.txt
→ text/ch10_chapter_10.txt:21「"Let me see."」
→ text/ch10_chapter_10.txt:63「"Let me see your stomach again," Carlos said, trying to lift Diana's sweater.」
→ text/ch10_chapter_10.txt:69「"Let me see, the kids aren't looking."」
→ text/ch10_chapter_10.txt:726「"My stomach. I have the same thing you do." Diana lifted her sweater to show her mother her wound.」
→ text/ch10_chapter_10.txt:732「"Let's see yours." She slid the parka off of her and lifted up her sweater.」
退出码 0
/usr/bin/awk 'NR==216 {print $0}' text/ch10_chapter_10.txt
→ "…opened her coat and lifted her sweater. Carmen didn't resist. A wound just like hers, dark and fresh, ran across her stomach. She said nothing and covered it back up."
/usr/bin/awk 'NR==903 {print $0}' text/ch10_chapter_10.txt
→ "Carlos tried to lift her sweater to check, but Diana stopped him, pushing his hand away."
/usr/bin/grep -nE "不肯|不让|拒绝|撩起|掀开" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md"
→ md:154（唯一一处）；退出码 0
```

**影响**：「谁都不肯让别人看」把本章两场**互相展示伤口**的戏整个抹掉了。原文里母女二人在草地上先后撩起衣服给对方看——Diana 先是俯身掀开自己的毛衣、看见母亲伤口「和她自己的一模一样」（`:216`），后来又撩起毛衣给母亲看，说「我和你一样」（`:726`），母亲也回手掀起自己的衣服让她看（`:732`）。真正「不肯让人看」的是**母亲对 Carlos**：她拒绝起身、拒绝上车、拒绝让人把她抬起来（`:858`「I'm not going anywhere until I've seen your sister myself.」／`:876`「I'm not moving.」／`:879`–`:880`「When they reached under her arms to lift her, she went limp.」），以及 Diana 对 Carlos 的拒绝（`:24`「"No."」／`:66`「"Stop! I told you, I'm fine," she said, swatting his hand away.」／`:903`）。md 的一句总结把「谁都不肯让别人看」安在母女两人身上，恰好写反了本章关系最松的一处。

**修法**：`md:154`「她和母亲身上各自带着一道腹部伤口，谁都不肯让别人看」改为「她和母亲身上各自带着一道腹部伤口，两人在草地上先后撩起衣服给对方看，而谁都不肯让 Carlos 插手」。

### 本轮结论

- **本章现有 2 条阻断**：F1（`md:87`「第二次看到那块广告牌」，见第六节）与 F2（`md:154`「谁都不肯让别人看」，见本节）。两条均附 `text/ch10_chapter_10.txt` 行号＋原文逐字＋取证命令，满足 R5 硬约束。
- F2 是轮次三新增；轮次二那 12 条提示项与 F1 的修法建议不受影响。
