---
title: "Channels"
source: https://developers.deepgram.com/docs/channels.md
path: docs/channels
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Channels

`channels` *int32* Default: `1`

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming: Flux

&#x20;All available languages

The default value is `1`.

The Channels feature is used when the [Encoding](/docs/encoding/) feature is also being used to submit streaming raw audio. It is not read at any other time.

## Enable Feature

To enable Channels, when you call Deepgram’s API, add a `channels` parameter in the query string and set it to the number of channels in your submitted audio.

`channels=NUMBER_OF_CHANNELS`
