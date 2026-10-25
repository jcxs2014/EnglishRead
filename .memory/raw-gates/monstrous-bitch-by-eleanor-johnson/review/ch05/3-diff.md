# ch05 对账（R3）

素读：`1-suread.json`（8 条，全部带 `text/ch05_3_roman_witch_bitches_the_persistence_of.txt:行` + 逐字 + 字符区间，子代理已脚本校验 `count==1`）。
机器：`2-machine.json`（rc=0，15 块，引语 15 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 284 行，15 块 + 词汇 26 条。原文 231 行 / 48,051 字符（去空白，实算一致）/ 9,424 词。

## 一、漏（素读有、md 无）

无。素读 8 条全部有落点：

| 素读事实 | md 落点 |
|---|---|
| L20 Lex Julia 授权父亲杀通奸女儿 | 概览 L18、结构列表 1、词汇表 `Lex Julia` |
| L39 贺拉斯《长短句集》第 5 首、卡尼迪亚等四女巫埋男孩取肝 | 原句 3–4、结构列表 2 |
| L53《埃涅阿斯纪》以击败狄多为代价建罗马 | 原句 5、概览 L18 |
| L62 第七卷阿莱克托抛蛇缠阿玛塔 | 原句 6–7、结构列表 6 |
| L114 卢坎《法萨利亚》埃里赫托造僵尸先知 | 原句 8、概览 L18 |
| L129 本章转折＝女巫「整合与正常化」 | 概览 L18、原句 9、证据链 |
| L143《金驴记》墨罗厄与潘西亚刺穿苏格拉底脖颈接血 | 结构列表 7、原句 11 邻域 |
| L158 lamia 已成普通名词 | 原句 11、结构列表 8 |

## 二、编（md 有、原文无）

无。逐条核过：

- 「卢坎的埃里赫托收下塞克斯图斯的报酬、把他放走」←「Erichtho simply **takes her payment from Sextus and sends him away**」
- 「连最高家长神朱庇特都对她无能为力」←「**The ultimate paterfamilias, Jove himself, holds no terrors for her**」
- 「她用三个短语收尾：生育的伤害、性的伤害、施巫的伤害」←「**Reproductive harm, sexual harm, spellcasting harm.**」
- 「狄多与卡米拉都因为太强而必须死，只有拉维尼娅因为子宫而活」←「Lavinia lives because **her womb represents the right to Roman lands** … so she gets a pass」＋Dido/Camilla 两段
- 「父亲可以因轻微罪过杀女儿」←「Roman fathers could—and did—kill their daughters for **fairly minor infractions**」
- 「Obyzouth 与 Gello」「Äl」← 原文同名段落，未改拼写

## 三、错（两边都有但不一致）

### 1. 【提示】《尤利娅法》的管辖范围在概览里被写宽了

- md:18「罗马丈夫可以因通奸合法杀妻，父亲可以因轻微罪过杀女儿，**《尤利娅法》把女性的性命直接写进家族法**」
- 原文：「Roman fathers could—and did—kill their daughters for fairly minor infractions: Augustus Caesar's legal code, the **Lex Julia, allowed fathers to slaughter their daughters if the daughters committed adultery** … a father could murder a daughter not only for adultery but for nearly any action that qualified as sexual turpitude.」
- 判断：Lex Julia 管的是「女儿通奸／性失节」这一档，不是笼统「把女性性命写进家族法」；md:44 的证据链写法（「把杀女写进法条」）是准的，概览这句过宽。降档提示，改法：`《尤利娅法》把父亲杀通奸女儿写成合法`。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch05 报出的行全部人读（①相对章号、②绝对断言、③数字、④亲属、⑤方向）；另对 `Lex Julia / proliferat / diminution / paterfamilias / adultery / Sextus / Jupiter / payment / Camilla / damages of` 十个关键串做了定位与上下文打印（脚本在 `/tmp/t3mb/`，未落 raw-gates）。
