# Search Strategies for Person Analyzer

This document contains detailed search strategies for each dimension of biographical analysis.

## General Principles

1. **Use Google AI Mode as primary source** - Most comprehensive and up-to-date
2. **Cross-validate with multiple sources** - Ensure accuracy
3. **Include person's name in every query** - Improve relevance
4. **Use specific keywords** - Better than generic terms
5. **Search in multiple languages** - If person is multilingual

## Dimension 1: Family Background (原生家庭)

**Key Information to Collect**:
- Birth date and place
- Parents' background, education, occupation, achievements
- Family's social class and capital
- Influence of relatives within 3 generations
- Special childhood experiences
- How family shaped their worldview and values

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} parents family background childhood upbringing")
Skill(skill="google-ai-mode", args="{person_name} birth date birthplace early life")
Skill(skill="google-ai-mode", args="{person_name} family influence childhood experiences")
```

**Alternative Keywords**:
- "family history", "ancestry", "heritage"
- "childhood", "early years", "formative years"
- "parents occupation", "family business"
- "social class", "family wealth"

## Dimension 2: Education Journey (求学经历)

**Key Information to Collect**:
- Schools attended (elementary, middle, high school, university) with dates
- Academic performance and achievements
- Leadership roles in student organizations
- Business attempts during school
- Influential books read
- Degrees obtained

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} education university degree student activities")
Skill(skill="google-ai-mode", args="{person_name} academic performance school achievements")
Skill(skill="google-ai-mode", args="{person_name} student leadership extracurricular")
```

**Alternative Keywords**:
- "alma mater", "graduated from"
- "student life", "college years"
- "academic honors", "scholarships"
- "thesis", "dissertation"

## Dimension 3: Work Experience (工作经历)

**Key Information to Collect**:
- When joined which industry and company
- Reasons for joining
- Company's scale, stage, and industry position
- Founder's entrepreneurial spirit
- Position and responsibilities
- Notable achievements and promotions
- Skills, knowledge, and network gained
- Lessons learned and reflections

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} career work experience companies positions achievements")
Skill(skill="google-ai-mode", args="{person_name} early career first job")
Skill(skill="google-ai-mode", args="{person_name} professional experience promotions")
```

**Alternative Keywords**:
- "employment history", "career path"
- "worked at", "joined company"
- "career progression", "job titles"
- "professional achievements"

## Dimension 4: Entrepreneurial Journey (创业经历)

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

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} startup founding company journey funding team")
Skill(skill="google-ai-mode", args="{person_name} entrepreneurship business ventures")
Skill(skill="google-ai-mode", args="{person_name} funding rounds investors valuation")
Skill(skill="google-ai-mode", args="{person_name} IPO acquisition exit")
```

**For Other Domains** (adapt accordingly):
- Major career breakthroughs
- Key projects or works
- Collaborations and partnerships
- Recognition and awards
- Career turning points

**Alternative Keywords**:
- "founded", "co-founder", "startup"
- "venture capital", "seed funding", "Series A/B/C"
- "business model", "product launch"
- "pivot", "acquisition", "merger"

## Dimension 5: Learning Ability (学习能力)

**Key Information to Collect**:
- How they continuously learn
- Learning methods and sources
- Mentors and teachers
- Core friend circle (3-5 examples)
- Cognitive leaps and growth
- Moments of enlightenment
- How they received help from mentors
- How they upgraded their wisdom

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} mentors influences learning books inspiration")
Skill(skill="google-ai-mode", args="{person_name} reading list favorite books")
Skill(skill="google-ai-mode", args="{person_name} advisors teachers coaches")
```

**Alternative Keywords**:
- "influenced by", "inspired by"
- "role models", "mentorship"
- "learning philosophy", "self-improvement"
- "books that changed", "recommended reading"

## Dimension 6: Life Trajectory Mapping (人生轨迹图)

**Two Dimensions**:
1. **Geographic Trajectory** - Physical location changes over time
2. **Social Class Trajectory** - Status/achievement changes over time

**For Each Critical Node - 节思行果 Framework**:
- **节 (Node/Juncture)**: What problem/challenge did they face at this critical juncture?
- **思 (Thinking)**: How did they analyze and think about it? What were their considerations?
- **行 (Action)**: What specific action did they take? What was their strategy?
- **果 (Result)**: What result did it bring? What were the consequences?
- **影响 (Impact)**: How did it influence their life direction and future decisions?

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} timeline major decisions turning points critical moments decision-making process")
Skill(skill="google-ai-mode", args="{person_name} life story biography chronology")
Skill(skill="google-ai-mode", args="{person_name} moved to relocated career change")
```

