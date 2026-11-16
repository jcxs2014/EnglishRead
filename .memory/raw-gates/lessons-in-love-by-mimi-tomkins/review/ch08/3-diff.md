# R3 对账 · ch08

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（洗手间镇定/赌局/三味之吻/煞白/要吐/Misty 放行/Ollie 首叫/妈妈教编发）在 md 均有 | 通过 |
| 编 | 无情节捏造 | 「前两味是鸡尾酒的回放」无据：本章鸡尾酒是 coconut rum + cranberry（text:41），raspberry/lime 非其成分 | 提示 |
| 错① | 计数 | md「喜剧在第 13 个词的地方谋杀高潮」；该句本身 7 词，13 无对应锚点 | 提示（计数无据） |
| 错② | 措辞 | 「Ollie 是 Ben 早就用的叫法」；ch01–07 均无 Ollie，本章 Ben 才首次用（text:32） | 提示 |
| 错③ | 结构 | 「三味『家』的吻收尾」；吻在中段，章末是编发/额头吻 | 提示 |

## 取证
```
/usr/bin/grep -n "coconut rum|" text/ch08_chap8.txt → 41: coconut rum and cranberry juice
/usr/bin/grep -l "Ollie" text/ch0[1-7]*.txt → 无输出
/usr/bin/grep -n "Ollie" text/ch08_chap8.txt → 32（Ben 首次）374（Eden 首叫）
```
