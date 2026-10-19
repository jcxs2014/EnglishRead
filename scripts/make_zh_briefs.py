#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成每批的派活简报（brief）。

AGENTS 8.1 第 7i 条：**子代理分批派，别共用一份任务书**——
「批数 ≥3 章时按章段切成多份 brief，每份写清**本批章号 + 本批专属判据**」
「同一问题被不同代理报成同一句话 / 同一配额被不同代理各判各的」

⇒ 本脚本为每批生成一份独立 brief：共同规则指向规格书（唯一副本），
**本批专属判据**（时间线位置 / 循环轮次 / 缺中文理解块的分布 / 尾节状态）写死在各批。
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = "notes/books/novels/maybe-next-time-by-cesca-major"
GATE = ".memory/raw-gates/maybe-next-time-by-cesca-major"
SPEC = f"{GATE}/2026-10-19-中文层重写规格.md"

# 每批专属判据：时间线位置 / 循环轮次 / 特殊提醒
NOTES = {
"B01": """**本批 = 现在线危机的前段**（ch03–ch06）。
- ch03「the morning of」：2021-12-03 早晨，Emma 日常失序的 setup；**有 3 块缺「中文理解」**（原句 8/9/10 附近），
  要从零补写四件套（关键词行已存在，**不要动**）。
- ch04「the commute」：同日早晨通勤，Dan 短信变冷；专业危机（Arthur 的 Guardian 风波）首次浮出。
- ch05「two years」：**Dan 的第 2 封周年信，写于 2008-12-03，回顾第 2 年**（不是现在线！）。
  ⚠️ 本章块内必须点明「这是 Dan 2008 年写的信、回顾两人相处的第 2 年」，否则读者会误读成当下发生的事。
- ch06「the meeting」：同日，Emma 陪 Linda/Arthur 去 Charter Publishing 开会，用谎话保住 Arthur 的合同。
- ⚠️ **时间跳转提醒**：ch05 是回信线，其余三章是现在线，块内要分清。""",

"B02": """**本批 = 现在线危机的转折 + 第 3 封回信**（ch07–ch10）。
- ch07「the realization」：同日，Emma 意识到 12 月 3 日的意义；**有 4 块缺「中文理解」**
  （原句 4「I was hiding,」/ 7「Oh God.」/ 9、10 的聊天消息附近）——短引语，
  分析要说明「这么短的一句话在此刻承担什么功能」，不能靠复述字数。
- ch08「the evening」：同日傍晚，Emma 的道歉与 Dan 的「It doesn't matter」。
- ch09「three years」：**Dan 的第 3 封周年信，写于 2009-12-03，回顾第 3 年**；
  信里首次出现「careering into the 'After'」＝ loop 的种子。**有 1 块缺「中文理解」**。
- ch10「the committee」：同日，办公室里的 Guardian 危机与 Miles 的「Don't worry about the sausages」。
- ⚠️ **时间跳转提醒**：ch09 是回信线，其余三章是现在线。""",

"B03": """**本批 = 现在线危机的三线并进 + 撞击的余波**（ch11、ch12、ch13、ch15）。
- ch11「the committee meeting」：同日，Emma 机械记录会议纪要。
- ch12「four years」：**Dan 的第 4 封周年信，写于 2010-12-03，回顾第 4 年**——
  Poppy 出生后的挣扎，Dan 丧亲之痛。**这一章是婚姻危机的起源**，块内要写清信件年份与回顾年份。
- ch13「the loop」：同日夜里，Emma 回家晚、Miles 未睡；**loop 的第 2 轮**（ch02 是第 1 轮）。
  **有 2 块缺「中文理解」**。
- ch15「the aftermath」：Dan 死后 Emma 跪在现场的余波；**有 1 块缺「中文理解」**。
- ⚠️ **时间跳转提醒**：ch12 是回信线（2010），其余三章是现在线。ch15 紧接 ch14（撞击），是同一夜。""",

"B04": """**本批 = 最后一封信 + 循环重置 + 第 5 封回信**（ch16–ch19）。
- ch16「fifteen years」：**Dan 写于 2021-12-03 的第 15 封（＝最后一封普通周年）信**，
  回顾第 15 年。⚠️ 注意它在书里排在 ch19（2011）**之前**——这不是编年序，别当错。
- ch17「the reset」：Emma 再次在 12 月 3 日早晨醒来，Dan 还活着——**loop 的机制揭晓**。
- ch18「the second loop」：**loop 第 2 轮**（Emma 试探现实）；**有 3 块缺「中文理解」**。
- ch19「five years」：**Dan 的第 5 封周年信，写于 2011-12-03，回顾第 5 年**（分居年，Dan 道歉求复合）。
- ⚠️ **时间跳转提醒**：ch16、ch19 是回信线，ch17、ch18 是现在线的循环轮次。
  ch18 块内要点明「这是第 2 轮循环」。""",

"B05": """**本批 = 循环第 3 轮（Emma 主动改变）**（ch20–ch23）。
- ch20「the third loop」：**loop 第 3 轮**（Emma 试图改变）；**有 3 块缺「中文理解」**。
- ch21「the meeting again」：**第 3 轮里的 Arthur 会议**，Emma 的改变反而弄巧成拙；
  **有 2 块缺「中文理解」**。
- ch22「the lunch」：**第 3 轮**，Emma 试图向 Hattie 解释循环；**有 1 块缺「中文理解」**。
- ch23「six years」：**Dan 的第 6 封周年信，写于 2012-12-03，回顾第 6 年**（Dan 康复之年、阳台坠落）。
- ⚠️ **时间跳转提醒**：ch23 是回信线（2012），其余三章是现在线第 3 轮。""",

"B06": """**本批 = 循环第 3 轮后半 + 第 7 封回信**（ch24–ch27）。
- ch24「telling jas」：**第 3 轮**，Emma 终于把循环告诉 Jas。
- ch25「checking dan」：**第 3 轮**，Emma 打电话确认 Dan 还活着。（本章只有 3 块，短引语多，
  分析要说明短句在通话场景里的功能。）
- ch26「seven years」：**Dan 的第 7 封周年信，写于 2013-12-03，回顾第 7 年**（Miles 出生后的家庭幸福年）。
- ch27「the letter」：**第 3 轮**，Emma 终于写成了给 Dan 的信（loop 模式的第一次成功修正）。
- ⚠️ **时间跳转提醒**：ch26 是回信线（2013），其余三章是现在线第 3 轮。""",

"B07": """**本批 = 循环第 4–5 轮 + 第 8 封回信**（ch28–ch31）。
- ch28「quitting」：Emma 终于退出委员会（committee）。
- ch29「the attempt」：**loop 第 4 轮**，Emma 最绝望的修正尝试。
- ch30「eight years」：**Dan 的第 8 封周年信，写于 2014-12-03，回顾第 8 年**（Emma 转行做 Agent）。
- ch31「the fifth loop」：**loop 第 5 轮**，Emma 已接受循环、开始尝试。
- ⚠️ **时间跳转提醒**：ch30 是回信线（2014），其余三章是现在线的第 4/5 轮。""",

"B08": """**本批 = 循环第 6–7 轮 + 第 9 封回信**（ch32–ch35）。
- ch32「the bench」：**loop 第 6 轮**，Emma 独自坐在长椅上怀疑现实；**有 1 块缺「中文理解」**。
- ch33「the hospital」：**第 6 轮**，Emma 走医疗系统这条路。
- ch34「the death」：**loop 第 7 轮**，Emma 阻止 Dan 出门却失败；**有 7 块缺「中文理解」**
  ——本批最重的一块。本章的块多是**极短对白**（"Being mean how?" / "Dan was in the room." /
  "He was lying on the floor next to the sofa."），
  分析要说明短句**在对话链上的位置与功能**（谁在问、谁在答、停顿在哪），**不能靠复述字数凑数**。
- ch35「nine years」：**Dan 的第 9 封周年信，写于 2015-12-03，回顾第 9 年**（装修房子之年）。
- ⚠️ **时间跳转提醒**：ch35 是回信线（2015），其余三章是现在线第 6/7 轮。""",

"B09": """**本批 = 循环第 8 轮（Emma 的崩溃与出走）**（ch36–ch39）。
- ch36「the breakdown」：**loop 第 8 轮**，Emma 精神崩溃、破罐破摔；**有 1 块缺「中文理解」**。
- ch37「the zoo」：**第 8 轮**，Emma 请假出走。
- ch38「the ritz」：**第 8 轮**，Emma 与 Hattie 在丽兹酒店。
- ch39「ten years」：**Dan 的第 10 封周年信，写于 2016-12-03，回顾第 10 年**（Pangbourne 求婚年）。
- ⚠️ **时间跳转提醒**：ch39 是回信线（2016），其余三章是现在线第 8 轮。""",

"B10": """**本批 = 循环第 8–9 轮**（ch40–ch43）。
- ch40「the sleep」：**loop 第 8 轮**续（Emma 醉在 Soho）。
- ch41「the revelation」：**loop 第 9 轮**，学校来电：Poppy 被人霸凌。
- ch42「eleven years」：**Dan 的第 11 封周年信，写于 2017-12-03，回顾第 11 年**（Ibiza 婚礼年，
  信里出现 "We need to keep carving out time for each other."——**这句在 ch47 会再次出现**，
  是呼应，两处都应点出）。
- ch43「the truth」：**loop 第 9 轮**，Emma 去找 Hattie 对质。
- ⚠️ **时间跳转提醒**：ch42 是回信线（2017），其余三章是现在线第 8/9 轮。""",

"B11": """**本批 = 循环第 10 轮与绝望谷底 + 第 12 封回信**（ch44–ch47）。
- ch44「the despair」：**loop 第 10 轮**，Emma 意识到「是 Hattie 撞死了 Dan」。
- ch45「the phone calls」：**第 10 轮**，Emma 辞职、打给父母。
- ch46「the despair」：present-day 循环的**最低谷**（"I wanted to die"）；注意本书有两个
  名为 the despair 的章（ch44 与 ch46），**ch46 是绝望弧线的顶点**。
- ch47「the twelfth letter」：**Dan 的第 12 封周年信，写于 2018-12-03，回顾第 12 年**（Hattie 婚礼年）；
  块内要点明与 ch42 "We need to keep carving out time for each other." 的呼应。
- ⚠️ **时间跳转提醒**：ch47 是回信线（2018），其余三章是现在线第 10 轮与绝望谷。""",

"B12": """**本批 = 从绝望到接受 + 第 13 封回信**（ch48–ch51）。
- ch48「the gift」：present-day 循环的**转折点**——Emma 把循环当作「礼物」。
- ch49「the gift day」：**gift arc #1**（Emma 的第一个「礼物」日）。
- ch50「the tiktok day」：**gift arc #2**（发现 Poppy 的 TikTok 霸凌、每日例程成形）。
- ch51「the thirteenth letter」：**Dan 的第 13 封周年信，写于 2019-12-03，回顾第 13 年**
  （Emma 四十岁生日、佛罗伦萨）；信里出现 "Forty Reasons You Love Me"（Dan 给自己的清单）。
- ⚠️ **时间跳转提醒**：ch51 是回信线（2019），其余三章是现在线的 gift arc。
- ⚠️ **叙述层级提醒**：ch48/ch50 里 Emma 在读 Ernestina 的书稿——凡引到书稿内容，
  必须标明「这是 Emma 读到的书稿里的一句」，不要与 Emma 自己的叙述混为一谈。""",

"B13": """**本批 = gift arc 续 + 第 14 封回信 + 怒火转向**（ch52–ch55）。
- ch52「the audiobooks」：**gift arc #3**（给 Jurek 妈妈送有声书、带 Gus 看兽医、帮编辑 Charlie）。
- ch53「the poppy day」：**gift arc #4**（Poppy 霸凌的深挖）。
- ch54「the fourteenth letter」：**Dan 的第 14 封周年信，写于 2020-12-03，回顾第 14 年**
  （COVID 封控年、居家教学）。
- ch55「the hattie confrontation」：Emma 的怒火转向 Hattie——**她无法原谅 Hattie**。
- ⚠️ **时间跳转提醒**：ch54 是回信线（2020），其余三章是现在线。
- ⚠️ **叙述层级提醒**：ch52 有 Ernestina 书稿、有声书内容——引到时标明层级。""",

"B14": """**本批 = 原谅 → 完美日 → 死亡信 → 重启**（ch56–ch59）。
- ch56「the forgiveness」：Emma 每晚回事故现场，最终原谅 Hattie；Hattie 揭露 Ed 的虐待与流产。
- ch57「the perfect day」：**resolution arc**——Hattie 住进家里、全家滑冰、
  Emma 告诉 Dan 循环真相（"You die. Tonight."）。
- ch58「the last letter」：**Dan 死前半小时写的信**（10:17 p.m.）——他给 Emma 的最后留言。
- ch59「the loop」：**循环重启**（同一个早晨，但 Emma 变了）。本章只有 1 个引语块，
  分析要写足（这是全书的收束，读者需要知道它意味着什么）。
- ⚠️ **时间跳转提醒**：ch58 是 Dan 的最后一封信（2021-12-03 夜里，**不是周年信**），
  其余三章是现在线。ch59 是循环的第 11 轮（承接 ch56–ch58）。""",

"B15": """**本批 = 两章样板（ch01、ch02）——只做「去夹杂」，不做重写**。
- ch01「how we met」是**全书的原生样板**（作者手笔），ch02「present day crisis」紧随其后。
- 这两章的「中文理解」已经是中文，**不要动**。
- 待处理的只有：`为什么这样写` 与 `读者视角提示` 里的**中英夹杂**
  （ch01：why 6 块、tip 7 块；ch02：why 11 块、tip 11 块、zh 2 块）——
  即把**裸英文术语/短引**尽量改写成中文表述，**但保留真正需要逐字引用的英文证据**。
- ⚠️ **ch01 的 H1 标题、导航、词汇表一律不动**。
- ch02 的文件级尾节（`## 读者视角提示` 小节）是英文，**要改写成中文**（见规格书第 0 节）。
- ⚠️ **本批判据与其它批不同**：这里是**减法**（把英文术语换成中文），
  不是重写。**不要改变任何分析结论**。""",
}