**Alternative Keywords**:
- "pivotal moment", "turning point", "crossroads"
- "major decision", "life-changing"
- "relocated", "moved to", "based in"
- "career transition", "life transition"

## Dimension 7: Success Logic and Insights (成功逻辑)

**Analysis Focus**:
- Underlying logic of their success
- Patterns and principles
- Insights for others in the same domain
- Transferable lessons

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} success factors key to success")
Skill(skill="google-ai-mode", args="{person_name} philosophy principles values")
Skill(skill="google-ai-mode", args="{person_name} advice lessons learned")
```

**Alternative Keywords**:
- "success story", "how they succeeded"
- "business philosophy", "management style"
- "lessons learned", "advice for"
- "what made them successful"

## Dimension 8: Failures and Setbacks (失败与挫折)

**Key Information to Collect**:
- Major failures and setbacks throughout their life
- Critical mistakes and misjudgments
- How they responded to failures
- Lessons learned from failures
- How failures shaped their future decisions
- Recovery strategies and resilience patterns
- What they would do differently in hindsight

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} failures setbacks mistakes controversies bankruptcy crisis recovery")
Skill(skill="google-ai-mode", args="{person_name} failed ventures unsuccessful projects")
Skill(skill="google-ai-mode", args="{person_name} challenges obstacles difficulties")
```

**Alternative Keywords**:
- "failed", "failure", "unsuccessful"
- "bankruptcy", "financial crisis"
- "controversy", "scandal", "criticism"
- "setback", "obstacle", "challenge"
- "recovery", "comeback", "resilience"

## Dimension 9: Relationship Network (人际关系网络)

**Key Information to Collect**:
- Who did they meet at each life stage?
- What relationships were formed and why?
- How did these people influence their decisions?
- What collaborations or conflicts emerged?
- How did their network evolve over time?
- Key mentors, partners, rivals, and supporters
- Network effects on their success

**Search Strategy**:
```
Skill(skill="google-ai-mode", args="{person_name} relationships network mentors partners collaborators team members investors advisors")
Skill(skill="google-ai-mode", args="{person_name} co-founders team early employees")
Skill(skill="google-ai-mode", args="{person_name} friends colleagues associates")
```

**Alternative Keywords**:
- "worked with", "collaborated with"
- "mentored by", "advised by"
- "co-founder", "business partner"
- "investor", "backer", "supporter"
- "rival", "competitor", "conflict with"

## Advanced Search Techniques

### 1. Time-Based Searches
Add year ranges to get specific period information:
```
"{person_name} 1990-2000"
"{person_name} early career 1980s"
```

### 2. Source-Specific Searches
Target specific types of sources:
```
"{person_name} interview"
"{person_name} biography book"
"{person_name} documentary"
"{person_name} speech transcript"
```

### 3. Relationship Searches
Find connections through other people:
```
"{person_name} AND {known_associate}"
"{person_name} worked with"
"{person_name} mentored by"
```

### 4. Event-Based Searches
Search around known events:
```
"{person_name} {company_name} founding"
"{person_name} {award_name}"
"{person_name} {conference_name}"
```

### 5. Negative Keywords
Exclude irrelevant results:
```
"{person_name} -actor" (if there's a famous actor with same name)
"{person_name} -sports" (if not interested in sports career)
```

## Quality Checks

After collecting information, verify:
1. **Date consistency** - Do dates align across sources?
2. **Fact cross-validation** - Do multiple sources confirm the same facts?
3. **Source credibility** - Are sources reliable and authoritative?
4. **Completeness** - Are there gaps in the timeline?
5. **Contradictions** - Are there conflicting accounts?

## Common Pitfalls to Avoid

1. **Name confusion** - Verify you're researching the right person
2. **Outdated information** - Check publication dates
3. **Biased sources** - Balance positive and critical sources
4. **Missing context** - Understand the historical/cultural context
5. **Over-reliance on one source** - Always cross-validate

## Tips for Better Results

1. **Start broad, then narrow** - Begin with general searches, then get specific
2. **Use quotes for exact phrases** - "exact phrase" vs exact phrase
3. **Try different name formats** - Full name, nickname, maiden name
4. **Search in native language** - If person is from non-English country
5. **Look for primary sources** - Interviews, autobiographies, speeches
6. **Check recent news** - For current information
7. **Explore social media** - LinkedIn, Twitter, personal blogs
8. **Academic databases** - For scientists and researchers
9. **Industry publications** - For domain-specific information
10. **Archive sites** - For historical information
