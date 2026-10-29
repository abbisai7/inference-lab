# Development runbook

## Current capabilities

The repository has documentation, three repo-scoped skills, and standard-library foundation validation tooling. The application is not implemented. Run commands below from the repository root using Python 3.9 or newer. No application dependency installation is required for these checks.

```sh
python3 scripts/validate_repo.py
python3 scripts/validate_repo.py --json
python3 -m unittest discover -s tests/unit -p 'test_*.py' -v
```

The validator exits 0 on success and 1 on structural findings. It checks required foundation files, inline relative Markdown file links (excluding fenced examples and remote URLs), named requirement/coverage correspondence, and unfinished or unverified work in Complete records. Two original documentation records retain historical schemas and are explicitly reported as exempt from current completion schema checks. It does not validate reference-style links or anchors, evidence truth, runtime behavior, implicit skill routing, or index synchronization; those require review. It is not wired to CI or a hook.

## Skill checks

The optional bundled skill-creator `quick_validate.py` checks skill metadata/scaffolding. Its path is host-specific; it requires PyYAML. In the initial validation, PyYAML was installed into a temporary directory for the bundled Python only, with no repository runtime dependency. Do not use that ephemeral installation as an application setup instruction. Repository structural/unit checks remain self-contained.

Open this repository in Codex to discover `.agents/skills/`. See [skills](../skills.md) for expected routing, invocation, and limits. File existence does not prove discovery in a different workspace or already-running chat.

## Application command availability

| Operation | Current state |
| --- | --- |
| Install application dependencies | No manifest yet |
| Start API/UI or supporting services | Not implemented |
| Application unit/integration/load/failure tests | Not implemented; existing unit tests cover foundation validator only |
| Application lint/type-check/build | Not configured |
| CI, deployment, scheduled retrospectives | Not configured |

Add exact verified commands, prerequisites, configuration examples without secrets, expected outcomes, shutdown, and troubleshooting as each capability is delivered. Follow [the workflow](../workflow.md) before changing behavior. Never mark a procedure verified without executing it.

Before making changes, follow [the branch-and-PR workflow](contributing.md). The first publication to main is explicitly authorized; all later changes use topic branches and PRs.
