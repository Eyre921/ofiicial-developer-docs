---
title: "Routing Preferences"
source: https://docs.fireworks.ai/nexus/routing-preferences
path: nexus/routing-preferences
---

Adjust how strongly a firerouter request favors its primary model or lower-cost models.

Routing preference controls how strongly a `firerouter` request favors its primary model or lower-cost models. Set it per HTTP request with `x-routing-preference`, or configure it for a supported harness with FireConnect.

## Preference levels

Send an integer from **1** (strongest preference for the primary model) to **5** (strongest preference for lower-cost models):

| Value | Name                | Behavior                                        |
| ----- | ------------------- | ----------------------------------------------- |
| `1`   | `max-intelligence`  | Keep the turn on the primary model              |
| `2`   | `more-intelligence` | Lean toward the primary, compared with balanced |
| `3`   | `balanced`          | Default when the header is omitted              |
| `4`   | `more-savings`      | Lean toward lower cost, compared with balanced  |
| `5`   | `max-savings`       | Prefer the lower-cost models in the route       |

## HTTP header

The HTTP header accepts only the integers `1` to `5`. Names such as `balanced` are FireConnect CLI values, not HTTP header values.

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

## FireConnect

When you connect a harness to `firerouter` or a supported `firerouter/...` ID, pass `--routing-preference` with the connect command:

```bash wrap theme={null}
fireconnect claude --model firerouter --routing-preference 4
fireconnect opencode --model firerouter --routing-preference 2
fireconnect pi --model firerouter --routing-preference 5
```

| Harness                                      | Supported model IDs                                 |
| -------------------------------------------- | --------------------------------------------------- |
| Claude Code                                  | Bare `firerouter` only                              |
| OpenCode, Pi, VS Code                        | `firerouter` or any ID beginning with `firerouter/` |
| Codex, Cursor IDE, Copilot, DeepSeek Harness | Not supported                                       |

FireConnect accepts values `1` to `5` or the corresponding level names. Claude Code returns an error if you combine `--routing-preference` with a compound ID such as `firerouter/opus`. Cursor CLI is not supported.

## When to adjust

* **High-volume workloads with many simple requests**: try `4` or `5` so summaries, formatting, and straightforward Q\&A are more likely to use a lower-cost model.
* **Tasks where quality is critical** (security review, complex reasoning, nuanced writing): try `1` or `2` so the router favors its primary model.
* **Evaluating routing**: start at `3` (balanced), then move one step at a time and compare cost and output quality.

## Related

* [FireRouter](/nexus/firerouter): `firerouter`, `firerouter/opus`, and `firerouter/astra`
* [APIs and SDKs](/nexus/apis-and-sdks): HTTP headers and Provider Keys
* [FireConnect](/nexus/fireconnect): enable a router in a coding harness
