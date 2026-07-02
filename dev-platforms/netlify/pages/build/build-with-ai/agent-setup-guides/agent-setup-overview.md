---
title: "AI context files"
source: https://docs.netlify.com/build/build-with-ai/agent-setup-guides/agent-setup-overview.md
path: build/build-with-ai/agent-setup-guides/agent-setup-overview
---

---
title: "Agent setup overview"
description: "Learn how to set up most agents, including custom agents, quickly."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Learn how to set up most agents, including custom agents, quickly. For even more specific setup guidance, check out our agent setup guides for your specific agent.

### Promoted Content

**Title - Quick setup**

**description**
Equip your agent with the latest Netlify context, including agent skills:

```
fetch https://netlify.ai to help me deploy and build with Netlify using the latest agent skills
```

## MCP servers, plugins, and more

Netlify offers an [MCP server](https://github.com/netlify/netlify-mcp), which you can connect to through a connector, plugin, or your agent.

Learn more about [Netlify's MCP server](https://github.com/netlify/netlify-mcp).

For specific guidance on connecting to Netlify's remote MCP server, check your agent setup guide or MCP server directory or marketplace.

For example, you can find Netlify in [Cursor's marketplace](https://cursor.com/marketplace/netlify) or in [Claude's Connector Directory](https://claude.com/connectors/netlify).

### Quick setup for Code Editors

Some code editors support a quick MCP server connection that you can click to get started. Learn more in your code editor docs or MCP server directory.

[![Install MCP Server on Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=netlify&config=eyJjb21tYW5kIjoibnB4IC15IEBuZXRsaWZ5L21jcCJ9)

[![Add MCP Server netlify to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=netlify&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBuZXRsaWZ5L21jcCJdfQ%3D%3D)

[![Install on VS Code](https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF)](https://insiders.vscode.dev/redirect/mcp/install?name=netlify&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40netlify%2Fmcp%22%5D%7D)

[![Install on VS Code Insiders Edition](https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5)](https://insiders.vscode.dev/redirect/mcp/install?name=netlify&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40netlify%2Fmcp%22%5D%7D&quality=insiders)

### Connect to MCP server with `.json` file

To connect to the Netlify MCP server with a `.json` file, we recommend you check with your AI tool, IDE, or agent to learn specific configuration requirements.

In general, we recommend Netlify's remote MCP server setup over using Netlify's local MCP server. Most often people only use the local MCP server when their local environment restricts remote MCP servers.

Here is a general example of a `.json` MCP server configuration file used to connect to Netlify's remote MCP server at `https://netlify-mcp.netlify.app/mcp`:

```json
{
  "context_servers": {
    "netlify": {
      "url": "https://netlify-mcp.netlify.app/mcp"
    }
  }
}
```

Note: Your AI tool, IDE, or agent setup may require some changes from the above example, such as saving the file as `mcp.json`, `settings.json`, changing `mcpServers` to `ContextServers` and/or requiring another field such as `"type":"http"`. Check your agent setup guide or MCP server setup docs or marketplace for the most accurate setup instructions.

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
| [netlify-config](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-config) | [File-based configuration](/build/configure-builds/file-based-configuration/) | `netlify.toml` configuration - redirects, headers, build settings, and deploy contexts |
| [netlify-cli-and-deploy](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-cli-and-deploy) | [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli/) | Commands, Git and manual deploys, and environment variables |
| [netlify-deploy](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-deploy) | [Create deploys](/deploy/create-deploys/) | Authentication, site linking, Deploy Previews, and production deploys |
| [netlify-frameworks](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-frameworks) | [Framework adapters](/build/frameworks/frameworks-api/) | Vite, Astro, TanStack Start, and Next.js on Netlify |
| [netlify-caching](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-caching) | [Caching](/build/caching/caching-overview/) | CDN cache control, cache tags, purge, and stale-while-revalidate |
| [netlify-ai-gateway](https://github.com/netlify/context-and-tools/tree/main/skills/netlify-ai-gateway) | [AI Gateway](/build/ai-gateway/overview/) | Proxy for OpenAI, Anthropic, and Google AI SDKs |

