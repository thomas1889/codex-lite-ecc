# Codex Lite: a small, Codex-native development toolkit

**Purpose:** define and build a focused, low-maintenance alternative to the Everything Claude Code toolkit, designed for Codex from day one.

**Status:** the v0.1 starter is published; this plan records the v0.2 supervised-learning addition and follow-on work.

## Product definition

Codex Lite packages reusable development instructions and skills around Codex's native project conventions. It helps developers plan, implement, review, and verify changes, then turn approved lessons into skills that can improve future sessions.

The repository linked for this project is a Claude Code toolkit. Its checked-out snapshot (revision `432485b`, fetched 2026-10-28) contains 81 tracked files, including 11 skill folders, 9 agent prompts, 15 slash-command files, 5 hook files, 8 rule files, 8 runtime/setup scripts, and 1 MCP configuration. These are inventory counts, not one-to-one capability comparisons. Codex Lite uses the same broad workflow idea but implements it with Codex-native files and a much smaller opt-in surface. It is an independent, MIT-licensed implementation inspired by general workflows; it does not copy upstream files or imply endorsement.

## Goals and non-goals

### Goals

- Work in a Codex project using `AGENTS.md`, portable `SKILL.md` files, and optional Codex plugin packaging.
- Ship a tiny starter bundle with clear instructions and five focused skills: planning, implementation discipline, review, verification, and continuous learning.
- Preserve existing user and project configuration.
- Make integrations, multi-agent roles, and lifecycle hooks opt-in and independently reviewable.
- Support use by copying the starter into a repo, using its skills as a plugin, or selectively copying skills into `.agents/skills/`.

### Non-goals for v1

- Recreating hundreds of upstream skills, commands, or specialized agents.
- Enabling MCP servers, global hooks, scheduled jobs, or multi-agent execution by default. The one bundled learning hook runs only after the user trusts its definition.
- Requiring a hosted service, API key, package manager, or runtime dependency.
- Overwriting an existing `AGENTS.md`, Codex config, or user skill.

## Lightweight design

```text
codex-lite/
├── AGENTS.md                    # concise project-wide workflow and safety baseline
├── README.md                    # install choices, usage, maintenance
├── SPRINTS.md                   # staged plan and acceptance criteria
├── LICENSE                      # MIT
├── .agents/
│   └── plugins/marketplace.json # local plugin catalog
├── .codex-plugin/
│   └── plugin.json              # optional Codex plugin metadata
├── skills/
│   ├── plan-change/SKILL.md
│   ├── implement-change/SKILL.md
│   ├── review-change/SKILL.md
│   ├── verify-change/SKILL.md
│   └── continuous-learning/SKILL.md
├── hooks/hooks.json             # optional, local-only learning prompt
└── scripts/hooks/continuous_learning.py # counts prompts; never reads transcripts
```

The v0.2 kit contains 13 tracked files: five skills, one concise `AGENTS.md`, one optional hook manifest, and one dependency-free Python hook helper, plus the README, sprint plan, plugin catalog, plugin manifest, and license. The helper stores only a per-session prompt count in plugin data; it does not parse transcripts or write learnings. Python is needed only for the automatic nudge; the learning skill remains usable without it.

## Product decisions

| Topic | v1 decision | Reason |
|---|---|---|
| Primary host | Codex CLI and Codex app | Use Codex-native instructions, skills, plugin format, and project agent files |
| Baseline | `AGENTS.md` | No plugin is required for project guidance |
| Skills | Five small workflow skills | Covers the coding loop and approved learning without a huge catalog |
| Plugin | Optional skills plus a local learning hook | Installs as one unit without MCP or global config changes |
| MCP | None by default | External services add access, configuration, and maintenance overhead |
| Hooks | One local learning hook, reviewed and trusted by the user | Offers one end-of-turn review after 10 prompts; stores no prompt contents |
| Agents | Deferred | Native roles can be added after validating useful read-only cases |
| Installer | Manual copy first | Simple, auditable, and reversible; automation only after install paths are validated |
| User config | Never edited by default | Prevent accidental changes to global Codex settings |
| Checks | Validate skill/plugin metadata and the optional hook's state transitions | The hook is dependency-free Python and does not call external services |

## Sprint plan

Assumption: one developer, one-week sprints. Re-estimate after Sprint 0; sprint durations are planning units, not promised calendar dates.

### Sprint 0 — Scope and compatibility spike (2–3 days)

**Objective:** confirm the smallest useful product boundary and validate the target Codex install surfaces.

**Stories**

- As a maintainer, I can explain what Codex Lite adds in one paragraph and what it intentionally excludes.
- As a Codex user, I can install locally without changing global configuration.
- As a maintainer, I can distinguish project guidance, discoverable skills, optional plugin packaging, and agent definitions.

**Tasks**

