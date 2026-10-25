# ch04 对账（R3）

素读：`1-suread.json`（8 条，全部带 `text/ch04_2_greek_monstrous_bitches_screaming_furi.txt:行` + 逐字 + 字符区间，子代理已脚本校验 `count==1`）。
机器：`2-machine.json`（rc=0，15 块，引语 15 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 288 行，15 块 + 词汇 21 条。原文 284 行 / 51,813 字符（去空白，实算一致）/ 10,133 词。

## 一、漏（素读有、md 无）

无。素读 8 条全部有落点：

| 素读事实 | md 落点 |
|---|---|
| L20 公元前五世纪雅典悲剧的范式西传 | 概览 L18、原句 1 |
| L66 复仇女神连宙斯都受制 | 原句 4、证据链 |
| L48 克吕泰涅斯特拉浴中刺杀阿伽门农 | 原句 3、结构列表 4 |
| L136《俄瑞斯忒亚》与《恩玛·艾利什》同构 | 概览 L18、原句 13 邻域 |
| L161 美狄亚毒袍烧死公主与国王 | 结构列表 14、原句 9 邻域 |
| L167 杀子＝怪物性落到人间女子 | 原句 9、原句 10 |
| L230 阿伽维肢解彭透斯 | 原句 12、原句 13 |
| L262 拉弥亚公元前六世纪、上半身女人下半身蛇 | 原句 14、结构列表 15 |

## 二、编（md 有、原文无）

无。逐条核过：

- 「雅典娜根本不曾经过女人的身体」←「the one goddess in the Greek pantheon who was **born from a male alone**」（概览、原句 6 中文理解）
- 「布里斯埃伊斯」←「He bullied his troops, he **stole Achilleus's concubine Briseis** and enslaved her」（结构列表 4）
- 「佩利亚斯／谋害」←「Medea **conspires to bring about the death of** another king, King Pelias of Iolcus」（结构列表 14）
- 「肢解亲兄」←「Medea chops up her brother and throws his body parts into the sea」（结构列表 14）
- 「为她写过一整部戏却只剩一句台词」←「That contribution was a play called Lamia. … **only one line of this play survives**」（概览 L18）
- 「地母／看门狗」←「The bloodsucking, flesh-eating, vengeful, loudmouthed might of the **doglike** Furies is domesticated, banished, exiled, and controlled」（概览 L18）

## 三、错（两边都有但不一致）

### 1. 【提示】「美狄亚是这一章唯一来自东方的女性形象」把范围说绝对了

- md:150（原句 7 的「为什么这样写」）：「美狄亚是这一章唯一来自东方的女性形象」
- 原文只说「**Medea's Easternness is not incidental**; Euripides is leveraging the latent Greek cultural awareness…」，并未说她是本章唯一非希腊出身的形象——同章末节还写拉米亚「born in Libya」（原句 14 引语内）。
- 判断：「东方性被作者着意利用」这一点成立且只落在美狄亚身上；但「唯一来自东方」与拉米亚的利比亚出身相抵。改法：`美狄亚是这一章唯一被作者着意点明「东方性」的女性形象`。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch04 报出的行全部人读（①相对章号、②绝对断言、③数字、④亲属、⑤方向）；另把 `1-suread.json` 8 条逐条回原文比对，并对 `Athena / born from a male alone / Briseis / Pelias / conspires / Lamia one line / brother / longest` 八个关键串做了定位（探针在 `/tmp`）。
