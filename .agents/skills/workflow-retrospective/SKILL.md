---
name: workflow-retrospective
description: Assess completed phases or repeated delivery failures using actual records, code, checks, and review evidence. Recommend focused workflow or skill improvements; initial assessment is read-only, not a generic code review or automatic rewrite.
---

# Workflow Retrospective

Begin read-only. Inspect applicable instructions, selected records, relevant build-log events, context, reviews, code/check evidence, and invoked skills. Follow [the workflow](../../../docs/workflow.md) and [skill guide](../../../docs/skills.md). Select material evidence rather than loading all history.

Audit the AGENTS.md reading map and docs index for missing, stale, or misrouted guidance; inspect relevance, not only whether links resolve. Recommend narrow corrections while preserving the initial read-only boundary.

Compare intended and observed execution: requirement omissions, misleading completion, repeated discovery, routing mistakes, drift, unavailable checks, review gaps, measured cost/time, and useful safeguards. Distinguish observed evidence, historical reports, and hypotheses. Do not manufacture root causes or savings from estimates.

Return a concise assessment with concrete examples and linked evidence, impact, contributing conditions, existing safeguard, recommended owner (instruction/skill/test/validator/docs), smallest correction, added overhead, and proposed validation. Explain what worked as well as what failed. Prefer narrowing an existing procedure over overlapping skills or universal rules.

Do not mutate code, harness, skills, global settings, or external systems during the initial assessment. If the user explicitly requests improvements, first report the assessment, then use a bounded record for supported changes under normal authorization. A request to assess is not permission to rewrite.

Recommend retrospectives after substantial phases or repeated failures. Skills are not schedulers; no recurring automation without a user request. Disclose unavailable evidence and do not claim broad routing reliability from a scenario review.

If authorized improvement implementation follows the assessment, use a topic branch and PR under the repository contribution workflow; do not edit or push main directly. Assessment alone remains read-only.
