# Change 0007: Explain repository contents in the README

Type: Documentation
Status: In progress

## Summary

Replace the exhaustive directory tree with a concise purpose-oriented guide to the important files, folders, and component subfolders. Preserve setup/validation and navigation, and distinguish planned application folders from working foundation tooling. No files or application structure are removed.

## Requirements and acceptance criteria

- R1 — Explain instead of enumerate: remove the full tree and explain each meaningful repository area without listing historical records or placeholder files individually.
- R2 — Accurate navigation: link key files and folders, retain foundation validation commands, and distinguish planned application code from existing tools/tests.
- R3 — Proportionate delivery: validate documentation, record the change, and publish a separate PR from current main without merging it.

## Implementation plan

- [x] Replace the README tree and redundant navigation with short purpose tables.
- [x] Check links, content accuracy, reading-map relevance, and whitespace; update index/changelog/log.
- [ ] Commit and push the documentation branch; open a PR to main.

## Validation and coverage

| Named requirement | Implementation | Verification evidence | Status |
| --- | --- | --- | --- |
| R1 — Explain instead of enumerate | README purpose tables; exhaustive tree removed | [Self-review and checks](../build-log.md) | Verified |
| R2 — Accurate navigation | Linked guide and preserved validation commands | [Link validation and self-review](../build-log.md) | Verified |
| R3 — Proportionate delivery | Pending | Pending | Pending |

## Operational impact

README and change-tracking documents only; no runtime, API, deployment, or directory changes. No additional ADR or lesson is needed. AGENTS.md reading map and docs index checked; existing README/workflow routes remain applicable.

## Results and learning

README self-review confirmed the purpose descriptions against actual files, explicit planned/implemented distinctions, retained commands, and no exhaustive tree. `python3 scripts/validate_repo.py` passed; `git diff --check` passed. Reading map/docs index checked; no routing change needed. PR publication pending. No application/unit tests were run for this documentation-only edit; no new reusable lesson or ADR was needed.
