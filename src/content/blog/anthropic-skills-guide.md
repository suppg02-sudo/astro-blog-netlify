---
pubDatetime: 2026-02-01T00:00:00Z
title: "Mastering Anthropic's Skills: Build Custom AI Agents with Progressive Disclosure"
postSlug: "anthropic-skills-guide"
description: "Mastering Anthropic's Skills: Build Custom AI Agents with Progressive Disclosure"
tags:
  - skills
  - openagents
  - ai
---

In the rapidly evolving landscape of AI development, few concepts have emerged as elegantly powerful as Anthropic's skills system. Released relatively recently, skills represent one of the most important advancements in AI agent architecture—and what makes them truly remarkable is their beautiful simplicity. This guide will walk you through how to implement the skills pattern in any custom AI agent, unlocking the power of progressive disclosure for your own projects.

## Understanding the Skills Philosophy

### The Problem with Traditional Approaches

Traditional AI agent architectures suffer from a fundamental flaw: they attempt to equip agents with dozens of capabilities upfront, overwhelming the context window with information that may never be used in a given conversation. Methods like MCP (Model Context Protocol) servers dump all available tools into the agent's context from the start, creating massive overhead and potentially degrading performance.

Anthropic's insight was revolutionary in its simplicity: why give an agent all capabilities when it only needs one or two for any specific task?

### The Solution: Progressive Disclosure

Progressive disclosure is the core concept behind skills. Instead of overwhelming the agent with everything upfront, we allow it to discover and load capabilities only when needed. This approach offers several key benefits:

- **Context Efficiency**: Only relevant information enters the context window
- **Better Performance**: LLMs work with focused, relevant instructions
- **Scalability**: Add dozens of skills without degrading performance
- **Flexibility**: Use any LLM provider, not just Claude
- **Modularity**: Skills are self-contained and easy to maintain

## The Three-Layer Skills Architecture

The skills system works through a three-layer progressive disclosure model:

{{< mermaid >}}
graph TD
    A[Layer 1: Skill Description] -->|When needed| B[Layer 2: skill.md]
    B -->|References| C[Layer 3: Reference Docs]
    A -->|50-100 words| D[System Prompt]
    B -->|300-500 lines| E[Context Window]
    C -->|Specific Details| E
    E --> F[Agent Execution]

    style A fill:#e1f5fe
    style B fill:#b3e5fc
    style C fill:#81d4fa
    style D fill:#4fc3f7
    style E fill:#29b6f6
    style F fill:#0288d1
{{< /mermaid >}}

### Layer 1: Skill Description (YAML Front Matter)

The first layer is a concise 50-100 word description stored in the YAML front matter of each skill file. This description appears in the agent's system prompt and serves as a "catalog" entry that tells the agent what capabilities are available. The agent reads all descriptions at startup, so keeping them concise is critical.

**Best Practices:**
- Length: 50-100 words maximum
- Clear indication of when to use the skill
- Descriptive enough for the agent to understand trigger conditions
- Approximately 5% of the total skill context

Example:
```yaml
---
description: "Process and extract information from PDF documents. Use this skill whenever the user requests PDF analysis, text extraction, or document parsing. Supports form filling, data extraction, and content analysis."
---
```

### Layer 2: skill.md (Main Instructions)

When the agent identifies that a skill is needed based on the description, it loads the `skill.md` file containing comprehensive instructions for using that capability. This is the primary documentation for the skill and should be 300-500 lines long (approximately 30% of total context).

The `skill.md` contains:
- Detailed usage instructions
- Step-by-step procedures
- Tool integration guidance
- Error handling strategies
- Reference to Layer 3 documents

### Layer 3: Reference Documents

The third layer provides additional depth when needed. Skills can reference supplementary documentation, API references, Python scripts, or other supporting materials. The agent only loads these when specifically required, maintaining the progressive disclosure principle.

**Examples:**
- API documentation for external services
- Python scripts for specific operations
- Standard operating procedures
- Domain-specific reference guides

## Building a Custom Agent with Dynamic System Prompts

The key to implementing skills outside the Claude ecosystem is the dynamic system prompt. Instead of a static prompt, we build our system prompt at runtime by collecting skill descriptions and injecting them into our base instructions.

### System Prompt Architecture

```python
@agent.system_prompt
def skills_system_prompt(ctx: RunContext[None]) -> str:
    """Dynamic system prompt that loads skill descriptions."""
    # Base instructions (static)
    base_prompt = """
    You are an AI agent with access to various skills.
    Skills represent specialized capabilities you can load when needed.
    Always check if a skill is relevant before attempting a task.

    Available Skills Metadata:
    {skills_metadata}

    How to Use Skills:
    1. Identify when a skill is relevant to the user's request
    2. Call the load_skill tool with the skill name
    3. Read the skill.md to understand full instructions
    4. Call read_reference if additional documentation is needed
    5. Execute the task using the provided instructions
    """

    # Load skill descriptions dynamically
    skills_metadata = load_skill_descriptions(SKILLS_DIR)

    return base_prompt.format(skills_metadata=skills_metadata)
```

