---
title: "Coding Harnesses"
source: https://docs.fireworks.ai/nexus/harnesses
path: nexus/harnesses
---

Connect Claude Code, the Claude Agent SDK, Claude Desktop, OpenCode, Codex, Pi, Cursor IDE, VS Code, Copilot, or DeepSeek Harness to Fireworks, with FireConnect or by editing the harness settings yourself.

Most harnesses below work two ways. **FireConnect** writes the settings for you and restores them with `off`. **Manual setup** shows the same settings so you can apply them yourself, with no extra tool installed. Claude Desktop is FireConnect only.

<Columns>
  <Card title="Claude Code" icon="asterisk" href="#claude-code">
    Messages API
  </Card>

  <Card title="Claude Desktop" icon="desktop" href="#claude-desktop">
    macOS only
  </Card>

  <Card title="Codex CLI, Codex app, and ChatGPT" icon="square-terminal" href="#codex">
    Responses API
  </Card>

  <Card title="OpenCode" icon="code" href="#opencode">
    Chat Completions
  </Card>

  <Card title="Pi" icon="terminal" href="#pi">
    Chat Completions
  </Card>

  <Card title="Cursor IDE" icon="arrow-pointer" href="#cursor-ide">
    Chat Completions
  </Card>

  <Card title="VS Code" icon="window-maximize" href="#vs-code">
    Chat Completions
  </Card>

  <Card title="Copilot App" icon="github" href="#copilot-app">
    Chat Completions
  </Card>

  <Card title="Copilot CLI" icon="github" href="#copilot-cli">
    Chat Completions
  </Card>

  <Card title="DeepSeek Harness" icon="fish" href="#deepseek-harness">
    Chat Completions
  </Card>
</Columns>

