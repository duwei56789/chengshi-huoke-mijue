#!/usr/bin/env python3
"""Build a WorkBuddy-uploadable skill ZIP from this repository.

Usage:
    python scripts/build_zip.py

Only the Python 3 standard library is required. The archive root contains a
single skill folder whose name matches the `name` field in SKILL.md; this is
required for WorkBuddy / Open Platform to parse the package correctly.
"""

import base64
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILL_ID = "baishu-chengshi-mijue"
DIST = REPO / "dist"
ZIP_PATH = DIST / "chengshi-huoke-skill-public.zip"
B64_PATH = DIST / "chengshi-huoke-skill-public.zip.b64"


def main() -> None:
    skill = REPO / "SKILL.md"
    refs = sorted((REPO / "references").glob("*.md"))
    if not skill.is_file():
        raise SystemExit("SKILL.md not found in the repository root")
    if not refs:
        raise SystemExit("no reference documents found in references/")

    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write(skill, f"{SKILL_ID}/SKILL.md")
        for ref in refs:
            archive.write(ref, f"{SKILL_ID}/references/{ref.name}")

    B64_PATH.write_text(
        base64.b64encode(ZIP_PATH.read_bytes()).decode("ascii"),
        encoding="ascii",
    )

    print(f"Wrote {ZIP_PATH} ({ZIP_PATH.stat().st_size} bytes)")
    print(f"Wrote {B64_PATH}")
    with zipfile.ZipFile(ZIP_PATH) as archive:
        for name in archive.namelist():
            print(f"  {name}")


if __name__ == "__main__":
    main()
