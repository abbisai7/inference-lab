# Change 0004: Concise agent guidance

Type: Documentation
Status: Complete

## Summary

Keep AGENTS.md short and useful as always-available guidance. Add task-based reading instructions and explicit protection for project-specific contracts, while linking detailed procedures instead of duplicating them. No application behavior changes.

## Current status

Updated and self-reviewed. AGENTS.md is 74 readable lines and 524 words, with explicit reading conditions, contract-preservation rules, verified commands, and scoped completion/deployment guidance.

## Requirements and acceptance criteria

- R1 — Concise navigation: AGENTS.md stays below the agreed approximate 80–100-line ceiling without hiding excessive text in long lines, and retains purpose, structure, change rules, checks, and deployment pointers.
- R2 — Preserve project contracts: tell agents when to inspect applicable API/downstream constraints and tests, preserve compatibility, and investigate disagreements instead of silently normalizing unfamiliar behavior.
- R3 — Selective knowledge: link detailed workflow/architecture/operations, clarify that references require reading, and keep required knowledge in checked-in docs rather than adding MEMORY.md.

## Implementation plan

- [x] Rewrite AGENTS.md with concise sections and a task-to-reading map.
- [x] Update index, changelog, and observed execution evidence.
- [x] Check links, length, preserved rules, and requirement coverage before completion.

## Validation and coverage

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Concise navigation | AGENTS.md sections, commands, and links | [Observed checks and self-review](../build-log.md) | Verified |
| R2 — Preserve project contracts | Task-reading table and compatibility/inconsistency rules | [Observed checks and self-review](../build-log.md) | Verified |
| R3 — Selective knowledge | Conditional documentation links and checked-in knowledge guidance | [Observed checks and self-review](../build-log.md) | Verified |

## Operational impact

Documentation only; no application, runtime configuration, deployment, or skill changes. Existing historical review snapshots remain historical and are not rewritten.

## Results and learning

Verified local links with `python3 scripts/validate_repo.py`; checked length with `wc -l -w -c AGENTS.md` (74 lines, 524 words, 4347 bytes). Self-review confirmed the previous essential workflow, skill/orchestration, evidence, test, security, resource and deployment rules remain present or linked. The new rules explicitly require relevant contracts and consumer/tests before compatibility changes and investigation of discrepancies. No contract behavior was invented and no MEMORY.md or separate AGENT.md was created. No unit/application tests were run because this is a guidance-only edit. Existing review hashes intentionally identify the older foundation snapshot, not this later document change.

## Execution and review references

See [build log](../build-log.md). This small change uses self-review, not independent delegation.
