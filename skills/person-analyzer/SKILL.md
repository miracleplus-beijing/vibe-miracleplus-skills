---
name: person-analyzer
description: Deep biographical analysis tool for researching and analyzing life trajectories of influential figures across all domains. Systematically collects biographical data, career milestones, decision-making patterns, and life-changing moments through multi-source web research. Use when users want to understand someone's complete life journey, analyze their success patterns, or study their decision-making at critical junctures. Trigger keywords include "analyze person", "life trajectory", "biography analysis", "人物分析", "人生轨迹", "创业者分析", or when a person's name is provided with analysis intent.
---

# Person Analyzer: Deep Biographical Intelligence Tool

深度人物传记分析工具，系统化地研究和分析各领域影响力人物的完整人生轨迹。

## Quick Start

When triggered, Person Analyzer automatically:
1. Collects biographical data from multiple web sources
2. Analyzes life trajectory across 7 key dimensions
3. Identifies critical decision points and their outcomes
4. Cross-validates information from multiple sources
5. Generates comprehensive life trajectory report

## Parameters

Parse these optional parameters from user input:

- `--domain=[entrepreneur|scientist|artist|politician|athlete|all]` (default: `entrepreneur`)
  - `entrepreneur`: Focus on business and startup journey
  - `scientist`: Focus on research and academic career
  - `artist`: Focus on creative work and artistic development
  - `politician`: Focus on political career and public service
  - `athlete`: Focus on sports career and achievements
  - `all`: General analysis applicable to any domain

- `--depth=[shallow|medium|deep]` (default: `medium`)
  - `shallow`: Basic biography and key milestones (10 min timeout)
  - `medium`: Full 7-dimension analysis (30 min timeout)
  - `deep`: Deep analysis + cross-validation + timeline visualization (60 min timeout)

- `--language=[chinese|english]` (default: `chinese`)
  - `chinese`: Report in Chinese with English names preserved
  - `english`: Report in English

- `--timeline=[on|off]` (default: `on`)
  - `on`: Generate visual timeline diagrams (time + space dimensions)
  - `off`: Text-only report

## Environment Setup

### Dependency Management

This skill uses **uv** to manage Python dependencies. Before first use, install dependencies:

```bash
cd .claude/skills/person-analyzer
uv sync
```

Core dependencies include:
- `httpx` - Async HTTP client
- `pydantic` - Data validation
- `python-dotenv` - Environment variable management
- `jinja2` - Report template rendering
- `beautifulsoup4` - HTML parsing
- `matplotlib` - Timeline visualization (optional)

### Environment Variables

Check for environment variables in order of priority:
1. `./person-analyzer/.env` (project-level)
2. `~/.config/person-analyzer/.env` (global-level)
3. System environment variables

```bash
# Optional - Primarily uses Google AI Mode, these APIs are backups
TAVILY_API_KEY=xxx              # Tavily search API key (backup)
FIRECRAWL_API_KEY=xxx           # Firecrawl web scraping API key (backup)
```

**Note**: This skill primarily uses **Google AI Mode** for information search, no additional API keys required. Tavily and Firecrawl are only used as backup data sources.

### Directory Structure

Ensure the following structure exists (create if missing):

```
./person-analyzer/
├── .env                        # Environment configuration
├── config/
│   └── domain_templates.json  # Domain-specific question templates
├── reports/                    # Generated reports
│   ├── entrepreneur/
│   ├── scientist/
│   ├── artist/
│   └── general/
├── data/                       # Raw biographical data
│   └── {person_name}/
│       ├── biography.json      # Basic biographical info
│       ├── sources.json        # Source URLs and credibility
│       ├── timeline.json       # Life events timeline
│       └── validation.json     # Cross-validation results
├── cache/                      # Cached search results
└── index.json                  # Analysis index
```

## Core Workflow Overview

### Phase 1: Setup and Person Identification (Automatic)