## Before you start

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    [Install FireConnect](/nexus/fireconnect#quick-start) and sign in once:

    ```bash wrap theme={null}
    fireconnect login
    ```

    * **Connect:** `fireconnect <harness>`. Add `--model <id>` to choose a model or router. Browse IDs with `fireconnect model list`.
    * **Quit first:** fully quit Cursor IDE, VS Code, and the Copilot App before connecting or running `off`. Restart other harnesses, including Claude Desktop, after connecting.
    * **Check:** `fireconnect <harness> status` is read-only and safe while the app is open.
    * **Undo:** `fireconnect <harness> off` restores the settings FireConnect saved under `~/.fireconnect/`.
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    Create an API key in [Fireworks settings](https://app.fireworks.ai/settings/users/api-keys) and export it:

    ```bash wrap theme={null}
    export FIREWORKS_API_KEY="fw_..."
    ```

    Every harness uses the same Fireworks endpoints:

    | Harness API | Base URL |
    | - | - |
    | Anthropic Messages | `https://api.fireworks.ai/inference` |
    | OpenAI Chat Completions or Responses | `https://api.fireworks.ai/inference/v1` |

    Use any model ID from [Open Models](/nexus/open-models), such as `glm-latest`, or a router from [FireRouter](/nexus/firerouter#supported-models), such as `firerouter/opus`. Back up a settings file before you edit it.
  </Tab>
</Tabs>

## Claude Code

<Badge>Anthropic Messages</Badge> <Badge>FireRouter</Badge> <Badge>Native web search</Badge>

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect claude
    fireconnect claude status
    ```

    Start a new session, or exit and run `claude --resume <id>`. FireConnect selects FireRouter by default. To choose another model, pass `--model`:

    ```bash wrap theme={null}
    fireconnect claude --model glm-5p3-flash
    ```

    `--model` sets the default model for new sessions and adds it to `/model`. `/model` also lists `auto`, the routers, and the Fireworks catalog. Your own picker rows are not changed.

    To send one Claude tier or your subagents to a specific model, pin that slot:

    ```bash wrap theme={null}
    fireconnect claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest
    ```

    Tier flags are `--opus`, `--sonnet`, `--haiku`, `--fable`, and `--subagent`. Unpinned slots stay on Claude Code's defaults. Running `fireconnect claude` again keeps your pins. Pass `native`, such as `--sonnet native`, to release a slot.

    <Tree>
      <Tree.Folder name="~">
        <Tree.Folder name=".claude">
          <Tree.File name="settings.json" />
        </Tree.Folder>

        <Tree.File name=".claude.json" />

        <Tree.Folder name=".fireconnect">
          <Tree.File name="backup for off" />
        </Tree.Folder>
      </Tree.Folder>
    </Tree>

    <Accordion title="See what FireConnect writes">
      ```json ~/.claude/settings.json theme={null}
      {
        "env": {
          "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
          "ANTHROPIC_CUSTOM_HEADERS": "X-Fireworks-Api-Key: fw_...",
          "DISABLE_TELEMETRY": "1",
          "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
          "ENABLE_TOOL_SEARCH": "true"
        },
        "modelPicker": {
          "options": [
            { "model": "firerouter[1m]", "label": "FireRouter" },
            { "model": "auto[1m]", "label": "Auto" }
          ]
        },
        "model": "firerouter[1m]",
        "statusLine": { "type": "command", "command": "... claude-statusline.mjs" }
      }
      ```

      * The Fireworks key goes in a custom header, so your Claude login stays available for routes with Claude models.
      * `[1m]` marks 1M-context models.
      * A pinned tier adds `ANTHROPIC_DEFAULT_<TIER>_MODEL` to `env`, such as `ANTHROPIC_DEFAULT_SONNET_MODEL`. A pinned subagent adds `CLAUDE_CODE_SUBAGENT_MODEL`.
      * The status line shows the estimated session cost. It is added only if you do not already have one.
      * FireConnect also turns off Claude Code telemetry and nonessential traffic, and enables MCP tool search.
      * `~/.claude.json` records approval for the FireConnect credential so Claude Code does not prompt for it.
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    <Steps>
      <Step title="Point Claude Code at Fireworks" icon="file-pen">
        Add these values to `~/.claude/settings.json`:

        ```json ~/.claude/settings.json theme={null}
        {
          "env": {
            "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
            "ANTHROPIC_AUTH_TOKEN": "fw_YOUR_FIREWORKS_API_KEY"
          },
          "model": "glm-latest"
        }
        ```

        Or set them for one shell:

        ```bash wrap theme={null}
        export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"
        export ANTHROPIC_API_KEY="$FIREWORKS_API_KEY"
        claude --model glm-latest
        ```
      </Step>

      <Step title="Start a session" icon="play">
        Run `claude`. Claude Code may ask once whether to use the API key; approve it.
        <Check>The first reply comes from the Fireworks model you set.</Check>
      </Step>

      <Step title="Optional: use FireRouter" icon="shuffle">
        Set `"model": "firerouter/opus"`. For Claude models in the route, connect an Anthropic [Provider Key](/nexus/provider-keys), or add `x-anthropic-api-key` to `ANTHROPIC_CUSTOM_HEADERS`.
      </Step>
    </Steps>

    Claude Code's `/model` picker does not list Fireworks models you set by hand. Change models in `settings.json` or with `claude --model <id>`. Claude Code may log `unrecognized_model` for Fireworks IDs; requests still succeed.
  </Tab>
</Tabs>

<AccordionGroup>
  <Accordion title="Routers and credentials">
    * Bare `firerouter` and routes with Claude models can use your Claude login when you connect with FireConnect.
    * Optional: save an OpenAI key once with `fireconnect configure --openai-api-key sk-...` so FireRouter can also reach GPT models. FireConnect sends it on bare `firerouter` and on routes that name a GPT model ID, such as `firerouter/gpt-5.6-sol`.
    * Family routes such as `firerouter/sol` and `firerouter/astra` don't use the saved key. Connect an OpenAI [Provider Key](/nexus/provider-keys), or send `x-openai-api-key` with manual setup.
    * See [Routing Preferences](/nexus/routing-preferences) for `--routing-preference` and [Harness Compatibility](/nexus/harness-compatibility) for cross-harness support.
  </Accordion>

  <Accordion title="Usage and cost">
    For the status line and `fireconnect claude usage`, see [Usage and Cost](/nexus/metrics). Claude Code's own in-app cost uses Anthropic list prices; use the FireConnect status line for the Fireworks estimate. For a side-by-side comparison, see the [Side-by-Side Demo](/nexus/demo).
  </Accordion>

  <Accordion title="Troubleshooting">
    * Text-only models fail on pasted images. Use `/rewind`, or switch to a vision model such as `glm-5p3-flash`.
    * Resume or restart the session after changing models.
    * Auto mode says classifier requests are billed: this is expected, once per session, and auto mode keeps working. Its safety checks run on your Sonnet slot and bill to Anthropic. To bill them at Fireworks rates, pin Sonnet with `fireconnect claude --sonnet <id>`.
  </Accordion>
</AccordionGroup>

## Claude Agent SDK

<Badge>Anthropic Messages</Badge>

The Claude Agent SDK can reuse the Claude Code settings above. Connect Claude Code first, with FireConnect or manually:

```bash wrap theme={null}
fireconnect claude --model firerouter/opus
```

In the SDK query options, include `settingSources: ["user"]`. The SDK then reads the Fireworks endpoint, model, and credentials from `~/.claude/settings.json`.

`fireconnect claude` does not configure Claude Desktop. See [Claude Desktop](#claude-desktop).

## Claude Desktop

<Badge>Anthropic Messages</Badge> <Badge>macOS only</Badge>

FireConnect runs Claude Desktop's Chat, Cowork, and Code on Fireworks models. It requires macOS and a stored credential from `fireconnect login`. **Quit and reopen Claude Desktop after `on` or `off`.**

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect claude-desktop on
    fireconnect claude-desktop status
    ```

    Reopen Claude Desktop. The picker starts on `auto`, followed by the Fireworks models, in place of your claude.ai subscription models.

    `on` brings your connectors along automatically. Each one asks you to sign in once the first time you use it. `off` puts your previous setup back, including your claude.ai models.

    <Frame>
      <img alt="Claude Desktop model picker in Cowork showing Auto selected, then Kimi K3 Fast, Kimi K3, MiniMax M3, GLM 5.3 Fast, GLM 5.3, and DeepSeek V4.1 Flash" />
    </Frame>

    <Accordion title="See what FireConnect writes">
      * `on` writes a third-party inference provider profile, Claude Desktop's own supported mechanism. The profile points at a small local gateway that FireConnect runs as a launchd service. It starts at login and restarts after a crash.
      * `on` does not copy custom skills or plugins into third-party mode. Conversations stay in the mode they were made in.
      * Connector OAuth clients you register are saved in `~/.fireconnect/claude-desktop/oauth-clients.json`, readable only by you. They survive `off` and `on`.
      * `off` restores your previous provider profile and the device settings FireConnect changed, then removes the local gateway service. Nothing of yours is deleted.
    </Accordion>
  </Tab>
</Tabs>

**What moves with you**

* Connectors move automatically with `on`. Sign in to each one once the first time you use it.
* Connector OAuth clients you register are saved and survive `off` and `on`.
* Conversations, custom skills, and plugins stay where they are. Third-party mode does not show your claude.ai sessions, and your subscription does not show sessions you start while connected. Nothing is deleted.
* MCPs that need an OAuth client ID and secret do not move. Create your own client, such as a **Desktop app** client in Google Cloud for the Google-hosted connectors. If you need one of these connectors, [reach out to the team](https://fireworks.ai/contact).

Run `fireconnect claude-desktop mcp sync` when you add a connector later and want it in third-party mode too.

<AccordionGroup>
  <Accordion title="Where did my previous conversations go?">
    Your conversations are still there. Conversations stay in the mode they were made in. Claude Desktop's third-party mode does not show conversations from your claude.ai subscription, and your subscription does not show conversations you start while connected. Nothing is deleted. Run `fireconnect claude-desktop off` and reopen Claude Desktop to see your previous conversations again.
  </Accordion>

  <Accordion title="Connectors">
    Claude Desktop's third-party mode hides the in-app connector browser. Manage connectors with FireConnect instead:

    * `on` imports the connectors you already use, from Desktop session history, your previous Desktop config, and your claude.ai organization when the Claude Code CLI is installed and signed in.
    * `fireconnect claude-desktop mcp add <name> <url>` and `mcp remove <name>` manage entries by hand. Removals stick across syncs.
    * Each connector asks you to sign in once the first time you use it after `on`.

    Google-hosted connectors (Gmail, Google Drive, Google Calendar, BigQuery) need a Google OAuth client you own, created as a **Desktop app** client in Google Cloud. One client covers all four:

    ```bash wrap theme={null}
    fireconnect claude-desktop mcp add gmail https://gmailmcp.googleapis.com/mcp/v1 \
      --client-id "<ID>.apps.googleusercontent.com" --client-secret "<SECRET>"
    ```

    The hosted Figma connector does not work in third-party mode. Turn on the Figma desktop app's local server in Dev Mode, then run `fireconnect claude-desktop mcp add figma-desktop http://127.0.0.1:3845/mcp`.
  </Accordion>

  <Accordion title="Troubleshooting">
    * `status` shows the local gateway is not responding: run `fireconnect claude-desktop on` to restart it.
    * Models are missing from the picker: run `on` once while online, then restart Claude Desktop.
    * The Code tab says the API key was rejected: run `on` again to refresh the key from your stored credential.
    * A connector sign-in error won't clear: `mcp remove` it, then `mcp add` it again with your own OAuth client (Google) or the local server (Figma).
  </Accordion>
</AccordionGroup>

## Codex

<Badge>OpenAI Responses</Badge> <Badge>FireRouter</Badge> <Badge>Native web search</Badge>

The Codex CLI, the Codex app, and the ChatGPT desktop app share one config in `~/.codex/config.toml`, so one setup covers all three. **Quit the Codex app and the ChatGPT app** before you change it so their model lists refresh.

<Warning>
  MCP servers and plugins in the ChatGPT desktop app don't work reliably while
  FireConnect is on. See [Harness Compatibility](/nexus/harness-compatibility#mcp).
</Warning>

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect codex
    fireconnect codex status
    ```

    The default model is `auto`. To add FireRouter to the Codex and ChatGPT model pickers, run `fireconnect codex --model firerouter`. Exit Codex and run `codex resume <id>`, or start a new session.

    <Frame>
      <img alt="Codex CLI model picker showing Auto selected, FireRouter, and Fireworks DeepSeek, GLM, and Kimi models" />
    </Frame>

    <Tree>
      <Tree.Folder name="~/.codex">
        <Tree.File name="config.toml" />

        <Tree.File name="fireworks-model-catalog.json" />
      </Tree.Folder>
    </Tree>

    <Accordion title="See what FireConnect writes">
      ```toml ~/.codex/config.toml theme={null}
      model_provider = "fireworks-ai"
      model_catalog_json = "~/.codex/fireworks-model-catalog.json"
      model = "auto"

      [model_providers.fireworks-ai]
      name = "Fireworks"
      base_url = "https://api.fireworks.ai/inference/v1"
      wire_api = "responses"
      experimental_bearer_token = "fw_..."
      requires_openai_auth = false
      ```

      FireConnect keeps your other TOML settings, saves the key with file mode `0600`, and writes a model catalog so Codex knows each model's context window and capabilities. The catalog also makes Codex auto-review use the model you picked, so approvals are reviewed on Fireworks. Connected before FireConnect 0.9.8? Run `fireconnect codex` once, or auto-review keeps denying every approval.
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    <Steps>
      <Step title="Add a Fireworks provider" icon="file-pen">
        ```toml ~/.codex/config.toml theme={null}
        model_provider = "fireworks-ai"
        model = "glm-latest"

        [model_providers.fireworks-ai]
        name = "Fireworks"
        base_url = "https://api.fireworks.ai/inference/v1"
        wire_api = "responses"
        env_key = "FIREWORKS_API_KEY"
        ```
      </Step>

      <Step title="Run Codex" icon="play">
        ```bash wrap theme={null}
        codex
        ```

        <Check>Codex answers from `glm-latest`.</Check>
      </Step>
    </Steps>

    Without a model catalog, Codex warns that it has no metadata for Fireworks models and uses fallback limits. FireConnect writes that catalog for you.
  </Tab>
</Tabs>

<Frame>
  <img alt="ChatGPT desktop model picker showing FireRouter selected alongside Auto and Fireworks models" />
</Frame>

When you resume an old session, select the provider explicitly:

```bash wrap theme={null}
codex resume <id> -c model_provider="fireworks-ai"
```

<Warning>
  **MiniMax models don't work on Codex.** Codex may insert assistant messages between `tool_calls` and `tool_results`, which MiniMax templates reject. Use a Chat Completions harness such as OpenCode for MiniMax.
</Warning>

## OpenCode

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter</Badge>

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect opencode
    fireconnect opencode status
    ```

    Restart OpenCode. The default model is `auto`, stored as `fireworks-ai/auto`. Short IDs such as `glm-5p2` expand to full Fireworks paths.

    <Frame>
      <img alt="OpenCode model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and other models" />
    </Frame>

    <Accordion title="See what FireConnect writes">
      ```json ~/.config/opencode/opencode.json theme={null}
      {
        "provider": {
          "fireworks-ai": {
            "options": { "apiKey": "fw_..." },
            "models": {
              "auto": { "name": "Auto", "limit": { "context": 1048575, "output": 131072 } },
              "glm-latest": { "name": "GLM (Latest)" }
            }
          }
        },
        "model": "fireworks-ai/auto"
      }
      ```

      The file is saved with mode `0600`. FireConnect never changes `auth.json`. Use `--config-path` for a config stored elsewhere.
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    **Fastest:** in OpenCode, run `/connect`, search **fireworks.ai**, paste your key, and pick a model with `/models`.

    **Or edit the config** to add routers and pin a default:

    ```json ~/.config/opencode/opencode.json theme={null}
    {
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "fireworks-ai": {
          "options": { "apiKey": "{env:FIREWORKS_API_KEY}" },
          "models": {
            "glm-latest": { "name": "GLM (Latest)" },
            "firerouter/opus": { "name": "FireRouter Opus" }
          }
        }
      },
      "model": "fireworks-ai/glm-latest"
    }
    ```

    <Check>`opencode run -m fireworks-ai/firerouter/opus "hello"` answers through FireRouter.</Check>
  </Tab>
</Tabs>

## Pi

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter</Badge>

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect pi
    fireconnect pi status
    ```

    Restart Pi if it was running. The default model is `auto`.

    <Tree>
      <Tree.Folder name="~/.pi/agent">
        <Tree.File name="settings.json" />

        <Tree.File name="auth.json" />

        <Tree.File name="models.json" />
      </Tree.Folder>
    </Tree>

    <Accordion title="See what FireConnect writes">
      ```json ~/.pi/agent/settings.json theme={null}
      {
        "defaultProvider": "fireworks",
        "defaultModel": "auto",
        "enabledModels": ["fireworks/accounts/fireworks/routers/*", "fireworks/auto"]
      }
      ```

      ```json ~/.pi/agent/auth.json theme={null}
      { "fireworks": { "type": "api_key", "key": "fw_..." } }
      ```

      `models.json` adds the Fireworks catalog to Pi's built-in `fireworks` provider. FireConnect tracks the IDs it adds so `off` removes only those. Use `--settings-path` for a settings file stored elsewhere.
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    Pi has a built-in `fireworks` provider that reads `FIREWORKS_API_KEY`. Set it as the default:

    ```json ~/.pi/agent/settings.json theme={null}
    {
      "defaultProvider": "fireworks",
      "defaultModel": "accounts/fireworks/routers/glm-latest"
    }
    ```

    <Check>`pi -p "hello"` answers from GLM.</Check>
  </Tab>
</Tabs>

## Cursor IDE

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter with Provider Keys</Badge>

`fireconnect cursor` configures Cursor IDE. Cursor CLI (`agent` or `cursor-agent`) is not supported. **Fully quit Cursor IDE before connecting or running `off`.**

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect cursor
    fireconnect cursor status
    ```

    FireConnect points every existing mode in `modelConfig` at the Fireworks default and registers the catalog in the picker. Reopen Cursor IDE and choose a Fireworks model.

    <Frame>
      <img alt="Cursor IDE model picker showing Auto selected with Fireworks DeepSeek, GLM, Kimi, and MiniMax models" />
    </Frame>

    <Accordion title="See what FireConnect writes">
      Cursor IDE stores AI settings in SQLite (`state.vscdb` under `~/.config/Cursor`, `~/Library/Application Support/Cursor`, or `%APPDATA%\Cursor`):

      | Setting | Value |
      | - | - |
      | `cursorAuth/openAIKey` | Your Fireworks key |
      | `openAIBaseUrl` | `https://api.fireworks.ai/inference/v1` |
      | `aiSettings.userAddedModels` | The Fireworks catalog, tracked for a clean `off` |
      | `aiSettings.modelOverrideDisabled` | Cursor's built-in models, hidden while connected |
      | `aiSettings.modelConfig[<mode>]` | The Fireworks model for each mode |

      Your previous auth state is saved under `~/.fireconnect/cursor/`. Use `--db-path` for a non-default `state.vscdb`.
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    <Steps>
      <Step title="Open model settings" icon="gear">
        In Cursor IDE, open **Settings**, then **Models**.
      </Step>

      <Step title="Add your Fireworks key" icon="key">
        Under **API Keys**, paste your Fireworks key into **OpenAI API Key**. Turn on **Override OpenAI Base URL** and enter `https://api.fireworks.ai/inference/v1`.
      </Step>

      <Step title="Add a model" icon="plus">
        Add a custom model with a Fireworks ID, such as `glm-latest`, then select it in chat.
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Warning>
  **While connected, only Fireworks models work.** Cursor IDE's built-in models are hidden until you run `off`. Cursor IDE also enforces a server-side allowlist, so not every Fireworks model is selectable. Some features may still use Cursor's own backend, depending on plan and version.
</Warning>

## VS Code

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter</Badge>

FireConnect adds a **Fireworks** provider to GitHub Copilot Chat's custom endpoints. This requires Copilot **Pro or Enterprise**. **Quit VS Code before connecting or running `off`.**

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect vscode
    fireconnect vscode status
    ```

    Restart VS Code, then pick a model under **Other Models → Fireworks** in Copilot Chat. `glm-latest` and `glm-fast-latest` are text-only; `glm-5p3-flash` supports images.

    <Frame>
      <img alt="VS Code Chat model picker showing the Fireworks provider with Auto selected and DeepSeek, GLM, and Kimi models" />
    </Frame>

    <Accordion title="See what FireConnect writes">
      ```json chatLanguageModels.json theme={null}
      [
        {
          "name": "Fireworks",
          "vendor": "customendpoint",
          "apiType": "chat-completions",
          "apiKey": "${input:chat.lm.secret.fw-...}",
          "models": [
            {
              "id": "auto",
              "name": "Auto",
              "url": "https://api.fireworks.ai/inference",
              "maxInputTokens": 1048575,
              "maxOutputTokens": 131072,
              "vision": true,
              "toolCalling": true
            }
          ]
        }
      ]
      ```

      The key is stored separately in `state.vscdb`, encrypted with Electron `safeStorage`. On Linux, encryption needs `libsecret`; without it, VS Code only obfuscates the key and FireConnect warns you.

      | Platform | `chatLanguageModels.json` | `state.vscdb` |
      | - | - | - |
      | Linux | `~/.config/Code/User/` | `~/.config/Code/User/globalStorage/` |
      | macOS | `~/Library/Application Support/Code/User/` | `~/Library/Application Support/Code/User/globalStorage/` |
      | Windows | `%APPDATA%\Code\User\` | `%APPDATA%\Code\User\globalStorage\` |
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    In Copilot Chat, open **Language Models**, click **+ Add Models...**, and choose **Custom Endpoint**. Use `https://api.fireworks.ai/inference/v1`, your Fireworks key, and a model ID such as `glm-latest`.

    Follow the step-by-step screenshots in [GitHub Copilot](/ecosystem/integrations/github-copilot).
  </Tab>
</Tabs>

## Copilot App

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter with Provider Keys</Badge>

The GitHub Copilot **desktop app** keeps its built-in models and adds Fireworks alongside them. **Quit the app before connecting or running `off`.**

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect copilot-app
    fireconnect copilot-app status
    ```

    Reopen the app and pick a Fireworks model in **Settings → Model providers**.

    <Accordion title="See what FireConnect writes">
      FireConnect writes to `~/.copilot/data.db` (SQLite, movable with `COPILOT_HOME`):

      | Table | What FireConnect adds |
      | - | - |
      | `model_providers` | One `Fireworks` provider of type `openai`, with base URL `https://api.fireworks.ai/inference/v1` and your key as an `Authorization: Bearer` header |
      | `provider_models` | One row per model, with token limits and reasoning efforts (`low`, `medium`, `high`, `max`) |

      `off` deletes the provider and its models. Use `--db-path` for a non-default database.
    </Accordion>
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    In **Settings → Model providers**, add a provider with the values FireConnect uses:

    | Field | Value |
    | - | - |
    | Base URL | `https://api.fireworks.ai/inference/v1` |
    | API key | Your Fireworks key |
    | Models | Fireworks IDs, such as `glm-latest` or `kimi-latest` |
  </Tab>
</Tabs>

The app's bring-your-own-key path does not support image input, the hover-card Context row, or AI-credits pricing. FireConnect can add any FireRouter ID, but the app cannot send a local Anthropic or OpenAI key. Without a matching [Provider Key](/nexus/provider-keys), FireRouter serves those routes with open models. See [Harness Compatibility](/nexus/harness-compatibility).

## Copilot CLI

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter with manual setup</Badge>

The `copilot` command (`@github/copilot`) reads plain JSON under `~/.copilot`, separate from the desktop app.

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect copilot-cli
    fireconnect copilot-cli status
    ```

    Start a new `copilot` session. Switch models with `copilot --model fireworks/<name>` or `/model`.

    <Frame>
      <img alt="Copilot CLI model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and MiniMax models" />
    </Frame>

    `off` restores `providers.json` from its snapshot, or deletes it if FireConnect created it. Use `--providers-path` for a non-default location.
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    ```json ~/.copilot/providers.json theme={null}
    {
      "providers": [
        {
          "name": "fireworks",
          "type": "openai",
          "wireApi": "completions",
          "baseUrl": "https://api.fireworks.ai/inference/v1",
          "apiKey": "fw_YOUR_FIREWORKS_API_KEY"
        }
      ],
      "models": [
        {
          "id": "glm-latest",
          "provider": "fireworks",
          "wireModel": "glm-latest",
          "name": "GLM (Latest)",
          "maxPromptTokens": 1048576,
          "maxContextWindowTokens": 1048576,
          "maxOutputTokens": 131072,
          "capabilities": { "supports": { "reasoningEffort": true } }
        }
      ]
    }
    ```

    ```json ~/.copilot/settings.json theme={null}
    { "model": "fireworks/glm-latest" }
    ```

    For a FireRouter route with Claude or GPT models, add a `headers` map to the provider, such as `"headers": { "x-anthropic-api-key": "sk-ant-..." }`, and use the router ID, such as `firerouter/opus`, as the model `id` and `wireModel`. FireConnect adds these routes but does not send your provider keys, so use manual setup to send them yourself. The [harness setup](/nexus/firerouter/setup#set-up-your-harness) generates the full file.
  </Tab>
</Tabs>

<Note>
  Use provider-prefixed model IDs such as `fireworks/glm-latest`. The CLI rejects a bare `glm-latest` and silently falls back to its configured model.
</Note>

## DeepSeek Harness

<Badge>OpenAI Chat Completions</Badge> <Badge>FireRouter with manual setup</Badge>

DeepSeek's coding agent (`dsh`) runs named profiles, such as `tui`, `web`, and `headless`, under `$DSH_HOME`, which defaults to `~/.dsh`. Restart `dsh` after changing a profile.

<Tabs>
  <Tab title="FireConnect" icon="bolt">
    ```bash wrap theme={null}
    fireconnect deepseek
    fireconnect deepseek status
    ```

    Restart `dsh`. It starts on `auto` and goes straight to Fireworks, with no DeepSeek key prompt.

    FireConnect adds a `fireworks` provider to `~/.dsh/settings.yaml` and to each existing profile's `cordis.patch.yml`, which `dsh` 0.1.7 and later read. `off` restores both from the snapshot under `~/.fireconnect/deepseek/`.

    <Tree>
      <Tree.Folder name="~/.dsh">
        <Tree.File name="settings.yaml" />

        <Tree.File name=".credentials.yaml" />

        <Tree.Folder name="profiles/<profile>">
          <Tree.File name="cordis.patch.yml" />
        </Tree.Folder>
      </Tree.Folder>
    </Tree>

    Connected before FireConnect 0.9.8? Run `fireconnect deepseek` once so `dsh` 0.1.7 and later stop asking for a DeepSeek key.

    FireConnect can add any FireRouter ID, but it does not send provider keys from `dsh`. To use Claude or GPT models in a route, connect a [Provider Key](/nexus/provider-keys) or use manual setup.
  </Tab>

  <Tab title="Manual setup" icon="wrench">
    Create the profile folder once, then add a patch to it. Repeat for each profile you use.

    ```bash wrap theme={null}
    dsh --profile tui --dump-config > /dev/null
    ```

    ```yaml ~/.dsh/profiles/tui/cordis.patch.yml theme={null}
    - id: llm-pi-ai
      config:
        providers:
          fireworks:
            displayName: Fireworks
            apiKeyEnv: FIREWORKS_API_KEY
            api: openai-completions
            baseURL: https://api.fireworks.ai/inference/v1
            models:
              - id: glm-latest
                name: GLM (Latest)
                reasoning: true
                contextWindow: 1048576
                maxTokens: 131072
    - id: agent-default-model
      config:
        provider: fireworks
        model: glm-latest
    ```

    ```bash wrap theme={null}
    export FIREWORKS_API_KEY="fw_..."
    dsh tui
    ```

    For a FireRouter route with Claude or GPT models, add `headers` to the provider, such as `x-anthropic-api-key: sk-ant-...`, and use the router ID as the model. The [harness setup](/nexus/firerouter/setup#set-up-your-harness) generates the full patch.
  </Tab>
</Tabs>
