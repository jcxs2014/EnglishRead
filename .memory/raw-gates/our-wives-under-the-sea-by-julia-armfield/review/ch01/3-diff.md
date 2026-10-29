# ch01 对账（R1 素读 7 条 / relations 3 / numbers 8 ↔ md 8 块）

## 漏（素读有、md 无）
| 素读条目 | md 状态 | 判定 |
|---|---|---|
| 早六点鼻血 → 递法兰绒 → Leah 推手说没事 → 鞋不配对 → Miri 硬套鞋要送 A&E | 导航「一句话概括」写到「清晨六点 Leah 照例流鼻血，说这是压力突然消失的缘故」；正文 Q6 写血的成因、Q7 写镜中溺死者；**推手/鞋不配对/A&E 未进正文** | **已修**：新增原句 6（`At around six this morning… this state of half remove.`，41 词），覆盖分房 + 半在场；鞋不配对/A&E 转入该块读者提示 |
| Miri 输完除 personnel number 的全部细节，第三个录音声音训斥并挂断 | Q8 中文理解：「被一套索要编号的自动语音拦下，最后被切断」+「为什么这样写」提到声明编号顺序错一个就切断 | 已覆盖 |

## 编（md 有、原文无）
无。逐块核 Q1–Q8 的每条断言（含「购物单 milk, cheese, sleep aid [any]…」在导航）均能在 text/ch01_miri.txt 找到对应句。

## 错（两边都有但不一致）
无。数字全部一致：上个月（`since she returned last month`）、六点（`At around six this morning` / `woken at six fifteen`）、三点（`It’s three o’clock`）、午夜（`until midnight`）、第五十次（`for the fiftieth time`）。

## 修复后复跑
`bash scripts/chapter.sh` → 9 块 / 查无 0 / 关键词不成立 0 / rc=0（本书中位 6，范围 3–12）。

## 备注
R1 的「Miri–母亲 母女」一条是子代理按书名推的，原文只写 `My mother used to say…`；md 未使用该定性，不构成缺陷（记入 4-verdict 已核实节以备后续）。
