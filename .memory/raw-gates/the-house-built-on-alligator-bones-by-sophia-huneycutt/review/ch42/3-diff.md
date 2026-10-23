# ch42（Chapter Forty-One）R3/R4 差异与取证

## 探针

| 探针 | 结果 |
|---|---|
| v42（词表例句逐字） | 25 行，flagged 1（batshit）→ F-42-1 |
| ap42（直撇号＋backtick span） | ASCII 撇号 0，span MISS 0 |
| in42（非块内嵌英文） | 未命中 3，模板 2（`Chapter Forty-One`／`Tropes`）＋`rotten to the core`（→F-42-2） |

## 假红取证

- **F-42-1**：`/usr/bin/grep -n "batshit" text/ch42_chapter_forty_one.txt` → L99 "Gazzie’s batshit crazy. Has anger issues. But she’s also funny. And passionate." rc=0。词表例句在 "And passionate." 截断并补了收尾引号 ”，flat 后串含 ” 而原文该处无闭引号（句子延续 "And she does care about people…"）——例句截断型，词头与内容均逐字有据。
- **F-42-2**：`/usr/bin/grep -rn "rotten" text/` → 本章无；text/ch41_chapter_forty.txt:144 "Said we were rotten to the core, herself included."（Caroline 判词）——原句6「为什么这样写」跨章回指上一章，有据。

## 定点取证（/usr/bin/grep，text/ch42_chapter_forty_one.txt）

- L9 Honda／foot-long crack／storm shutters／plywood／alligator-skulled skeleton key；L21 hurt over a million alligators；L27 imagined rifle／coal-black／Something clicked—her rifle；L30 "Haints didn't sit on couches."
- L45 watery red paint／break the façade；L51 storm shutters／cleanup crew；L57 "Oh, she told me to get out."／waited on the patio；L66 so tired of being angry；L87 "therapeutic slaughtering"。
- L99 started to like her／batshit crazy；L102 "her only adviser is a stone-cold bitch of a haint"；L108 manslaughter／fifteen or twenty years tops／more stable。
- L132 vase 白蓝瓷瓷瓶坠落／sunning alligator halved；L135 empire／dominate nature in the cruelest way possible。
- L144 "It's possible…It's not like she's a psychopath."；L162 "My mother technically died of a heart attack."；L183 "Then maybe you shouldn't," coldly。
- L204 "Why are you telling me this?"；L213 "An evil person wouldn't regret their actions"…He didn't return to the couch。
- L240 "This family is all I have."；L270 repeated；L273 "You have me."；L276 "to keep me out of the storm"；L348 "They shouldn't have."
- L315 "I don't usually let people take me for a fool."

## 导航断言

全部回源命中（见上）；原句1–10 引语逐字（s42 20 facts MISS 0＋机器层 segment_miss 0）。
