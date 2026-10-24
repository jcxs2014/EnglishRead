# T1 自检 — In Your Heart a Devil

抽样章：ch02 / ch11 / ch21（N=20，ceil(20/8)=3；首末必含 ch02、ch21；等距取 index 9 = ch11）

## 发现与整改（位置 / 改前 / 改后 / 原文依据）

1. **00_金句精选.md 全篇 62 处相对章号**：把 chNN 文件序号当书内章号（如「第四章」指 ch04）。
   改后按书内罗马章号重映射（ch04=II=第二章 … ch20=XVIII=第十八章，ch02=Prologue=序章；第一章=ch03 不变）。
   依据：text/ 各章标题行（第一行 Unknown、第二行 I/II/…/XVIII）。
2. **00_概述.md 第 18 行**「马车驶入 S— House」→「汽车驶入 S— House」。依据：ch04_ii.txt L110「We parked by the grand door」+ L32「the car」。
3. **00_概述.md 第 24 行**「一辆马车滑出路面…车夫 Tom」→「一辆汽车…司机 Tom」。依据：ch15_xiii.txt L128「I recognised the car」、L137-140「the car veered… slid straight off the road… the car crashed into it」；ch16_xiv.txt L38「it was his car…Alexander's driver」。
4. **00_概述.md 第 18 行**「管家 Mrs White 待她温和，却提醒她有些房间不要进、夜里不要乱走」→「初见时冷淡而不耐烦，后来才慢慢成为她在这座房子里唯一的盟友」。依据：ch04_ii.txt L143「mean set to her shoulders…spoke brusquely…eyes brimming with impatience」（原文无「别进房间/别乱走」的提醒，属捏造）。
5. **00_概述.md 第 22 行时序**：原写「Nick 出现…紧接着 Mrs White 消失」→ 改为「先是 Mrs White 消失…不久之后，Nick 在雨中走来」。依据：ch10_viii.txt（Mrs White 消失）在 ch11_ix.txt（Nick 初遇「It wasn't long after Mrs White's departure that I met Nick」）之前。
6. **ch21 authors note.md 第 45 行**「Eliza 家的马车」→「Alexander 的汽车」。依据：ch16_xiv.txt L38「it was his car…Alexander's driver」。

## 复核记录

- assertion_scan 候选共 308 行：①62 / ②95 / ③34 / ④73 / ⑤18 / ⑥11，**全部读过**（T2 实质完成，未另起 T2）。
- 抽样章素读复核：ch02 / ch11 / ch21 用 production/chNN-suread.json 重建 facts 重跑 `suread.py`，24/24 锚点全中；抽 3 条事实回源（ch02 脉搏/海、ch11 bewitchment、ch21 Giles Ædie）均与原文一致。
- 总览三篇全篇人判：概述 8 段 + 3 主题 + 4 人物弧光；金句 30 句 × 4 子项；情感节点 10 节点 × 2 引语。引语由 gate ⑭ 验证 49/49 可核实。
- 未发现引语截短、跨段拼接、说话人归属错误（ch02 说话人=Alexander、ch11=Nick/Stewart、ch21=作者，均核对原文邻域）。

## 结论

阻断 5 处（3 捏造/事实错 + 2 类章号系统性错）已全部整改；候选 308/308 已读。T1 为**同会话自检**，非异会话终审。
