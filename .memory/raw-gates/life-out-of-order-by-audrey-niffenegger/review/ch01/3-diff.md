# ch01 对账（R3）

素读：`1-suread.json`（10 条，全部带 `text/ch01_the_last_party.txt:行` + 逐字，已脚本校验 10/10 命中本行）。
机器：`2-machine.json`（rc=0，块数 10，引语 10 段全 ok，segs 10 / miss 0，空引号 0，结构 0；`block_hint` 提示块数 10 略高于本书中位 6）。
md 155 行，10 块 + 5 条导航 + 词汇 17 条。

## 一、漏（素读有、md 无）

### 1. 【阻断】章首抬头里的三个 Alba 只落了一个，且把两个「年长 Alba」并成一人

- 原文抬头（逐字）：`text/ch01_the_last_party.txt:18`
  「Monday, December 26, 2022, and Tuesday, December 27, 2022 (Alba is 21, 29, and 47, Zach is 22)」
- 原文还有一处明写这是**两个不同的年长版本**：`:1925`
  「My other self is fully dressed, but not in Caralora’s clothes. I look at her more carefully and realize that **she’s older than the self we were with earlier**; her hair is going gray.」
  （即：藤椅/床罩那位是 2031 年来的 29 岁版；地下室灰发那位更老 = 47 岁版。）
- md 侧：`ch01 the last party.md:11` 只写「同屋里还坐着**一位**从 2031 年旅行回来的年长 Alba」；`:15` 引抬头时停在日期，**把「(Alba is 21, 29, and 47, Zach is 22)」整段省掉**；全文无 29、无 47、无 Zach 22 岁（`/usr/bin/grep -nE "2031|29|47|22 岁" ` 仅命中 `:11`、`:155` 两处「2031」）。
- 后果：读者以为全场只有「21 岁 + 一位年长版」；而结尾「That was me…I'm on my way to help a friend」（`:2008`）与地下室灰发版的存在都失去落点。抬头级数字按作业单要求是必抄项。

### 2. 【提示】四处细节未落（不阻断，但都是可补的一句）

| 细节 | 原文 | md 侧 |
|---|---|---|
| Zach 的来历 | `:586`「Tulsa. I moved to Chicago four years ago.」；`:670`「Seventeen and thirteen. RaeAnn and Suellen.」 | 只写「Junior 带来的」「自称服务生、刚烧掉小说」（md:11、md:14），无 Tulsa、无两个妹妹 |
| Nadia 为何懂时间旅行 | `:877`「Like the doctor who first discovered time-travel genes?」｜`:881`「She’s his daughter」 | 全章未提 Kendrick / Chrono-Displacement Disorder；`grep -nE "Kendrick|Chrono" ch01*.md` 无命中 |
| 父亲之死的日期与职业 | `:698`「He got shot. On New Year’s Eve. It was 2006 turning into 2007.」；`:708`「He was a librarian at the Newberry Library.」 | 只有「丧父」（md:11）、「活不到四十四岁」（md:65 解读），无日期、无 Newberry |
| 被抬走的五人姓名 | `:1954`「Junior, Buddy, Art, Rick and Terry」 | 只写「Junior 等五人」（md:11） |

## 二、编（md 有、原文无）

### 1. 【提示】「死在医院」

- md:11「她在示威中打倒的警察一周后**死在医院**」。
- 原文 `:1711`「Hyde Park demo—she hit a policeman with her sign when he grabbed her from behind. **He died of brain hemorrhage a week ago.**」
- 原文只说脑出血死、一周前；**没有医院**，也没说她把人「打倒」（hit with her sign）。地点与动作强度都是 md 加的。属小细节添加，判提示。

## 三、错（两边都有但不一致）

### 1. 【提示】「三段带名字的第一人称声部（Alba—Zach—Alba）交替」——实为 7 段

- md:15「三段带名字的第一人称声部（Alba—Zach—Alba）交替，同一夜被两个人各写一遍」。
- 取证：`/usr/bin/grep -nE "^(Alba|Zach):" text/ch01_the_last_party.txt` → 命中 **7 行**：`:23 Alba`、`:194 Zach`、`:204 Alba`、`:1267 Zach`、`:1476 Alba`、`:1864 Zach`、`:1883 Alba`（`grep -c` = 7）。
- 声部是 2 个，段落是 7 段，不是 3 段。属形态断言错，判提示。

### 2. 【提示】「全屋人替她演一场正常派对」——满屋客人并非同谋

- md:13「Nadia 以女友身份贴住 Junior，**全屋人替她演一场正常派对**」。
- 原文 `:158`「The place is packed with people **I don’t recognize**. If I didn’t know better I’d think that Nick and C-lora have made a new set of friends—whiter friends…」；`:159`「I wonder where all these people came from—did we hire actors?」；`:1911`「all these sleeping people are more than asleep; Nadia catches my glance and makes the sign for a **spiked drink**」。
- 即：客人是 Junior 那一圈陌生人，后来被下药放倒，既不知情也不是演员。参与行动的只有 Nick、Caralora、Gomolinski 兄妹、Alba、Zach 这几个。判提示（叙述范围夸大，非情节捏造）。

## 四、R4 逐块对应（10 块）

| 块 | 引语（text 行） | 这段中文是不是在讲这句引语 | 三问要点 |
|---|---|---|---|
| 1 | `:23` 前二句 | 是。母亲端饭—退出—不逼问，全在引语里 | 主语 Mama / 受事 Alba；「连拒绝都被允许」＝`let me be` |
| 2 | `:35` 前三句 | 是。琴的身份（祖父的 Guarneri）→ 不碰 → 不知拿那些钟点怎么办 | 「技艺还在」是 md 加的转述，未离题 |
| 3 | `:104` 全句 | 是。戒严/宵禁时间窗 + 「不想让我们的计划失败」 | 主语 we/she；「一小时内进屋」＝`be indoors in an hour` |
| 4 | `:199` Zach 声部 | 是。维多利亚女家庭教师比喻、浓妆、病白脸 | 观察者 Zach，被看者 Alba——方向没反 |
| 5 | `:537` | 是。不能说「上周刚见过没死的爸」；活不到 44 岁 | 受事＝父亲；「她能说出口的只有一句「记得」」对应上一轮 `Yeah . . .` |
| 6 | `:1144` | 是。藤椅、橙黄印花床罩、两人都冷、脚边盘子和保温瓶 | 「未来的人没有体面的衣服」是对 bedspread 的合理读法 |
| 7 | `:1238` | 是。宵禁、不能解释议程、不能让她当见证人、唯一的黑人、所以下药 | 说话人 Max；受事 Lucinda；「十六岁」见 `:1140`「much younger than sixteen」 |
| 8 | `:1398` | 是。四个 you 从句＝逃童年/要冒险/乐观务实/修烂东西 | 说话人年长 Alba，对象 Zach；「也是她自己未来会嫁的那个人」属解读 |
| 9 | `:1936` | 是。白衣人、无脸、像人形空白、从屏幕这头到那头 | 主语 figures；观看者＝地下室的人 |
| 10 | `:2116` | 是。回去只为有地方躲、把被子拉过头顶等难过变睡 | 主语 I；与开头床上呼应 |

密度：10 块中文理解 80–110 字量级（`2-machine.json` `blocks[].cjk` 全 >60），无一块只复述字面。