TEMPLATE = """# 派活简报 {batch}：{chs}

> **共同规格（唯一副本，必读）**：`.memory/raw-gates/maybe-next-time-by-cesca-major/2026-10-19-中文层重写规格.md`
> ⚠️ 该文件里有**硬禁令**（证据先行 / 禁令 1–5 / 防幻觉条款 / 编辑纪律 / 验收命令），
> **没读就不要动手**。本简报只写**本批专属判据**。

## 本批清单

- 派活数据：`{gate}/batches/{batch}.json`（每章每块的现状、引语、flags、原文路径）
- 目标书目录：`{book}/`
- 原文提取件：`{book}/text/chNN_chapter_<N>.txt`（**先读它再写分析**）

{note}

## 你要做什么（逐块）

1. **读** `{gate}/batches/{batch}.json` —— 里面列了本章每个待改块：
   `n`（原句编号）、`line`、`quote`（引语）、`zh`/`why`/`tip`（现状）、`flags`（要改什么）。
2. **读**该章原文 `text/chNN_chapter_<N>.txt`（用 `sed -n` / `grep`，**不信记忆**），
   看清楚引语在原文里的上下文、说话人、前后情节。
3. **写**三个字段的中文版（`flags` 标了才需要写；没标的保持原样）：
   - `中文理解`——用自己的话说明这句话说了什么、谁说的、在场景里起什么作用
   - `为什么这样写`——中文散文体分析作者的写法选择与效果
   - `读者视角提示`——中文：词义提示 + 理解要点
4. **写成一份 JSON spec**（格式见规格书「用法」节），存到
   `.memory/raw-gates/maybe-next-time-by-cesca-major/batches/{batch}.spec.json`，
   然后运行：

   ```bash
   cd /Users/jcxs2014/Documents/Works/EnglishRead
   python3 scripts/rewrite_zh_fields.py \\
     "notes/books/novels/maybe-next-time-by-cesca-major" \\
     ".memory/raw-gates/maybe-next-time-by-cesca-major/batches/{batch}.spec.json"
   ```

   ⚠️ **不要手改 md**（整文件 write 会误伤引语行/关键词行/词表）——
   这个脚本做块作用域内的行级替换，并**断言引语行与关键词行逐字未变**。

5. **跑验收**（规格书第 7 节），贴原始输出。

## 硬约束（重复强调）

- **只碰本批的 md 文件**；不碰 `text/`、`library/`、其它章、`.memory/` 下的其它文件。
- **不执行 `git add` / `git commit`**（由主会话统一提交）。
- 分析层里出现的**英文必须逐字取自本章 `text/`**（或该块引语本身）——
  写完跑 `python3 scripts/check_analysis_quotes.py "<书目录>" --file "<md 文件名>"`，
  **「疑似伪造」必须清零**；跨章引用要在块内标出 chNN。
- **禁**「N 个词 / N 个分句」「倒数第二段」「独立成段」「全章唯一」「第一次」「最高级」
  这类不可核断言（禁令 2 / 2a）。
- 短引语块（尤其 ch34）**不许靠复述字数凑数**——要分析短句在对话链上的功能。
- **不做**「改写引语」「改关键词」「删引语」——那些是别的任务。

## 回报格式

1. 本批**改了哪些章、每个章各几个块**；
2. `check_chinese_layer.py` 里**本批章号一条都不再出现**的证据（贴原始输出）；
3. `verify_quotes.py` 仍 100% 的证据；
4. `check_analysis_quotes.py` 本批文件**疑似伪造 0** 的证据；
5. `corruption_scan.py` FAIL 0 的证据；
6. **遇到判断不了的地方**（例如引语在原文里找不到、或语义有歧义）——
   **不要猜**，在回报里单列「待人工判定」清单交回主会话。
"""


def main():
    gate = GATE
    for batch in sorted(NOTES):
        p = os.path.join(ROOT, gate, "batches", f"{batch}.json")
        if not os.path.exists(p):
            print(f"❓ 缺 {p}")
            continue
        d = json.load(open(p, encoding="utf-8"))
        chs = "、".join(c["file"][:3] for c in d["chapters"])
        body = TEMPLATE.format(
            batch=batch, chs=chs, note=NOTES[batch], gate=gate, book=BOOK
        )
        out = os.path.join(ROOT, gate, "batches", f"{batch}.brief.md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(body)
        print(f"✏️  {out}")


if __name__ == "__main__":
    main()
