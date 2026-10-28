---
name: implement-change
description: Implement a focused code change using the repository's existing architecture and conventions. Use after requirements are clear, especially for feature work or bug fixes.
---

# Implement a change

1. Read the applicable project instructions and the code that owns the behavior.
2. For behavior changes, identify or add a focused regression test using the project's existing test framework.
3. Make the smallest coherent implementation that satisfies the request.
4. Preserve existing APIs and configuration unless the requested behavior requires a change.
5. Avoid unrelated cleanup, speculative abstractions, and new dependencies.
6. Inspect the final diff. Summarize behavior changed and any relevant checks or limitations.
