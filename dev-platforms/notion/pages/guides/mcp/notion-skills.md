---
title: "Use Notion Skills with MCP"
source: https://developers.notion.com/guides/mcp/notion-skills
path: guides/mcp/notion-skills
---

Learn how MCP clients create, find, and use reusable instructions stored as Notion pages.

A Notion Skill is a page you own with instructions for a repeatable workflow. You can maintain it yourself or ask an assistant to do it for you.

## Create a Skill

To create a page as a Skill, call `notion-create-pages` with `is_skill: true` on that page. Before writing it, read the `notion://docs/skills` MCP resource for focused guidance on when a Skill is appropriate and how to write instructions another assistant can follow.

If the MCP client cannot read resources, pass `notion://docs/skills` to `notion-fetch` instead. Do not send this URI to a general web-fetching tool.

To turn an existing page into a Skill without changing its content, call `notion-convert-page-to-skill` with the page's full Notion URL. The connected user must be able to edit the page.

## Find and use a Skill

If the user provides an exact Skill URL, call `notion-fetch` directly. Otherwise, call `notion-search-skills` with the Skill name or a short description of the task. Omit the query to list up to 10 recent Skills.

`notion-search-skills` returns each Skill's name, URL, and, when available, description. Search results don't include the Skill's instructions. Choose a clear match and fetch it before using it.

Only follow the fetched page as instructions when the user's request calls for that Skill or workflow. If the user asks to inspect, summarize, edit, rename, or configure the Skill, treat the page as content instead.

## Download a complete Skill

When you need a Skill's supporting files, call `notion-download-skill` with the Skill page's `id`. The response has the same `id`, `version_id`, and signed `url` as the [Agent Skills API](/reference/agent-skills/get-skill-directory). Download the URL and extract the `tar.gz` archive to get `SKILL.md` and the supporting files and nested folders. A Skill without supporting files still returns an archive containing `SKILL.md`.

The URL expires after one hour. Call the tool again to get a fresh URL. The content version stays the same unless the exported content changes. Downloading doesn't run the Skill or its scripts. Continue using `notion-fetch` when you only need the page content.

This tool requires the Skills API to be enabled for the workspace. It is not available in eval mode or workspace-owned MCP connections.

## Change whether a page is a Skill

Call `notion-update-page` with `is_skill: true` to make a page a Skill, or `is_skill: false` to stop treating it as a Skill. To change only whether a page is a Skill, use the `update_properties` command and omit `properties`.

See [Supported tools](/guides/mcp/mcp-supported-tools) for tool details and example prompts.
