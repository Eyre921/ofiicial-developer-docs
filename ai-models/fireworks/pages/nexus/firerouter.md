---
title: "FireRouter"
source: https://docs.fireworks.ai/nexus/firerouter
path: nexus/firerouter
---

Learn what FireRouter is, how it picks a model for each user turn, which models it routes to, how to pass Anthropic or OpenAI credentials, and how to watch routing live.

FireRouter gives you one model ID, `firerouter`, and picks a model for each new user turn. Easy turns can go to a Fireworks open model. Harder turns can go to a closed model such as Claude Opus or GPT Sol. You pay the selected model's rate for each turn instead of a closed model's rate on every turn.

## How FireRouter works

1. You send a request to Fireworks with the `firerouter` model ID and your Fireworks API key.
2. For each new user turn, FireRouter predicts which available model will handle the turn well at the lowest cost.
3. The selected model serves the whole turn, including its tool calls, until the next user turn.
4. Fireworks open models run on Fireworks serverless. Closed models run on your own Anthropic or OpenAI account, using a credential you provide.
5. The response `model` field names the model that served the turn, such as `glm-5p3` or `claude-opus-5-5`.

FireRouter works with the Chat Completions, Messages, and Responses APIs. Fireworks updates the models behind `firerouter` after evaluating them, so you do not need to change your model ID.

## Choose a router

