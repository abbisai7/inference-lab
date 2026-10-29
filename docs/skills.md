# Repository workflow skills

Skills live under `.agents/skills/`, versioned with this project. Open Codex with this repository as its workspace so repo-scoped skill discovery applies. If a newly created skill is not listed, reload/start a fresh repository session and inspect discovery; do not assume it has loaded merely because the files exist. This chat did not begin in the repository, so discovery here is not claimed.

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [harness-author](../.agents/skills/harness-author/SKILL.md) | Plan a change or improve the engineering harness | Planning does not implement application code |
| [change-delivery](../.agents/skills/change-delivery/SKILL.md) | Implement and verify a selected change, including relevant delegated work | Does not launch unrelated phases or deployments |
| [workflow-retrospective](../.agents/skills/workflow-retrospective/SKILL.md) | Diagnose actual workflow friction and propose improvements | Initial assessment is read-only; does not silently rewrite skills |

The descriptions allow implicit matching. Explicit invocation is useful when routing matters: “Use $harness-author to plan streaming chat”; “Use $change-delivery to implement the selected record”; “Use $workflow-retrospective to evaluate Phase 01.” Names are examples of invocation, not commands that run automatically.

Skills hold procedures; AGENTS.md holds persistent rules; build records hold task requirements; scripts perform repeatable mechanical checks. No PROMPTS.md is needed. Skills are not schedulers, hard enforcement, or a guarantee of completeness. Test scope boundaries and revise them from observed failures rather than adding universal rules for every example.

## Validation and scenario coverage

`python3 scripts/validate_repo.py` checks repository structure and local Markdown file links. Unit tests exercise validator behavior with isolated fixture repositories. Skill-creator's `quick_validate.py` checks each skill's basic frontmatter/structure when that bundled tool and PyYAML are available; it is not a repository runtime dependency.

Review skills with realistic requests: a planning-only request must produce no application edits; implementation must reconcile requirements without claiming unrun checks; a retrospective must distinguish observed evidence from expected behavior and remain read-only initially. Record outcomes and limitations in the foundation review. Broad routing and long-term reliability require future real usage; scenario review does not prove implicit invocation reliability.

## Foundation validation evidence

All three skills passed the bundled skill-creator validator. An independent static review evaluated planning-only, unavailable-runtime implementation, and read-only retrospective scenarios. A separate agent actually exercised harness-author in an isolated copied fixture, producing a Draft plan with Pending application criteria and no application code. Delivery and retrospective were not executed end to end. See [foundation review](../harness/code_review/change-0003-foundation-review.md) and [build log](../harness/build-log.md). Implicit discovery/routing still needs observation in a fresh repository session.

After the empty-main bootstrap, all three skills follow the [branch-and-PR workflow](runbooks/contributing.md) for authorized repository edits. Initial-main source publication is not the normal delivery path.
