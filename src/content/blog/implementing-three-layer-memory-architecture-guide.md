---
pubDatetime: 2026-03-17T00:00:00Z
title: "Implementation Guide: Building the Three-Layer Memory Architecture"
postSlug: "implementing-three-layer-memory-architecture-guide"
description: "Step-by-step technical implementation of PostgreSQL + OpenViking + Apache AGE memory system with code samples, scripts, and deployment instructions"
tags:
  - apache-age
  - code
  - postgresql
  - implementation
  - tutorial
  - openviking
---

## Overview

This guide provides **hands-on implementation details** for building the three-layer memory architecture described in [Part 1](/posts/postgresql-openviking-apache-age-memory-architecture/).

**What you'll build:**
- PostgreSQL schema with hierarchical URIs and tiered content
- Auto-extraction from conversation sessions
- Apache AGE graph for relationship mapping
- Python tools for memory operations
- Migration scripts for existing memories

**Prerequisites:**
- PostgreSQL 15+ with pgvector extension
- Python 3.10+
- Apache AGE extension
- Basic SQL and Python knowledge

---

## Phase 1: Schema Enhancement (Week 1)

### Step 1.1: Install Required Extensions

```sql
-- Connect to your database
\c memory_db

-- Install pgvector (if not already installed)
CREATE EXTENSION IF NOT EXISTS vector;

-- Install Apache AGE
CREATE EXTENSION IF NOT EXISTS age;

-- Verify installations
SELECT * FROM pg_extension WHERE extname IN ('vector', 'age');
```

**Expected output:**
```
  extname  | extversion 
-----------+------------
 vector    | 0.5.0
 age       | 1.4.0
```

### Step 1.2: Add Hierarchical Columns

```sql
-- Add OpenViking-style columns
ALTER TABLE memories 
ADD COLUMN uri TEXT UNIQUE,
ADD COLUMN parent_uri TEXT,
ADD COLUMN abstract TEXT,
ADD COLUMN overview TEXT,
ADD COLUMN session_id UUID,
ADD COLUMN extracted_at TIMESTAMP,
ADD COLUMN is_directory BOOLEAN DEFAULT FALSE;

-- Create indexes for hierarchical queries
CREATE INDEX idx_memories_uri ON memories(uri);
CREATE INDEX idx_memories_parent_uri ON memories(parent_uri);
CREATE INDEX idx_memories_session_id ON memories(session_id);
CREATE INDEX idx_memories_extracted_at ON memories(extracted_at);

-- Create partial index for unindexed memories
CREATE INDEX idx_memories_unextracted 
ON memories(extracted_at) 
WHERE extracted_at IS NULL;
```

### Step 1.3: Create Session Tracking Tables

```sql
-- Sessions table
CREATE TABLE sessions (
    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    ended_at TIMESTAMP,
    message_count INT DEFAULT 0,
    memory_extracted BOOLEAN DEFAULT FALSE,
    metadata JSONB DEFAULT '{}'
);

-- Session messages table
CREATE TABLE session_messages (
    id BIGSERIAL PRIMARY KEY,
    session_id UUID NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content TEXT NOT NULL,
    captured_at TIMESTAMP NOT NULL DEFAULT now(),
    metadata JSONB DEFAULT '{}'
);

-- Index for fast session queries
CREATE INDEX idx_session_messages_session_id 
ON session_messages(session_id, captured_at DESC);
```

### Step 1.4: Create URI Generation Function

