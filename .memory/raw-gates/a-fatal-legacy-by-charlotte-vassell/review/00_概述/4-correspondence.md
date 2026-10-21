# 00_概述.md · R4 逐条对应（引语逐字 / 章号归属 / 是否支撑所在段落）

> 每条英文引语一行。共 18 条（全书梗概 8 + 三个主题 3 + 人物弧光 7）。
> 逐字 = 与 `text/chNN_N.txt` 逐字符相同（Python `str.find` 命中，且全章唯一命中）；
> 章号 = 引语实际所在章是否等于标注的（chNN）；
> 支撑 = 「这段中文是不是在讲这句引语」。
> 机器层：`2-machine.txt`（`overview.py quotes` 18/18 ✅；`labels` 18 条带标签、跳过 0）。

| # | 位置 | 章:区间 | 引语（起） | 逐字 | 章号 | 支撑 | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | §一 | ch01:[2340,2403) | "The shrunken heads watch from their cabinet as his heart stops." | ✅ | ✅ ch01 | ✅ | §一「临死前…柜子里的标本看着他咽气」＝引语本身，全文唯一命中 |
| 2 | §二 | ch09:[2732,2837) | "‘It’s worth a bomb.’ Amy stared at the whiteboard. ‘I wonder who inherits the Institute with Digby gone?’" | ✅ | ✅ ch09 | ✅ | §二「研究所值多少／谁继承这一格」＝引语原话 |
| 3 | §三 | ch19:[41,263) | "‘I’ve got the information from the Post Office,… The PO Box is located in Barnet… Mrs Beverley Parkin… three months.’" | ✅ | ✅ ch19 | ⚠️ **不对应** | §三讲的是「被抄走的一份履历」（Isolde 的哥哥/瓦格纳/芭蕾/草莓过敏），引语讲的是**邮政信箱的归属与期限**——那是 §四 的内容。引语被提前一段；§四 反而无引语 |
| 4 | §四 | ch25:[9283,9460) | "‘What do Digby and Scott have in common? They were both lonely men…’" | ✅ | ✅ ch25 | ✅ | §四「两桩命案并到同一点：都发生在第一次约会，两个都是孤独的男人」＝引语原话 |
| 5 | §五 | ch33:[13426,13463) | "‘Priory Square. It’s Beauchamp land.’" | ✅ | ✅ ch33 | ✅ | §五「普里奥里广场姓 Beauchamp」＝引语原话 |
| 6 | §六 | ch42:[10017,10216) | "‘No, that’s Mel, her sister.’ … ‘Mel’s the voice. Eulalia is the face. That’s why they resent each other.’" | ✅ | ✅ ch42 | ✅ | §六「欧拉莉亚负责露面，梅尔负责出声」＝引语原话 |
| 7 | §七 | ch48:[3594,3683) | "‘Yes,’ Matt said, staring at Caius’s printout of the square on the whiteboard. ‘But why?’" | ✅ | ✅ ch48 | ✅ | §七「只剩一片空白——为什么」＝引语原话（说话人：Matt，见 3-diff B9） |
| 8 | §八 | ch52:[10204,10367) | "‘Willow Bell, I am arresting you for the murders of Digby Combe-Watson and Scott Brown.’…" | ✅ | ✅ ch52 | ✅ | §八「当场以两起谋杀罪逮捕」＝引语原话 |
| 9 | 主题一 | ch11:[6493,6960) | "‘He called it “Our Apologia”. …directly inherit a colonial horror…’" | ✅ | ✅ ch11 | ✅ | 主题一「写一本自辩书…直接继承一份殖民恐怖」＝引语原话 |
| 10 | 主题二 | ch16:[292,628) | "‘…there are only ten Isoldes in the entire UK. One is in a nursing home in Surrey. Seven are in primary school…’" | ✅ | ✅ ch16 | ✅ | 主题二「叫 Isolde 的只有十个人，七个上小学，一个养老院」＝引语原话 |
| 11 | 主题三 | ch52:[6319,6577) | "Caius and Matt came over and they watched as the little robot shone a light on the crypt…" | ✅ | ✅ ch52 | ✅ | 主题三「收藏的尽头，是把人摆进柜子…一具压一具的骸骨」＝引语原话 |
| 12 | 弧光·凯厄斯 | ch54:[10854,11022) | "‘He’s very good. He’ll come around.’ Hampton pushed a little bile…" | ✅ | ✅ ch54 | ✅ | 弧光「他拒绝了，但对方说他会回头」＝引语原话 |
| 13 | 弧光·卡莉 | ch54:[4055,4097) | "‘Yes, please.’ Callie sat up. ‘I’m sorry.’" | ✅ | ✅ ch54 | ✅ | 弧光「她在沙发上开口的第一句是道歉」＝引语原话 |
| 14 | 弧光·迪吉 | ch04:[4095,4152) | "The poor guy had kept the ad. A memento of their romance." | ✅ | ✅ ch04 | ✅ | 弧光「把交友广告剪报当成一段恋情的纪念品」＝引语原话 |
| 15 | 弧光·威尔洛 | ch52:[10593,10828) | "‘Forensics found the paper cup late last night with Scott’s address on… It had Willow’s prints on it,…’" | ✅ | ✅ ch52 | ✅ | 弧光「用真 Isolde 的名字…把日记伪装成粉丝信…被捕时一个字没说」——引语落在「栽赃链的物证」上，支撑成立 |
| 16 | 弧光·梅尔 | ch45:[5559,5751) | "Her coming off some quite heavy antipsychotics… Mel’s dependent on her. Well, they’re codependent." | ✅ | ✅ ch45 | ✅ | 弧光「这对姐妹既怨恨又依赖，连药都要捏在对方手里」＝引语原话 |
| 17 | 弧光·欧拉莉亚 | ch42:[6228,6414) | "‘Yes. I suppose. Eulalia and Mel are quite clearly sisters but one of them… looks like a goddess and the other looks like a Picasso…’" | ✅ | ✅ ch42 | ✅ | 弧光「是姐姐梅尔的声音借出去的那张脸」——引语给出「神像 vs 毕加索」的分工比喻，支撑成立 |
| 18 | 弧光·罗比 | ch37:[2691,2913) | "‘Amy’s trying to tell you the answers to your questions because we’ve already asked them ourselves, but you keep cutting her off…’" | ✅ | ✅ ch37 | ⚠️ **偏弱** | 引语内容是「马特抱怨罗比打断艾米」，落在**罗比打断人**这一性格上；该段落的三个主干（翻白板背面＝ch48、「但为什么」＝马特的话、要求逐句交代出处＝原文没有）本条一条都不支撑。**建议改引 ch48 罗比追问白板颜色/意义那两句** |

## 统计

- 逐字：**18/18 ✅**（独立复核：每条在其标注章 `find` 命中且**全 54 章唯一命中**；机器 `overview.py quotes` 00_概述 18/18 ✅）
- 章号归属：**18/18 ✅**（无跨章错标；机器 `labels` 18 条带标签、跳过 0、待人判 0）
- 对应：**16 对应 / 2 提示（#3 段落错位、#18 对应偏弱） / 0 阻断**
- d2 形态：18 条英文引语**全部独立成行**（`> "…"`），无一内联在正文行内；每行末尾带（chNN）；机器 `full` 段「F 无引号引语标签：对 0｜跳过 0」「E H1 语义错配：0」
