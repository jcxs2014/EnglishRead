# Getaway Girl 剩余修复指令

> 背景：独立审查发现 82 FAIL，已修复 12 条（7 A类虚构词 + 45 跨章例句 + 总览重命名 + 引语截断）。
> 剩余 70 条 FAIL 全为"词汇分配错误"——词条被标到了错误的章节（该词不在该章出现）。

## 当前状态

```
check_vocab: 70 FAIL / 28 WARN
verify_quotes: 113/114（ch19 已修复）
verify_overview_quotes: 25/25（总览已重命名为 00_ 前缀）
```

## 修复方案

对每条 FAIL，执行以下步骤：

1. **定位词条**：读该章 md 文件的 `## 本章词汇` 部分，找到 FAIL 对应的词条行
2. **验证该词是否在该章出现**：`grep -i "word" text/chNN_<slug>.txt`
   - 在本章出现 → 例句来自其他章节，找本章的真实例句替换
   - 不在本章出现 → 该词应移到正确章节，或替换为本章真实出现的词
3. **替换例句**：从 `text/chNN_<slug>.txt` 中 grep 该词，取一个完整句子作为新例句
4. **验证**：替换后跑 `python3 scripts/check_vocab.py notes/books/novels/getaway-girl-by-tessa-bailey` 确认 FAIL 减少

## 70 条 FAIL 清单（按章节）

```
ch10: 4 条 — tuxedo/pant/throb/whimper
ch11: 7 条 — uninhibited/fasten/knead/beckon/deja vu/squeak/whimper
ch12: 3 条 — chandelier/foyer/balcony
ch13: 6 条 — hallucination/guileless/grudging/whittled/couplehood/hallucination
ch15: 5 条 — worshipping/percussive/knuckles/hand slides/belt buckle
ch17: 5 条 — parted lips/drape/grudging/axe/stoops
ch18: 5 条 — props/abrasive/precariousness/grinding/clit
ch19: 4 条 — maniac/vindictive/garner/motorcycle
ch21: 2 条 — trail/fingertips
ch22: 1 条 — garner
ch23: 5 条 — precariousness/Relief/jealousy/cursory/preamble
ch24: 3 条 — peephole/throng/husky
ch26: 3 条 — catastrophic/ambiance/preclude
ch27: 5 条 — gutted/catastrophic/maneuvered/bereft/plaster
ch28: 1 条 — timbre
ch29: 1 条 — snare（已改 trap，但例句仍需确认）
```

## 关键文件

- 书籍目录：`notes/books/novels/getaway-girl-by-tessa-bailey/`
- epub：`library/Getaway Girl (Tessa Bailey) (Z-Library).epub`
- 文本：`text/chNN_<slug>.txt`（check_vocab 用此文件验证例句归属）
- 审查脚本：`python3 scripts/check_vocab.py notes/books/novels/getaway-girl-by-tessa-bailey`

## 注意事项

- **不要用 epub 全文搜索**——check_vocab 只检查对应章节的 text/ 文件
- **替换例句必须来自该章的 text/ 文件**，否则仍然 FAIL
- 如果某词在该章完全没有出现，需要**删除该词条**或**用本章真实出现的词替换**
- 修改后跑 check_vocab 确认 FAIL 减少再继续下一条
- 每次修改一个文件，修改前先 `read_file` 确认内容
