# 夹具：残句缺词（bookform_hole）

**期望**：`bash scripts/chapter.sh "scripts/tests/bookform_hole/ch01 test.md"` → **rc=1**，输出含
`残句缺词 1` 与 `❌ 残句缺词：… 「…把 吉隆坡 的 写成 南迪妮 的日常…」`。

**防的是什么**：2026-10-21 `finding-darla` 修复方把 `""` 填了字、句子仍读不通（「把 吉隆坡 的 写成…」
少了宾语），而 `check_chinese_layer` 只数汉字 ⇒ 门禁全绿。判据：**`的` 后直接跟动词/连词 = 缺词**。

**反向对照**：`fitcher-s-bird` / `capture` / `the-dues` / `fabulous-bodies` 全部 0 处；全库 551 本只命中 finding-darla。
