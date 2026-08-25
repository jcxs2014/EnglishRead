// explorer-drawer-close.inline.ts
// 小屏 drawer 拦截：点击 nav-file-title 后自动关闭抽屉，避免用户点击文章标题后
// 仍需手动点击汉堡菜单的体验断层
// 由 Head 组件加载（参见 quartz/components/Head.tsx 引入方式）

function closeMobileDrawerIfOpen() {
  const drawer = document.querySelector(".explorer")
  if (!drawer) return
  if (drawer.classList.contains("collapsed")) return
  drawer.classList.add("collapsed")
  drawer.setAttribute("aria-expanded", "false")
  document.documentElement.classList.remove("mobile-no-scroll")
}

function attachDrawerCloseOnLinkClick() {
  document.querySelectorAll(".nav-file-title").forEach((link) => {
    link.addEventListener("click", () => closeMobileDrawerIfOpen())
  })
  // 文件夹按钮点击也收起抽屉（折叠展开场景）
  document.querySelectorAll(".folder-button").forEach((btn) => {
    btn.addEventListener("click", () => closeMobileDrawerIfOpen())
  })
}

// SPA 导航后 DOM 替换，需要重新绑定
function rebindAfterNav() {
  // 当前 drawer 切换走 document 上的 nav 事件（Quartz 原生 SPA）
  attachDrawerCloseOnLinkClick()
}

// SPA 模式：在 nav / render 后重新绑定
document.addEventListener("nav", rebindAfterNav)
document.addEventListener("render", rebindAfterNav)

// 首次加载
attachDrawerCloseOnLinkClick()

// 监听全 body 点击（事件委托），即使 SPA 替换后未及时重绑也能兜底
document.body.addEventListener(
  "click",
  (e) => {
    const target = e.target as HTMLElement
    if (!target) return
    const link = target.closest(".nav-file-title, .folder-button")
    if (!link) return
    closeMobileDrawerIfOpen()
  },
  true,
)
