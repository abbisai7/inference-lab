# Lessons and gotchas

Keep reusable findings concise and evidence-linked. An observation is not a universal rule; include the environment and limits where relevant. Operational procedures belong in runbooks and architectural decisions in ADRs.

## 2026-10-29 — One canonical agent instruction file

Use a single AGENTS.md for contributor/agent instructions. A separate AGENT.md plus a forwarding AGENTS.md added unnecessary duplication during scaffolding. Detailed product/design requirements now live in docs/ and are linked from the agent guide. See the original [ADR-0001](decisions/0001-spec-driven-development.md), now superseded by [ADR-0002](decisions/0002-unified-change-records.md).

## Future entry format

Date and title; observed behavior; cause if established; practical action; evidence/spec/experiment link; limits or unresolved questions. Do not record hypothetical experiments as completed findings.

## 2026-10-29 — A plan needs explicit evidence tracking

The user reported professional experience of agents missing planned details. We adopted stable acceptance IDs, coverage rows, checkpoints, and a final reconciliation review to expose omissions. This is a process decision, not measured proof that omissions have been eliminated. See [CHG-0002](../harness/build/0002-unified-change-workflow.md).

## 2026-10-29 — Names and ownership matter more than extra files

The user found acceptance IDs alone unclear and requested the published harness layout. Pair reference IDs with descriptive names and complete behavior; explain status in plain language. Assign each document one authoritative purpose and move content instead of maintaining parallel copies. These are adopted working practices, not measured improvements in delivery speed or correctness. See [ADR-0003](decisions/0003-repository-harness.md).

## 2026-10-29 — Context preserves reasoning, not routine progress

Our early guidance reduced context to handoffs. The cookbook discussion clarified that material discoveries, constraints, rationale, and unresolved questions deserve phase context, while routine progress belongs in the build log. Current instructions separate them and retain historical records. This correction is not proof that future omissions are eliminated.
