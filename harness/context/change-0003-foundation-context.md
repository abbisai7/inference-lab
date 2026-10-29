# Context: Foundation finalization

## Material decisions and constraints

- The user finalized the full harness and omitted PROMPTS.md. Skills replace reusable prompt procedures; see [ADR-0004](../../docs/decisions/0004-final-foundation-and-skills.md).
- Context records material discoveries and rationale, not routine progress or copied plans. The build log owns observed evidence, and build records link verdicts to it.
- The user wants selective multi-agent planning/implementation/testing/validation with bounded context. More agents may increase token use; no savings are established. See [orchestration](../../docs/orchestration.md).
- This chat started outside the repository. Creating `.agents/skills/` does not prove the current chat has discovered those skills. Verify availability after opening the repository in Codex; implicit routing remains unmeasured.
- System and bundled Python lacked PyYAML. Metadata generation worked with an explicit skill name; validator-only PyYAML was installed in a temporary directory for bundled Python, without adding app dependencies. Do not make ephemeral host paths part of application setup.

## Downstream implications

Application implementation has not started. Next create the Phase 01 streaming-chat record and choose actual runtime commands there. Current unit tests cover foundation validation only; no chat/auth/load results exist. Native model-side cancellation must be measured when inference is implemented, rather than assuming closing HTTP always stops model work.

## Evidence references

See the [foundation record](../build/change-0003-finalize-foundation.md), [build log](../build-log.md), and [review](../code_review/change-0003-foundation-review.md). These observations guide later work but do not establish runtime readiness.
