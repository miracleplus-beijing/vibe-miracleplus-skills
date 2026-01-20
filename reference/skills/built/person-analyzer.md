# Person-Analyzer

**类型**: 自研Skill

**评分**: 5/5

**领域**: 市场调查

**描述**: Deep biographical analysis tool for researching and analyzing life trajectories of influential figures

## 主要功能
- 深度人物传记分析
- 多源网络研究
- 生命轨迹分析(7-9个维度)
- 关键决策点识别
- 信息交叉验证
- 生成综合报告
- 时间线可视化

## 分析维度
1. 原生家庭(Family Background)
2. 求学经历(Education Journey)
3. 工作经历(Work Experience)
4. 创业经历/职业里程碑(Entrepreneurial Journey)
5. 学习能力(Learning Ability)
6. 人生轨迹图(Life Trajectory Mapping)
7. 成功逻辑(Success Logic)
8. 失败与挫折(Failures & Setbacks)
9. 人际关系网络(Relationship Network)

## 参数
- `--domain`: entrepreneur/scientist/artist/politician/athlete/all (默认: entrepreneur)
- `--depth`: shallow/medium/deep (默认: medium)
- `--language`: chinese/english (默认: chinese)
- `--timeline`: on/off (默认: on)

## 依赖要求
- httpx
- pydantic
- python-dotenv
- jinja2
- beautifulsoup4
- matplotlib

## 数据源
- Google AI Mode (主要)
- Tavily API (备用)
- Firecrawl API (补充)

## 输出
- Markdown报告
- JSON数据
- 时间线可视化

## 链接
- **原始路径**: `D:\University\Junior\MiraclePlus\code\miracleplus-skills\person-analyzer`
- **GitHub**: [待添加]
- **飞书文档**: [待添加]