```sql
-- Function to generate hierarchical URIs
CREATE OR REPLACE FUNCTION generate_memory_uri(
    memory_type VARCHAR,
    scope VARCHAR DEFAULT 'user',
    custom_path VARCHAR DEFAULT NULL
) RETURNS TEXT AS $$
DECLARE
    base_uri TEXT;
    timestamp_part TEXT;
    random_suffix TEXT;
BEGIN
    -- Build base URI
    base_uri := CASE scope
        WHEN 'project' THEN 'viking://project'
        ELSE 'viking://user'
    END;
    
    -- Add memory type directory
    base_uri := base_uri || '/memories/' || memory_type || 's';
    
    -- Generate path
    IF custom_path IS NOT NULL THEN
        -- Use custom path (e.g., "architecture/caching-strategy")
        base_uri := base_uri || '/' || custom_path || '.md';
    ELSE
        -- Auto-generate from timestamp
        timestamp_part := to_char(now(), 'YYYY-MM-DD-HH24-MI-SS');
        random_suffix := substr(md5(random()::text), 1, 8);
        base_uri := base_uri || '/' || timestamp_part || '-' || random_suffix || '.md';
    END IF;
    
    RETURN base_uri;
END;
$$ LANGUAGE plpgsql;

-- Test the function
SELECT generate_memory_uri('decision', 'user', 'architecture/caching-strategy');
-- Result: viking://user/memories/decisions/architecture/caching-strategy.md

SELECT generate_memory_uri('action', 'project');
-- Result: viking://project/memories/actions/2026-03-17-14-30-45-a3b2c1d4.md
```

---

## Phase 2: Tiered Content Generation (Week 2-3)

### Step 2.1: Create Content Generation Function

```python
#!/usr/bin/env python3
"""
generate_tiers.py - Generate L0 (abstract) and L1 (overview) from full content.

Usage:
    python3 generate_tiers.py --memory-id <uuid>
    python3 generate_tiers.py --all-unprocessed
    python3 generate_tiers.py --batch-size 100
"""

import os
import sys
import argparse
import psycopg2
from psycopg2.extras import RealDictCursor
import openai
from typing import Dict, List, Optional
import json

# Configuration
PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "memory_user",
    "password": os.getenv("PG_PASSWORD"),
    "dbname": "memory_db",
}

openai.api_key = os.getenv("OPENAI_API_KEY")

# Alternative: Use your local LLM
ZAI_API_URL = "http://localhost:8002/v1/chat/completions"


def get_connection():
    return psycopg2.connect(**PG_CONFIG)


def generate_abstract(content: str, llm_client=None) -> str:
    """
    Generate L0 abstract: 1-sentence summary (~100 tokens)
    """
    prompt = f"""Summarize this memory in ONE concise sentence (max 30 words):

{content[:2000]}

Abstract:"""

    if llm_client:
        # Use local LLM
        response = llm_client.chat.completions.create(
            model="local-model",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        return response.choices[0].message.content.strip()
    else:
        # Use OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        return response.choices[0].message.content.strip()


def generate_overview(content: str, memory_type: str, llm_client=None) -> str:
    """
    Generate L1 overview: Structured summary (~2k tokens)
    """
    prompt = f"""Create a structured overview of this {memory_type} memory.

Format:
## Summary
[2-3 sentence overview]

## Key Points
- [Point 1]
- [Point 2]
- [Point 3]

## Context
[When/where this applies]

## Impact
[Consequences or implications]

Content:
{content[:6000]}

Overview:"""

    if llm_client:
        response = llm_client.chat.completions.create(
            model="local-model",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    else:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()


def generate_tiers_for_memory(memory_id: str) -> Dict[str, str]:
    """
    Generate abstract and overview for a single memory.
    Returns: {"abstract": str, "overview": str}
    """
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Fetch memory
    cur.execute(
        "SELECT content, memory_type FROM memories WHERE memory_id = %s",
        (memory_id,)
    )
    memory = cur.fetchone()
    
    if not memory:
        raise ValueError(f"Memory not found: {memory_id}")
    
    # Generate tiers
    abstract = generate_abstract(memory['content'])
    overview = generate_overview(memory['content'], memory['memory_type'])
    
    # Update memory
    cur.execute(
        """
        UPDATE memories 
        SET abstract = %s, overview = %s, updated_at = now()
        WHERE memory_id = %s
        """,
        (abstract, overview, memory_id)
    )
    conn.commit()
    
    cur.close()
    conn.close()
    
    return {"abstract": abstract, "overview": overview}


def process_unprocessed_memories(batch_size: int = 100) -> int:
    """
    Process all memories without abstracts/overviews.
    Returns: Number of memories processed
    """
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Fetch unprocessed memories
    cur.execute(
        """
        SELECT memory_id FROM memories 
        WHERE abstract IS NULL OR overview IS NULL
        ORDER BY created_at DESC
        LIMIT %s
        """,
        (batch_size,)
    )
    memories = cur.fetchall()
    
    processed = 0
    for memory in memories:
        try:
            generate_tiers_for_memory(memory['memory_id'])
            processed += 1
            print(f"✓ Processed {memory['memory_id']} ({processed}/{len(memories)})")
        except Exception as e:
            print(f"✗ Failed {memory['memory_id']}: {e}")
    
    cur.close()
    conn.close()
    
    return processed


def main():
    parser = argparse.ArgumentParser(description="Generate tiered content for memories")
    parser.add_argument("--memory-id", help="Process specific memory")
    parser.add_argument("--all-unprocessed", action="store_true", help="Process all unprocessed")
    parser.add_argument("--batch-size", type=int, default=100, help="Batch size for --all-unprocessed")
    
    args = parser.parse_args()
    
    if args.memory_id:
        result = generate_tiers_for_memory(args.memory_id)
        print(json.dumps(result, indent=2))
    elif args.all_unprocessed:
        processed = process_unprocessed_memories(args.batch_size)
        print(f"\nProcessed {processed} memories")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

### Step 2.2: Run Bulk Generation

```bash
# Set environment variables
export PG_PASSWORD="your_password"
export OPENAI_API_KEY="sk-..."  # or use local LLM

