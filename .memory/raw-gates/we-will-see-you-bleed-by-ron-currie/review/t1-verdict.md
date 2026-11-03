# T1 自检 · we-will-see-you-bleed-by-ron-currie

抽样章（先定后读）：**ch01, ch05, ch09, ch13, ch17, ch21**（共 6 章 = ceil(21/4)，等距取样，含首章 ch01 与末章 ch21）。

## 逐项记录（位置 / 改前 / 改后 / 依据）

- 00_金句精选.md ⑱上下文：「感官剥夺进行到第五分钟」→「感官剥夺刚刚开始」——原文无「五分钟」计时（text/ch12 第 76 段只写 immediate animal panic），属无据数字。
- 00_情感节点.md 节点八：「数日后 Charlie 回镇挑衅」→「随后 Charlie 回镇挑衅」——ch07 夜袭与 ch10 对峙间隔未明写「数日」，改模糊表述。
- 00_概述.md 主题一：「Charlie 面孔的 Huang」乱词 →「Babs 肿成一条缝的右眼」——依据 text/ch16「Her right eye had swelled completely shut」（已在写作期修复，此处留档）。
- 00_金句精选.md ⑩：补回说话人插入语「Babs said.」（拼接红线，修复留档）；㉑ 删「Here?」半句（/ 拼接，修复留档）。
- 00_金句精选.md 章标修正：⑧ ch5→ch4、⑯ ch9→ch13、㉖㉗㉘ ch19→ch20（overview.py labels 抓出，修复留档）。

## 抽样章复读结论（ch01 / ch05 / ch09 / ch13 / ch17 / ch21）

- ch01：7 块引语回读原文邻域一致；素读 8 锚点复验全中；「二十九岁」「240 吨」「1968/1977」回源无误。
- ch05：桥塌段「46 词块」「bullwhips」等逐字无误；「十四岁」与 ch06「Just turned fourteen」一致；「Resplendissante」拼写与原文一致。
- ch09：便士/crawl space/TEC-9 数字（100 克/半公斤/200 粒/50 发弹匣）回源无误；「Thomaston」拼写无误。
- ch13：Maguire 档案（1976/1973-76/Gloversville）回源无误；「120 岁」原文为 appeared to be at least 120——概述措辞「120 岁的」已含 at-least 语义，保留。
- ch17：TEC-9/半吨 TNT/「two hundred pills」回源无误；Reagan 面具「foam latex」逐字无误。
- ch21：「Jean-Louis Lebris de Yonne」「Ramadi」「Devil's Night in October 1988」回源无误；「two bouquets」结构意图（首尾呼应式收束）确认非重复收录。

- ① 相对章号扫出 6 处偏差，全部整改：ch07「下一章→随后」（Clement 复出实际在 ch09-11）；ch08「上一章→两章前」（密约在 ch06）；ch12「前一章→此前」、「上一章→（删相对词）」（里根段在 ch08）；ch15「下一章→当晚」（闯红灯在本章内）；ch16「下一章→本章随后」（处决在本章末）。

## assertion_scan 候选行

见 t1-candidates.txt（原始输出存档）；命中行逐条人判：年龄/年份/数字类全部回源核对（二十九/十四/五十年/四十年/1918/1968/1984/1988/2001），无阻断型残留。

## 台账

- 读了哪些候选行：assertion_scan 全量输出中 ①②③⑥ 类全读、④⑤ 类各抽 20 行；共核 38 行。
- 结论：**阻断 0**；提示级修复 11 处（5 处总览 + 6 处相对章号）；T1 为同会话自检（自检有效率未测，不能替代异会话审查）。
