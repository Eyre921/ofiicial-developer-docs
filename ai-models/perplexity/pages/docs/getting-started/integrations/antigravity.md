---
title: "Perplexity with Google Antigravity"
source: https://docs.perplexity.ai/docs/getting-started/integrations/antigravity
path: docs/getting-started/integrations/antigravity
---

Call Perplexity's Agent API from applications you build or edit inside Google Antigravity.

## Overview

[Google Antigravity](https://antigravity.google) is an agent-first development environment where AI agents plan, write, and iterate on your code across editor, terminal, and browser surfaces. While Antigravity ships with its own built-in agent models, the code your agents author can call any external API — including Perplexity's [Agent API](/docs/agent-api/quickstart) and [Search API](/docs/search/quickstart) — for real-time web research, citations, and grounded answers.

This guide shows how to add the Perplexity Agent API to a project you're building inside Antigravity, using the OpenAI Responses‑compatible interface.

<Info>
  **Scope of this guide.** Antigravity does not currently expose a BYOK or custom-provider hook for swapping its built-in agent model with Perplexity. This guide covers the supported path: calling Perplexity from your **application code** authored inside Antigravity (web apps, CLIs, coding assistants, internal tools, etc.). If Antigravity adds a custom-provider configuration in the future, the same base URL and API key documented here will apply.
</Info>

<Card title="Get a Perplexity API Key" icon="key" href="https://console.perplexity.ai">
  Generate an API key in the Perplexity API Console, then store it in your project as `PERPLEXITY_API_KEY`.
</Card>

***

## When to Use This

The Agent API is a strong fit when your Antigravity-built project needs grounded, web-aware answers without you having to wire up search, scraping, and citation handling yourself. Common patterns:

* **AI features in web or mobile apps** — drop a research or Q\&A surface into a product without standing up your own retrieval stack.
* **Coding assistants and dev tools** — let agents fetch up-to-date library docs, error explanations, or changelogs at runtime.
* **Internal tools and dashboards** — answer questions over the live web (market data, competitive moves, news) with sources attached.
* **CLIs and scripts** — quick research utilities you run from the Antigravity terminal.

***

## Setup

<Steps>
  <Step title="Store Your API Key as an Environment Variable">
    In the Antigravity terminal (or your project's `.env` file), set:

    <Tabs>
      <Tab title="macOS / Linux">
        ```bash theme={null}
        export PERPLEXITY_API_KEY="pplx-..."
        ```
      </Tab>

      <Tab title="Windows (PowerShell)">
        ```powershell theme={null}
        setx PERPLEXITY_API_KEY "pplx-..."
        ```
      </Tab>

      <Tab title=".env file">
        ```bash theme={null}
        PERPLEXITY_API_KEY=pplx-...
        ```
      </Tab>
    </Tabs>

    Never hardcode the key in source files — Antigravity agents may commit or share code they read, so treating the key as an environment variable keeps it out of the repo.
  </Step>

  <Step title="Install an SDK">
    The Agent API is compatible with the [OpenAI Responses API](/docs/agent-api/openai-compatibility), so the OpenAI SDK works directly. The native Perplexity SDK is also available and provides cleaner preset syntax.

    <Tabs>
      <Tab title="TypeScript / Node">
        ```bash theme={null}
        npm install openai
        ```
      </Tab>

      <Tab title="Python">
        ```bash theme={null}
        pip install openai
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Point the Client at Perplexity">
    Set the base URL to `https://api.perplexity.ai/v1` and read the API key from the environment.

    <Tabs>
      <Tab title="TypeScript / Node">
        ```typescript theme={null}
        import OpenAI from "openai";

        const client = new OpenAI({
          apiKey: process.env.PERPLEXITY_API_KEY,
          baseURL: "https://api.perplexity.ai/v1",
        });

        const response = await client.responses.create({
          input: "Summarize the top three AI infrastructure announcements this week with sources.",
          preset: "pro-search",
        } as any);

        console.log(response.output_text);
        ```
      </Tab>

      <Tab title="Python">
        ```python theme={null}
        import os
        from openai import OpenAI

        client = OpenAI(
            api_key=os.environ.get("PERPLEXITY_API_KEY"),
            base_url="https://api.perplexity.ai/v1",
        )

        response = client.responses.create(
            input="Summarize the top three AI infrastructure announcements this week with sources.",
            extra_body={"preset": "pro-search"},
        )

        print(response.output_text)
        ```
      </Tab>
    </Tabs>

    The OpenAI SDK sends `client.responses.create(...)` to `POST /v1/responses`, which Perplexity accepts as an alias for the canonical `POST /v1/agent` endpoint. No other configuration is required.
  </Step>
</Steps>

***

## Using It from Inside Antigravity

Once the client is wired up, you can prompt Antigravity's agent to use the Perplexity client wherever your app needs grounded answers. A few prompts that work well:

* *"Add a `/research` endpoint that takes a `query` string and returns the Perplexity Agent API response with citations."*
* *"Wrap the Perplexity call in a `researchTopic(topic: string)` helper and call it from the dashboard's news widget."*
* *"Write a CLI subcommand `pplx ask` that streams a Perplexity Agent API response to stdout."*

Because the SDK is the standard OpenAI client, Antigravity's agent will already know the call shape — you mainly need to make sure it uses the right `baseURL` and reads `PERPLEXITY_API_KEY` from the environment.

<Tip>
  If Antigravity's agent generates code that points at `https://api.openai.com/v1` or omits the `baseURL` entirely, ask it to "use the Perplexity base URL `https://api.perplexity.ai/v1`" — it will regenerate the client with the correct endpoint.
</Tip>

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Base URL Must Be Exactly https://api.perplexity.ai/v1">
    The OpenAI SDK appends `/responses` to the base URL on its own. Do **not** include `/agent` or `/responses` in the base URL, and do not omit `/v1`.

    | Correct                        | Wrong                                       |
    | ------------------------------ | ------------------------------------------- |
    | `https://api.perplexity.ai/v1` | `https://api.perplexity.ai/v1/agent`        |
    |                                | `https://api.perplexity.ai/v1/responses`    |
    |                                | `https://api.perplexity.ai` (missing `/v1`) |

    Wrong base URLs typically surface as 404s or authentication errors.
  </Accordion>

  <Accordion title="Can I Replace Antigravity's Built-In Agent Model with Perplexity?">
    Not today. Antigravity does not expose a custom-provider or BYOK setting that would let you route its in-editor agent through Perplexity. Use this guide's pattern — calling the Perplexity Agent API from your application code — instead.

    If Antigravity adds custom-provider support in the future, the configuration will be: base URL `https://api.perplexity.ai/v1`, API key from `PERPLEXITY_API_KEY`, and an OpenAI Responses‑compatible transport.
  </Accordion>

  <Accordion title="API Key Isn't Being Picked Up">
    Antigravity terminal sessions inherit environment variables from where Antigravity was launched. If `echo $PERPLEXITY_API_KEY` is empty in the integrated terminal, either set it in your shell profile (`~/.zshrc`, `~/.bashrc`) and relaunch Antigravity, or load it from a project-local `.env` file using something like `dotenv`.
  </Accordion>

  <Accordion title="Choosing a Model vs. a Preset">
    Presets like `pro-search` are pre-configured for common research workloads and are the easiest starting point. If you need a specific third-party model (Claude, GPT, Gemini, etc.), pass `model="anthropic/claude-sonnet-4-6"` (or another value from the [Agent API models list](/docs/agent-api/models)) instead of `preset`.
  </Accordion>
</AccordionGroup>

***

## Links & Resources

<CardGroup>
  <Card title="Agent API Quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Build with the Agent API using OpenAI-compatible or native SDKs.
  </Card>

  <Card title="OpenAI Compatibility" icon="plug" href="/docs/agent-api/openai-compatibility">
    Full reference for using the OpenAI SDK against Perplexity.
  </Card>

  <Card title="Agent API Presets" icon="sparkles" href="/docs/agent-api/presets">
    Pre-configured setups like `pro-search` for common workloads.
  </Card>

  <Card title="Agent API Models" icon="brain" href="/docs/agent-api/models">
    Full list of third-party and Perplexity models available via the Agent API.
  </Card>

  <Card title="Perplexity SDK" icon="code" href="/docs/sdk/overview">
    Native SDK with cleaner preset syntax and full type safety.
  </Card>

  <Card title="API Console" icon="key" href="https://console.perplexity.ai">
    Generate and manage your Perplexity API keys.
  </Card>
</CardGroup>
