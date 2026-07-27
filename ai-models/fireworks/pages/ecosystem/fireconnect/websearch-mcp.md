---
title: "WebSearch MCP"
source: https://docs.fireworks.ai/ecosystem/fireconnect/websearch-mcp
path: ecosystem/fireconnect/websearch-mcp
---

Fireworks-hosted live web search for coding harnesses via HTTP MCP

WebSearch MCP provides live internet search through Fireworks. It works from **any harness that supports HTTP MCP** once you add the server URL and authenticate with a Fireworks API key.

This is separate from the [Fireworks Docs MCP](/ecosystem/integrations/development-setup), which searches Fireworks documentation only.

## Access

Web search MCP is not enabled on every account. [Contact the Fireworks team](https://fireworks.ai/contact) to request access, then use a standard [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) as the bearer token below.

### Check eligibility

There is no self-serve toggle in the Fireworks dashboard yet. After access is granted:

| Method                                 | Eligible                                              | Not eligible                                   |
| -------------------------------------- | ----------------------------------------------------- | ---------------------------------------------- |
| Connect the MCP server in your harness | Server connects; search tools respond                 | Auth or connection errors                      |
| `fireconnect claude on`                | Prints `Web search → fireworks-websearch (installed)` | Skips MCP setup; Fireworks routing still works |

If you see auth errors, [contact the Fireworks team](https://fireworks.ai/contact) to confirm web search is enabled on your account.

## MCP endpoint

Use this HTTP MCP server in any harness that supports remote MCP:

| Field    | Value                                          |
| -------- | ---------------------------------------------- |
| **URL**  | `https://mcp.fireworks.ai/work/mcp`            |
| **Auth** | `Authorization: Bearer YOUR_FIREWORKS_API_KEY` |

Example JSON (exact file and shape depend on your harness):

```json theme={null}
{
  "mcpServers": {
    "fireworks-websearch": {
      "type": "http",
      "url": "https://mcp.fireworks.ai/work/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_FIREWORKS_API_KEY"
      }
    }
  }
}
```

Replace `YOUR_FIREWORKS_API_KEY` with your Fireworks API key. Wire this into your harness MCP config the same way you would any other HTTP MCP server.

## FireConnect integration

FireConnect can install and wire WebSearch MCP automatically. **Today this is integrated for Claude Code only.** OpenCode, Codex, Pi, Cursor, VS Code, and other harnesses are coming soon.

For Claude Code with FireConnect:

```bash theme={null}
fireconnect claude on
```

For eligible accounts, FireConnect installs `fireworks-websearch`, adds Claude Code-specific `permissions.deny` entries for built-in web tools, and configures keychain-backed auth. Look for `Web search → fireworks-websearch (installed)` in the CLI output.

On other harnesses, add the [MCP endpoint](#mcp-endpoint) manually until FireConnect support ships.

## Claude Code manual setup

Claude Code is the most common path today. You can configure the MCP yourself or use FireConnect above.

**Prerequisites**

* [Claude Code](https://claude.ai/code) installed
* A Fireworks API key with web search access
* Claude Code routed through Fireworks ([FireConnect](/ecosystem/fireconnect/claude-code) or [manual settings](/ecosystem/firerouter/claude-code))

### 1. Add the MCP server

Add the [MCP endpoint](#mcp-endpoint) to `~/.claude.json` (merge with any existing `mcpServers` entries).

Or add it from the CLI:

```bash theme={null}
claude mcp add --transport http fireworks-websearch https://mcp.fireworks.ai/work/mcp \
  --header "Authorization: Bearer YOUR_FIREWORKS_API_KEY"
```

### 2. Deny Claude Code's built-in web tools

Claude Code's built-in `WebSearch` and `WebFetch` tools are Anthropic server-side tools. They do not run when inference is routed through Fireworks. Deny them in `~/.claude/settings.json`:

```json theme={null}
{
  "permissions": {
    "deny": ["WebSearch", "WebFetch"]
  }
}
```

Merge this with your existing `permissions` rules if you already have them.

### 3. Connect in Claude Code

1. Restart Claude Code.
2. Run `/mcp` and connect to `fireworks-websearch`.

`fireconnect claude off` removes the FireConnect-managed MCP entry and restores your previous settings.

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [Claude Code](/ecosystem/fireconnect/claude-code)
