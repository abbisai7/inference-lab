# Deployment and recovery runbook

Status: Planned; no OCI resources or deployment procedures have been created or verified.

Follow [the workflow](../workflow.md) and link deployment evidence to a [change record](../../harness/build/README.md).

## Intended topology

Initially all services are local. Later OCI hosts the HTTPS API and supporting services; native Ollama on the Mac is reached over a restricted private connection. Keep administration and observability private. Mac sleep or network loss can make inference unavailable.

## Required before deployment completion

The deployment milestone must supply and exercise exact procedures for:

- Prerequisites, configuration/secrets, network access, and HTTPS.
- Reproducible deployment, schema migrations, and persistent data.
- Liveness/readiness checks, smoke tests, dashboards, and failure diagnosis.
- Backup creation and demonstrated restoration.
- Rollout, rollback, migration compatibility, and shutdown.
- Mac/network/inference outage behavior and recovery.

For each procedure record commands, expected outcomes, environment, verification evidence, and limitations. These are pending requirements, not working instructions or a production-readiness claim.
