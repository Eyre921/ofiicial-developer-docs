---
title: "Routing preferences"
source: https://docs.fireworks.ai/ecosystem/firerouter/routing-preferences
path: ecosystem/firerouter/routing-preferences
---

Tune FireRouter between closed-source quality and open-model savings

FireRouter routes each new user turn sent to `firerouter` to either a closed-source model (pass-through) or a Fireworks open model (redirect). The **`x-routing-preference`** request header controls the quality-versus-cost tradeoff.

Set the preference per request with the HTTP header below, or pass `--routing-preference` when you run `fireconnect <harness> on`.

## Preference levels

Send an integer from **1** (most quality-protective) to **5** (most savings-focused):

| Value | Name                | Behavior                                                                                                                       |
| ----- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `1`   | `max-intelligence`  | For ranked routes, force the route's primary with no cross-model fallback. Retryable failures may receive one same-model retry |
| `2`   | `more-intelligence` | Increase intelligence weighting relative to balanced                                                                           |
| `3`   | `balanced`          | Default when the header is omitted. FireRouter's standard tradeoff                                                             |
| `4`   | `more-savings`      | Increase cost weighting relative to balanced                                                                                   |
| `5`   | `max-savings`       | For ranked routes, rank eligible models by cost                                                                                |

In-order routes keep their configured model order instead of using this ranking.

## HTTP header

Set the header on each request:

```text theme={null}
-H "x-routing-preference: 4"
```

The HTTP header accepts only the integers `1`–`5`. Names such as `balanced` are FireConnect CLI values, not HTTP header values.

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

On Claude Code, `--routing-preference` requires at least one slot set to `firerouter`. See [Choose where FireRouter is used](/ecosystem/fireconnect/claude-code#choose-where-firerouter-is-used).

Supported on Claude Code, OpenCode, Pi, and VS Code. Values are `1`–`5` or the level names (`max-intelligence`, `balanced`, `max-savings`, etc.). The flag applies when at least one configured slot uses `firerouter`. Codex, Cursor, and DeepSeek Harness do not support `--routing-preference`.

You can also store a global Anthropic BYOK key once:

```bash theme={null}
fireconnect configure --anthropic-api-key sk-ant-...
```

## When to adjust

* **High-volume workloads with many simple requests**: try `4` or `5` to redirect summaries, formatting, and straightforward Q\&A.
* **Tasks where quality is critical** (security review, complex reasoning, nuanced writing): try `1` or `2` to keep closed-source models on harder prompts.
* **Evaluating routing**: start at `3` (balanced), then move one step at a time and compare cost and output quality.

For eligible tool-call continuations, modes `2`–`4` may reuse the model selected for the same user turn when route caching is available. Modes `1` and `5` do not use this route cache.

## Related

* [Overview](/ecosystem/firerouter/overview): how redirect vs. pass-through works
* [FireConnect overview](/ecosystem/fireconnect/overview#firerouter-and-smart-routers): enable FireRouter in coding harnesses
* [Quickstart](/ecosystem/firerouter/quickstart): API call examples
* [LiteLLM](/ecosystem/firerouter/litellm): add FireRouter to LiteLLM Proxy
