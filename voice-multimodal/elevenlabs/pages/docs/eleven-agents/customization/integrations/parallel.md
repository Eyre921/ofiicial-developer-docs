---
title: "Parallel"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/parallel.md
path: docs/eleven-agents/customization/integrations/parallel
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Parallel

## Overview

Connect your ElevenLabs AI agents with [Parallel](https://parallel.ai) to perform web searches during conversations. Your agents can search the web, retrieve relevant content with excerpts, and ground their responses with up-to-date information.

## Capabilities

| Capability                | Support                                    |
| ------------------------- | ------------------------------------------ |
| Zero retention mode (ZRM) | Not supported                              |
| Attachments in tools      | Not supported — tools operate on text only |

## Setup

This integration uses a **Parallel API key** for authentication.

#### Create a Parallel account

Sign up at [parallel.ai](https://parallel.ai) if you do not already have an account.

#### Get your API key

In the [Parallel Platform](https://platform.parallel.ai), go to **Settings > API Keys** and find the **App Keys** section. You can either copy the API key for the default app, or create a new app to track usage separately.

#### Connect in ElevenLabs

In the ElevenLabs integration setup, paste your Parallel API key in the **API Key** field.

## Search options

Each search is described by two parameters that the agent provides:

* **Objective** — a concise, self-contained description of the search goal, naming the key entity or topic along with any freshness or source requirements.
* **Search queries** — three short keyword queries (roughly three to six words each) that approach the objective from different angles. These are keyword phrases rather than full sentences or questions.

Searches run in Parallel's `fast` mode and return up to 10 results with excerpts.

## Useful links

* [Parallel API documentation](https://docs.parallel.ai)
* [Parallel Platform](https://platform.parallel.ai)