# Generate for all unprocessed memories
python3 generate_tiers.py --all-unprocessed --batch-size 50

# Or process specific memory
python3 generate_tiers.py --memory-id "abc123-def456-..."
```

**Expected output:**
```
✓ Processed abc123-def456-... (1/50)
✓ Processed def456-ghi789-... (2/50)
...
✓ Processed xyz789-abc123-... (50/50)

Processed 50 memories
```

---

## Phase 3: Apache AGE Graph Setup (Week 4)

### Step 3.1: Create Property Graph

```sql
-- Create the memory graph
SELECT create_graph('memory_graph');

-- Verify graph creation
SELECT * FROM cypher('memory_graph', $$
    RETURN 'Graph created successfully'
$$) as (result text);
```

### Step 3.2: Define Node Types

```sql
-- Create Memory nodes
SELECT * FROM cypher('memory_graph', $$
    CREATE CONSTRAINT memory_id_unique IF NOT EXISTS
    FOR (m:Memory) REQUIRE m.id IS UNIQUE
$$) as (result text);

-- Create Skill nodes
SELECT * FROM cypher('memory_graph', $$
    CREATE CONSTRAINT skill_id_unique IF NOT EXISTS
    FOR (s:Skill) REQUIRE s.id IS UNIQUE
$$) as (result text);

-- Create Context nodes
SELECT * FROM cypher('memory_graph', $$
    CREATE CONSTRAINT context_id_unique IF NOT EXISTS
    FOR (c:Context) REQUIRE c.id IS UNIQUE
$$) as (result text);
```

### Step 3.3: Populate Nodes from Existing Data

```sql
-- Populate Memory nodes
INSERT INTO cypher('memory_graph', $$
    MATCH (m:Memory)
    RETURN m
$$)
SELECT 
    json_build_object(
        'id', memory_id,
        'uri', uri,
        'title', substring(content, 1, 100),
        'type', memory_type,
        'priority', priority
    )::text
FROM memories
WHERE uri IS NOT NULL;

