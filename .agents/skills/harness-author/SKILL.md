---
name: harness-author
description: Create or revise bounded engineering build records and repository harness conventions before implementation. Use for feature or bug planning, acceptance criteria, and harness improvements; not for executing application work or ordinary conceptual questions.
---

# Harness Author

Inspect applicable AGENTS.md, the selected record or PLANS.md, and relevant implementation before proposing a change. Follow [the workflow](../../../docs/workflow.md); use the existing [record template](../../../harness/build/template.md). Read only relevant architecture, ADRs, context, and tests; expand discovery when dependencies require it.

Produce one human-readable record with a short summary/current status, named observable requirements with stable IDs, explicit exclusions, concrete steps, verification coverage, operational impact, and unresolved questions. For bugs distinguish reproduction, hypothesis, and cause. Keep spec and implementation together. Scale detail to the change; do not invent future phases, commands, capacity, or approvals.

Planning-only requests authorize planning artifacts, not application code, tests, dependencies, deployment, or implementation-side context/review records. Resolve blocking uncertainty; use existing user authorization for routine documentation updates rather than inventing extra approval gates. Record material scope changes explicitly.

Preserve source ownership: direction in GOALS.md, sequence in PLANS.md, task requirements in build records, execution evidence in build-log, discoveries in context, findings in reviews, durable knowledge in docs. No PROMPTS.md. Update relevant indexes and changelog for completed planning changes without claiming application completion.

Run available structural checks, report actual results/limits and proposed next action, and stop at the requested planning boundary. If implementation is explicitly included, hand off the bounded record to the delivery procedure; do not infer that from a planning request.

Follow the repository [branch-and-PR workflow](../../../docs/runbooks/contributing.md). After the initial-main bootstrap exception, branch before any repository edits, including planning/docs, and deliver authorized changes via a PR to main. Do not directly push/force-push main, silently merge, or request third-party reviewers without user instruction.
