---
title: "FireRouter Setup"
source: https://docs.fireworks.ai/nexus/firerouter/setup
path: nexus/firerouter/setup
---

Set up FireRouter in a coding harness with FireConnect, in an LLM gateway such as LiteLLM or Portkey, or from the OpenAI, Anthropic, or Fireworks SDK.

Use the same model ID, such as `auto` or `firerouter/opus`, from a coding harness, an LLM gateway, or your own code. Every path needs a Fireworks API key. Each closed provider in the route also needs a credential. See [Provide Anthropic and OpenAI credentials](/nexus/firerouter#provide-anthropic-and-openai-credentials).

| You are using | Setup |
| - | - |
| Claude Code, Codex, OpenCode, Cursor IDE, or another coding harness | [FireConnect](#fireconnect) |
| LiteLLM, Portkey, or another LLM gateway | [LLM gateway](#llm-gateway) |
| Your own app, agent, or script | [API and SDK](#api-and-sdk) |

## Choose a model ID

| Model ID | What it routes across | Credentials |
| - | - | - |
| `auto` | Fireworks open models only | Fireworks API key |
| `firerouter` | Claude Opus or GPT Sol, [picked from your credentials and client](/nexus/firerouter#how-bare-firerouter-picks-its-closed-model), plus the open-model mix | Fireworks key, plus an Anthropic or OpenAI credential |
| `firerouter/opus`, `firerouter/sol`, `firerouter/astra` | The named closed family, plus the open-model mix | Fireworks key, plus the matching provider credential |
| `firerouter/opus/glm-5p3` | Only the models you list | Fireworks key, plus a credential for each closed provider listed |

Start with `auto` if you only have a Fireworks key. Without a closed-model credential, any `firerouter` ID serves every turn with open models. See [Build a router ID](/nexus/firerouter#build-a-router-id) and [Supported models](/nexus/firerouter#supported-models).

## FireConnect

Use FireRouter in any coding harness. [FireConnect](/nexus/fireconnect) writes the settings for you and restores them with `off`. Manual setup gives you the same settings to add yourself, with nothing to install.

### Set up your harness

Pick your harness, a model or router ID, and a setup method. Start with `auto` to route across Fireworks open models with only a Fireworks key, or choose **Build your own** to compose a `firerouter` route with Claude, GPT, and open models. The commands and config files update as you choose, including the provider-key headers your route needs.

<FireRouterHarnessSetup />

<Accordion title="FireConnect quick start for Claude Code">
  <Steps>
    <Step title="Install and sign in">
      ```bash wrap theme={null}
      curl -fsSL https://fireconnect.fireworks.ai/install.sh | bash
      fireconnect login
      ```
    </Step>

    <Step title="Connect with a router">
      ```bash wrap theme={null}
      fireconnect claude --model firerouter
      ```
    </Step>

    <Step title="Restart and pick FireRouter">
      Start a new session and open `/model`. Routes with Claude models use your Claude login.
    </Step>

    <Step title="Watch routing live">
      ```bash wrap theme={null}
      fireconnect claude live
      ```

      A meter beside Claude Code shows the model selected for each turn. See [Watch routing live](/nexus/firerouter#watch-routing-live).
    </Step>
  </Steps>
</Accordion>

### Which harnesses can send provider keys

| Harness | FireConnect with Claude routes | FireConnect with GPT routes | Manual setup |
| - | - | - | - |
| Claude Code | Your Claude login, or `--anthropic-api-key` | OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| Codex CLI, Codex app, ChatGPT desktop, OpenCode, Pi, VS Code | `--anthropic-api-key`, or an Anthropic Provider Key | OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| Copilot CLI, DeepSeek Harness | Not supported yet | OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| Cursor IDE, Copilot App | Not supported | OpenAI Provider Key | Provider Keys only; these apps cannot send extra headers |

FireConnect has no local OpenAI key option yet, so GPT routes such as `firerouter/astra` and `firerouter/sol` need an OpenAI [Provider Key](/nexus/provider-keys) when you connect with FireConnect. To send your own OpenAI key, use manual setup. For every harness's files and restore behavior, see [Coding Harnesses](/nexus/harnesses) and [Harness Compatibility](/nexus/harness-compatibility).

## LLM gateway

You do not need FireConnect behind a gateway. The gateway sends the exact `firerouter/...` model ID and your Fireworks API key to Fireworks. Clients and harnesses behind the gateway call the router ID with only their gateway key.

### Set up your gateway

Choose LiteLLM or Portkey, pick a preset or build your own route, and choose where the provider keys live. The widget writes the gateway config and a test request.

<FireRouterGatewaySetup />

Clients never need provider keys when the gateway stores them or when [Provider Keys](/nexus/provider-keys) is connected. For other gateways and more detail on each credential option, see [LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials).

## API and SDK

FireRouter works on all three Fireworks inference APIs. Use the SDK you already have and point it at Fireworks.

| API | Endpoint | SDKs |
| - | - | - |
| Chat Completions (OpenAI-compatible) | `https://api.fireworks.ai/inference/v1/chat/completions` | OpenAI SDK, Fireworks SDK |
| Responses (OpenAI-compatible) | `https://api.fireworks.ai/inference/v1/responses` | OpenAI SDK |
| Messages (Anthropic-compatible) | `https://api.fireworks.ai/inference/v1/messages` | Anthropic SDK, Fireworks SDK |

In every SDK, the API key is your **Fireworks** API key. Send closed-provider keys as extra headers:

| Header | When |
| - | - |
| `x-anthropic-api-key` | The route includes a Claude model and no Anthropic Provider Key is connected |
| `x-openai-api-key` | The route includes a GPT model and no OpenAI Provider Key is connected |

Leave out a header when the matching [Provider Key](/nexus/provider-keys) is connected. A header, when sent, takes precedence over the stored key for that request. [Amazon Bedrock](/nexus/provider-keys/bedrock) has no request header; it uses Provider Keys only.

Install the SDKs you use:

<CodeGroup>
  ```bash Python theme={null}
  pip install openai anthropic fireworks-ai
  ```

  ```bash TypeScript theme={null}
  npm install openai @anthropic-ai/sdk
  ```
</CodeGroup>

### Build your request

Pick your models, API, and language. The router ID and the command update as you choose, with the provider headers your route needs.

<FireRouterBuilder />

### Examples

The examples below use two router IDs:

* **`firerouter/astra`** in the Chat Completions and Responses examples. FireRouter routes between GPT Astra and the Fireworks open-model mix, so it needs an OpenAI key. `firerouter/sol` works the same way with GPT Sol.
* **`firerouter/opus`** in the Messages examples. FireRouter routes between Claude Opus and the Fireworks open-model mix, so it needs an Anthropic key.

Any router ID works on any API. To use a different route, change `model` and send the header for each closed provider in it. See [Supported models](/nexus/firerouter#supported-models) and [Build a router ID](/nexus/firerouter#build-a-router-id).

#### Chat Completions

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.fireworks.ai/inference/v1/chat/completions \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "x-openai-api-key: $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "firerouter/astra",
      "messages": [{"role": "user", "content": "Say pong in one word."}]
    }'
  ```

  ```python OpenAI SDK (Python) theme={null}
  import os

  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["FIREWORKS_API_KEY"],
      base_url="https://api.fireworks.ai/inference/v1",
      # Omit when an OpenAI Provider Key is connected.
      default_headers={"x-openai-api-key": os.environ["OPENAI_API_KEY"]},
  )

  response = client.chat.completions.create(
      model="firerouter/astra",
      messages=[{"role": "user", "content": "Say pong in one word."}],
  )

  print(response.model, response.choices[0].message.content)
  ```

  ```typescript OpenAI SDK (TypeScript) theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.FIREWORKS_API_KEY,
    baseURL: "https://api.fireworks.ai/inference/v1",
    // Omit when an OpenAI Provider Key is connected.
    defaultHeaders: { "x-openai-api-key": process.env.OPENAI_API_KEY },
  });

  const response = await client.chat.completions.create({
    model: "firerouter/astra",
    messages: [{ role: "user", content: "Say pong in one word." }],
  });

  console.log(response.model, response.choices[0].message.content);
  ```

  ```python Fireworks SDK (Python) theme={null}
  import os

  from fireworks import Fireworks

  # Reads FIREWORKS_API_KEY from the environment.
  client = Fireworks(
      # Omit when an OpenAI Provider Key is connected.
      default_headers={"x-openai-api-key": os.environ["OPENAI_API_KEY"]},
  )

  response = client.chat.completions.create(
      model="firerouter/astra",
      messages=[{"role": "user", "content": "Say pong in one word."}],
  )

  print(response.model, response.choices[0].message.content)
  ```
</CodeGroup>

#### Responses

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.fireworks.ai/inference/v1/responses \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "x-openai-api-key: $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "firerouter/astra",
      "input": "Say pong in one word."
    }'
  ```

  ```python OpenAI SDK (Python) theme={null}
  import os

  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["FIREWORKS_API_KEY"],
      base_url="https://api.fireworks.ai/inference/v1",
      # Omit when an OpenAI Provider Key is connected.
      default_headers={"x-openai-api-key": os.environ["OPENAI_API_KEY"]},
  )

  response = client.responses.create(
      model="firerouter/astra",
      input="Say pong in one word.",
  )

  print(response.model, response.output_text)
  ```

  ```typescript OpenAI SDK (TypeScript) theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.FIREWORKS_API_KEY,
    baseURL: "https://api.fireworks.ai/inference/v1",
    // Omit when an OpenAI Provider Key is connected.
    defaultHeaders: { "x-openai-api-key": process.env.OPENAI_API_KEY },
  });

  const response = await client.responses.create({
    model: "firerouter/astra",
    input: "Say pong in one word.",
  });

  console.log(response.model, response.output_text);
  ```
</CodeGroup>

#### Messages

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.fireworks.ai/inference/v1/messages \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "firerouter/opus",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Say pong in one word."}]
    }'
  ```

  ```python Anthropic SDK (Python) theme={null}
  import os

  import anthropic

  client = anthropic.Anthropic(
      api_key=os.environ["FIREWORKS_API_KEY"],
      base_url="https://api.fireworks.ai/inference",
      # Omit when an Anthropic Provider Key is connected.
      default_headers={"x-anthropic-api-key": os.environ["ANTHROPIC_API_KEY"]},
  )

  message = client.messages.create(
      model="firerouter/opus",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Say pong in one word."}],
  )

  text = next(block.text for block in message.content if block.type == "text")
  print(message.model, text)
  ```

  ```typescript Anthropic SDK (TypeScript) theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic({
    apiKey: process.env.FIREWORKS_API_KEY,
    baseURL: "https://api.fireworks.ai/inference",
    // Omit when an Anthropic Provider Key is connected.
    defaultHeaders: { "x-anthropic-api-key": process.env.ANTHROPIC_API_KEY },
  });

  const message = await client.messages.create({
    model: "firerouter/opus",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Say pong in one word." }],
  });

  const text = message.content.find((block) => block.type === "text");
  console.log(message.model, text?.type === "text" ? text.text : "");
  ```

  ```python Fireworks SDK (Python) theme={null}
  import os

  from fireworks import Fireworks

  # Reads FIREWORKS_API_KEY from the environment.
  client = Fireworks(
      # Omit when an Anthropic Provider Key is connected.
      default_headers={"x-anthropic-api-key": os.environ["ANTHROPIC_API_KEY"]},
  )

  message = client.messages.create(
      model="firerouter/opus",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Say pong in one word."}],
  )

  text = next(block.text for block in message.content if block.type == "text")
  print(message.model, text)
  ```
</CodeGroup>

The Anthropic SDK base URL is `https://api.fireworks.ai/inference`, without `/v1`. The SDK adds `/v1/messages`. Some models return a `thinking` block before the text, so read the first `text` block rather than `content[0]`.

### Check which model served the request

Each example prints the response `model` field. It names the model that served the turn, such as `glm-5p3-flash`, `claude-opus-5-5`, or `gpt-6-astra`, not the router ID you sent. To confirm closed-model access, add `x-routing-preference: 1` so the route's primary model serves the turn. See [Verify routing](/nexus/firerouter#verify-routing).

For errors, limits, and more API details, see [APIs and SDKs](/nexus/apis-and-sdks).
