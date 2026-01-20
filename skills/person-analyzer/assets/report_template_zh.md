# {{person_name}} 深度人物分析报告

**分析日期**: {{analysis_date}}
**分析领域**: {{domain}}
**分析深度**: {{depth}}
**可信度评分**: {{credibility_score}}/100

---

## 执行摘要

{{executive_summary}}

### 核心亮点
{{#each highlights}}
- {{this}}
{{/each}}

---

## 一、原生家庭：底层操作系统

### 基本信息
- **出生日期**: {{birth_date}}
- **籍贯**: {{birth_place}}

### 父母背景

{{parents_background}}

### 家庭影响

{{family_influence}}

### 特殊经历

{{special_childhood_experiences}}

### 底层操作系统塑造

{{operating_system_formation}}

**三观（世界观、人生观、价值观）**:
{{worldview}}

**三格（人格、品格、性格）**:
{{character}}

**思维模型**:
{{thinking_model}}

**行为习惯**:
{{behavior_patterns}}

### 社会资本

{{social_capital}}

**数据来源**:
{{#each dimension1_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 二、求学经历

### 教育时间线

| 时间段 | 学校 | 学位/阶段 | 重要事件 |
|--------|------|----------|---------|
{{#each education_timeline}}
| {{period}} | {{school}} | {{degree}} | {{events}} |
{{/each}}

### 学业表现

{{academic_performance}}

### 学生领导力

{{student_leadership}}

### 商业尝试

{{business_attempts}}

### 影响深远的阅读

{{influential_books}}

### 折腾经历

{{school_adventures}}

### 对底层操作系统的影响

{{education_impact}}

**数据来源**:
{{#each dimension2_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 三、工作经历

### 职业时间线

{{#each work_experiences}}
#### {{company_name}} ({{start_date}} - {{end_date}})

- **加入时间**: {{join_date}}
- **所属行业**: {{industry}}
- **加入理由**: {{reason}}
- **公司情况**:
  - 规模: {{company_scale}}
  - 发展阶段: {{company_stage}}
  - 行业地位: {{industry_position}}
  - 创始人特点: {{founder_characteristics}}
- **加入方式**: {{how_joined}}
- **担任职务**: {{position}}
- **主要成就**: {{achievements}}
- **职务升迁**: {{promotions}}
- **收获影响**:
  - 职业技能: {{skills_gained}}
  - 认知提升: {{cognition_growth}}
  - 人脉网络: {{network_expansion}}
- **经验教训**: {{lessons_learned}}
- **个人反思**: {{personal_reflections}}

{{/each}}

**数据来源**:
{{#each dimension3_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 四、{{career_milestone_title}}

### {{#if is_entrepreneur}}创业动机{{else}}职业突破契机{{/if}}

{{motivation}}

### {{#if is_entrepreneur}}商业机会发现{{else}}关键机会识别{{/if}}

{{opportunity_discovery}}

### {{#if is_entrepreneur}}创业方向确定{{else}}职业方向选择{{/if}}

{{direction_determination}}

### {{#if is_entrepreneur}}资源整合{{else}}资源获取{{/if}}

{{resource_integration}}

### {{#if is_entrepreneur}}团队组建{{else}}核心合作者{{/if}}

{{team_building}}

### {{#if is_entrepreneur}}创业历程{{else}}职业里程碑{{/if}}

{{#each ventures}}
#### 第{{index}}{{#if ../is_entrepreneur}}次创业{{else}}个重要阶段{{/if}}: {{name}}

- **时间**: {{date}}
- **方向**: {{direction}}
{{#if ../is_entrepreneur}}
- **第一桶金**: {{first_revenue}}
- **融资记录**:
  | 时间 | 轮次 | 金额 | 投资方 | 估值 |
  |------|------|------|--------|------|
  {{#each funding_rounds}}
  | {{date}} | {{round}} | {{amount}} | {{investors}} | {{valuation}} |
  {{/each}}
- **股权分配**: {{equity_structure}}
- **激励机制**: {{incentive_design}}
{{/if}}
- **高光时刻**: {{highlights}}
- **至暗时刻**: {{dark_moments}}
- **失败教训**: {{failures_and_lessons}}
{{#if ../is_entrepreneur}}
- **退出情况**: {{exit_status}}
{{/if}}

{{/each}}

### {{#if is_entrepreneur}}创业锚点{{else}}职业锚点{{/if}}

{{career_anchor}}

### {{#if is_entrepreneur}}企业家精神体现{{else}}专业精神体现{{/if}}

{{professional_spirit}}

**数据来源**:
{{#each dimension4_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 五、学习能力

### 持续学习方式

{{learning_methods}}

### 学习对象和方法

{{learning_sources}}

### 拜师经历

{{mentorship}}

### 核心朋友圈

{{#each core_friends}}
#### {{name}}
- **关系**: {{relationship}}
- **背景**: {{background}}
- **影响**: {{influence}}

{{/each}}

### 认知跃迁

{{cognitive_leaps}}

### 成长历程

{{growth_journey}}

### 高人开悟

{{enlightenment_moments}}

### 觉醒时刻

{{awakening_moments}}

### 贵人相助

{{mentor_help}}

### {{#if is_entrepreneur}}商业智慧升级{{else}}专业智慧升级{{/if}}

{{wisdom_upgrade}}

**数据来源**:
{{#each dimension5_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 六、人生轨迹图

### 时间维度：社会阶层变化

{{#if timeline_enabled}}
{{social_class_chart}}
{{/if}}

```mermaid
graph LR
{{#each social_class_trajectory}}
    {{node_id}}[{{class_level}}] -->|{{event}}|
{{/each}}
```

### 空间维度：地理位置迁移

{{#if timeline_enabled}}
{{geographic_map}}
{{/if}}

```mermaid
graph LR
{{#each geographic_trajectory}}
    {{node_id}}[{{location}}] -->|{{year}}|
{{/each}}
```

### 关键节点分析

{{#each critical_nodes}}
#### 关键节点 {{index}}: {{event_name}} ({{year}})

**节思行果分析**:

- **节 (关键节点)**: {{problem}}
- **思 (思考过程)**: {{thinking}}
- **行 (采取行动)**: {{action}}
- **果 (产生结果)**: {{result}}
- **影响 (人生影响)**: {{impact}}
- **可信度**: {{credibility}}/100
- **数据来源**:
  {{#each sources}}
  - [{{name}}]({{url}})
  {{/each}}

{{/each}}

**数据来源**:
{{#each dimension6_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 七、成功逻辑与启示

### 成功的底层逻辑

{{#each success_logic}}
{{index}}. **{{title}}**: {{description}}
{{/each}}

### 可复制的模式

{{replicable_patterns}}

### 不可复制的因素

{{non_replicable_factors}}

### 对同领域人士的启示

{{#each insights}}
{{index}}. **{{title}}**: {{description}}
{{/each}}

**数据来源**:
{{#each dimension7_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 八、失败与挫折：反面的成长

### 重大失败经历

{{#each major_failures}}
#### 失败 {{index}}: {{failure_name}} ({{year}})

- **失败类型**: {{failure_type}}
- **背景情况**: {{context}}
- **失败原因**: {{root_cause}}
- **损失程度**: {{impact_level}}
- **情绪反应**: {{emotional_response}}
- **应对策略**: {{coping_strategy}}
- **恢复过程**: {{recovery_process}}
- **吸取教训**: {{lessons_learned}}
- **后续影响**: {{long_term_impact}}

{{/each}}

### 关键误判与失误

{{#each misjudgments}}
#### 误判 {{index}}: {{misjudgment_name}}

- **决策时间**: {{decision_time}}
- **决策内容**: {{decision_content}}
- **误判原因**: {{misjudgment_reason}}
- **实际后果**: {{actual_consequence}}
- **认知盲区**: {{blind_spot}}
- **如何发现错误**: {{how_discovered}}
- **纠正措施**: {{correction_measures}}
- **事后反思**: {{hindsight_reflection}}

{{/each}}

### 挫折应对模式

{{resilience_patterns}}

### 失败对成功的贡献

{{failure_to_success_contribution}}

**数据来源**:
{{#each dimension8_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 九、人际关系网络：成功的社会资本

### 关系网络全景图

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

### 分阶段人际关系分析

{{#each life_stages}}
#### {{stage_name}} ({{time_period}})

##### 核心关系人物

{{#each key_people}}
**{{name}}** - {{relationship_type}}

- **背景**: {{background}}
- **相识契机**: {{meeting_context}}
- **相识时间**: {{meeting_time}}
- **互动频率**: {{interaction_frequency}}
- **关系性质**: {{relationship_nature}}
- **影响方向**: {{influence_direction}}
- **关键互动**:
  {{#each key_interactions}}
  - {{date}}: {{description}}
  {{/each}}
- **提供资源**: {{resources_provided}}
- **对其影响**: {{influence_on_person}}
- **关系演变**: {{relationship_evolution}}
- **当前状态**: {{current_status}}

{{/each}}

##### 网络特征
- **网络规模**: {{network_size}}
- **网络密度**: {{network_density}}
- **核心圈层**: {{core_circle_description}}
- **网络价值**: {{network_value}}

{{/each}}

### 关键关系类型分析

#### 导师型关系 (Mentors)

{{#each mentors}}
- **{{name}}**: {{influence_summary}}
{{/each}}

#### 合作伙伴关系 (Partners)

{{#each partners}}
- **{{name}}**: {{collaboration_summary}}
{{/each}}

#### 竞争对手关系 (Competitors)

{{#each competitors}}
- **{{name}}**: {{competition_summary}}
{{/each}}

#### 支持者关系 (Supporters)

{{#each supporters}}
- **{{name}}**: {{support_summary}}
{{/each}}

### 人际网络演化规律

{{network_evolution_patterns}}

### 网络效应分析

{{network_effects_analysis}}

**数据来源**:
{{#each dimension9_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}/100
{{/each}}

---

## 十、数据可信度评估

### 整体可信度评分: {{overall_credibility}}/100

### 各维度可信度

| 维度 | 可信度评分 | 主要来源数量 | 交叉验证状态 |
|------|-----------|-------------|-------------|
| 原生家庭 | {{dim1_credibility}} | {{dim1_sources_count}} | {{dim1_validation_status}} |
| 求学经历 | {{dim2_credibility}} | {{dim2_sources_count}} | {{dim2_validation_status}} |
| 工作经历 | {{dim3_credibility}} | {{dim3_sources_count}} | {{dim3_validation_status}} |
| 创业经历 | {{dim4_credibility}} | {{dim4_sources_count}} | {{dim4_validation_status}} |
| 学习能力 | {{dim5_credibility}} | {{dim5_sources_count}} | {{dim5_validation_status}} |
| 人生轨迹 | {{dim6_credibility}} | {{dim6_sources_count}} | {{dim6_validation_status}} |
| 成功逻辑 | {{dim7_credibility}} | {{dim7_sources_count}} | {{dim7_validation_status}} |
| 失败挫折 | {{dim8_credibility}} | {{dim8_sources_count}} | {{dim8_validation_status}} |
| 人际网络 | {{dim9_credibility}} | {{dim9_sources_count}} | {{dim9_validation_status}} |

### 信息冲突记录

{{#each conflicts}}
#### 冲突 {{index}}: {{topic}}

- **来源A**: [{{sourceA_name}}]({{sourceA_url}}) - 可信度: {{sourceA_credibility}}
  - 说法: {{sourceA_claim}}
- **来源B**: [{{sourceB_name}}]({{sourceB_url}}) - 可信度: {{sourceB_credibility}}
  - 说法: {{sourceB_claim}}
- **处理方式**: {{resolution}}

{{/each}}

### 未验证信息

{{#each unverified_info}}
- **信息**: {{claim}}
- **来源**: [{{source_name}}]({{source_url}})
- **原因**: {{reason}}

{{/each}}

---

## 九、数据来源

### 主要来源

- Google AI Mode: {{google_ai_queries}} 次查询
- Tavily搜索: {{tavily_queries}} 次查询
- Firecrawl: {{firecrawl_pages}} 页处理

### 具体来源列表

#### 高可信度来源 (80-100分)
{{#each high_credibility_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}
{{/each}}

#### 中等可信度来源 (60-79分)
{{#each medium_credibility_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}
{{/each}}

#### 低可信度来源 (40-59分)
{{#each low_credibility_sources}}
- [{{name}}]({{url}}) - 可信度: {{credibility}}
{{/each}}

---

## 十、方法论说明

**数据收集**: {{data_collection_method}}

**交叉验证**: {{validation_method}}

**可信度评估**: {{credibility_assessment_method}}

**局限性**: {{limitations}}

---

*报告由 Person Analyzer 生成*
*生成时间: {{generation_timestamp}}*
*分析耗时: {{analysis_duration}}*
