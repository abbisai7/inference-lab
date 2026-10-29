# ADR-0001: Spec-driven development

Status: Superseded by [ADR-0002](0002-unified-change-records.md)

Date: 2026-10-29

Links: [documentation foundation plan](../../harness/build/0001-documentation-foundation.md)

This record preserves the original decision. The combined change workflow in ADR-0002 is current.

## Context

The project is a learning lab with staged product, infrastructure, and operational work. The user requested vision, ADRs, plans, experiments, runbooks, changelog updates, and recorded lessons, with focused agent guidance.

## Decision

Use docs/ as the documentation source of truth, indexed by docs/README.md. Define behavior in specs before implementation, create a plan for each change, and record consequential decisions in ADRs. Record completed changes in the root changelog, empirical evidence in experiments, reusable gotchas in lessons, and verified operating procedures in runbooks. Keep AGENTS.md focused on navigation and working practices.

Scale the process to the change: a short maintenance plan is enough for small documentation fixes; a separate feature spec or ADR is not required for every edit. Distinguish intended behavior from verified functionality.

## Alternatives

A single large agent document mixes contributor instructions with changing product requirements. Implementation-first development makes acceptance criteria and learning evidence harder to recover. Neither supports the requested workflow as clearly.

## Consequences

Changes have traceable intent and evidence, with some documentation upkeep. Cross-link authoritative documents to limit duplication. No new approval gate is introduced by this process.