This approach gives us:
- **Static Content**: Base instructions that don't change
- **Dynamic Content**: Skill descriptions loaded at runtime
- **Extensibility**: Add new skills without modifying the agent code
- **Universal Compatibility**: Works with any LLM provider

### The load_skill Tool Pattern

The heart of the skills implementation is a simple but powerful tool pattern:

```python
@tool
def load_skill(skill_name: str) -> str:
    """Load a skill's instructions into context.

    Args:
        skill_name: Name of the skill to load (must match folder name)

    Returns:
        Full content of skill.md with all instructions
    """
    skill_path = Path(SKILLS_DIR) / skill_name / "skill.md"

    if not skill_path.exists():
        raise ValueError(f"Skill '{skill_name}' not found")

    with open(skill_path) as f:
        return f.read()
```

When the agent calls `load_skill`, the tool response becomes part of the conversation context. The agent now has all the detailed instructions it needs to use that capability effectively.

### Supporting Tools

Two additional tools complete the skills implementation:

```python
@tool
def read_reference(skill_name: str, ref_file: str) -> str:
    """Load reference documentation for a skill.

    Args:
        skill_name: Name of the skill
        ref_file: Path to reference file within the skill folder

    Returns:
        Content of the reference document
    """
    ref_path = Path(SKILLS_DIR) / skill_name / "reference" / ref_file

    if not ref_path.exists():
        raise ValueError(f"Reference file not found: {ref_file}")

    with open(ref_path) as f:
        return f.read()

@tool
def list_references(skill_name: str) -> list[str]:
    """List all available reference documents for a skill.

    Args:
        skill_name: Name of the skill

    Returns:
        List of reference file names
    """
    ref_dir = Path(SKILLS_DIR) / skill_name / "reference"

    if not ref_dir.exists():
        return []

    return [f.name for f in ref_dir.iterdir() if f.is_file()]
```

These tools provide unlimited depth for progressive disclosure while keeping the discovery process simple and efficient.

## Skills Directory Structure

Organize your skills following this structure:

```
skills/
├── weather/
│   ├── skill.md
│   ├── reference/
│   │   ├── api_reference.md
│   │   └── location_codes.md
│   └── scripts/
│       └── weather_parser.py
├── recipe_finder/
│   ├── skill.md
│   └── reference/
│       └── recipe_api.md
├── pdf_processing/
│   ├── skill.md
│   ├── reference/
│   │   ├── forms_guide.md
│   │   └── extraction_rules.md
│   └── scripts/
│       └── pdf_parser.py
└── code_review/
    ├── skill.md
    └── reference/
        ├── style_guide.md
        └── common_patterns.md
```

Each skill is self-contained in its own folder, making it easy to add, remove, or modify capabilities independently.

## Building Your Own Skills

### Using Claude Desktop as a Skill Builder

One of the most powerful features of Claude Desktop is the Skill Creator—a skill that helps you build more skills. Here's how to use it:

1. Open Claude Desktop
2. Go to **File > Settings > Capabilities**
3. Scroll down to **Skills**
4. Go to **Example Skills**
5. Toggle on **Skill Creator**

Now you can ask Claude to help you build any skill:

> "Help me build a skill for LinkedIn posting"
> "Create a skill for generating PowerPoint presentations"
> "Build a skill to create standard operating procedures"

Claude will guide you through the process, creating a complete `skill.md` file and any necessary reference documentation. You can then copy these files directly into your custom agent's skills directory.

### Skill Development Best Practices

Based on Anthropic's documentation and real-world implementation:

1. **Description Layer (50-100 words)**:
   - Focus on when to use the skill
   - Be specific about trigger conditions
   - Avoid technical details
   - Keep it discoverable

2. **skill.md Layer (300-500 lines)**:
   - Provide comprehensive step-by-step instructions
   - Include error handling
   - Reference external APIs or tools
   - Include examples of usage
   - Link to reference documents

3. **Reference Layer (as needed)**:
   - API documentation
   - Code samples
   - Configuration guides
   - Domain-specific knowledge
   - Troubleshooting guides

## Real-World Example: Skills in Action

Let's see how skills work in practice with a multi-capability agent:

