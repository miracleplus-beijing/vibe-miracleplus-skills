---
name: alpha-sight
description: Scientific Research Engineering Assistant for fetching, analyzing arXiv papers, and transforming them into actionable project improvements or code implementations. Use when the user provides an arXiv ID (e.g., 2401.12345, arxiv:2401.12345), mentions keywords (arxiv, paper, 论文, latest research, frontiers, 前沿), references technical domains (MoE, Transformer, Diffusion, RL, LLM, etc.), or requests to reproduce (复现), implement, or analyze papers (分析论文).
---

# Alpha-Sight: Scientific Research Engineering Assistant

A powerful skill for fetching, analyzing arXiv papers, and transforming them into actionable project improvements or code implementations.

## Quick Start

When triggered, Alpha-Sight automatically:
1. Fetches paper metadata and PDF from arXiv
2. Analyzes the paper based on specified depth
3. Generates a comprehensive report
4. Optionally reproduces code (if requested or depth=deep)

## Parameters

Parse these optional parameters from user input:

- `--depth=[shallow|medium|deep]` (default: `medium`)
  - `shallow`: Abstract and key information only (5 min timeout)
  - `medium`: Full analysis + project fit assessment (15 min timeout)
  - `deep`: Full analysis + code reproduction (30 min timeout)

- `--language=[english|chinese]` (default: `english`)
  - `english`: Report in English
  - `chinese`: Report in Chinese with key translations

- `--cleanup=[on-success|always|never]` (default: `on-success`)
  - `on-success`: Clean temp files after success
  - `always`: Always clean
  - `never`: Keep all files for debugging

## Environment Setup

### Required Environment Variables

Check for these environment variables in order of priority:
1. `./alpha-sight/.env` (project-level)
2. `~/.config/alpha-sight/.env` (global-level)
3. System environment variables

```bash
SEMANTIC_SCHOLAR_API_KEY=xxx  # Optional, for citation analysis
```

### Directory Structure

Ensure the following structure exists (create if missing):

```
./alpha-sight/
├── .env                    # Environment configuration
├── index.json              # Historical records index
├── papers/                 # PDF storage
│   └── {arxiv_id}.pdf
├── reports/                # Analysis reports
│   └── {arxiv_id}_analysis.md
└── sandbox/                # Sandbox for reproduction
    └── {arxiv_id}_reproduction/
        ├── official_repo/  # Official repository (if available)
        ├── custom_impl/    # Custom implementation
        └── .venv/          # Virtual environment
```

## Core Workflow Overview

### Phase 1: Paper Acquisition (Automatic)

1. **Parse User Input** - Extract arXiv ID, keywords, or domain
2. **Fetch Paper Metadata** - Use `scripts/arxiv_fetcher.py` or call arXiv API directly
3. **Download PDF** - Save to `./alpha-sight/papers/{arxiv_id}.pdf`
4. **Check History** - Read `./alpha-sight/index.json` to avoid duplicate analysis

**Tools**: WebFetch (arXiv API), Bash (download PDF), Read (check index)

### Phase 2: Initial Analysis (Automatic)

1. **Extract Key Information** - Title, authors, abstract, categories, key contributions
2. **Fetch Citation Data** - Use `scripts/semantic_scholar_fetcher.py` if API key available
3. **Generate Initial Report** - Create basic Markdown report

**Tools**: Read (PDF), WebFetch (Semantic Scholar), Write (report)

### Phase 3: Deep Analysis (User Confirmation Required)

**Skip if `depth=shallow`**

1. **Read Paper Content** - Focus on Method, Algorithm, Implementation sections
2. **Analyze Current Project** - Identify tech stack and relevant patterns
3. **Generate Project Fit Assessment** - Relevance score, application scenarios, suggestions
4. **Create Architecture Comparison** - Mermaid diagram comparing paper vs. current project
5. **Ask User for Reproduction** - If `depth=medium`, ask; if `depth=deep`, proceed automatically

**Tools**: Read (PDF, project files), Glob (find files), Grep (search patterns), AskUserQuestion (if depth=medium)

**For detailed workflow**: See [references/workflow_details.md](references/workflow_details.md)

### Phase 4: Code Reproduction (Conditional)

**Only execute if user confirmed OR `depth=deep`**

#### Step 1: Find Official Repository

Search in this order:
1. Check arXiv page for "Code" link
2. Parse PDF for GitHub/GitLab URLs
3. Query Semantic Scholar API for linked repositories
4. Search Papers with Code database

#### Step 2a: If Official Repository Found

```bash
cd ./alpha-sight/sandbox/{arxiv_id}_reproduction/
git clone {repo_url} official_repo
cd official_repo

# Create virtual environment with uv
uv venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
uv pip install -r requirements.txt

# Try to run (with timeout)
```

#### Step 2b: If No Official Repository - Self-Implementation Loop

**Maximum 5 iterations:**

