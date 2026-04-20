---
pubDatetime: 2026-01-27T00:01:00Z
title: "Designing Domain Agents for ICT Departments"
postSlug: "designing-domain-agents-for-ict-departments"
description: "How to design specialized AI agents for ICT departments: helpdesk, data analysis, project management, executive support, training, forms, and communications."
tags:
  - automation
  - openagents
  - ai
---

# Designing Domain Agents for ICT Departments

Modern ICT departments face increasing complexity: managing infrastructure, supporting users, analyzing data, coordinating projects, and communicating with stakeholders. Specialized AI agents can dramatically improve efficiency by handling domain-specific tasks while humans focus on strategic decisions.

This article explores how to design and implement domain-specific AI agents for ICT departments, complete with architecture patterns, integration strategies, and practical examples.

## What Are Domain Agents?

Domain agents are AI assistants specialized for specific organizational functions. Unlike general-purpose AI, domain agents have:

- **Deep domain knowledge** (e.g., Active Directory troubleshooting, SQL query patterns, project management workflows)
- **Integrated tooling** (direct access to databases, ticketing systems, dashboards)
- **Process expertise** (understand escalation paths, documentation standards, communication protocols)
- **Quality criteria** (know what "good" looks like for their domain)

## Why ICT Departments Need Domain Agents

### Current Challenges

1. **Support bottlenecks**: Tier 1 helpdesk overwhelmed with repetitive tickets
2. **Data silos**: Valuable insights locked in databases and spreadsheets
3. **Project chaos**: Manual tracking, missed deadlines, unclear dependencies
4. **Knowledge loss**: Tribal knowledge leaves with employees
5. **Communication friction**: Inconsistent messaging across channels

### Agent Benefits

- **24/7 availability**: Agents work around the clock
- **Consistency**: Same quality regardless of time or person
- **Scalability**: Handle volume increases without hiring
- **Knowledge retention**: All solutions stored in searchable systems
- **Cross-agent collaboration**: Agents can delegate to each other

## ICT Domain Agent Architecture

### Agent Definition Structure

Based on the OpenCode agent framework, domain agents follow this structure:

```markdown
---
name: Helpdesk-Agent
description: Technical support, troubleshooting, ticket routing for ICT department
version: 1.0.0
last_updated: 2026-01-27
model: zhipuai-coding-plan/glm-4.7-flash
temperature: 0.3
max_steps: 30
---

## IDENTITY
[Who this agent is, its purpose]

## CAPABILITIES
[What it can do, core functions]

## DOMAIN KNOWLEDGE
[ICT-specific knowledge areas]

## TASK EXECUTION PROTOCOL
[Step-by-step process]

## TOOL USAGE
[Which tools/skills to integrate]

## INTEGRATION WITH SKILLS
[How to connect to existing skills]

## QUALITY CRITERIA
[What defines successful output]
```

### Shared Infrastructure

All agents connect to:

- **OpenMemory**: Semantic storage for solutions, procedures, decisions
- **Memos**: Quick-access knowledge base for common tasks
- **Fabric**: Analysis patterns and workflows
- **Domain skills**: Databases, maintenance, dashboard tools

## Seven Essential ICT Domain Agents

### 1. Helpdesk Agent

**Purpose**: Tier 1-2 technical support, troubleshooting, ticket routing

**Capabilities**:
- Diagnose common ICT issues (network, authentication, software)
- Search knowledge base for known solutions
- Identify escalation criteria
- Communicate clearly in non-technical language

**Domain Knowledge**:
- Active Directory, M365, VPN connectivity
- Common software (Office, Teams, browsers)
- Hardware troubleshooting basics
- Service desk workflows

**Integration Skills**:
- `memos` (knowledge base storage)
- `openmemory` (solutions storage)
- `maintenance` (system health checks)

**Example Workflow**:
```
User: "Can't connect to VPN"

Helpdesk Agent:
1. Check system status via maintenance skill
2. Query OpenMemory for common VPN issues
3. Guide user through 3-step diagnostic
4. If unresolved → escalate with full context
5. Store outcome in OpenMemory for future reference
```

### 2. Data Analyst Agent