1. **Parse User Input** - Extract person name, domain, and parameters
2. **Load Configuration** - Read environment variables and domain templates
3. **Create Directory Structure** - Create if not exists
4. **Load Analysis Index** - Read from `index.json` to check history
5. **Normalize Person Name** - Handle different name formats (Chinese/English)

**Tools**: Read (config files), Bash (create directories)

### Phase 2: Multi-Source Data Collection (Parallel Execution)

根据 `--domain` 参数并行执行数据收集。

#### 2.1 Basic Biographical Information (All Domains)

**Data Sources**:
- Wikipedia / Baidu Baike
- LinkedIn / Professional profiles
- Official websites / Personal blogs
- News articles and interviews
- Academic profiles (for scientists)

**Collection Strategy** (Priority Order):

1. **Use Google AI Mode Search** (Primary Method):
```
Skill(skill="google-ai-mode", args="{person_name} biography birth date education background family")
```

2. **Use Tavily API Search** (Backup Method):
```python
curl -X POST "https://api.tavily.com/search" \
  -H "Content-Type: application/json" \
  -d '{
    "api_key": "$TAVILY_API_KEY",
    "query": "{person_name} biography education family background",
    "search_depth": "advanced",
    "max_results": 20
  }'
```

3. **Use Firecrawl for Structured Extraction** (Supplementary):
```python
curl -X POST "https://api.firecrawl.dev/v0/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "{wikipedia_url}",
    "formats": ["markdown", "structured"],
    "extract": {
      "schema": {
        "birth_date": "string",
        "birth_place": "string",
        "education": "array",
        "family_background": "string"
      }
    }
  }'
```

**Output**: Save to `data/{person_name}/biography.json`

#### 2.2 Seven-Dimension Deep Analysis

**Note**: Detailed search strategies for all dimensions are available in `references/search_strategies.md`.

Based on the domain and the analysis framework you provided, collect data for:

##### Dimension 1: Family Background (原生家庭)

**Key Questions**:
- Birth date and place
- Parents' background, education, occupation, achievements
- Family's social class and capital
- Influence of relatives within 3 generations
- Special childhood experiences
- How family shaped their worldview and values

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 2: Education Journey (求学经历)

**Key Questions**:
- Schools attended (elementary, middle, high school, university) with dates
- Academic performance and achievements
- Leadership roles in student organizations
- Business attempts during school
- Influential books read
- Degrees obtained

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 3: Work Experience (工作经历)

**Key Questions**:
- When joined which industry and company
- Reasons for joining
- Company's scale, stage, and industry position
- Founder's entrepreneurial spirit
- Position and responsibilities
- Notable achievements and promotions
- Skills, knowledge, and network gained
- Lessons learned and reflections

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 4: Entrepreneurial Journey (创业经历 / Career Milestones)

**For Entrepreneurs**:
- How entrepreneurial dream was ignited
- How business opportunities were discovered
- How direction was determined
- How resources were integrated
- How core team was assembled
- Funding history and equity distribution
- High moments and dark moments
- Failures and lessons
- Finding the career anchor point
- Exit experiences (IPO, acquisition)

**For Other Domains** (adapt questions):
- Major career breakthroughs
- Key projects or works
- Collaborations and partnerships
- Recognition and awards
- Career turning points

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 5: Learning Ability (学习能力)

**Key Questions**:
- How they continuously learn
- Learning methods and sources
- Mentors and teachers
- Core friend circle (3-5 examples)
- Cognitive leaps and growth
- Moments of enlightenment
- How they received help from mentors
- How they upgraded their wisdom

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 6: Life Trajectory Mapping (人生轨迹图)

**Two Dimensions**:
1. **Geographic Trajectory** - Physical location changes over time
2. **Social Class Trajectory** - Status/achievement changes over time

