# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- Considering: scoring rubric for structured final feedback.
- Considering: difficulty level selection (junior / mid / senior).

## [1.1.0] - 2026-09-09
### Changed
- Removed dependency on resume/file upload. The assistant now gathers tech stack and project context directly through conversation at the start of the interview.
- Updated interview behavior so that if a candidate fails to answer or skips a question, the assistant moves on to the next question without revealing the correct answer or explanation.
- Clarified that no correctness feedback (right/wrong) is given for any answer during the interview, whether correct, incorrect, partial, or skipped.

## [1.0.0] - Initial Version
### Added
- Initial system prompt for AI-driven technical mock interviews.
- Dynamic question generation based on candidate's stated tech stack and project.
- End-of-interview summary feedback (on request).
