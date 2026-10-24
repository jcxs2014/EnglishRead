# T1 自检判定 · john-grebble-is-gone-by-peter-james（2026-10-24）

抽样章：**ch01 + ch05**（ceil(5/8)=1 → 最少 2 章、首末必含；抽样于动手前声明，assertion_scan 之后未再调整）。ch01 复用素读清单（8/8 锚点全命中，production/ch01-suread.json）＋抽 3 条事实回源核对无误；ch05 同（8/8，production/ch05-suread.json）。引语邻域重点重读：ch01 三处、ch05 两处。

## 查出并已整改的缺陷（12 处内容 + 4 处指称，全部改后复验）

| # | 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|---|
| 1 | ch02:131 / 金句⑭上下文 | 二十万英镑 | 两万英镑 | "How does twenty thousand pounds in cash sound?" |
| 2 | ch04 导航 | 把哥哥引进核地堡 | 把弟弟引进核地堡 | Geoff 是 "malignant younger brother"（ch01） |
| 3 | ch04:48 | 他明知道哥哥刚把 352,000 镑 | 他明知道弟弟刚把 | 同上 |
| 4 | ch01:64 | 本章结尾他要打给 Geoff | 当天下午他不得不拨给 Geoff | 电话在 ch03（当日晚间），非 ch01 末 |
| 5 | ch02:133 | 四个词收束全章 | 五个词 | And he would. Oh yes. = 5 词 |
| 6 | ch05:40 | fitted him well 四个词 | 三个词 | fitted him well = 3 词 |
| 7 | ch02:61 | 三个逗号串成一帧 | 两个逗号串成三帧 | 原句 2 处逗号 |
| 8 | ch04:96 | 三十年窝囊 | 半生窝囊 | 原文无三十年，属凭空数字 |
| 9 | ch03:68 | 你带我弟弟的护照陪我 | 你带上你的护照陪我 | 说话人视角：对 Geoff 说 your passport |
| 10 | ch05:60 | 两度杀人未遂 | 刚刚把亲弟弟反锁进地堡、正用弟弟护照逃亡 | 「两度」无据 |
| 11 | ch03:76 | in cash 出现两次（域不明） | 从电话报价到本条款出现两次 | 章内 2 次（L1117/L1198），块内 1 次 |
| 12 | ch02:171 | 欠他人情的弟弟 | 欠着他四万多镑的弟弟 | "It's over forty thousand." |
| 13-16 | 金句 ②⑧⑪⑯ 呼应关系 | 指称错位（⑭/玻璃内外/㉒反杀/㉓含茶） | 改为与实际被指金句相符 | 逐条回查目标金句内容 |

概述层六类断言抽查：352,000 镑（ch03 Dubai 段）／Lewes+Ford 两监狱／诈骗老太 3 万镑／申报人 Geoffrey Anthony Grebble／Crawley／一周后 Southampton——逐条有 text/ 支撑；「唯一对他好」「几乎全部社交宇宙」有 "the only person there" 与 "almost his entire social universe" 逐字支撑。

## 记录不改（评析修辞类从宽，共 7 处）

「第一次同台对质」「唯一的行动纲领」「全章唯一的抒情时刻」「全书唯一需要的暴力比喻」「作者唯一一次表态」「暴力在这里第一次替所有制度失灵出头」「所有大事之后都要泡茶」——均为评析层修辞判断，非事实断言。

## 覆盖与结论

- t1-candidates.txt：assertion_scan 原始输出，候选 120 行（①14/②15/③62/④17/⑤7/⑥5），①②③⑥ 全量 98 行逐条判定，④⑤ 34 行全读（未抽 20 而是全读）。
- 整改后复验：五章 chapter.sh 全 EXIT=0 / overview quotes 50/50 / structure order 43 块 0 缺陷 / corruption_scan 0 / gate.sh EXIT=0。
- 查出阻断 <3 条 ⇒ 不触发 T2。**T1 为同会话自检**，有效率未测——验收仍以异会话复核为准。
