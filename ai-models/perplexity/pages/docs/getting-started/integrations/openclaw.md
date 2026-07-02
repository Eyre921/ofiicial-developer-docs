---
title: "Perplexity with OpenClaw"
source: https://docs.perplexity.ai/docs/getting-started/integrations/openclaw
path: docs/getting-started/integrations/openclaw
---

Use Perplexity as an LLM provider and web search provider in OpenClaw.

## Overview

<u>[OpenClaw](https://openclaw.ai)</u> is an open-source AI agent that runs in your terminal and connects to multiple LLM providers, featuring support for Perplexity as a web search provider for real-time information retrieval.

You can configure OpenClaw to use Perplexity's Agent API models as your agent, and the Perplexity Search API for web search tool calls. This allows you to leverage Perplexity's powerful models and up-to-date search results directly within OpenClaw's agent framework.

<Card title="Get a Perplexity API Key" icon="key" href="https://console.perplexity.ai">
  Navigate to the API Console and generate a new key to use with OpenClaw.
</Card>

***

## Search API Setup (Use Perplexity as your Web Search Provider)

Use Perplexity Search API as OpenClaw's web search backend for real-time information retrieval.

<Steps>
  <Step title="Configure the Search Provider">
    <Tabs>
      <Tab title="Interactive CLI (Recommended)">
        The quickest way — no file editing required:

        ```bash theme={null}
        openclaw configure --section web
        ```

        Select **Perplexity** when prompted for a search provider, then paste your API key.
      </Tab>

      <Tab title="Config File (JSON)">
        Edit your `openclaw.json` (run `openclaw config file` to locate it):

        ```json theme={null}
        {
          "plugins": {
            "entries": {
              "perplexity": {
                "config": {
                  "webSearch": {
                    "apiKey": "pplx-..."
                  }
                }
              }
            }
          },
          "tools": {
            "web": {
              "search": {
                "provider": "perplexity"
              }
            }
          }
        }
        ```
      </Tab>

      <Tab title="Environment Variable">
        Set the environment variable and OpenClaw will auto-detect it:

        <Tabs>
          <Tab title="macOS / Linux">
            ```bash theme={null}
            export PERPLEXITY_API_KEY="pplx-..."
            ```
          </Tab>

          <Tab title="Windows (PowerShell)">
            ```powershell theme={null}
            setx PERPLEXITY_API_KEY="pplx-..."
            ```
          </Tab>
        </Tabs>

        Or set `PERPLEXITY_API_KEY` in `~/.openclaw/.env` for daemon installs.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Start using OpenClaw with Perplexity Search">
    Start OpenClaw and ask anything that requires web search:

    ```
    openclaw
    > What are the latest developments in quantum computing?
    ```

    OpenClaw will use Perplexity Search API to retrieve structured results and incorporate them into its response.
  </Step>
</Steps>

### Search Tool Parameters

When OpenClaw invokes `web_search` with Perplexity as the provider, these parameters are available:

| Parameter             | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `query`               | Search query (required)                                |
| `count`               | Number of results (1–10, default: 5)                   |
| `country`             | ISO 3166-1 alpha-2 country code (e.g., `US`, `DE`)     |
| `language`            | ISO 639-1 language code (e.g., `en`, `fr`)             |
| `freshness`           | Time filter: `day`, `week`, `month`, or `year`         |
| `date_after`          | Results published after this date (`YYYY-MM-DD`)       |
| `date_before`         | Results published before this date (`YYYY-MM-DD`)      |
| `domain_filter`       | Domain allowlist or denylist (max 20 entries)          |
| `max_tokens`          | Total content budget (default: 25,000, max: 1,000,000) |
| `max_tokens_per_page` | Per-page token limit (default: 2,048)                  |

<Tip>
  Domain filters support allowlists (`["nature.com", "science.org"]`) and denylists (`["-reddit.com", "-pinterest.com"]`), but you cannot mix both in the same request. See the [domain filter guide](/docs/search/filters/domain-filter) for details.
</Tip>

***

## Agent API Setup (Use Perplexity as your LLM Provider)

Use Perplexity's Agent API to run models like Claude Sonnet, GPT-5, Gemini, and Sonar as your OpenClaw coding agent.

<Steps>
  <Step title="Get Your API Key">
    <Card title="Generate API Key" icon="key" href="https://console.perplexity.ai">
      Navigate to the API Console and generate a new key.
    </Card>
  </Step>

  <Step title="Install OpenClaw">
    If you haven't installed OpenClaw yet:

    <Tabs>
      <Tab title="macOS / Linux">
        ```bash theme={null}
        curl -fsSL https://openclaw.ai/install.sh | bash
        ```
      </Tab>

      <Tab title="Windows (PowerShell)">
        ```powershell theme={null}
        iwr -useb https://openclaw.ai/install.ps1 | iex
        ```
      </Tab>
    </Tabs>

    For Docker, Podman, Nix, or other installation methods, see the [OpenClaw install documentation](https://docs.openclaw.ai/install).
  </Step>

  <Step title="Configure Perplexity as an LLM Provider">
    <Tabs>
      <Tab title="Onboarding CLI (Recommended)">
        The quickest way — no file editing required:

        ```bash theme={null}
        openclaw onboard \
          --auth-choice custom-api-key \
          --custom-base-url "https://api.perplexity.ai/v1" \
          --custom-api-key "pplx-YOUR_KEY_HERE" \
          --custom-model-id "anthropic/claude-sonnet-4-6" \ 
          --custom-compatibility openai \
          --custom-provider-id perplexity \
          --install-daemon
        ```

        This registers Perplexity as a provider with one model. To add more models, re-run with a different `--custom-model-id` or switch to the config file method.

        You can replace `anthropic/claude-sonnet-4-6` with any model ID from the [Agent API models list](/docs/agent-api/models) to change your default model.
      </Tab>

      <Tab title="Config File (All Models)">
        Edit your `openclaw.json` (run `openclaw config file` to locate it):

        ```json theme={null}
        {
        "agents": {
          "defaults": {
            "model": {
              "primary": "perplexity/anthropic/claude-sonnet-4-6" // Set your default model here
            }
          }
        },
        "models": {
          "mode": "merge",
          "providers": {
            "perplexity": {
              "baseUrl": "https://api.perplexity.ai/v1",
              "apiKey": "pplx-YOUR_KEY_HERE",
              "api": "openai-responses",
              "models": [
                {
                  "id": "perplexity/sonar",
                  "name": "Sonar (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0.25, "output": 2.50, "cacheRead": 0.0625, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                },
                {
                  "id": "anthropic/claude-opus-4-7",
                  "name": "Claude Opus 4.7 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 5.00, "output": 25.00, "cacheRead": 0.50, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "anthropic/claude-opus-4-5",
                  "name": "Claude Opus 4.5 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 5.00, "output": 25.00, "cacheRead": 0.50, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "anthropic/claude-sonnet-4-6",
                  "name": "Claude Sonnet 4.6 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 3.00, "output": 15.00, "cacheRead": 0.30, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "anthropic/claude-sonnet-4-5",
                  "name": "Claude Sonnet 4.5 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 3.00, "output": 15.00, "cacheRead": 0.30, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "anthropic/claude-haiku-4-5",
                  "name": "Claude Haiku 4.5 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 1.00, "output": 5.00, "cacheRead": 0.10, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "openai/gpt-5.4",
                  "name": "GPT-5.4 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                },
                {
                  "id": "openai/gpt-5.2",
                  "name": "GPT-5.2 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 1.75, "output": 14.00, "cacheRead": 0.175, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                },
                {
                  "id": "openai/gpt-5.1",
                  "name": "GPT-5.1 (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 1.25, "output": 10.00, "cacheRead": 0.125, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                },
                {
                  "id": "openai/gpt-5-mini",
                  "name": "GPT-5 Mini (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0.25, "output": 2.00, "cacheRead": 0.025, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                },
                {
                  "id": "google/gemini-3.1-pro-preview",
                  "name": "Gemini 3.1 Pro (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 2.00, "output": 12.00, "cacheRead": 0.20, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "google/gemini-3-flash-preview",
                  "name": "Gemini 3 Flash (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0.50, "output": 3.00, "cacheRead": 0.05, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "google/gemini-2.5-pro",
                  "name": "Gemini 2.5 Pro (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 1.25, "output": 10.00, "cacheRead": 0.125, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "google/gemini-2.5-flash",
                  "name": "Gemini 2.5 Flash (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0.30, "output": 2.50, "cacheRead": 0.03, "cacheWrite": 0 },
                  "contextWindow": 200000,
                  "maxTokens": 16384
                },
                {
                  "id": "nvidia/nemotron-3-super-120b-a12b",
                  "name": "Nemotron 3 Super (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                },
                {
                  "id": "xai/grok-4-1-fast-non-reasoning",
                  "name": "Grok 4.1 Fast (Perplexity)",
                  "api": "openai-responses",
                  "reasoning": false,
                  "input": ["text"],
                  "cost": { "input": 0.20, "output": 0.50, "cacheRead": 0.05, "cacheWrite": 0 },
                  "contextWindow": 128000,
                  "maxTokens": 16384
                }
              ]
            }
          }
        }
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Start using OpenClaw">
    Launch OpenClaw and your agent will use Perplexity:

    ```bash theme={null}
    openclaw
    ```
  </Step>
</Steps>

### Agent API Configuration Tips

<AccordionGroup>
  <Accordion title="API transport must be openai-responses">
    Perplexity's Agent API uses the [OpenAI Responses format](/docs/agent-api/openai-compatibility). In `openclaw.json`, set the `api` field to `"openai-responses"` at both the provider level and each model entry.

    Using `"openai-completions"` will not work.
  </Accordion>

  <Accordion title="Base URL must be exactly https://api.perplexity.ai/v1">
    Do **not** include `/agent` or `/responses` in the URL. OpenClaw appends `/responses` automatically.

    Wrong base URLs will cause authentication errors or 404s.

    | Correct                        | Wrong                                       |
    | ------------------------------ | ------------------------------------------- |
    | `https://api.perplexity.ai/v1` | `https://api.perplexity.ai/v1/agent`        |
    |                                | `https://api.perplexity.ai/v1/responses`    |
    |                                | `https://api.perplexity.ai` (missing `/v1`) |
  </Accordion>

  <Accordion title="Model ID format">
    In the config, model IDs under a provider block omit the provider prefix. The full model reference adds it:

    * Config model ID: `anthropic/claude-sonnet-4-6`
    * Full model reference: `perplexity/anthropic/claude-sonnet-4-6`
  </Accordion>
</AccordionGroup>

<Tip>
  For the latest model list and pricing, see the [Agent API models page](/docs/agent-api/models) and [pricing page](/docs/getting-started/pricing).
</Tip>

***

## Links & Resources

<CardGroup>
  <Card title="Agent API Quickstart" icon="robot" href="/docs/agent-api/quickstart">
    Use third-party models with built-in tools and function calling
  </Card>

  <Card title="Agent API Models" icon="list" href="/docs/agent-api/models">
    Full list of available models and pricing
  </Card>

  <Card title="Search API Quickstart" icon="search" href="/docs/search/quickstart">
    Full Perplexity Search API documentation
  </Card>

  <Card title="OpenAI Compatibility" icon="plug" href="/docs/agent-api/openai-compatibility">
    How the Agent API works with OpenAI-compatible clients
  </Card>

  <Card title="OpenClaw Documentation" icon="book" href="https://docs.openclaw.ai">
    OpenClaw's official documentation
  </Card>

  <Card title="API Console" icon="key" href="https://console.perplexity.ai">
    Generate and manage your API keys
  </Card>
</CardGroup>
