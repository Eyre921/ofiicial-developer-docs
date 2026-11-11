---
title: "Send your first request"
source: https://langfuse.com/docs/gateway/get-started/first-request.md
path: docs/gateway/get-started/first-request
---

---
title: Send your first request
seoTitle: "Send your first request through the Langfuse AI Gateway (beta)"
description: Create a personal gateway API key, connect your coding agent, SDK, or app to the Langfuse AI Gateway, and see your first trace.
---

# Send your first request

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

This page walks you through how to send your first request through the Gateway. If the gateway is not set up for your organization yet, ask an admin to follow [Set up the gateway](/docs/gateway/get-started/admin-setup) first.

## Setup steps [#setup-steps]

<Steps>

### Create a gateway API key [#create-a-key]

Go to **AI Gateway → Gateway keys** and select **Create key**.

Export the key and your region's gateway host in your shell. The setup for each client in the next steps uses these variables.

```sh
export LANGFUSE_GATEWAY_KEY="<your-gateway-key>"
# 🇪🇺 EU region
export LANGFUSE_GATEWAY_HOST="https://gateway.cloud.langfuse.com"
# 🇺🇸 US region: https://gateway.us.cloud.langfuse.com
# 🇯🇵 Japan region: https://gateway.jp.cloud.langfuse.com
# ⚕️ HIPAA region: https://gateway.hipaa.cloud.langfuse.com
# Self-hosted: the gateway URL of your deployment
```

  You need the AI Gateway, Member, Admin, or Owner organization role. Viewers
  can't create gateway keys. See [roles and
  permissions](/docs/administration/rbac).

  For CI or a shared service, ask an admin for a service account key. See [API
  keys](/docs/gateway/features/api-keys).

### Pick a model [#list-models]

