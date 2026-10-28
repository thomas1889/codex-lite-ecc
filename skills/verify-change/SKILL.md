---
name: verify-change
description: Choose and run proportionate checks for a code change, then report the actual results. Use before handing off non-trivial implementation work or when asked to verify.
---

# Verify a change

1. Inspect project scripts and instructions to find the checks relevant to the changed files and behavior.
2. Prefer focused tests first, then required type checks, lint, build, or broader tests as appropriate.
3. Do not run destructive, expensive, networked, or production-targeting checks without authorization.
4. Capture the exact pass/fail outcome. If blocked, state the missing prerequisite or failure.
5. Review the diff after checks to catch generated files or unintended edits.
6. Report commands/checks run, results, and checks not run. Never imply verification that did not happen.