-- Populate Skill nodes (from your skills directory)
INSERT INTO cypher('memory_graph', $$
    CREATE (s:Skill $props)
    RETURN s
$$)
SELECT json_build_object(
    'id', skill_id,
    'name', skill_name,
    'category', category
)::text as props
FROM skills;  -- Adjust to your skills table
```

### Step 3.4: Create Relationship Functions

```python
#!/usr/bin/env python3
"""
create_relationships.py - Auto-create graph relationships from memory content.

Usage:
    python3 create_relationships.py --session-id <uuid>
    python3 create_relationships.py --all-memories
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
import re

PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "memory_user",
    "password": os.getenv("PG_PASSWORD"),
    "dbname": "memory_db",
}


def create_based_on_relationship(memory_id: str, related_memory_id: str, strength: float = 0.8):
    """
    Create BASED_ON relationship between two memories.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor()
    
    # Use AGE cypher query
    cur.execute("""
        SELECT * FROM cypher('memory_graph', $$
            MATCH (m1:Memory {id: '%s'}), (m2:Memory {id: '%s'})
            CREATE (m2)-[:BASED_ON {strength: %f}]->(m1)
            RETURN m1, m2
        $$) as (m1 text, m2 text)
    """ % (related_memory_id, memory_id, strength))
    
    conn.commit()
    cur.close()
    conn.close()


def create_uses_skill_relationship(memory_id: str, skill_name: str):
    """
    Create USES relationship between memory and skill.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor()
    
    cur.execute("""
        SELECT * FROM cypher('memory_graph', $$
            MATCH (m:Memory {id: '%s'}), (s:Skill {name: '%s'})
            CREATE (m)-[:USES]->(s)
            RETURN m, s
        $$) as (m text, s text)
    """ % (memory_id, skill_name))
    
    conn.commit()
    cur.close()
    conn.close()


def infer_relationships_from_content(memory_id: str, content: str, memory_type: str):
    """
    Analyze content and create inferred relationships.
    """
    # Pattern matching for skill references
    skill_patterns = {
        r'\bTDD\b': 'test-driven-development',
        r'\bdebugging\b': 'systematic-debugging',
        r'\bcode review\b': 'code-review',
        r'\brefactor': 'refactoring',
        r'\bbrainstorm': 'brainstorming',
    }
    
    # Find skill references
    for pattern, skill_name in skill_patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            try:
                create_uses_skill_relationship(memory_id, skill_name)
                print(f"  → Uses skill: {skill_name}")
            except Exception as e:
                print(f"  ✗ Failed to link skill {skill_name}: {e}")


def process_session_memories(session_id: str):
    """
    Process all memories from a session and create relationships.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Fetch session memories
    cur.execute("""
        SELECT memory_id, content, memory_type
        FROM memories
        WHERE session_id = %s
        ORDER BY created_at
    """, (session_id,))
    
    memories = cur.fetchall()
    
    for i, memory in enumerate(memories):
        print(f"Processing {memory['memory_id']} ({i+1}/{len(memories)})")
        
        # Create relationships based on content analysis
        infer_relationships_from_content(
            memory['memory_id'],
            memory['content'],
            memory['memory_type']
        )
        
        # Link to previous memory in session (temporal chain)
        if i > 0:
            prev_memory_id = memories[i-1]['memory_id']
            create_based_on_relationship(
                memory['memory_id'],
                prev_memory_id,
                strength=0.7
            )
            print(f"  → Based on: {prev_memory_id}")
    
    cur.close()
    conn.close()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-id", help="Process specific session")
    parser.add_argument("--all-memories", action="store_true", help="Process all memories")
    
    args = parser.parse_args()
    
    if args.session_id:
        process_session_memories(args.session_id)
    elif args.all_memories:
        # Process all sessions
        conn = psycopg2.connect(**PG_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT session_id FROM memories WHERE session_id IS NOT NULL")
        sessions = cur.fetchall()
        cur.close()
        conn.close()
        
        for session_id in sessions:
            print(f"\n=== Processing session {session_id[0]} ===")
            process_session_memories(session_id[0])


if __name__ == "__main__":
    main()
```

---

## Phase 4: Session Memory Extraction (Week 5)

### Step 4.1: Create Extraction Function

```sql
-- Function to extract memories from session
CREATE OR REPLACE FUNCTION extract_session_memories(
    p_session_id UUID
) RETURNS TABLE (
    memory_id UUID,
    memory_type VARCHAR,
    uri TEXT
) AS $$
DECLARE
    session_content TEXT;
    extracted_memories JSONB;
BEGIN
    -- Aggregate session content
    SELECT string_agg(content, E'\n\n' ORDER BY captured_at)
    INTO session_content
    FROM session_messages
    WHERE session_id = p_session_id;
    
    -- Call LLM to extract memories (pseudo-code)
    -- In practice, you'd call Python/external service
    extracted_memories := llm_extract_memories(session_content);
    
    -- Insert extracted memories
    INSERT INTO memories (
        memory_id, content, abstract, overview, 
        memory_type, uri, session_id, extracted_at
    )
    SELECT 
        gen_random_uuid(),
        mem->>'content',
        mem->>'abstract',
        mem->>'overview',
        mem->>'type',
        generate_memory_uri(mem->>'type', 'user', mem->>'path'),
        p_session_id,
        now()
    FROM jsonb_array_elements(extracted_memories) mem
    RETURNING memories.memory_id, memories.memory_type, memories.uri;
END;
$$ LANGUAGE plpgsql;
```

### Step 4.2: Create Python Extraction Service

```python
#!/usr/bin/env python3
"""
session_extractor.py - Extract memories from conversation sessions.

Usage:
    python3 session_extractor.py --session-id <uuid>
    python3 session_extractor.py --daemon  # Run as background service
"""

import os
import sys
import json
import time
import psycopg2
from psycopg2.extras import RealDictCursor
import openai
from typing import List, Dict

PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "memory_user",
    "password": os.getenv("PG_PASSWORD"),
    "dbname": "memory_db",
}

openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_memories_from_session(session_id: str) -> List[Dict]:
    """
    Extract structured memories from session messages.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Fetch session messages
    cur.execute("""
        SELECT role, content, captured_at
        FROM session_messages
        WHERE session_id = %s
        ORDER BY captured_at
    """, (session_id,))
    
    messages = cur.fetchall()
    
    if not messages:
        return []
    
    # Format conversation
    conversation = "\n\n".join([
        f"{msg['role'].upper()}: {msg['content']}"
        for msg in messages
    ])
    
    # Call LLM to extract memories
    prompt = f"""Analyze this conversation and extract structured memories.

For each memory, provide:
- type: decision, action, preference, or insight
- path: hierarchical path (e.g., "architecture/caching-strategy")
- abstract: 1-sentence summary (max 30 words)
- overview: structured summary (key points, context, impact)
- content: full memory content (2-5 sentences)

Conversation:
{conversation[:10000]}

Return JSON array:
[
  {{
    "type": "decision",
    "path": "architecture/caching-strategy",
    "abstract": "...",
    "overview": "...",
    "content": "..."
  }},
  ...
]"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    memories = json.loads(response.choices[0].message.content)
    
    # Insert into database
    for memory in memories.get('memories', []):
        cur.execute("""
            INSERT INTO memories (
                memory_id, content, abstract, overview,
                memory_type, uri, session_id, extracted_at
            ) VALUES (
                gen_random_uuid(), %s, %s, %s, %s,
                generate_memory_uri(%s, 'user', %s),
                %s, now()
            )
            RETURNING memory_id, uri
        """, (
            memory['content'],
            memory['abstract'],
            memory['overview'],
            memory['type'],
            memory['type'],
            memory['path'],
            session_id
        ))
        
        result = cur.fetchone()
        memory['memory_id'] = str(result['memory_id'])
        memory['uri'] = result['uri']
    
    # Mark session as extracted
    cur.execute("""
        UPDATE sessions 
        SET memory_extracted = true, ended_at = now()
        WHERE session_id = %s
    """, (session_id,))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return memories.get('memories', [])


