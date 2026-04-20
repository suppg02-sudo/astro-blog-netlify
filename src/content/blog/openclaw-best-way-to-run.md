---
pubDatetime: 2026-02-08T22:45:00Z
title: "I figured out the best way to run OpenClaw"
postSlug: "openclaw-best-way-to-run"
description: "I figured out the best way to run OpenClaw"
tags:
  - automation
  - matthew-berman
  - openclaw
  - ai
  - cloudbot
---

## Video Transcript

**Source**: YouTube video by Matthew Berman  
**Duration**: ~22 minutes  
**Video ID**: 3GrG-dOmrLU

### Key Topics

Matthew Berman discusses the optimal approach to running OpenClaw, covering:

#### Model Selection Strategy
The choice of which model to use is one of the biggest open questions. The answer is to use multiple models:
- Use the best possible model for complex tasks
- Implement fallback models as backup
- Consider both local and cloud-based models
- Best models are less susceptible to prompt injection

#### Scheduling and Automation
- Recurring tasks can be set to run every 30 minutes or any custom interval
- Uses cron jobs for more complex scheduling
- CloudBot learns and adapts to your preferences as you configure it

#### Analytics Integration
Example workflow for checking YouTube performance:
- Ask CloudBot to fetch last 3 videos and their analytics
- CloudBot accesses YouTube API and analytics API
- Results posted to Telegram or Slack for team visibility

#### Security Practices
For handling file downloads and complex tasks:
- Always scan files for malicious content before processing
- Use the best available model for security-sensitive operations
- Implement proposal/approval workflows before making changes
- Builds confidence in automated task execution

#### Real-World Use Cases
Personal automation examples:
- Schedule management: Upload recycling company schedule, get weekly reminders
- Content checking: Automated performance monitoring for videos
- File processing: Secure download and analysis workflows

#### Context Window Optimization
- Store topic-specific conversation history instead of full history
- Saves memory and context window space
- Enables multi-day and multi-week conversation continuity
- Only loads relevant context for specific tasks

### Summary

The best way to run OpenClaw involves a multi-faceted approach combining appropriate model selection, intelligent scheduling, robust security practices, and efficient context management. Matthew demonstrates how CloudBot can be configured to automate complex workflows while maintaining security and reliability.

### Full Transcript

View the complete transcript: [Transcript File](/media/docs/output/youtube_I_figured_out_the_best_way_to_run_OpenClaw_3GrG-dOmrLU_20260208_224559.txt)

### Resources
- **Video Link**: https://www.youtube.com/watch?v=3GrG-dOmrLU
- **Channel**: [Matthew Berman](https://www.youtube.com/@matthew_berman)

---

*This blog post was automatically created from a YouTube video transcript. For more context and details, watch the full video above.*