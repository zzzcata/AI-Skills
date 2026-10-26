# Cursor

For Cursor versions supporting Agent Skills, run from the library root:

```sh
python3 scripts/install.py writing-assistant --target /path/to/project/.cursor/skills
```

Start a new agent session if needed and ask to use `writing-assistant`.
Confirm skill support in your installed Cursor version. For versions without
skill discovery, attach the relevant SKILL.md and supporting files as context.
This library does not generate Cursor rules, which have different semantics.