def run_daemon():
    """
    Run as background service, checking for new sessions to extract.
    """
    print("Starting session extraction daemon...")
    
    while True:
        try:
            conn = psycopg2.connect(**PG_CONFIG)
            cur = conn.cursor()
            
            # Find unprocessed sessions
            cur.execute("""
                SELECT session_id
                FROM sessions
                WHERE memory_extracted = false
                  AND ended_at IS NOT NULL
                  AND ended_at < now() - interval '5 minutes'
                LIMIT 10
            """)
            
            sessions = cur.fetchall()
            cur.close()
            conn.close()
            
            for session_id in sessions:
                print(f"Processing session {session_id[0]}")
                memories = extract_memories_from_session(str(session_id[0]))
                print(f"  Extracted {len(memories)} memories")
                
                # Create graph relationships
                for memory in memories:
                    # Relationship creation logic here
                    pass
            
            # Sleep before next check
            time.sleep(60)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-id", help="Extract specific session")
    parser.add_argument("--daemon", action="store_true", help="Run as daemon")
    
    args = parser.parse_args()
    
    if args.session_id:
        memories = extract_memories_from_session(args.session_id)
        print(f"Extracted {len(memories)} memories:")
        for mem in memories:
            print(f"  - [{mem['type']}] {mem['uri']}")
    elif args.daemon:
        run_daemon()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

### Step 4.3: Run Extraction Daemon

```bash
# Extract specific session
python3 session_extractor.py --session-id "abc123-def456-..."

# Run as background daemon
nohup python3 session_extractor.py --daemon > /var/log/memory-extractor.log 2>&1 &
```

---

## Phase 5: Memory Query Tools (Week 6+)

### Step 5.1: Hierarchical Query Tool

```python
#!/usr/bin/env python3
"""
memory_query.py - Query memories with hierarchical and graph support.

Usage:
    python3 memory_query.py search "cache optimization"
    python3 memory_query.py browse "viking://user/memories/architecture"
    python3 memory_query.py graph "abc123-def456-..." --depth 3
    python3 memory_query.py impact "viking://user/memories/preferences/testing-approach"
"""

import os
import sys
import json
import argparse
import psycopg2
from psycopg2.extras import RealDictCursor

PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "memory_user",
    "password": os.getenv("PG_PASSWORD"),
    "dbname": "memory_db",
}


def hierarchical_search(query: str, tier: str = 'abstract', limit: int = 10):
    """
    Search with tiered loading (L0, L1, L2).
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Select column based on tier
    tier_column = {
        'abstract': 'abstract',
        'overview': 'overview',
        'full': 'content'
    }.get(tier, 'abstract')
    
    cur.execute("""
        SELECT 
            memory_id,
            uri,
            memory_type,
            %s as content,
            created_at
        FROM memories
        WHERE uri IS NOT NULL
          AND to_tsvector('english', %s) @@ plainto_tsquery('english', %s)
        ORDER BY ts_rank(to_tsvector('english', %s), plainto_tsquery('english', %s)) DESC
        LIMIT %s
    """, (tier_column, tier_column, query, tier_column, query, limit))
    
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    return results


def browse_directory(uri: str, recursive: bool = False):
    """
    Browse memories in a directory structure.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    if recursive:
        # Find all descendants
        cur.execute("""
            SELECT memory_id, uri, abstract, memory_type
            FROM memories
            WHERE uri LIKE %s
            ORDER BY uri
        """, (uri + '%',))
    else:
        # Find immediate children
        cur.execute("""
            SELECT memory_id, uri, abstract, memory_type
            FROM memories
            WHERE parent_uri = %s
               OR uri LIKE %s
            ORDER BY uri
        """, (uri, uri + '/_%'))
    
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    return results


def graph_query(memory_id: str, depth: int = 2):
    """
    Find related memories via graph relationships.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute("""
        SELECT * FROM cypher('memory_graph', $$
            MATCH path = (center:Memory {id: '%s'})-[*1..%d]-(related:Memory)
            RETURN 
                related.id as memory_id,
                related.uri as uri,
                type(relationships(path)[1]) as relationship,
                length(path) as distance
            ORDER BY distance, related.priority DESC
        $$) as (memory_id text, uri text, relationship text, distance int)
    """ % (memory_id, depth))
    
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    return results


def impact_analysis(uri: str):
    """
    Find all memories that depend on this memory.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute("""
        SELECT * FROM cypher('memory_graph', $$
            MATCH (target:Memory {uri: '%s'})<-[:BASED_ON*1..5]-(dependent:Memory)
            RETURN 
                dependent.id as memory_id,
                dependent.uri as uri,
                dependent.title as title,
                length(shortestPath((target)-[*]-(dependent))) as distance
            ORDER BY distance
        $$) as (memory_id text, uri text, title text, distance int)
    """ % (uri,))
    
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Memory query tools")
    parser.add_argument("command", choices=['search', 'browse', 'graph', 'impact'])
    parser.add_argument("query", help="Search query or URI")
    parser.add_argument("--tier", choices=['abstract', 'overview', 'full'], default='abstract')
    parser.add_argument("--depth", type=int, default=2, help="Graph traversal depth")
    parser.add_argument("--recursive", action="store_true", help="Browse recursively")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    if args.command == 'search':
        results = hierarchical_search(args.query, args.tier)
    elif args.command == 'browse':
        results = browse_directory(args.query, args.recursive)
    elif args.command == 'graph':
        results = graph_query(args.query, args.depth)
    elif args.command == 'impact':
        results = impact_analysis(args.query)
    
    if args.json:
        print(json.dumps(results, indent=2, default=str))
    else:
        for r in results:
            print(f"\n{r.get('uri', r.get('memory_id'))}")
            if 'abstract' in r:
                print(f"  {r['abstract'][:100]}...")
            if 'relationship' in r:
                print(f"  → {r['relationship']} (distance: {r['distance']})")


if __name__ == "__main__":
    main()
```

