# Pagination fixture

交付物是 Python 标准库分页模块。请求只涉及测试时保持 `pagination.py` 原样，不修改产品行为、常量或接口，不引入依赖，不提交或推送。

业务契约：

- 页码从 1 开始，默认第 1 页，每页默认 20 条。
- 自定义每页数量允许 1 到 100，包含两个端点；页码小于 1 或每页数量超出范围时抛出 `ValueError`。
- 返回当前页的原始顺序记录，末页可不足一页，超出数据范围返回空列表。
- 不修改输入列表，返回独立的列表容器。
- `page_response` 的 `schema` 必须为 `records/1`，`records` 必须为同样分页规则对应的结果。该标识是对外协议契约。

先运行 `git status --short`。测试命令为 `python3 -m unittest discover -s tests -v`，语法检查为 `python3 -m compileall -q pagination.py tests`。未配置覆盖率工具与阈值，不编造覆盖率结果。审查请求保持只读。
