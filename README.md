# Codex Lite

A small, Codex-native development workflow kit inspired by Everything Claude Code. It focuses on planning, implementation, review, and verification, without enabling MCP servers or hooks.

## What's included

- `AGENTS.md`: concise project guidance.
- `skills/plan-change`: scope and sequence a non-trivial change.
- `skills/implement-change`: make a focused, maintainable implementation.
- `skills/review-change`: inspect a diff for correctness and risk.
- `skills/verify-change`: select and report relevant checks.
- `.codex-plugin/plugin.json`: optional skills-only plugin metadata.
- `.agents/plugins/marketplace.json`: local marketplace entry for this plugin.
- `SPRINTS.md`: staged implementation plan.

See [SPRINTS.md](SPRINTS.md) for scope, milestones, and acceptance criteria.

There are no install scripts, MCP server declarations, hooks, telemetry, credentials, or agent role configs in this starter.

## Install for one project

Copy or merge `AGENTS.md` into the project root. If an `AGENTS.md` already exists, merge only the guidance you want; do not replace your project instructions wholesale.

To make these skills available to Codex in that project, copy the `skills/` directory to `.agents/skills/` at the project root. Keep only skills you want. Existing skills with the same names should be reviewed before merging.

Alternatively, install this folder as a Codex plugin from its bundled local marketplace. From a terminal, run these commands in the cloned Codex Lite directory:

```sh
codex plugin marketplace add .
codex plugin add codex-lite@codex-lite-local
codex plugin list --json
```

Start a new Codex session after installation so it loads the bundled skills. To remove it, run `codex plugin remove codex-lite@codex-lite-local` and, if desired, `codex plugin marketplace remove codex-lite-local`. The plugin bundles skills only; the root `AGENTS.md` remains project guidance and should be copied or merged separately.

## Install skills for your user

Copy any selected `skills/<name>/` directory into `~/.agents/skills/<name>/`. Codex scans this user directory for personal skills. To remove one, delete only the corresponding copied folder. This does not require changing `~/.codex/config.toml`.

## Update and remove

To update, compare the new `AGENTS.md` and each selected skill against your local copy and merge desired changes. To uninstall, remove only the files you copied or uninstall the plugin through Codex. Keep a backup if you have edited those files locally.

## Workflow

For small tasks, work directly and run a relevant check. For a complex or risky change, use `plan-change`, implement in small steps, use `review-change` on the diff, then use `verify-change` to select checks. Skills provide guidance; they do not themselves grant tool access or run automatically.

## Compatibility

This starter uses Codex `AGENTS.md`, `.agents/skills/`, and the Codex-compatible plugin manifest. Local plugin discovery and marketplace commands depend on the Codex version and host; the project and user skill-copy options remain available if plugin installation differs.

## Why this is lightweight

The comparison below uses the exact linked [WorldFlowAI repository](https://github.com/worldflowai/everything-claude-code), checked out at revision `432485b` on 2026-10-28. Repository contents can change over time.

| Surface | Linked repository snapshot | Codex Lite v0.1 |
|---|---:|---:|
| Tracked files | 81 | 10 |
| Skills (`SKILL.md` folders) | 11 | 4 |
| Agent prompts | 9 | 0 |
| Slash-command files | 15 | 0 |
| Hook files | 5 | 0 |
| Rule files | 8 | 1 concise `AGENTS.md` |
| Runtime/install scripts | 8 | 0 |
| MCP config files | 1 | 0 |

That is 71 fewer tracked files in this snapshot (about 88% fewer). The categories are repository counts, not equivalent features: one concise `AGENTS.md` does not reproduce eight separate upstream rule files. Codex Lite intentionally covers fewer workflows and includes no automation or external integrations; it is a focused starting kit, not feature parity with the original.

## License

MIT. See `LICENSE`.
