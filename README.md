<p align="center">
  <img src="/docs/assets/banner.png" alt="AI Technical Interview Assistant banner" width="100%" />
</p>

<h1 align="center">AI Technical Interview Assistant</h1>

<p align="center">
  A conversational AI that conducts live technical mock interviews based on your tech stack and project experience — no resume upload needed.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="status" />
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="license" />
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs welcome" />
  
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-how-it-works">How it works</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

## Features

- 🗣️ **Fully conversational** — no file or resume upload required, just chat.
- 🧠 **Adaptive questions** — generated live from your stated tech stack and project, not a fixed question bank.
- 🎯 **One question at a time** — mirrors the pacing of a real interview.
- 🤐 **Neutral by design** — never reveals correctness mid-interview, and never leaks answers if you skip a question. It simply moves forward.
- 📋 **Optional final feedback** — ask for a summary evaluation only at the end, if you want one.
- 🔌 **Model-agnostic prompt** — built to run on top of any LLM chat interface or API (e.g., Claude).

## Demo

<!-- <p align="center">
  <img src="/docs/assets/demo-screenshot.png" alt="Mock interview session demo" width="80%" />
</p> -->

> The assistant asks a question, and whether you answer, skip, or say "I don't know," it responds neutrally and moves to the next question — no correctness feedback until you explicitly ask for a wrap-up summary.

## How It Works

```
 1. Assistant asks about your tech stack + a recent project
             │
             ▼
 2. Generates a relevant question from what you shared
             │
             ▼
 3. You answer (or skip) ──► Neutral acknowledgment ──► Next question
             │
             ▼
 4. After N questions, interview wraps up
             │
             ▼
 5. (Optional) You ask for feedback → summary evaluation
```

See [`PROMPT_DESIGN.md`](./PROMPT_DESIGN.md) for the full system prompt and the reasoning behind each rule.

## Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/ai-interview-assistant.git
   cd ai-interview-assistant
   ```

2. **Grab the system prompt**
   Copy the prompt from [`docs/PROMPT_DESIGN.md`](./PROMPT_DESIGN.md) into your LLM app of choice (Claude, a custom chatbot, an API call, etc.).

3. **Start a session**
   Open a new conversation with the prompt loaded — the assistant will kick off by asking about your tech stack and a recent project.

4. **Do the interview**
   Answer each question as it comes. Skipping a question is fine — the assistant moves on without judgment or hints.

5. **Get feedback (optional)**
   At the end, ask something like *"How did I do?"* to get a summary evaluation.

## Project Structure

```
.
├── docs/
│   ├── assets/
│   │   ├── banner.png
│   │   └── demo-screenshot.png
│   ├── README.md
│   ├── PROMPT_DESIGN.md
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   └── CHANGELOG.md
└── README.md
```

## Roadmap

- [ ] Structured scoring rubric for final feedback
- [ ] Difficulty levels (junior / mid / senior)
- [ ] Topic focus mode (system design, DSA, behavioral, etc.)
- [ ] Per-question timers
- [ ] Hosted chat UI (React/Next.js) with session history

See open [issues](../../issues) for the current backlog.

## Contributing

Contributions are welcome! Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before opening a PR — especially the section on preserving core interview behaviors (no resume upload, no mid-interview correctness feedback).

1. Fork the repo
2. Create your branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push and open a PR

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  <sub>Built for practicing technical interviews the way they actually feel — one question at a time, no hand-holding.</sub>
</p>
