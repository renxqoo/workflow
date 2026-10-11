# workflow

通用 agent skill 集合。不绑定特定项目，任何 git 仓库可用。

## skills

| skill | 用途 |
| --- | --- |
| [to-issue](skills/to-issue/SKILL.md) | 现象 → 结构化 issue：证据工厂定位（三档纪律，档 2 复现脚本是全链路资产）+ 查重合并 + grilling 澄清（裁决标注契约，下游免重问）+ 零上下文自检发布 + 生命周期回写。止于发布，接力模式不锁定 |
| [feature-dev](skills/feature-dev/SKILL.md) | 新功能开发生产级工作流（fork 自 feature-dev-v2）：需求分级 → 方案先行 → 测试口径先定 → 小步实现四门验证 → 对抗审查 → 收口验收 |
| [pr-review-loop](skills/pr-review-loop/SKILL.md) | PR 建立后的对抗审查-修复-复查循环：风险面组路（agent 裁量路数）、finding 四分类处置、原审查者复查、共识诚实降级（同源模型先验共享）、回归用例结构化、CI/owner 收口三态 |
| [repo-migration](skills/repo-migration/SKILL.md) | 旧仓库/单体应用迁移重构到新架构的全流程方法论（fork 自 repo-migration-e2e-v2）：三件文档先行、逐模块裁决、隔离式 e2e 装置、双形态冒烟、验收核销 |
| [verify-harness](skills/verify-harness/SKILL.md) | 为仓库生成并持续维护验证装置：验证命题先讲清（四门验自洽、单测验零件、对抗审意图、本装置验「组装后的交付物在真实形态下产生声称的行为」）；资产盘点（包装复用既有 e2e/kit/fake，不另起炉灶）→ 仓库访谈五问（锚点交付物，不预设目录形态）→ 装置文档（launch/doctor/drive/evidence/cleanup + 默认/冒烟/real 三门）+ 功能地图（改动面→旅程映射）→ 自证跑通才交付；维护模式做防腐审计（源读波/活跑波/三分类处置） |

三件套流水线：**to-issue（问题定义）→ feature-dev（读 issue 实现，PR 带 Closes #N）→ pr-review-loop（审查，残留 finding 回流 to-issue）**。接力模式不锁定：人工逐段发起，或编排 agent 接管全流程（软件工厂形态）均可——每个 skill 的产出物自带下游接力指引，两种模式共用。

## 结构约定

```
skills/<skill-name>/
├── SKILL.md          # 工作流主文档（YAML frontmatter：name + description）
└── references/       # 按需加载的支撑文档（rubric / 模板 / 判断框架）
```

- SKILL.md 只留工作流骨架；维度、模板、细则全部下沉 references，
  主会话按索引表按需读；
- 每个引用 pstack 风格的写作纪律：信号清单 + 为什么 + 证据要求，
  不写「检查 X 质量」的空话；
- description 写足触发词（中英），skill 的触发完全依赖它。
