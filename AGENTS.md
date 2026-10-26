# Working in AI Skills

This repository stores portable AI instructions, not a running application.
Use the existing checkout; do not create a worktree unless explicitly requested.

- Keep canonical skills under `skills/<name>/SKILL.md`.
- Use lowercase hyphenated names and single-line `name` and `description` metadata.
- Keep instructions independent of vendors; put discovery details in `adapters/`.
- Never add credentials or machine-specific absolute paths to skills.
- Preserve existing installed files; the installer must never silently overwrite them.
- Run `python3 scripts/validate.py` after changes and exercise helper behavior when changing scripts.
- No dependency installation or service startup is needed. Python 3.10+ is sufficient.
