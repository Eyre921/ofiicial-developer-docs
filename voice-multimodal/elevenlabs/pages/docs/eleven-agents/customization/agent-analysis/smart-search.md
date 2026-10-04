---
title: "Searching conversations"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/smart-search.md
path: docs/eleven-agents/customization/agent-analysis/smart-search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Searching conversations

## Overview

Conversation history includes a search bar with two modes for finding messages across all your agent conversations.

Keyword search performs full-text matching and supports the same filters as the conversation list (time range, duration, ratings, tools, languages, and more). Smart search uses semantic search to match transcript chunks by meaning — useful when you don't know the exact phrasing a caller used.

![Conversation history search field with the search mode menu
open](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5a8ee4f43638200e84fc77961ee4388ea3a32314c03a7e74ffaba6acf695ee68/assets/images/conversational-ai/smart-search-conversation-history.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261004%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261004T233208Z&X-Amz-Expires=604800&X-Amz-Signature=f347bde4a567c16ba230ff1d24d354cf77dee7f7940ba29cc11236525e8ef4f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Note**
>
> A query that matches a conversation id pattern (e.g. `conv_…`) searches for that conversation
> directly instead of running search.

## Keyword vs Smart search

| Mode         | How it matches                       | Filters                                       |
| ------------ | ------------------------------------ | --------------------------------------------- |
| Keyword      | Full-text / fuzzy on message content | All conversation filters available            |
| Smart search | Semantic similarity via embeddings   | Most filters disabled while a query is active |

The mode is stored in the URL so links are shareable and reload-safe. Default is keyword.

## API reference

* [Text search](/docs/api-reference/conversations/messages/text-search) — keyword / full-text
* [Smart search](/docs/api-reference/conversations/messages/search) — semantic search
