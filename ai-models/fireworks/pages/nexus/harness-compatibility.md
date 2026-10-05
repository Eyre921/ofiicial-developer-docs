---
title: "Harness Compatibility"
source: https://docs.fireworks.ai/nexus/harness-compatibility
path: nexus/harness-compatibility
---

Compare FireRouter support, closed-model credentials, and MCP behavior across coding harnesses connected through FireConnect.

Use this page to check whether FireConnect can add FireRouter to your harness and what it changes about Model Context Protocol (MCP) configuration. For setup commands and restart rules, see [Coding Harnesses](/nexus/harnesses).

<Tabs>
  <Tab title="FireRouter">
    | Harness | Request API | FireRouter compatibility | Local provider credentials |
    | - | - | - | - |
    | Claude Code | Messages | Supports `firerouter` and `firerouter/...` IDs | Anthropic login, OAuth, or `ANTHROPIC_API_KEY`; OpenAI key |
    | Claude Agent SDK | Messages | Supported when the SDK reads the user settings written by FireConnect | Same as Claude Code |
    | OpenCode | Chat Completions | Supports `firerouter` and `firerouter/...` IDs | Anthropic and OpenAI keys |
    | Codex | Responses | Supports `firerouter` and `firerouter/...` IDs | `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` environment references |
    | Codex app, ChatGPT desktop | Responses | Uses the FireRouter IDs registered through the shared Codex configuration | No separate local provider-key configuration |
    | Pi | Chat Completions | Supports `firerouter` and `firerouter/...` IDs | Anthropic and OpenAI keys |
    | Cursor IDE | Chat Completions | Supports `firerouter` and `firerouter/...` IDs. Closed models need Provider Keys | None |
    | VS Code | Chat Completions | Supports `firerouter` and `firerouter/...` IDs | Anthropic and OpenAI keys |
    | Copilot App | Chat Completions | Supports `firerouter` and `firerouter/...` IDs. Closed models need Provider Keys | None |
    | Copilot CLI | Chat Completions | Supports `firerouter` and `firerouter/...` IDs. Closed models need Provider Keys or manual setup | Provider-key headers in manual setup |
    | DeepSeek Harness | Chat Completions | Supports `firerouter` and `firerouter/...` IDs. Closed models need Provider Keys or manual setup | Provider-key headers in manual setup |
    | Claude Desktop | Messages | Not offered. The picker lists `auto` and Fireworks models | Not applicable |

    **Provide a local key.** Where a harness supports one, pass it when you
    connect, or store it once for every harness:

    ```bash wrap theme={null}
    fireconnect opencode --model firerouter/opus --anthropic-api-key "$ANTHROPIC_API_KEY"
    fireconnect configure --anthropic-api-key "$ANTHROPIC_API_KEY"
    fireconnect configure --openai-api-key "$OPENAI_API_KEY"
    ```

    * Both keys are optional. FireConnect connects without them and never prompts for an OpenAI key.
    * FireConnect also reads `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` from your environment.
    * Codex stores environment references, so FireConnect adds a line to your shell config that exports the saved keys. Open a new terminal before starting Codex.
    * The OpenAI key goes out on bare `firerouter` and on routes that name a GPT model ID, such as `firerouter/gpt-5.6-sol`. Family routes such as `firerouter/sol` and `firerouter/astra` need an OpenAI Provider Key or manual setup.

    **Harnesses without a local key.** Cursor IDE, Copilot App, Copilot CLI,
    and DeepSeek Harness accept every FireRouter ID, including bare
    `firerouter`. Without a matching Provider Key, FireRouter serves those
    routes with open models only.

    * Cursor IDE and the Copilot App cannot send extra headers, so closed models there need a [Provider Key](/nexus/provider-keys).
    * Copilot CLI and DeepSeek Harness can send the headers with [manual setup](/nexus/firerouter/setup#set-up-your-harness).

    Provider Keys is not yet available on every account;
    [contact the Fireworks team](https://fireworks.ai/demo-request) to enable
    it. For direct HTTP calls, see
    [APIs and SDKs](/nexus/apis-and-sdks#credentials) or
    [LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials).

    Automated live-inference validation covers Claude Code, OpenCode, Codex,
    Pi, and DeepSeek Harness. Cursor IDE, VS Code, Copilot App, Copilot CLI,
    and ChatGPT desktop are validated at the configuration layer.
  </Tab>

  <Tab title="MCP">
    Your MCP servers keep working after you connect a harness to Fireworks.
    FireConnect changes where model requests go, not which tools the harness
    loads. Fireworks models call MCP tools the same way the harness's default
    models do.

    <Columns>
      <Card title="Your servers stay" icon="plug">
        FireConnect keeps every MCP server you configured, and
        `fireconnect <harness> off` leaves them in place.
      </Card>

      <Card title="Tool search stays on" icon="magnifying-glass">
        In Claude Code, FireConnect sets `ENABLE_TOOL_SEARCH` so large MCP
        tool sets still load on demand.
      </Card>

      <Card title="Web search is built in" icon="globe" href="/nexus/web-search">
        The Fireworks WebSearch MCP is retired. Claude Code's native
        `WebSearch` tool replaces it.
      </Card>
    </Columns>

    ### What FireConnect changes

    | Harness | What happens to MCP |
    | - | - |
    | Claude Code | Your servers stay in `~/.claude.json`. FireConnect removes only its retired `fireworks-websearch` server and sets `ENABLE_TOOL_SEARCH` |
    | Codex | Your servers stay in `[mcp_servers]` in `~/.codex/config.toml` |
    | OpenCode | Your servers stay in the `mcp` block of `opencode.json` |
    | Codex app | FireConnect doesn't touch MCP. Set up servers in the app as usual |
    | ChatGPT desktop | <Badge>Unreliable</Badge> MCP servers and plugins don't work reliably while FireConnect is on |
    | Pi, Cursor IDE, VS Code, Copilot App, Copilot CLI, DeepSeek Harness | FireConnect doesn't touch MCP. Set up servers in the harness as usual |
    | Claude Agent SDK | FireConnect doesn't touch MCP. MCP follows the setting sources your application loads |
    | Claude Desktop | Third-party mode hides the connector browser. Run `fireconnect claude-desktop mcp sync` after `on` to import your connectors, then sign in to each once. See [Claude Desktop](/nexus/harnesses#claude-desktop) |

    <Warning>
      MCP servers and plugins in ChatGPT desktop don't work reliably while
      FireConnect is on. If you depend on them there, run
      `fireconnect codex off` before using them.
    </Warning>

    ### Check that an MCP tool works

    <Steps>
      <Step title="Connect the harness" icon="plug">
        ```bash theme={null}
        fireconnect claude
        ```

        Use `fireconnect codex` or `fireconnect opencode` for the other
        harnesses.
      </Step>

      <Step title="Confirm the server is configured" icon="list-check">
        <CodeGroup>
          ```bash Claude Code theme={null}
          claude mcp list
          # docs: npx -y your-mcp-server - ✔ Connected
          ```

          ```toml Codex theme={null}
          # ~/.codex/config.toml, next to the settings FireConnect adds
          [mcp_servers.docs]
          command = "npx"
          args = ["-y", "your-mcp-server"]
          ```

          ```json OpenCode theme={null}
          // ~/.config/opencode/opencode.json
          {
            "mcp": {
              "docs": {
                "type": "local",
                "command": ["npx", "-y", "your-mcp-server"],
                "enabled": true
              }
            }
          }
          ```
        </CodeGroup>

        In Claude Code, add a server with `claude mcp add <name> -- <command>`.
      </Step>

      <Step title="Ask the model to call a tool" icon="wrench">
        Start a new session and ask for something only the tool can answer,
        such as "Call the docs search tool and summarize the first result."
        The harness shows the tool call, and the answer uses the tool's output.
      </Step>
    </Steps>

    <Tip>
      Setting up Claude Code by hand? Add `"ENABLE_TOOL_SEARCH": "true"` to
      `env` in `~/.claude/settings.json`. Claude Code turns MCP tool search off
      when `ANTHROPIC_BASE_URL` points anywhere other than Anthropic.
    </Tip>

    <Note>
      Upgrading from the Fireworks WebSearch MCP? `fireconnect claude` removes
      the `fireworks-websearch` server for you and leaves your other servers
      in place. See [Web Search](/nexus/web-search) for which harnesses have
      native web search.
    </Note>
  </Tab>
</Tabs>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Nothing changed after --model">
    Restart or reopen the harness. Claude Code and Codex load a new model in a
    new or resumed session. See [Coding Harnesses](/nexus/harnesses) for each
    harness.
  </Accordion>

  <Accordion title="A FireRouter route never uses Claude or GPT">
    The harness cannot send a local provider key, or the route does not pick
    up your saved key. Connect the matching
    [Provider Key](/nexus/provider-keys), use
    [manual setup](/nexus/firerouter/setup#set-up-your-harness) on a harness
    that can send headers, or use a harness that supports a local key.
  </Accordion>

  <Accordion title="Claude Code says auto mode classifier requests are billed">
    Expected once per session. Auto mode's safety checks run on your Sonnet
    slot, so they bill to Anthropic. To bill them at Fireworks rates, pin
    Sonnet with `fireconnect claude --sonnet <id>`.
  </Accordion>
</AccordionGroup>

## Microsoft Foundry

FireRouter is not available on Microsoft Foundry, and Foundry support differs by harness. See the compatibility matrix in [Foundry for Coding Harnesses](/nexus/microsoft-foundry#choose-a-path), including [Claude Code through a gateway](/nexus/microsoft-foundry#claude-code-through-a-gateway).

## Related setup

* [Coding Harnesses](/nexus/harnesses): connect commands, files changed, and restart rules
* [FireRouter](/nexus/firerouter): router IDs and composition
* [Provider Keys](/nexus/provider-keys): account-level closed-model credentials
* [Routing Preferences](/nexus/routing-preferences): quality and savings controls by harness
