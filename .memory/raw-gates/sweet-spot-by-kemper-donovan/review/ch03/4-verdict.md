# ch03 判定表（R5）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 姐姐（非妹妹）二十五年前自杀 | `text/ch03_chapter_33.txt:100` `I was two years younger` | 原写「妹妹」有误，已改「姐姐」 | 阻断（已修） |
| 2 | `I'm engaged` 未成块 | `text/ch03_chapter_3.txt:70` | 关键句未引，块数已满无法补 | 提示 |
| 3 | 周五晚撒骨灰未成块 | 本章对话段 | 关键设定未引，块数已满 | 提示 |
| 4 | 15 块引语逐字 | `2-machine.json` 15/15 ok | 通过 | — |
| 5 | 「哇，太好了，恭喜」确为原文 | `ch03_chapter_3.txt` `“Oh wow! That’s amazing, congratulations!”` | 通过（非编造） | — |
| 6 | 关键词均在本块引语内 | bracing/Google Imaging/sap my libido/ahead of time；They attract/herky-jerky/gastro-cardiac/vital organs；…；Boy Scout/Earl Grey/marginal humiliations | 通过 | — |
| 7 | 施事三问 | 原句 1–15 主语为她本人，或明确为她所引 Denny / Abi 的话 | 通过 | — |
| 8 | 「骗局/招待」类细节 | 原句 15 的 Earl Grey 漏收钱、她解释早到先吃一轮 | 与原文一致 | — |

## 已核实为正确
- 原句 3「deluge rather than a shower」的水喻升级，与原文 `a deluge rather than a shower, and nothing cleansing about it` 一致。
- 原句 6「yoking my words to their high-profile plow」译为「套在别人犁上的牲口」，正确。
- 原句 10「regularly」拆掉她的惊讶表演，与 `I looked up Denny regularly` 一致。
- 原句 12 三个坐标（二十年前 / 十四岁 / 刀抵喉咙）与原文一致。
- 原句 14「五月中旬」＝`middle of May`；「Sweet Spot 第一次以地名从她嘴里出现」成立。
- 原句 15「童子军名誉」「Earl Grey」「marginal humiliations」逐字在引语内。
- 词汇 17 条例句均可逐字回 `text/ch03_chapter_3.txt`。
- 已改 1 处（妹妹→姐姐），`chapter.sh` EXIT=0。
