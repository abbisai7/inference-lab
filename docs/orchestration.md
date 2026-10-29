# Selective multi-agent delivery

## Purpose and limits

Keep the coordinator focused on scope and completion while moving bounded exploration, implementation, testing, or review into focused agent contexts. This can improve elapsed time and context quality; it can also increase total token use. Measure usage where available, elapsed time, rework, and missed requirements before claiming improvement.

These agents help build the application; they are separate from the local LLM that will serve chat requests. Skills are reusable procedures; agent roles are assignments to workers. We initially use the host's available subagent tools, not a custom orchestration service or an always-running agent fleet. No custom model defaults or global agent configuration are required.

## Role and dependency flow

Request → orchestrator triage → relevant discovery/planning → implementation → stable snapshot → testing and review → fix/recheck as needed → coverage reconciliation and evidence → completion.

| Role | Task and output |
| --- | --- |
| Orchestrator | Own user intent and scope, choose workers, reconcile findings, own shared records/status, decide completion from evidence |
| Research/planning | Inspect relevant code/contracts, surface uncertainty, propose bounded steps and acceptance checks; no application writes during planning-only work |
| Implementation | Change assigned components and run focused checks; return paths, actual results, limitations |
| Testing | Exercise named requirements, write tests only if assigned those paths, reproduce failures; do not silently fix implementation or weaken expectations |
| Review/validation | Inspect the selected snapshot against requirements and test relevance; report correctness/coverage/operational findings with evidence |

Testing asks whether specified behavior works under stated conditions. Validation asks whether all required behavior was implemented and whether the evidence is meaningful. The orchestrator must inspect results; agent agreement is not proof.

## When to delegate

Small low-risk changes default to one agent. Ordinary implementation benefits from a fresh testing/review pass when available. Substantial or ambiguous work can add focused planning and separate test/review roles. Start with at most two workers concurrently, subject to host limits. Roles can execute sequentially; do not create one permanent agent per role.

Parallelize independent read-heavy tasks. Implementation depends on settled requirements; test execution depends on available code; final review depends on a stable snapshot. A tester may develop a black-box test approach while implementation proceeds, with disjoint file ownership. Never run load benchmarks alongside competing tests/inference jobs on the Mac.

## Bounded context

Read AGENTS.md, the selected record, and relevant source/test paths. Use indexes/searches to find applicable constraints and expand along dependencies as needed; this is not permission to skip necessary system invariants. Do not pass the full parent chat by default. Use fresh-context delegation where supported; if the host inherits history, disclose that context/cost isolation is limited.

Each assignment includes: objective and named requirements; selected record; applicable instructions/decisions; relevant paths; allowed writes/exclusions; examined revision or snapshot; expected checks; output format; and stop condition. Include material user clarifications, not an entire conversation transcript. Workers may request additional context rather than guess.

Worker reports contain outcomes, changed paths or findings, executed checks/results, evidence references, blockers, and limits. Keep raw logs in local generated artifacts, excluded from Git. A material context record carries discoveries and reasoning, not routine command output. A fresh session may resume from these references after inspecting current code.

## Writes, evidence, and snapshots

The orchestrator alone edits shared build records, indexes, changelog and build log during delegation. Workers report their results; assign separate test or implementation paths explicitly. In a shared checkout, avoid overlapping writers. Use isolated worktrees when concurrent implementation genuinely requires them; integrate and verify before completion. Do not silently create separate user-owned chats for internal workers.

Identify the revision and dirty state. For uncommitted work, record a content hash manifest of the files under test/review so the examined snapshot can be identified and verified; retain the patch/files as well when reconstruction is required; do not claim a commit exists. Freeze relevant files while checks run. If fixes change the examined snapshot, rerun affected checks and obtain updated review where findings require it. No worker may quietly redefine requirements or claim independent review of its own work.

If delegation is unavailable, use the same sequence with self-review and disclose reduced independence. If a required environment/check is unavailable, keep affected requirements unverified instead of inferring success. Bound exploratory retries by the task and report unresolved blockers.

## Skills and improvement

The change-delivery skill coordinates this procedure; harness-author structures the selected record; workflow-retrospective compares execution with the intended process. Significant discoveries become context, reviews own findings, and the build log owns observed execution. No background scheduler is created by a skill.

Recommended retrospective cadence is after a substantial phase or repeated failure, not a mandatory calendar schedule. Evaluate actual usage/time and requirement coverage; reduce delegation if repeated discovery and coordination outweigh the benefit.

## Review/fix/re-review and PR boundary

Follow [the contribution runbook](runbooks/contributing.md). The initial review for substantive code should use a fresh task context with requirements/contracts and exact diff/snapshot, rather than the author's full conversation or conclusion. Review findings return to the author; the author investigates, fixes, reruns checks, and submits the changed snapshot for re-review. Reuse the reviewer to check resolutions and regressions; major scope changes can justify a fresh broad pass. Record findings/rounds and explicitly label unavailable independence. All post-bootstrap work uses a topic branch and PR; delegation does not authorize direct main updates or merging.