**For Each Critical Node - 节思行果 Framework**:
- **节 (Node/Juncture)**: What problem/challenge did they face at this critical juncture?
- **思 (Thinking)**: How did they analyze and think about it? What were their considerations?
- **行 (Action)**: What specific action did they take? What was their strategy?
- **果 (Result)**: What result did it bring? What were the consequences?
- **影响 (Impact)**: How did it influence their life direction and future decisions?

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 7: Success Logic and Insights (成功逻辑)

**Analysis**:
- Underlying logic of their success
- Patterns and principles
- Insights for others in the same domain
- Transferable lessons

**Output**: Save dimension-specific data to `data/{person_name}/dimensions/`

##### Dimension 8: Failures and Setbacks Analysis (失败与挫折分析)

**Key Questions**:
- Major failures and setbacks throughout their life
- Critical mistakes and misjudgments
- How they responded to failures
- Lessons learned from failures
- How failures shaped their future decisions
- Recovery strategies and resilience patterns
- What they would do differently in hindsight

**Analysis Focus**:
- Not just highlight moments, but also dark valleys
- Failed ventures, rejected proposals, lost opportunities
- Personal crises, health issues, relationship breakdowns
- Financial difficulties, bankruptcy experiences
- Public controversies and reputation damage
- Career setbacks and demotions
- How they rebuilt after each failure

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

##### Dimension 9: Relationship Network Mapping (人际关系网络)

**Key Questions**:
- Who did they meet at each life stage?
- What relationships were formed and why?
- How did these people influence their decisions?
- What collaborations or conflicts emerged?
- How did their network evolve over time?
- Key mentors, partners, rivals, and supporters
- Network effects on their success

**For Each Life Stage**:
- **Family Network**: Parents, siblings, relatives and their influence
- **Education Network**: Teachers, classmates, study groups
- **Work Network**: Bosses, colleagues, subordinates
- **Business Network**: Co-founders, investors, advisors, competitors
- **Social Network**: Friends, mentors, community leaders
- **Professional Network**: Industry peers, association members

**Relationship Analysis**:
- **Connection Type**: Mentor, partner, competitor, supporter, critic
- **Meeting Context**: How and when they met
- **Interaction Frequency**: Regular, occasional, one-time
- **Influence Direction**: One-way or mutual influence
- **Key Moments**: Critical interactions that changed trajectory
- **Relationship Evolution**: How it changed over time
- **Network Value**: What resources/knowledge/opportunities they provided

**Search Strategy**: See `references/search_strategies.md` for detailed queries.

**Output**: Save dimension-specific data to `data/{person_name}/dimensions/`

### Phase 3: Cross-Validation and Credibility Assessment

**Critical for ensuring accuracy**:

1. **Source Credibility Scoring**:
```python
def calculate_source_credibility(source):
    score = 0

    # Official sources (highest credibility)
    if source in ["official_website", "verified_interview", "autobiography"]:
        score = 100

    # High credibility sources
    elif source in ["wikipedia", "major_news", "academic_profile"]:
        score = 80

    # Medium credibility sources
    elif source in ["blog", "social_media_verified", "industry_publication"]:
        score = 60

    # Low credibility sources
    else:
        score = 40

    return score
```

2. **Cross-Reference Validation**:
- Compare same facts from multiple sources
- Flag contradictions
- Prioritize higher credibility sources
- Mark uncertain information

3. **Event Verification**:
- Check dates consistency
- Verify company/institution existence
- Confirm public records (funding, IPO, etc.)
- Validate awards and recognitions

**Output**: Save to `data/{person_name}/validation.json`

### Phase 4: Timeline Generation (If --timeline=on)

1. **Extract All Time-Stamped Events**
2. **Create Two Visualizations**:
   - Geographic trajectory map (if matplotlib available)
   - Social class/achievement trajectory chart

3. **Generate Mermaid Diagrams** for text-based timeline

**Tools**: Python scripts with matplotlib (optional), Mermaid syntax

### Phase 5: Report Generation

