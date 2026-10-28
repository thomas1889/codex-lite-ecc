---
name: continuous-learning
description: Turn a reusable lesson from a coding session into a focused, privacy-safe Codex skill. Use when asked to learn or remember a pattern, or when the learning hook requests a review.
---

# Continuous learning

Convert a proven, reusable lesson from the current conversation into a skill that Codex can discover in later sessions. Do not treat every fix as a lesson.

## Find a useful pattern

Look for a user correction, non-obvious error resolution, repeatable debugging method, framework workaround, or project convention that is likely to help again. Skip typos, one-time changes, external outages, guesses, and information that is already clear in existing instructions or skills.

Use only the current conversation and relevant project files. Do not open or parse Codex transcript files. Never preserve credentials, private keys, personal or customer data, private conversation details, or other sensitive information. Generalize examples and remove identifying details.

## Draft and save

1. Check `.agents/skills/learned/` and nearby skills for an existing match. Prefer improving a focused existing skill over duplicating it.
2. Draft one small `SKILL.md` with valid `name` and `description` frontmatter. Explain when it applies, the proven steps, and important limits; include an example only when it makes the pattern easier to reuse.
3. Show the proposed path and complete draft to the user. Do not create or edit a file until the user approves that draft.
4. By default, save approved project learnings to `.agents/skills/learned/<slug>/SKILL.md`. Save a user-wide learning under `~/.agents/skills/learned/<slug>/SKILL.md` only when the user asks for a global skill.
5. If a matching skill already exists, show a focused proposed diff and get approval before changing it.
6. Confirm the saved skill has valid frontmatter and a precise trigger description, then report its path and scope.

If no durable pattern emerged, say so briefly and make no change. A learning-hook prompt is only a request to review; it never authorizes writing. Do not commit, push, or change Codex settings as part of saving a learning.

Invoke directly with `$continuous-learning` when you want to review a session for learnings.
