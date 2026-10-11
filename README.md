# workflow

通用 agent skill 集合。不绑定特定项目，任何 git 仓库可用。

## skills

| skill | 用途 |
| --- | --- |
| [pr-review-loop](skills/pr-review-loop/SKILL.md) | PR 建立后的对抗审查-修复-复查循环，直到代码可安全合并：按 diff 风险面组多路独立审查 agent（正确性恒定 + 风险路按触发条件），finding 四分类处置（修/顺手修/落档不改/驳回），修复推送后原审查者复查，循环直到全部通过；5 软轮上限 + 诊断三分类升级，防假绿抽查收口 |

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
