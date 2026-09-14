# Generic runtime contract

The exact application can differ, but generated projects should keep these contracts explicit so the asset pipeline and runtime do not drift apart.

## Action index

```json
{
  "schemaVersion": 1,
  "actions": [
    {
      "id": "action_id",
      "label": "Human-readable label",
      "frameCount": 4,
      "fps": 5,
      "spec": "action_id/animation-spec.json"
    }
  ]
}
```

## Animation spec

```json
{
  "schemaVersion": 1,
  "action": "action_id",
  "fps": 5,
  "loop": true,
  "frames": [
    { "index": 0, "file": "frames/action-id-01.png", "beat": "start" },
    { "index": 1, "file": "frames/action-id-02.png", "beat": "peak" }
  ]
}
```

Use a `sequence` array instead of `frames` when a drag or return motion intentionally repeats a middle frame. Keep frame duration overrides in the spec when a hold is part of the action.

## Cutout manifest

```json
{
  "schemaVersion": 1,
  "stage": "runtime_transparent_extraction",
  "preserveOriginalCanvas": true,
  "assets": [
    {
      "group": "action_id",
      "source": "../actions/action_id/frames/action-id-01.png",
      "output": "actions/action_id/action-id-01.png"
    }
  ]
}
```

When extraction needs a deterministic repair, prefer narrow region metadata such as seeded light-color components or traced masks. Do not put raw user reference paths into a public manifest.

## Scheduling contract

Represent schedule rules as local-time half-open intervals (`start <= now < end`) and document overlap priority. If the user asks for overlapping intervals, preserve their stated priority or ask them to resolve it before implementation.
