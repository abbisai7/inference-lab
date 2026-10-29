# Change 0005: Keep the reading map current

Type: Documentation
Status: Complete

## Summary

Maintain the AGENTS.md reading map when documentation or system boundaries change, and audit it at phase retrospectives. Refresh links and relevance without adding a background schedule or loading all history.

## Requirements and acceptance criteria

- R1 — Change-driven maintenance: change completion checks the reading map and docs index whenever contracts, components, commands, or document locations change.
- R2 — Phase-level review: retrospectives check the map for stale or missing guidance while retaining their read-only assessment boundary; links and skill structure remain valid.

## Implementation plan

- [x] Add concise maintenance instructions and delivery/retrospective checks.
- [x] Validate links, skill structure, and AGENTS.md length; record results.

## Validation and coverage

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Change-driven maintenance | AGENTS.md, workflow, delivery skill | [Observed checks and self-review](../build-log.md) | Verified |
| R2 — Phase-level review | Retrospective skill and workflow | [Observed checks and self-review](../build-log.md) | Verified |

## Operational impact

Instruction-only edits; no scheduler, application, or deployment changes.

## Results and learning

Self-review confirmed update triggers, index maintenance, semantic relevance checks, and the retrospective read-only boundary. Repository validation passed; both edited skills passed bundled quick validation. AGENTS.md remains 78 lines. No app/unit tests or independent delegation were needed for this narrow instruction edit. Reading map checked: current links remain appropriate, so no routing-table entries changed. Structural links cannot prove that a reading map remains semantically relevant; completion review and retrospectives must inspect that explicitly.
