# Alpha-Sight

**类型**: 自研Skill

**评分**: 4/5

**领域**: 产品开发

**描述**: Scientific Research Engineering Assistant for analyzing arXiv papers and reproducing code

## 主要功能
- 从arXiv获取论文元数据和PDF
- 分析论文内容（浅层、中等、深层三个深度）
- 生成综合分析报告
- 可选的代码复现（官方仓库或自实现）
- 项目适配度评估

## 依赖要求
- Python >= 3.9
- 工具: uv, git
- 可选: docker
- API: arXiv API, Semantic Scholar API

## 参数
- `--depth`: shallow/medium/deep (默认: medium)
- `--language`: english/chinese (默认: english)
- `--cleanup`: on-success/always/never (默认: on-success)

## 环境变量
- SEMANTIC_SCHOLAR_API_KEY (可选)

## 链接
- **原始路径**: `D:\University\Junior\MiraclePlus\code\miracleplus-skills\alpha-sight`
- **GitHub**: [待添加]
- **飞书文档**: [待添加]