Generate comprehensive report using templates from `assets/report_template_{zh|en}.md`

**CRITICAL: Use Incremental Writing to Avoid Token Limits**

Due to the length of the report, you MUST write it section by section using multiple Write tool calls. Never attempt to write the entire report in a single call.

**Writing Strategy**:
1. **Write in 9-10 separate parts** corresponding to the main sections
2. **First write**: Create the file with header and first section (执行摘要 + 一、原生家庭)
3. **Subsequent writes**: Append each section using Edit tool to add content at the end
4. **Each part should be 200-400 lines** to stay within token limits
5. **Verify each write succeeds** before moving to the next section

**Section Writing Order**:
1. Part 1: Header + 执行摘要 + 一、原生家庭
2. Part 2: 二、求学经历
3. Part 3: 三、工作经历
4. Part 4: 四、创业经历/职业里程碑
5. Part 5: 五、学习能力
6. Part 6: 六、人生轨迹图
7. Part 7: 七、成功逻辑与启示
8. Part 8: 八、失败与挫折
9. Part 9: 九、人际关系网络
10. Part 10: 十、数据可信度评估 + 数据来源 + 方法论说明 + Footer

**Implementation**:
```python
# First write - create file with initial sections
Write(file_path=report_path, content=part1_content)

# Subsequent writes - append sections
Read(file_path=report_path)  # Read current content
Edit(file_path=report_path, old_string=last_line_of_current_content, new_string=last_line + "\n\n" + part2_content)

# Repeat for all remaining parts
```


**Report Structure**:

The complete report structure with 10 major sections is defined in `assets/report_template_zh.md` (Chinese) and `assets/report_template_en.md` (English). The report includes:

1. Executive Summary (执行摘要)
2. Family Background (原生家庭)
3. Education Journey (求学经历)
4. Work Experience (工作经历)
5. Career Milestones (创业经历/职业里程碑)
6. Learning Ability (学习能力)
7. Life Trajectory (人生轨迹图)
8. Success Logic (成功逻辑与启示)
9. Failures & Setbacks (失败与挫折)
10. Relationship Network (人际关系网络)
11. Data Credibility Assessment (数据可信度评估)
12. Data Sources & Methodology (数据来源与方法论)

**Report Path**: `person-analyzer/reports/{domain}/{person_name}_analysis.md`

**Tools**: Write (first section), Edit (append subsequent sections), Read (templates)

### Phase 6: Index Update and Cleanup

1. **Update Analysis Index** (`index.json`):
```json
{
  "analyses": [
    {
      "id": "{person_name}_{date}",
      "person_name": "{name}",
      "domain": "{domain}",
      "depth": "{depth}",
      "language": "{language}",
      "generated_at": "{timestamp}",
      "report_path": "reports/{domain}/{person_name}_analysis.md",
      "credibility_score": 85,
      "stats": {
        "sources_count": 45,
        "validated_facts": 120,
        "conflicts_found": 3
      }
    }
  ],
  "last_updated": "{timestamp}"
}
```

2. **Cache Management**:
   - Store search results for deduplication
   - Clean old cache entries (>30 days)

3. **Output Summary** to user

**Tools**: Write (index.json), Bash (cleanup)

## Error Handling

### Common Errors

1. **Person Not Found**
   - Try alternative name spellings
   - Search in different languages
   - Suggest user to provide more context
   - Mark as "insufficient_data"

2. **Conflicting Information**
   - Document all versions
   - Note credibility of each source
   - Flag in report
   - Do not make assumptions

3. **API Rate Limits**
   - Implement exponential backoff
   - Spread requests over time
   - Cache results aggressively
   - Retry up to 3 times

4. **Timeout Errors**
   - Set per-phase timeouts
   - Mark incomplete sections in report
   - Preserve partial data
   - Suggest re-run with different parameters

5. **Data Source Unavailable**
   - Continue with available sources
   - Note gaps in report
   - Provide partial results
   - Suggest manual verification