| Model ID | What it can use | Credentials |
| - | - | - |
| `firerouter` | Claude Opus or GPT Sol, [chosen from your credentials and client](#how-bare-firerouter-picks-its-closed-model), plus the Fireworks open-model mix | Fireworks key, plus an Anthropic or OpenAI credential |
| `auto` | Fireworks open models only | Fireworks key |
| `auto-instant` | The lowest-latency Fireworks open models | Fireworks key |

Use `firerouter` for closed-model quality with open-model savings. Use `auto` if you only have a Fireworks key.

To choose the models yourself, see [Pin specific models](#pin-specific-models).

### How bare `firerouter` picks its closed model

`firerouter` picks one closed model from the credentials available to the request. It then routes between that model and the open-model mix:

| Credentials available | Closed model |
| - | - |
| Anthropic only | Claude Opus |
| OpenAI only | GPT Sol |
| Anthropic and OpenAI | GPT Sol for Responses API requests and Codex. Claude Opus for Messages API requests, Claude Code, and other Chat Completions clients. |
| Neither | None. Kimi K3 and the open-model mix serve every turn. |

The open-model mix currently includes GLM 5.3 and GLM 5.3 Flash. Fireworks manages it and updates it as new open models are released and evaluated.

Easy turns usually go to the open-model mix. Harder turns usually go to the closed model. At routing preference `1`, every turn uses the closed model.

If you connected [Amazon Bedrock](/nexus/provider-keys/bedrock), FireRouter prefers a Bedrock model from the family it picked above, which can be GPT Astra or an earlier Opus or Sol version. To choose the closed model yourself, see [Pin specific models](#pin-specific-models).

In Codex, FireConnect's **FireRouter** row is `firerouter`, so GPT turns use GPT Sol, unless you mapped GPT Astra in Bedrock. See [Codex](/nexus/harnesses#codex).

### Route across open models with `auto`

`auto` and `auto-instant` route each turn across Fireworks open models only, so they need no closed-model credential. Fireworks picks the models behind them and updates them as new open models are released and evaluated.

| Model ID | Best for | Models it uses today |
| - | - | - |
| `auto` | The best open model for each turn | GLM 5.3, GLM 5.3 Flash, and Kimi K3 |
| `auto-instant` | The lowest latency | GLM 5.3 Flash, with other open models taking over when it is slow |

FireConnect defaults Codex to `firerouter` and other harnesses to `auto`. Claude Code keeps Claude's tier models, adds `auto` and `firerouter` to `/model`, and starts on `firerouter` unless you already chose a Fireworks model. See [Open Models](/nexus/open-models) for fast-model governance and other open-model IDs.

## Supported models

FireRouter can route to these models. `firerouter` uses Claude Opus or GPT Sol, plus the open-model mix. To route to the others, [pin them](#pin-specific-models).

### Closed models

| Family | Current model ID | Provider credential |
| - | - | - |
| Claude Opus | `claude-opus-5-5` | Anthropic |
| Claude Fable | `claude-fable-5-1` | Anthropic, with data retention enabled on your Anthropic organization |
| Claude Sonnet | `claude-sonnet-5-5` | Anthropic |
| GPT Sol | `gpt-6.1-sol` | OpenAI |
| GPT Astra | `gpt-6-astra` | OpenAI |
| GPT Luna | `gpt-6-luna` | OpenAI |

Anthropic serves Claude Fable only to organizations with data retention enabled. Otherwise, Fable requests return a `400` error from Anthropic.

### Fireworks open models

| Family | Model IDs |
| - | - |
| Kimi | `kimi-k3`, `kimi-k3-fast` |
| GLM | `glm-5p3`, `glm-5p3-fast`, `glm-5p3-flash` |
| DeepSeek | `deepseek-v4p1-flash` |

Open models use your Fireworks API key. No other credential is needed.

<Note>
  Aliases such as `glm-latest` and `kimi-fast-latest` are Fireworks serverless
  model IDs that you call directly, without FireRouter. See
  [Open Models](/nexus/open-models) for `-latest` aliases.
</Note>

## Use FireRouter from your tools

The model ID is the same everywhere. Only the setup changes.

| You are using | Setup guide | Closed-model credential |
| - | - | - |
| Claude Code, Codex, OpenCode, or another coding harness | [Set up with FireConnect](/nexus/firerouter/setup#fireconnect) | Your Claude login in Claude Code, your Codex sign-in in the Codex CLI, a local key in some harnesses, or Provider Keys |
| LiteLLM, Portkey, or another LLM gateway | [Connect an LLM gateway](/nexus/firerouter/setup#llm-gateway) | Provider Keys, or keys stored in the gateway config |
| Your own app, agent, or script | [Use the API or SDK](/nexus/firerouter/setup#api-and-sdk) | Provider Keys, or a request header |

You do not need FireConnect to use FireRouter from an application or gateway. You need a Fireworks API key, plus an Anthropic or OpenAI credential for closed models.

## Provide Anthropic and OpenAI credentials

FireRouter calls closed models through your own Anthropic, OpenAI, or [Amazon Bedrock](/nexus/provider-keys/bedrock) account. Your Fireworks API key is always required. Each closed provider FireRouter uses also needs a credential. For Anthropic and OpenAI, there are two ways to provide one. Bedrock uses Provider Keys only, with each model mapped to a Bedrock model ID and region.

| | Provider Keys | Request headers |
| - | - | - |
| **Where the key lives** | Stored once in your Fireworks account by an admin | Sent with every request as `x-anthropic-api-key` or `x-openai-api-key` |
| **Who holds the key** | Only the account admin who connects it | Every client, or the gateway that adds the header |
| **Exposure** | Never returned in full after you save it | Can appear in client configs and gateway request logs |
| **Best for** | Production, shared gateways, and teams | Testing, or choosing a key per request |
| **Availability** | Not enabled on every account | Every account |

If a request carries a provider header, that header takes precedence over the stored Provider Key for that provider.

In the Codex CLI, your Codex sign-in can also pay for GPT turns, through your ChatGPT plan or the OpenAI key you signed in with. For GPT turns, FireRouter uses an `x-openai-api-key` header first, then your Codex sign-in, then an OpenAI Provider Key. Your ChatGPT plan doesn't cover `gpt-5.5`, `gpt-5.6-terra`, or `gpt-5.6-luna`. Those turns need an OpenAI Provider Key. See [Codex](/nexus/harnesses#codex).

<Note>
  Provider Keys is not yet available on every account. If **Provider Keys**
  does not appear in [Settings](https://app.fireworks.ai/settings/provider-keys),
  [contact the Fireworks team](https://fireworks.ai/demo-request) to enable it.
  Self-serve setup is coming soon.
</Note>

Setup steps: [Provider Keys](/nexus/provider-keys), [request headers for APIs and SDKs](/nexus/apis-and-sdks#credentials), and [gateway credentials](/nexus/llm-gateways#provide-closed-model-credentials).

### What happens without a closed-model credential

If no credential is available for a closed provider, FireRouter leaves that provider's models out and serves the turn with the other models. For example, `firerouter` with no Anthropic or OpenAI credential serves every turn with Fireworks open models.

A request returns `400 no_credential` instead when you set routing preference `1`, which forces the route's closed primary, or when you call a closed model ID directly, such as `claude-opus-5-5` without `firerouter/`.

## Verify routing

To confirm that closed models are reachable:

1. Send a request with the `x-routing-preference: 1` header. FireRouter then uses the closed model on every turn.

   ```bash wrap theme={null}
   curl https://api.fireworks.ai/inference/v1/chat/completions \
     -H "Authorization: Bearer $FIREWORKS_API_KEY" \
     -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
     -H "x-routing-preference: 1" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "firerouter",
       "messages": [{"role": "user", "content": "Say pong in one word."}]
     }'
   ```

2. Check the response `model` field. It should name the closed model, such as `claude-opus-5-5`. A `400 no_credential` error means the provider credential is missing.

3. Remove the header and send an easy prompt. The `model` field usually names an open model such as `glm-5p3`. Harder prompts, such as debugging a concurrency bug or writing a proof, are more likely to use the closed model. No single request is guaranteed to use either.

## Watch routing live

In Claude Code, you can watch each turn's model choice as you work. [Connect Claude Code](/nexus/harnesses#claude-code) with a FireRouter model, install `tmux`, then run:

```bash wrap theme={null}
fireconnect claude live
```

Claude Code opens on the left. A live meter on the right adds one row per user turn with the model or models selected, token buckets, cache share, estimated cost, and a prompt preview.

<Frame>
  <img alt="Split terminal with Claude Code on the left and a live meter on the right showing GLM 5.3 Flash and Opus 5 model choices, token buckets, cache share, and estimated cost per turn" />
</Frame>

To follow a specific session, run `fireconnect claude live --session <id>`. Meter columns and pricing: [Session Cost](/nexus/session-usage).

## Balance quality and savings

Routing preference controls how strongly a `firerouter` request favors its primary model or lower-cost models. Send `x-routing-preference` with a value from `1` (`max-intelligence`) to `5` (`max-savings`). The default is `3` (`balanced`).

Routing preference is set per request with the header. It is not part of the model ID, and FireConnect no longer sets it. See [Routing Preferences](/nexus/routing-preferences).

## Pay for the model that serves each turn

* **Fireworks open models** bill to your Fireworks account at their [serverless rates](/serverless/pricing).
* **Closed models** bill to the Anthropic or OpenAI account whose credential served the turn. A ChatGPT sign-in in the Codex CLI bills most GPT turns to your ChatGPT plan. The exceptions bill to your OpenAI Provider Key, as listed in [Provide Anthropic and OpenAI credentials](#provide-anthropic-and-openai-credentials).
* **Cached input** bills at the serving model's cached-input rate.

Use [Usage and Cost](/nexus/metrics) to review Fireworks usage and Claude Code session estimates.

## Pin specific models

Most users should use `firerouter`. FireConnect lists only `firerouter`.

FireRouter still accepts router IDs that name specific models. Use them from the API, SDKs, or an LLM gateway. In FireConnect, pass one with `--model`.

### Build a router ID

A router ID is `firerouter/` followed by up to eight models, separated by slashes. The first model is the primary.

| Router ID | What FireRouter does | Credentials |
| - | - | - |
| `firerouter/opus` | Routes between Claude Opus and the open-model mix | Anthropic |
| `firerouter/astra` | Routes between GPT Astra and the open-model mix. Also sends medium-difficulty turns to GPT Sol. | OpenAI |
| `firerouter/glm-5p3` | Serves GLM 5.3 on every turn | None |
| `firerouter/opus/glm-5p3` | Picks only from the models you list | Anthropic |
| `firerouter/auto` | Same as `auto`. `firerouter/auto-instant` matches `auto-instant`. | None |

* **Aliases:** `opus`, `fable`, `sol`, `astra`, `luna`, `kimi` or `k3`, and `glm` follow the newest model in each family. Claude Sonnet has no alias.
* **Model IDs:** use one from [Supported models](#supported-models) to pin a version. Earlier versions such as `claude-opus-5` or `gpt-5.6-sol` also work.
* **One closed model:** FireRouter routes between it and the open-model mix. At routing preference `1`, every turn uses it.
* **GPT Astra:** for Astra and open models only, without GPT Sol, use `firerouter/gpt-6-astra`.
* **One open model:** it serves every turn, with no routing. If it can't serve a turn, FireRouter may finish that turn on another Fireworks open model.
* **Listed models:** FireRouter picks only from your list. The primary serves turns when FireRouter can't make a confident choice, and every turn at routing preference `1`. If the picked model can't serve a turn, FireRouter may finish it on another Fireworks open model. It never falls back to a closed model, and it doesn't fall back at routing preference `1`.
* **Credentials:** `opus`, `fable`, or a `claude-...` model needs an Anthropic credential. `sol`, `astra`, `luna`, or a `gpt-...` model needs an OpenAI credential.
* **Errors:** an unknown alias or model, such as `firerouter/sonnet`, or more than eight models returns `404 Model id not found`.

To pick models and copy a ready-to-run command, use the [interactive builder](/nexus/firerouter/setup#build-your-request).

## Limitations

* FireRouter is not available through Microsoft Foundry. See [Foundry for Coding Harnesses](/nexus/microsoft-foundry).
* Accounts with data residency enabled cannot use FireRouter. Use a residency-compatible pinned serverless model instead.