```python
# User interaction example
user_input = "Help me find a dinner recipe with chicken"

# Agent thought process:
# 1. Recognizes "recipe" and "dinner" as keywords
# 2. Scans skill descriptions in system prompt
# 3. Identifies "recipe_finder" skill as relevant
# 4. Calls load_skill("recipe_finder")
# 5. Reads detailed instructions from skill.md
# 6. Follows instructions to call recipe API
# 7. Returns results to user

# Later in same conversation
user_input = "What's the weather in Tokyo?"

# Agent thought process:
# 1. Recognizes "weather" keyword
# 2. Loads weather skill (different from recipe skill)
# 3. Follows weather-specific instructions
# 4. Makes API call with Tokyo as parameter
# 5. Returns weather data
```

Notice how the agent only loads one or two skills per conversation, regardless of how many dozens are available. This is the power of progressive disclosure in action.

## Evaluation and Testing (Evals)

When you have dozens of skills, how do you ensure your agent uses them correctly? Manual testing becomes impractical, which is where automated evaluation comes in.

### Creating Evaluation Tests

Define test cases in YAML files that specify expected skill usage:

```yaml
evals:
  - name: weather_skill_test
    input: "What's the weather in New York right now?"
    expected_skills:
      - weather

  - name: recipe_finder_test
    input: "Find me a chicken dinner recipe"
    expected_skills:
      - recipe_finder

  - name: pdf_processing_test
    input: "Extract data from this PDF document"
    expected_skills:
      - pdf_processing
```

### Custom Evaluators

Create custom evaluators to verify skill loading:

```python
def skill_usage_evaluator(response, expected_skills):
    """Verify that expected skills were loaded."""
    actual_skills = []
    for tool_call in response.tool_calls:
        if tool_call.tool_name == "load_skill":
            actual_skills.append(tool_call.args["skill_name"])

    return set(actual_skills) == set(expected_skills)
```

### Running Evaluations

Run your entire test suite with a single command:

```bash
python run_evals.py
```

This provides immediate feedback on whether your agent correctly identifies and uses the appropriate skills. Run evals after every change to:
- System prompt
- Skill descriptions
- Tool configurations
- Skill content

## Observability in Production

Evals are great for local testing, but production agents require ongoing monitoring. Logfire provides comprehensive observability for Pydantic AI agents.

### Setting Up Logfire

```python
import logfire

logfire.configure(
    token=os.getenv("LOGFIRE_TOKEN"),
    # Automatically instrument Pydantic AI agents
    instrument_pydantic_ai=True
)

# Now all agent interactions are tracked automatically
```

### What You Can Monitor

Logfire gives you visibility into:

1. **Token Usage and Costs**: Track expenditure across all interactions
2. **Tool Call Patterns**: See which skills are loaded most frequently
3. **Decision Traces**: Understand why agents make specific choices
4. **Error Rates**: Identify problematic skills or configurations
5. **Performance Metrics**: Monitor response times and success rates

### Production Debugging

When users report issues, you can:

- Trace specific user interactions
- Identify which skills were loaded (or should have been)
- See tool parameters and responses
- Understand the agent's decision-making process
- Spot patterns in failures or edge cases

This level of observability is essential for maintaining reliable production systems, especially as your skill ecosystem grows.

## Universal Applicability

Perhaps the most powerful insight from Anthropic's skills system is that it's not tied to the Claude ecosystem at all. The pattern works with:

- **Multiple LLM Providers**: OpenAI, Anthropic, Ollama, OpenRouter
- **Different Frameworks**: LangChain, CrewAI, Phantic AI, or no framework
- **Local AI**: Run locally with complete control
- **Custom Workflows**: Integrate into your existing systems

The core principles are simple enough to implement in any environment, making skills a universal pattern for building powerful, context-efficient AI agents.

## Conclusion: Simplicity as Superpower

Anthropic's skills system demonstrates that the most powerful innovations are often the simplest. By implementing progressive disclosure through a three-layer architecture, we can:

- Give agents dozens of capabilities without overwhelming them
- Use any LLM provider or framework
- Build modular, maintainable skill systems
- Ensure reliability through automated evaluation
- Maintain production observability

The beauty of skills is that you can start simple—just a description and a skill.md—and add reference documents as needed. The system scales naturally from a handful of skills to dozens, with no architectural changes required.

Whether you're building AI agents for personal projects, enterprise applications, or anything in between, the skills pattern provides a proven foundation for creating capable, context-efficient systems.

Start small: implement the basic `load_skill` pattern, create your first few skills, and watch as your agent becomes more capable without becoming more complex. That's the true power of progressive disclosure.

---

**Resources:**
- [Anthropic Skills Best Practices](https://docs.anthropic.com)
- [Pydantic AI Evaluation Framework](https://docs.pydantic-ai.dev)
- [Logfire Observability](https://logfire.pydantic.dev)
- [Skills Template Repository](https://github.com/your-repo/skills-template)