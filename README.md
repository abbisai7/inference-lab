# Inference Lab

A guided local-LLM engineering lab for API design, identity, streaming, observability, load testing, and recovery. We use readable requirements, bounded implementation plans, meaningful tests, and explicit verification evidence.

## Current state

Repository foundation only: scaffold, documentation, three repo-scoped skills, and structural validation tooling. No application, model service, deployed resources, CI, or measured serving capacity exists. The Mac M4 with 16 GB memory is the initial inference target; a later phase moves the API to OCI.

Repository: [abbisai7/inference-lab](https://github.com/abbisai7/inference-lab). After the initial bootstrap, all changes use a topic branch and PR; see [contribution workflow](docs/runbooks/contributing.md).

## Start here

- [Goals](GOALS.md): purpose, users, boundaries, learning outcomes.
- [Phase index](PLANS.md): sequence and current work.
- [Workflow](docs/workflow.md): how features, bugs, tests, deployments, and experiments proceed; includes a presentation explanation.
- [Orchestration](docs/orchestration.md): selective agents and context/evidence boundaries.
- [Skills](docs/skills.md): reusable planning, delivery, and retrospective procedures.
- [Build records](harness/build/README.md), [documentation index](docs/README.md), [agent instructions](AGENTS.md), [changelog](CHANGELOG.md).

## Validate the foundation

From the repository root with Python 3.9+:

```sh
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests/unit -p 'test_*.py' -v
```

These are foundation checks, not application tests or CI enforcement. See [development runbook](docs/runbooks/development.md) for limitations and future app command availability. Open this repo in Codex to discover its skills; file existence does not prove live discovery in this chat.

## Structure

```text
inference-lab/
├── .agents/
│   └── skills/
│       ├── change-delivery/
│       │   ├── agents/
│       │   │   └── openai.yaml
│       │   └── SKILL.md
│       ├── harness-author/
│       │   ├── agents/
│       │   │   └── openai.yaml
│       │   └── SKILL.md
│       └── workflow-retrospective/
│           ├── agents/
│           │   └── openai.yaml
│           └── SKILL.md
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── core/
│   │   ├── db/
│   │   ├── inference/
│   │   ├── observability/
│   │   ├── schemas/
│   │   └── services/
│   └── migrations/
├── docs/
│   ├── architecture/
│   │   └── requirements.md
│   ├── decisions/
│   │   ├── 0001-spec-driven-development.md
│   │   ├── 0002-unified-change-records.md
│   │   ├── 0003-repository-harness.md
│   │   ├── 0004-final-foundation-and-skills.md
│   │   ├── README.md
│   │   └── template.md
│   ├── experiments/
│   │   └── template.md
│   ├── runbooks/
│   │   ├── contributing.md
│   │   ├── deployment.md
│   │   └── development.md
│   ├── README.md
│   ├── lessons.md
│   ├── orchestration.md
│   ├── skills.md
│   └── workflow.md
├── frontend/
├── harness/
│   ├── build/
│   │   ├── 0001-documentation-foundation.md
│   │   ├── 0002-unified-change-workflow.md
│   │   ├── README.md
│   │   ├── change-0003-finalize-foundation.md
│   │   ├── change-0004-concise-agent-guidance.md
│   │   ├── change-0005-maintain-reading-map.md
│   │   ├── change-0006-pr-only-workflow.md
│   │   ├── phase-00-harness-adoption.md
│   │   └── template.md
│   ├── code_review/
│   │   ├── README.md
│   │   ├── change-0003-foundation-review.md
│   │   └── change-0003-snapshot.json
│   ├── context/
│   │   ├── README.md
│   │   └── change-0003-foundation-context.md
│   └── build-log.md
├── infra/
│   ├── compose/
│   ├── observability/
│   │   ├── grafana/
│   │   ├── loki/
│   │   ├── otel/
│   │   ├── prometheus/
│   │   └── tempo/
│   └── oci/
├── scripts/
│   └── validate_repo.py
├── tests/
│   ├── failure/
│   ├── integration/
│   ├── load/
│   └── unit/
│       └── test_validate_repo.py
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── GOALS.md
├── PLANS.md
└── README.md
```

The harness owns bounded work and evidence; docs preserve system knowledge; skills package procedures. No application or CI is implemented yet.
