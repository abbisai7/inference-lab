# CHG-0001: Documentation foundation

Type: Documentation
Status: Complete

## Summary

Established the initial documentation foundation before application work. This historical record used separate specs and plans; [CHG-0002](0002-unified-change-workflow.md) migrates it to the unified workflow. Completion and verification below refer to the original documentation work.

## Outcome and approach

Separate product direction, feature behavior, implementation plans, architectural decisions, measurements, operations, and reusable lessons. Keep AGENTS.md focused on repository navigation and the change workflow.

## Steps

1. Capture the agreed vision, roadmap, and existing architecture requirements.
2. Add spec, plan, ADR, and experiment templates with explicit status/evidence fields.
3. Add a documentation index, lessons log, honest runbook skeletons, and changelog.
4. Update AGENTS.md and README; verify links, required files, and scaffold status statements.

## Validation and completion

Completion requires all described documents, valid local Markdown file links, preserved existing design constraints, and no invented application commands or experiment results.

## Operational impact

Documentation only. No services, dependencies, deployments, data migrations, or runtime behavior change. Rollback consists of reverting this documentation change.

## Results and documentation

Established the documentation workflow and migrated detailed architecture guidance out of AGENTS.md. A local documentation check verified relative Markdown links, required documents, and removal of populated-directory placeholders. No application tests apply to this documentation-only change. See CHANGELOG.md and docs/lessons.md.

## Historical acceptance coverage

| Criterion | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| AC-01: Establish the documentation foundation | Initial docs, templates, and contributor guide | Original recorded check: 17 Markdown files and 30 local links passed; no runtime changes | Verified |

The criterion ID and this coverage row were added during migration; they do not imply a new execution of historical checks. See CHG-0002 for verification of the migrated layout.
