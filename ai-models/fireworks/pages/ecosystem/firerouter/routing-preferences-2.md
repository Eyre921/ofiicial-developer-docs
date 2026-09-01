---
title: "Routing preferences"
source: https://docs.fireworks.ai/ecosystem/firerouter/routing-preferences
path: ecosystem/firerouter/routing-preferences
---

Tune FireRouter between closed-source quality and open-model savings

FireRouter scores each request to `firerouter` and routes to either a closed-source model (pass-through) or a Fireworks open model (redirect). The **`x-routing-preference`** request header lets you bias that decision toward quality or savings.

## Preference levels

Send an integer from **1** (most quality-protective) to **5** (most savings-focused):

| Value | Name                | Behavior                                                           |
| ----- | ------------------- | ------------------------------------------------------------------ |
| `1`   | `max-intelligence`  | Strongest bias toward pass-through; use when quality is critical   |
| `2`   | `more-intelligence` | Favor closed-source models on borderline requests                  |
| `3`   | `balanced`          | Default when the header is omitted. FireRouter's standard tradeoff |
| `4`   | `more-savings`      | Favor open-model redirects on borderline requests                  |
| `5`   | `max-savings`       | Strongest bias toward redirect; maximize cost savings              |

## HTTP header

Set the header on each request:

```bash theme={null}
-H "x-routing-preference: 4"
```

Example with curl:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "x-routing-preference: 4" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "firerouter",
    "messages": [{"role": "user", "content": "Add a docstring to this function."}]
  }'
```

If the header is missing, invalid, or out of range, FireRouter uses the balanced default (`3`).

## FireConnect

When you enable FireRouter through FireConnect, pass `--routing-preference` on `on` instead of setting a header yourself:

```bash theme={null}
fireconnect claude on --model firerouter --routing-preference 4
fireconnect opencode on --model firerouter --routing-preference 2
fireconnect pi on --model firerouter --routing-preference 5
```

Supported on Claude Code, OpenCode, Pi, and VS Code. Values are `1`–`5` or the level names (`max-intelligence`, `balanced`, `max-savings`, etc.). The flag applies when at least one configured slot uses `firerouter`. Codex, Cursor, and DeepSeek Harness do not support `--routing-preference`.

You can also store a global Anthropic BYOK key once:

```bash theme={null}
fireconnect configure --anthropic-api-key sk-ant-...
```

## When to adjust

* **High-volume workloads with many simple requests**: try `4` or `5` to redirect summaries, formatting, and straightforward Q\&A.
* **Tasks where quality is critical** (security review, complex reasoning, nuanced writing): try `1` or `2` to keep closed-source models on harder prompts.
* **Evaluating routing**: start at `3` (balanced), then move one step at a time and compare cost and output quality.

FireRouter caches routing decision within a conversation, so preference changes can take a few turns to take effect without restarting your client.

## Related

* [Overview](/ecosystem/firerouter/overview): how redirect vs. pass-through works
* [FireConnect overview](/ecosystem/fireconnect/overview#firerouter): enable FireRouter in coding harnesses
* [Quickstart](/ecosystem/firerouter/quickstart): API call examples
* [LiteLLM](/ecosystem/firerouter/litellm): add FireRouter to LiteLLM Proxy
