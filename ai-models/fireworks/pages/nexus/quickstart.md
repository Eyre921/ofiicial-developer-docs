---
title: "Quickstart"
source: https://docs.fireworks.ai/nexus/quickstart
path: nexus/quickstart
---

Connect a coding harness, application, or LLM gateway to Fireworks and make your first Nexus request.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

Pick how you work. Each path takes a few minutes and uses the same Fireworks models, routers, and account controls.

> **[Coding harness](#connect-a-coding-harness)**
>
> Claude Code, Codex, OpenCode, Cursor IDE, and more

> **[API or SDK](#call-the-api)**
>
> OpenAI, Anthropic, or Fireworks SDK

> **[LLM gateway](#use-an-llm-gateway)**
>
> LiteLLM, Portkey, and other gateways

You need a [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) for the API and gateway paths. FireConnect can create one for you when you sign in.

## Connect a coding harness

**1. Install FireConnect**

```bash wrap theme={null}
curl -fsSL https://fireconnect.fireworks.ai/install.sh | bash
```

Requires Node.js 18 or later. On Windows, run it from Git Bash.

**2. Sign in**

```bash wrap theme={null}
fireconnect login
```

Sign in with your browser, or paste an existing Fireworks key.

**3. Connect your harness**

```bash Claude Code theme={null}
fireconnect claude
```

```bash Codex CLI theme={null}
fireconnect codex
```

```bash ChatGPT desktop app theme={null}
# Quit the ChatGPT desktop app first
fireconnect chatgpt
```

```bash OpenCode theme={null}
fireconnect opencode
```

```bash Cursor IDE theme={null}
fireconnect cursor
```

```bash VS Code theme={null}
fireconnect vscode
```

```bash Pi theme={null}
fireconnect pi
```

The Codex CLI and the ChatGPT desktop app share one config, so `fireconnect codex` and `fireconnect chatgpt` connect both. For desktop apps, including Cursor IDE and VS Code, quit the app first. See [Coding Harnesses](/nexus/harnesses) for every harness.

**4. Restart and pick a model**

Restart the harness and open its model picker. You will see `auto`, FireRouter, and Fireworks open models.

![Claude Code model picker with FireRouter selected and Auto, DeepSeek, GLM, Kimi, and MiniMax options](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/claude-model-picker.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=cab8623549ed73df655ebfb39dd11fb0)

> [!TIP]
>
> `fireconnect claude status` shows Fireworks as the provider and the configured model.

> [!TIP]
>
> **Prefer not to install anything?** Every harness has a **Manual setup** tab
> in [Coding Harnesses](/nexus/harnesses) with the exact settings to add
> yourself.

## Call the API

**1. Export your key**

```bash wrap theme={null}
export FIREWORKS_API_KEY="fw_..."
```

**2. Send a request**

Point the SDK you already use at Fireworks:

```bash cURL theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-latest",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

```python OpenAI SDK theme={null}
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/inference/v1",
)

response = client.chat.completions.create(
    model="glm-latest",
    messages=[{"role": "user", "content": "Say pong in one word."}],
)

print(response.choices[0].message.content)
```

```python Anthropic SDK theme={null}
import os

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/inference",
)

message = client.messages.create(
    model="glm-latest",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say pong in one word."}],
)

print(next(block.text for block in message.content if block.type == "text"))
```

```python Fireworks SDK theme={null}
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="glm-latest",
    messages=[{"role": "user", "content": "Say pong in one word."}],
)

print(response.choices[0].message.content)
```

> [!TIP]
>
> The reply says `pong`.

**3. Try a router**

Change `model` to `firerouter`. FireRouter picks a model for each turn, and the response `model` field shows which one served it. Claude and GPT turns need a [provider credential](/nexus/firerouter#provide-anthropic-and-openai-credentials).

More examples, including the Responses API: [FireRouter Setup](/nexus/firerouter/setup#api-and-sdk).

## Use an LLM gateway

**1. Add a Fireworks model to LiteLLM**

```yaml config.yaml theme={null}
model_list:
  - model_name: glm-latest
    litellm_params:
      model: fireworks_ai/accounts/fireworks/routers/glm-latest
      api_key: os.environ/FIREWORKS_API_KEY
      api_base: https://api.fireworks.ai/inference/v1
```

**2. Start the proxy**

```bash wrap theme={null}
pip install "litellm[proxy]"
litellm --config config.yaml
```

**3. Send a request**

```bash wrap theme={null}
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-latest",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

> [!TIP]
>
> The reply says `pong`.

Using Portkey, or adding FireRouter to your gateway? See [FireRouter Setup](/nexus/firerouter/setup#llm-gateway) and [LLM Gateways](/nexus/llm-gateways).

## Next steps

> **[Open Models](/nexus/open-models)**
>
> Use `auto`, follow a model family, choose a fast tier, or pin a version.

> **[FireRouter](/nexus/firerouter)**
>
> Let one model ID choose a model for each new user turn.

> **[Usage and Cost](/nexus/metrics)**
>
> See session estimates and Fireworks model usage by model, user, or API key.

> **[Spend Limits](/nexus/usage-limits)**
>
> Set per-user caps for supported Fireworks serverless models.
