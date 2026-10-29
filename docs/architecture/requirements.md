# Architecture requirements

Status: intended constraints for future specs. No application is implemented yet.

## Boundaries and resources

Keep HTTP routing/schemas, business logic, authentication, persistence, inference, and telemetry separate. Use an asynchronous inference adapter with configurable endpoint and model. Run Ollama natively on macOS; introduce optional Compose profiles for supporting services to fit 16 GB memory. Measure before selecting model settings and operational limits.

## Identity and data

Use maintained security libraries. Plan Argon2id password hashing, short-lived signed JWT access tokens, rotating refresh sessions, and logout revocation. Validate signatures, allowed algorithms, expiry, issuer, and audience. Keep browser access tokens in memory and protect refresh cookies with HttpOnly, appropriate Secure/SameSite settings, and CSRF controls. Specify local and HTTPS cookie behavior in the identity spec.

Separate identity from authorization. Enforce roles and conversation ownership server-side. Preserve application identities and ownership when introducing OIDC. Keep secrets and personal data out of source control; do not log credentials, tokens, or chat bodies by default.

## Streaming and reliability

Propagate cancellation and release admission capacity on success, failure, disconnect, and timeout. Use explicit deadlines, bounded queues, and concurrency limits. Do not retry partially streamed answers automatically. Distinguish liveness from dependency-aware readiness. Cover inference restarts, Mac sleep, and network loss in failure scenarios.

## Observability and measurement

Propagate request IDs and trace context; use structured logs. Measure queue wait, first generated token, full stream completion, generation speed, errors, rejections, and active requests independently. HTTP headers are not generated tokens or completed answers. Avoid unbounded metric labels, including user and request IDs.

Report latency alongside errors and achieved throughput. Separate warm and cold runs. Record model/version, context/output limits, workload, load pattern, duration, sample count, hardware, and configuration. Use fake inference to isolate API overhead. Make no unmeasured capacity claims.

## Deployment

Keep inference, databases, telemetry, and administration private. Public API access requires HTTPS. Use a restricted private connection between OCI and the Mac; Tailscale is the planned initial approach. Document configuration, migrations, durable storage, restore, and rollback before calling the deployment verified. Additional API workers do not imply additional inference capacity.
