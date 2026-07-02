---
title: "Perplexity with Pipedream"
source: https://docs.perplexity.ai/docs/getting-started/integrations/pipedream
path: docs/getting-started/integrations/pipedream
---

Wire Perplexity into Pipedream workflows alongside 3,000+ other apps — automate research, summarization, and grounded responses with code and no-code steps.

## Overview

[Pipedream](https://pipedream.com) is a workflow automation platform with 3,000+ pre-built app integrations. The Perplexity app lets you authenticate once and then call Perplexity's chat completions and search endpoints from any Pipedream workflow — whether triggered by an email, a webhook, an RSS feed, a Slack message, a Google Sheets update, or a schedule.

<Info>
  **Pipedream** supports both no-code visual steps and full-code Node.js / Python steps in the same workflow. Learn more at [pipedream.com](https://pipedream.com).
</Info>

## Authentication

<Steps>
  <Step title="Get your API key">
    Generate a Perplexity API key from the [API portal](https://www.perplexity.ai/account/api/keys).
  </Step>

  <Step title="Connect Perplexity in Pipedream">
    In Pipedream, open any workflow and add the **Perplexity** app to a step. Click **Connect new account** and paste your API key. Pipedream stores it securely and references it via `$auth.api_key` in all future steps.
  </Step>
</Steps>

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Built-in Action: Chat Completions

The Perplexity app ships a **Chat Completions** action that generates a model response for a chat conversation with full Perplexity search controls — no code required.

* **Endpoint**: `POST /v1/chat/completions`
* **Inputs**: model, messages, search recency, domain filter, etc.
* **Output**: full chat completion response including `choices[0].message.content` and `citations`.

Add it from the step picker by searching **Perplexity → Chat Completions**.

## Custom Code Step

For full control — async chat completions, embeddings, or the Agent API — use a Pipedream **Node.js code step** that references your saved Perplexity connection:

```javascript theme={null}
import { axios } from "@pipedream/platform";

export default defineComponent({
  props: {
    perplexity: {
      type: "app",
      app: "perplexity",
    },
  },
  async run({ steps, $ }) {
    return await axios($, {
      method: "POST",
      url: "https://api.perplexity.ai/v1/chat/completions",
      headers: {
        Authorization: `Bearer ${this.perplexity.$auth.api_key}`,
        "Content-Type": "application/json",
        "X-Pplx-Integration": "pipedream/1.0",
      },
      data: {
        model: "sonar-pro",
        messages: [
          { role: "user", content: "Summarize this week's AI research." },
        ],
      },
    });
  },
});
```

You can swap the URL to call any [Perplexity API endpoint](/api-reference):

* `/v1/chat/completions` — Sonar chat completions
* `/v1/agent` — Agent API with third-party models and presets
* `/search` — raw ranked web results
* `/v1/embeddings` — vector embeddings
* `/v1/async/chat/completions` — async chat completions

## Example Workflows

Common Perplexity-on-Pipedream patterns:

* **Customer support automation** — incoming email triggers a Perplexity Chat Completions step that drafts a response, then logs the conversation in a CRM.
* **News-feed summarization** — new article from an RSS trigger is summarized by Perplexity and posted to a Slack channel with citations.
* **Brand monitoring** — social media mentions are piped through Perplexity for sentiment analysis and entity extraction, then written to a Google Sheet.
* **Daily research digest** — a scheduled cron triggers a Perplexity query, and the result is emailed or posted to a chat channel every morning.

## Security & Credentials

Pipedream stores your Perplexity API key encrypted at rest and injects it into every step via the `$auth` object — your key never appears in step UI or logs. You can rotate the key at any time from your account's **Connected Accounts** page.

## Links & Resources

<CardGroup>
  <Card title="Pipedream Perplexity App" icon="plug" href="https://pipedream.com/apps/perplexity">
    Official Perplexity app on Pipedream.
  </Card>

  <Card title="Pipedream Docs" icon="book" href="https://pipedream.com/docs">
    Full Pipedream documentation.
  </Card>

  <Card title="Perplexity API Reference" icon="code" href="/api-reference">
    Full Perplexity API reference.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Sonar models.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [Pipedream documentation](https://pipedream.com/docs)
* Review our [FAQ](/docs/resources/faq)
