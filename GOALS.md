# Goals and vision

## Purpose

Learn to design, secure, measure, and operate an LLM-backed application by building it, applying load, introducing failures, and explaining the observed results.

## Users and experience

Initially support invited individuals with private conversations and user/admin roles. Provide a minimal browser UI with streaming chat and saved history as milestones deliver those capabilities. Explain each layer through guided implementation and experiments.

## Intended system

Start locally on an Apple M4 Mac with 16 GB unified memory: FastAPI, a small quantized model served by native Ollama, PostgreSQL, and Redis. Add Prometheus/Grafana, structured logs/Loki, and OpenTelemetry/Tempo incrementally. First learn JWT sessions; later introduce OAuth/OIDC through Keycloak.

Later move the API to an OCI instance and reach Mac inference over a restricted private connection. Keep the inference endpoint configurable. A single Mac remains a capacity and availability dependency.

## Success criteria

- Explain a request from login and authorization through queueing, inference, streaming, and persistence.
- Demonstrate user isolation and correct session behavior through repeatable checks.
- Diagnose bottlenecks with logs, metrics, traces, and dashboards.
- Measure first-token latency, completion latency, P90/P99, throughput, failures, and rejections under stated workloads.
- Demonstrate bounded overload behavior, cancellation, dependency failures, and recovery.
- Reproduce deployment and recovery steps from verified runbooks.

Production practices are a learning objective; production readiness is earned through environment-specific verification, not implied by this vision. Establish capacity and latency targets from measurements.

## Deferred

Public signup, organizations, billing, Kubernetes, multi-machine inference, and model training. Keep the UI small and focus on system behavior.

## Ownership

This is the authoritative project direction. Read [PLANS.md](PLANS.md) for milestone sequencing and [the workflow](docs/workflow.md) for how work proceeds. Detailed acceptance criteria belong in the selected build record, not duplicated here.
