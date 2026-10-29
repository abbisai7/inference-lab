# Phase 00: Adopt the repository harness

Type: Documentation
Status: Complete

## Summary

Adopt the requested root GOALS.md, PLANS.md, PROMPTS.md and harness layout while preserving application folders and durable system documentation. Keep requirements and implementation together in each build record. Make reports understandable through descriptive requirements and plain-language status explanations.

## Current status

Documentation migration is verified and complete. The next application phase has not started. No application, CI, inference service, or deployment has been implemented.

## Requirements and acceptance criteria

- R1 — Clear document ownership: direction lives in GOALS.md, the phase index in PLANS.md, reusable requests in PROMPTS.md, and detailed change records in harness/build/.
- R2 — Preserve history and guidance: migrate existing records, goals, and roadmap without losing requirements; preserve architecture, decisions, experiments, runbooks, and lessons under docs/.
- R3 — Understandable reporting: requirements have descriptive names and complete sentences, with IDs used only as reference keys; explain what each status means.
- R4 — Support growth: define bounded phases, small follow-up changes, append-only evidence, context handoffs, review records, and log archival without duplicate sources of truth.
- R5 — Verified migration: local links resolve, indexes agree, and descriptions distinguish scaffolding from working application capabilities.

## Implementation plan

- [x] Move direction and roadmap to root documents; migrate change records to harness/build/ and repair links.
- [x] Add reusable prompts, build log, context/review guidance, and source-of-truth rules.
- [x] Update templates, workflow, agent instructions, README, ADRs, lessons, and changelog.
- [x] Check all requirements and links; record observed results and reconcile completion.

## Validation and coverage

| Requirement | Implementation | Evidence | Status |
| --- | --- | --- | --- |
| R1 — Clear document ownership | Root direction/index/prompts and harness/build records | Required-file and migrated-source checks passed; ownership sections reviewed | Verified |
| R2 — Preserve history and guidance | Migrated historical records and durable docs/ | Both historical records and architecture/experiments/runbooks/lessons verified present; local links checked | Verified |
| R3 — Understandable reporting | Named requirements, status summary, and template explanations | Required template sections checked; descriptive examples and status meanings reviewed | Verified |
| R4 — Support growth | PLANS.md, workflow, build-log, review/context guidance | Reviewed bounded phase/maintenance naming, phase splitting, log archival, and source-of-truth rules | Verified |
| R5 — Verified migration | Updated indexes, references, README, ADRs and changelog | Python final structural/link check passed: 26 Markdown files and 86 local links; no duplicate direction/plan folders | Verified |

## Operational impact

Documentation only; no dependencies, services, migrations, infrastructure, or public access changes. Files remain local and uncommitted. Rollback would restore the previous document locations and links.

## Results and learning

2026-10-29: Completed the harness adoption and reconciled all five named requirements. A Python check enumerated root/docs/harness Markdown, resolved 85 relative links across 26 files, checked required root/harness documents and retained history, confirmed old direction/plan paths were removed, and checked human-readable template and workflow sections. Reviewed operational claims and corrected a stale link label found during the scan. No application tests, benchmarks, code reviews, or deployments ran.

Completion is documentation-only and manually reviewed. No revision exists because the repository is uncommitted. The layout does not establish runtime scalability or automatically enforce completion. See ADR-0003, the changelog, and the build log for ownership and evidence details.

Final revalidation passed with 86 links after adding the completion-log reference. The check script initially included the coverage-table header in its requirement count; it was corrected and rerun successfully.
