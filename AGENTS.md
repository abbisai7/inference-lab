# Working in Inference Lab

## Purpose and structure

A guided local-LLM engineering lab: M4 inference first, OCI-hosted API later.
Current state: scaffold, docs, three repo skills, and foundation validation;
no application services, deployment, or CI yet.

- `backend/app/`: API, auth, configuration, persistence, inference, telemetry.
- `backend/migrations/`: schema changes; `frontend/`: chat UI.
- `infra/`: Compose, observability, OCI; `tests/`: unit/integration/load/failure.
- `scripts/`: repeatable commands; `.agents/skills/`: reusable procedures.
- `GOALS.md`: direction; `PLANS.md`: phase sequence; `docs/`: durable knowledge.
- `harness/build/`: combined requirements/plans and linked coverage verdicts.
- `harness/build-log.md`: observed execution; `context/`: material discoveries;
  `code_review/`: findings and resolutions (both under `harness/`).

## Read what applies before changing code

Start with the selected build record and affected code/tests. Use the
[docs index](docs/README.md); read linked pages deliberately, not all history.

| Change area | Required reading and inspection |
| --- | --- |
| API, streaming, inference | Applicable contracts/consumer expectations, adapter code, compatibility tests, [architecture requirements](docs/architecture/requirements.md) |
| Identity or persistence | Applicable ownership/data invariants, schemas, migrations, negative-access tests, architecture requirements |
| Deployment or configuration | Target-environment constraints and [deployment runbook](docs/runbooks/deployment.md) |
| Workflow or agent behavior | [Workflow](docs/workflow.md), [orchestration](docs/orchestration.md), relevant [skills](docs/skills.md) |

Keep this map and the docs index current when contracts, components, commands,
or document locations change. Recheck relevance before closing affected changes
and at phase retrospectives; remove stale pointers rather than adding duplicates.

Contracts may be project-specific. Preserve downstream formats, ordering,
error semantics, and invariants unless the change explicitly includes migration.
Do not “standardize” surprising behavior without understanding its consumers.
Locate current contracts through the docs index and relevant code/test references;
if missing or inconsistent, investigate and surface the gap before changing it.
Required knowledge belongs in checked-in docs/tests; no separate MEMORY.md is
needed. Capture material discoveries in context, then update durable docs as needed.

## Change and completion rules

- After the authorized empty-main bootstrap, make EVERY project change on a
  topic branch from current `origin/main`, including docs/plans. Deliver via PR;
  never push/force-push main or merge without explicit user instruction.
  Follow [contribution workflow](docs/runbooks/contributing.md).

- Create/update one [build record](harness/build/template.md) before implementation.
  Use a short summary, named requirements with stable IDs, steps, and coverage.
- Resolve blocking questions; obtain agreement for material scope changes.
  Never silently drop requirements or weaken tests to claim success.
- Use `$harness-author` to plan, `$change-delivery` to implement/verify,
  and `$workflow-retrospective` to assess actual process evidence.
- Delegate substantive work selectively under the orchestration rules;
  small changes stay single-agent. Assign file ownership, keep context focused,
  and identify test/review snapshots. Disclose self-review or unavailable checks.
- Log actual commands/results; link evidence from coverage rows. Update changelog,
  indexes, affected docs/runbooks, and useful lessons without duplicating records.
- Before Complete, reconcile every requirement and step with actual evidence;
  unresolved required findings or unverified criteria keep the change open.
  Report outcomes, checks actually run, and remaining limitations.

## Build, test, and deployment

From the repository root, Python 3.9+:

```sh
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests/unit -p 'test_*.py' -v
```

These validate the foundation only, not application correctness or evidence truth.
Application setup/build/start commands are not defined; see the
[development runbook](docs/runbooks/development.md). Run checks relevant to changes.
Deployment requires environment/revision, configuration/secrets, migrations,
health/telemetry, restore and rollback evidence; local checks alone are insufficient.

Keep secrets, personal data, model downloads, and runtime artifacts out of Git.
Keep Ollama native on macOS and telemetry optional within the 16 GB memory budget.
Run performance experiments without competing workloads; remove populated `.gitkeep`.
Keep this guide concise (roughly under 80–100 readable lines); move detail to docs
and add links with explicit reading conditions instead of growing a second manual.
