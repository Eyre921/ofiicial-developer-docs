---
title: "FireRouter Setup"
source: https://docs.fireworks.ai/nexus/firerouter/setup
path: nexus/firerouter/setup
---

Set up FireRouter in a coding harness with FireConnect, in an LLM gateway such as LiteLLM or Portkey, or from the OpenAI, Anthropic, or Fireworks SDK.

Use the same model ID, `firerouter` or `auto`, from a coding harness, an LLM gateway, or your own code. Every path needs a Fireworks API key. To add Claude or GPT, also provide an Anthropic or OpenAI credential. See [Provide Anthropic and OpenAI credentials](/nexus/firerouter#provide-anthropic-and-openai-credentials).

| You are using | Setup |
| - | - |
| Claude Code, Codex, OpenCode, Cursor IDE, or another coding harness | [FireConnect](#fireconnect) |
| The ChatGPT desktop app or Claude Desktop | [Desktop apps](#desktop-apps) |
| LiteLLM, Portkey, or another LLM gateway | [LLM gateway](#llm-gateway) |
| Your own app, agent, or script | [API and SDK](#api-and-sdk) |

## Choose a model ID

| Model ID | What it routes across | Credentials |
| - | - | - |
| `firerouter` | Claude Opus or GPT Sol, [picked from your credentials and client](/nexus/firerouter#how-bare-firerouter-picks-its-closed-model), plus the Fireworks open-model mix | Fireworks key, plus an Anthropic or OpenAI credential |
| `auto` | Fireworks open models only | Fireworks API key |

* Use `firerouter` for most work.
* Without a closed-model credential, `firerouter` uses Fireworks open models only.
* To choose the models yourself, see [Pin specific models](/nexus/firerouter#pin-specific-models).

## FireConnect

Use FireRouter in any coding harness. [FireConnect](/nexus/fireconnect) writes the settings for you and restores them with `off`. Manual setup gives you the same settings to add yourself, with nothing to install.

### Set up your harness

Pick your harness, a router, and a setup method. Pick `firerouter` to route between Claude or GPT and Fireworks open models. Pick `auto` if you have only a Fireworks key. The commands and config files update as you choose, including the provider-key headers you need.

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
      Start a new session and open `/model`. Claude turns use your Claude login.
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

| Harness | FireConnect with Claude turns | FireConnect with GPT turns | Manual setup |
| - | - | - | - |
| Claude Code | Your Claude login, or an exported `ANTHROPIC_API_KEY` | `--openai-api-key`, or an OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| Codex CLI, ChatGPT desktop app | Anthropic Provider Key | Your Codex sign-in (a ChatGPT plan or an OpenAI key), or an OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| OpenCode, Pi, VS Code | `--anthropic-api-key`, or an Anthropic Provider Key | `--openai-api-key`, or an OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| Copilot CLI, DeepSeek Harness | Anthropic Provider Key | OpenAI Provider Key | Sends `x-anthropic-api-key` and `x-openai-api-key` |
| Cursor IDE, Copilot App | Anthropic Provider Key | OpenAI Provider Key | Provider Keys only; these apps cannot send extra headers |

* **Save a key once:** `fireconnect configure --anthropic-api-key sk-ant-...` or `fireconnect configure --openai-api-key sk-...`. Both are optional; FireConnect connects without them. `fireconnect configure --unset openai-api-key` or `--unset anthropic-api-key` clears a saved key from FireConnect and every harness.
* **Where a saved OpenAI key goes:** FireConnect sends it with `firerouter`, so FireRouter can pick GPT Sol.
* **Codex uses its own sign-in** for GPT turns, not a saved key. See [Codex](/nexus/harnesses#codex).
* **No key, no problem:** every harness above accepts `firerouter`. When no closed-model key reaches FireRouter, it uses Fireworks open models only.

For every harness's files and restore behavior, see [Coding Harnesses](/nexus/harnesses) and [Harness Compatibility](/nexus/harness-compatibility).

### Desktop apps

<Tabs>
  <Tab title="ChatGPT desktop app" icon="sparkles">
    The ChatGPT desktop app shares the Codex CLI's config, so one command sets up both. Quit the ChatGPT desktop app first:

    ```bash wrap theme={null}
    fireconnect chatgpt
    ```

    Reopen the app. FireRouter (`firerouter`) is the default model in its model list, and it routes between GPT Sol and Fireworks open models.

    * GPT turns use the app's own sign-in: your ChatGPT plan, or the OpenAI key you signed in with. See [Codex](/nexus/harnesses#codex) for the exceptions.
    * Sign-in billing is tested in the Codex CLI. The ChatGPT desktop app is not tested yet.
  </Tab>

  <Tab title="Claude Desktop" icon="desktop">
    FireConnect doesn't add FireRouter to Claude Desktop yet. On macOS, connect it with:

    ```bash wrap theme={null}
    fireconnect claude-desktop on
    ```

    Reopen Claude Desktop. The picker starts on `auto`, which routes across Fireworks open models, followed by the Fireworks models. See [Claude Desktop](/nexus/harnesses#claude-desktop).

    To route between Claude and open models, use FireRouter in [Claude Code](/nexus/harnesses#claude-code).
  </Tab>
</Tabs>

## LLM gateway

You do not need FireConnect behind a gateway. The gateway sends the `firerouter` model ID and your Fireworks API key to Fireworks. Clients and harnesses behind the gateway call `firerouter` with only their gateway key.

### Set up your gateway

Choose LiteLLM or Portkey, pick a model ID, and choose where the provider keys live. The widget writes the gateway config and a test request.

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
| `x-anthropic-api-key` | You want Claude and no Anthropic Provider Key is connected |
| `x-openai-api-key` | You want GPT and no OpenAI Provider Key is connected |

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

Pick an API and a language. The command updates with the provider header that API needs.

<FireRouterBuilder />

### Examples

Every example uses `firerouter`. The provider key you send picks the closed model:

* **Chat Completions and Responses** examples send an OpenAI key. FireRouter routes between GPT Sol and the Fireworks open-model mix.
* **Messages** examples send an Anthropic key. FireRouter routes between Claude Opus and the Fireworks open-model mix.

Send both keys, or connect [Provider Keys](/nexus/provider-keys) for both providers, and FireRouter picks by API. See [How bare `firerouter` picks its closed model](/nexus/firerouter#how-bare-firerouter-picks-its-closed-model).

#### Chat Completions

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.fireworks.ai/inference/v1/chat/completions \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "x-openai-api-key: $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "firerouter",
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
      model="firerouter",
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
    model: "firerouter",
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
      model="firerouter",
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
      "model": "firerouter",
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
      model="firerouter",
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
    model: "firerouter",
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
      "model": "firerouter",
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
      model="firerouter",
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
    model: "firerouter",
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
      model="firerouter",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Say pong in one word."}],
  )

  text = next(block.text for block in message.content if block.type == "text")
  print(message.model, text)
  ```
</CodeGroup>

The Anthropic SDK base URL is `https://api.fireworks.ai/inference`, without `/v1`. The SDK adds `/v1/messages`. Some models return a `thinking` block before the text, so read the first `text` block rather than `content[0]`.

### Check which model served the request

Each example prints the response `model` field. It names the model that served the turn, an open model or the closed model, not the router ID you sent. To confirm closed-model access, add `x-routing-preference: 1` so the route's primary model serves the turn. See [Verify routing](/nexus/firerouter#verify-routing).

For errors, limits, and more API details, see [APIs and SDKs](/nexus/apis-and-sdks).
