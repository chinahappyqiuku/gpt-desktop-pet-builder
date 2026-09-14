# Privacy-safe publishing

This Skill is intended to be public and reusable. It must describe the method without carrying any private character instance.

## Keep out of the public package

- real-person reference photos or face crops;
- generated frames derived from a real person's likeness;
- names, nicknames, contact details, chat transcripts, or personal schedules;
- absolute local paths, temporary clipboard paths, and application data paths;
- filled spreadsheets, QA screenshots containing real faces, executables, caches, and API keys;
- metadata that embeds the source file path or account name.

## Safe public contents

- the generic `SKILL.md` workflow;
- blank brief templates with neutral labels;
- generic scripts and JSON schemas;
- synthetic placeholders only when they are clearly marked as placeholders;
- a README that states the Skill is GPT-specific and does not include private assets.

## User-owned private workspace

Keep reference images, filled briefs, generated source frames, cutouts, and executable builds in a separate private project directory. Add those directories to `.gitignore` if the user is working inside a Git repository. Do not solve privacy by renaming a private image; exclude it from the public package entirely.

## Publishing gate

Before a public commit or archive:

1. Run `scripts/check_skill_privacy.py`.
2. Inspect the file list and text scan results.
3. Confirm that no real-person likeness asset is present.
4. Confirm that the target GitHub repository, visibility, and owner are the ones the user intended.
5. Only then push or upload. If the repository target or authentication is unavailable, stop after producing the sanitized local package and report the exact blocker.
