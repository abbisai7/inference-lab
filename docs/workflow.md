# How we develop and deliver changes

## Explain our approach

“We define expected behavior before implementation and keep it with the implementation plan in one readable change record. We deliver small pieces, verify each named requirement, and record what actually happened. For substantive work, we selectively delegate planning, implementation, testing, and review with focused context. Before closing a change, we reconcile all requirements against evidence and update operating documentation. Retrospectives improve the process using observed failures, not additional paperwork by default.”

This describes the agreed process. The repository has a scaffold, workflow skills, and structural validation tooling; no working chat application, deployed services, or CI exists.

## Where information belongs

| Source | Owns |
| --- | --- |
| [GOALS.md](../GOALS.md) | Purpose, users, outcomes, constraints, exclusions |
| [PLANS.md](../PLANS.md) | Planned phase sequence and links; status shown there is a summary |
| [AGENTS.md](../AGENTS.md) | Persistent repository rules and verified commands |
| [Build records](../harness/build/README.md) | Scope, named requirements, implementation plan, planned checks, and a coverage verdict linked to evidence |
| [Build log](../harness/build-log.md) | Observed implementation progress, verification results, and append-only event history |
| [Context](../harness/context/README.md) | Material discoveries, clarifications, constraints, rationale, unresolved questions |
| [Reviews](../harness/code_review/README.md) | Review scope, detailed findings, resolution, and review verdict |
| Architecture and ADRs | Durable system explanation and consequential design rationale |
| Experiments and runbooks | Measured investigations and repeatable operating procedures |
| [Lessons](lessons.md) and [changelog](../CHANGELOG.md) | Reusable findings and concise completed-change summaries |

The harness is the supporting structure for executing development. Docs explain the system and its practices beyond one change. Link authoritative sources instead of copying plans or evidence into multiple locations. Context is not a progress log or merely a disposable handoff. Durable architectural decisions belong in ADRs; context links them and preserves phase-specific reasoning.

## One readable record per change

Use [the template](../harness/build/template.md) for features, bugs, refactors, infrastructure, deployments, and documentation. The first sections are Summary and Current status, readable without implementation details. Then define requirements, optional investigation, concrete implementation steps, validation coverage, operational impact, and results.

Pair IDs with names and complete behavior: “R1 — Keep conversations private: a signed-in user can access only conversations they own.” Reports use names and explain what remains; avoid unexplained abbreviations or percentages.

The PM and developer may write different sections, but the workflow does not require two people or separate spec/plan files. A small fix may need only a short record. Split growing phases into linked independently verifiable changes.

## Lifecycle and completion

Draft → Ready → In progress → Complete; Superseded links a replacement. Ready means blocking requirements are resolved, not that extra approval is required. Record blockers explicitly. Completing code does not imply deployment unless deployment is part of the acceptance criteria.

1. Follow the [branch-and-PR workflow](runbooks/contributing.md): after the initial-main bootstrap, create/use a topic branch before editing. Inspect relevant code and prior decisions; do not read every document by default.
2. Define expected outcomes, exclusions, named requirements, failure behavior, and meaningful acceptance checks.
3. Plan the implementation, dependencies, tests, and operational implications. Add an ADR only for a significant choice.
4. Implement within scope; record material progress and executed checks in the build log. Capture context discoveries when they affect later work.
5. Verify each requirement. A test file existing is not evidence it ran; a passing suite does not establish complete requirement coverage.
6. Review the actual code and evidence. Resolve findings or document explicitly accepted limitations without contradicting requirements.
7. Reconcile the whole record, update the roadmap/index summaries, changelog and affected docs, then mark Complete only when every current requirement is Verified and all steps are finished or explicitly reconciled with agreed scope. Commit/push the topic branch and open a PR to main. Implementation completion is separate from PR merge and deployment; merge only with explicit user authorization.

Coverage states: Pending (not established), Implemented (written but not verified), Verified (relevant checks passed), Blocked (a stated obstacle). Verified verdicts link an observed passing check or concrete manual procedure/result. Pending, Implemented, and Blocked rows state missing evidence and blockers explicitly; do not invent checks to populate the table. Significant scope changes require user agreement. Keep deferred requirements visible or explicitly agree to remove them with linked follow-up work.

## Features and bugs

Feature example: users see an answer progressively; cancellation stops model work and frees capacity; ownership checks protect conversations when identity is in scope. These are examples, not implemented capabilities. Specify and verify them independently.

For a bug, link the existing expected behavior, reproduce actual behavior where possible, and distinguish hypotheses from established causes. Establish a failing regression check where meaningful, apply a bounded fix, and verify the correction and affected behavior. If reproduction is unavailable, disclose the alternative evidence and limits. Do not change requirements merely to fit the current implementation.

## Testing, deployment, and experiments

Choose checks from behavior: unit tests for isolated rules; integration tests for API/auth/persistence/streaming; controlled load tests for capacity; failure/recovery tests for reliability. Fake inference isolates API overhead from model capacity. Report errors/rejections with latency and throughput; distinguish first generated token from headers and full stream completion.

Deployment needs a selected revision/environment, configuration and exposure, migration compatibility, smoke checks and telemetry, abort conditions, rollback and restoration procedures. The deployment runbook is still planned. Only claim procedures verified after actually exercising them in the intended environment.

Experiments start with a question, stated workload/configuration, and cleanup/recovery plan. Record measurements separately from interpretation, confounders, and limitations. Failed/inconclusive experiments are useful. The Mac's inference capacity and a possible 4,000-RPS API benchmark are separate questions; neither is a proven capacity target.

## Skills, orchestration, and retrospectives

Use [repo skills](skills.md) to package repeated procedures; [orchestration](orchestration.md) defines context and role boundaries. Skills guide work; structural scripts and tests enforce only what they actually check. There is no automatic CI enforcement or scheduled retrospective configured.

Run an evidence-backed retrospective after a substantial phase or repeated omission. Compare intended versus actual work, identify missed requirements and unnecessary overhead, and propose the smallest improvement. Initial assessment is read-only; implement improvements only within the user's authorized scope. Validate changes to instructions/skills with realistic scenarios. Prefer improving an existing skill over adding overlapping ones.

## Keep the reading map current

When a change adds, moves, removes, or revises contracts, component boundaries, developer/deployment commands, or knowledge documents, update the AGENTS.md change-area map and docs index in that same change. Before closure, check both link validity and whether the target actually supplies the applicable guidance. If no update is needed, a brief “reading map checked; no change needed” in the change results is enough. Keep AGENTS.md short and link detail.

At each substantial-phase retrospective, assess missing entries, stale guidance, incorrect reading conditions, and repeated discovery. The retrospective remains read-only initially: report findings and implement corrections only within authorized improvement work. This is event-driven maintenance, not a configured background schedule. Link validation catches missing files but not stale meaning.
