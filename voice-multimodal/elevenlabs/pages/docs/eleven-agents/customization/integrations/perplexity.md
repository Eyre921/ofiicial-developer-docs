---
title: "Perplexity"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/perplexity.md
path: docs/eleven-agents/customization/integrations/perplexity
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Perplexity

## Overview

Connect your ElevenLabs AI agents with Perplexity to answer questions from the live web during conversations. Agents can ask a question and receive a short answer backed by cited sources, or search the web directly for pages and articles. Use this to ground responses in information that is newer than the agent's own knowledge.

## Setup

This integration uses a **Perplexity API key** for authentication.

#### Create a Perplexity account

Sign up at [perplexity.ai](https://www.perplexity.ai) if you do not already have an account.

#### Add a payment method

Perplexity bills API usage pay-as-you-go. Add a payment method in the [API console](https://console.perplexity.ai) before generating a key.

#### Generate an API key

Go to [console.perplexity.ai/project/keys](https://console.perplexity.ai/project/keys) and create a new key. It starts with `pplx-`.

#### Connect in ElevenLabs

In the ElevenLabs integration setup, paste your Perplexity API key in the **API Key** field.

## Tools

The integration exposes two tools. Which one the agent picks depends on whether the caller wants an answer or a list of sources.

| Tool     | What it returns                                      |
| -------- | ---------------------------------------------------- |
| `Ask`    | A short prose answer with the URLs it was drawn from |
| `Search` | Web pages with a title, link and short extract each  |

### Ask

Ask sends the question to Perplexity's Agent API, which searches the web and writes an answer. Responses are constrained to roughly three sentences of plain prose, sized to be read aloud, and the sources behind the answer are returned alongside it. Use it for questions such as "what happened with X this week", where the caller wants the answer spoken back to them.

### Search

Search queries Perplexity's Search API and returns the pages themselves, each with a title, link and short extract. The agent can restrict results to specific domains, or to a recency window of an hour, day, week, month or year. It returns three pages by default, short enough to read out during a call, and up to twenty when the caller asks for a particular number.

### Search modes

Search runs against the open web by default. The `search_type` parameter on the Search tool selects the mode, and you change it when configuring the tool:

| Mode     | Returns                                 |
| -------- | --------------------------------------- |
| `web`    | Web pages. The default.                 |
| `fast`   | Web pages, optimized for lower latency. |
| `people` | Profile information about individuals.  |

Your configuration fixes the mode for every call the agent makes. If you select `people`, edit the Search tool's **Condition prompt** to say it looks up individuals, so the agent calls it for the right questions.

## How answers are shortened

Both tools return deliberately small results, sized to what a caller can absorb in conversation. The integration defaults the number of pages returned to three, requests the shortest available page extracts, and instructs the answer model to stay within a few sentences. Each of these is a parameter on the tool, so raise them when configuring it if your agent needs fuller context.

## Useful links

* [Perplexity API documentation](https://docs.perplexity.ai)
* [Perplexity API console](https://console.perplexity.ai)
* [Agent API reference](https://docs.perplexity.ai/api-reference/agent-post)
* [Search API reference](https://docs.perplexity.ai/api-reference/search-post)
