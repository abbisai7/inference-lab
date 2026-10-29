---
name: change-delivery
description: Implement and verify a selected repository change with requirement coverage and selective subagent orchestration. Use for authorized features, bugs, infrastructure, or deployment work; not planning-only requests or read-only retrospectives.
---

# Change Delivery

Read applicable AGENTS.md, the selected build record, and relevant source/test/decision references. Follow [the workflow](../../../docs/workflow.md) and [orchestration](../../../docs/orchestration.md). If no bounded record exists, create it before implementation; resolve blocking requirements rather than guessing.

Choose the smallest effective execution shape. Small changes can stay single-agent. For substantive work, delegate bounded research, implementation, testing or review only when useful and authorized. Use fresh task contexts where supported, with named requirements, relevant paths, allowed writes, snapshot, checks, output, and stop condition. Never copy the entire chat by default. No global configuration/model changes or separate user-owned chats are implied.

The orchestrator owns scope, shared records/logs/indexes, and final reconciliation. Assign disjoint writer paths. Test/review depend on a stable identified snapshot; invalidate affected evidence after fixes. Testers must not weaken expectations to pass. Role instructions do not change sandbox permissions. If workers are unavailable, proceed sequentially and label self-review honestly.

Implement and run meaningful checks tied to every requirement. Use failing regression checks where appropriate. Record exact observed commands/results and limitations in the build log; capture material discoveries in context and detailed findings in reviews. Reference these from coverage rows instead of duplicating evidence. Do not infer success from code existing, a test file, or agent consensus.

Before Complete, reread the full record and compare requirements, code, checks and findings. All current criteria must be Verified, required findings resolved/explicitly accepted, and planned steps reconciled. Check the AGENTS.md reading map and docs index against changed contracts, component boundaries, commands, and document locations; update relevant pointers in the same change or record that no update was needed. Update changelog and affected architecture/runbooks/lessons; preserve failed observations with correction entries. Unavailable required checks keep work open. Deployment requires environment/revision and operational evidence; code completion does not imply rollout.

Report named outcomes, actual checks, review independence, and remaining limits. Do not launch later phases automatically. Routine authorized implementation does not require another permission ceremony; scope changes and external actions stay within user authorization.

Follow the repository [branch-and-PR workflow](../../../docs/runbooks/contributing.md). After the initial-main bootstrap exception, branch before any repository edits, including planning/docs, and deliver authorized changes via a PR to main. Do not directly push/force-push main, silently merge, or request third-party reviewers without user instruction.
For substantive code, obtain initial fresh-context review with requirements/contracts and the examined diff/snapshot. Investigate findings, fix or document evidence-backed dispositions, rerun affected checks, and request re-review of the changed snapshot and potential regressions. Preserve review rounds and leave unresolved required findings open. Opening a PR does not authorize merging.
