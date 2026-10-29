# Delivery plan and phase index

All application milestones are planned, not implemented. Create a build record containing requirements and an implementation plan before starting each milestone; select concrete interfaces and acceptance criteria there.

| Milestone | Outcome and verification focus |
| --- | --- |
| 1. One observable request | Streaming FastAPI-to-Ollama chat, cancellation, health/readiness, fake inference backend, baseline experiment |
| 2. Identity and ownership | Invited users, JWT/refresh sessions, user/admin roles, private conversations; negative authorization tests |
| 3. Observability | Metrics, logs, traces, Grafana dashboards; correlate request flow and identify latency sources |
| 4. Overload control | Shared limits, bounded admission, deadlines, budgets; verify capacity release and explicit rejections |
| 5. Performance and failures | k6 workloads, concurrency/arrival-rate comparisons, cold/warm runs, dependency outages and recovery |
| 6. OCI deployment | HTTPS API, private Mac inference connectivity, durable storage, backup/restore, rollout/rollback exercises |
| 7. OAuth/OIDC | Keycloak login, external identity mapping, preserved ownership and roles, tested migration from password login |

Foundational request IDs, timings, configuration, and secure coding practices begin with the features that need them. Each milestone delivers a design explanation, verification evidence, experiment where relevant, and current runbooks.

## Current work and phase ownership

- Phase 00: [Repository harness adoption](harness/build/phase-00-harness-adoption.md) — Complete (documentation verified; application not started).
- Foundation finalization: [Change 0003](harness/build/change-0003-finalize-foundation.md) — Complete (foundation only; no app implementation).
- Phases 01–07 correspond to milestones 1–7 above — Not started. No detailed build records exist yet. Before Phase 01, create a bounded streaming-chat record from [the template](harness/build/template.md).
- Earlier completed documentation work is listed in [the build index](harness/build/README.md).

This file owns sequence and links; build records own detailed requirements, steps, and coverage verdicts linked to observed build-log evidence. Keep the index status synchronized at checkpoints. Do not prefill speculative implementation plans for all future milestones.

For a large milestone, use linked small records such as `phase-01a-streaming-api.md` and `phase-01b-chat-ui.md`. For later maintenance use descriptive records such as `change-0003-disconnect-cleanup.md`, with a type covering bugs, refactors, infrastructure, deployments, or documentation. Examples are naming guidance, not existing work. IDs need only be unique in this directory. Parent phases remain open until required child outcomes are verified.
