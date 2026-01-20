# {{person_name}} - Deep Biographical Analysis Report

**Analysis Date**: {{analysis_date}}
**Domain**: {{domain}}
**Analysis Depth**: {{depth}}
**Credibility Score**: {{credibility_score}}/100

---

## Executive Summary

{{executive_summary}}

### Key Highlights
{{#each highlights}}
- {{this}}
{{/each}}

---

## I. Family Background: Operating System Foundation

### Basic Information
- **Birth Date**: {{birth_date}}
- **Birth Place**: {{birth_place}}

### Parents' Background

{{parents_background}}

### Family Influence

{{family_influence}}

### Special Childhood Experiences

{{special_childhood_experiences}}

### Operating System Formation

{{operating_system_formation}}

**Worldview, Life Philosophy, Values**:
{{worldview}}

**Personality, Character, Temperament**:
{{character}}

**Thinking Models**:
{{thinking_model}}

**Behavioral Patterns**:
{{behavior_patterns}}

### Social Capital

{{social_capital}}

**Data Sources**:
{{#each dimension1_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## II. Education Journey

### Education Timeline

| Period | Institution | Degree/Stage | Key Events |
|--------|-------------|--------------|------------|
{{#each education_timeline}}
| {{period}} | {{school}} | {{degree}} | {{events}} |
{{/each}}

### Academic Performance

{{academic_performance}}

### Student Leadership

{{student_leadership}}

### Business Attempts

{{business_attempts}}

### Influential Reading

{{influential_books}}

### Notable Experiences

{{school_adventures}}

### Impact on Operating System

{{education_impact}}

**Data Sources**:
{{#each dimension2_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## III. Work Experience

### Career Timeline

{{#each work_experiences}}
#### {{company_name}} ({{start_date}} - {{end_date}})

- **Join Date**: {{join_date}}
- **Industry**: {{industry}}
- **Reason for Joining**: {{reason}}
- **Company Profile**:
  - Scale: {{company_scale}}
  - Stage: {{company_stage}}
  - Industry Position: {{industry_position}}
  - Founder Characteristics: {{founder_characteristics}}
- **How Joined**: {{how_joined}}
- **Position**: {{position}}
- **Key Achievements**: {{achievements}}
- **Promotions**: {{promotions}}
- **Gains**:
  - Skills: {{skills_gained}}
  - Cognition: {{cognition_growth}}
  - Network: {{network_expansion}}
- **Lessons Learned**: {{lessons_learned}}
- **Personal Reflections**: {{personal_reflections}}

{{/each}}

**Data Sources**:
{{#each dimension3_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## IV. {{career_milestone_title}}

### {{#if is_entrepreneur}}Entrepreneurial Motivation{{else}}Career Breakthrough Catalyst{{/if}}

{{motivation}}

### {{#if is_entrepreneur}}Business Opportunity Discovery{{else}}Key Opportunity Identification{{/if}}

{{opportunity_discovery}}

### {{#if is_entrepreneur}}Direction Determination{{else}}Career Direction Choice{{/if}}

{{direction_determination}}

### {{#if is_entrepreneur}}Resource Integration{{else}}Resource Acquisition{{/if}}

{{resource_integration}}

### {{#if is_entrepreneur}}Team Building{{else}}Core Collaborators{{/if}}

{{team_building}}

### {{#if is_entrepreneur}}Entrepreneurial Journey{{else}}Career Milestones{{/if}}

{{#each ventures}}
#### {{#if ../is_entrepreneur}}Venture{{else}}Phase{{/if}} {{index}}: {{name}}

- **Time**: {{date}}
- **Direction**: {{direction}}
{{#if ../is_entrepreneur}}
- **First Revenue**: {{first_revenue}}
- **Funding History**:
  | Date | Round | Amount | Investors | Valuation |
  |------|-------|--------|-----------|-----------|
  {{#each funding_rounds}}
  | {{date}} | {{round}} | {{amount}} | {{investors}} | {{valuation}} |
  {{/each}}
- **Equity Structure**: {{equity_structure}}
- **Incentive Design**: {{incentive_design}}
{{/if}}
- **Highlights**: {{highlights}}
- **Dark Moments**: {{dark_moments}}
- **Failures and Lessons**: {{failures_and_lessons}}
{{#if ../is_entrepreneur}}
- **Exit Status**: {{exit_status}}
{{/if}}

{{/each}}

### {{#if is_entrepreneur}}Career Anchor{{else}}Professional Anchor{{/if}}

{{career_anchor}}

### {{#if is_entrepreneur}}Entrepreneurial Spirit{{else}}Professional Spirit{{/if}}

{{professional_spirit}}

**Data Sources**:
{{#each dimension4_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## V. Learning Ability

### Continuous Learning Methods

{{learning_methods}}

### Learning Sources and Methods

{{learning_sources}}

### Mentorship

{{mentorship}}

### Core Friend Circle

{{#each core_friends}}
#### {{name}}
- **Relationship**: {{relationship}}
- **Background**: {{background}}
- **Influence**: {{influence}}

{{/each}}

### Cognitive Leaps

{{cognitive_leaps}}

### Growth Journey

{{growth_journey}}

### Enlightenment Moments

{{enlightenment_moments}}

### Awakening Moments

{{awakening_moments}}

### Mentor Support

{{mentor_help}}

### {{#if is_entrepreneur}}Business Wisdom Upgrade{{else}}Professional Wisdom Upgrade{{/if}}

{{wisdom_upgrade}}

**Data Sources**:
{{#each dimension5_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## VI. Life Trajectory Mapping

### Time Dimension: Social Class Evolution

{{#if timeline_enabled}}
{{social_class_chart}}
{{/if}}

```mermaid
graph LR
{{#each social_class_trajectory}}
    {{node_id}}[{{class_level}}] -->|{{event}}|
{{/each}}
```

### Space Dimension: Geographic Migration

{{#if timeline_enabled}}
{{geographic_map}}
{{/if}}

```mermaid
graph LR
{{#each geographic_trajectory}}
    {{node_id}}[{{location}}] -->|{{year}}|
{{/each}}
```

### Critical Node Analysis

{{#each critical_nodes}}
#### Critical Node {{index}}: {{event_name}} ({{year}})

**节思行果 (Node-Think-Act-Result) Analysis**:

- **节 (Node/Juncture)**: {{problem}}
- **思 (Thinking)**: {{thinking}}
- **行 (Action)**: {{action}}
- **果 (Result)**: {{result}}
- **影响 (Impact)**: {{impact}}
- **Credibility**: {{credibility}}/100
- **Data Sources**:
  {{#each sources}}
  - [{{name}}]({{url}})
  {{/each}}

{{/each}}

**Data Sources**:
{{#each dimension6_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## VII. Success Logic and Insights

### Underlying Logic of Success

{{#each success_logic}}
{{index}}. **{{title}}**: {{description}}
{{/each}}

### Replicable Patterns

{{replicable_patterns}}

### Non-Replicable Factors

{{non_replicable_factors}}

### Insights for Peers

{{#each insights}}
{{index}}. **{{title}}**: {{description}}
{{/each}}

**Data Sources**:
{{#each dimension7_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## VIII. Failures and Setbacks: Growth from Adversity

### Major Failures

{{#each major_failures}}
#### Failure {{index}}: {{failure_name}} ({{year}})

- **Failure Type**: {{failure_type}}
- **Context**: {{context}}
- **Root Cause**: {{root_cause}}
- **Impact Level**: {{impact_level}}
- **Emotional Response**: {{emotional_response}}
- **Coping Strategy**: {{coping_strategy}}
- **Recovery Process**: {{recovery_process}}
- **Lessons Learned**: {{lessons_learned}}
- **Long-term Impact**: {{long_term_impact}}

{{/each}}

### Critical Misjudgments and Mistakes

{{#each misjudgments}}
#### Misjudgment {{index}}: {{misjudgment_name}}

- **Decision Time**: {{decision_time}}
- **Decision Content**: {{decision_content}}
- **Misjudgment Reason**: {{misjudgment_reason}}
- **Actual Consequence**: {{actual_consequence}}
- **Blind Spot**: {{blind_spot}}
- **How Discovered**: {{how_discovered}}
- **Correction Measures**: {{correction_measures}}
- **Hindsight Reflection**: {{hindsight_reflection}}

{{/each}}

### Resilience Patterns

{{resilience_patterns}}

### How Failures Contributed to Success

{{failure_to_success_contribution}}

**Data Sources**:
{{#each dimension8_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## IX. Relationship Network: Social Capital for Success

### Network Overview

{{#if network_visualization_enabled}}
```mermaid
graph TD
    {{person_name}}[{{person_name}}]
    {{#each network_nodes}}
    {{node_id}}[{{person_name}}<br/>{{relationship_type}}]
    {{person_name}} -->|{{connection_strength}}| {{node_id}}
    {{/each}}
```
{{/if}}

### Stage-by-Stage Relationship Analysis

{{#each life_stages}}
#### {{stage_name}} ({{time_period}})

##### Key People

{{#each key_people}}
**{{name}}** - {{relationship_type}}

- **Background**: {{background}}
- **Meeting Context**: {{meeting_context}}
- **Meeting Time**: {{meeting_time}}
- **Interaction Frequency**: {{interaction_frequency}}
- **Relationship Nature**: {{relationship_nature}}
- **Influence Direction**: {{influence_direction}}
- **Key Interactions**:
  {{#each key_interactions}}
  - {{date}}: {{description}}
  {{/each}}
- **Resources Provided**: {{resources_provided}}
- **Influence on Person**: {{influence_on_person}}
- **Relationship Evolution**: {{relationship_evolution}}
- **Current Status**: {{current_status}}

{{/each}}

##### Network Characteristics
- **Network Size**: {{network_size}}
- **Network Density**: {{network_density}}
- **Core Circle**: {{core_circle_description}}
- **Network Value**: {{network_value}}

{{/each}}

### Key Relationship Types

#### Mentors

{{#each mentors}}
- **{{name}}**: {{influence_summary}}
{{/each}}

#### Partners

{{#each partners}}
- **{{name}}**: {{collaboration_summary}}
{{/each}}

#### Competitors

{{#each competitors}}
- **{{name}}**: {{competition_summary}}
{{/each}}

#### Supporters

{{#each supporters}}
- **{{name}}**: {{support_summary}}
{{/each}}

### Network Evolution Patterns

{{network_evolution_patterns}}

### Network Effects Analysis

{{network_effects_analysis}}

**Data Sources**:
{{#each dimension9_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}/100
{{/each}}

---

## X. Data Credibility Assessment

### Overall Credibility Score: {{overall_credibility}}/100

### Dimension-wise Credibility

| Dimension | Credibility | Source Count | Validation Status |
|-----------|-------------|--------------|-------------------|
| Family Background | {{dim1_credibility}} | {{dim1_sources_count}} | {{dim1_validation_status}} |
| Education | {{dim2_credibility}} | {{dim2_sources_count}} | {{dim2_validation_status}} |
| Work Experience | {{dim3_credibility}} | {{dim3_sources_count}} | {{dim3_validation_status}} |
| Career Milestones | {{dim4_credibility}} | {{dim4_sources_count}} | {{dim4_validation_status}} |
| Learning Ability | {{dim5_credibility}} | {{dim5_sources_count}} | {{dim5_validation_status}} |
| Life Trajectory | {{dim6_credibility}} | {{dim6_sources_count}} | {{dim6_validation_status}} |
| Success Logic | {{dim7_credibility}} | {{dim7_sources_count}} | {{dim7_validation_status}} |
| Failures & Setbacks | {{dim8_credibility}} | {{dim8_sources_count}} | {{dim8_validation_status}} |
| Relationship Network | {{dim9_credibility}} | {{dim9_sources_count}} | {{dim9_validation_status}} |

### Information Conflicts

{{#each conflicts}}
#### Conflict {{index}}: {{topic}}

- **Source A**: [{{sourceA_name}}]({{sourceA_url}}) - Credibility: {{sourceA_credibility}}
  - Claim: {{sourceA_claim}}
- **Source B**: [{{sourceB_name}}]({{sourceB_url}}) - Credibility: {{sourceB_credibility}}
  - Claim: {{sourceB_claim}}
- **Resolution**: {{resolution}}

{{/each}}

### Unverified Information

{{#each unverified_info}}
- **Information**: {{claim}}
- **Source**: [{{source_name}}]({{source_url}})
- **Reason**: {{reason}}

{{/each}}

---

## IX. Data Sources

### Primary Sources

- Google AI Mode: {{google_ai_queries}} queries
- Tavily Search: {{tavily_queries}} queries
- Firecrawl: {{firecrawl_pages}} pages

### Detailed Source List

#### High Credibility Sources (80-100)
{{#each high_credibility_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}
{{/each}}

#### Medium Credibility Sources (60-79)
{{#each medium_credibility_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}
{{/each}}

#### Low Credibility Sources (40-59)
{{#each low_credibility_sources}}
- [{{name}}]({{url}}) - Credibility: {{credibility}}
{{/each}}

---

## X. Methodology

**Data Collection**: {{data_collection_method}}

**Cross-Validation**: {{validation_method}}

**Credibility Assessment**: {{credibility_assessment_method}}

**Limitations**: {{limitations}}

---

*Report generated by Person Analyzer*
*Generation Time: {{generation_timestamp}}*
*Analysis Duration: {{analysis_duration}}*
