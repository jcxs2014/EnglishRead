# C-symlinks.md · 增量复核任务 C · 软链来源（只记录，不追究）

- 范围：`$B` = `notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell`
- 任务：只回答「现在有没有残留、有没有断链」——**不为找来源花时间**。

## 一 · 三条命令的实测

```bash
cd ~/Documents/Works/EnglishRead
B=notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell

$ git ls-files -s "$B" | awk '$1=="120000"' | wc -l
0

$ ls "$B"/*.md | wc -l
57

$ ls "$B" | wc -l
59
```

| 项 | 期望 | 实测 | 结论 |
|---|---|---|---|
| git mode `120000`（软链）条目 | 0 | **0** | ✔ 无残留 |
| `ls "$B"/*.md \| wc -l` | 指令写「54 章」 | **57** | ⇒ **57 = 54 章 + 三篇总览**，**不是缺件**（见下方口径说明） |
| `ls "$B" \| wc -l` | 59 | **59** | ✔ 与指令一致（57 + `library` + `text`） |

### 口径说明（§三 那行注释的修正）

指令 §三 写「`ls "$B"/*.md | wc -l` → 54 章」，**这一行注释写错了**：该命令统计的是**全部 `.md`**，而书目录里有 **54 章 + 3 篇总览（`00_概述.md` / `00_情感节点.md` / `00_金句精选.md`）= 57**。拆分核对：

```bash
$ ls "$B" | grep '^ch[0-9]' | wc -l
54
$ ls "$B" | grep '^00_' | wc -l
3
```

⇒ **54 章齐、3 篇总览齐、总计 57**，不是差异、不是缺件。（与「执行前补记」第 1 条一致。）

章号连续性：

```bash
$ ls "$B" | grep '^ch[0-9]' | sed 's/ .*//' | sort | tr '\n' ' '
ch01 ch02 ch03 ch04 ch05 ch06 ch07 ch08 ch09 ch10 ch11 ch12 ch13 ch14 ch15 ch16 ch17
ch18 ch19 ch20 ch21 ch22 ch23 ch24 ch25 ch26 ch27 ch28 ch29 ch30 ch31 ch32 ch33
ch34 ch35 ch36 ch37 ch38 ch39 ch40 ch41 ch42 ch43 ch44 ch45 ch46 ch47 ch48 ch49
ch50 ch51 ch52 ch53 ch54
```

⇒ **ch01–ch54 无缺号、无重号**。

## 二 · 断链检查

```bash
$ find "$B" -type l | wc -l
0
```

⇒ **书目录内连软链文件本身都不存在**（不是「软链在但指空」），自然**无断链**。

## 三 · 全库层面的附带观察（不属于本书，不处理）

```bash
$ git ls-files -s | awk '$1=="120000"' | wc -l
0

$ find . -type l -not -path './.git/*' | wc -l
17

$ find . -type l -not -path './.git/*' ! -exec test -e {} \; -print
./sync_memory.sh
./check_collab.sh
./setup_multi_ide.sh
```

- 全库 **17 个软链**，其中 **3 个已断**（`sync_memory.sh` / `check_collab.sh` / `setup_multi_ide.sh`，均指向 `/Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/`）。
- 这 3 个**与本书无关**：位于**仓库根目录**，且 `git ls-files -s` 对它们返回空 ⇒ **未被 git 跟踪**（`git log --oneline -- sync_memory.sh` 显示 `ab56229e9 gitignore: 添加符号链接，移除追踪（跨机器路径不同不适用 git）`）。
- 其余 14 个在 `site/node_modules/` 下，属依赖目录，与内容无关。
- **本次不处理、不追责**（§三 明令「只记录，不追究」）。

## 四 · 一句话结论

**那 53 个无扩展名孪生软链已彻底清除：书目录内 git mode `120000` 条目 = 0、文件系统内软链 = 0、断链 = 0；54 章（ch01–ch54 无缺号）＋ 3 篇总览 ＝ 57 个 `.md` 齐备，目录条目 59 与指令一致；无残留、无断链。**

（另记：全库根目录有 3 个与本书无关的断链脚本软链，均未被 git 跟踪，不在本次范围内。）

## 五 · 档位

**通过**（无缺陷，无阻断/提示/假红；未追查软链来源——按 §三 指示）。
