# Marketplace maintenance rules

This repository is a curated marketplace for GitHub Copilot and Claude Code.

## Goals

- Keep the repository easy to install and easy to extend.
- Prefer shared structures that work in both ecosystems.
- Keep naming consistent and kebab-case.

## Required conventions

- Every distributable plugin must live under `plugins/<plugin-name>/`.
- Every plugin must include a root `plugin.json` for GitHub Copilot CLI.
- Every Claude-compatible plugin must include `.claude-plugin/plugin.json`.
- Every skill must live in `skills/<skill-name>/SKILL.md`.
- Marketplace entries must be kept in sync in both:
  - `.github/plugin/marketplace.json`
  - `.claude-plugin/marketplace.json`
- Prefer relative plugin sources such as `./plugins/<plugin-name>`.

## When adding a new plugin

1. Validate the plugin name is kebab-case.
2. Create the plugin skeleton.
3. Add or update the marketplace entry.
4. Ensure descriptions are short and actionable.
5. Do not add MCP configuration unless the plugin really needs it.
6. Keep the initial version at `1.0.0` unless there is a reason to change it.

## Review checklist

- Is the plugin name unique?
- Does the plugin have at least one skill or one agent?
- Are both marketplace manifests aligned?
- Are instructions clear enough for automatic selection?
- Are there any duplicated versions or conflicting names?
