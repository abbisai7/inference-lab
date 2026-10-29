# CHG-0002: Unified change workflow

Type: Documentation
Status: Complete

## Summary

Combine requirements and implementation plans in one document per change. Explain the full contributor workflow and introduce criterion-level evidence and a completion review to make omissions visible. This changes documentation only; no application or deployment is delivered.

## Requirements and acceptance criteria

- AC-01: One changes directory supports features, bugs, refactors, infrastructure, deployments, and documentation, with no separate specs/plans directories.
- AC-02: A human-readable template starts with a short summary and contains requirements, implementation, verification, operational impact, and results.
- AC-03: The workflow explains feature development, bug fixing, testing, deployment, experiments, and how to present the approach.
- AC-04: Stable acceptance IDs, coverage tracking, checkpoints, scope changes, and completion reconciliation are documented in contributor instructions.
- AC-05: Existing history is preserved, local links resolve, and unimplemented capabilities remain clearly marked.

## Implementation plan

- [x] Consolidate spec and plan templates and migrate the foundation record.
- [x] Add workflow documentation, examples, a contributor reading path, and a presentation explanation.
- [x] Update agent guidance, indexes, roadmap, runbooks, ADRs, lessons, and changelog.
- [x] Verify links, document structure, migration, coverage, and final scope; record evidence.

## Validation and coverage

| Criterion | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| AC-01 | changes directory and migrated foundation record | Python assertions confirmed consolidation, historical record, and absent old directories | Verified |
| AC-02 | changes/template.md | Checked summary and all combined template sections | Verified |
| AC-03 | workflow.md and runbook entry points | Checked feature, bug, testing, deployment, experiment, and presentation sections; README contains full tree | Verified |
| AC-04 | workflow.md and AGENTS.md | Checked criterion statuses; reviewed checkpoint, scope-change, and completion instructions | Verified |
| AC-05 | ADR history, updated references, honest runbooks | 20 Markdown files and 59 local links checked; no stale directory paths; reviewed supersession and scaffold status | Verified |

## Operational impact

No runtime changes, migrations, or deployment. Source changes remain local and uncommitted. Rollback would restore the previous docs layout and references.

## Results and learning

2026-10-29: Consolidated records, added the workflow and complete repository tree, and updated contributor instructions and related docs. A Python documentation check walked all root/docs Markdown files, resolved relative links, checked required sections and migrated paths, and verified ADR statuses. It passed for 20 Markdown files and 59 local links. Final review reconciled AC-01 through AC-05 with the changed documents and verified there are no unfinished steps.

No application tests or benchmarks apply to this documentation-only change. Source is local and uncommitted, so no commit revision is available. Completion gates are documented manual practices, not automated enforcement; the checks establish document structure and references, not runtime correctness or absence of future omissions. See CHANGELOG.md and the 2026-10-29 evidence-tracking entry in docs/lessons.md.
