# Phase NN or Change NNNN: Descriptive title

Type: Feature | Bug fix | Refactor | Infrastructure | Deployment | Documentation
Status: Draft | Ready | In progress | Complete | Superseded
Links: related changes, ADRs, experiments, and runbooks as applicable

## Summary

In three to five plain sentences explain the problem, proposed change, and expected user or operator outcome. Keep this current if scope changes. A reader should understand the change without reading the detailed plan.

## Current status

In plain language: what works, what remains, blockers, and next action. State whether verification or deployment is pending. Avoid unsupported percentages.

## Requirements and acceptance criteria

State scope and exclusions. Give each independently verifiable requirement a stable ID AND a descriptive name, such as “R1 — Keep conversations private.” Write the complete expected behavior for readers unfamiliar with the project; explain abbreviations on first use. An ID is a reference key, not a description. Define externally observable behavior and meaningful negative cases; include interfaces or data contracts where needed. Resolve blocking questions before marking Ready. Link existing requirements instead of copying them.

## Investigation

For bugs: reproduction, actual versus expected behavior, and cause once established. For uncertain work: evidence and open questions. Omit this section when unnecessary; do not present hypotheses as established causes.

## Implementation plan

Describe the chosen approach and tradeoffs, then list concrete steps in dependency order as checkboxes. Link steps to acceptance IDs where useful. Split large changes into independently verifiable child changes linked from a parent overview.

- [ ] Concrete implementation step.
- [ ] Verification and documentation updates.

## Validation and coverage

Map EVERY acceptance criterion to its implementation and meaningful evidence. Pending means work has not been established as complete; Implemented means code exists but verification is outstanding; Verified means relevant checks were run and passed; Blocked means a stated obstacle prevents progress. Include an explanatory sentence when the label alone would be ambiguous. Record commands/procedures, environment/revision when available, actual results, and limitations. A test file merely existing is not proof that it passed or covers the requirement.

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Descriptive requirement name | Not implemented | No checks run | Pending |

## Operational impact

Configuration/secrets, migrations, compatibility, resource implications, telemetry, rollout, rollback, and runbook updates as relevant. State not applicable with a reason for changes without operational impact.

## Results and learning

What shipped, verification results, remaining limitations, changelog update, and linked lessons/experiments. Before Complete, reconcile the entire document with the actual implementation and inspect each criterion. Record scope adjustments with reasons and user agreement for material requirement changes. Do not silently drop or renumber criteria. Keep incomplete work visible; superseded changes need a replacement link.

For longer work, link dated build-log checkpoints here. Put material discoveries and reasoning in phase context, rather than duplicating routine execution history. Keep current status synchronized with observed evidence.

## Execution and review references

Link relevant [build-log](../build-log.md) events, review findings under harness/code_review/, and optional context handoffs. Keep requirements here, observed execution in the log, actionable review findings in reviews, and durable operating procedures in runbooks. Do not copy the same content into all four places. Self-review is not an independent review.

Repository checks validate structure, not the truth of evidence. A Complete record cannot contain unfinished steps or unverified requirements. Use meaningful names alongside stable IDs.
