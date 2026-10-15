---
title: "Routing Preferences"
source: https://docs.fireworks.ai/nexus/routing-preferences
path: nexus/routing-preferences
---

Adjust how strongly a firerouter request favors its primary model or lower-cost models.

Routing preference controls how strongly a `firerouter` request favors its primary model or lower-cost models. Set it per HTTP request with the `x-routing-preference` header.

## Preference levels

Send an integer from **1** (strongest preference for the primary model) to **5** (strongest preference for lower-cost models):

| Value | Name | Behavior |
| - | - | - |
| `1` | `max-intelligence` | Keep the turn on the primary model |
| `2` | `more-intelligence` | Lean toward the primary, compared with balanced |
| `3` | `balanced` | Default when the header is omitted |
| `4` | `more-savings` | Lean toward lower cost, compared with balanced |
| `5` | `max-savings` | Prefer the lower-cost models in the route |

## HTTP header

The header accepts only the integers `1` to `5`. The names in the table are labels, not header values.

Set the header on an API request:

```bash wrap theme={null}
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

If the header is missing, invalid, or out of range, the router uses balanced behavior. It does not add a literal `x-routing-preference: 3` header.

## In a coding harness

To set a preference in a harness, send the header with [manual setup](/nexus/firerouter/setup#set-up-your-harness), for example in `ANTHROPIC_CUSTOM_HEADERS` for Claude Code or `http_headers` for Codex. Cursor IDE and the Copilot App cannot send extra headers.

FireConnect no longer sets routing preference. It ignores `--routing-preference` and prints a deprecation warning. On `on`, `off`, and `upgrade`, it also removes an `x-routing-preference` header from Claude Code, OpenCode, Pi, and VS Code configs, including one you added by hand.

## When to adjust

* **High-volume workloads with many simple requests**: try `4` or `5` so summaries, formatting, and straightforward Q\&A are more likely to use a lower-cost model.
* **Tasks where quality is critical** (security review, complex reasoning, nuanced writing): try `1` or `2` so the router favors its primary model.
* **Evaluating routing**: start at `3` (balanced), then move one step at a time and compare cost and output quality.

## Related

* [FireRouter](/nexus/firerouter): how `firerouter` picks a model for each turn
* [APIs and SDKs](/nexus/apis-and-sdks): HTTP headers and Provider Keys
* [FireConnect](/nexus/fireconnect): enable a router in a coding harness
