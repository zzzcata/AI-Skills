#!/usr/bin/env python3
"""Validate the library's intentionally small Agent Skills metadata subset."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def validate(skill):
    errors = []
    if skill.is_symlink() or any(p.is_symlink() for p in skill.rglob('*')):
        return [f'{skill.name}: symlinks are not supported']
    entry = skill / 'SKILL.md'
    if not entry.is_file():
        return [f'{skill.name}: missing SKILL.md']
    try:
        text = entry.read_text(encoding='utf-8')
        lines = text.splitlines()
        end = lines.index('---', 1) if lines and lines[0] == '---' else -1
        if end < 0:
            return [f'{skill.name}: missing front matter']
        meta = {}
        for line in lines[1:end]:
            key, sep, value = line.partition(':')
            if not sep or key not in {'name', 'description'} or key in meta:
                errors.append(f'{skill.name}: unsupported or duplicate metadata: {line}')
            meta[key] = value.strip()
        if meta.get('name') != skill.name or not NAME.fullmatch(skill.name) or len(skill.name) > 64:
            errors.append(f'{skill.name}: invalid or mismatched name')
        if not meta.get('description') or len(meta['description']) > 1024:
            errors.append(f'{skill.name}: description must contain 1–1024 characters')
        if not '\n'.join(lines[end + 1:]).strip():
            errors.append(f'{skill.name}: missing instructions')
        for doc in skill.rglob('*.md'):
            for link in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', doc.read_text(encoding='utf-8')):
                url = urlsplit(link.strip('<>'))
                if url.scheme or url.netloc or not url.path:
                    continue
                target = (doc.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(skill.resolve()) or not target.exists():
                    errors.append(f'{doc.relative_to(ROOT)}: missing or escaping link: {link}')
    except (ValueError, OSError, UnicodeError) as exc:
        errors.append(f'{skill.name}: {exc}')
    return errors


def main():
    skills = sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir())
    errors = [error for skill in skills for error in validate(skill)]
    if not skills:
        errors.append('No skills found')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Validated {len(skills)} skill(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
