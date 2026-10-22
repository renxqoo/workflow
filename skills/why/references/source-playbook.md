# 来源索引

按问题与线索选择相关来源；表格是选项，不是需要逐项完成的清单。先检查当前宿主实际可用工具和参数，不假定服务已连接或某个命令存在。优先使用已授权的只读连接；访问失败时记录限制，继续不受影响的调查。

| 线索 | 参考材料 | 适用来源 |
| --- | --- | --- |
| 引入时间、评审或实现缘由 | [代码历史](sources/code-archaeology.md) | git、PR、仓库文档与测试 |
| 需求、业务约束、范围变化 | [工单](sources/linear.md) | Linear、Jira、GitHub Issues 等 |
| 设计取舍与方案记录 | [文档](sources/notion.md) | Notion、Confluence、Google Docs 等 |
| 评审之外的讨论 | [团队聊天](sources/slack.md) | Slack、Teams 等 |
| 运行故障、超时与资源限制 | [运行观测](sources/datadog.md) | Datadog、Grafana、日志与追踪等 |
| 异常、修复与受影响发布 | [错误追踪](sources/sentry.md) | Sentry、Rollbar 等 |
| 阈值、实验与产品行为 | [分析数据](sources/databricks.md) | Databricks、Snowflake、BigQuery 等 |

出现防御逻辑或事故线索时，按需补充[事故与复盘](sources/incident-postmortem.md)。来源文件名保留常见服务名，方法可用于同类系统；不能照搬其他公司的表名、字段或工具接口。
