---
title: "AI context files"
source: https://docs.netlify.com/build/build-with-ai/agent-setup-guides/agent-setup-overview.md
path: build/build-with-ai/agent-setup-guides/agent-setup-overview
---

---
title: "Agent setup overview"
description: "Learn how to set up most agents, including custom agents, quickly."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Learn how to set up most agents, including custom agents, quickly. For even more specific setup guidance, check out our agent setup guides for your specific agent.

### Promoted Content

**Title - Quick setup**

**description**
Equip your agent with the latest Netlify context, including agent skills:

```
fetch https://netlify.ai to help me deploy and build with Netlify using the latest agent skills
```

## MCP Server support

Connect to the Netlify MCP server to equip your agent with the best of Netlify expertise and the Netlify CLI.

### Connect to Netlify's remote MCP server 

Netlify offers an [MCP server](https://github.com/netlify/netlify-mcp), which you can connect to through a connector, plugin, or your agent.

To start connecting to Netlify's remote MCP server by running this command and following the prompts to select the agents you want to configure:

```
npx -y add-mcp https://netlify-mcp.netlify.app/mcp
```

If you would like to use your agent's own official setup command, check out the agent-specific MCP instructions below:

- [Claude Code](/build/build-with-ai/agent-setup-guides/set-up-claude-code-for-netlify/#connect-to-the-netlify-mcp-server)
- [Codex](/build/build-with-ai/agent-setup-guides/set-up-codex-for-netlify/#install-netlify-mcp-server)
- [Claude Web](/build/build-with-ai/agent-setup-guides/set-up-claude-web-for-netlify/#connect-netlify-to-claude-web) via Claude's Netlify Connector
- [Claude Desktop](/build/build-with-ai/agent-setup-guides/set-up-claude-desktop-for-netlify/#connect-to-the-netlify-connector) via Claude's Netlify Connector
- [ChatGPT](/build/build-with-ai/agent-setup-guides/use-netlify-with-chatgpt/#find-netlify-in-chatgpt-apps) via ChatGPT's Netlify App
- [Antigravity](/build/build-with-ai/agent-setup-guides/set-up-antigravity-for-netlify/#connect-to-the-netlify-mcp-server)
- [Antigravity CLI](/build/build-with-ai/agent-setup-guides/set-up-antigravity-cli-for-netlify/#connect-to-the-netlify-mcp-server)

The following editors allow one-click install of our MCP with the following links

[![Install MCP Server on Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=netlify&config=eyJ1cmwiOiJodHRwczovL25ldGxpZnktbWNwLm5ldGxpZnkuYXBwL21jcCJ9)

[![Add MCP Server netlify to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=netlify&config=eyJ1cmwiOiJodHRwczovL25ldGxpZnktbWNwLm5ldGxpZnkuYXBwL21jcCJ9)

[![Install on VS Code](https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF)](https://insiders.vscode.dev/redirect/mcp/install?name=netlify&config=%7B%22url%22%3A%20%22https%3A%2F%2Fnetlify-mcp.netlify.app%2Fmcp%22%7D)

[![Install on VS Code Insiders Edition](https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5)](https://insiders.vscode.dev/redirect/mcp/install?name=netlify&config=%7B%22url%22%3A%20%22https%3A%2F%2Fnetlify-mcp.netlify.app%2Fmcp%22%7D&quality=insiders)

### Connect to Netlify's Local MCP server

Our recommendation is to use the remote MCP server to have the most up-to-date version of the MCP capabilities. However, some developers are required to use local MCP servers in their environments. You can use the following command to install Netlify's local MCP:

```
npx -y add-mcp "npx -y @netlify/mcp"
```

## Agent skills

To help your agent build with best practices, check out our agent skills for building and deploying on Netlify.

You can share a skill directly with your agent or have all skills installed in your local project files or repository. Some agents also support invoking a specific skill by name in a command, such as Claude Code with `/<skill-name>`.

To install agent skills for Netlify with any agent directly in your terminal or agent chat:

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