### Graceful Degradation

If data sources fail:
1. Continue with remaining sources
2. Note failures in report
3. Provide partial results
4. Lower credibility score accordingly

## Performance Optimization

1. **Parallel Execution**
   - Run dimension searches in parallel
   - Use async operations where possible
   - Batch API requests

2. **Caching Strategy**
   - Cache search results (30 days)
   - Deduplicate across sources
   - Store processed data for quick regeneration

3. **Resource Limits**
   - shallow: 10 min timeout, max 50 API calls
   - medium: 30 min timeout, max 150 API calls
   - deep: 60 min timeout, max 300 API calls

## Output Format

### Success Message

```
✓ 人物分析完成!

人物: {person_name}
领域: {domain}
分析深度: {depth}
可信度评分: {score}/100

📊 数据统计:
- 来源数量: {count}
- 验证事实: {count}
- 发现冲突: {count}
- 关键节点: {count}
- 失败经历: {count}
- 关键关系: {count}

📄 报告: person-analyzer/reports/{domain}/{person_name}_analysis.md
🗂️ 索引: person-analyzer/index.json

🔑 核心发现:
- {insight_1}
- {insight_2}
- {insight_3}
```

## Tools to Use

### Claude Code Tools

- **Skill**: Call `google-ai-mode` skill for latest information (primary data source)
- **Bash**:
  - Call Python scripts for data processing
  - Call Tavily/Firecrawl APIs (backup)
  - Create directory structure
  - Clean cache
- **Read**: Read config files, templates, cached data
- **Write**: Create reports, update index, save data
- **Glob**: Find config files
- **Grep**: Search cached data

### Python Scripts

This skill provides the following Python scripts for data processing:

1. **config_loader.py** - Configuration and data loading
2. **api_client.py** - API client management
3. **data_processor.py** - Data processing and validation
4. **report_generator.py** - Report generation
5. **index_manager.py** - Index and cache management
6. **timeline_generator.py** - Timeline visualization

## Important Notes

1. **Prioritize Google AI Mode** - This is the preferred way to get latest information
2. **Always cross-validate critical facts** from multiple sources
3. **Respect rate limits** of all data sources
4. **Cite sources** for all claims in report
5. **Update index.json** after each analysis
6. **Clean cache regularly** to save space
7. **Use correct skill name**: `google-ai-mode` (call with Skill tool)
8. **Prioritize quality over quantity** - Focus on significant events
9. **Maintain objectivity** - Report facts, not opinions
10. **Flag uncertain information** clearly in report
11. **Adapt questions** based on domain parameter
12. **Protect API keys** - Never expose in reports or logs

## Writing Style Requirements - CRITICAL

**IMPORTANT: The report MUST NOT look like it was written by AI. Follow these strict guidelines:**

