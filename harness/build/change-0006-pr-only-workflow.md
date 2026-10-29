# Change 0006: PR-only contribution workflow

Type: Documentation
Status: Complete

## Summary

Document the user's empty-main bootstrap exception and require a topic branch and pull request for the initial project files and every later repository change. Define the fresh-context review/fix/re-review procedure and main-branch protection configuration. This record verifies contribution guidance; actual initial push and hosted protection must be verified separately on GitHub after publication.

## Requirements and acceptance criteria

- R1 — Branch and PR discipline: all post-bootstrap changes, including documentation and plans, start from current main on a topic branch and are delivered through a PR; no direct/force pushes to main or unrequested merges.
- R2 — Review loop: substantive changes get scoped fresh-context review, findings reconciliation, fixes/tests and re-review of the changed snapshot, with small documentation changes using proportionate self-review.
- R3 — Protection and setup guidance: document the SSH remote, bootstrap exception, protection prerequisites/settings, verification, and truthful distinction between intended and actually configured settings.

## Implementation plan

- [x] Update persistent rules, workflow, skills, review conventions and contribution runbook.
- [x] Check documentation links, edited skill metadata, and foundation unit tests before publication.
- [x] Record scoped documentation results without claiming remote operations have happened before they do.

## Validation and coverage

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Branch and PR discipline | AGENTS.md, contribution/workflow docs and three skills | [Observed checks and self-review](../build-log.md) | Verified |
| R2 — Review loop | Contribution/orchestration docs, review conventions, delivery skill | [Observed checks and self-review](../build-log.md) | Verified |
| R3 — Protection and setup guidance | Contribution runbook, PR template, owner-managed protection disclosure | [Observed checks and self-review](../build-log.md) | Verified |

## Operational impact

The user initially authorized initial publication and protection, then chose branch/PR delivery and owner-managed GitHub settings. An empty initial commit d9fce16 was pushed to main to establish a base. All project files are on chore/initial-foundation for PR delivery. No GitHub settings were changed or independently verified. This guidance does not enable CI, request third-party reviewers, merge PRs, alter repository visibility, or lock main read-only. Hosted settings can change independently; verify them on GitHub.

## Results and learning

Documentation and local contribution-policy self-review complete. `python3 scripts/validate_repo.py` passed; all 14 foundation tests passed; all three edited skills passed bundled quick validation; AGENTS.md is 83 lines. Initial file-marker scan found no common private-key/GitHub/OpenAI token patterns; this is not a comprehensive secret audit.

SSH access confirmed; remote was empty at both inspections. Empty base commit d9fce16 was successfully pushed and chore/initial-foundation created from it. Owner-managed protection remains unverified. At this documentation snapshot the project commit/push/PR is the next authorized external action; the task result will report its actual outcome. No merge is authorized. No application implementation or CI was added.
