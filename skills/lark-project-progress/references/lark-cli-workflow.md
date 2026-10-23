# lark-cli 工作流

用于执行已有表定位、建表、字段及视图调整和批量写入时查阅。命令形状已按 lark-cli 帮助核对；运行时仍以安装版本的 `--help` 和 `lark-base` 文档为准。所有变量来自用户输入、字段映射或 API 返回，不能换成技能内保存的项目链接或 ID。

## 目标与身份

默认代表用户操作并显式使用 `--as user`；用户指定应用身份时遵从其选择。认证和权限问题按 `lark-shared` 处理，不为获得访问权限自动换身份。解析 Wiki 形式的任务表链接也优先使用 Base 的 URL 解析入口。

```bash
lark-cli base +url-resolve --url "$TASK_TABLE_URL" --as user --format json
lark-cli base +table-list --base-token "$TASK_BASE_TOKEN" --as user --format json
lark-cli base +field-list --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --as user --format json
```

解析结果提供资源类型和真实 Base、table、view 坐标。链接未定位唯一表时，依据表列表和用户语义选择；仍不明确则询问。不要把 Wiki token 或整个 URL 当作 Base token。

需要解析“我”的人员身份时，按 `lark-shared` 查看当前用户；其他人通过通讯录解析，不猜人员 ID。不要输出认证密钥。

## 读取与去重

仅投影本次所需且真实存在的字段。输出文件在本次任务临时目录中使用相对路径；CLI 的 `--output` 和 `@file` 不接受绝对路径。

```bash
lark-cli base +record-list --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --field-id "$TASK_TITLE_FIELD" --field-id "$TASK_STATUS_FIELD" --format ndjson --output "$TASK_RECORDS_FILE" --as user
```

指定视图范围时增加真实 `--view-id`。整表去重时省略该参数；需要页面、负责人或说明时按已发现 schema 追加 `--field-id`。读取输出摘要中的 `records_count`、`has_more`、`next_offset`、`rev` 和范围信息。

`has_more=true` 时，保留相同查询条件，使用返回的 `next_offset` 传给 `--offset`，每块输出不同文件，直到完整。快照版本变化且可能影响匹配时，重新取得一致输入或明确范围限制。JSON 成功信封判断 `ok == true`，不检查不存在的顶层 `code`；`record_not_found`、部分失败和被忽略字段仍须单独处理。

## 明确要求新建时

先确定新表位于已有 Base，还是创建新的 Base。名称、目标容器和可用字段来自用户要求及当前盘点。仅要求空表时可直接创建结构；同时要求按代码填充待办时，先完成子功能盘点再创建和写入，不能把页面名直接当作子任务。新 Base 与首表可以一次创建，避免留下默认空表。

```bash
lark-cli base +base-create --name "$TASK_PROJECT_NAME" --table-name "$TASK_TABLE_NAME" --fields "$TASK_FIELDS_JSON" --as user --format json
lark-cli base +table-create --base-token "$TASK_BASE_TOKEN" --name "$TASK_TABLE_NAME" --fields "$TASK_FIELDS_JSON" --as user --format json
```

两条命令是不同选择，不是连续执行的固定步骤。目标文件夹或时区已明确时，按当前帮助增加对应参数。字段创建前按需读取：

```bash
lark-cli skills read lark-base references/lark-base-field-schema.md
lark-cli skills read lark-base references/lark-base-field-create.md
```

推荐的最小信息是任务名称、所属页面、进展；负责人、优先级、功能说明及日期按实际管理需求补充，不强制固定字段名。名称放在主字段；单选的页面与状态选项从本项目范围和用户偏好产生，不预填其他项目的页面清单。使用人员默认值或动态日期前核对字段协议。

已有表需要补充字段时：

```bash
lark-cli base +field-create --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --json @new-fields.json --as user --format json
```

文件内容是单个字段对象或字段对象数组，不额外包装 `fields`。只有确需变更的字段才提交；保留用户现有字段和选项。

## 页面分组

调整视图前读取当前配置，并阅读视图生命周期协议：

```bash
lark-cli skills read lark-base references/lark-base-view.md
lark-cli base +view-get --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --view-id "$TASK_VIEW_ID" --as user --format json
lark-cli base +view-get-group --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --view-id "$TASK_VIEW_ID" --as user --format json
lark-cli base +view-get-visible-fields --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --view-id "$TASK_VIEW_ID" --as user --format json
```

链接包含视图或用户指定名称时优先使用该视图。未指定时先用 `+view-list` 查找；存在唯一符合本次用途的 grid 时复用。需要按页面长期浏览但没有唯一合适视图时，可新建一个专用 grid，并先检查是否已有同用途视图，保留其他视图。只读汇报不创建视图，也不默认复制多种视图。

```bash
lark-cli base +view-create --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --json @view.json --as user --format json
lark-cli base +view-set-group --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --view-id "$TASK_VIEW_ID" --json @page-group.json --as user --format json
lark-cli base +view-set-visible-fields --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --view-id "$TASK_VIEW_ID" --json @visible-fields.json --as user --format json
```

`page-group.json` 使用 `{"group_config":[{"field":"实际页面字段","desc":false}]}` 形状。`visible-fields.json` 使用 `{"visible_fields":[...]}`，这是完整的有序列表；遗漏的原列会隐藏，因此以当前列表为基础加入本次需要的列。不要凭空覆盖筛选和排序。

## 批量同步

先在本地计算待新增、待更新和未变的记录集合。字段名或 ID 必须来自实际 schema；写入仅包含可写字段。以下 JSON 说明结构，示例名称和 ID 均需换成本次已解析的值：

```json
{
  "create_records": [
    {
      "实际任务字段": "详情资料与能力数据对接",
      "实际页面字段": ["模型详情"],
      "实际状态字段": ["实际未开始选项"]
    }
  ]
}
```

```json
{
  "update_records": {
    "实际记录ID": {
      "实际状态字段": ["实际进行中选项"]
    }
  }
}
```

```bash
lark-cli base +record-batch-create --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --json @create-records.json --as user --format json
lark-cli base +record-batch-update --base-token "$TASK_BASE_TOKEN" --table-id "$TASK_TABLE_ID" --json @update-records.json --as user --format json
```

单批最多 200 条，同一表串行写入。单选和人员字段均采用各自协议的数组结构，不能把显示名称当作人员 ID。更新为字段增量，不把未修改字段补成空值；计算字段和附件不作为普通单元格写入。用安全的 argv 或相对 JSON 文件传参，避免将 JSON 当作 shell 转义。

保存新建响应中的真实记录 ID，并在最终回查时按任务和页面核对对应关系。请求结果不明时先按本次任务集合回查，不立即再次创建；异步生效时遵循当前协议，不把立即读不到当作失败。明确部分成功时只继续未成功项。回查若无法证明记录由本轮创建，只报告已确认存在及未确认数量，不将其全部归入本轮新增。

## 验收

本轮相关写入完成后统一回查，不逐条写后立即读。核对：

- 本次目标范围是否完整；新增及更新任务的页面、名称、状态、负责人和功能说明是否符合实际计划。
- 记录是否重复或缺失；未涉及的用户字段是否保留，已被用户删除的任务是否被误恢复。
- 页面分组和可见列是否正确；汇报中的新增、更新、未变与失败数量是否与响应及记录一致。

成功响应只说明写表成功，不代表接口已经联调完成。若远端权限、确认门禁或外发范围阻断部分操作，保留已完成部分并说明剩余动作，不反复重放同一批写入。
