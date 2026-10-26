# AI Skills

A portable library of reusable AI skills. Keep the canonical instructions in
`skills/<name>/SKILL.md` and supporting material beside them. Adapters describe
how to make those skills available to particular tools.

## Quick start

Requires Python 3.10+ and Git. No packages, credentials, or running services are required.

```sh
python3 scripts/validate.py
python3 scripts/install.py writing-assistant --target /path/to/project/.agents/skills
```

The installer copies selected skills into an explicit target directory. Existing
entries are never overwritten. Installed copies are snapshots: edit this library,
validate, then deliberately remove or relocate an old copy before reinstalling.
Do not store credentials in skills or supporting files.

## Layout

- `skills/`: canonical Agent Skills format instructions and optional `references/`, `scripts/`, or `assets/`.
- `adapters/`: discovery and installation guidance for each tool.
- `scripts/`: dependency-free validation and installation helpers.
- `AGENTS.md`: instructions for AI tools working on this repository.

## Add a skill

Create `skills/<lowercase-hyphen-name>/SKILL.md` with this header:

```markdown
---
name: example-skill
description: Explain when to use this skill and what it accomplishes.
---

# Example skill

Give actionable instructions, inputs, expected output, and verification steps.
```

Use plain, single-line `name` and `description` values. This library deliberately
uses a small metadata subset so validation needs no YAML dependency. Keep the
name equal to the directory name (at most 64 characters). Use relative Markdown
links for supporting files. Keep tool-specific APIs and installation details in
adapters; describe any unavailable capability and its fallback in the skill.

Run `python3 scripts/validate.py` before committing. CI runs the same check.
Validation checks structure, metadata, and local Markdown link destinations;
it cannot establish that a skill produces good answers. Try each skill on a
representative task in your chosen tool before relying on it.

## Tool support

See [Codex](adapters/codex/README.md), [Claude Code](adapters/claude/README.md),
[Cursor](adapters/cursor/README.md), and [GitHub Copilot](adapters/copilot/README.md),
and [Microsoft Copilot](adapters/microsoft-copilot/README.md).
Microsoft Copilot has its own adapter for Microsoft 365 and consumer chat workflows. Automatic discovery depends on the product
and version. For other tools, attach or
paste a skill and its relevant supporting files, or create an adapter matching
that tool's documented discovery mechanism.

## Available skills

- [writing-assistant](skills/writing-assistant/SKILL.md): Draft and revise clear writing.
- [prioratize-features](skills/prioratize-features/SKILL.md): Review supplied requirements, preserve contractual coverage, and recommend evidence-based feature priorities and scope simplifications. The original skill name is preserved.