### Step 5.2: Usage Examples

```bash
# Search with tiered loading (L0 = abstract only)
python3 memory_query.py search "cache optimization" --tier abstract

# Search with full content (L2)
python3 memory_query.py search "microservices" --tier full

# Browse directory structure
python3 memory_query.py browse "viking://user/memories/architecture"

# Browse recursively
python3 memory_query.py browse "viking://user/memories" --recursive

# Graph query: find related memories
python3 memory_query.py graph "abc123-def456-..." --depth 3

# Impact analysis: what depends on this?
python3 memory_query.py impact "viking://user/memories/preferences/testing-approach"
```

---

## Migration Script: Existing Memories

```python
#!/usr/bin/env python3
"""
migrate_to_three_layer.py - Migrate existing flat memories to three-layer architecture.

Usage:
    python3 migrate_to_three_layer.py --dry-run  # Preview changes
    python3 migrate_to_three_layer.py --execute  # Apply changes
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor

PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "memory_user",
    "password": os.getenv("PG_PASSWORD"),
    "dbname": "memory_db",
}


def migrate_memories(dry_run: bool = True):
    """
    Add URIs and parent URIs to existing memories.
    """
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Fetch memories without URIs
    cur.execute("""
        SELECT memory_id, memory_type, scope, created_at
        FROM memories
        WHERE uri IS NULL
        ORDER BY created_at
    """)
    
    memories = cur.fetchall()
    print(f"Found {len(memories)} memories to migrate")
    
    for i, memory in enumerate(memories):
        # Generate URI
        date_part = memory['created_at'].strftime('%Y-%m-%d')
        random_suffix = memory['memory_id'][:8]
        
        uri = f"viking://{memory['scope']}/memories/{memory['memory_type']}s/{date_part}-{random_suffix}.md"
        
        # Determine parent URI
        parent_uri = f"viking://{memory['scope']}/memories/{memory['memory_type']}s"
        
        if dry_run:
            print(f"[{i+1}/{len(memories)}] Would set: {uri}")
        else:
            cur.execute("""
                UPDATE memories
                SET uri = %s, parent_uri = %s, updated_at = now()
                WHERE memory_id = %s
            """, (uri, parent_uri, memory['memory_id']))
            
            if (i + 1) % 100 == 0:
                conn.commit()
                print(f"[{i+1}/{len(memories)}] Committed batch")
    
    if not dry_run:
        conn.commit()
        print(f"✓ Migrated {len(memories)} memories")
    
    cur.close()
    conn.close()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--execute", action="store_true", help="Apply changes")
    
    args = parser.parse_args()
    
    if args.execute:
        migrate_memories(dry_run=False)
    elif args.dry_run:
        migrate_memories(dry_run=True)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

---

## Monitoring & Maintenance

### Database Health Check

```sql
-- Check memory distribution
SELECT 
    memory_type,
    scope,
    COUNT(*) as total,
    COUNT(abstract) as has_abstract,
    COUNT(overview) as has_overview,
    COUNT(uri) as has_uri
