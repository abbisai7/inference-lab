# Changelog

Record completed repository changes under Unreleased. Link their change record and relevant decisions. Move entries into a dated release section when a release actually occurs.

## Unreleased

### Added

- Initial repository scaffold for backend, frontend, infrastructure, scripts, tests, and documentation.
- Spec-driven documentation workflow with vision, roadmap, spec/plan/ADR templates, architecture requirements, experiment template, lessons log, and runbook skeletons. See [documentation foundation plan](harness/build/0001-documentation-foundation.md).

### Changed

- Consolidated contributor guidance into `AGENTS.md` and focused it on repository navigation, implementation workflow, verification, and deployment expectations.

- Combined specifications and plans under docs/changes/ for all change types, with summaries, acceptance coverage, checkpoint guidance, and a final reconciliation gate. Added the contributor workflow and presentation explanation; preserved ADR history. See [CHG-0002](harness/build/0002-unified-change-workflow.md).

- Adopted root goals, phase index, reusable prompts, and a repository harness with migrated build records, execution log, review/context guidance, and plain-language requirements. See [Phase 00](harness/build/phase-00-harness-adoption.md).

- Finalized the foundation without PROMPTS.md; added three repository-scoped skills, selective orchestration, clarified context/review and evidence ownership, and a standard-library structural validator with fixture tests. Application implementation remains deferred. See [Change 0003](harness/build/change-0003-finalize-foundation.md).

- Shortened and reorganized AGENTS.md with task-based reading, project-contract compatibility rules, and checked-in knowledge guidance. See [Change 0004](harness/build/change-0004-concise-agent-guidance.md).

- Made reading-map maintenance part of affected change completion and phase retrospectives, including link relevance and documentation-index updates. See [Change 0005](harness/build/change-0005-maintain-reading-map.md).

- Documented the initial-main bootstrap exception followed by mandatory topic branches and PRs, main-protection settings, fresh-context review/fix/re-review, and a PR template. See [Change 0006](harness/build/change-0006-pr-only-workflow.md).
