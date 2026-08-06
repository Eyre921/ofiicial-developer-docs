---
title: "NIM compatibility"
source: https://docs.fireworks.ai/tools-sdks/nim-compatibility
path: tools-sdks/nim-compatibility
---

Point NVIDIA NIM and vLLM OpenAI clients at Fireworks. We translate common extras like chat_template_kwargs so requests don't fail with Extra inputs are not permitted.

If you already call models through **NVIDIA NIM**, **vLLM**, or another OpenAI-compatible stack that sends NIM-style extras, you can point that client at Fireworks without rewriting every request.

Fireworks Chat Completions is OpenAI-compatible. NIM and vLLM often add fields that aren't in the OpenAI schema — for example `chat_template_kwargs` to turn thinking off. Without translation, those requests fail with `400 Extra inputs are not permitted`. Fireworks accepts the common ones and maps them onto native parameters.

For first-party Fireworks apps, prefer native controls such as [`reasoning_effort`](/api-reference/post-chatcompletions). See the [Reasoning guide](/guides/reasoning).

Also see: [OpenAI compatibility](/tools-sdks/openai-compatibility) · [Anthropic compatibility](/tools-sdks/anthropic-compatibility).

## Quickstart

Use any OpenAI-compatible client. Set the base URL to Fireworks and use your Fireworks API key:

```python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<FIREWORKS_API_KEY>",
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k3",
    messages=[{"role": "user", "content": "Say hi in one word."}],
    # NIM-style: disable thinking without rewriting to reasoning_effort
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
)

print(response.choices[0].message.content)
```

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k3",
    "messages": [{"role": "user", "content": "Say hi in one word."}],
    "chat_template_kwargs": {"enable_thinking": false}
  }'
```

Set `model` to a Fireworks model resource name (for example `accounts/fireworks/models/kimi-k3`). Streaming works the same way — translation happens before the response starts.

<Tip>
  When you control the request body yourself, prefer native Fireworks fields (`reasoning_effort`, `prompt_truncate_len`, `response_format`). Use NIM field names when you're migrating an existing NIM or vLLM client and want drop-in behavior.
</Tip>

## Thinking and reasoning

NIM clients usually toggle thinking with `chat_template_kwargs`. Fireworks maps those onto [`reasoning_effort`](/api-reference/post-chatcompletions):

| What you send                                                               | What Fireworks does                                                                          |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `chat_template_kwargs: {"enable_thinking": false}` (or `"thinking": false`) | Sets `reasoning_effort` to `"none"` and drops the kwargs object                              |
| `{"enable_thinking": true}` alone (or `"thinking": true`)                   | Drops the kwargs object and leaves thinking at the **model default** (does not force a tier) |
| `{"reasoning_budget": 512}`                                                 | Sets `reasoning_effort` to that integer token budget (when thinking isn't off)               |
| `{"low_effort": true}`                                                      | Sets `reasoning_effort` to `"low"` (when no budget is set)                                   |
| `reasoning_effort: "auto"`                                                  | Drops `"auto"` (Fireworks doesn't accept it) so the model default applies                    |

Other keys inside `chat_template_kwargs` (for example `parallel_reasoning_mode`) are dropped with the object — they aren't applied.

When thinking is on, responses may include `message.reasoning_content`. When thinking is off (`reasoning_effort: "none"`), `reasoning_content` is typically null. Details: [Reasoning](/guides/reasoning).

<Note>
  If both `reasoning_effort: "auto"` and a thinking kwargs mapping are present, Fireworks drops `"auto"` first, then applies the kwargs mapping (so `enable_thinking: false` still becomes `"none"`).
</Note>

### Example: tools with thinking off

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k3",
    "messages": [{"role": "user", "content": "Call the say tool with x=hi."}],
    "tools": [{
      "type": "function",
      "function": {
        "name": "say",
        "description": "Echo text",
        "parameters": {
          "type": "object",
          "properties": {"x": {"type": "string"}},
          "required": ["x"]
        }
      }
    }],
    "tool_choice": "required",
    "chat_template_kwargs": {"enable_thinking": false}
  }'
```

