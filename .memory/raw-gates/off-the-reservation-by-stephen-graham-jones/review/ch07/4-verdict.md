# ch07 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，11 块 11 引语，issues 全空。
R4 人判：11/11 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块9 读者视角「Seine 已悄悄给某人发过定位」 | text/ch07:428「"st p ng MSP"—Minneapolis-St. Paul…how you text when all you have is a number pad」 | 字面有据；「定位」措辞过度具体（短信文本≠GPS），「给某人」为推断 | 提示（不修） |
| Mooch 真名 Rita Kills-in-the-Water 未入 md | text/ch07:278「"Rita Kills-in-the-Water…"」；/usr/bin/grep -rn "Rita" text/ → 仅 ch07:278 与 ch03:95（同事名单）；md 全查无 | 一次性揭示、后文不用，漏不造成障碍 | 提示（不修） |
| 「博物馆台阶/秘密英雄/幻境 Sebby」场景未入块 | text:22182 anchor 命中；后文「using his hand to tell Sebby to stay」 | Nate 想象版本，非主线转折 | 提示（不修） |
| 断舌揭示与六银钉 | 素读#7（六颗银色圆头钉、上二下四构成脸）与导航「六颗银钉拼成的脸」 | 一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -n "MSP\|st p ng" text/ch07_6_roadkill.txt` → 行428；退出码 0
- `/usr/bin/grep -rn "Rita" text/` → ch07:278、ch03:95；退出码 0
- `/usr/bin/grep -c "cowboy" …`（前章同法在本章未用）；素读 anchor 偏移验证 True ×8

## 已核实为正确

- 块4 Seine 的保护动作链（扑倒→护头→半空转体→背挡墙）与素读#2 完全一致；「absorb the impact into the wall」译「用自己挡住撞向墙壁的冲击」方向无误。
- 块5「Like she should have been from the Sundancer」译「就像它本该被房车撞死时那样」——补刀只是让死亡提前的语义保留完整。
- 块6 Seine 以 Sebby 类比 Trace（「sort of like your Spear Woman friend」）——说话人=Seine、听者=Nate，md 中文「你那位 Spear Woman 朋友」归属无误。

**结论：阻断 0、提示 3（均不修）。本章干净。**
