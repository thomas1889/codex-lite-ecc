# Codex Lite

A small, Codex-native development workflow kit inspired by Everything Claude Code. It covers planning, implementation, review, verification, and supervised continuous learning.

## What's included

- `AGENTS.md`: concise project guidance.
- `skills/plan-change`: scope and sequence a non-trivial change.
- `skills/implement-change`: make a focused, maintainable implementation.
- `skills/review-change`: inspect a diff for correctness and risk.
- `skills/verify-change`: select and report relevant checks.
- `skills/continuous-learning`: turn approved lessons into reusable Codex skills.
- `.codex-plugin/plugin.json`: optional plugin metadata.
- `.agents/plugins/marketplace.json`: local marketplace entry.
- `hooks/hooks.json` and `scripts/hooks/continuous_learning.py`: optional local learning nudge.
- `SPRINTS.md`: staged implementation plan.

There are no MCP server declarations, telemetry, credentials, or agent role configs. The single optional hook counts prompts per session; it does not store prompt text, inspect transcript files, or write learnings.

## Install for one project

Copy or merge `AGENTS.md` into the project root. If an `AGENTS.md` already exists, merge only the guidance you want; do not replace your project instructions wholesale.

To make the skills available in a project, copy the `skills/` directory to `.agents/skills/`. Keep only skills you want, and review any existing skills with the same names before merging.

Alternatively, install this folder as a Codex plugin from its bundled local marketplace. From a terminal, run these commands in the cloned Codex Lite directory:

```sh
codex plugin marketplace add .
codex plugin add codex-lite@codex-lite-local
codex plugin list --json
```

Start a new Codex session so it loads the bundled skills. Codex requires you to review and trust plugin hooks before they run; use `/hooks` in the CLI to inspect and trust the learning hook. The automatic nudge requires Python 3 on the machine running Codex. Skills still work without Python, and you can invoke `$continuous-learning` directly. To remove the plugin, run `codex plugin remove codex-lite@codex-lite-local` and, if desired, `codex plugin marketplace remove codex-lite-local`. The root `AGENTS.md` remains project guidance and should be copied or merged separately.

## Install skills for your user

Copy selected `skills/<name>/` directories into `~/.agents/skills/<name>/`. Codex scans this user directory for personal skills. To save a learning across projects, use `~/.agents/skills/learned/<slug>/SKILL.md` only when you choose global scope. To remove a copied skill, delete only its folder. No Codex settings file needs to change.

## Update and remove

Compare updated `AGENTS.md` and skill files with your local copies before merging. Preserve learned skills under `.agents/skills/learned/` or `~/.agents/skills/learned/`. To uninstall, remove only the files you copied or uninstall the plugin through Codex. Keep a backup if you edited those files locally.

## Workflow

For small tasks, work directly and run a relevant check. For a complex or risky change, use `plan-change`, implement in small steps, use `review-change` on the diff, then use `verify-change` to select checks. Skills provide instructions; they do not grant tool access.

## Self-improving workflow

After ten user prompts in one session, the optional local hook asks Codex to review the current conversation for one reusable correction, debugging technique, workaround, or project convention. The hook keeps only a per-session count under the plugin's data directory and removes that count at session end. It does not read or save transcript contents. Short sessions are left alone.

If a durable pattern emerges, `continuous-learning` drafts a focused skill and shows it to you. It saves the file only after you approve the exact draft. Project learnings go to `.agents/skills/learned/<slug>/SKILL.md`, where Codex can discover them in later sessions. A global learning is saved only if you explicitly request that scope. One-off fixes and sensitive or private details are not saved. If no reusable pattern emerged, no skill is created.

You can request this review at any time with `$continuous-learning`. Without the optional hook, the skill remains available for explicit or implicit invocation.

## Compatibility

The kit uses Codex `AGENTS.md`, `.agents/skills/`, a Codex-compatible plugin manifest, and the Codex plugin-hook format. Hook support and trust review depend on the Codex version and host; manual skill installation and explicit `$continuous-learning` remain available if hooks are unavailable.

## Why this is lightweight

The comparison below uses the linked [WorldFlowAI repository](https://github.com/worldflowai/everything-claude-code), checked out at revision `432485b` on 2026-10-28. Repository contents can change over time.

| Surface | Linked repository snapshot | Codex Lite v0.2 |
|---|---:|---:|
| Tracked files | 81 | 13 |
| Skills (`SKILL.md` folders) | 11 | 5 |
| Agent prompts | 9 | 0 |
| Slash-command files | 15 | 0 |
| Hook files | 5 | 1 |
| Rule files | 8 | 1 concise `AGENTS.md` |
| Runtime/install scripts | 8 | 1 optional Python hook |
| MCP config files | 1 | 0 |

That is 68 fewer tracked files in this snapshot (about 84% fewer). The counts are not feature equivalents: one concise `AGENTS.md` does not reproduce eight separate upstream rule files. Codex Lite supports fewer workflows. Its hook only requests an occasional learning review; it adds no MCP integrations, automatic skill writes, or transcript retention.

## License

MIT. See `LICENSE`.

## References

- [Everything Claude Code continuous-learning skill](https://github.com/worldflowai/everything-claude-code/blob/main/skills/continuous-learning/SKILL.md) and [`/learn` workflow](https://github.com/worldflowai/everything-claude-code/blob/main/commands/learn.md).
- [OpenAI Docs: Build skills](https://learn.chatgpt.com/docs/build-skills) and [Codex hooks](https://developers.openai.com/codex/hooks).
