#!/usr/bin/env python3
"""Bundle optional channel context so individually installed skills remain portable."""
from pathlib import Path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = (root / 'profiles/shipshitshow.md').read_bytes()
drift = []
for skill in sorted(root.glob('*/SKILL.md')):
    target = skill.parent / 'references/channel-profile.md'
    if not target.is_file() or target.read_bytes() != source:
        drift.append(skill.parent.name)
        if not args.check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source)
if args.check and drift:
    parser.exit(1, 'Channel profile drift: ' + ', '.join(drift) + '\n')
print('Channel profiles are synchronized.' if not drift else 'Updated: ' + ', '.join(drift))
