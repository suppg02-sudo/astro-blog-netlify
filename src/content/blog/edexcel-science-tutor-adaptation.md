---
pubDatetime: 2026-02-11T10:00:00Z
title: "Adapting an Interactive Coding Tutor for GCSE Combined Science"
postSlug: "edexcel-science-tutor-adaptation"
description: "How to adapt the interactive coding tutor architecture to create a real-time TTS revision tool for Edexcel Combined Science GCSE Foundation tier."
tags:
  - tts
  - education
  - revision
  - science
  - edexcel
  - gcse
  - ai
---

## The Idea

There's a blog post doing the rounds about building an interactive coding tutor — one where you click on lines of code and an AI voice explains what they do in real time. The stack is Node.js, React, GPT-4 Mini, and InWorld TTS. The latency is around 350ms from click to hearing an explanation. It works brilliantly for teaching React design patterns.

The question is: can the same architecture work for GCSE science revision?

## Why It Fits

The core interaction model — click something, hear an explanation — translates directly to science. Instead of clicking a line of code, a student clicks on the mitochondria in a cell diagram, or the ammeter in a circuit, or a reactant in a chemical equation. The backend generates a Foundation-level explanation using GPT-4 Mini, InWorld TTS converts it to speech, and the student hears it in under half a second.

The "good code vs bad code" comparison from the coding tutor becomes "correct method vs common mistakes" in core practicals. Click a step in the experiment, hear what to do. Click the "common mistake" panel, hear what students typically get wrong and why it loses marks.

## The Specification

The target is Edexcel Combined Science (1SC0), Foundation tier. This is important because **Combined Science is one qualification — a double award giving two grades — not three separate GCSEs**. The content is deliberately smaller than separate sciences. Some topics are excluded entirely. The tutor must match this scope exactly or it wastes revision time on material that will never appear in the exam.

There are 6 papers, 18 core practicals, and a physics equation sheet provided in the exam. Foundation tier caps at grade 5 and excludes all Higher-only content.

## What Gets Built

The tutor has six main features:

### 1. Clickable Scientific Diagrams
SVG-based visuals of cells, circuits, waves, atomic structures, the EM spectrum. Click any labelled part, hear an explanation that matches CGP terminology. Diagrams highlight the active region while audio plays.

### 2. Equation Interaction
Physics and chemistry equations rendered with KaTeX. Click any variable for an explanation. Clearly marked whether each equation is given on the exam sheet or must be memorised. Foundation tier only — no Higher-only equations shown.

### 3. Core Practical Walkthroughs
All 18 practicals step-by-step. Variables identified, safety covered, common mistakes explained. These are guaranteed exam content worth 15% of all marks. The "good method vs bad method" pattern maps perfectly from the coding tutor.

### 4. Exam Question Practice
Past paper questions and LLM-generated questions in Edexcel style. Submit an answer, hear mark scheme feedback via TTS: "You'd score 3 out of 4 because you didn't mention the control variable."

### 5. Command Word Training
What Edexcel means by Describe, Explain, Calculate, Compare, Evaluate, Suggest. Available as a clickable reference on every question. Understanding command words is where most Foundation students lose marks.

### 6. Ask Tutor
Free-form voice or text questions on any topic, exactly as in the original coding tutor.

## Content Structure

**6 papers, 2 per subject area:**

| Paper | Area | Topics |
|---|---|---|
| Papers 1-2 | Biology | Cells, genetics, homeostasis, ecosystems |
| Papers 3-4 | Chemistry | Atomic structure, reactions, rates, atmosphere |
| Papers 5-6 | Physics | Motion, energy, waves, electricity, magnetism |

Physics comes first (weakest area for this student), then chemistry, then biology. The student starts using the Physics MVP within two weeks while the rest is being built.

## What Doesn't Get Built

This is for one student revising for summer exams. No user accounts, no database, no analytics dashboard, no gamification. Progress is a simple checklist stored in the browser. The exam is the motivation — the tool just needs to be fast, accurate, and friction-free.

## Build Approach

- **Week 1**: Content prep — parse CGP text, past papers, mark schemes into structured JSON
- **Week 2**: Physics Paper 5 MVP ships — student starts revising Physics 1
- **Week 3**: Physics Paper 6 complete — all physics topics, core practicals, calculation practice
- **Weeks 4-5**: Chemistry papers 3-4 with equation balancing and practical walkthroughs
- **Weeks 6-7**: Biology papers 1-2 with diagram labelling and fieldwork explanations
- **Week 8+**: Timed paper practice, weak topic review loops, command word training

The stack stays identical to the coding tutor: Node.js backend, React frontend, GPT-4 Mini for explanations, InWorld TTS for voice. The only new frontend libraries are KaTeX for equations and D3/React-SVG for interactive diagrams.

## The Key Constraint

Every explanation, every question, every practical must be **Foundation-tier Combined Science only**. The system prompt explicitly forbids Higher-only content. It never says "at Higher tier you would also learn..." because that creates anxiety. It matches CGP terminology exactly. It knows which equations are on the exam sheet. It understands what Edexcel command words require for full marks.

The architecture from the coding tutor is sound. The adaptation is mostly a content and prompt engineering challenge, not a technical one.

## Success Metrics

The tutor works if:

1. Student can click any diagram part and hear explanation within 500ms
2. All 18 core practicals have complete walkthroughs with variables, method, safety, common mistakes
3. Exam questions generate feedback matching real Edexcel mark schemes
4. Physics equations are clearly marked: given on sheet vs must memorise
5. Command words are explained on every question
6. Student uses it daily without friction — fast, clear navigation, no bugs
7. Content matches CGP terminology — no confusion between resources

## What's Next

The formal plan is documented. The student will supply:
- CGP revision guides (scanned/photographed)
- Past papers (PDFs)
- Mark schemes (PDFs)
- Textbook (reference)

Then:
1. Extract and structure all content into JSON
2. Build Physics MVP (week 2)
3. Student begins revising while remaining subjects are built
4. Full tutor ready by week 8 for intensive exam prep

The core insight: the real-time TTS feedback model that works for code explanation works just as well for science. Click a diagram, hear science. Submit an answer, hear marks and feedback. The architecture is proven. This is adaptation, not invention.

---

**Full technical plan**: [/media/docs/output/edexcel-science-tutor-plan.md](/media/docs/output/edexcel-science-tutor-plan.md)

**Original blog post**: [Interactive Coding Tutor with Real-Time TTS](/posts/interactive-coding-tutor-real-time-tts/)