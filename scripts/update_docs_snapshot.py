#!/usr/bin/env python3
"""Fetch Maton docs corpus and emit only reviewable metadata."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

URL = "https://docs.maton.ai/llms-full.txt"
TARGET = Path("references/maton-docs-snapshot.json")

with urlopen(URL, timeout=90) as response:
    body = response.read()
TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(json.dumps({
    "source": URL,
    "bytes": len(body),
    "sha256": hashlib.sha256(body).hexdigest(),
}, indent=2) + "\n")
print(TARGET)
