---
title: "Supported Audio Formats"
source: https://developers.deepgram.com/docs/supported-audio-formats.md
path: docs/supported-audio-formats
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Supported Audio Formats

# Common audio formats

Deepgram can handle nearly all audio formats and encodings available (over 100+). Some of the most common audio formats and encodings we support include:

* MP3
* MP4
* MP2
* AAC
* WAV
* FLAC
* PCM
* M4A
* Ogg
* Opus
* WebM

# Using other audio formats

We recommend testing small sets of audio when first operating with new audio sources to ensure compatibility.

Because audio format is largely unconstrained, we always recommend to ensure compatibility by testing small sets of audio when first operating with new audio sources.

# Audio format best practices

Generally you don't have to specify the audio format in your API request but if you know the format of your audio, providing it in you API request can help reduce unnecessary computation.

***
