# ch01 R4 判定表

覆盖声明：R1 素读（先 text 后 md）→ R2 chapter.sh --json（rc=0）→ R3 对账 → R4 逐块 12/12。

| 断言 | 证据（text/ 区间） | 结论 | 档位 |
|---|---|---|---|
| 原句1 中文理解「15 岁/一见钟情/英俊尸体」 | "at fifteen...swooning over a handsome corpse in uniform"（区间 128–262） | 与原文一致 | 正确 |
| 原句2「祖母/隧道/骑士团」 | "living beneath the city in the network of old tunnels"（798–893） | 一致；读者视角引祖母语「Life will surely wear that passion down」逐字在原文 | 正确 |
| 原句3「麦芽糖/小酒吧/英国人为主」 | "The foreigners were predominantly British...barley sugar"（1691–1900） | 一致 | 正确 |
| 原句4「Gina 父母+哥哥 2 月亡」 | "Her parents and older brother...February"（4700–5100） | 施事正确（德军炸弹；"a single German bomber"） | 正确 |
| 原句5 中文理解「五百年前骑士团」 | "Five hundred brave Knights"=骑士人数；"sixteenth century"=时代 | **数字/年代错** | **阻断→已修**（4948be8d8） |
| 原句6「mantra/hope」 | "I won't let the Germans take my hope"（8983–9019） | 一致 | 正确 |
| 原句7「9 月婚期/slump」 | "that was September...Right after you turn sixteen"（11870–12040） | 一致；「换一个 Falzon」对应 "If I had no choice but to marry a Falzon, it would be you" | 正确 |
| 原句8「rooted/dare Fate」 | "as if she was meant to dare Fate"（17070–17170） | 一致 | 正确 |
| 原句9「finger-four/酒吧偷师」 | "she'd interrogated one of the airmen in her father's bar"（19900–20200） | 施事正确（她问、飞行员答） | 正确 |
| 原句10「德国人听见祈祷→锁定→命中」 | "it was the German pilot who heard her plea. He was the one who got the bead"（23350–23600） | 施事链正确（德机 get the bead，Spit 被击中） | 正确 |
| 原句11「头垂/likely dead/溺亡」 | "his head was slumped...he would surely drown"（25600–25780） | 一致 | 正确 |
| 原句12「could not allow/Valentina ran」 | "She could not allow that...Valentina ran."（25710–25913） | 一致 | 正确 |

## 修复记录

- 阻断 1：原句5「五百年前」→「十六世纪五百名骑士两度顶住奥斯曼围攻」（数字→年代误读）。
- 提示 2：①原句3「全部来源」绝对化→「日常来源」；②Stuka 坠海细节未入块（取舍可接受，记档不改）。

## 关键词/引语长度抽检

- 12 块关键词全部在本块引语内（gate lane ④ rc=0）✅；引语 17–58 词，全部 ≤100 ✅。

## 已核实为正确

以下写法回原文核对后成立，后续不得以「读着不对」为由改动（除非给出反证）：
1. 原句2 读者视角引祖母语「生活会磨平这份激情」——原文 "‘Life will surely wear that passion down,’ the older woman had said to Valentina's mother"（text/ch01 区间 406–520）。
2. 原句4「Gina 的父母和哥哥」——原文 "Her parents and older brother had been at the afternoon matinee"（older brother=哥哥）。
3. 原句10「德国人『听见』她祈祷」——原文 "it was the German pilot who heard her plea"（反讽修辞，非错归）。

结论：ch01 修复后机器层 rc=0，人判层 12/12 块对应成立。**已核实为正确**。
