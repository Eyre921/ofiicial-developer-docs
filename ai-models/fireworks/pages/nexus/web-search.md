---
title: "Web Search"
source: https://docs.fireworks.ai/nexus/web-search
path: nexus/web-search
---

Use native web search and fetch in Claude Code, Codex, and ChatGPT while connected through FireConnect.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

Web search is built into Fireworks. When Claude Code calls its native `WebSearch` tool, Fireworks runs the search server-side and returns the results, with no MCP server or search service to set up. Connect the harness through [Coding Harnesses](/nexus/harnesses).

| Harness | Search behavior | Wire API |
| - | - | - |
| Claude Code | Native `WebSearch` and `WebFetch` remain available | Messages |
| Codex CLI and ChatGPT desktop app | Native web search remains available | Responses |
| OpenCode, Pi, Cursor IDE, VS Code, Copilot, and DeepSeek Harness | FireConnect does not add web search | Not applicable |

> [!NOTE]
>
> Web search pricing will be published soon.

## See native search in action

Native web search works with any Fireworks model and a standard `fw_...` key. Fire Pass keys can't use it. Both examples use FireRouter, but native web search works without a model router.

![Claude Code using native Web Search twice and returning a sourced list of pancake restaurants in San Francisco](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/claude-web-search.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=52c69f46be8ecc6fa25fe4e9c21148c4)

![Codex CLI searching the web and returning a list of pancake restaurants in San Francisco](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/codex-web-search.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=ed717d4f9732c88b782e72f8c03fe044)

## Upgrade from the retired MCP

FireConnect versions before 0.9.7 installed the `fireworks-websearch` MCP for Claude Code. That MCP is no longer available, because Fireworks now handles Claude Code's native search tools server-side.

```bash wrap theme={null}
fireconnect upgrade
```

The upgrade removes the retired MCP and legacy tool denials that FireConnect added. Restart Claude Code afterward.
