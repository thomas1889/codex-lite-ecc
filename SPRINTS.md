# Codex Lite: a small, Codex-native development toolkit

**Purpose:** define and build a focused, low-maintenance alternative to the Everything Claude Code toolkit, designed for Codex from day one.

**Status:** implementation-ready proposal. This sprint plan is included in the Codex Lite repository so it travels with the starter kit.

## Product definition

Codex Lite packages a small set of reusable development instructions and skills around Codex's native project conventions. It should help a developer plan a change, implement it safely, review it, and verify it without making the user's Codex environment noisy or changing their tool permissions.

The repository linked for this project is a Claude Code toolkit. Its checked-out snapshot (revision `432485b`, fetched 2026-10-28) contains 81 tracked files, including 11 skill folders, 9 agent prompts, 15 slash-command files, 5 hook files, 8 rule files, 8 runtime/setup scripts, and 1 MCP configuration. These are inventory counts, not one-to-one capability comparisons. Codex Lite uses the same broad workflow idea but implements it with Codex-native files and a much smaller opt-in surface. It is an independent, MIT-licensed implementation inspired by general workflows; it does not copy upstream files or imply endorsement.

## Goals and non-goals

### Goals

- Work in a Codex project using `AGENTS.md`, portable `SKILL.md` files, and optional Codex plugin packaging.
- Ship a tiny starter bundle with clear instructions and four focused skills: planning, implementation discipline, review, and verification.
- Preserve existing user and project configuration.
- Make integrations, multi-agent roles, and any automation opt-in and independently reviewable.
- Support use by copying the starter into a repo, using its skills as a plugin, or selectively copying skills into `.agents/skills/`.

### Non-goals for v1

- Recreating hundreds of upstream skills, commands, or specialized agents.
- Enabling MCP servers, hooks, scheduled jobs, or multi-agent execution by default.
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
│   └── verify-change/SKILL.md
└── .codex/
    └── agents/                  # optional read-only roles, added in a later sprint
```

The starter kit contains `AGENTS.md`, `README.md`, `SPRINTS.md`, a marketplace catalog, a plugin manifest, a license, and four skill definitions. It intentionally has no MCP manifest, hook manifest, shell installer, or agent role. These can be evaluated later behind explicit, separate decisions.

## Product decisions

| Topic | v1 decision | Reason |
|---|---|---|
| Primary host | Codex CLI and Codex app | Use Codex-native instructions, skills, plugin format, and project agent files |
| Baseline | `AGENTS.md` | No plugin is required for project guidance |
| Skills | Four small workflow skills | Covers the end-to-end coding loop without a huge catalog |
| Plugin | Optional, skills-only | Installs as one unit without MCP or hooks |
| MCP | None by default | External services add access, configuration, and maintenance overhead |
| Hooks | None in v1 | Avoid surprise execution and approval burden |
| Agents | Deferred | Native roles can be added after validating useful read-only cases |
| Installer | Manual copy first | Simple, auditable, and reversible; automation only after install paths are validated |
| User config | Never edited by default | Prevent accidental changes to global Codex settings |
| Tests | Validate metadata and file layout, plus human workflow checks | No runtime code exists in the initial scope |

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
- As a developer, I can opt into a single skills-only plugin instead of copying files.
- As a user with local conventions, my existing instructions remain authoritative.

**Tasks**

1. Refine `AGENTS.md` to state scope, plan-before-complex-work, focused edits, evidence-based review, and honest verification.
2. Complete the four skill definitions and add one short example each.
3. Add plugin metadata with skills only; leave MCP and hooks absent.
4. Document project-local copy and global selective-copy install methods.
5. Add a non-destructive update/uninstall procedure.

**Acceptance criteria**

- Each skill is one workflow, has a clear trigger, and fits within a short read.
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
- No default networked integrations or automatic hooks are present.
- Feedback is captured as actionable issues; no feature is added solely to match upstream volume.

## Backlog after v1

1. Optional read-only explorer/reviewer roles.
2. A small project-local setup/validation script, only if manual installation causes repeat errors.
3. A separate optional MCP add-on with one integration at a time and explicit setup documentation.
4. A curated skill index generated from actual user demand.
5. Automated compatibility checks against officially documented plugin/agent schemas.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Codex configuration or plugin schema changes | Pin a minimum supported version; validate on each release; keep a no-plugin fallback |
| Instructions conflict with a project's existing `AGENTS.md` | Recommend merging small sections; never replace files in an installer |
| Scope quietly expands into an ECC clone | Four-skill cap for v1; require evidence from users for additions |
| Plugin metadata encourages unsafe defaults | Skills-only manifest; test that no MCP/hooks/config mutations are included |
| Skill guidance becomes stale or too verbose | Assign an owner and review activation criteria during each release |

## Definition of done for v1

- The starter kit is installable as a project-local Codex plugin or by copying its skills.
- It supports planning, implementation, review, and verification in a clean project.
- It does not modify user configuration, enable MCPs, install hooks, or run an installer script.
- The README provides setup, update, uninstall, limitations, and contribution guidance.
- Metadata checks and app/CLI walkthroughs pass.
- The sprint acceptance criteria and unsupported-version limits are recorded.

## QA snapshot (2026-10-28)

- Checked with Codex CLI `0.164.0-alpha.11.1` in a disposable `CODEX_HOME` under the workspace.
- Local marketplace discovery and plugin installation succeeded; Codex listed all four bundled `SKILL.md` files.
- The installed bundle had no `.mcp.json` and no `hooks/` directory.
- Plugin and marketplace entries were removed from the disposable Codex config. Plugin cache cleanup returned Windows `Access is denied`; the temporary smoke-test directory remains outside the deliverable.
- The app UI and other Codex versions were not tested.

## References

- [Upstream Everything Claude Code repository](https://github.com/worldflowai/everything-claude-code) — project inspiration and source context.
- [OpenAI Developers: Codex plugins and plugin packaging](https://developers.openai.com/api/docs/guides/agents-api/tools/plugins) — plugin packaging, manifests, bundled skills and MCP format.
- [OpenAI Developers: Skills](https://learn.chatgpt.com/docs/build-skills) — skill format, invocation, and user/project skill locations.
- [OpenAI Developers: Plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins) — local marketplace file and source path requirements.
- [OpenAI Developers: Codex configuration reference](https://developers.openai.com/codex/config-reference) — Codex settings reference.
- [OpenAI Developers: Codex subagents](https://developers.openai.com/codex/multi-agent) — optional native agent roles and constraints.
