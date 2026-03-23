# Claude workspace guide

This repository hosts a portable marketplace for GitHub Copilot and Claude Code.

## Primary objective

Help maintain and grow the marketplace with minimal duplication.

## Preferred approach

- Reuse shared folder conventions whenever possible.
- Keep marketplace manifests aligned between Copilot and Claude.
- Favor simple relative sources for plugins in the same repository.
- Keep plugin descriptions concise and installation-friendly.

## Safe defaults

- Use kebab-case for plugin and skill names.
- Use `1.0.0` as the initial version for new plugins.
- Keep the first iteration skill-first and lightweight.
- Add agents only when they improve discoverability or workflow quality.

## Files that matter most

- `.claude-plugin/marketplace.json`
- `.github/plugin/marketplace.json`
- `plugins/*/plugin.json`
- `plugins/*/.claude-plugin/plugin.json`
- `plugins/*/skills/**/SKILL.md`
- `.github/agents/*.agent.md`
