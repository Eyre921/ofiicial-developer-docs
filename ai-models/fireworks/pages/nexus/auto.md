---
title: "Nexus Auto"
source: https://docs.fireworks.ai/nexus/auto
path: nexus/auto
---

Nexus Auto picks a Fireworks open model or an Anthropic or OpenAI model for each turn. Set it up in a coding harness, an LLM gateway, or an SDK.

Use the model ID `auto`.

* Easy turns go to a Fireworks open model.
* Harder turns go to an Anthropic or OpenAI model on your own account.
* You pay the chosen model's rate for each turn, not a closed model's rate on every turn.

Nexus Auto was formerly FireRouter. The `firerouter` model ID no longer works; use `auto` instead.

* FireRouter and the `firerouter` model ID are no longer available. Use `auto` in model pickers, SDK calls, and gateway configs.
* For each new user turn, Nexus Auto predicts which available model will handle it well at the lowest cost. That model serves the whole turn, including its tool calls, until the next user turn.
* Open models run on Fireworks serverless. Closed models run on your own Anthropic or OpenAI account.
* Nexus Auto works with the Chat Completions, Messages, and Responses APIs.
* Fireworks evaluates and updates the models behind `auto`, so the model ID stays the same.
* `auto` is the only Nexus Auto model ID. It needs a Fireworks key, plus an Anthropic or OpenAI credential for closed models.

## Which models `auto` can use

With only your Fireworks key, `auto` uses Fireworks open models. If you connect an Anthropic or OpenAI [Provider Key](/nexus/provider-keys), it can also use those models.

To keep `auto` on open models only, run `nexus auto --providers fireworks`.

| Credentials available | Models `auto` can use |
| - | - |
| Fireworks key only | Fireworks open models |
| Plus an Anthropic credential | Fireworks open models and Anthropic models |
| Plus an OpenAI credential | Fireworks open models and OpenAI models |
| Plus both | Fireworks open models, Anthropic models, and OpenAI models |

* With [Amazon Bedrock](/nexus/provider-keys/bedrock) connected, Nexus Auto can serve the model families routed there through the AWS account.

Limit to open models even when Anthropic or OpenAI credentials exist, then rerun the harness command (replace `claude` with the harness):

```bash wrap theme={null}
nexus auto --providers fireworks
nexus claude
```

* **Global setting:** saved in `~/.nexus/config.json`. Each harness picks it up the next time its command runs. Claude Desktop picks it up on its next request.
* **One value today:** `--providers` accepts only `fireworks`.
* **Saved keys:** Anthropic and OpenAI keys saved with `nexus auto` stay saved, but Nexus CLI doesn't send them while the limit is set.
* **Check or undo:** `nexus auto` shows the current setting. `nexus auto --reset` goes back to the default.
* **Account first:** the account's model restrictions always apply first.
* **Cursor IDE:** the setting has no effect there.

## Set up

### Nexus CLI

Connect your tool with [Nexus Desktop](/nexus/desktop) or the [Nexus CLI](/nexus/cli). Both set the model to `auto`:

```bash wrap theme={null}
nexus claude   # or codex, chatgpt, cursor, vscode, and more
```

Setup steps for each tool are in [Coding Harnesses](/nexus/harnesses).

* **Nexus CLI:** `nexus login`, optionally `nexus auto --anthropic-api-key`, then `nexus <harness>` and `nexus <harness> status`. Harness commands: `claude`, `codex`, `chatgpt`, `opencode`, `pi`, `vscode`, `copilot-cli`, `deepseek`, `cursor`, `copilot-app`. Each harness starts on `auto` after a restart (Claude Code: start a new session).
* **Claude Desktop:** Nexus CLI only, macOS. Run `nexus login`, optionally `nexus auto --anthropic-api-key`, then `nexus claude-desktop on` and `nexus claude-desktop status`. Quit and reopen Claude Desktop. The picker shows `auto` along with the Claude models.
* A connected [Provider Key](/nexus/provider-keys) adds Anthropic and OpenAI models in every harness. Without one, a developer can save their own key, then run the harness command again: `nexus auto --anthropic-api-key` (prompts for the key; or `--openai-api-key`), then for example `nexus opencode`. Cursor IDE and the Copilot App need a Provider Key.
* **Manual setup:** each harness page has a manual setup section with the config file. Set the model to `auto` and add `x-anthropic-api-key` or `x-openai-api-key` headers where the harness supports them. Cursor IDE, the Copilot App, and Claude Desktop can't send provider-key headers. See [manual setup](/nexus/manual-setup).
* Manual configs for Claude Code, Codex, OpenCode, Pi, Copilot CLI, and DeepSeek Harness were tested with a live request. The others mirror the settings Nexus CLI writes.
* Claude Code manual setup with an Anthropic key: set `ANTHROPIC_API_KEY` to the Anthropic key and put the Fireworks key in `ANTHROPIC_CUSTOM_HEADERS` as `X-Fireworks-Api-Key: fw_...`. Claude Code sends the Anthropic key as its API key.
* Codex manual setup: in `~/.codex/config.toml`, add `env_http_headers = { "x-anthropic-api-key" = "ANTHROPIC_API_KEY" }` to the `fireworks-ai` provider. The Codex CLI and the ChatGPT desktop app both read this file. Quit them before editing it.
* Wire API per harness: Messages for Claude Code and Claude Desktop, Responses for Codex and the ChatGPT desktop app, Chat Completions for the rest.

