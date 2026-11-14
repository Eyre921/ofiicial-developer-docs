---
title: "Migrate to Fireworks"
source: https://docs.fireworks.ai/tools-sdks/migrate-to-fireworks
path: tools-sdks/migrate-to-fireworks
---

Move an app from the OpenAI, Anthropic, NVIDIA NIM, or vLLM APIs to Fireworks. Keep your SDK and change the base URL, API key, and model name.

Fireworks accepts OpenAI, Anthropic, and NVIDIA NIM or vLLM requests, so your SDK and app code stay as they are. You change three values: the base URL, the API key, and the model name.

| Your app uses | Start here |
| - | - |
| OpenAI SDKs or the OpenAI API format | [OpenAI compatibility](/tools-sdks/openai-compatibility) |
| Anthropic SDKs or the Messages API | [Anthropic compatibility](/tools-sdks/anthropic-compatibility) |
| NVIDIA NIM or vLLM, including their extra request fields | [NIM compatibility](/tools-sdks/nim-compatibility) |

## How to migrate

**1. Create an API key**

Create a key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys) and export it:

```bash theme={null}
export FIREWORKS_API_KEY="<YOUR_FIREWORKS_API_KEY>"
```

**2. Point your client at Fireworks**

Pick your API in the tabs below. In your existing code, update the highlighted lines: the base URL, API key, and model name. The rest of your code stays the same.

```python OpenAI {5-6,10} theme={null}
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.environ["FIREWORKS_API_KEY"],
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k3",
    messages=[{"role": "user", "content": "Say hello in one word."}],
)
print(response.choices[0].message.content)
```

```python Anthropic {5-6,10} theme={null}
import os
import anthropic

client = anthropic.Anthropic(
    base_url="https://api.fireworks.ai/inference",  # no /v1
    api_key=os.environ["FIREWORKS_API_KEY"],
)

response = client.messages.create(
    model="accounts/fireworks/models/kimi-k3",
    max_tokens=256,
    messages=[{"role": "user", "content": "Say hello in one word."}],
)
print(response.content[0].text)
```

```python NIM / vLLM {5-6,10} theme={null}
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.environ["FIREWORKS_API_KEY"],
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k3",
    messages=[{"role": "user", "content": "Say hello in one word."}],
    # NIM-style extras still work. Fireworks maps this to reasoning_effort="none".
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
)
print(response.choices[0].message.content)
```

```bash cURL theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k3",
    "messages": [{"role": "user", "content": "Say hello in one word."}]
  }'
```

```bash Environment variables theme={null}
# OpenAI SDKs
export OPENAI_BASE_URL="https://api.fireworks.ai/inference/v1"
export OPENAI_API_KEY="$FIREWORKS_API_KEY"

# Anthropic SDKs, Claude Code, and the Claude Agent SDK
export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"  # no /v1
export ANTHROPIC_AUTH_TOKEN="$FIREWORKS_API_KEY"
```

**3. Pick a replacement model**

Fireworks model names use the format `accounts/fireworks/models/<model>`. To find the closest match for the model you use today, see [Compare models](/guides/recommended-models) or browse the [model catalog](https://fireworks.ai/models).

**4. Check what behaves differently**

Most requests work unchanged. These are the differences that most often affect a migration:

* OpenAI: when the prompt plus `max_tokens` exceeds the context window, Fireworks lowers `max_tokens` instead of returning an error. Set `context_length_exceeded_behavior` to `error` to match OpenAI. Streaming responses include `usage` in the final chunk.
* Anthropic: Fireworks does not run server-side tools such as web search, code execution, memory, or web fetch. Declare them as client-side tools and run them yourself. The `anthropic-version` header is ignored.
* NIM and vLLM: Fireworks maps the thinking keys in `chat_template_kwargs` to `reasoning_effort` and drops any other keys in that object.

Each guide lists every supported field: [OpenAI](/tools-sdks/openai-compatibility#api-compatibility), [Anthropic](/tools-sdks/anthropic-compatibility#differences-from-anthropic), [NIM](/tools-sdks/nim-compatibility).

**5. Test before you switch traffic**

Send one request first. Then run the prompts, tool calls, and streaming paths your app depends on, and compare output quality and latency before you move production traffic.

## Next steps

> [card] [Get an API key](https://app.fireworks.ai/settings/users/api-keys)
>
> Create and manage keys in the Fireworks dashboard.

> [card] [Compare models](/guides/recommended-models)
>
> Open-weight alternatives to Claude, GPT, and Gemini by use case.