Pick a model you can call. Its ID has the form `<connection>:<model>`, for example `openai-prod:<model>`. See [model IDs](/docs/gateway/features/models#model-ids) for which form to send.

**Langfuse UI**

Go to **AI Gateway → Providers & Models → Models** and choose a provider connection in the filter. The list shows each model's name without the connection prefix, the routes it supports, and whether it's enabled. Add the connection's name as the prefix when you call a model.

  ![Providers & Models page on the Models tab, filtered to one provider connection, listing model names with a copy button, their supported routes, and an Enabled switch per model](/images/docs/ai-gateway/models-list.png)

  If the page says "No providers yet", your organization hasn't added a
  provider connection yet. Ask your admin.

**API**

Call the gateway's models endpoints. A model list also confirms that your key works.

```sh
curl -s "$LANGFUSE_GATEWAY_HOST/openai/v1/models" \
  -H "Authorization: Bearer $LANGFUSE_GATEWAY_KEY" | head -c 300

curl -s "$LANGFUSE_GATEWAY_HOST/anthropic/v1/models?limit=1000" \
  -H "x-api-key: $LANGFUSE_GATEWAY_KEY" \
  -H "anthropic-version: 2023-06-01" | head -c 300
```

### Connect your coding agent or app [#send-a-request]

**Claude Code**

_**Requires** Claude Code 2.1 or later and an `ANTHROPIC` provider connection._

Log out of any Claude subscription, point Claude Code at the gateway's Anthropic route, and run a prompt:

```sh
claude /logout
export ANTHROPIC_BASE_URL="$LANGFUSE_GATEWAY_HOST/anthropic"   # no /v1: Claude Code appends /v1/messages
export ANTHROPIC_AUTH_TOKEN="$LANGFUSE_GATEWAY_KEY"            # sent as Authorization: Bearer
unset ANTHROPIC_API_KEY                                       # a different value here causes a 401
claude -p "Reply with: hello gateway"
```

- [Full Claude Code guide](/integrations/developer-tools/claude-code-gateway#claude-code-cli)

**Claude Desktop**

_**Requires** an `ANTHROPIC` provider connection._

1. Open **Developer → Configure Third-Party Inference**. If the **Developer** menu is unavailable, open **Help → Troubleshooting** and enable Developer Mode.
2. Under **Connection**, set **Inference provider** to **Gateway** and **Gateway base URL** to `https://gateway.cloud.langfuse.com/anthropic`, without `/v1`. Set **Credential kind** to **Static API key**, enter your gateway key under **Gateway API key**, and select **Bearer** as the **Gateway auth scheme**.
3. Under **Capabilities → General restrictions**, add `*` to **Allowed egress hosts**. Otherwise, Claude can't reach services outside the gateway, such as GitHub.
4. Select **Apply Changes**, then **Save & Restart**, and send a message in a new session.

_This example uses the EU host. If your organization is in another region, use your region's [gateway host](/docs/gateway/features/rest-api#gateway-hosts)._

- [Full Claude Desktop guide](/integrations/developer-tools/claude-code-gateway#claude-desktop)

**Codex**

_**Requires** Codex CLI 0.157 or later and an `OPENAI` provider connection._

Export the gateway key:

```sh
 export LANGFUSE_GATEWAY_KEY="<your-gateway-key>"
```

Add this to `~/.codex/config.toml` (`$CODEX_HOME/config.toml` if you set `CODEX_HOME`). Put `model` and `model_provider` next to your other top-level keys, before any `[table]` section, and the `[model_providers.langfuse]` table after them:

```toml filename="~/.codex/config.toml"
model = "<model-id>"               # an OpenAI model ID
model_provider = "langfuse"

[model_providers.langfuse]
name = "Langfuse AI Gateway"
base_url = "https://gateway.cloud.langfuse.com/openai/v1"
env_key = "LANGFUSE_GATEWAY_KEY"   # sent as Authorization: Bearer
wire_api = "responses"
```

_This example uses the EU host. If your organization is in another region, use your region's [gateway host](/docs/gateway/features/rest-api#gateway-hosts)._

Then run a prompt:

```sh
codex exec "Reply with exactly: PONG"
```

- [Full Codex guide](/integrations/developer-tools/codex-gateway)

**OpenCode**

_**Requires** OpenCode 2.0 or later and an `ANTHROPIC` provider connection._

Point OpenCode's Anthropic provider at the gateway in `opencode.json` (project root or `~/.config/opencode/opencode.json`). Remove any stored OpenCode account connection first, otherwise OpenCode keeps using it.

```json filename="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/<model-id>",
  "small_model": "anthropic/<small-model-id>",
  "providers": {
    "anthropic": {
      "settings": {
        "baseURL": "https://gateway.cloud.langfuse.com/anthropic/v1",
        "apiKey": "{env:LANGFUSE_GATEWAY_KEY}"
      }
    }
  }
}
```

_This example uses the EU host. If your organization is in another region, use your region's [gateway host](/docs/gateway/features/rest-api#gateway-hosts)._

Then run a prompt:

```sh
opencode run "Reply with exactly: pong"
```

- [Full OpenCode guide](/integrations/developer-tools/opencode-gateway)

**Pi**

_**Requires** Pi 1.5.0 or later and an `ANTHROPIC` provider connection._

Install Pi:

```sh
npm install -g @earendil-works/pi-coding-agent
```

Add the gateway's Anthropic route as a provider in `~/.pi/agent/models.json`. Set the model values to those of the model you picked:

```json filename="~/.pi/agent/models.json"
{
  "providers": {
    "langfuse-anthropic": {
      "baseUrl": "https://gateway.cloud.langfuse.com/anthropic",
      "api": "anthropic-messages",
      "apiKey": "$LANGFUSE_GATEWAY_KEY",
      "compat": { "sendSessionAffinityHeaders": true },
      "models": [
        {
          "id": "<anthropic-model-id>",
          "reasoning": true,
          "input": ["text", "image"],
          "contextWindow": 200000,
          "maxTokens": 64000
        }
      ]
    }
  }
}
```

_This example uses the EU host. If your organization is in another region, use your region's [gateway host](/docs/gateway/features/rest-api#gateway-hosts)._

Then run a prompt:

```sh
pi -p --provider langfuse-anthropic --model <anthropic-model-id> "Reply with exactly: pong"
```

- [Full Pi guide](/integrations/developer-tools/pi-agent-gateway)

**GitHub Copilot**

_**Requires** an `ANTHROPIC` provider connection._

Point Copilot CLI at the gateway's Anthropic route and start it:

```sh
export COPILOT_PROVIDER_BASE_URL="$LANGFUSE_GATEWAY_HOST/anthropic"
export COPILOT_PROVIDER_TYPE="anthropic"
export COPILOT_PROVIDER_API_KEY="$LANGFUSE_GATEWAY_KEY"
export COPILOT_MODEL="<model-id>"   # an Anthropic model ID
copilot
```

Send a prompt in `copilot`. If `~/.copilot/providers.json` already lists providers or models, it takes precedence and these variables have no effect. For the OpenAI route and the GitHub Copilot app, see the full guide.

- [Full GitHub Copilot guide](/integrations/developer-tools/github-copilot-gateway)

**OpenAI SDK**

Set the base URL to the gateway's OpenAI route and pass the gateway key as the API key.

Python:

```bash
pip install openai
```

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.environ["LANGFUSE_GATEWAY_HOST"] + "/openai/v1",
    api_key=os.environ["LANGFUSE_GATEWAY_KEY"],
)

response = client.responses.create(model="<model-id>", input="Say hello")
print(response.output_text)
```

TypeScript:

```bash
npm install openai
```

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/openai/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});

const response = await client.responses.create({
  model: "<model-id>",
  input: "Say hello",
});
console.log(response.output_text);
```

- [Full OpenAI SDK guide](/integrations/model-providers/openai-gateway)

**Anthropic SDK**

Set the base URL to the gateway's Anthropic route, without `/v1`, and pass the gateway key as the API key.

Python:

```bash
pip install anthropic
```

```python
import os

from anthropic import Anthropic

client = Anthropic(
    base_url=os.environ["LANGFUSE_GATEWAY_HOST"] + "/anthropic",
    api_key=os.environ["LANGFUSE_GATEWAY_KEY"],
)

message = client.messages.create(
    model="<model-id>",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello"}],
)
print(message.content[0].text)
```

TypeScript:

```bash
npm install @anthropic-ai/sdk
```

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/anthropic`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});

const message = await client.messages.create({
  model: "<model-id>",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Say hello" }],
});
console.log(message.content);
```

- [Full Anthropic SDK guide](/integrations/model-providers/anthropic-gateway)

**Vercel AI SDK**

Point the AI SDK's OpenAI provider at the gateway's OpenAI route:

```bash
npm install ai @ai-sdk/openai
```

```ts
import { createOpenAI } from "@ai-sdk/openai";
import { generateText } from "ai";

const openai = createOpenAI({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/openai/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});

const { text } = await generateText({
  model: openai("<model-id>"),
  prompt: "Say hello",
});
console.log(text);
```

For Anthropic models, see the full guide.

- [Full Vercel AI SDK guide](/integrations/frameworks/vercel-ai-sdk-gateway)

**REST API**

Call a model with the OpenAI Chat Completions API:

```sh
curl -si "$LANGFUSE_GATEWAY_HOST/openai/v1/chat/completions" \
  -H "Authorization: Bearer $LANGFUSE_GATEWAY_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"<model-id>","messages":[{"role":"user","content":"Say hello"}]}'
```

The response is OpenAI's own response. Its headers include `langfuse-trace-id`, the ID of the trace the gateway recorded.

- [REST API](/docs/gateway/features/rest-api)

Replace `<model-id>` with the model ID you picked in the previous step.

### See your trace in Langfuse (optional) [#view-the-trace]

Open the organization's ingestion project in Langfuse and go to **Tracing** to see your request. What's recorded depends on the organization's [ingestion mode](/docs/gateway/features/tracing#ingestion-modes).

  You need Viewer access or above to the ingestion project to see gateway
  traces. If you can't open it, ask an admin to add you.

</Steps>

## Not seeing what you expected? [#not-seeing-what-you-expected]

For error codes, see [Troubleshooting](/faq/all/ai-gateway-error-codes). Quote the `langfuse-request-id` response header when you report a problem.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/gateway/get-started/first-request.md`.

### Querying these docs

If the answer is not on this page, query the documentation instead of guessing:

- **Semantic search** across all Langfuse docs, returning an answer with the relevant pages and excerpts. Ask a specific, self-contained question:

  ```bash
  curl -sG "https://langfuse.com/api/search-docs" --data-urlencode "query=How do I trace a LangGraph agent?"
  ```

- **Index of every page**: <https://langfuse.com/llms.txt>, with per-section indexes [llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), and [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt).

### Before writing Langfuse code

- **Install the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill).** It encodes Langfuse's own best practices for instrumentation, prompt management, and evaluation, and materially improves results.
- **Read [What does a good trace look like?](https://langfuse.com/docs/observability/best-practices.md)** before instrumenting an application.
- **Verify endpoints, parameters, and response fields** against the [API reference](https://api.reference.langfuse.com) instead of inferring them from code examples.
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx @langfuse/cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