Nexus CLI saves a key from `nexus auto` in `~/.nexus/config.json`. It sends the key only from harnesses that have no sign-in of their own for that provider:

| Harness | Anthropic model turns | OpenAI model turns |
| - | - | - |
| Claude Code, Claude Agent SDK | Claude login or an exported `ANTHROPIC_API_KEY` | A key saved with `nexus auto`, or a Provider Key |
| Codex CLI, ChatGPT desktop app | A key saved with `nexus auto`, or a Provider Key | Codex sign-in (a ChatGPT plan or an OpenAI key) |
| OpenCode, Pi, VS Code, Copilot CLI, DeepSeek Harness | A key saved with `nexus auto`, or a Provider Key | A key saved with `nexus auto`, or a Provider Key |
| Claude Desktop | A key saved with `nexus auto`, or a Provider Key | A key saved with `nexus auto`, or a Provider Key |
| Cursor IDE, Copilot App | Provider Key only | Provider Key only |

* The Claude Agent SDK matches Claude Code when it reads the user settings that Nexus CLI writes. Claude Desktop's picker lists `auto` and Fireworks models only.
* **Where the key goes:** Nexus CLI writes it into the harness config as an `x-anthropic-api-key` or `x-openai-api-key` header. VS Code gets it on the `auto` model only. Claude Desktop's local proxy adds it to `auto` turns from the next request, so Claude Desktop doesn't need a restart.
* **No environment keys:** Nexus CLI never reads `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from the environment, and it writes nothing to the shell profile. A harness can still read its own variable, as Claude Code does with `ANTHROPIC_API_KEY`.
* **Check a key:** `nexus auto` shows which keys are saved on this machine and which Provider Keys are connected to the account. A saved key takes precedence over the Provider Key for that provider.
* **Remove a key:** `nexus auto --unset anthropic-api-key` or `nexus auto --unset openai-api-key` removes the key from Nexus CLI and from every harness that holds a copy. Restart those harnesses afterward. If a harness is open, Nexus CLI skips it and says to quit it and run the command again.
* **Only through `nexus auto`:** harness commands such as `nexus opencode` don't accept `--anthropic-api-key` or `--openai-api-key`. `nexus configure` still accepts them, but they are deprecated.
* **Upgrading from an earlier release:** the upgrade removes the `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` exports that earlier versions added to the shell profile. It also clears `{env:...}` key references from `~/.nexus/config.json`. A literal key saved with `nexus configure` is kept and sent as shown in the table.

### LLM gateway

Point your [LLM gateway](/nexus/llm-gateways), such as LiteLLM or Portkey, at Fireworks with your Fireworks API key and the model `auto`. Clients behind the gateway use only their gateway key.

* **LiteLLM:** in `config.yaml`, set `model_name: auto` and `litellm_params.model: fireworks_ai/accounts/fireworks/routers/auto`, with `api_key: os.environ/FIREWORKS_API_KEY` and `api_base: https://api.fireworks.ai/inference/v1`. Recent LiteLLM versions turn a short ID into a model path that returns 404.
* LiteLLM keys in the gateway config: add `extra_headers` with `x-anthropic-api-key: os.environ/ANTHROPIC_API_KEY` (and `x-openai-api-key: os.environ/OPENAI_API_KEY`). Set every variable before starting the proxy (`litellm --config config.yaml --port 4000`). A missing one makes each request fail with a 500. Clients send only their LiteLLM key.
* LiteLLM keys from each client: set `general_settings.forward_client_headers_to_llm_api: true`. Each client sends its own provider-key header.
* LiteLLM returns `model_name` in the response `model` field, not the model that served the turn.
* **Portkey:** create a Fireworks integration with the Fireworks API key, then call `https://api.portkey.ai/v1/chat/completions` with `x-portkey-api-key` and model `@YOUR_FIREWORKS_INTEGRATION/auto`. Portkey sends the rest of the ID to Fireworks unchanged.
* Portkey has no per-model header injection, so it supports Provider Keys or keys from each client. Clients list the provider-key headers in `x-portkey-forward-headers`, and should add them to `x-portkey-sensitive-headers` so Portkey masks them in logs.
* With Provider Keys, no provider credential passes through the gateway. Otherwise, check that the gateway redacts the provider-key headers, since gateways often log request headers.
* Other gateways and each credential option: [LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials).