## Prompt truncation

| NIM / vLLM               | Fireworks                        |
| ------------------------ | -------------------------------- |
| `truncate_prompt_tokens` | Renamed to `prompt_truncate_len` |

If you send both, `prompt_truncate_len` wins.

## Structured outputs (`guided_*`)

NIM/vLLM guided decoding fields map onto Fireworks [`response_format`](/structured-responses/structured-response-formatting):

| NIM / vLLM                  | Fireworks `response_format`                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `guided_json: <schema>`     | `{"type": "json_schema", "json_schema": {"name": "response", "schema": <schema>}}`                             |
| `guided_grammar: "<abnf>"`  | `{"type": "grammar", "grammar": "<abnf>"}`                                                                     |
| `guided_choice: ["a", "b"]` | `{"type": "json_schema", "json_schema": {"name": "choice", "schema": {"type": "string", "enum": ["a", "b"]}}}` |

If more than one `guided_*` field is present, priority is `guided_json` → `guided_grammar` → `guided_choice`. An explicit `response_format` in the request always wins over guided fields.

`guided_regex` is **not** supported (Fireworks grammars are ABNF-style). That field is stripped so the request doesn't 400 — use `guided_grammar` or native `response_format` instead.

## Fields we ignore (stripped)

These NIM/vLLM extras have no Fireworks Chat Completions equivalent. Fireworks removes them so your request isn't rejected. They do **not** change generation:

`guided_regex`, `guided_decoding_backend`, `stop_token_ids`, `include_stop_str_in_output`, `skip_special_tokens`, `spaces_between_special_tokens`, `best_of`, `use_beam_search`, `add_generation_prompt`, `continue_final_message`, `add_special_tokens`, `detokenize`, `allowed_token_ids`, `bad_words`, `include_reasoning`, `nvext`

<Note>
  `min_tokens` is **kept**. Fireworks supports it natively — it is not stripped.
</Note>

Anything else Fireworks already supports (`top_k`, `min_p`, `repetition_penalty`, and other native fields) passes through unchanged.

## Prefer native parameters when you can

```python theme={null}
client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k3",
    messages=[...],
    reasoning_effort="none",   # instead of chat_template_kwargs.enable_thinking=false
    prompt_truncate_len=4096,  # instead of truncate_prompt_tokens
    response_format={          # instead of guided_json / guided_grammar
        "type": "json_schema",
        "json_schema": {"name": "answer", "schema": {...}},
    },
)
```

## Good to know

* **Models that can't disable reasoning.** Mapping `enable_thinking: false` → `reasoning_effort: "none"` returns 400 on models that don't allow `"none"` (same as sending `reasoning_effort: "none"` directly).
* **`enable_thinking: true` vs LiteLLM.** Fireworks leaves model-default thinking (omits `reasoning_effort`). Some LiteLLM Fireworks mappings send `"medium"` instead. Set an explicit `reasoning_effort` when you need a specific tier.
* **Accepted string efforts** include `low`, `medium`, `high`, `xhigh`, `max`, `none`, and (when the model supports it) `adaptive`. `"auto"` is dropped to the model default.
* **OpenAI-standard traffic is unchanged.** Normal `reasoning_effort` values (`"high"`, `"low"`, …) and `tool_choice: "auto"` are not rewritten.

## Next steps

<CardGroup>
  <Card title="Reasoning" href="/guides/reasoning" icon="brain">
    Native reasoning\_effort, streaming, and tool use
  </Card>

  <Card title="Structured responses" href="/structured-responses/structured-response-formatting" icon="brackets-curly">
    json\_schema and grammar response\_format
  </Card>

  <Card title="OpenAI compatibility" href="/tools-sdks/openai-compatibility" icon="code">
    Use the OpenAI SDK with Fireworks
  </Card>
</CardGroup>
