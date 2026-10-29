# Build and change records

Requirements and implementation plans stay together in one readable document per bounded phase or change. Use [the template](template.md) and [workflow](../../docs/workflow.md). Start with a summary and named requirements; identifiers supplement the wording rather than replace it.

| Record | Type | Status |
| --- | --- | --- |
| [Original documentation foundation](0001-documentation-foundation.md) | Documentation | Complete |
| [Unified change workflow](0002-unified-change-workflow.md) | Documentation | Complete |
| [Phase 00: Harness adoption](phase-00-harness-adoption.md) | Documentation | Complete |
| [Foundation finalization](change-0003-finalize-foundation.md) | Documentation | Complete |
| [Concise agent guidance](change-0004-concise-agent-guidance.md) | Documentation | Complete |
| [Reading-map maintenance](change-0005-maintain-reading-map.md) | Documentation | Complete |
| [PR-only workflow](change-0006-pr-only-workflow.md) | Documentation | Complete |
| [README repository guide](change-0007-readme-repository-guide.md) | Documentation | Complete |
| [Short README](change-0008-short-readme.md) | Documentation | Complete |

[PLANS.md](../../PLANS.md) owns phase sequencing. Future phases get detailed records when they are planned. Keep legacy record names for history; new phase files use `phase-NN-description.md` and maintenance uses `change-NNNN-description.md`. Keep filenames unique and cross-link dependencies. This directory supports features, bugs, refactors, infrastructure, deployments, and documentation, not only initial development.

Observed execution evidence belongs in the build log; build records link it from coverage rows. Legacy records retain original wording/history. Current records use named requirements and the combined template.
