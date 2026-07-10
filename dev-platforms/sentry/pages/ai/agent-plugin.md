---
title: "Agent Plugin"
source: https://docs.sentry.io/ai/agent-plugin.md
path: ai/agent-plugin
---

---
title: "Agent Plugin"
description: "Install the Sentry plugin for your AI coding assistant so it can set up Sentry, find and fix production issues, and configure monitoring, all from a prompt."
url: https://docs.sentry.io/ai/agent-plugin/
---

# Agent Plugin

Whether you're adding Sentry to a new project, debugging a spike in errors, or wiring up alerts, just ask. The plugin gives your assistant the context it needs to do it right.

Supports **Claude Code**, **Cursor**, **Codex**, and **Grok**.

## [Install](https://docs.sentry.io/ai/agent-plugin.md#install)

Run this in your terminal:

```bash
npx @sentry/ai install
```

The installer detects which assistants you have on your machine, lets you pick the ones you want, and wires the plugin into each. Already have it? The same command updates you to the latest version.

Restart your AI tools afterward so they load the plugin.

The plugin configures the [Sentry MCP server](https://mcp.sentry.dev) for you during install, so there's nothing else to connect. A few workflow tasks also need the [GitHub CLI](https://cli.github.com/) (`gh`) for reading and replying to PR comments.

## [What You Can Do](https://docs.sentry.io/ai/agent-plugin.md#what-you-can-do)

**Set up Sentry in any project.** The plugin detects your stack, recommends the right features, and walks through the whole installation, so you're not copy-pasting from docs.

```text
> Add Sentry to my Next.js app
> Set up Sentry in my Rails project
> Add error monitoring to my iOS app
```

**Find and fix production issues.** Query your Sentry environment, triage errors, and fix them in place.

```text
> What are the top errors in the last 24 hours?
> Which issues are affecting the most users?
> Fix the recent Sentry errors
```

**Review code with Sentry context.** Resolve the bugs that Sentry and Seer flag in your pull request comments.

```text
> Review PR #123 and fix the Sentry comments
```

**Configure monitoring.** Set up alerts, instrument your AI and LLM calls, and connect OpenTelemetry pipelines.

```text
> Create a Slack alert for new high-priority issues
> Monitor my OpenAI calls with Sentry
> Set up an OTel Collector with the Sentry exporter
```

## [Remove the Plugin](https://docs.sentry.io/ai/agent-plugin.md#remove-the-plugin)

```bash
npx @sentry/ai remove
```

This only offers the assistants that currently have the plugin and removes just the Sentry plugin, leaving each tool's marketplace registered. Restart your AI tools afterward to drop it.

## [Contributing](https://docs.sentry.io/ai/agent-plugin.md#contributing)

The plugin is built from the [sentry-for-ai](https://github.com/getsentry/sentry-for-ai) repository, the source of truth for every skill and command. To add a skill or fix an existing one, open a pull request there. Skills follow the [Agent Skills specification](https://agentskills.io/specification): each is a directory with a `SKILL.md` file that holds YAML frontmatter and markdown instructions.

