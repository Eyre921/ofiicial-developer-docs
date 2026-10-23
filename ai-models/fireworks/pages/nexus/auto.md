---
title: "Nexus Auto"
source: https://docs.fireworks.ai/nexus/auto
path: nexus/auto
---

Nexus Auto picks a Fireworks open model or an Anthropic or OpenAI model for each turn. Set it up in a coding harness, an LLM gateway, or an SDK.

Nexus Auto gives you one model ID, `auto`, and picks a model for each new user turn. Easy turns can go to a Fireworks open model. Harder turns can go to an Anthropic or OpenAI model on your own account. You pay the selected model's rate for each turn, not a closed model's rate on every turn.

> [!NOTE]
>
> Nexus Auto was formerly called FireRouter, and its model ID was `firerouter`. FireRouter and the `firerouter` model ID are no longer available. Use `auto` everywhere, including in model pickers, SDK calls, and gateway configs.

## How Nexus Auto works

For each new user turn, Nexus Auto predicts which available model will handle it well at the lowest cost. That model serves the whole turn, including its tool calls, until the next user turn. Open models run on Fireworks serverless. Closed models run on your own Anthropic or OpenAI account. The response `model` field names the model that served the turn, such as `glm-5p3` or `claude-opus-5-5`.

Nexus Auto works with the Chat Completions, Messages, and Responses APIs. Fireworks updates the models behind `auto` after evaluating them, so your model ID stays the same.

## Choose a model ID

| Model ID | What it uses | Credentials |
| - | - | - |
| `auto` | Fireworks open models, plus Anthropic or OpenAI models when you provide those credentials | Fireworks key. Add an Anthropic or OpenAI credential for closed models |

