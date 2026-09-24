---
title: "Web Search"
source: https://docs.fireworks.ai/nexus/web-search
path: nexus/web-search
---

Use native web search and fetch in Claude Code, Codex, and ChatGPT while connected through FireConnect.

FireConnect preserves native web search when a supported harness routes through Fireworks. Connect the harness through [Coding Harnesses](/nexus/harnesses). You do not need a separate search service or command.

| Harness                                                          | Search behavior                                    | Wire API       |
| ---------------------------------------------------------------- | -------------------------------------------------- | -------------- |
| Claude Code                                                      | Native `WebSearch` and `WebFetch` remain available | Messages       |
| Codex and ChatGPT                                                | Native web search remains available                | Responses      |
| OpenCode, Pi, Cursor IDE, VS Code, Copilot, and DeepSeek Harness | FireConnect does not add web search                | Not applicable |

## See native search in action

Native web search works with any Fireworks model. Both examples use FireRouter, but native web search works without a model router.

<Frame>
  <img alt="Claude Code using native Web Search twice and returning a sourced list of pancake restaurants in San Francisco" />
</Frame>

<Frame>
  <img alt="Codex CLI searching the web and returning a list of pancake restaurants in San Francisco" />
</Frame>

## Upgrade from the retired MCP

Earlier FireConnect versions installed the `fireworks-websearch` MCP for Claude Code. That MCP is retired because the Fireworks Messages endpoint supports Claude Code's native search tools.

```bash wrap theme={null}
fireconnect upgrade
```

The upgrade removes the retired MCP and legacy tool denials that FireConnect added. Restart Claude Code afterward.
