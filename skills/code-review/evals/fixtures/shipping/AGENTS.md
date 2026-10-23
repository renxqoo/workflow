# Shipping review fixture

当前项目是 Python 标准库运费模块。需求见 SPEC.md，编码约束见 CODING_STANDARDS.md。

代码审查默认只读，不修改产品、测试、文档、index 或 Git refs，不提交、推送、访问网络或发布评论。必要复现可在独立进程或临时副本进行，不改变受审文件。

先看 Git 状态，并按用户指定的对象审查。已有测试入口为 `python3 -B -m unittest discover -s tests -v`；未配置构建、覆盖率或 CI，不编造相关结果。
