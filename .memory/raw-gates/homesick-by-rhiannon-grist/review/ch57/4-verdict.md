# ch57 4-verdict

- 文件：`ch57 worth sticking around for.md`
- 结论：**1 阻断 / 0 提示**

## 说明

**阻断 1（词汇表结构破损·渲染层）**：`## 本章词汇` 的 ⭐⭐⭐ 表在 `desiccated` 行之后被插入 3 个空行 + 一行与上句完全重复的文本（文件第 111–114 行），Markdown 表格在此处被截断，其后的 `sodden`～`wingback` 六行会脱离表格渲染成普通段落，重复行会原样显示在页面上。

```
$ sed -n '108,116p' "notes/books/novels/homesick-by-rhiannon-grist/ch57 worth sticking around for.md"
```

修法见《复核与修复指令》§3-A（删除第 111–114 行，保留第 110 行的完整行）。

## 已核实为正确

① 石头原话“still good… the right place, with the right support”；② 总监“painted teal. All eight of them.”；③ 码／句“Positive. I’m still here, aren’t I?”；④ 末句“you’re worth sticking around for.”；⑤ 新邻居问句与她替对方说完“A semi-detached?”的桥段。
