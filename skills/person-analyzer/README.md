# Person Analyzer

深度人物传记分析工具，系统化地研究和分析各领域影响力人物的完整人生轨迹。

## 功能特点

- **七维度深度分析**: 原生家庭、求学经历、工作经历、职业里程碑、学习能力、人生轨迹、成功逻辑
- **多领域支持**: 创业者、科学家、艺术家、政治家、运动员等
- **交叉验证**: 从多个来源验证信息，确保数据可信度
- **可视化时间线**: 生成人生轨迹的时间和空间维度图表
- **多语言报告**: 支持中英文报告生成

## 快速开始

### 1. 安装依赖

```bash
cd .claude/skills/person-analyzer
uv sync
```

### 2. 配置环境变量（可选）

```bash
cp .env.example .env
# 编辑 .env 文件，添加 API keys（可选，主要使用 Google AI Mode）
```

### 3. 使用示例

```bash
# 分析创业者
"分析马斯克的人生轨迹"

# 深度分析科学家
"Analyze Richard Feynman --domain=scientist --depth=deep --language=english"

# 分析艺术家并生成时间线
"研究周杰伦 --domain=artist --timeline=on"
```

## 参数说明

### --domain

分析领域：
- `entrepreneur`: 创业者（默认）
- `scientist`: 科学家
- `artist`: 艺术家
- `politician`: 政治家
- `athlete`: 运动员
- `all`: 通用分析

### --depth

分析深度：
- `shallow`: 基础传记和关键里程碑（10分钟）
- `medium`: 完整七维度分析（30分钟，默认）
- `deep`: 深度分析 + 交叉验证 + 时间线可视化（60分钟）

### --language

报告语言：
- `chinese`: 中文报告（默认）
- `english`: 英文报告

### --timeline

时间线生成：
- `on`: 生成可视化时间线（默认）
- `off`: 仅文本报告

## 七维度分析框架

### 1. 原生家庭：底层操作系统
- 出生日期、籍贯
- 父母背景、教育、职业、成就
- 家庭社会阶层和资本
- 三代以内直系亲属影响
- 特殊童年经历
- 三观、三格、思维模型、行为习惯的塑造

### 2. 求学经历
- 教育时间线（小学、中学、大学）
- 学业表现
- 学生领导力
- 在校商业尝试
- 影响深远的阅读
- 对底层操作系统的影响

### 3. 工作经历
- 职业时间线
- 每段工作的详细信息
- 职业技能、认知、人脉的积累
- 经验教训和反思

### 4. 职业里程碑（根据领域调整）
- 创业者：创业历程、融资、团队、高光/至暗时刻
- 科学家：研究突破、学术合作、荣誉
- 艺术家：代表作品、风格演变、艺术认可
- 政治家：政治理念、重要政绩、领导力
- 运动员：训练历程、重大比赛、突破性成就

### 5. 学习能力
- 持续学习方式和方法
- 拜师经历
- 核心朋友圈（3-5人）
- 认知跃迁和成长
- 高人开悟和觉醒时刻
- 贵人相助
- 智慧升级

### 6. 人生轨迹图
- 时间维度：社会阶层变化
- 空间维度：地理位置迁移
- 关键节点分析：
  - 面临的问题
  - 思考过程
  - 采取的行动
  - 产生的结果
  - 对人生方向的影响

### 7. 成功逻辑与启示
- 成功的底层逻辑
- 可复制的模式
- 不可复制的因素
- 对同领域人士的启示

## 数据来源

### 主要来源
- **Google AI Mode**: 主要数据源，获取最新信息
- **Tavily API**: 备用搜索引擎
- **Firecrawl API**: 备用网页抓取工具

### 数据类型
- 维基百科 / 百度百科
- LinkedIn / 专业档案
- 官方网站 / 个人博客
- 新闻文章和采访
- 学术档案（科学家）
- 传记和自传

## 可信度评估

### 来源可信度评分
- 官方来源（官网、认证采访、自传）: 100分
- 高可信度来源（维基百科、主流新闻、学术档案）: 80分
- 中等可信度来源（博客、认证社交媒体、行业出版物）: 60分
- 低可信度来源（社交媒体、论坛）: 40分

### 交叉验证
- 从多个来源验证同一事实
- 标记信息冲突
- 优先采用高可信度来源
- 标记未验证信息

## 输出文件

### 报告
- 路径: `reports/{domain}/{person_name}_analysis_{zh|en}.md`
- 格式: Markdown
- 包含: 完整七维度分析、可信度评估、数据来源

### 数据文件
- 路径: `data/{person_name}/`
- 包含:
  - `biography.json`: 基础传记信息
  - `sources.json`: 来源URL和可信度
  - `timeline.json`: 人生事件时间线
  - `validation.json`: 交叉验证结果
  - `dimensions/`: 各维度详细数据

### 索引
- 路径: `index.json`
- 包含: 所有分析的历史记录和统计信息

## 目录结构

```
person-analyzer/
├── .env                        # 环境配置
├── .env.example                # 环境配置示例
├── skill.md                    # Skill 定义
├── README.md                   # 本文件
├── pyproject.toml              # Python 依赖
├── config/
│   └── domain_templates.json  # 领域特定问题模板
├── reports/                    # 生成的报告
│   ├── entrepreneur/
│   ├── scientist/
│   ├── artist/
│   ├── politician/
│   ├── athlete/
│   └── general/
├── data/                       # 原始传记数据
│   └── {person_name}/
│       ├── biography.json
│       ├── sources.json
│       ├── timeline.json
│       ├── validation.json
│       └── dimensions/
├── cache/                      # 缓存的搜索结果
├── assets/                     # 资源文件
│   ├── report_template_zh.md  # 中文报告模板
│   └── report_template_en.md  # 英文报告模板
├── scripts/                    # Python 脚本
│   ├── config_loader.py       # 配置加载器
│   ├── data_processor.py      # 数据处理器
│   ├── report_generator.py    # 报告生成器
│   └── index_manager.py       # 索引管理器
├── references/                 # 参考文档
└── index.json                  # 分析索引
```

## 注意事项

1. **优先使用 Google AI Mode**: 这是获取最新信息的首选方式
2. **交叉验证关键事实**: 从多个来源验证重要信息
3. **尊重速率限制**: 遵守所有数据源的API限制
4. **引用来源**: 在报告中为所有声明提供来源
5. **更新索引**: 每次分析后更新 index.json
6. **定期清理缓存**: 节省存储空间
7. **标记不确定信息**: 在报告中清楚标记未验证的信息
8. **根据领域调整**: 基于 domain 参数调整问题
9. **保护 API 密钥**: 永远不要在报告或日志中暴露

## 示例输出

分析完成后，你将看到：

```
✓ 人物分析完成!

人物: Elon Musk
领域: entrepreneur
分析深度: medium
可信度评分: 87/100

📊 数据统计:
- 来源数量: 45
- 验证事实: 120
- 发现冲突: 3
- 关键节点: 12

📄 报告: person-analyzer/reports/entrepreneur/Elon_Musk_analysis_zh.md
🗂️ 索引: person-analyzer/index.json

🔑 核心发现:
- 原生家庭赋予的工程师思维和冒险精神
- 从 Zip2 到 PayPal 的连续创业经验积累
- 第一性原理思维在 SpaceX 和 Tesla 的应用
```

## 贡献

欢迎提交问题和改进建议！

## 许可证

MIT License
