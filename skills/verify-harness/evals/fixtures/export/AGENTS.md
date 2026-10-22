# Export fixture

本项目交付 Python 标准库 CLI `report.py`，读取 CSV 金额并写 JSON 汇总。金额使用 Decimal；导出中 total 是两位小数字符串，rows 是数据行数。

已有检查：`python3 -m unittest discover -s tests` 验证计算，`python3 scripts/check_export.py --evidence-dir evidence/export` 验证真实CLI与结果文件；CI运行这两项。修改计算选择单测，修改消费入口/导出装配选择check_export；代码提交前按现有CI要求验证。无需包管理器和新增框架。

本次装置文档可放 `verify/`，沿用已有入口和证据目录；不要改产品、原测试或CI，不新增定时任务、依赖或真实服务。测试清理只处理本次临时目录，不删除 evidence。证据不包含凭证。
