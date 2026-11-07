"""Run from the pinned upstream source checkout; do not execute a modified builder."""
from pathlib import Path
import hashlib
import json
import sys

recipe=Path(__file__).resolve().parent
manifest=json.loads((recipe/'inputs.json').read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(recipe/'edp-trace.patch')==manifest['patch_sha256'],'Unexpected patch'
key='patched_sha256' if '--patched' in sys.argv else 'base_sha256'
for name, expected in manifest[key].items():
    assert sha(Path('WhateverXe')/name)==expected,'Source differs: '+name
print('PASS: '+key+'; pinned patch')
