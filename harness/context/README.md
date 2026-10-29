# Phase context: what future work must know

Context preserves material discoveries, decisions, clarifications, constraints, assumptions, and unresolved questions from executing a phase. It is more than a handoff or progress summary. Create a phase-specific file when the work actually produces material context: `phase-NN-description-context.md` (or a matching change name).

Record information only if omitting it could change later implementation/verification, repeat significant discovery, break a contract/invariant, hide a blocker, or affect operations/recovery. Include the reasoning, downstream implications, and provenance: code path, observed command/result, user clarification, ADR, or review finding. Mark hypotheses and assumptions explicitly; do not convert them into facts.

Do not include transcripts, routine progress, repeated plans, raw test output, credentials, or temporary dead ends with no lasting effect. Requirements belong in build records, observed execution in the build log, findings in reviews, and durable architecture choices in ADRs. Link these sources. Update context when a material discovery occurs and review it at handoff/phase close. Its existence is not proof of completion.

Example (hypothetical): “Closing the API-to-model connection did not establish that model work stopped in the tested runtime. Verify model-side cancellation in later capacity tests.” Include actual evidence before treating that as an observed finding.

A handoff can point to this context plus the selected record and latest log evidence; avoid creating a second status authority.
