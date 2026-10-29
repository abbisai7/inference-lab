# Change 0008: Keep the README brief

Type: Documentation
Status: Complete

## Summary

The user found the purpose tables too detailed. Replace them with a short project introduction, top-level area bullets, and links to maintained documentation. This supersedes the presentation choice in Change 0007, not the underlying folder structure.

## Requirements and acceptance criteria

- R1 — Brief overview: remove tables, exhaustive file/subfolder explanations, and boxed structure/command listings; keep only short descriptions of major repository areas.
- R2 — Useful entry point: retain accurate scaffold status and links to goals, roadmap, workflow, contribution instructions, and validation guidance.

## Implementation plan

- [x] Rewrite README, update change index/changelog, and check links and whitespace.

## Validation and coverage

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Brief overview | 22-line README; short top-level bullets, no tables/fences | [Self-review and checks](../build-log.md) | Verified |
| R2 — Useful entry point | Accurate status and linked maintained documentation | [Link validation](../build-log.md) | Verified |

## Operational impact

Documentation only; no application, folder, or runtime changes. Reading map and docs index remain applicable. No new ADR or lesson needed.

## Results and learning

`python3 scripts/validate_repo.py` and `git diff --check` passed. Self-review confirmed 22 lines, no tables/code fences, only major-area explanations, accurate scaffold status, and required entry links. Reading map/docs index checked; no update needed. No unit/application tests or independent delegation for this small documentation edit. Branch docs/short-readme is based on current origin/main; commit/push/PR delivery follows these local results, with the actual outcome reported by the task.