1. Confirm supported Codex surfaces against current official docs and the supported CLI version.
2. Keep the four core workflows: plan, implement, review, verify.
3. Create the starter directory and document the three installation paths.
4. Record compatibility questions and decide the minimum Codex version to support.

**Acceptance criteria**

- A clean repository can follow README instructions without modifying `~/.codex/config.toml`.
- The plugin manifest validates against the currently supported schema and references only bundled content.
- Skills use valid frontmatter and accurately describe when they activate.
- Open questions are either closed with evidence or recorded as Sprint 1 blockers.

**Exit gate:** a dry-run installation walkthrough succeeds on a clean test project.

### Sprint 1 — Starter core (1 week)

**Objective:** publish a usable, minimal kit.

**Stories**

- As a developer, I can get concise plan/implement/review/verify guidance in a project.
- As a developer, I can opt into one Codex plugin with the workflow skills and learning hook instead of copying files.
- As a user with local conventions, my existing instructions remain authoritative.

**Tasks**

1. Refine `AGENTS.md` to state scope, plan-before-complex-work, focused edits, evidence-based review, and honest verification.
2. Complete the five skill definitions, including continuous learning.
3. Add plugin metadata and a local-only learning hook; keep MCP and global config changes absent.
4. Document project-local copy and global selective-copy install methods.
5. Add a non-destructive update/uninstall procedure.

**Acceptance criteria**

- Each skill is one workflow, has a clear trigger, and fits within a short read.
- The learning flow drafts a single reusable skill, waits for user approval, and stores it in a Codex-discoverable project location.
- The learning hook does not store prompt text, parse transcript files, or write learned skills.
- README states that skills are opt-in and project instructions should be merged rather than overwritten.
- No secrets, credentials, telemetry, downloads, or scripts run during installation.
- One sample task can proceed from plan to verification using only bundled material.

**Exit gate:** new-user walkthrough completes without maintainer explanation.

### Sprint 2 — Quality and compatibility (1 week)

**Objective:** make the kit predictable across the Codex app and CLI.

**Stories**

- As a maintainer, I can catch malformed skill metadata and plugin paths before release.
- As a Codex app user, I can discover the plugin and use the included skills.
- As a CLI user, I can use project instructions even when plugin installation is unavailable.

**Tasks**

1. Add lightweight metadata checks for required files, frontmatter, unique names, and in-bundle paths.
2. Run a clean-install and removal walkthrough in both app and CLI.
3. Test instruction precedence in a repository that already has an `AGENTS.md`.
4. Record compatibility results and known platform/version limits.
5. Add release checklist and versioning policy.

**Acceptance criteria**

- Validation fails on missing `SKILL.md`, duplicate skill names, malformed JSON, and paths outside the plugin root.
- Validation does not install or enable the plugin.
- Existing project and user config remain byte-for-byte unchanged during the walkthrough.
- All install paths and rollback steps are documented.

**Exit gate:** compatibility matrix has at least one supported CLI and one supported app build, or clearly labels unsupported paths.

### Sprint 3 — Optional native roles (1 week, only if users ask for them)

**Objective:** add limited delegation support without making it mandatory.

**Candidate roles**

- `explorer`: read-only repository navigation and evidence gathering.
- `reviewer`: read-only correctness/security review.

**Tasks**

1. Confirm current Codex role schema and feature availability.
2. Provide roles as an optional project-local `.codex/agents/` set.
3. Keep role permissions read-only and state that the parent owns edits.
4. Document prerequisites and a no-agent fallback.

**Acceptance criteria**

- Roles use supported configuration fields for the minimum supported Codex version.
- No role executes a mutation, deploy, external post, or credential change.
- Core workflow still works with multi-agent features disabled.

**Gate:** skip this sprint unless Sprint 2 feedback demonstrates a real need for roles.

### Sprint 4 — Release and adoption (3–5 days)

**Objective:** package a stable v1 and collect focused feedback.

**Tasks**

1. Choose repository name and final license/attribution text.
2. Publish a versioned release and checksums for the source archive if needed.
3. Create a short quickstart and contribution guide.
4. Ask 3–5 Codex users to complete the same small coding task with the kit installed and without it.
5. Use findings to decide whether the next increment should be richer skills, optional roles, or an installer.

**Acceptance criteria**

- Fresh install, use, update, and removal instructions are independently reproducible.
- No networked integrations or global hooks are enabled. The optional local learning hook requires trust review and runs only after the session prompt threshold.
- Feedback is captured as actionable issues; no feature is added solely to match upstream volume.

### Sprint 5 — Supervised continuous learning (1 week)

**Objective:** add the source project's most valuable loop in a Codex-native form: experience becomes a reviewed skill that can improve later sessions.

**Tasks**

