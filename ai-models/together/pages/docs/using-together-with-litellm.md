---
title: "Power Claude Code with LiteLLM and Together AI"
source: https://docs.together.ai/docs/using-together-with-litellm
path: docs/using-together-with-litellm
---

Run Claude Code on Together coding models through a local LiteLLM proxy.

Run Claude Code on Together coding models such as GLM 5.3, Kimi K3, and DeepSeek V4 by routing it through [LiteLLM](https://docs.litellm.ai/), an open-source gateway you run on your own machine. The LiteLLM proxy serves the Anthropic Messages API used by Claude Code and sends each call to the Together API.

<Tip>
  [TogetherLink](/docs/how-to-use-togetherlink) also runs Claude Code on Together models, with no proxy to manage.
</Tip>

## Requirements

* Claude Code, [installed](https://docs.anthropic.com/en/docs/claude-code/setup) and working.
* Python 3.10 or later, with `pip` or [uv](https://docs.astral.sh/uv/).
* A [Together API key](/docs/api-keys-authentication).

## Step 1: Install LiteLLM

Install the proxy with `pip` or `uv`:

<CodeGroup>
  ```bash pip theme={null}
  pip install "litellm[proxy]>=1.100.0"
  ```

  ```bash uv theme={null}
  uv tool install "litellm[proxy]>=1.100.0"
  ```
</CodeGroup>

## Step 2: Export your Together API key

LiteLLM reads the key from `TOGETHERAI_API_KEY`, not `TOGETHER_API_KEY` like the Together SDKs. Set it in your terminal before starting:

```bash theme={null}
export TOGETHERAI_API_KEY=<together_api_key>
```

## Step 3: Configure the proxy

Define your models in a `config.yaml`. Prefix each Together model ID with `together_ai/`, and give each model a short alias to pass to Claude Code. Any model from the [serverless catalog](/docs/serverless/models) works:

```yaml config.yaml theme={null}
model_list:
  - model_name: glm-5.3
    litellm_params:
      model: together_ai/zai-org/GLM-5.3
      api_key: os.environ/TOGETHERAI_API_KEY
  - model_name: kimi-k3
    litellm_params:
      model: together_ai/moonshotai/Kimi-K3
      api_key: os.environ/TOGETHERAI_API_KEY
```

## Step 4: Start the proxy

Start the server:

```bash theme={null}
litellm --config config.yaml --port 4000 --host 127.0.0.1
```

<Tip>
  The `--host 127.0.0.1` flag keeps the proxy reachable only from your own machine.
</Tip>

The proxy takes over this terminal, so open a new one and verify it serves your models:

```bash theme={null}
curl http://localhost:4000/v1/models
```

You should see your aliases in the response:

```json theme={null}
{
  "data": [
    { "id": "glm-5.3", "object": "model" },
    { "id": "kimi-k3", "object": "model" }
  ]
}
```

## Step 5: Connect Claude Code

In the same terminal, point Claude Code at the proxy and pass an alias from your config:

```bash theme={null}
export ANTHROPIC_BASE_URL=http://localhost:4000
export ANTHROPIC_AUTH_TOKEN=anything
claude --model glm-5.3
```

The proxy doesn't check `ANTHROPIC_AUTH_TOKEN`, so any value works. Setting it lets Claude Code run without an Anthropic login. If you're logged in to Claude Code, you can omit it.

Claude Code starts as usual, with every request going through the proxy to the Together API.

<Check>
  Claude Code is now running on GLM 5.3, served by Together AI through your own gateway.
</Check>

## Secure the proxy (optional)

A master key makes the proxy require a key on every request. Set one before exposing the proxy beyond your machine, since anyone who can reach an unauthenticated proxy can spend on your Together account. The master key is a secret you make up, not a key issued by Together or LiteLLM:

```yaml config.yaml theme={null}
general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
```

Export a random value in the terminal that runs the proxy, then restart it:

```bash theme={null}
export LITELLM_MASTER_KEY=sk-$(openssl rand -hex 16)
litellm --config config.yaml --port 4000 --host 127.0.0.1
```

Clients now authenticate with the master key. Pass it as `ANTHROPIC_AUTH_TOKEN` for Claude Code, and as a Bearer token for direct calls to the proxy. To give other people their own keys and budgets instead of sharing the master key, create [virtual keys](https://docs.litellm.ai/docs/proxy/virtual_keys), which also require a Postgres database.

## Troubleshooting

**Requests fail with `No connected db`:** The proxy has a master key configured and the token you passed doesn't match it. This usually means `LITELLM_MASTER_KEY` is unset or has a different value in the terminal where you ran `claude` or `curl`. Export the value the proxy started with and try again.

**The proxy logs `Invalid model name passed in model=claude-sonnet-5`:** Something in your session, such as a subagent pinned to Anthropic's `sonnet` alias, requested a model that isn't in your `model_list`. Claude Code keeps working, but those requests fail. To route the aliases to a Together model, export `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5.3` (and the matching `OPUS` and `HAIKU` variables) before starting Claude Code.

## Next steps

<CardGroup>
  <Card title="TogetherLink" icon="link" href="/docs/how-to-use-togetherlink">
    Run Claude Code on Together models without hosting a proxy.
  </Card>

  <Card title="Serverless models" icon="stack-2" href="/docs/serverless/models">
    Browse every model you can serve through the proxy.
  </Card>

  <Card title="OpenAI compatibility" icon="plug" href="/docs/inference/openai-compatibility">
    See how the Together API maps to OpenAI's format.
  </Card>

  <Card title="Third-party integrations" icon="puzzle" href="/docs/inference/sdk-integrations">
    Use Together through other partner SDKs and gateways.
  </Card>
</CardGroup>
