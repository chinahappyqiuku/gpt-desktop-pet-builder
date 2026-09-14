# Staged generation workflow

This is the reusable interaction script for GPT. Keep the gates visible to the user and do not silently skip them.

## Phase A: preflight and character bible

1. Read the completed brief and list missing or contradictory fields.
2. Inspect each local reference image. Record only visual production facts: number of characters, pose, clothing, palette, proportions, and continuity constraints.
3. Create an anonymous character bible. Do not copy names, filenames containing personal information, face descriptions beyond the requested visual facts, or the reference images into the skill package.
4. Convert the action matrix into stable IDs, filenames, frame counts, loop rules, and a time schedule.

## Phase B: approval gates

### Default frame

Generate one neutral/default frame with the final canvas, character placement, clothing, and transparent-background intent. Present it as a preview and ask for explicit approval or corrections.

### Action drafts

After the default frame is approved, generate one representative frame per action. Check:

- identity, clothing, and proportions remain stable;
- linked hands or paired characters stay connected;
- props appear in front when required;
- feet touch or leave the ground as intended;
- expressions match the action;
- the canvas anchor does not drift.

Ask for approval before generating the remaining frames.

### Final frame set

Generate the approved number of frames. Prefer small, coherent frame counts over unnecessary near-duplicates. Keep all frames at one pixel size and use the same composition prompt plus a frame-specific motion clause.

## Prompt pattern

Compose prompts from these blocks:

1. **Identity block:** use the approved reference image(s), neutral labels, and stable clothing/accessory facts.
2. **Style block:** illustration style, lighting, line quality, palette, and background intent.
3. **Continuity block:** canvas size, character order, relative scale, hand links, and objects that must not change.
4. **Action block:** the exact pose, expression, limb direction, and prop interaction for this frame.
5. **Negative block:** no extra characters, no missing limbs, no fused hands, no duplicate props, no cropped feet, no text, no watermark, and no background elements that were not requested.

Do not put real-person names or private file paths into a reusable prompt template. Pass private references to the image tool through its supported local-image mechanism only.

## Transparent processing and repair loop

1. Save the generated source PNG separately from its processed RGBA cutout.
2. Run the deterministic extraction tool and preserve the original canvas size.
3. Render the cutout on a checkerboard and on a saturated green or magenta background.
4. Pay special attention to white socks, collars, shoe panels, highlights, pale hair, and light props. Matte extraction commonly removes these when their colors resemble the background.
5. Restore only bounded, source-connected light-color components or explicitly traced masks. Avoid opaque rectangles that include background.
6. Re-render and compare source/cutout side by side. Repeat until the result passes the QA checklist.

## Repair decision tree

- Missing hand, foot, shoe, or accessory: repair the source frame first; then regenerate the cutout.
- Light fabric becomes transparent: restore the bounded light component from the source and verify on a saturated background.
- Foreground table, chair, door, or floor disappears: preserve the requested scene region; keep the outside background transparent.
- Character shifts between frames: align canvas and anchor before changing the artwork.
- A prop or limb appears/disappears between frames: regenerate the affected frame with a continuity constraint, then re-run the entire action QA.
