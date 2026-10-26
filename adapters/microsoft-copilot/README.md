# Microsoft Copilot

This adapter covers Microsoft 365 Copilot and consumer Microsoft Copilot.
Keep canonical skills in `skills/`; use the workflows below to supply their
instructions to Microsoft Copilot.

## Use a skill in chat


The `.github/skills` installation described in the [GitHub Copilot adapter](../copilot/README.md) targets its coding workflow.
It does not install anything into Microsoft 365 Copilot, Word, Teams, or the
consumer Copilot chat application.

For a chat workflow, paste the contents of the selected `SKILL.md` into the chat,
or attach it if that interface supports the file type. Include any referenced
supporting files and your task inputs. Explicitly ask Copilot to apply the
instructions to those inputs. File support and context limits vary by product,
license, and tenant policy; manual context is not automatic skill discovery.

## Persistent organizational agents

For a persistent organizational agent, use your organization's supported agent
builder (for example Copilot Studio). Adapt the skill body to that builder's
instruction field, configure approved knowledge and tools separately, and test
on representative inputs. This repository does not deploy or configure such an
agent, and copying a SKILL.md alone does not configure its knowledge or tools.
