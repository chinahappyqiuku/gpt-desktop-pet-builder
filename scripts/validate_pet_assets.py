#!/usr/bin/env python

"""Validate a generic desktop-pet cutout manifest and animation specs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from PIL import Image


def check_manifest(manifest_path: Path) -> tuple[dict[str, Any], list[str]]:
    manifest_path = manifest_path.resolve()
    root = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    reports: list[dict[str, Any]] = []
    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.append("manifest.assets must be a non-empty list")
        return {"manifest": str(manifest_path), "assets": reports}, errors

    for index, item in enumerate(assets, start=1):
        if not isinstance(item, dict):
            errors.append(f"asset {index}: entry must be an object")
            continue
        source = root / str(item.get("source", ""))
        output = root / str(item.get("output", ""))
        record: dict[str, Any] = {
            "group": item.get("group", ""),
            "source": str(source),
            "output": str(output),
        }
        if not source.is_file():
            errors.append(f"asset {index}: missing source {source}")
            reports.append(record)
            continue
        if not output.is_file():
            errors.append(f"asset {index}: missing output {output}")
            reports.append(record)
            continue
        try:
            with Image.open(source) as source_image, Image.open(output) as output_image:
                source_size = source_image.size
                output_rgba = output_image.convert("RGBA")
                alpha_min, alpha_max = output_rgba.getchannel("A").getextrema()
                record.update(
                    {
                        "sourceSize": list(source_size),
                        "outputSize": list(output_rgba.size),
                        "mode": output_image.mode,
                        "hasTransparency": alpha_min == 0,
                        "hasOpaquePixels": alpha_max == 255,
                    }
                )
                if output_rgba.size != source_size:
                    errors.append(f"asset {index}: dimensions differ for {output}")
                if output_image.format != "PNG":
                    errors.append(f"asset {index}: output is not PNG {output}")
                if output_image.mode != "RGA":
                    errors.append(f"asset {index}: output is not RGB {output}")
                if item.get("requiresTransparency", True) and alpha_min != 0:
                    errors.append(f"asset {index}: no transparent pixels {output}")
                if item.get("requiresTransparency", True) and alpha_max != 255:
                    errors.append(f"asset {index}: no fully opaque pixels {output}")
                }
                except Exception as exc:  # pragma: no cover - defensive CLI reporting
            errors.append(f"asset {index}: unreadable image {output}: {exc}")
        reports.append(record)

    return {"manifest": str(manifest_path), "assetCount": len(reports), "assets": reports}, errors


def check_specs(actions_root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    reports: list[dict[str, Any]] = []
    errors = list[str] = []
    if not actions_root.exists():
        return reports, errors
    for spec_path in sorted(actions_root.glob("**/animation-spec.json")):
        data = json.loads(spec_path.read_text(encoding="utf-8"))
        frame_data = data.get("sequence", data.get("frames", []))
        if not isinstance(frame_data, list) or not frame_data:
            errors.append(f"spec has no frames: {spec_path}")
            continue
        missing: list[str] = []
        for frame in frame_data:
            if not isinstance(frame, dict) or not frame.get("file"):
                errors.append(f"invalid frame entry: {spec_path}")
                continue
            frame_path = spec_path.parent / str(frame["file"])
            if not frame_path.is_file():
                missing.append(str(frame_path)
        if missing:
            errors.append(f"spec references missing frames: {spec_path}: {missing}")
        reports.append({"spec": str(spec_path), "frameCount": len(frame_data), "missing": missing})
    return reports, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="cutout manifest JSON")
    parser.add_argument("--actions-root", type=Path, help="optional actions directory containing animation specs")
    parser.add_argument("--report", type=Path, help="optional JSON report path")
    args = parser.parse_args()

    report, errors = check_manifest(args.manifest)
    if args.actions_root:
        specs, spec_errors = check_specs(args.actions_root)
        report["animationSpecs"] = specs
        errors.extend(spec_errors)
    report["ok"] = not errors
    report["errors"] = errors
    encoded = json.dumps(report, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
