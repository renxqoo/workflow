# 浏览器功能地图

| 改动面 | 用例和命令 | 证明内容 | 前置与限制 |
| --- | --- | --- | --- |
| 模型目录 | `npm run e2e e2e/catalog.spec.js` | 分类筛选、详情入口；上游故障时仍显示所有分类 | 无 |
| 移动菜单 | `npm run e2e e2e/navigation.spec.js` | 菜单导航与焦点均通过 | 390px 视口 |
| 旧首页入口 | `npm run e2e e2e/legacy.spec.js` | `/home-v2` 跳转到根路径 | 无 |