### API and SDK

Point the OpenAI SDK at Fireworks and set the model to `auto`:

```python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_FIREWORKS_API_KEY",
    base_url="https://api.fireworks.ai/inference/v1",
)

response = client.chat.completions.create(
    model="auto",
    messages=[{"role": "user", "content": "Say pong in one word."}],
)
print(response.model, response.choices[0].message.content)
```

`auto` also works with the Anthropic SDK and the Responses API. Examples for both are in [APIs and SDKs](/nexus/apis-and-sdks).

| API | Base URL to configure | Full endpoint | Typical clients |
| - | - | - | - |
| Anthropic Messages | `https://api.fireworks.ai/inference` | `https://api.fireworks.ai/inference/v1/messages` | Anthropic SDK, Claude Code |
| OpenAI Chat Completions | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/chat/completions` | OpenAI SDK, Fireworks SDK, most gateways and harnesses |
| OpenAI Responses | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/responses` | OpenAI SDK, Codex |

Anthropic-style clients add `/v1/messages` to the base URL themselves, so their base URL ends at `/inference`.

Install: `pip install openai anthropic fireworks-ai` (Python) or `npm install openai @anthropic-ai/sdk` (TypeScript).

Sending a closed-model key per request (omit the header when Provider Keys are connected):

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/inference/v1",
    default_headers={"x-anthropic-api-key": os.environ["ANTHROPIC_API_KEY"]},
)
```

* Responses API: same client, `client.responses.create(model="auto", input=...)`, and send `x-openai-api-key` instead.
* Anthropic Messages: `anthropic.Anthropic(api_key=FIREWORKS_API_KEY, base_url="https://api.fireworks.ai/inference", default_headers={"x-anthropic-api-key": ...})`, with `max_tokens` set. Raw HTTP also sends `anthropic-version: 2023-06-01`.
* Some models return a `thinking` block before the text, so read the first `text` block rather than `content[0]`.
* TypeScript uses the same settings with `baseURL` and `defaultHeaders`.
* Errors and limits: [APIs and SDKs](/nexus/apis-and-sdks).

## Provide Anthropic and OpenAI credentials

Nexus Auto calls closed models through your own Anthropic, OpenAI, or [Amazon Bedrock](/nexus/provider-keys/bedrock) account.

* **[Provider Keys](/nexus/provider-keys) (recommended):** an admin connects the key once in Nexus settings, and it applies to everyone on the account.
* **Request headers:** send `x-anthropic-api-key` or `x-openai-api-key` with each request.

Without a credential for a provider, Nexus Auto uses the other models.

| | Provider Keys | Request headers |
| - | - | - |
| **Where the key lives** | Stored once in the Fireworks account by an admin | Sent with every request as `x-anthropic-api-key` or `x-openai-api-key` |
| **Who holds the key** | Only the account admin who connects it | Every client, or the gateway that adds the header |
| **Exposure** | Never returned in full after saving | Can appear in client configs and gateway request logs |
| **Best for** | Production, shared gateways, and teams | Testing, or choosing a key per request |
| **Availability** | Every Nexus plan | Every account |

* Bedrock uses Provider Keys only, with each model mapped to a Bedrock model ID and region.
* A request header takes precedence over the stored Provider Key for that provider.
* A request returns `400 no_credential` when it calls a closed model ID such as `claude-opus-5-5` directly and that credential is missing.

Every Nexus plan includes Provider Keys. You can also use your own key: save it with `nexus auto`, or send it as a request header.

## Check which model served a turn

The response `model` field names the model that served the turn, such as `glm-5p3` or `claude-opus-5-5`. In Claude Code, the status line also shows it.

Test request:

```bash wrap theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

* To confirm a closed-model credential, call that model ID directly, such as `claude-opus-5-5`. A `400 no_credential` error means the credential is missing.
* An easy prompt usually gets an open model. A harder prompt, such as debugging a concurrency bug or writing a proof, is more likely to get the closed model. No single request is guaranteed to use either.

## Cost and effort

* Open models bill to your Fireworks account at [serverless rates](/serverless/pricing).
* Closed models bill to the Anthropic or OpenAI account whose credential served the turn.
* Set [effort](/nexus/orchestration-preferences) in your tool. Higher effort asks for a more thorough attempt.

