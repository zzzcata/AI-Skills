# GitHub Copilot

This adapter covers GitHub Copilot for coding. For Microsoft 365 Copilot and
consumer Microsoft Copilot, see the [Microsoft Copilot adapter](../microsoft-copilot/README.md).

## GitHub Copilot in VS Code

For versions supporting Agent Skills, install into the target project's
`.github/skills` directory. Run from the AI Skills library root:

```sh
python3 scripts/install.py writing-assistant prioratize-features --target /path/to/project/.github/skills
```

On Windows PowerShell, use your Python launcher and an explicit Windows path:

```powershell
py -3 scripts/install.py writing-assistant prioratize-features --target 'C:\Projects\MyProject\.github\skills'
```

Open the target project in VS Code with GitHub Copilot enabled. Start a new
agent chat and explicitly request a skill, for example:

> Use prioratize-features on only the attached requirements. Begin with backlog
> analysis and ask clarification questions before recommendations that depend on them.

Skill discovery depends on the installed VS Code and Copilot versions and any
organization policies. Consult the [VS Code Agent Skills documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
for current availability and settings. If the agent cannot discover the skill,
attach its `SKILL.md` and relevant supporting files to the chat and explicitly
ask it to follow those instructions. Check the response against the requested
workflow before relying on it.

The installer refuses to replace existing skill directories. Installed skills
are snapshots; update the library first, then deliberately relocate or remove
old installed copies before reinstalling. No Copilot credentials are stored here.
