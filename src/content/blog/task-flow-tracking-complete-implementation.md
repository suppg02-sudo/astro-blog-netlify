---
pubDatetime: 2026-02-03T23:00:00Z
title: "Task Flow Tracking: Complete Implementation for Agent→Skill→Tool→Memory→Changes"
postSlug: "task-flow-tracking-complete-implementation"
description: "Task Flow Tracking: Complete Implementation for Agent→Skill→Tool→Memory→Changes"
tags:
  - skills
  - openagents
  - automation
  - monitoring
  - workflow
---

## The Missing Piece in Session Tracking

For weeks, we had session outcome tracking and skill usage analysis—but something critical was missing. We could see **what** was accomplished, but not **how** it was accomplished. We could track which skills were used, but not the complete journey from agent invocation to skill loading, tool execution, memory operations, and final file changes.

Today, that changes.

## Introducing Complete Task Flow Tracking

I've built a comprehensive system that automatically captures the entire task execution flow:

**Agent → Skill → Tool → Memory → Changes**

This isn't just metadata—it's the complete story of how your tasks get done.

## What's Being Tracked

### 1. Agent Usage

**Which agents were invoked, when, and in what order.**

- Agent name and type
- Invocation count per session
- Order of agent calls

### 2. Skill Operations

**Every skill interaction is captured.**

- Skill loads from OpenCode
- Task delegations to subagents
- Skill usage frequency over time
- Skill effectiveness metrics

### 3. Tool Executions

**Complete tool call history with performance data.**

- Tool name and type (bash, read, write, edit, etc.)
- Execution duration (milliseconds)
- Order of tool calls
- Tool parameters and results

### 4. Memory Operations

**OpenMemory integration tracked comprehensively.**

- Memory stores (what you saved)
- Memory queries (what you retrieved)
- Memory list operations
- Memory reinforcement actions
- Memory gets for specific items

### 5. File Modifications

**Every file change is cataloged.**

- Files written (write tool)
- Files edited (edit tool)
- Files read (read tool)
- Scripts executed (bash tool)
- File paths and timestamps

## Flow Visualization

The system automatically generates Mermaid diagrams showing complete task flow:

{{< mermaid >}}
graph TD
    Start([Start Task])
    
    subgraph Agents["🟦 Agent Layer"]
        Agent1([OpenCode Agent])
        Agent2([Subagent])
        Agent3([Browser Automation])
    end
    
    subgraph Skills["🟩 Skill Layer"]
        Skill1([Load: hugo])
        Skill2([Load: opencode])
        Skill3([Delegate: presentation])
    end
    
    subgraph Tools["🟨 Tool Layer"]
        Tool1([bash: chmod scripts])
        Tool2([write: create files])
        Tool3([read: load config])
        Tool4([openmemory: store outcome])
        Tool5([bash: build site])
    end
    
    subgraph Memory["🟪 Memory Layer"]
        Mem1([Store: draft])
        Mem2([Query: related context])
        Mem3([Store: final outcome])
    end
    
    subgraph Files["🔴 File Layer"]
        File1([Write: .py scripts])
        File2([Write: .sh scripts])
        File3([Write: blog post])
    end
    
    End([Complete])

    Start --> Agent1
    Agent1 --> Skill1
    Skill1 --> Tool1
    Tool1 --> File1
    Skill1 --> Tool2
    Tool2 --> File2
    File2 --> Mem1
    Mem1 --> Skill2
    Skill2 --> Tool3
    Tool3 --> Tool5
    Tool5 --> File3
    File3 --> Mem2
    Mem2 --> Skill3
    Skill3 --> Mem3
    Mem3 --> End

    classDef agent fill:#b6e,stroke:#333,stroke-width:2px
    classDef skill fill:#9cf,stroke:#333,stroke-width:2px
    classDef tool fill:#69b,stroke:#333,stroke-width:2px
    classDef memory fill:#96f,stroke:#333,stroke-width:2px
    classDef file fill:#f96,stroke:#333,stroke-width:2px

    class Agent1 agent
    class Agent2,Agent3,Agent4,Agent5 subagents
    class Skill1,Skill2,Skill3 skill
    class Tool1,Tool2,Tool3,Tool4,Tool5 tool
    class Mem1,Mem2,Mem3 memory
    class File1,File2,File3 file
{{< /mermaid >}}

