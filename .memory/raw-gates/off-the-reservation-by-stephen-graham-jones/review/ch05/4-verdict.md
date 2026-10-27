# ch05 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，10 块 10 引语，issues 全空。
R4 人判：10/10 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块5 读者视角「Gladstone 歌主题＝注定战死的白人士兵（小大角）」 | text/ch05:260「that one about the doomed white soldier at Little Bighorn」 | 有据 | 已核实为正确 |
| 块2 读者视角「老牛仔是本章反复出现的旁观者」 | /usr/bin/grep -c "cowboy" → 7；退出码 0 | 「反复出现」有据 | 已核实为正确 |
| 素读#4 Mooch 白发/染发剂未入 md | text anchor「…clearing off a shelf of hair dye.」命中验证 True | 人物细节非关键转折 | 提示（不修） |
| 块9 施事：碰屏幕者=车尾的现实 Nate | 引语「in the back of the Sundancer, he reached to the screen」 | 与中文理解「车尾的 Nate」一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -n "soldier\|Custer\|cavalry\|Long Hair" text/ch05_4_he_stood_dying.txt` → 行260/395/398；退出码 0
- `/usr/bin/grep -c "cowboy" text/ch05_4_he_stood_dying.txt` → 7；退出码 0
- `/usr/bin/grep -c "afraid of catching his eye, getting a sermon" …` → 1；退出码 0

## 已核实为正确

- 块10「call a hunter home」与 T1 整改后的读者视角（「曾祖母让年幼的儿子点起、为迷路猎人引路的那堆火」）——ch02 原句6 的亲属链为据，本轮不再改动。
- 块4 生皮绳「打成 X 形」——原文「a rawhide string tied in a fancy X over it」逐字，X 形动机（防晒卷）与中文一致；此 X 与后文 Christian 圣经皮绳、瓷鹿 X 同族，非 md 过度解读。
- 块6「pouring color back into the world」译「把色彩重新灌回世界」方向无误。

**结论：阻断 0、提示 1（不修）。本章干净。**
