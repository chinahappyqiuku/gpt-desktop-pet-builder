#!/usr/bin/env python3
"""Check that a public Skill package contains no private assets or local paths."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FORBIDDEN_BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff",
    ".xlsx", ".xls", ".csv", ".zip", ".7z", ".exe", ".dll", ".pyc",
}
PRIVATE_TEXT_PATTERNS = {
    "windows_absolute_path": re.compile(r"\b[A-Za-z]:[\\/]"),
    "unix_home_path": re.compile(r"/(?:Users|home)/"),
    "local_temp_or_appdata_path": re.compile(r"(?i)(?:AppData[\\/]|Local[\\/]Temp[\\/])"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="skill directory to inspect")
    args = parser.parse_args()
    root = args.root.resolve()
    forbidden_files: list[str] = []
    text_findings: list[dict[str, object]] = []

    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        relative = str(path.relative_to(root))
        if path.suffix.lower() in FORBIDDEN_BINARY_SUFFIXES:
            forbidden_files.append(relative)
            continue
        try:
            data = path.read_bytes()
            if b"\x00" in data:
                continue
            text = data.decode("utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for name, pattern in PRIVATE_TEXT_PATTERNS.items():
            matches = pattern.findall(text)
            if matches:
                text_findings.append({"file": relative, "kind": name, "count": len(matches)})

    report = {
        "root": str(root),
        "ok": not forbidden_files and not text_findings,
        "forbiddenFiles": forbidden_files,
        "textFindings": text_findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
