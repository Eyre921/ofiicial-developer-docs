---
title: "Web Search"
source: https://docs.fireworks.ai/nexus/web-search
path: nexus/web-search
---

Use native web search and fetch in Claude Code, Codex, and ChatGPT while connected through FireConnect.

Web search is built into Fireworks. When Claude Code calls its native `WebSearch` tool, Fireworks runs the search server-side and returns the results, with no MCP server or search service to set up. Connect the harness through [Coding Harnesses](/nexus/harnesses).

| Harness | Search behavior | Wire API |
| - | - | - |
| Claude Code | Native `WebSearch` and `WebFetch` remain available | Messages |
| Codex CLI, Codex app, and ChatGPT desktop | Native web search remains available | Responses |
| OpenCode, Pi, Cursor IDE, VS Code, Copilot, and DeepSeek Harness | FireConnect does not add web search | Not applicable |

<Info>
  Web search pricing will be published soon.
</Info>

## See native search in action

Native web search works with any Fireworks model. Both examples use FireRouter, but native web search works without a model router.

<Frame>
  <img alt="Claude Code using native Web Search twice and returning a sourced list of pancake restaurants in San Francisco" />
</Frame>

<Frame>
  <img alt="Codex CLI searching the web and returning a list of pancake restaurants in San Francisco" />
</Frame>

## Upgrade from the retired MCP

FireConnect versions before 0.9.7 installed the `fireworks-websearch` MCP for Claude Code. That MCP is no longer available, because Fireworks now handles Claude Code's native search tools server-side.

```bash wrap theme={null}
fireconnect upgrade
```

The upgrade removes the retired MCP and legacy tool denials that FireConnect added. Restart Claude Code afterward.