### Language Style
1. **Use natural, human-like language** - Write as if a professional biographer is telling a story
2. **Avoid AI clichés** - Never use phrases like:
   - "值得注意的是" (It's worth noting that)
   - "需要指出的是" (It should be pointed out that)
   - "总的来说" (In general / Overall)
   - "综上所述" (In conclusion / To sum up)
   - "不难发现" (It's not hard to see)
   - "可以说" (It can be said that)
   - "众所周知" (As we all know)
   - "毫无疑问" (Without a doubt)
   - Excessive use of "然而" (However), "因此" (Therefore), "此外" (Furthermore)
3. **Use concrete details over abstract descriptions** - Show, don't tell
4. **Vary sentence structure** - Mix short and long sentences naturally
5. **Use active voice** - Prefer "他创立了公司" over "公司被他创立"
6. **Include specific numbers, dates, and names** - Avoid vague generalizations
7. **Use colloquial expressions when appropriate** - Make it feel human and relatable

### Content Style
1. **Tell stories, not summaries** - Use narrative techniques
2. **Include contradictions and complexities** - Real people are not perfect
3. **Use direct quotes when available** - Let the person speak in their own words
4. **Show personality through details** - Habits, quirks, preferences
5. **Avoid excessive praise or hero worship** - Be balanced and objective
6. **Include failures and mistakes prominently** - Don't sugarcoat
7. **Use specific examples over general statements** - "他每天5点起床跑步" instead of "他很自律"

### Structural Style
1. **Vary paragraph lengths** - Don't make every paragraph the same length
2. **Use transitions naturally** - Connect ideas through context, not formulaic phrases
3. **Break up long sections** - Use subheadings and white space
4. **Start sections with hooks** - Grab attention, don't just state facts
5. **End sections with insights** - Leave the reader thinking

### Tone Guidelines
1. **Be conversational but professional** - Like a well-researched magazine article
2. **Show curiosity and investigation** - "Records show..." "According to..."
3. **Acknowledge uncertainty** - "Details are unclear" "Sources conflict on this point"
4. **Use rhetorical questions sparingly** - Only when genuinely thought-provoking
5. **Avoid moral judgments** - Present facts and let readers decide

### Examples of Good vs Bad Writing

**BAD (AI-like)**:
> 值得注意的是，马云在创业初期面临了诸多挑战。然而，他凭借坚韧不拔的精神和卓越的领导力，最终取得了巨大的成功。可以说，他的成功并非偶然。

**GOOD (Human-like)**:
> 1995年，马云从美国回来，脑子里装着一个疯狂的想法。他要做"中国黄页"，但没人相信互联网能赚钱。他挨家挨户推销，被拒绝了无数次。有一次，他给一个企业老板讲了三个小时，对方最后说："小马，你这个东西我看不懂，但我看你这个人还不错，给你几千块钱试试。"

**BAD (AI-like)**:
> 他的学习能力非常强，善于从失败中总结经验教训，不断提升自己的认知水平。

**GOOD (Human-like)**:
> 每次创业失败后，他都会把团队叫到一起，花一整天时间复盘。他在白板上写下三个问题：我们错在哪里？如果重来会怎么做？这次学到了什么？这些复盘笔记，他一直保存着，装了整整两个文件夹。

### Implementation in Report Generation

When generating report content using Claude:
1. **Explicitly instruct Claude to avoid AI clichés** in every prompt
2. **Request specific examples and stories** rather than summaries
3. **Ask for varied sentence structures** and natural transitions
4. **Emphasize narrative flow** over structured listing
5. **Request concrete details** with numbers, dates, and quotes
6. **Instruct to write like a professional biographer** not a report generator

### Quality Check Before Finalizing

Before saving the report, verify:
- [ ] No AI cliché phrases present
- [ ] Varied sentence lengths and structures
- [ ] Specific examples with concrete details
- [ ] Natural transitions between sections
- [ ] Balanced tone (not overly positive)
- [ ] Failures and contradictions included
- [ ] Reads like a magazine article, not a corporate report

## Example Usage

```
User: "分析马斯克的人生轨迹"
→ Triggers skill with default parameters (domain=entrepreneur, depth=medium, language=chinese)

User: "Analyze Steve Jobs --depth=deep --language=english"
→ Deep analysis of Steve Jobs in English

User: "研究费曼的成长经历 --domain=scientist"
→ Analyze Richard Feynman as a scientist

User: "分析周杰伦 --domain=artist --timeline=on"
→ Analyze Jay Chou as an artist with timeline visualization
```

## References

- [Report Templates](references/report_templates.md) - Complete Chinese and English report templates
- [Domain Templates](references/domain_templates.md) - Domain-specific question templates
- [Search Strategies](references/search_strategies.md) - Optimized search queries for different dimensions
- [Validation Methods](references/validation_methods.md) - Cross-validation and credibility assessment methods
- [Timeline Generation](references/timeline_generation.md) - Timeline visualization guide
