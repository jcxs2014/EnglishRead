# ch13 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，10 块 10 引语，issues 全空。
R4 人判：10/10 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块5「他们其实是老师」的反转 | 引语「They were the teachers, actually, opening up a whole new world of delights」；素读#6 | 转述准确，反讽保留 | 已核实为正确 |
| 素读细节级漏 ×4（头盔砸鼻／四道扣环靴锤／九十秒·囚犯·嗓音模仿／Mooch 被扛回） | 素读 anchor 命中 True ×4 | 狩猎场景细节，非关键转折 | 提示（不修） |
| 块9「real eyes…fabric panel hidden in the neck」 | 素读#8「真眼藏在颈部布板里」 | 一致 | 已核实为正确 |

取证命令记录：
- 素读 anchor 偏移验证 True ×8（ch13 子代理自证 + 本会话抽验）
- `/usr/bin/grep -n "Ninety seconds" text/ch13_12_for_your_next_stunt.txt` → 命中（素读#7）；退出码 0

## 已核实为正确

- 块1「You're proof of that」译「你就是证明」——月亮人自指为「偏差」的产物，md 保留第一人称转述视角。
- 块3「This is delicious」译「这真是美味」——残忍品味直陈，未软化。
- 块8「You're the only one she has eyes for」译「她的眼里只有你」——误认的心理机制（儿子戏服）与素读#8 一致。

**结论：阻断 0、提示 1（合并细节漏，不修）。本章干净。**
