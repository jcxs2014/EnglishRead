# ch03 对账（R3）

素读：`1-suread.json`（8 条，全部带 `text/ch03_1_monstrous_bitches_of_ancient_mesopotam.txt:行` + 逐字 + 字符区间，子代理已脚本校验 `count==1`）。
机器：`2-machine.json`（rc=0，15 块，引语 15 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 279 行，15 块 + 词汇 22 条。原文 300 行 / 42,752 字符（去空白，实算一致）。

## 一、漏（素读有、md 无）

无。素读 8 条全部有落点：

| 素读事实 | md 落点 |
|---|---|
| L26 横向万神殿 → 以马尔杜克为唯一主导神的原初一神教 | 概览 L18、结构列表 3、原句 2 |
| L37 拉玛什图杀孕妇、吸胎儿、屠新生儿 | 结构列表 5–6、原句 4 |
| L40 公元前第二千纪初定型、咒语更早、比马尔杜克古老 | 结构列表 5、原句 10 语境 |
| L107 阿努之女因 `malevolent will` / `base counsel` 被逐 | 结构列表 8、原句 5、原句 7 |
| L204 转向提亚马特、二人有隐蔽关系 | 结构列表 11、原句 13–14 |
| L212 约公元前 1100 年、七块泥板 | 概览 L18、结构列表 11、原句 10 |
| L248 碎尸造地 | 结构列表 11、证据链、原句 12 邻域 |
| L297 莉莉图与拉玛什图融合成「超级怪物母狗」、性/生育/声音三特征 | 结构列表 12、原句 15 |

## 二、编（md 有、原文无）

无。逐条核过的具名细节全部有原文：

- 「接生婆的伪装」←「She masquerades as a midwife」；「喂奶的邀请」←「She suckles piglets and puppies at her own breasts」（结构列表 10）
- 「狼形外貌」←「Lamashtu is wolflike in appearance」（结构列表 10、原句 8）
- 「子宫与喉头」←「Her power resides dually in her womb and in her larynx」（概览 L18；比「嗓音」更精确）
- 「强暴至死」←「Symbolically, then, Marduk rapes Tiamat to death」（证据链、原句 12）
- 「大胆与贪婪」←「her outspokenness and rapacity」（原句 7 中文理解）
- 「超级怪物母狗」←「a kind of **Uber Monstrous Bitch**」（概览 L18；Uber＝超级，不是自造）

## 三、错（两边都有但不一致）

### 1. 【提示】「一神教」丢掉了原文的 `proto-`

- 原文：「gave way to a **proto-monotheistic** religion, in which there was one god who was clearly primary and dominant over all the others」；随后一句才是「This shift toward **monotheism** in religion correlated with…」。
- md:18「马尔杜克被抬为**一神教**的主宰」、结构列表 3「被抬为唯一主神」。
- 判断：原文用 `proto-monotheistic` 是为强调「尚未完成的一神教」，后一句的 `monotheism` 是简称；md 只取后者，少了「原初/雏形」。不影响论证方向，判提示。

### 2. 【提示】原句 13 的中文理解把引语之外的前一句也译了进来

- 引语从 `Tiamat was scary in theory` 起；md 的中文理解从「人们继续生活在对拉玛什图的恐惧里…」起，这一段对应的是**前一句** `People continued to live in fear of Lamashtu in a way they appear not to have lived in fear of Tiamat—who was, of course, dead and buried beneath their feet, offering them ground to stand on.`
- 判断：内容不错，但属「引语选短了」；中文理解宜从引语起点开始译，前一句可留给「表达方式」交代。降档提示。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch03 报出的行全部人读（①相对章号、②绝对断言、③数字、④亲属、⑤方向）；另把 `1-suread.json` 8 条逐条回原文比对，并对 `proto-monotheism / scribes / womb / larynx / rape / splits / midwife / wolf / Lilitu / Uber Monstrous Bitch` 十个关键串做了定位与上下文打印（探针在 `/tmp`，未落 raw-gates）。
