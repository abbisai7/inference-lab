# Review: Final repository foundation

Scope: stable workflow/orchestration/skill instructions, context and review conventions. Transient scripts/index updates were outside the independent pass.
Reviewer: fresh-context subagent foundation_review; independent of authoring. This is static instruction/scenario review, not runtime implicit-routing or application testing.
Snapshot: uncommitted files; the parent records content hashes of reviewed files in [the snapshot manifest](change-0003-snapshot.json). Two wording corrections below supersede the originally inspected wording; the reviewer rechecked both corrections and the final validator/tests.

## Scenarios assessed

1. Planning-only streaming chat: harness-author inspects relevant sources and creates a bounded planning record; does not implement app code or invent command success.
2. Bug implementation with unavailable runtime: change-delivery makes authorized progress, records missing evidence, and leaves affected criteria unverified/open.
3. Retrospective without write authorization: workflow-retrospective assesses evidence read-only and proposes corrections without mutating files.

All three are explicitly supported by the instructions. No must-fix scope/ownership contradictions found. This is scenario reasoning, not observed implicit skill selection or end-to-end invocation.

## Findings

| Finding | Consequence | Resolution | Status |
| --- | --- | --- | --- |
| Snapshot wording claimed hashes allow recovery | A reader could lose file contents while retaining only hashes | docs/orchestration.md now says hashes identify/verify; retain patch/files when reconstruction is required | Resolved; independently rechecked |
| Coverage wording implied all states need executed evidence | Pending/Blocked rows could encourage fabricated evidence | docs/workflow.md now requires passing evidence only for Verified; other rows state missing evidence/blockers | Resolved; independently rechecked |

## Additional validator finding and correction

The independent tooling review reproduced a completion bypass: only hyphen bullets were recognized, so asterisk/plus bullets could hide unfinished tasks or uncovered requirements. The parent added regression cases covering unordered and ordered markers. The red run observed eight failures across two test methods, then the fix made all 14 tests pass. The reviewer independently rechecked the corrected parser and reran the repository validator and unit suite successfully. The original red execution was observed by the parent, not independently repeated by the reviewer.

## Verdict and limits

Final independent verdict: no unresolved must-fix findings in reviewed scope. Independently executed `python3 -B scripts/validate_repo.py --json` (34 Markdown files, 104 inline local file links at that snapshot) and `python3 -B -m unittest discover -s tests/unit -p 'test_*.py' -v` (14 tests passed). Final closure edits to indexes/logs/results are parent-reconciled, not a claim that the reviewer inspected every later text edit.

Checks establish structure, not evidence truth, application behavior, index synchronization, or skill routing. No application/performance checks or live discovery tests were performed.

## Isolated explicit skill forward test

A second fresh-context agent, skill_forward_test, executed a realistic planning-only request using the actual harness-author SKILL.md in a temporary copied fixture at `/private/tmp/inference-lab-forward-bxac36o1`. It produced `harness/build/phase-01-streaming-chat.md` as Draft with seven named requirements, proposed steps/checks, open questions, and all application coverage Pending. It updated only planning/index/changelog/build-log artifacts in the fixture. The parent inspected the generated plan and confirmed the fixture's only Python sources remained the copied validator and its tests; no app/dependency files were created. The live repository's Phase 01 record was not created or changed by this test.

Fixture evidence: `python3 scripts/validate_repo.py --json` passed with 35 Markdown files and 115 inline local links; fixture unit suite passed 12 tests because the copy preceded the two later parser regressions. This is distinct from the final live repository's 14-test suite. Generated plan SHA-256: `b606f44015dffe677a1c8483d6db224fd6ff6b22ffcd7772f6fd47b573f56f24`. Temporary fixture files are not permanent repository deliverables.

The planning-only procedure was exercised successfully. Runtime implicit skill selection and delivery/retrospective execution were not forward-tested; those two boundaries received static scenario review. No claims are made about all-model routing reliability or production application behavior.
