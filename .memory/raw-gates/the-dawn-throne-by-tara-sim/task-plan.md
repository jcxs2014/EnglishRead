# The Dawn Throne (Tara Sim) · 任务表
- 体裁：novels（奇幻长篇，Dark Gods 系列第四部前作？副线=四贵族院政斗+神祇战争）；双 POV（Nikolas Cyr / Dante Lastrider 交替）
- 语料：text/ 51 件零偏移（ch00 = Perigee 序章；ch01–ch20 = Part I: Feather and Flower 的 I–XX；ch21–ch30 = Part II: Void and Flame 的 I–X；ch31–ch39 = Part III: Between the Wasteland and Sky 的 I–IX；ch40–ch49 = Part IV: First Light 的 I–X；ch50 = Apogee 尾声 93 词）；xx_the_four_noble_houses_of_nexus.txt = 装置页不写
- 部内章号重号 ⇒ H1 形态：`# NN. <罗马数字>（Part <N>: <部名>）`（sleepers `# NN. Chapter N（月名）`先例）；ch00/ch50 用书内自名 Perigee/Apogee
- 验收：verify_corpus PASS（expect 51 · anchors ch00=Phos/ch01=Nikolas,Phos/ch21/ch31=Nikolas,Phos · shared=Nikolas,Phos,Sol · FAIL 0 WARN 0）
- 批次节奏：长篇 1 章/次，每章 chapter.sh rc=0 立刻 pathspec commit；每批前 gate.sh
- 状态：ch01 试产验收通过（8a57ce346），批量推进 ch00–ch50 + 总览三篇 + T1

| 章 | 书内标题 | 词数 | 状态 | commit |
|---|---|---|---|---|
| ch00 | Perigee | 3047 | 完工 | c3a7e43b9 |
| ch01 | I | 3264 | 完工 | 8a57ce346 |
| ch02 | II | 3264 | 完工 | 048a51e2a |
| ch03 | III | 4578 | 完工 | f59e4fc12 |
| ch04 | IV | 4941 | 完工 | 9da0a5a43 |
| ch05 | V | 5300 | 完工 | e03b794c9 |
| ch06 | VI | 3511 | 完工 | 98d0c81c0 |
| ch07 | VII | 3611 | 完工 | e244d9fdd |
| ch08 | VIII | 2484 | 完工 | 7ca2dfdb1 |
| ch09 | IX | 1815 | 完工 | 667dad391 |
| ch10 | X | 2087 | 完工 | 35ea864a1 |
| ch11 | XI | 2565 | 完工 | e2909ffa9 |
| ch12 | XII | 2069 | 完工 | 5085c7999 |
| ch13 | XIII | 1787 | 完工 | 307baaa3b+cc52f0816 |
| ch14 | XIV | 2170 | 完工 | ae5f053aa |
| ch15 | XV | 1799 | 完工 | ef5e1add6 |
| ch16 | XVI | 1726 | 待写 | |
| ch17 | XVII | 1546 | 完工 | d801fc644 |
| ch18 | XVIII | 2199 | 完工 | 49de9102d |
| ch19 | XIX | 1633 | 完工 | 14ce4e8f3 |
| ch20 | XX | 1254 | 完工 | c29957a17 |
| ch21 | I（Part II） | 2465 | 完工 | 6f096f3a8 |
| ch22 | II（Part II） | 3685 | 完工 | e0b8340a3 |
| ch23 | III（Part II） | 3659 | 完工 | ee494a0f4 |
| ch24 | IV（Part II） | 2559 | 完工 | 45bf6e804 |
| ch25 | V（Part II） | 3153 | 完工 | 4e9db1295 |
| ch26 | VI（Part II） | 4910 | 完工 | 3321fc15b |
| ch27 | VII（Part II） | 2129 | 完工 | 25bb9e01e |
| ch28 | VIII（Part II） | 2239 | 完工 | bcd1a1233 |
| ch29 | IX（Part II） | 3578 | 完工 | ccf29d9db |
| ch30 | X（Part II） | 1921 | 完工 | 96e8e8c47 |
| ch31 | I（Part III） | 4376 | 完工 | e796bc0f6+c39a7c29e |
| ch32 | II（Part III） | 5411 | 完工 | 775574635 |
| ch33 | III（Part III） | 3995 | 完工 | f95cd0aba |
| ch34 | IV（Part III） | 1898 | 完工 | 274fb4e44 |
| ch35 | V（Part III） | 2226 | 完工 | 2b05e290b |
| ch36 | VI（Part III） | 5016 | 完工 | 1bbda72b7 |
| ch37 | VII（Part III） | 3844 | 完工 | c95b5f64e |
| ch38 | VIII（Part III） | 4702 | 完工 | 07f11fddd |
| ch39 | IX（Part III） | 3968 | 完工 | 787b22a0b |
| ch40 | I（Part IV） | 2287 | 完工 | a2514720a |
| ch41 | II（Part IV） | 3108 | 完工 | 946041f6f |
| ch42 | III（Part IV） | 2733 | 完工 | a7bb18d65 |
| ch43 | IV（Part IV） | 2831 | 完工 | f7ad1f84f |
| ch44 | V（Part IV） | 1930 | 完工 | 2dbd1c78a |
| ch45 | VI（Part IV） | 2372 | 待写 | |
| ch46 | VII（Part IV） | 1470 | 待写 | |
| ch47 | VIII（Part IV） | 2054 | 完工 | 0a83e8374 |
| ch48 | IX（Part IV） | 3470 | 完工 | de5b6ba50 |
| ch49 | X（Part IV） | 3186 | 完工 | (见 ch50 批次) |
| ch50 | Apogee | 93 | 待写 | |
| — | 总览三篇 00_概述/00_金句精选/00_情感节点 | | 最后写 | |
| — | T1 自检（t1-verdict/t1-candidates/台账） | | 完工前 | |
