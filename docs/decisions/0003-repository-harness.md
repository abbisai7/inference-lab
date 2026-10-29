# ADR-0003: Adopt the repository harness layout

Status: Accepted
Date: 2026-10-29
Amends: [ADR-0002](0002-unified-change-records.md)
Links: [Phase 00](../../harness/build/phase-00-harness-adoption.md)

Current ownership is amended by [ADR-0004](0004-final-foundation-and-skills.md): PROMPTS.md is removed and repo-scoped skills provide reusable procedures.

## Context

The user requested the GOALS.md, PLANS.md, PROMPTS.md and harness structure illustrated in OpenAI workflow guidance, and asked whether it can scale. Existing combined change records and durable operational documentation must remain useful. IDs alone were not understandable to new readers.

## Decision

Adopt root direction, phase index, reusable requests, and harness/build/, build-log.md, code_review/, and context/. Move existing combined records into harness/build/ and retain their names as history. Keep requirements and plans together as ADR-0002 specified; only their home changes. Move vision and roadmap to GOALS.md and PLANS.md instead of maintaining copies. Keep durable architecture, ADRs, experiments, runbooks, and lessons under docs/.

Require descriptive requirement names, full expected behavior, and plain-language status summaries. Bound phases, split large work into linked records, and archive long logs by phase when needed. Use the published example as adaptable guidance, not as a mandatory platform format.

## Alternatives and consequences

Keeping both old and new direction/plan folders would create drift. Replacing all docs with the harness would lose the distinction between execution records and durable system knowledge. This migration preserves that distinction. Root indexes and shared logs still require coordination for multiple contributors. The layout does not enforce correctness, prove runtime capacity, or establish CI/review automation.