Use `auto` for most work. To choose a model yourself, [pin one](#pin-a-specific-model).

### Which models `auto` can use

Nexus Auto picks the model for each turn as the turn arrives. What it can choose from depends on the credentials that reach the request:

| Credentials available | Models `auto` can use |
| - | - |
| Fireworks key only | Fireworks open models |
| Plus an Anthropic credential | Fireworks open models and Anthropic models |
| Plus an OpenAI credential | Fireworks open models and OpenAI models |
| Plus both | Fireworks open models, Anthropic models, and OpenAI models |

Fireworks manages and updates the models behind `auto`. To see which one served a turn, read the response `model` field (see [Check which model served a turn](#check-which-model-served-a-turn)). Set [effort](/nexus/orchestration-preferences) in the harness to ask for a lighter or more thorough attempt.

If you connected [Amazon Bedrock](/nexus/provider-keys/bedrock), Nexus Auto can serve the model families you routed there through your AWS account.

To keep Nexus Auto on open models even when you have Anthropic or OpenAI credentials, limit it to Fireworks. Then run your harness command again, replacing `claude` with your harness:

```bash wrap theme={null}
nexus auto --providers fireworks
nexus claude
```

* **Global setting:** Nexus CLI saves it in `~/.nexus/config.json`. Each harness picks it up the next time you run its command. Claude Desktop picks it up on its next request.
* **One value today:** `--providers` accepts only `fireworks`.
* **Saved keys:** Anthropic and OpenAI keys you saved with `nexus auto` stay saved, but Nexus CLI doesn't send them while the limit is set.
* **Check or undo:** run `nexus auto` to see the current setting, and `nexus auto --reset` to go back to the default.
* **Account first:** your account's model restrictions always apply first.
* **Cursor IDE:** the setting has no effect there.

## Set up

Every setup uses `auto` and your Fireworks API key. Only the way you provide the closed-model credential changes.

### Nexus CLI

[Nexus CLI](/nexus/cli) writes your coding harness settings and restores them with `off`. To edit the files yourself with nothing to install, use [manual setup](/nexus/manual-setup).

Pick your harness and a setup method. The commands and config files update as you choose, including any provider-key headers.

A connected [Provider Key](/nexus/provider-keys) adds Anthropic and OpenAI models in every harness. Without one, save your own key with `nexus auto`. Then run your harness command again, replacing `opencode` with your harness:

```bash wrap theme={null}
nexus auto --anthropic-api-key   # prompts for the key (or --openai-api-key)
nexus opencode
```

Nexus CLI saves the key in `~/.nexus/config.json`. It sends the key only from harnesses that have no sign-in of their own for that provider:

| Harness | Anthropic model turns | OpenAI model turns |
| - | - | - |
| Claude Code, Claude Agent SDK | Your Claude login or an exported `ANTHROPIC_API_KEY` | A key saved with `nexus auto`, or a Provider Key |
| Codex CLI, ChatGPT desktop app | A key saved with `nexus auto`, or a Provider Key | Your Codex sign-in (a ChatGPT plan or an OpenAI key) |
| OpenCode, Pi, VS Code, Copilot CLI, DeepSeek Harness | A key saved with `nexus auto`, or a Provider Key | A key saved with `nexus auto`, or a Provider Key |
| Claude Desktop | A key saved with `nexus auto`, or a Provider Key | A key saved with `nexus auto`, or a Provider Key |
| Cursor IDE, Copilot App | Provider Key only | Provider Key only |

The Claude Agent SDK matches Claude Code when it reads the user settings that Nexus CLI writes. Claude Desktop's picker lists `auto` and Fireworks models only.

* **Where the key goes:** Nexus CLI writes it into the harness config as an `x-anthropic-api-key` or `x-openai-api-key` header. VS Code gets it on the `auto` model only. Claude Desktop's local proxy adds it to `auto` turns from the next request, so Claude Desktop doesn't need a restart.
* **No environment keys:** Nexus CLI never reads `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment, and it writes nothing to your shell profile. A harness can still read its own variable, as Claude Code does with `ANTHROPIC_API_KEY`.
* **Check a key:** `nexus auto` shows which keys are saved on this machine and which Provider Keys are connected to your account. A saved key takes precedence over the Provider Key for that provider.
* **Remove a key:** `nexus auto --unset anthropic-api-key` or `nexus auto --unset openai-api-key` removes the key from Nexus CLI and from every harness that holds a copy. Restart those harnesses afterward. If a harness is open, Nexus CLI skips it and tells you to quit it and run the command again.
* **Only through `nexus auto`:** harness commands such as `nexus opencode` don't accept `--anthropic-api-key` or `--openai-api-key`. `nexus configure` still accepts them, but they are deprecated.
* **Upgrading from an earlier release:** the upgrade removes the `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` exports that earlier versions added to your shell profile. It also clears `{env:...}` key references from `~/.nexus/config.json`. A literal key saved with `nexus configure` is kept and sent as shown in the table.

Nexus CLI doesn't send saved keys from Cursor IDE or the Copilot App, so they need Provider Keys. In the other harnesses, you can add the headers yourself with [manual setup](/nexus/manual-setup).

For a full walkthrough, see [Claude Code](/nexus/harnesses/claude-code). For each harness's files and restore behavior, see [Coding Harnesses](/nexus/harnesses).

### LLM gateway

The gateway sends `auto` and your Fireworks API key to Fireworks, so you don't need Nexus CLI. Clients behind the gateway call `auto` with only their gateway key.

Choose LiteLLM or Portkey, a model ID, and where the provider keys live. The widget writes the gateway config and a test request.

For other gateways and each credential option, see [LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials).

### API and SDK

Point the SDK you already use at Fireworks. Its API key is your Fireworks API key. For an Anthropic or OpenAI model, connect a [Provider Key](/nexus/provider-keys) or send the provider's key as a header (see [Provide Anthropic and OpenAI credentials](#provide-anthropic-and-openai-credentials)).

| API | Base URL to configure | Full endpoint | Typical clients |
| - | - | - | - |
| Anthropic Messages | `https://api.fireworks.ai/inference` | `https://api.fireworks.ai/inference/v1/messages` | Anthropic SDK, Claude Code |
| OpenAI Chat Completions | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/chat/completions` | OpenAI SDK, Fireworks SDK, most gateways and harnesses |
| OpenAI Responses | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/responses` | OpenAI SDK, Codex |

Anthropic-style clients add `/v1/messages` to the base URL themselves, so their base URL ends at `/inference`.

```bash Python theme={null}
pip install openai anthropic fireworks-ai
```

```bash TypeScript theme={null}
npm install openai @anthropic-ai/sdk
```

Pick an API and a language. The code adds the provider header that API needs, or leaves it out if you have Provider Keys connected.

The Anthropic SDK's base URL is `https://api.fireworks.ai/inference`, without `/v1`. Some models return a `thinking` block before the text, so the snippet reads the first `text` block rather than `content[0]`. For errors and limits, see [APIs and SDKs](/nexus/apis-and-sdks).

## Provide Anthropic and OpenAI credentials

Nexus Auto calls closed models through your own Anthropic, OpenAI, or [Amazon Bedrock](/nexus/provider-keys/bedrock) account. For Anthropic and OpenAI, store the key once as a Provider Key or send it with each request. Bedrock uses Provider Keys only, with each model mapped to a Bedrock model ID and region.

| | Provider Keys | Request headers |
| - | - | - |
| **Where the key lives** | Stored once in your Fireworks account by an admin | Sent with every request as `x-anthropic-api-key` or `x-openai-api-key` |
| **Who holds the key** | Only the account admin who connects it | Every client, or the gateway that adds the header |
| **Exposure** | Never returned in full after you save it | Can appear in client configs and gateway request logs |
| **Best for** | Production, shared gateways, and teams | Testing, or choosing a key per request |
| **Availability** | Not enabled on every account | Every account |

A request header takes precedence over the stored Provider Key for that provider.

> [!NOTE]
>
> Provider Keys isn't available on every account yet. If **Provider Keys**
> doesn't appear in [Settings](https://app.fireworks.ai/settings/provider-keys),
> [contact the Fireworks team](https://fireworks.ai/demo-request) to turn it on.

Without a credential for a closed provider, Nexus Auto leaves that provider's models out and serves the turn with the others. A request returns `400 no_credential` when you call a closed model ID such as `claude-opus-5-5` directly and that credential is missing.

## Check which model served a turn

1. Send a request with `auto`:
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
2. Check the response `model` field. It names the model that served the turn, such as `glm-5p3` or `claude-opus-5-5`.
3. An easy prompt usually gets an open model. A harder prompt, such as debugging a concurrency bug or writing a proof, is more likely to get the closed model. No single request is guaranteed to use either. In a coding harness, set [effort](/nexus/orchestration-preferences) to ask for a lighter or more thorough attempt.
4. To confirm a closed-model credential, call that model ID directly, such as `claude-opus-5-5`. A `400 no_credential` error means the credential is missing.

## Watch orchestration live

In Claude Code, you can watch each turn's model choice as you work. [Connect Claude Code](/nexus/harnesses/claude-code) with `auto`. The status line shows the model that served the latest turn and the estimated session cost. For a per-turn breakdown of model choices, tokens, and estimated cost, run:

```bash wrap theme={null}
nexus claude usage
```

Pick a session to open its live meter, or pass `--session <id>` to open one directly. See [Usage and Cost](/nexus/metrics) for the columns and pricing.

## Balance quality and savings

Set [effort](/nexus/orchestration-preferences) in the harness. Higher effort asks for a more thorough attempt. Lower effort asks for a lighter one. Nexus Auto uses that when it picks a model.

## Pay for the model that serves each turn

Open models bill to your Fireworks account at their [serverless rates](/serverless/pricing). Closed models bill to the Anthropic or OpenAI account whose credential served the turn. In the Codex CLI, a ChatGPT sign-in covers most OpenAI model turns; see [Who pays for OpenAI model turns](/nexus/harnesses/codex#who-pays-for-openai-model-turns). Cached input bills at the serving model's cached-input rate.

Use [Usage and Cost](/nexus/metrics) to review Fireworks usage and Claude Code session estimates.

## Supported models

`auto` decides which model serves each turn from the credentials you provide. To send every turn to one model below, [pin it](#pin-a-specific-model).

| Family | Current model ID | Credential |
| - | - | - |
| Claude Opus | `claude-opus-5-5` | Anthropic |
| Claude Fable | `claude-fable-5-1` | Anthropic, with data retention enabled |
| Claude Sonnet | `claude-sonnet-5-5` | Anthropic |
| GPT Sol | `gpt-6.1-sol` | OpenAI |
| GPT Astra | `gpt-6-astra` | OpenAI |
| GPT Luna | `gpt-6-luna` | OpenAI |
| Kimi | `kimi-k3`, `kimi-k3-fast` | Fireworks |
| GLM | `glm-5p3`, `glm-5p3-fast`, `glm-5p3-flash` | Fireworks |
| DeepSeek | `deepseek-v4p1-flash` | Fireworks |

Anthropic serves Claude Fable only to organizations with data retention enabled. Otherwise, Fable requests return a `400` error from Anthropic.

## Pin a specific model

To choose a model yourself, use its ID instead of `auto`. In a harness, pass it with `--model`. In a request, set it as the `model` value:

```bash wrap theme={null}
nexus claude --model glm-5p3
```

A pinned model serves every turn. A full model ID such as `glm-5p3` stays on that version. Aliases such as `glm-latest` track the current version in a family and also skip Nexus Auto. See [Open Models](/nexus/open-models).

> [!NOTE]
>
> Custom routes such as `firerouter/opus` are no longer available, and Nexus Auto does not accept `auto/...` route IDs. The latency-first `auto-instant` mix is retired too. Pin a model ID as shown above, or use `auto`. See [Deprecated and removed](/nexus/cli-reference#deprecated-and-removed).

## Limitations

* Nexus Auto is not available through Microsoft Foundry. See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry).
* Accounts with data residency enabled cannot use Nexus Auto. Use a residency-compatible pinned serverless model instead.

## Troubleshooting

> **Nexus Auto never uses an Anthropic or OpenAI model**
>
> No closed-model credential is reaching Nexus Auto. Save a key with `nexus auto --anthropic-api-key` or `--openai-api-key`, then run your harness command again. Or connect the matching [Provider Key](/nexus/provider-keys).
>
> Run `nexus auto` to see what's set:
>
> * **"saved, not sent while auto is limited to fireworks":** run `nexus auto --reset`, then run your harness command again.
> * **"Sign in to see status":** run `nexus login` so Nexus CLI can read your account's Provider Keys.
> * **"Not enabled on this account":** your account can't use Provider Keys yet. Save your own key with `nexus auto` instead.
>
> Nexus CLI doesn't send exported `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` values. In Codex, OpenAI model turns need a Codex sign-in or an OpenAI Provider Key.
