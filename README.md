# Inference Lab

A guided local-LLM engineering lab for API design, authentication, streaming, observability, load testing, and recovery. We define expected behavior, implement small changes, and verify each requirement with evidence.

## Current state

The foundation is implemented: repository scaffold, documentation, three Codex skills, and structural validation tooling. Application services, model serving, deployment, and CI are not implemented yet. Start with native inference on an M4 Mac with 16 GB memory; later host the API on OCI.

Repository: [abbisai7/inference-lab](https://github.com/abbisai7/inference-lab). All changes use a topic branch and PR; see [contributing](docs/runbooks/contributing.md).

## Key files

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Project overview, navigation, and validation commands. |
| [AGENTS.md](AGENTS.md) | Concise contributor/agent rules, required reading, and completion checks. |
| [GOALS.md](GOALS.md) | Purpose, intended users, learning outcomes, constraints, and exclusions. |
| [PLANS.md](PLANS.md) | Milestone sequence and links to current work; detailed plans live in build records. |
| [CHANGELOG.md](CHANGELOG.md) | Short history of completed repository changes. |
| [.gitignore](.gitignore) | Excludes secrets, dependencies, caches, model downloads, and runtime artifacts from Git. |
| [PR template](.github/PULL_REQUEST_TEMPLATE.md) | Prompts for the outcome, change record, actual verification, review, and operational impact. |

## Application and infrastructure folders

These folders currently contain placeholders for future implementation.

| Folder | Intended responsibility |
| --- | --- |
| [backend/app/api/](backend/app/api/) | HTTP routes, request handling, and streaming endpoints. |
| [backend/app/auth/](backend/app/auth/) | Identity/session handling and authorization helpers. |
| [backend/app/core/](backend/app/core/) | Application configuration and shared setup. |
| [backend/app/db/](backend/app/db/) | Database access and persistence definitions. |
| [backend/app/inference/](backend/app/inference/) | Configurable adapters connecting the API to real or fake inference. |
| [backend/app/observability/](backend/app/observability/) | Application logs, metrics, and trace instrumentation. |
| [backend/app/schemas/](backend/app/schemas/) | Validated request, response, and event structures. |
| [backend/app/services/](backend/app/services/) | Business logic coordinating persistence, inference, and request lifecycle. |
| [backend/migrations/](backend/migrations/) | Versioned database schema changes. |
| [frontend/](frontend/) | Minimal browser chat interface. |
| [infra/compose/](infra/compose/) | Local supporting-service orchestration. |
| [infra/observability/](infra/observability/) | Grafana dashboards, Prometheus metrics, Loki logs, OpenTelemetry collection, and Tempo traces in their respective subfolders. |
| [infra/oci/](infra/oci/) | Cloud deployment configuration for the OCI-hosted API. |

## Development harness and skills

The harness tracks individual changes and execution evidence. It complements the durable system knowledge in docs.

| Location | Purpose |
| --- | --- |
| [harness/build/](harness/build/README.md) | One record per bounded phase/change: readable summary, requirements, implementation steps, and verification coverage. Includes a shared template and index. |
| [harness/build-log.md](harness/build-log.md) | Observed progress, commands/results, blockers, and execution history. |
| [harness/code_review/](harness/code_review/README.md) | Review scope/snapshots, findings, fixes, and re-review results. |
| [harness/context/](harness/context/README.md) | Material discoveries, clarifications, constraints, rationale, and unresolved questions needed by future work. |
| [.agents/skills/](docs/skills.md) | Reusable procedures: **harness-author** plans; **change-delivery** implements/verifies; **workflow-retrospective** assesses and improves the process. Each skill has instructions in SKILL.md and UI metadata in agents/openai.yaml. |

## Documentation

| Location | Purpose |
| --- | --- |
| [docs/README.md](docs/README.md) | Index of maintained project knowledge. |
| [docs/workflow.md](docs/workflow.md) | Feature, bug, testing, deployment, and experiment workflow, with a presentation explanation. |
| [docs/orchestration.md](docs/orchestration.md) | Selective agent roles, focused context, write ownership, and stable review/test snapshots. |
| [docs/skills.md](docs/skills.md) | Skill responsibilities, invocation, discovery, and validation limits. |
| [docs/lessons.md](docs/lessons.md) | Reusable findings and gotchas with evidence. |
| [docs/architecture/](docs/architecture/) | System boundaries and cross-cutting requirements; current requirements describe intended behavior. |
| [docs/decisions/](docs/decisions/README.md) | Architecture Decision Records explaining consequential choices and alternatives. |
| [docs/experiments/](docs/experiments/) | Templates and future reports for reproducible measurements and failure investigations. |
| [docs/runbooks/](docs/runbooks/) | **development.md** covers verified local commands; **contributing.md** covers branches/PRs/review; **deployment.md** contains currently unverified deployment/recovery requirements. |

## Scripts, tests, and validation

| Location | Purpose and current state |
| --- | --- |
| [scripts/](scripts/) | Repeatable developer tools; currently validate_repo.py checks structural links and build-record coverage. |
| [tests/unit/](tests/unit/) | Currently contains 14 tests for the foundation validator; application unit tests come later. |
| [tests/integration/](tests/integration/) | Planned API/dependency integration tests. |
| [tests/load/](tests/load/) | Planned controlled load/performance workloads. |
| [tests/failure/](tests/failure/) | Planned failure injection and recovery scenarios. |

From the repository root with Python 3.9+:

```sh
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests/unit -p 'test_*.py' -v
```

These check the foundation, not application behavior or production readiness. See the [development runbook](docs/runbooks/development.md) for limitations and future startup commands. Open this repository in Codex to discover its skills; discovery is not proven merely by their files existing.

Historical records and empty-folder placeholders are intentionally not listed individually here. Follow the linked indexes for detail, and maintain these explanations when responsibilities change.
