# Inference Lab

A hands-on lab for building and operating an LLM-backed chat application: API design, authentication, observability, load testing, and recovery. Start with local inference on an M4 Mac, then move the API to OCI.

**Status:** repository foundation only. The application and deployment are not implemented yet.

## Repository areas

- [backend/](backend/) — API, business logic, persistence, and inference integration.
- [frontend/](frontend/) — browser chat interface.
- [infra/](infra/) — local services, observability, and cloud configuration.
- [tests/](tests/) — unit, integration, load, and failure scenarios.
- [scripts/](scripts/) — repeatable development and validation commands.
- [docs/](docs/README.md) — architecture, decisions, experiments, lessons, and runbooks.
- [harness/](harness/build/README.md) — change plans, execution evidence, reviews, and context.
- [.agents/skills/](docs/skills.md) — reusable planning, delivery, and retrospective procedures.

## Start here

Read the [goals](GOALS.md), [roadmap](PLANS.md), and [development workflow](docs/workflow.md).
Follow [AGENTS.md](AGENTS.md) and the [branch-and-PR process](docs/runbooks/contributing.md) when making changes.
See the [development runbook](docs/runbooks/development.md) for validation commands and current limitations.
