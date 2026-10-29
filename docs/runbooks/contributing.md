# Branches, pull requests, and main protection

## Repository and bootstrap exception

Repository: [abbisai7/inference-lab](https://github.com/abbisai7/inference-lab).
SSH remote: `git@github.com:abbisai7/inference-lab.git`. Default branch: main.
The user authorized the initial bootstrap, then chose a new-branch/PR delivery for all project files and took responsibility for GitHub protection settings. Because the remote had no branches, an empty root commit was published to main solely to establish a PR base; the complete scaffold/docs/skills/tooling is delivered on chore/initial-foundation. This empty-base publication is the only bootstrap exception. Repository identity is local to this checkout; use the verified GitHub account's noreply identity if no local author identity is configured. Never change global Git identity or expose a private email unnecessarily.

## Every later change

1. Inspect branch, working-tree status, applicable instructions, and selected record. Preserve unrelated work. Fetch origin and base a new descriptive branch on current main; do not reset or discard existing changes to accomplish this.
2. Use `feat/`, `fix/`, `docs/`, `chore/`, or `infra/` plus a descriptive slug. Branch before editing, including planning/docs work. Small related fixes may continue in their existing open PR branch.
3. Create/update the combined build record; implement within scope, run meaningful checks, record observed results, and maintain reading map/index and changelog.
4. For substantive code, obtain a scoped fresh-context review and fix/re-review as described below. Capture findings and exact examined snapshot. Small low-impact docs can use disclosed self-review.
5. Commit intended files, inspect the staged diff (including untracked files), and push the topic branch. Open a PR targeting main and link the change record, outcome, verification, operational impact and remaining limitations. Use the PR template. Attach the PR to the current Codex chat when supported.
6. Resolve review conversations and repeat affected checks after fixes. A clean review or green checks do not themselves authorize merging. Leave the PR ready for the user's merge decision unless they explicitly requested the merge. After merge, synchronize local main before starting the next branch; remove local branches only when their work is safely retained.

Typical commands, assuming a clean or deliberately preserved checkout:

```sh
git fetch origin
git switch main
git pull --ff-only origin main
git switch -c docs/example-change
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests/unit -p 'test_*.py' -v
git add <intended-files>
git diff --cached --check
git diff --cached
git commit -m "Describe the completed change"
git push -u origin docs/example-change
```

`<intended-files>` and the example branch are placeholders, not commands to copy literally. Use a connected GitHub PR tool or the GitHub UI to create the PR; gh CLI is optional. Do not use a force push to resolve divergent main history. Inspect and reconcile remote changes through the normal branch/PR process.

## Fresh-context review and re-review

A new OS window displaying the same chat is not new conversation context. Prefer a fresh-context reviewer subagent where available; use a separate fresh chat only when the user specifically wants a user-owned chat. Do not fork the entire author conversation as the review input.

Provide requirements and relevant contracts/constraints, base/head revision or identified uncommitted snapshot, affected paths and tests, observed check references, and a read-only code-review objective. The reviewer inspects actual code and consumer requirements directly, without relying on the author's conclusion of correctness. Return severity, location, defect, consequence and evidence; do not invent findings to fill a quota.

The author/orchestrator investigates each finding, fixes it or documents an evidence-backed rejection/explicit acceptance, and reruns affected checks. Send the updated snapshot and fix diff back for re-review; the same reviewer can verify prior findings and inspect the fix for regressions. Significant redesign can justify another fresh review. Record rounds and findings under harness/code_review/, with execution evidence in the build log. Unresolved required findings prevent completion. No actionable findings means no findings in the reviewed scope, not proof of bug-free software.

## Main-branch protection

Requested settings (verify actual GitHub state; this document is not enforcement):

- Protect branch pattern `main`; require a pull request before merging.
- Apply restrictions to administrators / do not allow bypassing.
- Require review conversation resolution.
- Block force pushes and deletion.
- Keep main writable through compliant PR merges. Do NOT enable GitHub's read-only “Lock branch” option, which would prevent normal contributions.
- Initially require zero human approvals so a solo owner can merge their own reviewed PR; agent review evidence is a repository practice, not a separate human approval. Add required human approvals when an eligible collaborator exists.
- Do not require nonexistent status checks. CI is not configured in the scaffold; enable actual stable checks and verify them before making them required.

If the owner needs to configure or verify protection later: Repository Settings → Branches → add classic protection rule for main (or equivalent active ruleset); configure the above; save; reopen and verify saved settings. Public repositories support branch protection on GitHub Free. Administration needs authenticated browser/API access; SSH push access does not grant a browser session.

Keep actual configuration outcomes in observed execution evidence or the task's final report. If setup is blocked, say which setting is unverified and retain the PR-only contribution rule locally. Never claim the branch is protected merely because this runbook exists.

For this bootstrap, the owner asked the agent not to change GitHub settings. Main protection is owner-managed and was not changed or independently verified. The empty-base push succeeding does not establish whether rules apply to subsequent updates.
