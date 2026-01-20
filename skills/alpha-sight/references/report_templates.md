# Report Templates

This document contains the complete report templates for both Chinese and English analysis reports.

## Table of Contents

- [Chinese Report Template](#chinese-report-template)
- [English Report Template](#english-report-template)
- [Template Variables](#template-variables)
- [Usage Guidelines](#usage-guidelines)

## Chinese Report Template

```markdown
# 论文深度分析报告：{Title}

## 基本信息
- **arXiv ID**: {arxiv_id}
- **发布日期**: {published_date}
- **作者**: {authors}
- **分类**: {categories}
- **项目主页**: {project_homepage} (如果有)

## 摘要

**核心创新点**: {one_sentence_summary}

{abstract_in_chinese_if_needed}

## 论文的Motivation分析

{分析论文想要解答的核心问题以及驱动解决问题的动力。包括：}
- 现有方法的局限性
- 待解决的关键问题
- 研究的必要性和重要性

## 论文的主要贡献点分析

1. **{贡献点1标题}**
   - {详细描述}
   - {技术细节}
   - {创新之处}

2. **{贡献点2标题}**
   - {详细描述}
   - {技术细节}
   - {创新之处}

3. **{贡献点3标题}**
   - {详细描述}
   - {技术细节}
   - {创新之处}

{根据实际情况添加更多贡献点}

## 技术细节深度分析

### 1. 核心架构

{描述论文提出的核心架构设计，包括：}
- 整体架构图（使用 Mermaid 或文字描述）
- 各模块功能
- 模块间交互关系

### 2. 关键算法

{详细描述核心算法，包括：}
- 算法伪代码或数学公式
- 算法复杂度分析
- 与现有方法的对比

### 3. 实现细节

{描述重要的实现细节，包括：}
- 数据预处理方法
- 模型训练策略
- 超参数设置
- 优化技巧

### 4. 技术创新点

{突出论文的技术创新，包括：}
- 新颖的设计思路
- 独特的技术手段
- 创新的应用方式

## 实验设计与验证分析

### 核心主张

{论文的核心假设和主要声明，例如：}
- 假设1：{描述}
- 假设2：{描述}
- 主要声明：{描述}

### 数据集与基线

**数据集**:
- {数据集名称1}: {规模、特点、用途}
- {数据集名称2}: {规模、特点、用途}

**基线方法**:
- {基线方法1}: {简要描述}
- {基线方法2}: {简要描述}

**实验环境**:
- 硬件: {GPU型号、数量等}
- 软件: {框架版本、依赖库等}

### 评价指标

{描述使用的评价指标及其合理性：}
- **{指标1}**: {定义、计算方法、为何选择}
- **{指标2}**: {定义、计算方法、为何选择}

### 实验结果

{总结主要实验结果，包括：}

**主要结果表格**:

| 方法 | {指标1} | {指标2} | {指标3} |
|------|---------|---------|---------|
| {基线1} | {值} | {值} | {值} |
| {基线2} | {值} | {值} | {值} |
| **本文方法** | **{值}** | **{值}** | **{值}** |

**关键发现**:
1. {发现1}
2. {发现2}
3. {发现3}

### 消融实验

{如果论文包含消融实验，描述：}
- 实验设计
- 各组件的贡献
- 关键组件分析

### 结论和定量分析

{基于实验结果的结论和关键定量分析：}
- 性能提升幅度
- 统计显著性
- 与理论预期的对比
- 局限性分析

## 项目契合度评估

> **注意**: 仅在 `depth=medium` 或 `depth=deep` 时包含此章节

### 相关性评分：{X}/10

{评估论文与当前项目的相关性，考虑：}
- 技术栈重叠度
- 应用场景相似度
- 实施可行性
- 预期收益

### 技术重叠

**当前项目技术栈**:
- {技术1}
- {技术2}
- {技术3}

**论文使用技术**:
- {技术1}
- {技术2}
- {技术3}

**重叠分析**:
{分析哪些技术可以直接复用，哪些需要适配}

### 潜在应用

1. **{应用场景1}**
   - 应用方式: {描述}
   - 预期效果: {描述}
   - 实施难度: {低/中/高}

2. **{应用场景2}**
   - 应用方式: {描述}
   - 预期效果: {描述}
   - 实施难度: {低/中/高}

## 实施建议

### 短期建议（1-2周）

1. **{建议1}**
   - 具体步骤: {描述}
   - 所需资源: {描述}
   - 预期产出: {描述}

2. **{建议2}**
   - 具体步骤: {描述}
   - 所需资源: {描述}
   - 预期产出: {描述}

### 中期建议（1-2月）

1. **{建议1}**
   - 具体步骤: {描述}
   - 所需资源: {描述}
   - 预期产出: {描述}

### 长期建议（3月以上）

1. **{建议1}**
   - 具体步骤: {描述}
   - 所需资源: {描述}
   - 预期产出: {描述}

## 代码复现状态

- **状态**: {成功/失败/部分成功/未尝试}
- **方法**: {官方仓库/自实现/无}
- **仓库地址**: {URL或"未找到"}
- **迭代次数**: {N次}
- **成功率**: {X%}
- **备注**: {详细说明}

### 复现过程

{如果进行了代码复现，描述：}
1. **第1次迭代**: {尝试内容、遇到的问题、解决方案}
2. **第2次迭代**: {尝试内容、遇到的问题、解决方案}
...

### 复现结果

{如果复现成功，提供：}
- 运行命令
- 输出结果
- 性能对比
- 代码路径: `./alpha-sight/sandbox/{arxiv_id}_reproduction/`

## 架构对比

{使用 Mermaid 图表对比论文方法与当前项目架构}

### 论文架构

\`\`\`mermaid
graph TD
    A[输入] --> B[模块1]
    B --> C[模块2]
    C --> D[输出]
\`\`\`

### 当前项目架构

\`\`\`mermaid
graph TD
    A[输入] --> B[现有模块1]
    B --> C[现有模块2]
    C --> D[输出]
\`\`\`

### 集成方案

\`\`\`mermaid
graph TD
    A[输入] --> B[现有模块1]
    B --> C[论文方法集成点]
    C --> D[现有模块2]
    D --> E[输出]
\`\`\`

## 相关论文

{如果有引用数据，列出相关论文：}

1. **{论文标题1}** (arXiv:{id})
   - 关系: {引用/被引用/相关}
   - 简介: {一句话描述}

2. **{论文标题2}** (arXiv:{id})
   - 关系: {引用/被引用/相关}
   - 简介: {一句话描述}

## 引用信息

- **被引用次数**: {count} (截至 {date})
- **参考文献数**: {count}
- **Semantic Scholar**: {URL}
- **arXiv**: https://arxiv.org/abs/{arxiv_id}

## 标签

{tags_list}

---

**报告生成时间**: {timestamp}
**分析深度**: {depth}
**生成工具**: Alpha-Sight v1.0
**PDF路径**: `./alpha-sight/papers/{arxiv_id}.pdf`
```

## English Report Template

```markdown
# Paper Analysis Report: {Title}

## Basic Information

- **arXiv ID**: {arxiv_id}
- **Published**: {published_date}
- **Authors**: {authors}
- **Categories**: {categories}
- **Project Homepage**: {project_homepage} (if available)

## Abstract

**Core Innovation**: {one_sentence_summary}

{original_abstract}

## Motivation Analysis

{Analyze the core problem the paper aims to solve and the driving forces, including:}
- Limitations of existing methods
- Key problems to be addressed
- Necessity and importance of the research

## Main Contributions Analysis

1. **{Contribution 1 Title}**
   - {Detailed description}
   - {Technical details}
   - {Innovation aspects}

2. **{Contribution 2 Title}**
   - {Detailed description}
   - {Technical details}
   - {Innovation aspects}

3. **{Contribution 3 Title}**
   - {Detailed description}
   - {Technical details}
   - {Innovation aspects}

{Add more contributions as needed}

## In-depth Technical Analysis

### 1. Core Architecture

{Describe the core architecture proposed in the paper, including:}
- Overall architecture diagram (using Mermaid or text description)
- Module functionalities
- Inter-module interactions

### 2. Key Algorithms

{Describe core algorithms in detail, including:}
- Algorithm pseudocode or mathematical formulas
- Algorithm complexity analysis
- Comparison with existing methods

### 3. Implementation Details

{Describe important implementation details, including:}
- Data preprocessing methods
- Model training strategies
- Hyperparameter settings
- Optimization techniques

### 4. Technical Innovations

{Highlight technical innovations in the paper, including:}
- Novel design ideas
- Unique technical approaches
- Innovative application methods

## Experimental Design and Validation Analysis

### Core Claims

{Core hypotheses and main claims of the paper, such as:}
- Hypothesis 1: {description}
- Hypothesis 2: {description}
- Main claim: {description}

### Datasets and Baselines

**Datasets**:
- {Dataset name 1}: {scale, characteristics, purpose}
- {Dataset name 2}: {scale, characteristics, purpose}

**Baseline Methods**:
- {Baseline 1}: {brief description}
- {Baseline 2}: {brief description}

**Experimental Setup**:
- Hardware: {GPU model, quantity, etc.}
- Software: {framework versions, dependencies, etc.}

### Evaluation Metrics

{Describe evaluation metrics and their rationale:}
- **{Metric 1}**: {definition, calculation method, why chosen}
- **{Metric 2}**: {definition, calculation method, why chosen}

### Experimental Results

{Summarize main experimental results, including:}

**Main Results Table**:

| Method | {Metric 1} | {Metric 2} | {Metric 3} |
|--------|------------|------------|------------|
| {Baseline 1} | {value} | {value} | {value} |
| {Baseline 2} | {value} | {value} | {value} |
| **Proposed** | **{value}** | **{value}** | **{value}** |

**Key Findings**:
1. {Finding 1}
2. {Finding 2}
3. {Finding 3}

### Ablation Studies

{If the paper includes ablation studies, describe:}
- Experimental design
- Contribution of each component
- Key component analysis

### Conclusions and Quantitative Analysis

{Conclusions based on experimental results and key quantitative analysis:}
- Performance improvement magnitude
- Statistical significance
- Comparison with theoretical expectations
- Limitation analysis

## Project Fit Assessment

> **Note**: Only included when `depth=medium` or `depth=deep`

### Relevance Score: {X}/10

{Assess the relevance of the paper to the current project, considering:}
- Technology stack overlap
- Application scenario similarity
- Implementation feasibility
- Expected benefits

### Technology Overlap

**Current Project Tech Stack**:
- {Tech 1}
- {Tech 2}
- {Tech 3}

**Paper Technologies**:
- {Tech 1}
- {Tech 2}
- {Tech 3}

**Overlap Analysis**:
{Analyze which technologies can be directly reused and which need adaptation}

### Potential Applications

1. **{Application Scenario 1}**
   - Application method: {description}
   - Expected effect: {description}
   - Implementation difficulty: {Low/Medium/High}

2. **{Application Scenario 2}**
   - Application method: {description}
   - Expected effect: {description}
   - Implementation difficulty: {Low/Medium/High}

## Implementation Suggestions

### Short-term Suggestions (1-2 weeks)

1. **{Suggestion 1}**
   - Specific steps: {description}
   - Required resources: {description}
   - Expected output: {description}

2. **{Suggestion 2}**
   - Specific steps: {description}
   - Required resources: {description}
   - Expected output: {description}

### Medium-term Suggestions (1-2 months)

1. **{Suggestion 1}**
   - Specific steps: {description}
   - Required resources: {description}
   - Expected output: {description}

### Long-term Suggestions (3+ months)

1. **{Suggestion 1}**
   - Specific steps: {description}
   - Required resources: {description}
   - Expected output: {description}

## Reproduction Status

- **Status**: {success/failed/partial/not_attempted}
- **Method**: {official_repo/self_implemented/none}
- **Repository URL**: {URL or "not found"}
- **Iterations**: {N times}
- **Success Rate**: {X%}
- **Notes**: {detailed explanation}

### Reproduction Process

{If code reproduction was performed, describe:}
1. **Iteration 1**: {attempt content, problems encountered, solutions}
2. **Iteration 2**: {attempt content, problems encountered, solutions}
...

### Reproduction Results

{If reproduction succeeded, provide:}
- Run commands
- Output results
- Performance comparison
- Code path: `./alpha-sight/sandbox/{arxiv_id}_reproduction/`

## Architecture Comparison

{Use Mermaid diagrams to compare paper method with current project architecture}

### Paper Architecture

\`\`\`mermaid
graph TD
    A[Input] --> B[Module 1]
    B --> C[Module 2]
    C --> D[Output]
\`\`\`

### Current Project Architecture

\`\`\`mermaid
graph TD
    A[Input] --> B[Existing Module 1]
    B --> C[Existing Module 2]
    C --> D[Output]
\`\`\`

### Integration Plan

\`\`\`mermaid
graph TD
    A[Input] --> B[Existing Module 1]
    B --> C[Paper Method Integration Point]
    C --> D[Existing Module 2]
    D --> E[Output]
\`\`\`

## Related Papers

{If citation data available, list related papers:}

1. **{Paper Title 1}** (arXiv:{id})
   - Relationship: {cites/cited_by/related}
   - Summary: {one-sentence description}

2. **{Paper Title 2}** (arXiv:{id})
   - Relationship: {cites/cited_by/related}
   - Summary: {one-sentence description}

## Citation Information

- **Cited by**: {count} (as of {date})
- **References**: {count}
- **Semantic Scholar**: {URL}
- **arXiv**: https://arxiv.org/abs/{arxiv_id}

## Tags

{tags_list}

---

**Report Generated**: {timestamp}
**Analysis Depth**: {depth}
**Generated by**: Alpha-Sight v1.0
**PDF Path**: `./alpha-sight/papers/{arxiv_id}.pdf`
```

## Template Variables

Replace these placeholders when generating reports:

### Basic Information
- `{Title}` - Paper title
- `{arxiv_id}` - arXiv ID (e.g., 2401.12345)
- `{published_date}` - Publication date
- `{authors}` - Comma-separated author list
- `{categories}` - arXiv categories (e.g., cs.LG, cs.AI)
- `{project_homepage}` - Project homepage URL (if available)

### Content
- `{one_sentence_summary}` - One-sentence core innovation summary
- `{abstract_in_chinese_if_needed}` - Chinese translation of abstract (for Chinese reports)
- `{original_abstract}` - Original English abstract (for English reports)

### Analysis
- `{X}` - Relevance score (1-10)
- `{depth}` - Analysis depth (shallow/medium/deep)
- `{timestamp}` - Report generation timestamp

### Reproduction
- `{status}` - Reproduction status (success/failed/partial/not_attempted)
- `{method}` - Reproduction method (official_repo/self_implemented/none)
- `{URL}` - Repository URL
- `{N}` - Number of iterations
- `{count}` - Citation count

### Tags
- `{tags_list}` - Comma-separated tags

## Usage Guidelines

### When to Use Each Template

- **Chinese Template**: Use when `--language=chinese` parameter is set
- **English Template**: Use when `--language=english` parameter is set (default)

### Sections to Include Based on Depth

**depth=shallow**:
- Basic Information
- Abstract
- Main Contributions Analysis (brief)
- Citation Information
- Tags

**depth=medium**:
- All shallow sections
- Motivation Analysis
- Technical Details (overview)
- Experimental Design (summary)
- Project Fit Assessment
- Implementation Suggestions (high-level)

**depth=deep**:
- All medium sections
- In-depth Technical Analysis (complete)
- Experimental Design and Validation (complete)
- Reproduction Status
- Reproduction Process
- Architecture Comparison
- Related Papers

### Best Practices

1. **Be Concise**: Focus on key insights, avoid verbosity
2. **Use Bullet Points**: For lists and structured information
3. **Include Diagrams**: Use Mermaid for architecture comparisons
4. **Quantify When Possible**: Include specific numbers and metrics
5. **Link to Sources**: Reference specific sections in the paper
6. **Highlight Innovations**: Clearly mark novel contributions
7. **Be Honest**: Note limitations and challenges
8. **Provide Context**: Explain why findings matter for the project

### Mermaid Diagram Tips

- Keep diagrams simple and focused
- Use consistent node naming
- Add comments for clarity
- Test diagrams render correctly
- Use appropriate diagram types (graph, flowchart, sequence, etc.)

### Language-Specific Notes

**Chinese Reports**:
- Keep technical terms in English with Chinese annotations
- Use Chinese punctuation (，。！？)
- Provide context for international readers
- Translate key concepts clearly

**English Reports**:
- Use clear, professional English
- Define technical terms on first use
- Follow academic writing conventions
- Be precise and unambiguous
