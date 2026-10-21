# 骨架层语言判据的阴性对照夹具（必须 rc=1）

**为什么要有这一份**：`check_chinese_layer.py` 在 2026-10-21 之前只查引语块下的四个字段
（中文理解 / 句子结构 / 关键词 / 为什么这样写），**`## 本章导航` 与 `## 一句话总结` 完全在口径外**。
实测 don-t-leave-her-alone：18 lane 全绿，而 ch11–ch17 的「一句话总结」散文中文占比只有 4%–11%。
补判据时若把标题名写错（例如写成「本章导览」）或正则没吃到列表项，本夹具必须仍然报红。

## 预期（阴性对照，必须 rc=1）

```
❌ 导航非中文：1 处
❌ 总结非中文：1 处
```

运行：

```bash
python3 scripts/check_chinese_layer.py scripts/tests/chinese_layer_nav; echo "rc=$?"
```
