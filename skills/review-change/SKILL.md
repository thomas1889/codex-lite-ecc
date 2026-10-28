---
name: review-change
description: Review a code diff for concrete correctness, security, compatibility, and test-coverage problems. Use after implementation or when asked to review a change.
---

# Review a change

1. Read the complete diff and enough surrounding code to understand the affected behavior.
2. Prioritize actionable defects: incorrect behavior, regressions, unsafe input handling, data loss, permission mistakes, and missing critical tests.
3. Trace each suspected issue to a specific changed line and a concrete failure scenario.
4. Do not report style preferences as defects. Do not assume a bug without evidence.
5. Report findings first, ordered by severity, with file and line references. If there are no findings, say so and mention unverified risks or checks.
