#!/usr/bin/env python3
"""Copy named, validated skills to an explicit destination without replacement."""
import argparse
import shutil
import sys
from pathlib import Path
from validate import NAME, ROOT, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='+', help='Skill directory names')
    parser.add_argument('--target', required=True, type=Path, help='Destination skills directory')
    args = parser.parse_args()
    target = args.target.expanduser().resolve()
    sources = []
    for name in dict.fromkeys(args.skills):
        if not NAME.fullmatch(name) or len(name) > 64:
            parser.error(f'Invalid skill name: {name}')
        source = ROOT / 'skills' / name
        if not source.is_dir():
            parser.error(f'Unknown skill: {name}')
        errors = validate(source)
        if errors:
            parser.error('; '.join(errors))
        destination = target / name
        if target.is_relative_to(source.resolve()) or destination == source.resolve():
            parser.error('Target must be outside the selected source skill')
        if destination.exists() or destination.is_symlink():
            parser.error(f'Refusing to overwrite: {destination}')
        sources.append(source)
    try:
        target.mkdir(parents=True, exist_ok=True)
        for source in sources:
            destination = target / source.name
            # Exclusive creation prevents overwrites even if another installer races us.
            destination.mkdir()
            try:
                shutil.copytree(source, destination, dirs_exist_ok=True)
            except Exception:
                shutil.rmtree(destination)
                raise
            print(f'Installed {source.name} into {destination}')
    except OSError as exc:
        print(f'Installation failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
