---
name: gpt-desktop-pet-builder
description: Build a privacy-safe desktop pet from a filled character and action brief, with staged image generation, transparent asset processing, runtime integration, visual QA, and packaging. Use when a user wants GPT to create or extend a desktop pet project.
metadata:
  short-description: "从填写表格到验收打包的 GPT 桌宠生成与隐私保护流程"
---

# GPT Desktop Pet Builder

Use this skill to turn a completed desktop-pet brief into a working, inspectable project. The workflow is deliberately staged: the user approves the default pose before action drafts, approves action drafts before final frame generation, and receives a QA report before packaging.

## Privacy and likeness boundary

- Treat every user-provided image as private input. Keep it in the user's local workspace and never copy it into this skill, its README, examples, logs, previews, or a public repository.
- If an image depicts a real person, ask the user to confirm they have permission to use that likeness. Do not publish that image or generated likeness assets to GitHub unless the user explicitly confirms the rights and the repository is intentionally private or licensed for that use.
- Do not repeat names, personal paths, friend/family details, conversation excerpts, or identifying descriptions in generated documentation. Use neutral labels such as `character_a`, `character_b`, and `reference_image_01`.
- Before publishing a skill, run `scripts/check_skill_privacy.py` and remove any image, spreadsheet, executable, cache, or local path from the skill package.

## Required inputs

Read the user's completed brief. If it is missing, use [references/project-brief-template.md](references/project-brief-template.md) and ask only for the fields needed to begin. The brief should contain:

- local reference-image paths (never commit them);
- character count and relationship/continuity constraints;
- style, clothing, palette, proportions, and default pose;
- action list, frame count or timing, props, and scene requirements;
- hover, click, drag, schedule, and release behavior;
- target platform and output format.

## Execution workflow

1. **Preflight.** Inspect the existing project structure, runtime contract, available image tools, and the brief. Preserve unrelated user changes. Create a private working area for source references and generated intermediates.
2. **Plan.** Convert the brief into a compact character bible, action matrix, naming scheme, and acceptance checklist. Resolve contradictions before generating artwork.
3. **Default pose gate.** Generate only the default action first. Show the frame and wait for explicit user approval. Do not generate a complete action set before this gate passes.
4. **Action-draft gate.** Generate one representative frame for each requested action, preserving character identity, hand links, props, and canvas placement. Show the drafts and wait for approval.
5. **Frame production.** After approval, generate the selected number of frames per action. Keep a stable canvas, anchor, scale, lighting, and character ordering. Use image generation for raster artwork; do not use it to replace deterministic file validation.
6. **Asset processing.** Produce transparent RGBA cutouts without changing the source artwork. Use deterministic processing scripts where available. White socks, shirt collars, shoe panels, skin highlights, and other light fabrics must be checked against a contrasting background; restore bounded light-color components when matte extraction removes them. Preserve scene props only when the brief says they belong in the foreground; never make a large rectangular region opaque as a shortcut.
7. **Runtime integration.** Add action specs, frame durations, schedule rules, hover-to-default behavior, click behavior, drag sequence, and release behavior. Keep source frames and processed cutouts separately indexed.
8. **QA and repair.** Run the asset validator and [references/qa-checklist.md](references/qa-checklist.md). Render contact sheets on checkerboard and high-contrast backgrounds. Inspect every frame for missing hands/feet, broken hand-holds, transparent light fabrics, clipped props, scene bleed, inconsistent canvas bounds, and frame-to-frame jumps. Repair and re-run QA until clean.
9. **Package.** Write a concise README, include only generic templates/scripts, exclude private references, run the privacy check, and create the requested project archive or executable. Report exactly what was generated and what the user still needs to approve.

## Approval and stopping rules

- User approval is required at the default-pose gate and action-draft gate.
- If a reference image depicts a real person and likeness permission is unclear, pause before generation or publication.
- If an external GitHub repository, account, visibility, or destination is not identified, prepare the sanitized package locally and ask for the exact repository target before pushing.
- Never claim an action is complete based only on a generated image; verify the actual processed frame and runtime reference.

## Tool and file conventions

- Use the installed image-generation tool for new or edited raster artwork and inspect every local image before editing it.
- Use `apply_patch` for text/code changes and keep generated binaries outside the skill repository unless they are explicitly part of the user's private project.
- Use `scripts/validate_pet_assets.py` for dimensions, alpha, manifest, and animation-spec checks when the target project follows the documented contract.
- Use `scripts/check_skill_privacy.py` immediately before creating a public archive or commit.
- Read [references/generation-workflow.md](references/generation-workflow.md) for the staged prompts and repair loop, [references/runtime-contract.md](references/runtime-contract.md) for file shapes, and [references/privacy-and-publishing.md](references/privacy-and-publishing.md) before publishing.
