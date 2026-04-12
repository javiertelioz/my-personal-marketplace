# Copilot instructions

## Build, test, and lint

This repository does not currently define build, test, or lint commands in package manifests, task runners, or GitHub Actions. Treat most work here as metadata and documentation maintenance unless new automation is added.

## High-level architecture

- This repository is a portable marketplace for **GitHub Copilot** and **Claude Code**, not a runnable application. The main deliverables are marketplace manifests, plugin manifests, skills, and agent definitions.
- `.github/plugin/marketplace.json` and `.claude-plugin/marketplace.json` are the top-level marketplace indexes. They should describe the same published plugins and point to local plugins via relative `source` paths such as `./plugins/<plugin-name>`.
- Each distributable plugin lives under `plugins/<plugin-name>/`. A plugin is only complete when both `plugins/<name>/plugin.json` and `plugins/<name>/.claude-plugin/plugin.json` exist and stay aligned.
- Skills live at `plugins/<name>/skills/<skill-name>/SKILL.md` and are referenced from plugin manifests via `skills[].entrypoint`.
- Repo-level agents live in `.github/agents/*.md`. They support marketplace maintenance but are separate from the plugin-packaged skills.
- The current seed plugin is `plugins/marketplace-curator/`. Its `scaffold-plugin` skill creates minimal portable plugin skeletons and leaves marketplace publishing as an explicit follow-up step.

## Key conventions

- Use **kebab-case** for plugin names and skill names.
- Use **`1.0.0`** as the initial version for new plugins unless there is a specific reason to do otherwise.
- Keep descriptions short, practical, and installation-friendly.
- Keep the two marketplace manifests aligned **semantically**, not byte-for-byte: the Copilot manifest currently uses a string `owner`, while the Claude manifest uses an owner object. Preserve the schema each file already uses.
- When adding, renaming, unpublishing, or version-bumping a plugin, update both marketplace manifests and both per-plugin manifests together.
- Prefer lightweight, skill-first plugins. Do not add extra files, agents, or MCP configuration unless they materially improve the workflow.
- When scaffolding a new plugin, do not assume it should be published immediately; updating marketplace manifests is a separate action.
