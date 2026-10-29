# Change 0003: Finalize the repository foundation

Type: Documentation
Status: Complete

## Summary

Reconcile the agreed repository structure and spec-driven workflow before application implementation. Keep the full harness, remove PROMPTS.md, create three repository-scoped skills, and document selective multi-agent delivery. Add repeatable structural checks without pretending they establish behavioral correctness.

## Current status

Foundation is complete and verified within its documented scope. The three skills and structural tooling are present; independent review and one isolated planning-procedure forward test completed. Application implementation, deployment, implicit routing, and measured capacity remain future work.

## Requirements and acceptance criteria

- R1 — Consistent structure: remove PROMPTS.md and obsolete active references; preserve historical records and one canonical home per concern.
- R2 — Readable change tracking: requirements have meaningful names and complete behavior, plans have summaries, and completion requires per-requirement evidence.
- R3 — Reusable skills: create harness-author, change-delivery, and workflow-retrospective under .agents/skills/ with focused triggers, usable metadata, and tested boundaries.
- R4 — Selective orchestration: define planning, implementation, testing, validation, context budgets, file ownership, stable snapshots, and single-agent defaults for small work.
- R5 — Clear evidence ownership: build records own requirements/plans and link verification verdicts; the build log owns observed execution evidence; context records material discoveries; reviews record findings.
- R6 — Reproducible validation: document and run structural checks, meaningful validator tests, skill validation, and a fresh review; disclose their limitations.
- R7 — Ready for implementation: update overview, workflow, roadmap, runbooks, changelog, and useful lessons while leaving all application milestones unimplemented.

## Implementation plan

- [x] Reconcile structure, document ownership, context/review guidance, and orchestration.
- [x] Initialize and author the three repository skills with focused trigger descriptions.
- [x] Add and exercise the repository validator and its behavioral tests.
- [x] Independently review the foundation and skill boundaries; address findings.
- [x] Reconcile every requirement, record observed checks, and update indexes/changelog.

## Validation and coverage

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Consistent structure | Root documents, harness, docs and repo skill tree | [Structure/link checks and review](../build-log.md) | Verified |
| R2 — Readable change tracking | Combined template, workflow and completion coverage | [Schema tests and scenario review](../code_review/change-0003-foundation-review.md) | Verified |
| R3 — Reusable skills | Three .agents/skills procedures and generated metadata | [Skill checks, independent scenarios and explicit planning forward test](../build-log.md) | Verified |
| R4 — Selective orchestration | docs/orchestration.md and delivery skill | [Independent scope/ownership review](../code_review/change-0003-foundation-review.md) | Verified |
| R5 — Clear evidence ownership | Workflow, context/review conventions and actual records | [Independent review and material context](../code_review/change-0003-foundation-review.md) | Verified |
| R6 — Reproducible validation | Validator, fixture tests and runbook | [Observed red/green checks and independent rerun](../build-log.md) | Verified |
| R7 — Ready for implementation | README, indexes, runbooks, changelog, lessons | [Final reconciliation and checks](../build-log.md) | Verified |

## Operational impact

Repository-local docs, skills, and validation tooling only. No model downloads, API implementation, runtime dependencies, services, CI, external account changes, commits, or deployments. Restore previous files to undo the change; preserve execution history through correction entries rather than erasing evidence.

## Results and learning

Reconciled the full agreed foundation: no PROMPTS.md, three focused repo skills, bounded orchestration, documented source ownership, readable change records, meaningful structural tests, review and material context. Independent review identified and rechecked a real Markdown-parser completion bypass; regression tests reproduced the failure before the correction. All seven named requirements are reconciled with linked evidence.

Checks validate the foundation only. No application/model service, production deployment, automated CI, schedule, or capacity measurement exists. Implicit routing and end-to-end delivery/retrospective skills remain future usage validation, explicitly outside the foundation acceptance scope. Local source is uncommitted. No application phase was automatically started.

## Execution and review references

See [build log](../build-log.md). See [review and forward-test results](../code_review/change-0003-foundation-review.md), [reviewed source hashes](../code_review/change-0003-snapshot.json), and [material context](../context/change-0003-foundation-context.md).