**Color-coded by event type:**
- 🟦 Blue = Agents (OpenCode, subagents)
- 🟩 Green = Skills (loaded, delegated)
- 🟨 Orange = Tools (bash, read, write, edit)
- 🟪 Purple = Memory (stores, queries)
- 🔴 Red = Files

## How It Works

### Automatic Extraction

The system parses OpenCode logs to extract flow data automatically:

1. **Scan Sessions**: Finds all recent sessions from storage
2. **Extract Logs**: Pulls relevant log lines for each session
3. **Parse Events**: Identifies agents, skills, tools, memory ops, file ops
4. **Build Flow**: Assembles complete timeline in order
5. **Generate Stats**: Calculates comprehensive statistics
6. **Store Data**: Saves as JSON for future analysis

No manual recording required—just let the system scan and capture.

### Real-Time Monitoring

For ongoing sessions, you can monitor in real-time:

```bash
# Monitor for new sessions (auto-capture every 60 seconds)
python3 /media/docs/output/auto_session_logger.py monitor 60
```

The system detects new sessions and automatically extracts their flow data as they complete.

## Complete System Architecture

The flow tracking system consists of four integrated components:

### Task Flow Tracker (`task_flow_tracker.py`)

Core extraction engine that parses logs and builds flow data.

**Features**:
- Agent usage tracking from `agent-usage-reminder` storage
- Tool execution parsing (completion, duration)
- Skill usage detection (loads, delegations)
- Memory operation tracking (stores, queries, lists)
- File operation detection (reads, writes, edits, scripts)
- Flow sequence building with timestamps
- Statistics aggregation

### Task Flow Visualizer (`task_flow_visualizer.py`)

Creates visual representations of task flow.

**Features**:
- Mermaid diagram generation
- Detailed flow breakdown table
- Node coloring by type (agent, skill, tool, memory, file)
- Timeline visualization

### Auto Session Logger (`auto_session_logger.py`)

Automates session flow extraction and outcome recording.

**Features**:
- Scan recent sessions
- Extract flow data automatically
- Auto-generate session outcomes
- Monitor for new sessions (real-time)
- Generate summary reports

### Session Analytics Dashboard (`session_analytics.py`)

Comprehensive dashboard combining outcomes and flow data.

**Features**:
- Integration with outcome tracking
- Integration with flow tracking
- Skill usage analysis
- File change metrics
- Automated insights and recommendations

## Real-World Examples

### Example 1: Hugo Blog Post Creation

**Flow Sequence**:
```
OpenCode Agent → Load Hugo Skill → Read Template → Read Config → 
Write Post → Memory Store Draft → Bash Build → Browser Verify → 
Memory Store Outcome
```

**Statistics**:
- 1 agent, 1 skill, 5 tools, 2 memory stores, 4 file ops
- Flow complexity: Moderate (9 events)
- Outcome: "Created Hugo blog post"

### Example 2: System Maintenance

**Flow Sequence**:
```
OpenCode Agent → Load Maintenance Skill → Bash Check Services → 
Bash Restart Container → Memory Store Status → Write Log
```

**Statistics**:
- 1 agent, 1 skill, 3 tools, 1 memory store, 2 file ops
- Flow complexity: Simple (5 events)
- Outcome: "System maintenance completed"

### Example 3: Research Task

**Flow Sequence**:
```
OpenCode Agent → Load Research Skill → Memory Query (Context) → 
Web Search → Memory Store Findings → Write Report → 
Memory Store Outcome
```

**Statistics**:
- 1 agent, 1 skill, 4 tools, 2 memory stores, 1 file op
- Flow complexity: Simple (6 events)
- Outcome: "Researched and documented topic"

## Analytics and Insights

### Flow Complexity Analysis

The system categorizes flows by complexity:

- **Simple (1-10 events)**: Focused task with clear linear path
- **Moderate (11-30 events)**: Multi-step task with some branching
- **Complex (30+ events)**: Large task with many steps, potential for decomposition