FROM memories
GROUP BY memory_type, scope
ORDER BY total DESC;

-- Check session extraction status
SELECT 
    COUNT(*) FILTER (WHERE memory_extracted) as extracted,
    COUNT(*) FILTER (WHERE NOT memory_extracted) as pending
FROM sessions;

-- Check graph relationships
SELECT * FROM cypher('memory_graph', $$
    MATCH ()-[r]->()
    RETURN type(r) as relationship, count(r) as count
    ORDER BY count DESC
$$) as (relationship text, count bigint);
```

### Cleanup Script

```sql
-- Remove orphaned memories (no session and older than 90 days)
DELETE FROM memories
WHERE session_id IS NULL
  AND created_at < now() - interval '90 days'
  AND priority < 5;

-- Vacuum and analyze
VACUUM ANALYZE memories;
VACUUM ANALYZE sessions;
VACUUM ANALYZE session_messages;
```

---

## Summary

You've now implemented:

| Component | Status | Files Created |
|-----------|--------|---------------|
| **Schema Enhancement** | ✅ Complete | SQL migrations |
| **Tiered Content** | ✅ Complete | `generate_tiers.py` |
| **Apache AGE Graph** | ✅ Complete | Graph setup scripts |
| **Session Extraction** | ✅ Complete | `session_extractor.py` |
| **Query Tools** | ✅ Complete | `memory_query.py` |
| **Migration Scripts** | ✅ Complete | `migrate_to_three_layer.py` |

### Next Steps

1. **Week 7**: Integrate with your agent (Superpowers skills)
2. **Week 8**: Add visualization tools (graph browser)
3. **Week 9**: Performance tuning (indexes, caching)
4. **Week 10+**: Advanced features (pattern discovery, auto-tagging)

### Troubleshooting

**Problem:** Apache AGE not available
```bash
# Install AGE extension
sudo apt-get install postgresql-15-age
# Or compile from source
git clone https://github.com/apache/age
cd age && make install
```

**Problem:** Slow graph queries
```sql
-- Add graph indexes
CREATE INDEX idx_memory_graph_memory_id ON memory_graph USING gin(id);
```

**Problem:** Memory extraction failing
```bash
# Check LLM API connectivity
curl -X POST http://localhost:8002/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "local", "messages": [{"role": "user", "content": "test"}]}'
```

---

## Related Posts

- [Part 1: Architecture Overview](/posts/postgresql-openviking-apache-age-memory-architecture/)
- [Superpowers Framework Integration](#) (coming soon)
- [Graph Visualization Tools](#) (coming soon)

---

## References

- [Apache AGE Documentation](https://age.apache.org/age-manual/master/index.html)
- [PostgreSQL pgvector Guide](https://github.com/pgvector/pgvector)
- [OpenViking Patterns](https://github.com/volcengine/OpenViking)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)