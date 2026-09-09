# AI Technical Interview Assistant

An AI-powered mock interview system that conducts live technical interviews based on a candidate's self-described tech stack and project experience — no resume upload required.

## Overview

This project uses a structured prompt to drive an LLM (e.g., Claude) through a full technical interview flow:

1. Asks the candidate about their tech stack and a recent project.
2. Dynamically generates relevant interview questions based on that input.
3. Conducts the interview one question at a time.
4. Stays neutral during the interview — never reveals whether an answer was right or wrong, and never supplies answers if the candidate can't respond. It simply moves on to the next question.
5. Optionally provides a summary evaluation only at the end, if requested.

## Why no resume upload?

The assistant is designed to work purely conversationally. Instead of parsing an uploaded resume/file, it asks the candidate directly about their stack and projects at the start of the session. This keeps the tool lightweight and usable in any chat interface without file-handling dependencies.

## Folder Structure

```
docs/
├── README.md           # This file — project overview
├── PROMPT_DESIGN.md     # The core interview logic and prompt structure
├── ARCHITECTURE.md      # How the system is structured / how to integrate it
├── CONTRIBUTING.md      # Guidelines for contributing
└── CHANGELOG.md         # Version history
```

## Quick Start

1. Copy the system prompt from `PROMPT_DESIGN.md` into your LLM application (chatbot, API call, etc.).
2. Start a new conversation — the assistant will begin by asking about your tech stack and a recent project.
3. Answer each question as it's asked. The interview proceeds one question at a time regardless of whether you answer correctly, incorrectly, or skip.
4. At the end, ask for feedback if you'd like a summary evaluation.

## Key Design Principles

- **No file dependency** — works from conversation only.
- **One question at a time** — avoids overwhelming the candidate.
- **Neutral mid-interview behavior** — no correctness feedback, no answer leakage, ever.
- **Adaptive questioning** — questions are generated from what the candidate actually says, not a fixed question bank.

## License

Add your license of choice here (e.g., MIT).
