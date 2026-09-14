# Desktop pet QA checklist

Run this checklist against the actual files that the runtime will load, not only against the source images.

## File and manifest checks

- Every manifest source exists and maps to exactly one output.
- Every output is RGBA PNG with the intended pixel dimensions.
- Every animation spec references existing frames and has a positive frame duration.
- Frame filenames, action IDs, and ordering are stable and portable across Windows paths.
- The output contains no source reference images, private spreadsheets, API keys, cache folders, or personal paths.

## Alpha and visual checks

- The cutout has both transparent and opaque pixels when transparency is required.
- Corners and outside scenery are transparent unless the brief explicitly requires a full scene.
- Character outlines are intact and there is no matte halo.
- White socks, collars, shoe panels, skin highlights, pale hair, and light-colored props remain opaque.
- Hands, fingers, feet, shoes, straps, bags, and other small accessories are present.
- There are no accidental holes inside the character or foreground props.
- Checkerboard and saturated-background previews show no unexpected rectangular patches.

## Continuity checks

- All frames share the same canvas, anchor, scale, and character order.
- Paired characters preserve the requested hand connection and relative spacing.
- Props stay attached to the correct character or remain in the requested scene layer.
- Motion reads smoothly from frame to frame; no frame has a sudden missing limb or changed outfit.
- The last frame loops cleanly into the first when the action is looping.

## Runtime checks

- Default action loads at startup.
- Hovering the character switches immediately to the default action.
- Timed actions follow the filled schedule and have a documented overlap priority.
- Dragging uses the requested target and sequence; release returns to the requested action.
- Manual action selection, menu behavior, scaling, and exit behavior still work.

## Release checks

- A contact sheet and a concise QA report are produced.
- The project or executable launches from a clean output directory.
- The public Skill package is generic and contains no user likeness assets or identifying material.
