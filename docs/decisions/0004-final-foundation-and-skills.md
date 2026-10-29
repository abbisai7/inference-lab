# ADR-0004: Final foundation, skills, and selective orchestration

Status: Accepted
Date: 2026-10-29
Amends: [ADR-0003](0003-repository-harness.md)
Links: [Foundation finalization](../../harness/build/change-0003-finalize-foundation.md)

## Context

The user finalized the full harness without PROMPTS.md, requested readable requirements and per-requirement verification, clarified the material purpose of context/review, and proposed skills plus selective multi-agent delivery to reduce repeated prompting and context noise.

## Decision

Keep GOALS.md, PLANS.md, AGENTS.md, README.md and CHANGELOG.md at root. Keep combined build records, observed build log, review findings, and material context in harness/. Keep durable architecture, decisions, experiments, runbooks, lessons and process explanation in docs/. Remove PROMPTS.md; repository-scoped skills package reusable procedures.

Create three focused skills: harness-author for planning; change-delivery for bounded implementation/orchestration; workflow-retrospective for read-only evidence-backed assessment before authorized improvements. Skills guide behavior; a standard-library validator checks file links and completion coverage mechanically. It cannot establish evidence truth or application correctness.

Use small-context assignments and explicit file ownership. Delegate substantive independent tasks selectively, retaining a single orchestrator for scope/status/evidence reconciliation. Testing and review examine identified snapshots, fixes invalidate affected results, and small changes default to one agent. Do not configure new global agents, models, CI, or schedules in the foundation change.

## Alternatives and consequences

One always-growing chat and all-repo context cause unnecessary repetition. Mandatory agents for every task increase cost and coordination. Dropping all logs/context makes reasoning and evidence hard to recover. The chosen approach keeps bounded execution with durable knowledge. Actual usage, implicit skill routing, model capacity, and production readiness still require measurement; directory structure guarantees none of them.
