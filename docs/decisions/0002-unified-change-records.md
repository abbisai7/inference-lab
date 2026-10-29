# ADR-0002: Combine specifications and implementation plans

Status: Accepted
Date: 2026-10-29
Supersedes: [ADR-0001](0001-spec-driven-development.md)
Links: [CHG-0002](../../harness/build/0002-unified-change-workflow.md)

Document locations are amended by [ADR-0003](0003-repository-harness.md); combined requirements and plans remain the approach.

## Context

Separate specs and plans add navigation overhead for a project where one person often owns requirements and implementation. Feature-only naming excludes bugs, infrastructure, and deployment work. The user also identified that an agent can miss planned requirements even when a plan exists.

## Decision

Use one numbered document per change in docs/changes/, with a short summary, requirements and acceptance IDs, implementation steps, verification coverage, operational impact, and results. Apply the same lifecycle to all change types with proportional detail. Keep docs/workflow.md as the human explanation and AGENTS.md as concise contributor instructions.

Require criterion-level evidence and an explicit final reconciliation before marking Complete. Record checkpoints for long work and make omissions visible. Preserve separate ADRs, experiments, architecture, runbooks, lessons, and changelog because they serve different durable purposes.

## Alternatives

Separate spec and plan files suit larger multi-team work but are unnecessary overhead here. Feature-only records exclude maintenance work. A single checklist without evidence does not establish that required behavior was verified.

## Consequences

One reading path supports quick summaries and implementation detail. Manual review and honest evidence remain necessary; document structure does not guarantee correctness. Split large changes into linked records. Superseded ADRs remain historical records, and no new mandatory approval ceremony is introduced.