### Effectiveness Metrics

Track performance across dimensions:

**Tool Efficiency:**
- Events per tool execution
- Average tool duration
- Tool usage patterns

**Skill Utilization:**
- Outcomes per skill use
- Skill load frequency
- Most effective skills

**Agent Performance:**
- Tasks completed per agent invocation
- Delegation depth
- Success rate

### Pattern Detection

The system identifies work patterns:

**Planner Pattern:**
- Low file operations
- High memory operations
- Low tool executions
- High outcome documentation

**Implementer Pattern:**
- High file operations
- High tool executions
- Low memory queries
- Direct execution focus

**Researcher Pattern:**
- High memory queries
- High web searches
- Moderate documentation
- Low file changes

## Storage Structure

All flow data stored in structured format:

```bash
/root/.local/share/opencode/storage/
├── task_flows/                      # NEW: Flow tracking data
│   ├── <session_id>.json          # Complete flow data
│   └── ...
├── session_outcomes/                # Session outcomes
├── session/                         # Session metadata
└── agent-usage-reminder/            # Agent usage records

/media/docs/output/
├── task_flow_tracker.py             # Core extraction
├── task_flow_visualizer.py          # Visualization
├── auto_session_logger.py           # Automation
├── session_analytics.py              # Dashboard
├── task-flow-<session_id>.md       # Generated diagrams
└── flow-summary-<date>.md          # Aggregate reports
```

## Integration with Existing Systems

The flow tracking system integrates seamlessly with:

### Session Outcome Tracking
- Manual outcome recording still available
- Auto-generates outcomes from flow data
- Combines with manual outcomes for complete picture

### Skill Usage Analysis
- Flow data enhances skill metrics
- Provides execution context for skills
- Shows skill effectiveness with actual usage patterns

### OpenMemory
- Memory operations fully tracked
- Stores flow metadata as memories
- Retrieves flow history via queries

## Benefits

### 1. Complete Visibility

See the entire journey from start to finish—not just the result.

### 2. Performance Insights

Identify bottlenecks, slow tools, inefficient patterns.

### 3. Workflow Optimization

Find optimal paths, eliminate redundant steps, improve efficiency.

### 4. Pattern Recognition

Understand how you work and optimize workflows accordingly.

### 5. Automatic Documentation

No manual recording required—system captures everything automatically.

## Getting Started

### Quick Demo

See the system in action:

```bash
# Run complete demo
bash /media/docs/output/task_flow_demo.sh
```

This shows sample flow data, visualizations, and statistics.

### Extract Existing Sessions

```bash
# Extract flows from last 7 days
python3 /media/docs/output/auto_session_logger.py scan 7
```

### Generate Visualizations

```bash
# Create Mermaid diagram
python3 /media/docs/output/task_flow_visualizer.py generate <session_id>
```

### Full Analytics

```bash
# Comprehensive dashboard with all data
python3 /media/docs/output/session_analytics.py dashboard 7
```

## Advanced Usage

### Real-Time Monitoring

Monitor for new sessions and auto-capture flow data:

```bash
# Check every 60 seconds
python3 /media/docs/output/auto_session_logger.py monitor 60
```

### Custom Analysis

Analyze specific sessions in detail:

```bash
# Extract flow
python3 /media/docs/output/task_flow_tracker.py extract <session_id>

# Analyze statistics
python3 /media/docs/output/task_flow_tracker.py analyze <session_id>

# Generate visualization
python3 /media/docs/output/task_flow_visualizer.py generate <session_id>
```

## Conclusion

This comprehensive task flow tracking system fills a critical gap in observability. By automatically capturing the complete journey from agent invocation to final changes, we gain unprecedented visibility into how work gets done.

The system isn't just tracking—it's understanding. And with understanding comes to ability to optimize, improve, and become more effective.

**Ready to see your complete task flows?**

```bash
# Start extracting flows
python3 /media/docs/output/auto_session_logger.py scan 7

# Generate your first dashboard
python3 /media/docs/output/session_analytics.py dashboard 7
```

All data stored locally, fully integrated with existing session tracking, and automatically captured from OpenCode logs.

Your complete task flow journey is now visible.