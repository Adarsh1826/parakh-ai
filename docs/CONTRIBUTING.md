# Contributing

Thanks for your interest in improving the AI Technical Interview Assistant.

## How to Contribute

1. Fork the repository and create a new branch for your change.
2. Make your changes (prompt updates, code, or docs).
3. Test your changes by running through a full mock interview session end-to-end.
4. Open a pull request with a clear description of what changed and why.

## Areas Open for Contribution

- **Prompt improvements** — refining question generation quality, tone, or flow logic in `PROMPT_DESIGN.md`.
- **Scoring/feedback system** — designing a structured rubric for end-of-interview summaries.
- **Frontend** — building or improving the chat UI.
- **Backend** — session management, API integration, rate limiting.
- **New interview modes** — e.g., system design focus, DSA focus, behavioral rounds.

## Guidelines for Prompt Changes

If you're modifying the core interview prompt, please preserve these non-negotiable behaviors unless discussed in an issue first:
- The assistant must never ask for a resume/file upload.
- The assistant must never reveal correctness of an answer mid-interview.
- The assistant must never explain or answer a question the candidate couldn't answer — it should move on silently.
- Only one question should be asked per turn.

## Reporting Issues

Please open an issue if you notice:
- The assistant leaking answers or correctness signals mid-interview.
- The assistant asking for a resume upload.
- Repetitive or irrelevant question generation.
- Any other deviation from the intended interview flow.

## Code Style (if contributing code)

- Use clear, descriptive commit messages.
- Keep pull requests focused on a single change where possible.
- Update relevant docs (`README.md`, `ARCHITECTURE.md`, `PROMPT_DESIGN.md`) alongside any behavioral changes.
