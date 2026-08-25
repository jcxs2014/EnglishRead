// explorer-drawer-close.inline.ts
// 小屏抽屉：点击目录内文章/文件夹后自动收起（Quartz 原生仅汉堡按钮可切换）
// 单一事件委托，SPA 导航无需重绑；加载顺序须在 spa router 之前

document.addEventListener(
  "click",
  (e) => {
    const target = e.target as HTMLElement | null
    if (!target?.closest(".nav-file-title, .folder-button")) return
    const drawer = document.querySelector(".explorer")
    if (!drawer || drawer.classList.contains("collapsed")) return
    drawer.classList.add("collapsed")
    drawer.setAttribute("aria-expanded", "false")
    document.documentElement.classList.remove("mobile-no-scroll")
  },
  true,
)
