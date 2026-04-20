---
pubDatetime: 2026-02-03T22:40:00Z
title: "Complete Task Flow Tracking: From Agent to Skill to Tool, Memory, and Final Changes"
postSlug: "complete-task-flow-tracking-agent-skill-tool-memory-changes"
description: "Complete Task Flow Tracking: From Agent to Skill to Tool, Memory, and Final Changes"
tags:
  - skills
  - openagents
  - automation
  - memory
  - monitoring
---

## The Missing Piece in Session Tracking

For weeks, we had session outcome tracking and skill usage analysis—but something was missing. We could see **what** was accomplished, but not **how** it was accomplished. We could track which skills were used, but not the complete journey from agent invocation to skill loading, tool execution, memory operations, and final file changes.

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

## Flow Visualization with Mermaid Diagrams

The system automatically generates Mermaid diagrams showing complete task flow:

{{< mermaid >}}
graph TD
    Start([Start Task])
    Agent1([OpenCode Agent])
    Skill1([Load: hugo])
    Tool1([Read: template.md])
    Tool2([Write: new-post.md])
    Memory1([Store: Draft])
    Tool3([Bash: build])
    End([End])

    Start --> Agent1
    Agent1 --> Skill1
    Skill1 --> Tool1
    Tool1 --> Tool2
    Tool2 --> Memory1
    Memory1 --> Tool3
    Tool3 --> End

    classDef agent fill:#b6e,stroke:#333,stroke-width:2px
    classDef skill fill:#9cf,stroke:#333,stroke-width:2px
    classDef tool fill:#69b,stroke:#333,stroke-width:2px
    classDef memory fill:#96f,stroke:#333,stroke-width:2px

    class Agent1 agent
    class Skill1 skill
    class Tool1,Tool2,Tool3 tool
    class Memory1 memory
{{< /mermaid >}}

**Color-coded by event type:**
- 🟦 Blue = Agents
- 🟩 Green = Skills
- 🟨 Orange = Tools
- 🟪 Purple = Memory

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

### 1. Task Flow Tracker (`task_flow_tracker.py`)

Core extraction engine that parses logs and builds flow data.

**Commands:**
```bash
# Extract flow from a session
python3 /media/docs/output/task_flow_tracker.py extract <session_id>

# Analyze flow and get insights
python3 /media/docs/output/task_flow_tracker.py analyze <session_id>
```

### 2. Task Flow Visualizer (`task_flow_visualizer.py`)

Creates visual representations of task flow.

**Commands:**
```bash
# Generate Mermaid diagram
python3 /media/docs/output/task_flow_visualizer.py generate <session_id>

# Analyze flow statistics
python3 /media/docs/output/task_flow_visualizer.py analyze <session_id>
```

### 3. Auto Session Logger (`auto_session_logger.py`)

Automates session flow extraction and outcome recording.

**Commands:**
```bash
# Scan and extract recent sessions
python3 /media/docs/output/auto_session_logger.py scan 7

# Get flow summary
python3 /media/docs/output/auto_session_logger.py summary
```

### 4. Session Analytics Dashboard (`session_analytics.py`)

Comprehensive dashboard combining outcomes and flow data.

**Commands:**
```bash
# Full analytics dashboard
python3 /media/docs/output/session_analytics.py dashboard 7
```

## Real-World Examples

### Example 1: Hugo Blog Post Creation

**Flow Sequence:**
```
OpenCode Agent → Load Hugo Skill → Read Template → Read Config → 
Write Post → Memory Store Draft → Bash Build → Browser Verify → 
Memory Store Outcome
```

**Statistics:**
- 1 agent, 1 skill, 5 tools, 2 memory stores, 4 file ops
- Flow complexity: Moderate (9 events)
- Outcome: Created Hugo blog post

### Example 2: System Maintenance

**Flow Sequence:**
```
OpenCode Agent → Load Maintenance Skill → Bash Check Services → 
Bash Restart Container → Memory Store Status → Write Log
```

**Statistics:**
- 1 agent, 1 skill, 3 tools, 1 memory store, 2 file ops
- Flow complexity: Simple (5 events)
- Outcome: System maintenance completed

### Example 3: Research Task

**Flow Sequence:**
```
OpenCode Agent → Load Research Skill → Memory Query Context → 
Web Search → Memory Store Findings → Write Report → 
Memory Store Outcome
```

**Statistics:**
- 1 agent, 1 skill, 4 tools, 2 memory stores, 1 file op
- Flow complexity: Simple (6 events)
- Outcome: Researched and documented topic

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

**Collaborator Pattern:**
- High agent usage
- High delegations
- Moderate tool usage
- Multiple skill interactions

## Storage Structure

All flow data stored in structured format:

```
/root/.local/share/opencode/storage/
├── task_flows/                      # NEW: Flow tracking data
│   ├── <session_id>.json          # Complete flow data
│   └── ...
├── session_outcomes/                # Session outcomes
├── session/                         # Session metadata
└── agent-usage-reminder/            # Agent usage records

/media/docs/output/
├── task-flow-tracker.py             # Core extraction
├── task-flow-visualizer.py          # Visualization
├── auto-session_logger.py           # Automation
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
# Comprehensive dashboard
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

## Future Enhancements

Potential improvements being considered:

1. **Integration with OpenCode UI** - Show flow in session view
2. **Real-time flow visualization** - Live updates during session
3. **Flow comparison** - Compare similar tasks across sessions
4. **Optimization suggestions** - AI-powered workflow optimization
5. **Export to external tools** - Integrate with other analytics platforms

## Conclusion

This comprehensive task flow tracking system fills a critical gap in observability. By automatically capturing the complete journey from agent invocation to final changes, we gain unprecedented visibility into how work gets done.

The system isn't just tracking—it's understanding. And with understanding comes the ability to optimize, improve, and become more effective.

**Ready to see your complete task flows?**

```bash
# Start extracting flows
python3 /media/docs/output/auto_session_logger.py scan 7

# Generate your first dashboard
python3 /media/docs/output/session_analytics.py dashboard 7
```

All data stored locally, fully integrated with existing session tracking, and automatically captured from OpenCode logs.

Your complete task flow journey is now visible.