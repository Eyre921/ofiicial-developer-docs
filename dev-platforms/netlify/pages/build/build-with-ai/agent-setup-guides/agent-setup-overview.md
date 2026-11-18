---
title: "AI context files"
source: https://docs.netlify.com/build/build-with-ai/agent-setup-guides/agent-setup-overview.md
path: build/build-with-ai/agent-setup-guides/agent-setup-overview
---

---
title: "Agent setup overview"
description: "Learn how to set up any agent with Netlify, including custom agents, and find setup guides for specific agents."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Learn how to set up any agent with Netlify, including custom agents, in a few minutes. For setup steps written for your specific agent, check out the [guides for specific agents](#guides-for-specific-agents) below.

### Promoted Content

**Title - Quick setup**

**description**
Equip your agent with the latest Netlify context, including agent skills:

```
fetch https://netlify.ai to get me set up with Netlify
```

Paste it into your agent and say what to build and deploy to Netlify in the same prompt. If your agent gives you a login link, open it and sign in to Netlify.

## Set up with the Netlify CLI

Run this in your project folder:

```
npx netlify@latest init
```

It signs you in, installs Netlify's agent skills, adds the Netlify MCP server for the agents it finds, and links the folder to a Netlify project. Then open your agent in the same folder and ask your agent for a draft or production deploy.

## MCP Server support

Connect to the Netlify MCP server to equip your agent with the best of Netlify expertise and the Netlify CLI.

### Connect to Netlify's remote MCP server 

Netlify offers an [MCP server](https://github.com/netlify/netlify-mcp), which you can connect to through a connector, plugin, or your agent.

To start connecting to Netlify's remote MCP server by running this command and following the prompts to select the agents you want to configure:

```
npx -y add-mcp https://mcp.netlify.com/mcp
```

To use your agent's own official setup, check out the [guides for specific agents](#guides-for-specific-agents) below.

The following editors allow one-click install of our MCP with the following links

[![Install MCP Server on Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=netlify&config=eyAidXJsIjogImh0dHBzOi8vbWNwLm5ldGxpZnkuY29tL21jcCJ9)

[![Add MCP Server netlify to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=netlify&config=eyAidXJsIjogImh0dHBzOi8vbWNwLm5ldGxpZnkuY29tL21jcCJ9)

[![Install on VS Code](https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF)](https://insiders.vscode.dev/redirect/mcp/install?name=netlify&config=%7B%22url%22%3A%20%22https%3A%2F%2Fmcp.netlify.com%2Fmcp%22%7D)

[![Install on VS Code Insiders Edition](https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5)](https://insiders.vscode.dev/redirect/mcp/install?name=netlify&config=%7B%22url%22%3A%20%22https%3A%2F%2Fmcp.netlify.com%2Fmcp%22%7D&quality=insiders)

### Note - Connected with the previous MCP server URL?

If you connected with the previous URL, `https://netlify-mcp.netlify.app/mcp`, your connection still works and you don't need to reconnect. Use `https://mcp.netlify.com/mcp` for new connections.

### Connect to Netlify's Local MCP server

Our recommendation is to use the remote MCP server to have the most up-to-date version of the MCP capabilities. However, some developers are required to use local MCP servers in their environments. You can use the following command to install Netlify's local MCP:

```
npx -y add-mcp "npx -y @netlify/mcp"
```

## Guides for specific agents

Each guide covers the setup path for one agent:

- [Claude](/build/build-with-ai/agent-setup-guides/set-up-claude-for-netlify/): Claude.ai and Claude Desktop, through the Netlify connector
- [Claude Code](/build/build-with-ai/agent-setup-guides/set-up-claude-code-for-netlify/): Claude Code in your terminal
- [ChatGPT](/build/build-with-ai/agent-setup-guides/use-netlify-with-chatgpt/): ChatGPT, through the Netlify app
- [Codex](/build/build-with-ai/agent-setup-guides/set-up-codex-for-netlify/): Codex in your terminal
- [Grok](/build/build-with-ai/agent-setup-guides/set-up-grok-for-netlify/): Grok, through the Netlify connector
- [Antigravity](/build/build-with-ai/agent-setup-guides/set-up-antigravity-for-netlify/): Antigravity, through the Netlify plugin
- [Antigravity CLI](/build/build-with-ai/agent-setup-guides/set-up-antigravity-cli-for-netlify/): Antigravity CLI in your terminal

## Agent skills

To help your agent build with best practices, check out our agent skills for building and deploying on Netlify.

The `fetch https://netlify.ai` message and `npx netlify@latest init` both install Netlify's agent skills for you. You can also share a skill directly with your agent or have all skills installed in your local project files or repository. Some agents also support invoking a specific skill by name in a command, such as Claude Code with `/<skill-name>`.

To install only Netlify's agent skills, run this in your terminal or agent chat:

```
npx skills add netlify/context-and-tools --skill '*' --yes
```

Learn more about agent skills for building and deploying on Netlify in our [official agent skills repository](https://github.com/netlify/context-and-tools).

### Agent skills highlights

Here are some highlights of agent skills for building and deploying on Netlify. Note that if you are using [Agent Runners](/build/build-with-ai/agent-runners/overview/), you don't need to invoke agent skills as they are applied automatically for you.

| Skill | Feature Support | Description |
|---|---|---|
| [netlify-functions](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-functions) | [Netlify Functions](/build/functions/overview/) | Modern syntax, routing, Background Functions, Scheduled Functions, and streaming |
| [netlify-edge-functions](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-edge-functions) | [Edge Functions](/build/edge-functions/overview/) | Deno runtime, middleware patterns, geolocation, and request manipulation |
| [netlify-blobs](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-blobs) | [Netlify Blobs](/build/data-and-storage/netlify-blobs/) | Key-value and binary object storage with zero configuration |
| [netlify-db](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-db) | [Netlify Database](/build/data-and-storage/netlify-database/) | Managed Postgres, Drizzle ORM integration, and migrations |
| [netlify-image-cdn](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-image-cdn) | [Image CDN](/build/image-cdn/overview/) | On-the-fly image transformation and optimization |
| [netlify-forms](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-forms) | [Netlify Forms](/manage/forms/setup/) | HTML form handling, AJAX submissions, and spam filtering |
| [netlify-config](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-config) | [File-based configuration](/build/configure-builds/file-based-configuration/) | `netlify.toml` configuration, including redirects, headers, build settings, and deploy contexts |
| [netlify-cli-and-deploy](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-cli-and-deploy) | [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli/) | Commands, Git and manual deploys, and environment variables |
| [netlify-deploy](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-deploy) | [Create deploys](/deploy/create-deploys/) | Authentication, site linking, Deploy Previews, and production deploys |
| [netlify-frameworks](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-frameworks) | [Framework adapters](/build/frameworks/frameworks-api/) | Vite, Astro, TanStack Start, and Next.js on Netlify |
| [netlify-caching](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-caching) | [Caching](/build/caching/caching-overview/) | CDN cache control, cache tags, purge, and stale-while-revalidate |
| [netlify-ai-gateway](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-ai-gateway) | [AI Gateway](/build/ai-gateway/overview/) | Proxy for OpenAI, Anthropic, and Google AI SDKs |

## Netlify configuration schema

Netlify publishes a JSON schema for `netlify.toml` that lists the supported properties and the values they accept. Point your agent to it when it writes or edits your Netlify configuration, so it uses properties that exist instead of guessing:

```
check netlify.toml against the schema at https://open-api.netlify.com/netlify.schema.json, and add "$schema" = "https://open-api.netlify.com/netlify.schema.json" at the top of the file
```

With the `$schema` key in the file, editors that support the schema also flag invalid values as you or your agent make changes. Learn more about [schema validation](/build/configure-builds/file-based-configuration/#schema-validation).