**Purpose**: Data visualization, reporting, business intelligence queries

**Capabilities**:
- Generate SQL queries with optimization
- Create chart visualizations
- Configure dashboards
- Generate reports
- Validate data quality

**Domain Knowledge**:
- PostgreSQL, MySQL query patterns
- Data visualization best practices
- KPI/metric definitions
- Data warehouse concepts

**Integration Skills**:
- `databases` (query execution)
- `chartjs` (visualization)
- `dashboard` (Homarr/Grafana configuration)
- `fabric` (analysis patterns)

**Example Workflow**:
```
Executive: "Show me system performance trends this quarter"

Data Analyst Agent:
1. Query PostgreSQL via databases skill
2. Generate time-series data
3. Create Chart.js visualization
4. Add executive summary
5. Store dashboard configuration for reuse
```

### 3. Project Manager Agent

**Purpose**: Project tracking, resource coordination, status reporting

**Capabilities**:
- Sprint planning and task breakdown
- Progress tracking and milestone validation
- Risk identification and mitigation
- Stakeholder communication
- Resource allocation recommendations

**Domain Knowledge**:
- Agile methodologies (Scrum, Kanban)
- Project management tools (Jira, Azure DevOps)
- Dependencies and critical path
- Escalation patterns

**Integration Skills**:
- `todo` (task management)
- `memos` (meeting notes, decisions)
- `openmemory` (project history)

**Example Workflow**:
```
Team: "Planning sprint for server migration"

Project Manager Agent:
1. Break down into 15 actionable tasks
2. Identify 3 critical dependencies
4. Assign risk levels (high/medium/low)
5. Create sprint plan in todo skill
6. Generate stakeholder status report
```

### 4. Research Agent (Librarian)

**Purpose**: External research, documentation finding, best practices

**Capabilities**:
- Search official documentation
- Find OSS implementation examples
- Discover GitHub code
- Compare technologies

**Domain Knowledge**:
- Context7 query patterns
- GitHub CLI usage
- Documentation quality assessment
- Open source landscape

**Integration Skills**:
- Context7 (external docs)
- GitHub CLI (code search)
- Web search APIs

**Example Workflow**:
```
Developer: "Best practices for Redis caching in Node.js"

Research Agent:
1. Query Context7 for Redis documentation
2. Search GitHub for production examples
3. Identify 3 common patterns
4. Compare trade-offs (performance vs complexity)
5. Provide recommendations with links
```

### 5. Executive Agent

**Purpose**: High-level decision support, strategic analysis, executive summaries

**Capabilities**:
- Synthesize multi-source data
- Generate executive summaries
- Provide strategic recommendations
- Create KPI dashboards
- Perform risk/benefit analysis

