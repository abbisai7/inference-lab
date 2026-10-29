# Review records

Reviews answer what was inspected, what was wrong or missing, and how findings were resolved. They are not second plans, progress logs, or generic implementation summaries. Create a review only when one actually occurs; `README.md` explains the convention, not proof of review.

Use a filename matching the build record, optionally with a review round. Identify scope, reviewer role, independent versus self-review, revision and dirty-state/snapshot evidence, named requirements examined, checks inspected/run, and review limitations.

For each actionable finding record severity, location, observed defect, consequence, supporting evidence, remediation, status (Open/Resolved/Accepted), and follow-up verification. Accepted findings need explicit rationale and appropriate user agreement if they materially alter requirements. Preserve history and link fixes/rechecks. If there are no actionable findings, state the inspected scope and limits; do not infer sign-off from an empty folder.

Review/validation asks whether the actual implementation satisfies ALL named requirements and whether tests establish their claims. Testing exercises behavior; both are useful. A different agent provides a fresh review perspective, not a guarantee of correctness. Changes after the examined snapshot require affected checks and findings to be revisited.

The build log links the review verdict and observed checks; the build record links the review and completion evidence. Detailed findings live here, not copied into all three files.

For substantive code, start with a fresh-context reviewer and a focused contract/diff handoff. Track each finding through author investigation, fix or evidence-backed disposition, affected test reruns, and reviewer recheck of the updated snapshot. Re-review must inspect the fix for regressions, not merely mark old comments resolved. See [contribution workflow](../../docs/runbooks/contributing.md).