- Nexus Auto uses the effort setting when it picks a model.
- In the Codex CLI, a ChatGPT sign-in covers most OpenAI model turns. See [Who pays for OpenAI model turns](/nexus/harnesses/codex#who-pays-for-openai-model-turns).
- Cached input bills at the serving model's cached-input rate.
- In [Claude Code](/nexus/harnesses/claude-code) on `auto`, the status line shows the model that served the latest turn and the estimated session cost. `nexus claude usage` shows model choices, tokens, and estimated cost per turn. Pick a session to open its live meter, or pass `--session <id>` to open one directly.
- See [Usage and Cost](/nexus/metrics) for the columns, pricing, Fireworks usage, and Claude Code session estimates.

## Supported models

| Family | Model IDs | Credential |
| - | - | - |
| Claude Opus, Sonnet, Fable | `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-fable-5-1` | Anthropic |
| GPT Sol, Astra, Luna | `gpt-6.1-sol`, `gpt-6-astra`, `gpt-6-luna` | OpenAI |
| Kimi, GLM, DeepSeek | `kimi-k3`, `kimi-k3-fast`, `glm-5p3`, `glm-5p3-fast`, `glm-5p3-flash`, `deepseek-v4p1-flash` | Fireworks |

* `auto` decides which model serves each turn from the credentials provided. To send every turn to one model, [pin it](#pin-a-specific-model).
* Anthropic serves Claude Fable only to organizations with data retention enabled. Otherwise, Fable requests return a `400` error from Anthropic.

## Pin a specific model

On Enterprise, to use one model for every turn, use its ID instead of `auto`, such as `nexus claude --model glm-5p3` or `"model": "glm-5p3"` in a request.

* A full model ID such as `glm-5p3` stays on that version. Aliases such as `glm-latest` track the current version in a family and also skip Nexus Auto. See [Open Models](/nexus/open-models).
* Custom routes such as `firerouter/opus` and the latency-first `auto-instant` mix are retired. Nexus Auto does not accept `auto/...` route IDs. Pin a model ID or use `auto`. See [Deprecated and removed](/nexus/cli-reference#deprecated-and-removed).

## Web search

Web search is built into Nexus. In Claude Code, Claude Desktop, Codex, and ChatGPT, the app's native web search remains available. Fireworks runs the search server-side, so no search MCP server is required.

* Fireworks runs the search server-side and returns the results.
* It works with any Fireworks model and a standard `fw_...` key, with or without Nexus Auto.

| Harness | Search behavior | Wire API |
| - | - | - |
| Claude Code | Native `WebSearch` and `WebFetch` remain available | Messages |
| Claude Desktop | Native web search remains available | Messages |
| Codex CLI and ChatGPT desktop app | Native web search remains available | Responses |
| OpenCode, Pi, Cursor IDE, VS Code, Copilot, and DeepSeek Harness | Nexus CLI does not add web search | Not applicable |

Upgrading from the retired MCP: versions before 0.9.7 installed the `fireworks-websearch` MCP for Claude Code. It is retired because Fireworks handles Claude Code's native search tools server-side. `nexus update` removes the retired MCP and the tool denials earlier versions added to Claude Code, keeps other MCP servers, and removes the `web_search = "disabled"` line that version 0.9.6 wrote into the Codex config. Restart Claude Code and Codex afterward.

### Data residency

* With US [data residency](/accounts/data-residency), Nexus Auto serves open-model turns from [US-only Serverless](/serverless/us-only-serverless). Send requests to `us.api.fireworks.ai`. Anthropic and OpenAI turns still run on your own provider account, where that provider's data policies apply. See [Enterprise Controls](/nexus/enterprise-controls#control-models-and-regions).
* A request to Nexus Auto from an account set to a region other than US is rejected for data residency. Pin a model served in that region.

## Troubleshooting

**Nexus Auto never uses an Anthropic or OpenAI model.** No closed-model credential is reaching it. Run `nexus auto` to see what's connected, and connect a [Provider Key](/nexus/provider-keys) if none is.

What `nexus auto` may show:

* **"saved, not sent while auto is limited to fireworks":** run `nexus auto --reset`, then run the harness command again.
* **No key saved:** run `nexus auto --anthropic-api-key` or `--openai-api-key`, then the harness command again. Or connect a Provider Key.
* **"Sign in to see status":** run `nexus login`, which lets Nexus CLI read the account's Provider Keys.
* **"Not enabled on this account":** Provider Keys isn't turned on for this account. Nexus accounts include it; for a Fireworks platform account, contact Fireworks. Until then, save your own key with `nexus auto` instead.
* Nexus CLI doesn't send exported `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` values. In Codex, OpenAI model turns need a Codex sign-in or an OpenAI Provider Key.