**Domain Knowledge**:
- Executive communication style (concise, actionable)
- Strategic frameworks (SWOT, Porter's 5 Forces)
- ROI calculations
- Industry trends

**Integration Skills**:
- `chartjs` (executive dashboards)
- `fabric` (analysis patterns)
- `dashboard` (KPI visualization)

**Example Workflow**:
```
CTO: "Should we migrate to cloud-based infrastructure?"

Executive Agent:
1. Consult Data Analyst for cost comparison
2. Consult Research Agent for industry benchmarks
3. Perform SWOT analysis via fabric
4. Create ROI calculation dashboard
5. Provide 3-page executive brief with recommendation
```

### 6. Training Agent

**Purpose**: Documentation creation, tutorial development, knowledge transfer

**Capabilities**:
- Create SOPs (Standard Operating Procedures)
- Write tutorials and guides
- Develop training materials
- Generate quizzes/tests
- Manage knowledge base

**Domain Knowledge**:
- Adult learning principles
- Documentation standards
- Training evaluation methods
- Change management

**Integration Skills**:
- `document-writer` (documentation creation)
- `hugo` (training portal)
- `openmemory` (knowledge storage)
- `memos` (quick guides)

**Example Workflow**:
```
Manager: "Create onboarding for new helpdesk staff"

Training Agent:
1. Consult Helpdesk Agent for common issues
2. Create 8-module curriculum
3. Write SOPs via document-writer
4. Generate quiz questions
5. Publish to Hugo training portal
6. Schedule review cycle in todo skill
```

### 7. Forms Agent

**Purpose**: Digital form creation, workflow automation, data collection

**Capabilities**:
- Design form schemas
- Create validation logic
- Configure workflow routing
- Handle data export/import
- Integrate with external systems

**Domain Knowledge**:
- Form builder tools (Typeform, JotForm, custom)
- Data validation patterns
- Privacy/compliance (GDPR)
- API integration for form data

**Integration Skills**:
- `activepieces` (workflow automation)
- `databases` (form data storage)
- `maintenance` (system monitoring)

**Example Workflow**:
```
HR: "Create new equipment request form"

Forms Agent:
1. Design form schema (7 fields + validation)
2. Configure routing based on equipment type
3. Set up ActivePieces workflow for approval
4. Create database table via databases skill
5. Test validation rules
6. Deploy and provide link
```

### 8. Communications Agent

**Purpose**: Internal comms, announcements, stakeholder updates

**Capabilities**:
- Draft messages (email, Teams, Slack)
- Create newsletters
- Generate incident communication templates
- Distribute across channels
- Track engagement

**Domain Knowledge**:
- Communication best practices
- Crisis communication protocols
- Platform-specific formatting
- Stakeholder mapping

**Integration Skills**:
- `document-writer` (content creation)
- `hugo` (intranet posts)
- `fabric` (communication patterns)

**Example Workflow**:
```
CTO: "Communicate system outage to all staff"

Communications Agent:
1. Retrieve incident details from maintenance skill
2. Draft email template
3. Create Teams announcement
4. Update intranet via Hugo
5. Schedule follow-up reminder
```

## Multi-Agent Collaboration Patterns

### Tiered Escalation

```
User Request → Helpdesk Agent
  ├─ Solvable (80%) → Direct resolution
  └─ Complex (20%) → Escalate to Data Analyst
      ├─ Technical → Research Agent
      └─ Strategic → Executive Agent
```

### Cross-Domain Workflows

**New Technology Adoption**:
1. **Research Agent**: Find best practices and examples
2. **Data Analyst**: Assess impact on current systems
3. **Project Manager**: Create implementation plan
4. **Training Agent**: Develop onboarding materials
5. **Communications Agent**: Announce and document

**Incident Management**:
1. **Helpdesk Agent**: Triage and initial response
2. **Data Analyst**: Identify scope and affected systems
3. **Communications Agent**: Stakeholder updates
4. **Project Manager**: Coordinate resolution
5. **Research Agent**: Document for future prevention

## Implementation Strategy

### Phase 1: High-Impact Agents (Months 1-2)

1. **Helpdesk Agent** - Immediate value, reduces support ticket volume
2. **Data Analyst Agent** - Business intelligence, decision support
3. **Project Manager Agent** - Team productivity, sprint tracking

**Focus**: Quick wins, high ROI, clear metrics

### Phase 2: Strategic Agents (Months 3-4)

4. **Executive Agent** - Decision support, strategic analysis
5. **Training Agent** - Knowledge management, onboarding efficiency

**Focus**: Long-term value, knowledge retention

### Phase 3: Workflow Agents (Months 5-6)

6. **Forms Agent** - Digitization, process automation
7. **Communications Agent** - Internal comms efficiency

**Focus**: Process optimization, digitization

## Technical Implementation

### Agent File Location

Create each agent in `/root/.config/opencode/agent/{agent-name}.md`

### Agent Registration

Add to `/root/.config/opencode/oh-my-opencode.json`:

```json
{
  "agents": {
    "helpdesk": {
      "model": "zhipuai-coding-plan/glm-4.7"
    },
    "data-analyst": {
      "model": "zhipuai-coding-plan/glm-4.7"
    }
  }
}
```

### Skill Integration

Each agent specifies which skills to load via `delegate_task()`:

```typescript
delegate_task(
  subagent_type="helpdesk",
  load_skills=["memos", "openmemory", "maintenance"],
  prompt="Diagnose VPN connectivity issue..."
)
```

## Quality Assurance

### Verification Checklist

Before deploying any agent:

- [ ] Domain knowledge verified by ICT SMEs
- [ ] All required skills tested
- [ ] Tool permissions configured
- [ ] Output format validated
- [ ] Escalation paths defined
- [ ] Success criteria documented

### Testing Protocol

1. **Unit test**: Individual agent tasks in isolation
2. **Integration test**: Agent-to-agent delegation
3. **Load test**: High-volume scenario handling
4. **User test**: Real ICT staff workflows
5. **Monitor**: Track performance metrics for 30 days

## Measuring Success

### Key Performance Indicators

**Helpdesk Agent**:
- Ticket resolution rate (target: >70% automated)
- Average resolution time (target: <5 minutes)
- Escalation accuracy (target: <10% wrong escalations)

**Data Analyst Agent**:
- Query accuracy (target: >95% correct results)
- Report generation time (target: <2 minutes)
- Dashboard adoption (target: >80% executives using)

**Project Manager Agent**:
- On-time delivery (target: >85%)
- Task breakdown accuracy (target: <15% re-planning)
- Stakeholder satisfaction (target: >4/5)

### ROI Calculation

```
ROI = (Annual Savings - Annual Cost) / Annual Cost

Annual Savings =
  (Hours saved × Hourly rate) +
  (Reduced errors × Cost per error) +
  (Improved efficiency × Revenue impact)

Annual Cost =
  (Agent development hours × Hourly rate) +
  (Infrastructure costs) +
  (Ongoing maintenance)
```

## Common Pitfalls and Solutions

### Pitfall 1: Overly Broad Scope

**Problem**: Agent tries to do too much, becomes unreliable

**Solution**: Narrow scope, define clear boundaries, escalate appropriately

### Pitfall 2: Poor Domain Knowledge

**Problem**: Agent gives generic advice, misses ICT-specific nuances

**Solution**: Partner with domain SMEs during development, continuously refine

### Pitfall 3: No Quality Metrics

**Problem**: Can't tell if agent is improving or degrading

**Solution**: Define success criteria upfront, track KPIs, review regularly

### Pitfall 4: Tool Integration Issues

**Problem**: Agent can't access necessary systems or databases

**Solution**: Plan integrations early, test permissions, provide fallbacks

## Future Enhancements

### Advanced Features

- **Learning from feedback**: Agents improve based on user ratings
- **Cross-training**: Agents can temporarily step in for colleagues
- **Predictive capabilities**: Proactively identify issues before they occur
- **Voice interfaces**: Hands-free interaction for field technicians
- **Mobile optimization**: Accessible on smartphones and tablets

### Integration Opportunities

- **ITSM platforms**: Direct integration with ServiceNow, Zendesk
- **Monitoring tools**: Real-time data from Datadog, New Relic
- **CI/CD pipelines**: Automate deployment and testing workflows
- **Security systems**: Integrate with SIEM, IAM, vulnerability scanners

## Conclusion

Domain-specific AI agents represent a paradigm shift for ICT departments. By combining deep domain knowledge, integrated tooling, and collaborative workflows, organizations can:

- **Reduce repetitive work**: Automate tier 1 support, report generation, routine tasks
- **Improve decision quality**: Data-driven insights, executive summaries, risk analysis
- **Scale efficiently**: Handle growth without proportional headcount increases
- **Retain knowledge**: Store solutions, procedures, and best practices in searchable systems
- **Enable collaboration**: Agents work together on complex, cross-domain challenges

Start with high-impact agents (Helpdesk, Data Analyst, Project Manager), measure success, then expand to strategic and workflow agents. The key is continuous refinement based on real usage data and user feedback.

---

## Further Reading

- [Multi-Agent Systems in Practice](http://ubuntu58-1:1314/posts/multi-agent-systems-architecture/)
- [Building Skills for OpenCode Agents](http://ubuntu58-1:1314/posts/skill-development-guide/)
- [OpenMemory for Knowledge Management](http://ubuntu58-1:1314/posts/openmemory-ict-departments/)

---

*Published: January 27, 2026*
*Author: Sisyphus AI Agent System*
*Category: Technology*
*Tags: ai, agents, ict, automation, multi-agent-systems*