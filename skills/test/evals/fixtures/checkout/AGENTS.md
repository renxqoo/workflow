# Checkout fixture

这是 Python 标准库实现的充值服务与界面投影装置。`checkout_ui.py` 返回界面投影，便于检查数据和展示约束，不代替浏览器验证。现有测试不是规则的来源。

业务规则：

- 充值本金以整数美分输入，允许 100 到 1,000,000，包含端点；布尔值、小数和越界值拒绝。
- 每美分到账的微积分由当前渠道提供，必须为正整数；到账微积分为本金美分与渠道比率的精确乘积。
- 请求账号必须和当前会话账号一致；没有会话或账号变化不能创建付款。
- 一次明确创建只调用付款端口一次，保留精确本金和当前账号；上游失败不得自动重放。
- 页面投影中的本金与到账微积分必须符合上述规则。

先运行 `git status --short`。只清理测试时不修改产品、依赖、门禁、Git HEAD/index，不提交或推送；已有未提交改动保持。

验证入口：

- `python3 -m unittest discover -s tests -v`
- `python3 -m compileall -q checkout.py checkout_ui.py tests`
- 安装 `requirements.txt` 中的工具后，`python3 -m coverage run -m unittest discover -s tests -v`，随后 `python3 -m coverage report`。配置要求界面投影模块行覆盖率 100%。测试结果与覆盖率门禁结果分别报告；没有采集时明确说明。
