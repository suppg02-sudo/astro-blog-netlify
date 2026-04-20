---
pubDatetime: 2026-02-02T12:01:00Z
title: "Building Custom AI Agents with Skills"
postSlug: "building-custom-ai-agents-with-skills"
description: "Building Custom AI Agents with Skills"
tags:
  - skills
  - openagents
  - ai
---

It hasn't been that long since Anthropic released skills to the world and it is one of the most important advancements in AI recently. And honestly, one of the biggest reasons it is so important is because of how beautifully simple it is—and that is the motto of Anthropic: "Simpler is better."

We see this looking at Claude code as well. I mean, when you get into how skills work and the idea of progressive disclosure that we'll get into, you can't help but thinking to yourself, "Why in the world was skills not commonplace ever since generative AI was a thing?" And people have been building their own version of skills before Anthropic popularized it. It's super easy to incorporate the idea of skills and progressive disclosure into any AI agent or tool that you want. And realize this: We are not limited to Claude's ecosystem to take advantage of skills. Anthropic does get a lot of credit for popularizing the idea, and we'll get into some of their best practices for creating skills as well. But this really is a universal concept.

It's all about strategizing how we can allow our agent to discover context and capabilities as it needs it to be more flexible and context efficient—as opposed to something like an MCP server or super long global rules where you're just dumping a bunch of context into the LLM right away and completely overwhelming it. So, as much as I really appreciate the Anthropic ecosystem like Claude Desktop and Claude Code, we don't always want to be limited to these platforms because a lot of the time you want to build skills into your own workflows or AI agents. You want to use different large language models, maybe even local AI. There's so many reasons to incorporate skills into our own systems and really build it out for all of the concepts from Anthropic's version of skills and we're going to map it into our own AI agent with system prompts and tools we give it.

And it's beautifully simple, right? Simple but powerful. And so this is only going to take like 10 to 15 minutes. And then you'll know after that exactly how to build this kind of thing into your own systems. And I've got a template for you of course as well.

## Three Things I Want to Cover

So, there's three things I want to cover with you in the next 15 minutes. It's going to be super value packed. So, first we need to get into at a high level how skills work and why they're so powerful, even if you've used them before. Going over this is going to be really valuable. Then we'll get into the template that I have for you. This is a GitHub repo that of course I will have linked in the description. And so, this is a demonstration using Phantic AI as my agent framework, how we can build our own idea of skills into any framework that we want. And so I'll go over how I'm building this with Phantic AI, but the concept here is going to work no matter what tool you end up using like Langchain, Crew AI, Eggno, no framework at all, literally anything that you want. And then just as an opportunity here to show you how far we can take our custom agents, I also want to get into evals and observability. So how can we make sure our agent is really following all of the instructions and capabilities that we give it? And so in our case right here, that it's truly leveraging the skills that we give. And so I'll get into that at the end just as a bonus on top of everything showing you how to build skills for yourself.

## Master Class on Skills: What They Are and Why They're So Important

So, first we need to get into at a high level how skills work and why they're so powerful, even if you've used them before. Going over this is going to be really valuable. Then we'll get into the template that I have for you. This is a GitHub repo that of course I will have linked in the description. And so, this is a demonstration using Phantic AI as my agent framework, how we can build our own idea of skills into any framework that we want. And so I'll go over how I'm building this with Phantic AI, but the concept here is going to work no matter what tool you end up using like Langchain, Crew AI, Eggno, no framework at all, literally anything that you want. And then just as an opportunity here to show you how far we can take our custom agents, I also want to get into evals and observability. So how can we make sure our agent is really following all of the instructions and capabilities that we give it? And so in our case right here, that it's truly leveraging the skills that we give. And so I'll get into that at the end just as a bonus on top of everything showing you how to build skills for yourself.

All right, so now let's go over a really really quick master class on skills, what they are, why they are so important. So Anthropic has this article that I'll link to in the description, a really good guide, and they cover best practices for building skills that we'll talk about in a little bit. And so, problem skills are solving. We want to give our agent a lot of different capabilities to supercharge them, but we don't want to overwhelm their context window. Agents are very prone to being overwhelmed when we give them a lot of information through our tools, conversation history, system prompt, everything goes in the window. And so other methods like giving a ton of tools up front to the agent even if it never needs to use them in a specific conversation. That is bad. And so with skills, best way to explain it is to go to a diagram here in the article. And I also of course have it blown up in another tab right here. So, beautifully simple power of skills is the idea of progressive disclosure.

### What Are Skills Solving?

The problem that skills are solving is: We want to give our agents a lot of different capabilities to supercharge them, but we don't want to overwhelm their context window. Agents are very prone to being overwhelmed when we give them a lot of information through our tools, conversation history, system prompt, everything goes in the window.

### The Core Concept: Progressive Disclosure

Instead of giving all tools up front to our agent like MCP servers, we are allowing our agent to discover capabilities over time as it actually needs them. And so only thing we're giving to the agent right away in the system prompt or you can think of it like global rules is the description of capability or skill. And so in this case as an example we have a PDF processing skill. So we're just telling the agent, "Hey, you have this capability if you need it. If the user actually asks you to do something with PDFs and then if the agent receives that kind of request and it wants to leverage the capability then it'll read the skill.md. So skill.md this is the main file that drives any skill that you'll see from Anthropic and all the ones that we'll go over with our custom implementation here. And so this has full instructions for the capability.

### Three Layers of Progressive Disclosure

There are typically three layers to progressive disclosure:

**Layer 1: Description (YAML front matter)**

This is the brief description that's loaded into the agent's system prompt upfront. For a PDF processing skill, it might be:
```yaml
---
description: "Process PDF documents and extract information like form fields, tables, and structured data."
tags: ["pdf", "documents", "extraction"]
---
```

**Layer 2: Skill.md (Main instructions)**

This is the full instruction set—typically 300-500 lines long. It contains:
- How to use the capability
- Tool parameters and responses
- Examples of when to use the capability
- References to third-layer documentation
- Edge cases and error handling

**Layer 3: Reference Documents (Third layer)**

These are additional files that the skill.md can reference for more specific use cases. For example:
- API documentation
- Code examples
- Fallback procedures
- Configuration files

### Key Benefits of Progressive Disclosure

1. **Context Efficiency**: Only load relevant context when needed
2. **Flexibility**: Easy to add new capabilities without modifying the system prompt
3. **Better Performance**: Smaller prompts mean faster token processing
4. **Reduced Overwhelm**: Agent doesn't have to process all capabilities upfront
5. **Scalability**: Can have hundreds of skills without performance impact

### Implementing Skills in Any Framework

The beauty of this pattern is that it's framework-agnostic. Whether you're using:
- Claude Desktop/Code (Anthropic)
- OpenAI (GPT models)
- LangChain (Python framework)
- CrewAI (Multi-agent framework)
- Phasic AI (as shown in the video)
- Custom agent frameworks
- Local AI models
- No framework at all (just your own tools)

All of these frameworks can implement the three-layer progressive disclosure pattern:
1. **Dynamic system prompts** that inject skill descriptions at runtime
2. **Load skill tool** that reads skill.md files when needed
3. **Read reference tool** that can access Layer 3 documents

### The Template Structure

Here's how the template from the video is structured:

```
skills/
├── recipe_finder/
│   ├── skill.md (YAML description)
│   ├── README.md (Usage examples)
│   └── api_reference.md (API docs)
├── weather/
│   ├── skill.md (YAML description)
│   ├── README.md (Usage examples)
│   └── api_reference.md (API docs)
├── world_clock/
│   └── skill.md (Simple conversion skill)
```

Each skill has:
- `skill.md`: The main instruction file (Layer 2)
- `README.md`: Usage documentation
- Optional reference docs: API specs, examples, config files

### Dynamic System Prompt Pattern

The video demonstrates how to build a dynamic system prompt:

1. **Static instructions** (base agent behavior)
2. **Dynamic skill list** (generated from YAML front matters)
3. **Tool definitions** (load_skill, read_reference)

Example prompt structure:
```python
You are an AI agent with the following capabilities:

## Capabilities
{{ skills }}

## Tools
- load_skill(skill_name: str) -> str: Load full instructions for a skill
- read_reference(file_path: str) -> str: Read reference documentation

## How to Use Skills
When a user requests a task that requires a specific skill, use the load_skill tool to load that skill's instructions. Only load the skill when actually needed to save context.
```

### Key Components Explained

#### YAML Front Matter

The video explains that best practices for skill descriptions:
- 50-100 words long
- Describes the capability clearly
- Includes tags for categorization
- Contains path to skill.md file

#### Skill.md File

Contains:
- Complete instructions for using the capability
- Tool parameter definitions
- Examples of typical usage
- References to Layer 3 documentation
- Error handling guidance
- Edge cases to consider

#### Tool Implementation

The video shows how to implement:
1. **Load skill tool**: Reads skill.md file and returns content
2. **Read reference tool**: Accesses Layer 3 docs

Tools are designed to:
- Be lazy (only load when called)
- Return complete file contents
- Provide clear error messages if files don't exist

### Why This Matters

Building custom AI agents with progressive disclosure skills offers several advantages:

1. **Universal Compatibility**: Works with any LLM or agent framework
2. **Scalability**: Can manage dozens or hundreds of skills
3. **Performance**: Better token efficiency by loading only what's needed
4. **Maintainability**: Easy to update skills independently
5. **Customization**: Tailor to your specific use cases
6. **Reusability**: Skills can be shared across different projects

### Example Use Cases from the Video

The video demonstrates several skills:

1. **Recipe Finder**: Searches for recipes (with chicken example)
2. **Weather API**: Gets weather for Tokyo (with reference doc loading)
3. **PDF Processing**: Processes PDFs with form extraction
4. **World Clock**: Simple time zone conversion skill

### Best Practices Summary

Based on the transcript and the demonstration, here are key best practices for building skills with progressive disclosure:

#### Design Principles
- **Keep descriptions short**: 50-100 words in YAML front matter
- **Make skill.md comprehensive**: 300-500 lines of instructions
- **Use clear tags**: Categorize capabilities for easy discovery
- **Reference Layer 3**: For complex skills, provide additional docs
- **Be explicit about when to use**: Clear conditions for tool invocation
- **Design for laziness**: Tools should only load when needed

#### Technical Implementation
- **Dynamic system prompts**: Inject skill descriptions at runtime
- **Tool architecture**: Separate load_skill and read_reference tools
- **File structure**: Organized skills directory with consistent naming
- **Error handling**: Graceful failures with clear messages

### Getting Started

If you want to implement skills in your own AI agent, here's how to get started:

1. **Choose your framework**: Select from Phantic AI, LangChain, CrewAI, or build your own
2. **Set up a skills directory**: Create a folder for your skill files
3. **Create the load_skill tool**: Implement a function to read and return skill.md content
4. **Create the read_reference tool**: Implement access to Layer 3 docs
5. **Design your YAML front matter**: Follow the 50-100 word guideline
6. **Write your skill.md files**: Start with comprehensive instructions for each capability
7. **Test incrementally**: Add skills one at a time and verify they work
8. **Add evals and observability**: As shown in the video, implement testing to ensure agent follows instructions

### Conclusion

The video teaches us that skills and progressive disclosure are not limited to the Claude ecosystem. This is a universal pattern that can be implemented in any framework. By using three-layer progressive disclosure—description (YAML front matter), skill.md (instructions), and reference documents (Layer 3)—you can build powerful, flexible, and efficient AI agents that scale gracefully.

The beauty is in the simplicity: each layer has a clear purpose, and together they create a system that's easy to understand, extend, and maintain. Whether you're using Claude, OpenAI, LangChain, Phantic AI, or a custom framework, you can implement this pattern to give your agents the capabilities they need, when they need them.

---