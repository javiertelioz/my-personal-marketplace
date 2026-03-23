# scaffold-plugin

## Purpose

Generate a minimal, portable plugin skeleton compatible with both GitHub Copilot and Claude Code.

## Input

| Field  | Required | Description                                       |
|--------|----------|---------------------------------------------------|
| `name` | yes      | Plugin name in kebab-case (e.g. `my-cool-plugin`) |

## Validation

- The name **must** be kebab-case: lowercase letters, digits, and hyphens only (`^[a-z0-9]+(-[a-z0-9]+)*$`).
- Reject names that contain uppercase letters, underscores, spaces, or leading/trailing hyphens.
- If the name is invalid, stop and report the validation error before creating any files.

## Output structure

Creates exactly these files under `plugins/<name>/`:

```
plugins/<name>/
  plugin.json
  .claude-plugin/
    plugin.json
  skills/
    .gitkeep
```

### `plugins/<name>/plugin.json`

```json
{
  "name": "<name>",
  "version": "1.0.0",
  "description": "Short description of <name>.",
  "skills": []
}
```

### `plugins/<name>/.claude-plugin/plugin.json`

Identical content to `plugins/<name>/plugin.json`.

### `plugins/<name>/skills/.gitkeep`

Empty file. Acts as a placeholder so the `skills/` directory is tracked by git.

## Rules

- Do **not** create README, CHANGELOG, tests, examples, badges, or any other optional files.
- Do **not** modify any marketplace manifest (`marketplace.json`) unless the caller explicitly includes the instruction `--publish`.
- Keep `description` in `plugin.json` as a short placeholder; the author fills it in manually.
- Do not add `skills` entries to `plugin.json` at scaffold time; the author adds them when the first skill is ready.

## Example invocation

```
scaffold-plugin my-data-tool
```

Expected result: three files created under `plugins/my-data-tool/`, no manifests touched.
