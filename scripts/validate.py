#!/usr/bin/env python3
"""Validate standalone skill metadata, local references and bundled context."""
from pathlib import Path
import re
import yaml
root = Path(__file__).resolve().parents[1]
errors = []
for entry in sorted(root.glob('*/SKILL.md')):
    content = entry.read_text()
    front = re.match(r'^---\n([\s\S]*?)\n---\n', content)
    try:
        meta = yaml.safe_load(front.group(1)) if front else {}
    except yaml.YAMLError as exc:
        errors.append(f'{entry}: invalid YAML: {exc}')
        continue
    if not isinstance(meta, dict) or meta.get('name') != entry.parent.name or not isinstance(meta.get('description'), str) or not meta['description'].strip():
        errors.append(f'{entry}: missing/mismatched name or description')
    if not re.fullmatch('[a-z0-9-]{1,64}', entry.parent.name):
        errors.append(f'{entry}: invalid skill name')
    for doc in entry.parent.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            if not link.startswith(('https://', 'http://', '#')) and not (doc.parent / link.split('#')[0]).is_file():
                errors.append(f'{doc}: missing reference {link}')
    ui = yaml.safe_load((entry.parent / 'agents/openai.yaml').read_text())['interface']
    if '$' + entry.parent.name not in ui.get('default_prompt', ''):
        errors.append(f'{entry}: default_prompt missing skill name')
if errors:
    raise SystemExit('\n'.join(errors))
print('Validated skill metadata and local references.')