1. Add a focused `continuous-learning` skill for identifying corrections, error resolutions, workarounds, and project conventions.
2. Add a Codex plugin hook that counts user prompts in plugin data and requests one review after ten prompts.
3. Avoid reading the transcript from the hook; Codex documentation says the transcript format is not a stable hook interface.
4. Require approval of the exact draft before saving to `.agents/skills/learned/<slug>/SKILL.md`; support global scope only when requested.
5. Document plugin hook trust, the optional Python 3 dependency, manual invocation, data handling, and removal.

**Acceptance criteria**

- The hook stores only a per-session count and cleans it up on `SessionEnd`.
- A session gets at most one review nudge, and the `Stop` continuation cannot loop.
- Missing or malformed hook input fails open without interrupting the user's work.
- No learning file is created or changed before the user approves its exact draft.
- The learned skill uses valid frontmatter and resides in a Codex-discoverable location.
- The skill works when the hook is unavailable or not trusted.

**Exit gate:** review the hook definition in Codex and confirm it writes no session content before trusting it.

## Backlog after v1

1. Optional read-only explorer/reviewer roles.
2. A small project-local setup/validation script, only if manual installation causes repeat errors.
3. A separate optional MCP add-on with one integration at a time and explicit setup documentation.
4. Review and prune duplicate or stale learned skills with user approval.
5. Automated compatibility checks against officially documented plugin/agent schemas.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Codex configuration or plugin schema changes | Pin a minimum supported version; validate on each release; keep a no-plugin fallback |
| Instructions conflict with a project's existing `AGENTS.md` | Recommend merging small sections; never replace files in an installer |
| Scope quietly expands into an ECC clone | Five-skill cap for v0.2; require evidence from users for additions |
| Plugin hooks surprise users | Keep one hook local-only, review/trust-gated, and free of prompt or transcript storage |
| Skill guidance becomes stale or too verbose | Assign an owner and review activation criteria during each release |

## Original v1 release acceptance baseline

- The starter kit is installable as a project-local Codex plugin or by copying its skills.
- It supports planning, implementation, review, and verification in a clean project.
- It does not modify user configuration, enable MCPs, install global hooks, or run an installer script.
- Its optional plugin hook only requests a learning review; saved skills require explicit user approval.
- The README provides setup, update, uninstall, limitations, and contribution guidance.
- Metadata checks and both app/CLI walkthroughs are release criteria; the QA snapshot below records the environment-specific coverage actually completed.
- The sprint acceptance criteria and unsupported-version limits are recorded.

## Original v0.1 QA snapshot (2026-10-28)

- Checked with Codex CLI `0.164.0-alpha.11.1` in a disposable `CODEX_HOME` under the workspace.
- Local marketplace discovery and plugin installation succeeded; Codex listed all four bundled `SKILL.md` files.
- The installed bundle had no `.mcp.json` and no `hooks/` directory.
- Plugin and marketplace entries were removed from the disposable Codex config. Plugin cache cleanup returned Windows `Access is denied`; the temporary smoke-test directory remains outside the deliverable.
- The app UI and other Codex versions were not tested.

## v0.2 learning-loop review

- Upstream `continuous-learning` uses a session-end evaluator to prompt review and a `/learn` workflow that asks before saving. Codex Lite adapts that review-and-approval loop to Codex skills and plugin hooks.
- Codex hooks expose `SessionEnd`, `Stop`, and `UserPromptSubmit`; non-managed plugin hooks require user review and trust. The helper relies only on the stable hook event fields and does not parse the transcript.
- The optional nudge requires Python 3. Explicit `$continuous-learning` invocation remains available without hook trust or Python.
- `skill-creator`'s `quick_validate.py` passed for the new skill, all three JSON manifests parsed, and a Python smoke check passed threshold, one-shot, recursion-guard, count-only storage, cleanup, and fail-open scenarios.
- Codex CLI `0.164.0-alpha.11.1` installed plugin v0.2.0 through the local marketplace in a disposable `CODEX_HOME`; `plugin list --json` reported it enabled.
- Live plugin-hook loading and trust approval were not exercised for v0.2; users must review and trust the hook in Codex before it runs.

## References

- [Upstream Everything Claude Code repository](https://github.com/worldflowai/everything-claude-code) — project inspiration and source context.
- [OpenAI Developers: Codex plugins and plugin packaging](https://developers.openai.com/api/docs/guides/agents-api/tools/plugins) — plugin packaging, manifests, bundled skills and MCP format.
- [OpenAI Developers: Skills](https://learn.chatgpt.com/docs/build-skills) — skill format, invocation, and user/project skill locations.
- [OpenAI Docs: Codex hooks](https://developers.openai.com/codex/hooks) — lifecycle events, inputs, transcript limitations, and hook trust.
- [OpenAI Developers: Plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins) — local marketplace file and source path requirements.
- [OpenAI Developers: Codex configuration reference](https://developers.openai.com/codex/config-reference) — Codex settings reference.
- [OpenAI Developers: Codex subagents](https://developers.openai.com/codex/multi-agent) — optional native agent roles and constraints.