```python
for iteration in range(1, 6):
    # 1. Read paper method section
    method_content = read_paper_section(["Method", "Algorithm", "Implementation"])

    # 2. Identify required libraries
    required_libs = extract_dependencies(method_content)

    # 3. Query Context7 (if available and needed)
    if context7_available and needs_documentation(required_libs):
        docs = query_context7(required_libs)

    # 4. Generate implementation code
    code = generate_implementation(
        paper_content=method_content,
        documentation=docs,
        previous_errors=errors_from_last_iteration
    )

    # 5. Save and run code in sandbox with timeout
    result = run_with_timeout(
        code=code,
        timeout=TIMEOUT_LIMITS[depth],
        memory_limit="4GB"
    )

    # 6. Check result and iterate or break
    if result.success:
        break
    elif iteration == 5:
        mark_as_partial_completion()
```

**Resource Limits**: Memory: 4GB, Disk: 2GB per sandbox, Timeout: Based on `depth` parameter

**Tools**: Bash (git clone, run sandbox), Read (paper, code), Write (implementation), mcp__context7 (if available)

**For detailed reproduction workflow**: See [references/workflow_details.md](references/workflow_details.md#phase-4-code-reproduction)

### Phase 5: Report Generation & Archiving

1. **Generate Final Report** - Use templates from `assets/report_template_{zh|en}.md`
2. **Update index.json** - Use `scripts/index_manager.py` or update manually
3. **Cleanup** - Based on `--cleanup` parameter

**Report Templates**: See [references/report_templates.md](references/report_templates.md) for complete templates

**Tools**: Write (report, index), Bash (cleanup)

## Error Handling

For common errors and handling strategies, see [references/error_handling.md](references/error_handling.md)

Quick reference:
- **Timeout Errors**: Log to report, mark as "partial", preserve files
- **Memory Errors**: Suggest lighter implementation, mark as "failed"
- **API Errors**: Retry with exponential backoff (arXiv: 3 times, Semantic Scholar: continue without)
- **Git Clone Errors**: Proceed to self-implementation

## Output Format

### Success Message

```
✓ Paper Analysis Complete

Paper: {title}
arXiv ID: {arxiv_id}
Relevance Score: {score}/10

Report: ./alpha-sight/reports/{arxiv_id}_analysis.md
PDF: ./alpha-sight/papers/{arxiv_id}.pdf

{If reproduced:}
Reproduction: {status}
Method: {official_repo | self_implemented}
Code: ./alpha-sight/sandbox/{arxiv_id}_reproduction/
```

### Language-Specific Output

If `--language=chinese`, translate all output messages to Chinese while keeping technical terms in English with Chinese annotations.

## Tools to Use

- **WebFetch**: Fetch arXiv API and Semantic Scholar API
- **Bash**: Download PDFs, git clone, run sandbox commands
- **Read**: Read PDF content, configuration files
- **Write**: Create reports, save code
- **Glob**: Find project files
- **Grep**: Search codebase patterns
- **mcp__context7__resolve-library-id**: Resolve library names (if available)
- **mcp__context7__query-docs**: Query library documentation (if available)
- **AskUserQuestion**: Confirm reproduction (when depth=medium)

## Scripts Available

- `scripts/arxiv_fetcher.py` - Fetch arXiv metadata and download PDFs
- `scripts/index_manager.py` - Manage index.json for tracking analyzed papers
- `scripts/semantic_scholar_fetcher.py` - Fetch citation data from Semantic Scholar
- `scripts/report_generator.py` - Generate report framework from templates

Usage examples:
```bash
# Fetch paper metadata and PDF
python scripts/arxiv_fetcher.py 2401.12345

# Add paper to index
python scripts/index_manager.py add 2401.12345 --metadata metadata.json

# Generate report framework
python scripts/report_generator.py 2401.12345 --language chinese --depth medium
```

## Important Notes

1. **Only process papers from arxiv.org** (English papers only)
2. **Always use `uv` for Python dependency management** in sandbox
3. **Never exceed resource limits** (4GB memory, 2GB disk, timeout per depth)
4. **Always update index.json** after each analysis
5. **Preserve sandbox on failure** for debugging
6. **Use Context7 only when available** - gracefully degrade if not
7. **Maximum 5 iterations** for self-implementation loop
8. **No user confirmation during iterations** - run automatically

## Example Usage

```
User: "Analyze arXiv 2401.12345"
→ Triggers skill with default parameters (depth=medium, language=english)

User: "Find latest MoE papers and analyze with deep reproduction --language=chinese"
→ Searches arXiv for MoE papers, analyzes with depth=deep, outputs in Chinese

User: "Reproduce this paper 2312.xxxxx"
→ Triggers skill with depth=deep (implied by "reproduce")
```

## References

- [Workflow Details](references/workflow_details.md) - Detailed Phase 2-5 workflows
- [Report Templates](references/report_templates.md) - Complete Chinese and English report templates
- [Error Handling](references/error_handling.md) - Comprehensive error handling strategies
- [arXiv API Documentation](references/arxiv_api.md) - arXiv API reference
- [Semantic Scholar API Documentation](references/semantic_scholar_api.md) - Semantic Scholar API reference
