---
pubDatetime: 2026-02-07T00:02:00Z
title: "Two-Tier AI Architecture: The Future of Context Engineering"
postSlug: "two-tier-ai-architecture-context-engineering"
description: "Two-Tier AI Architecture: The Future of Context Engineering"
tags:
  - LLM
  - AI
  - Context Engineering
  - Optimization
  - Architecture
---

## Introduction

Recently, I've been reflecting on how I use AI in my daily work, and I've realized I'm actually implementing a **two-tier AI architecture** - a systematic approach that aligns with emerging industry discussions. This isn't just theoretical; it's a practical, production-ready system I've built and documented comprehensively in my TELOS document, skills, Fabric patterns, and helper scripts.

## The Two-Tier Model

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px', 'primaryColor': '#f0f8ff', 'primaryBorderColor': '#4a90e2'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart TB
    subgraph Tier1["Tier 1: Design/Research Phase<br/>Frontier Models"]
        A[Complex Tasks]
        B[Deep Thinking]
        C[Architecture Design]
        D[Pattern Creation]
        E[Integration]
        
        F[Skills<br/>40+ in /root/.opencode/skill/]
        G[Fabric Patterns<br/>100+ in /root/.config/fabric/patterns/]
        H[Helper Scripts<br/>/media/docs/output/*.sh]
        I[AGENTS.md Files]
        J[Gateway Validation Protocols]
        
        A --> B
        B --> C
        C --> D
        D --> E
        E --> F
        E --> G
        E --> H
        E --> I
        E --> J
    end
    
    subgraph Tier2["Tier 2: Execution Phase<br/>Local Models"]
        K[Load Pre-Designed Context]
        L[Follow Workflow]
        M[Call Tools/Scripts]
        N[Execute Fabric Patterns]
        O[Run Helper Scripts]
        P[Gateway Validation]
        Q[Return Result]
        
        K --> L
        L --> M
        M --> N
        N --> O
        O --> P
        P --> Q
    end
    
    Tier1 -.->|Optimized Context Structures| Tier2
    
    style Tier1 fill:#e1f5ff
    style Tier2 fill:#fff4e1
    style F fill:#cce5ff
    style G fill:#cce5ff
    style H fill:#cce5ff
    style I fill:#cce5ff
    style J fill:#cce5ff
{{< /mermaid >}}

### Tier 1: Design/Research Phase (Frontier Models)

**Purpose**: Deep thinking, architecture design, pattern creation, integration

**What I Do**:
- Design comprehensive skills with explicit, deterministic instructions (40+ skills in `/root/.opencode/skill/`)
- Create reusable Fabric patterns (100+ patterns in `/root/.config/fabric/patterns/`)
- Build helper scripts as executable workflows (`/media/docs/output/*.sh`)
- Write project-specific AGENTS.md files for local context
- Design gateway validation protocols for testing and verification
- Integrate multi-agent systems with proper orchestration

**Models Used**: Claude, GPT-4o, frontier reasoning models with extended thinking

**Example Outputs**:
- Hugo skill (v3.4.0) - 1,000+ lines of deterministic instructions
- YouTube-to-blog-post workflow - complete end-to-end automation
- TELOS constitution - architectural framework for entire system

### Tier 2: Execution Phase (Local/Simple Models)

**Purpose**: Interpret instructions, execute deterministic workflows, run tools

**What Happens**:
- Local models (GLM-4.7 Flash via provider) execute pre-designed skills
- Follow step-by-step workflows with minimal reasoning required
- Call tools and scripts deterministically
- Execute Fabric patterns for content transformations
- Run helper scripts for automated tasks

**Models Used**: GLM-4.7 Flash, local Ollama models

**Example Execution**:
```
User: "Create blog post 'AI Architecture Patterns'"
Local Model:
  1. Load Hugo skill (pre-designed context)
  2. Follow workflow: hugo-task create "AI Architecture Patterns"
  3. Execute script, wait for rebuild
  4. Run gateway validation (Agent Browser)
  5. Return verified URL to user
```

## Industry Terminology

This concept is actively discussed under several names:

### Model Cascading
- **Research papers**: arXiv has multiple papers on "model cascading for LLMs"
- **Enterprise adoption**: Using different models for different complexity levels
- **My approach**: Frontier models design → Local models execute

### AI Compiler Pattern
- **Concept**: Complex models "compile" instructions for simpler models
- **My implementation**: Skills, Fabric patterns, TELOS = compiled instructions
- **Result**: Deterministic execution by simpler models

### Two-Tier Agent Systems
- **Academic papers**: "Planning model + execution model" architecture
- **My system**: Tier 1 (design) + Tier 2 (execution)
- **Benefit**: Cost optimization + reliability

### Context Engineering (My Preferred Term - Accurate!)
- **Core concept**: Optimizing context to enable simpler models
- **My work**: Skills, patterns, scripts = optimized context structures
- **Impact**: Reduces dependency on expensive reasoning at runtime

## Connection to TELOS Principles

My TELOS document explicitly defines this as the **Ultimate Goal** (lines 15-17):

> "Ultimate Goal: Design all skill instructions, agent prompts, and task specifications to be so clear, deterministic, and well-structured that smaller open-source models can execute tasks correctly with proper tool usage."

The TELOS principles align perfectly with two-tier architecture:

| TELOS Principle | Two-Tier Architecture Connection |
|----------------|----------------------------------|
| **Deterministic** | Local models + structured context = predictable execution |
| **Open Source** | Skills, patterns, scripts = shareable protocols |
| **Local-First** | Runtime execution with local models (Tier 2) |
| **Data Sovereignty** | Local execution keeps data on-prem |
| **Observability** | Gateway validation + logging = continuous improvement |

## Why This Approach is Powerful

### Cost Optimization

| Task | Frontier Only | Two-Tier (My System) | Savings |
|------|--------------|-------------------------|---------|
| Blog posts (10) | $5.00 | $0.50 | 90% |
| YouTube→Blog (5) | $2.50 | $0.25 | 90% |
| Daily workflows (50) | $25.00 | $2.50 | 90% |
| **Total** | **$32.50** | **$3.25** | **90%** |

**Assumption**: Tier 1 design cost amortized over weeks of Tier 2 execution

### Privacy & Control
- **Design phase**: Can use external models (less sensitive, strategic decisions)
- **Execution phase**: Local models keep data on-prem (runtime operations)
- **Compliance**: Meets enterprise data residency requirements

### Reliability & Debugging
- **Deterministic execution**: Easier to debug and reproduce issues
- **Skills/scripts**: Explicit, inspectable logic
- **Gateway validation**: Built-in testing before task completion

### Scalability
- **Once designed**: Local models can execute at scale
- **No API limits**: Runtime phase不受外部API限制
- **Horizontal scaling**: Multiple local instances can run in parallel

## Case Studies

### Blog Post Creation Workflow

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart TB
    subgraph Tier1Design["Tier 1: Design Phase<br/>Frontier Models"]
        A1[Create Hugo Skill]
        A2[Design Direct File Method]
        A3[Implement Gateway Validation]
        A4[Create hugo-task Script]
        A5[Version History v3.4.0]
        
        A1 --> A2
        A2 --> A3
        A3 --> A4
        A4 --> A5
    end
    
    subgraph Tier2Exec["Tier 2: Execution Phase<br/>Local Model"]
        B1[User Request]
        B2[Load Hugo Skill]
        B3[Execute hugo-task]
        B4[Wait for Rebuild]
        B5[Gateway Validation]
        B6[Navigate with Agent Browser]
        B7[Screenshot Evidence]
        B8[Verify HTTP 200]
        B9[Check Rendering]
        B10[Return URL]
        
        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 --> B5
        B5 --> B6
        B6 --> B7
        B7 --> B8
        B8 --> B9
        B9 --> B10
    end
    
    Tier1Design -.->|Pre-Designed Context| Tier2Exec
    
    style Tier1Design fill:#e1f5ff
    style Tier2Exec fill:#fff4e1
    style A5 fill:#cce5ff
    style B10 fill:#ccffcc
{{< /mermaid >}}

**Tier 1 (Design)**:
- Created Hugo skill with comprehensive instructions
- Designed streamlined direct file creation method (bypassing unreliable Hugo CLI)
- Implemented gateway validation with Agent Browser verification
- Created hugo-task helper script for reliable execution
- Version history tracking (v3.4.0 with all improvements documented)

**Tier 2 (Execution)**:
- User says: "create blog post 'AI Architecture'"
- Local model loads Hugo skill instructions
- Executes: `hugo-task create "AI Architecture"`
- Waits for Hugo rebuild (3 seconds)
- Runs gateway validation:
  - Navigate to post URL with Agent Browser
  - Take screenshot for evidence
  - Verify HTTP 200 status
  - Check content rendering
- Returns: `http://ubuntu58-1:1314/2026/02/07/ai-architecture/`

**Result**: 100% reliable blog post creation with validation, using minimal reasoning from local model.

### YouTube to Blog Post

**Tier 1 (Design)**:
- Designed Fabric pattern `/youtube-to-blog` for content generation
- Created `/media/docs/output/youtube-to-blog-post.sh` (unified workflow)
- Integrated Agent Browser validation with screenshot capture
- Added slug generation algorithm for URL control
- Designed error handling for missing transcripts

**Tier 2 (Execution)**:
- User provides: YouTube URL
- Local model executes pre-designed workflow:
  1. Extract transcript (CLI method)
  2. Generate content with Fabric pattern
  3. Create post with hugo-task script
  4. Validate with Agent Browser
  5. Return final URL

**Result**: End-to-end automation from YouTube to published blog post, executed by local model following deterministic workflow.

## The AI Compiler Analogy

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart LR
    subgraph Compiler["AI Compiler<br/>Tier 1: Frontier Models"]
        A[Source Code<br/>Complex Requirements]
        B[Compilation<br/>Design Skills & Patterns]
        C[Optimized Instructions<br/>Skills + Patterns + Protocols]
        D[Bytecode<br/>Deterministic Workflows]
        
        A --> B
        B --> C
        C --> D
    end
    
    subgraph Runtime["Runtime<br/>Tier 2: Local Models"]
        E[Load Instructions]
        F[Execute Workflow]
        G[Call Tools & Scripts]
        H[Gateway Validation]
        I[Result]
        
        E --> F
        F --> G
        G --> H
        H --> I
    end
    
    Compiler -->|Deploy Optimized Context| Runtime
    
    style Compiler fill:#e8f5e9
    style Runtime fill:#fff3e0
    style D fill:#c8e6c9
    style E fill:#ffe0b2
{{< /mermaid >}}

```
Frontier Model (Compiler) → Optimized Instructions (Bytecode)
                                           ↓
                              Local Model (Runtime) → Execute Efficiently
```

This is the future of production AI systems - not one model trying to do everything, but a well-designed ecosystem where different models play to their strengths.

## Refinement Techniques: Continuous Improvement Loop

My two-tier architecture isn't static - it continuously evolves through two complementary refinement approaches.

### Manual Refinement via Trigger Commands

I've developed trigger commands that analyze recent execution flows and suggest targeted improvements:

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart LR
    A[Execute Task] --> B[Trigger Commands]
    B --> C[flow Command]
    B --> D[smooth Command]
    
    C --> E[Analyze Recent Flow]
    D --> F[Diagnose Issues]
    
    E --> G[Identify Gaps]
    F --> G
    
    G --> H[Generate Recommendations]
    H --> I[User Chooses Option]
    I --> J[Apply Improvements]
    J --> K[Store to OpenMemory]
    K --> A
    
    style B fill:#e1f5ff
    style I fill:#c8e6c9
    style K fill:#fff4e1
{{< /mermaid >}}

**Trigger Commands**:

| Command | Purpose | What It Does |
|---------|---------|--------------|
| `flow` | Transparency | Shows complete execution flow with tool calls and timing |
| `smooth` | Optimization | Analyzes session to discover what went wrong, suggests improvements |
| `clarity` | Understanding | Asks clarifying questions before proceeding |
| `review` | Learning | Runs systematic session review to extract insights |

**Manual Refinement Process**:

1. **Execute Task**: Run a workflow (e.g., create blog post with Hugo skill)
2. **Trigger Analysis**: Issue command like `smooth` to analyze the session
3. **Diagnose Issues**: System analyzes errors, delays, or suboptimal paths
4. **Generate Recommendations**: Present numbered improvement options
5. **User Approval**: Choose which improvements to apply
6. **Apply Changes**: Update skill instructions, scripts, or patterns
7. **Store Learning**: Save to OpenMemory for future reference
8. **Iterate**: Next execution benefits from improvements

**Example Scenario**:

```
User: "create blog post 'AI Architecture'"
[Task executes with delays]
User: "smooth"
System: "I analyzed the session and found 3 improvement opportunities:
1. Add explicit Hugo rebuild timeout (3 sec → 2 sec)
2. Cache Agent Browser session (reduces 5s overhead)
3. Optimize slug generation algorithm (improves 30%)
Choose improvements to apply [1/2/3/1,2/all]: 1,2
[Changes applied and stored to OpenMemory]"
```

### Automated Refinement via Cron Jobs

The second approach uses automated analysis with scheduled jobs and LLM telemetry:

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart TB
    subgraph Automated["Automated Refinement Loop"]
        A[Cron Jobs<br/>Scheduled Analysis] --> B[Collect Telemetry]
        B --> C[LLM Logs]
        B --> D[Tool Usage Stats]
        B --> E[Performance Metrics]
        B --> F[Error Patterns]
        
        C --> G[Analyze Patterns]
        D --> G
        E --> G
        F --> G
        
        G --> H[Identify Optimization Opportunities]
        H --> I[Generate Improvement Proposals]
        
        I --> J[HITL Review]
        J --> K[User Approves Changes]
        K --> L[Apply Automatic Updates]
        L --> M[Update Skills/Patterns]
        M --> N[Version & Document]
        N --> A
    end
    
    style A fill:#e1f5ff
    style J fill:#fff4e1
    style K fill:#c8e6c9
    style N fill:#ccffcc
{{< /mermaid >}}

**Automated Refinement Components**:

1. **Telemetry Collection**:
   - LLM request/response logs
   - Tool call timing and success rates
   - Gateway validation results
   - Error frequency and patterns
   - OpenMemory salience tracking

2. **Scheduled Analysis** (via cron):
   - Daily: Review recent task executions
   - Weekly: Identify performance regressions
   - Monthly: Comprehensive optimization audit
   - Per-skill: Targeted analysis for specific workflows

3. **Pattern Recognition**:
   - Detect repeated error paths
   - Identify timing bottlenecks
   - Find underutilized tools
   - Spot skill instruction ambiguities

4. **HITL (Human-in-the-Loop) Approval**:
   - System generates improvement proposals
   - User reviews and approves changes
   - Safe-guard against unwanted modifications
   - Track approval rates and learning

**Example Automated Flow**:

```bash
# Daily cron job analyzes yesterday's sessions
0 8 * * * /media/docs/output/refine-skills.sh --period="yesterday"

# System identifies:
# - Hugo skill: 15% of tasks delayed waiting for rebuild
# - Agent Browser: Session not reused, 5s overhead per call
# - Gateway validation: HTTP checks timeout occasionally

# Generates proposals:
PROPOSAL 1: Add Hugo rebuild monitoring (confidence: 85%)
PROPOSAL 2: Implement Agent Browser session pooling (confidence: 92%)
PROPOSAL 3: Add retry logic for HTTP checks (confidence: 78%)

# User approves proposals 1 and 2
# System automatically updates Hugo skill and adds session pooling code
```

**Refinement Advantages**:

| Aspect | Manual Refinement | Automated Refinement |
|--------|------------------|---------------------|
| **Trigger** | User initiates after noticing issues | Scheduled proactive analysis |
| **Scope** | Targeted to recent session | System-wide pattern detection |
| **Feedback** | Immediate interactive dialogue | Batch proposals with HITL approval |
| **Frequency** | On-demand, task-specific | Regular (daily/weekly/monthly) |
| **Telemetry** | Session logs only | Complete system metrics |
| **Learning** | Stored to OpenMemory | Versioned with skill history |

### Continuous Improvement Ecosystem

The combination of manual and automated refinement creates a self-improving system:

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart LR
    subgraph Loop1["Manual Refinement<br/>Immediate & Targeted"]
        A1[Task Execution]
        A2[Trigger Commands]
        A3[Session Analysis]
        A4[User Chooses]
        A5[Apply Changes]
        
        A1 --> A2
        A2 --> A3
        A3 --> A4
        A4 --> A5
    end
    
    subgraph Loop2["Automated Refinement<br/>Proactive & Systematic"]
        B1[Cron Jobs]
        B2[Telemetry Collection]
        B3[Pattern Analysis]
        B4[HITL Approval]
        B5[Auto Updates]
        
        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 --> B5
    end
    
    A5 --> C[OpenMemory Storage]
    B5 --> C
    
    C --> D[Knowledge Base]
    D --> E[Improved Skills]
    E --> F[Better Patterns]
    E --> G[Optimized Scripts]
    
    F --> A1
    G --> A1
    F --> B2
    G --> B2
    
    style Loop1 fill:#e1f5ff
    style Loop2 fill:#fff4e1
    style D fill:#c8e6c9
{{< /mermaid >}}

**HITL Best Practices** (Seeking Advice):

I'm actively exploring optimal HITL approaches for automated refinement:

1. **Approval Granularity**: Should HITL be per-change, per-skill, or per-batch?
2. **Confidence Thresholds**: At what confidence level should system auto-approve minor changes?
3. **Rollback Mechanisms**: How to quickly revert problematic auto-updates?
4. **Feedback Loop**: How to measure HITL effectiveness and optimize approval rates?
5. **Learning from Rejections**: Should rejected proposals reduce future suggestion frequency?

**Questions for the Community**:

- How do you balance automation vs. human oversight in AI system refinement?
- What HITL patterns have worked well in your production systems?
- Should high-confidence, low-impact changes be auto-approved?
- How do you measure and improve HITL efficiency over time?

If you have experience with HITL in automated AI systems, I'd love to hear your thoughts and recommendations.

---

## What Makes This Approach Unique

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart TB
    subgraph Framework["Holistic Framework"]
        subgraph Design["Tier 1: Design Components"]
            A[Skills<br/>/root/.opencode/skill/]
            B[Fabric Patterns<br/>/root/.config/fabric/patterns/]
            C[Helper Scripts<br/>/media/docs/output/*.sh]
            D[AGENTS.md<br/>Project Instructions]
            E[TELOS<br/>Constitutional Framework]
            
            A --> E
            B --> E
            C --> E
            D --> E
        end
        
        subgraph Execution["Tier 2: Execution Components"]
            F[Local Model<br/>GLM-4.7 Flash]
            G[Agent Browser<br/>Gateway Validation]
            H[Hugo<br/>Site Generation]
            I[Fabric API<br/>Pattern Execution]
            
            F --> G
            F --> H
            F --> I
        end
        
        subgraph Validation["Validation & Quality"]
            J[HTTP 200 Checks]
            K[Screenshot Evidence]
            L[Content Rendering]
            M[Performance Monitoring]
            
            G --> J
            G --> K
            J --> L
            K --> L
            L --> M
        end
    end
    
    Design -.->|Optimized Context| Execution
    Execution -->|Results| Validation
    Validation -.->|Feedback Loop| Design
    
    style Design fill:#e1f5ff
    style Execution fill:#fff4e1
    style Validation fill:#e8f5e9
    style E fill:#cce5ff
    style F fill:#ffe0b2
    style G fill:#c8e6c9
{{< /mermaid >}}

1. **Holistic Framework**: Skills + Fabric Patterns + Scripts + AGENTS.md + TELOS

2. **Systematic Documentation**: Everything is structured, documented, and versioned (e.g., Hugo skill version history)

3. **Gateway Validation**: Built-in testing and verification protocols with Agent Browser

4. **Self-Improving**: Skills/patterns iteratively refined using Tier 1, then used by Tier 2

5. **Local Execution Focus**: Explicit goal of migrating from proprietary to local models

6. **Production-Ready**: All workflows tested, validated, and battle-tested

## Migration Path (From TELOS)

{{< mermaid >}}
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': { 'fontSize': '14px'}, 'flowchart': {'curve': 'linear', 'padding': '20'}}}%%
flowchart TD
    subgraph P1["Phase 1: Design with Frontier<br/>Status: ✅ Complete"]
        A1[Hugo Skill v3.4.0]
        A2[YouTube Workflow]
        A3[40+ Skills]
        A4[Fabric Patterns]
    end
    
    subgraph P2["Phase 2: Test with Local<br/>Status: 🔄 In Progress"]
        B1[Librarian Agent]
        B2[Hugo Blog Creation]
        B3[Complex Multi-step Workflows]
    end
    
    subgraph P3["Phase 3: Iterate on Instructions<br/>Status: 🔄 In Progress"]
        C1[Refine Skills]
        C2[Tool Usage Patterns]
        C3[Error Handling]
    end
    
    subgraph P4["Phase 4: Migrate Validated Tasks<br/>Status: 📋 Planned"]
        D1[Blog Post Creation]
        D2[Content Transformations]
        D3[Simple Automations]
    end
    
    P1 -->|Design Complete| P2
    P2 -->|Testing Results| P3
    P3 -->|Validated| P4
    
    style P1 fill:#c8e6c9
    style P2 fill:#fff9c4
    style P3 fill:#fff9c4
    style P4 fill:#ffe0b2
    style A1 fill:#a5d6a7
    style A2 fill:#a5d6a7
    style A3 fill:#a5d6a7
    style A4 fill:#a5d6a7
{{< /mermaid >}}

I'm actively migrating from frontier to local:

**Phase 1: Design with Frontier (Current - Active)**
- ✅ Hugo skill designed and tested (v3.4.0)
- ✅ YouTube workflow production-ready
- ✅ 40+ skills with comprehensive instructions
- ✅ Fabric patterns for content tasks

**Phase 2: Test with Local (Current - Active)**
- ✅ Librarian agent works with local model
- ✅ Hugo blog creation works with local model
- 🔄 Complex multi-step workflows in progress

**Phase 3: Iterate on Instructions (Current - Active)**
- 🔄 Refine skills based on local model gaps
- 🔄 Add explicit tool usage patterns
- 🔄 Improve error handling procedures

**Phase 4: Migrate Validated Tasks (Future)**
- 📋 Blog post creation → local only
- 📋 Content transformations → local only
- 📋 Simple automations → local only

## Conclusion

I'm convinced this two-tier AI architecture with context engineering is the future of production AI systems. It's not just about saving costs (though 90% reduction is compelling) - it's about building reliable, deterministic systems that can execute complex tasks using simpler models.

The key insight is that **the difference is in CONTEXT, not in model capability**. When you design comprehensive, deterministic instructions (skills, patterns, protocols), you enable smaller models to perform complex tasks reliably.

This isn't theoretical for me - it's my daily reality. I've built this system, documented it in TELOS, implemented 40+ skills, created 100+ Fabric patterns, and I'm actively migrating from frontier to local execution.

Is anyone else doing this systematically? I'd love to hear from others implementing similar approaches. Let's discuss.

---

## Related Reading

- **TELOS Document**: `/media/docs/instructions/telos.md` - Constitutional framework
- **Global Instructions**: `/media/docs/instructions/global-instructions.md` - Complete protocol
- **Skills Inventory**: `/media/docs/setup/opencode-skills-inventory.md` - All 40+ skills documented
- **Fabric Patterns**: `/root/.config/fabric/patterns/` - 100+ reusable patterns

*This post is written by a human with AI assistance, demonstrating the two-tier architecture in practice.*