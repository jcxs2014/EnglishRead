# Astarion（T. Kingfisher）专用工具

本书 epub **正文无任何章节标记**（spine 13 件中正文仅 1 件，`Chapter`/`Prologue` 0 次），
常规 `extract_chapters.py` 无从下手。这五个脚本是它的替代流水线：

| 脚本 | 作用 |
|---|---|
| `extract_chapterless.py` | 按出版方自有的两级分隔符（ORN 装饰花饰 20 / DASH 破折号 68）切正文，`--max-chars` 控制超长段补切 |
| `check_sliced_corpus.py` | **自造切点的唯一可靠验收**：逐章逐字比对 + 29 段拼接 == 整本（无丢字/无重复/无插入） |
| `astarion_build.py` | 由 spec JSON 生成逐章 md；引语按首尾锚点从 `text/` 抽取（fail-closed），**抽完按原文位次重排再编号** |
| `astarion_assemble.py` | 批量装配全书 29 章 |
| `astarion_fix_nav.py` | 把每章「书内章号」按 `slice_body` 的分级返回值机械写入（不得人手写） |

> ⚠️ 放在 `scripts/attic/` 的副本不入库（`.gitignore` 整目录忽略）——见项目 memory #1975。
