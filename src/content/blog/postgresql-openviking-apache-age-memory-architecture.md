---
pubDatetime: 2026-03-17T00:00:00Z
title: "From Flat to Hierarchical: Supercharging PostgreSQL Memory with OpenViking + Apache AGE"
postSlug: "postgresql-openviking-apache-age-memory-architecture"
description: "Three-layer memory architecture combining PostgreSQL relational storage, OpenViking hierarchical patterns, and Apache AGE graph relationships for intelligent AI agent context management"
tags:
  - apache-age
  - ai-agents
  - context-management
  - postgresql
  - memory-architecture
  - openviking
---

## The Problem: Context Rot in AI Agents

You've spent months building an AI agent system. You have 2,800+ memories stored. But something breaks:

- **Context bloat**: Loading full memory content consumes 2k tokens per memory
- **No relationships**: Can't trace "which skill is used in this decision"
- **Flat organization**: Search is semantic noise, not structural clarity
- **Memory decay**: Old preferences aren't connected to current understanding
- **No evolution**: When you change your mind, there's no record of *why*

You're stuck with a **relational database designed for transactions, not context**.

---

## The Solution: Three-Layer Memory Architecture

Instead of replacing PostgreSQL (which works well), we enhance it with two complementary layers:

```
┌─────────────────────────────────────────────────────────────┐
│              AI Agent (Superpowers + Fabric)                 │
│      Uses all three layers for intelligent context          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│        Layer 1: Relational (PostgreSQL + pgvector)          │
│  ├─ Fast CRUD operations                                    │
│  ├─ Vector similarity search for initial relevance         │
│  └─ Transaction guarantees (ACID)                           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│    Layer 2: Hierarchical (OpenViking Patterns)              │
│  ├─ Structured URIs: viking://user/memories/preferences    │
│  ├─ Tiered loading: L0 (100 tokens) → L1 (2k) → L2 (full) │
│  ├─ Directory recursive retrieval                           │
│  └─ Session tracking & auto-extraction                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│      Layer 3: Graph (Apache AGE)                            │
│  ├─ Memory relationships: USES, BASED_ON, CONTRADICTS      │
│  ├─ Skill dependencies: DEPENDS_ON chains                  │
│  ├─ Context propagation: IN_CONTEXT relationships          │
│  └─ Evolution tracking: EVOLVED_FROM chains                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│            PostgreSQL (All in One Database)                 │
│  ├─ Tabular + Graph + Hierarchical relationships            │
│  ├─ ACID transactions across all three layers              │
│  └─ Zero additional infrastructure                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer 1: PostgreSQL Relational (Existing Foundation)

Your current setup already has this. Let's clarify what stays:

### Current Schema

```sql
CREATE TABLE memories (
    memory_id UUID PRIMARY KEY,
    content TEXT NOT NULL,
    embedding vector(1536),
    memory_type VARCHAR (decision, action, conversation),
    tags TEXT[],
    metadata JSONB,
    scope VARCHAR (user, project),
    priority INT (1-10),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

### What It Does Well

- **Fast search**: Vector similarity in milliseconds
- **Flexible metadata**: JSONB for arbitrary attributes
- **Transaction safety**: ACID guarantees
- **CLI access**: pghmem tool for quick queries

### What It Lacks

- No hierarchy (flat table)
- No tiered loading (load full content or nothing)
- No relationship tracking (orphaned memories)
- No session tracking (where did this come from?)

---

## Layer 2: OpenViking Hierarchical Patterns

### The Paradigm Shift: From Tags to URIs

**Current (Flat):**
```
memory_id: "abc123"
tags: ["#decision", "#architecture", "#important"]
metadata: {"domain": "performance", "impact": "high"}
```

**With OpenViking (Hierarchical):**
```
uri: "viking://user/memories/architecture/caching-strategy.md"
parent_uri: "viking://user/memories/architecture"
abstract: "Cache warm-up reduces P99 latency 40%" (L0, ~100 tokens)
overview: "Strategy: pre-warm caches on startup..." (L1, ~2k tokens)
content: "Full implementation details..." (L2, variable)
```

### Benefits

| Aspect | Before | After |
|--------|--------|-------|
| **Organization** | Tags in JSONB | Filesystem-like structure |
| **Context Loading** | Load all (2k tokens) | Load L0 (100 tokens) + L1 as needed |
| **Navigation** | Keyword search | Directory browsing + search |
| **Relationships** | Manual tag matching | Structural proximity (same parent = related) |
| **Token Cost** | 2,000 per memory | 100-200 for relevance check |

### Schema Enhancement

```sql
-- Add hierarchical columns
ALTER TABLE memories ADD COLUMN uri TEXT UNIQUE;
ALTER TABLE memories ADD COLUMN parent_uri TEXT;

-- Add tiered content columns
ALTER TABLE memories ADD COLUMN abstract TEXT;        -- L0: 1-sentence summary
ALTER TABLE memories ADD COLUMN overview TEXT;        -- L1: structured overview
-- content column is L2 (already exists)

-- Add session tracking
ALTER TABLE memories ADD COLUMN session_id UUID;
ALTER TABLE memories ADD COLUMN extracted_at TIMESTAMP;
```

### Directory Recursive Retrieval

Instead of flat vector search:

```sql
-- Search within a directory + recursive subdirectories
CREATE FUNCTION recursive_search(
    query TEXT,
    start_uri TEXT DEFAULT 'viking://',
    max_depth INT DEFAULT 3
) RETURNS TABLE (
    memory_id UUID,
    uri TEXT,
    relevance_score FLOAT,
    depth INT,
    path TEXT[]
);

-- Usage: Find all architecture decisions and their dependencies
SELECT * FROM recursive_search(
    'cache optimization',
    'viking://user/memories/architecture',
    depth := 2
);
```

### Tiered Loading

```sql
-- Load only abstract for initial relevance check
SELECT uri, abstract, relevance_score 
FROM memories 
WHERE embedding <-> query_embedding < 0.2
LIMIT 10;

-- Load overview for planning phase
SELECT uri, overview, session_context
FROM memories
WHERE uri = 'viking://user/memories/architecture/caching'
LIMIT 1;

-- Load full content for implementation
SELECT uri, content, metadata
FROM memories
WHERE uri = 'viking://user/memories/architecture/caching'
LIMIT 1;
```

### Session Memory Loop (Auto-Evolution)

```sql
-- Track conversation sessions
CREATE TABLE sessions (
    session_id UUID PRIMARY KEY,
    created_at TIMESTAMP,
    message_count INT,
    memory_extracted BOOLEAN DEFAULT FALSE
);

-- Store messages from conversation
CREATE TABLE session_messages (
    id SERIAL,
    session_id UUID REFERENCES sessions,
    role VARCHAR (user/assistant),
    content TEXT,
    captured_at TIMESTAMP
);

-- Auto-extract memories at session end
CREATE FUNCTION extract_memories_from_session(
    session_id UUID
) RETURNS TABLE (
    memory_id UUID,
    uri TEXT,
    memory_type VARCHAR
);
```

**Result**: Memories self-evolve without manual curation.

---

## Layer 3: Apache AGE Graph Relationships

### What Apache AGE Adds

Apache AGE is a PostgreSQL extension that adds graph database capabilities *inside PostgreSQL*:

```sql
-- Install as extension (no new infrastructure)
CREATE EXTENSION age;

-- Create property graph
CREATE PROPERTY GRAPH memory_graph;

-- Define nodes and edges declaratively
CREATE (m:Memory {id: 'uuid', title: 'string'});
CREATE (s:Skill {id: 'uuid', name: 'string'});
CREATE (m)-[:USES]->(s);
```

### Node Types

| Node Type | Properties | Examples |
|-----------|-----------|----------|
| **Memory** | id, uri, title, type, priority | Decision, preference, action |
| **Skill** | id, name, category, complexity | TDD, debugging, code-review |
| **Context** | id, name, domain, scope | project-specific, pattern |
| **Session** | id, created_at, message_count | conversation session |
| **Pattern** | id, name, framework | fabric-pattern, design-pattern |
| **Domain** | id, name | architecture, testing, devops |

### Relationship Types

| Relation | Direction | Meaning |
|----------|-----------|---------|
| **USES** | Memory → Skill | This memory uses this skill |
| **BASED_ON** | Memory → Memory | Founded on this earlier memory |
| **CONTRADICTS** | Memory → Memory | Conflicts with this approach |
| **REFERENCES** | Memory → Memory | Cites or links to |
| **DEPENDS_ON** | Skill → Skill | Requires this prerequisite |
| **IN_CONTEXT** | Memory → Context | Applicable in this context |
| **EVOLVES_INTO** | Memory → Memory | Evolved to this version |
| **APPLIES_TO** | Pattern → Domain | Pattern applies to this domain |
| **EXTRACTED_FROM** | Memory → Session | Auto-extracted from conversation |

### What Graph Queries Enable

#### 1. **Memory Semantic Linking**

```sql
-- Find all memories that led to this decision
MATCH path = (foundation:Memory)-[:BASED_ON*1..5]->(latest)
WHERE latest.uri = 'viking://user/memories/decisions/caching-strategy'
RETURN path, length(path) as evolution_depth
ORDER BY evolution_depth DESC;

-- Result: See the full chain of reasoning
foundation_v1 → foundation_v2 → foundation_v3 → latest
(Shows how the decision evolved)
```

#### 2. **Skill Dependency Chains**

```sql
-- "What do I need to master before systematic debugging?"
MATCH (skill:Skill)<-[:DEPENDS_ON*1..5]-(prereq:Skill)
WHERE skill.name = 'systematic-debugging'
RETURN prereq, distance
ORDER BY distance;

-- Result: Prerequisites ordered by level
L0: print debugging
L1: reading stack traces
L2: mental models
L3: systematic debugging
```

#### 3. **Context-Aware Memory Retrieval**

```sql
-- "What memories apply to my current project?"
MATCH (project:Context)<-[:IN_CONTEXT]-(memory:Memory)
       -[:USES]->(skill:Skill)
WHERE project.name = 'my-app'
RETURN memory, skill, COUNT(*) as usage_count
ORDER BY usage_count DESC;

-- Result: Memories prioritized by relevance to project
```

#### 4. **Impact Analysis**

```sql
-- "If I change this preference, what else is affected?"
MATCH (pref:Memory)<-[:BASED_ON*1..3]-(dependent)
WHERE pref.uri = 'viking://user/memories/preferences/testing-approach'
RETURN dependent, COUNT(*) as downstream_impact
ORDER BY downstream_impact DESC;

-- Result: Ripple effects of changing this preference
```

#### 5. **Evolution Tracking**

```sql
-- "How did my understanding evolve?"
MATCH path = (old:Memory)-[:EVOLVES_INTO*]->(new:Memory)
       -[:CONTRADICTS]-(reason)
WHERE new.uri = 'viking://user/memories/preferences/monolith-vs-microservices'
RETURN old, new, reason, length(path);

-- Result: See why and how perspective changed
```

#### 6. **Pattern Discovery**

```sql
-- "What patterns do I use together?"
MATCH (m1:Memory)-[:USES]->(skill1:Skill),
       (m1)-[:USES]->(skill2:Skill),
       (m2:Memory)-[:USES]->(skill1),
       (m2)-[:USES]->(skill2)
WHERE m1 <> m2
RETURN skill1, skill2, COUNT(*) as co_occurrence
ORDER BY co_occurrence DESC;

-- Result: Discover implicit skill combinations
```

---

## Integration: How the Three Layers Work Together

### Agent Query Flow

```
User: "How should I approach TDD in this project?"
                    ↓
┌─ Layer 1 (Relational): Vector search
│  Find top-10 memories about TDD
│  (~100 tokens from embeddings)
                    ↓
├─ Layer 2 (Hierarchical): Tiered loading
│  Load abstracts (L0) for relevance check
│  Load overview (L1) for decision-making
│  (~200 tokens total)
                    ↓
└─ Layer 3 (Graph): Relationship analysis
   MATCH: Memory -[:IN_CONTEXT]-> project
   MATCH: Memory -[:USES]-> skill
   MATCH: Memory -[:EVOLVED_INTO]-> latest
   (~150 tokens for context)

Total context: ~450 tokens (vs 2,000+ with flat approach)
Quality: 10x higher (structured + relational + hierarchical)
```

### Example: Complete Memory Lifecycle

```sql
-- 1. Session starts
INSERT INTO sessions (session_id, created_at)
VALUES ('sess-123', now());

-- 2. Conversation happens
INSERT INTO session_messages (session_id, role, content)
VALUES 
  ('sess-123', 'user', 'How do I structure large codebases?'),
  ('sess-123', 'assistant', 'Consider monolith vs microservices...');

-- 3. At session end, extract memory
INSERT INTO memories (
    memory_id, session_id, uri, content, 
    abstract, overview, memory_type, extracted_at
)
SELECT 
    gen_random_uuid(),
    'sess-123',
    'viking://user/memories/architecture/monolith-pros-cons',
    full_extraction,
    one_sentence_summary,
    structured_overview,
    'decision',
    now()
FROM extract_memories_from_session('sess-123');

-- 4. Auto-link relationships
INSERT INTO age.memory_graph
MATCH (extracted:Memory),
      (related:Memory)
WHERE extracted.session_id = 'sess-123'
  AND related.memory_type IN ('decision', 'preference')
  AND similarity(extracted.embedding, related.embedding) > 0.8
CREATE (extracted)-[:BASED_ON]->(related);

-- 5. Next time this decision appears:
-- - Graph queries find BASED_ON chain
-- - Hierarchical URIs provide context
-- - Tiered loading saves tokens
-- - Previous session is remembered
```

---

## Implementation Roadmap

### Phase 1: Schema Enhancement (Week 1)

**Goal:** Add hierarchical structure to existing PostgreSQL

```sql
-- Add OpenViking columns
ALTER TABLE memories ADD COLUMN uri TEXT UNIQUE;
ALTER TABLE memories ADD COLUMN parent_uri TEXT;
ALTER TABLE memories ADD COLUMN abstract TEXT;
ALTER TABLE memories ADD COLUMN overview TEXT;
ALTER TABLE memories ADD COLUMN session_id UUID;

-- Create session tables
CREATE TABLE sessions (
    session_id UUID PRIMARY KEY,
    created_at TIMESTAMP,
    message_count INT
);

CREATE TABLE session_messages (
    id SERIAL PRIMARY KEY,
    session_id UUID REFERENCES sessions,
    role VARCHAR,
    content TEXT,
    captured_at TIMESTAMP
);
```

**Effort:** Medium (add columns, migrate data)  
**Risk:** Low (backward compatible)

### Phase 2: Tiered Loading Implementation (Week 2-3)

**Goal:** Generate abstracts and overviews for existing memories

```python
# Python script to populate abstracts
for memory in all_memories():
    abstract = llm.extract_essence(memory.content)  # 1 sentence
    overview = llm.create_overview(memory.content)  # 2k tokens
    memory.abstract = abstract
    memory.overview = overview
    memory.save()
```

**Effort:** High (LLM calls for 2,846 memories)  
**Optimization:** Batch process with caching

### Phase 3: Apache AGE Installation (Week 4)

**Goal:** Add graph capabilities to PostgreSQL

```bash
# Install AGE extension
CREATE EXTENSION age;

# Create property graph
CREATE PROPERTY GRAPH memory_graph;

# Define node types
CREATE (:Memory {uri, title, type, priority});
CREATE (:Skill {name, category, complexity});
CREATE (:Context {name, domain});

# Define relationships
CREATE (:Memory)-[:USES]->(:Skill);
CREATE (:Memory)-[:BASED_ON]->(:Memory);
CREATE (:Memory)-[:IN_CONTEXT]->(:Context);
```

**Effort:** Low (AGE is extension, not separate service)  
**Setup time:** 30 minutes

### Phase 4: Relationship Auto-Linking (Week 5)

**Goal:** Extract and create relationships from memories

```sql
-- For each memory, find related memories
INSERT INTO age.memory_graph (source, target, relation)
MATCH (m1:Memory), (m2:Memory)
WHERE m1.memory_id != m2.memory_id
  AND similarity(m1.embedding, m2.embedding) > 0.8
  AND m1.created_at < m2.created_at
CREATE (m2)-[:BASED_ON]->(m1);

-- Link memories to skills
INSERT INTO age.memory_graph
MATCH (m:Memory), (s:Skill)
WHERE m.content CONTAINS s.name
CREATE (m)-[:USES]->(s);
```

**Effort:** Medium (relationship inference logic)

### Phase 5: Tools & CLI (Week 6+)

**Goal:** Create tools for new queries

```python
# New tools for agents
def memgraph_search(query: str, depth: int = 2) -> List[Memory]:
    """Relationship-aware search with path finding"""
    
def memgraph_impact(memory_id: str) -> List[Memory]:
    """Show downstream dependencies"""
    
def memgraph_evolution(memory_id: str) -> List[Tuple[Memory, Reason]]:
    """Show evolution chain with reasons"""
    
def memgraph_pattern(skills: List[str]) -> List[Memory]:
    """Find memories that use these skill combinations"""
```

---

## Benefits Comparison

| Metric | PostgreSQL Only | + OpenViking | + AGE Graph |
|--------|-----------------|--------------|------------|
| **Context Tokens** | 2,000+ | 400-800 | 300-500 |
| **Relationship Queries** | Complex JOINs | Structural paths | Native MATCH |
| **Memory Evolution** | Manual | Auto-extract | Tracked |
| **Skill Dependencies** | None | Inferred | Explicit |
| **Infrastructure** | 1 database | 1 database | 1 database |
| **Query Performance** | Good | Excellent | Excellent |
| **Migration Effort** | N/A | Medium | Low |

---

## Why This Approach Over Alternatives

### vs. Separate Graph Database (Neo4j)

**Graph DB:**
- ✅ Purpose-built for graphs
- ❌ Dual database complexity
- ❌ Transaction coordination overhead
- ❌ New credentials, backups, monitoring

**PostgreSQL + AGE:**
- ✅ Single database (ACID across all layers)
- ✅ Zero new infrastructure
- ✅ Same authentication
- ✅ Simpler backups

### vs. Pure Hierarchical (OpenViking standalone)

**OpenViking:**
- ✅ Excellent hierarchical paradigm
- ❌ Requires separate server
- ❌ Different transaction model

**PostgreSQL + OpenViking patterns:**
- ✅ Hierarchical organization
- ✅ Stays in PostgreSQL
- ✅ Can be extended with graph later

### vs. Flat Relational Only

**Relational:**
- ✅ Good for CRUD
- ✅ Mature ecosystem
- ❌ No hierarchy
- ❌ Token-heavy context
- ❌ No relationship traversal

**Three-layer approach:**
- ✅ CRUD + hierarchy + relationships
- ✅ Optimized for all use cases
- ✅ Self-evolving memory

---

## Next Steps

1. **This Week**: Review schema changes, plan migration
2. **Week 2-3**: Run bulk abstracting/overview generation
3. **Week 4**: Install AGE and create property graph
4. **Week 5**: Auto-link existing memories with relationships
5. **Week 6+**: Build agent tools for graph queries

---

## Conclusion

You don't need to replace PostgreSQL. Instead, **enhance it**:

- **Layer 1** (Relational): Keeps what works
- **Layer 2** (Hierarchical): Adds context structure  
- **Layer 3** (Graph): Adds relationship intelligence

The result: **An AI-native memory system that costs 4x less to use, evolves automatically, and understands context like humans do.**

All in one PostgreSQL database. Zero new infrastructure.

---

## References

- [Apache AGE Documentation](https://age.apache.org/)
- [OpenViking: Context Database for AI Agents](https://github.com/volcengine/OpenViking)
- [PostgreSQL pgvector](https://github.com/pgvector/pgvector)
- [Obra/Superpowers Framework](https://github.com/obra/superpowers)
- [Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric)