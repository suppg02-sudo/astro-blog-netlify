---
pubDatetime: 2026-02-13T07:02:16Z
title: "Changes to Global Instructions (gr) in the Last 3 Versions"
postSlug: "global-instructions-version-history"
description: "Changes to Global Instructions (gr) in the Last 3 Versions"
tags:
  - documentation
  - opencode
  - global-instructions
---

## Introduction

The global instructions file (`global-instructions.md`) in OpenCode has undergone significant improvements in recent versions. Version tracking has been established to document these changes and ensure transparency in the development process. This post examines the three most recent versions and highlights the major enhancements.

## Version 3 (2026-02-12) - Auto Backup

**Date**: February 12, 2026
**Lines**: 1,934

Version 3 introduced comprehensive auto-backup functionality for the global instructions file. This version represented a significant expansion of the documentation system, nearly doubling in size from previous versions. The auto-backup feature ensures that changes to global rules are automatically saved and versioned, making it easier to track modifications and recover previous configurations if needed.

## Version 2 (2026-02-13) - Major Restructure

**Date**: February 13, 2026
**Lines**: 993
**Reduction**: 49% compared to Version 3

Version 2 brought a dramatic restructure of the entire global instructions document. Through careful organization and consolidation of redundant content, the document was reduced by nearly half while maintaining all critical functionality. Key changes included:

- **Trigger word files moved**: Trigger word definitions were separated into individual markdown files in the `/media/docs/instructions/triggers/` directory, improving maintainability and organization.
- **Better structure**: Logical grouping of related content and improved readability.
- **Enhanced navigation**: Clearer section headers and table of contents organization.

## Version 1 (2026-02-13) - Enhanced AGENTS.md Protocols

**Date**: February 13, 2026
**Lines**: 1,017

The first version of the day introduced enhanced protocols for the AGENTS.md file, which defines agent behavior guidelines:

- **Tool execution safety**: Added comprehensive safety guidelines for tool use, including the critical "Tool Execution Completion Protocol" to prevent incomplete tool invocations.
- **Skill management**: Expanded rules for skill discovery, loading, and delegation patterns.
- **Browser validation**: Strengthened requirements for web server testing with agent browser automation.
- **Task delegation**: Refined task delegation patterns and requirements.

A new "rules" trigger was also added, enabling interactive menu-driven restructuring of rules files.

## Summary of Changes

| Version | Date | Lines | Key Changes |
|---------|------|-------|-------------|
| Version 3 | 2026-02-12 | 1,934 | Auto backup functionality |
| Version 2 | 2026-02-13 | 993 | Major restructure, 49% reduction, trigger word files moved |
| Version 1 | 2026-02-13 | 1,017 | Enhanced AGENTS.md protocols, rules trigger added |

## Impact and Benefits

These incremental improvements have made the OpenCode global instructions more:

- **Maintainable**: Separated trigger word files and better organization
- **Safe**: Comprehensive safety protocols and tool execution rules
- **Testable**: Standardized browser validation requirements
- **Transparent**: Version tracking and clear change documentation

The ongoing evolution of global instructions reflects a commitment to maintaining high-quality, well-documented agent behaviors and workflows.

## Conclusion

The last three versions demonstrate a continuous effort to improve the OpenCode configuration and documentation system. Each version has built upon previous improvements, creating a more robust and maintainable foundation for agent operations. Version 2's restructure, in particular, shows that significant improvements can be achieved through careful organization and consolidation.

---

**Published**: February 13, 2026
**Source**: OpenCode Global Instructions Version History