# Architecture

## Overview

This project is prompt-driven rather than code-driven — the core logic lives in a system prompt (see `PROMPT_DESIGN.md`) that can be deployed on top of any LLM chat interface or API. This document outlines how to structure an actual application around that prompt.

## Conceptual Flow

```
┌─────────────────────┐
│   User opens chat    │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────────────┐
│ Assistant asks about stack   │
│ and recent project           │
└──────────┬───────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Candidate responds            │
└──────────┬───────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Assistant generates question  │
│ based on stated stack/project │
└──────────┬───────────────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
 Answered     Not answered
     │           │
     └─────┬─────┘
           ▼
┌─────────────────────────────┐
│ Neutral acknowledgment        │
│ (no correctness feedback)     │
└──────────┬───────────────────┘
           │
           ▼
  Loop until question count
  reached or candidate ends
           │
           ▼
┌─────────────────────────────┐
│ Optional final summary        │
│ (only if requested)           │
└───────────────────────────────┘
```

## Suggested Implementation Options

### Option A — Chat UI wrapper (recommended for MVP)
- Frontend: simple chat UI (React, Next.js, or similar).
- Backend: thin API layer that forwards conversation history to the Claude API with the system prompt from `PROMPT_DESIGN.md`.
- State: conversation history maintained client-side or in a lightweight session store (no database required for MVP).

### Option B — API integration into an existing platform
- Embed the system prompt into an existing interview/hiring platform's chatbot layer.
- Pass the system prompt once per session; maintain multi-turn context via the API's message history.

## Components (if building a full app)

| Component        | Responsibility                                      |
|-------------------|------------------------------------------------------|
| `chat-ui`         | Renders conversation, collects candidate input       |
| `session-manager` | Tracks question count, conversation state per user   |
| `llm-client`      | Sends system prompt + history to Claude API          |
| `interview-config`| (Optional) stores difficulty level, topic focus, question count |

## State to Track Per Session
- Full conversation history (required for context-aware follow-up questions).
- Number of questions asked so far (to trigger wrap-up).
- Whether the candidate has requested final feedback.

## Notes
- No resume parsing, file storage, or file upload pipeline is needed — this significantly simplifies the architecture compared to resume-based interview tools.
- If resume-based question generation is added later, this would require a file upload + parsing step (e.g., PDF/DOCX text extraction) feeding into Step 1 of the prompt instead of/alongside the conversational ask.
