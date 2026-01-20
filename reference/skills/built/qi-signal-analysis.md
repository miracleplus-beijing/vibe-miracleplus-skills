# Qi-Signal-Analysis

**类型**: 自研Skill

**评分**: 5/5

**领域**: 市场调查

**描述**: Automated analysis system for Qi Lu's X (Twitter) posts shared in Feishu group chats

## 主要功能
- 从飞书获取Qi Lu的X链接
- 爬取X内容并分类
- 内容搜索和事实核查
- Claude分析
- 生成综合报告
- 发送飞书通知
- 交互式评估系统

## 工作流程
1. Phase 1: 飞书消息获取
2. Phase 2: X内容爬取
3. Phase 3: 内容分析
4. Phase 4: 飞书Webhook通知
5. Phase 5: 交互式评估

## 参数
- `--start "YYYY-MM-DD HH:MM"`: 开始时间
- `--end "YYYY-MM-DD HH:MM"`: 结束时间
- `--fetch-only`: 仅获取数据
- `--analyze-from <json_file>`: 从现有数据分析
- `--no-send`: 跳过飞书发送
- `--verbose`: 详细日志

## 依赖要求
- uv包管理
- 多个API(Feishu, Twitter, Tavily, Firecrawl, Claude)

## 输出
- Markdown报告
- JSON数据
- 飞书文档
- 评估记录

## 链接
- **原始路径**: `D:\University\Junior\MiraclePlus\code\miracleplus-skills\qi-signal-analysis`
- **GitHub**: [待添加]
- **飞书文档**: [待添加]
