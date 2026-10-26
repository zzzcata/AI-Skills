# Codex

From the library root, install selected skills into a project's skill directory:

```sh
python3 scripts/install.py writing-assistant --target /path/to/project/.agents/skills
```

For user-wide installation use `--target "$HOME/.agents/skills"`.
Start a new Codex session if discovery does not refresh. Ask to use the skill by
name (for example, `$writing-assistant`). Check your Codex version's documentation
if skill discovery differs. `AGENTS.md` in this library guides repository work;
it does not itself install the skills into other projects.
