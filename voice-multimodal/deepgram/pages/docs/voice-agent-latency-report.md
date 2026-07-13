---
title: "Latency Report"
source: https://developers.deepgram.com/docs/voice-agent-latency-report.md
path: docs/voice-agent-latency-report
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Latency Report

&#x20;Voice Agent

The `LatencyReport` message is the richest latency signal the Agent API emits. The server sends it after each turn with a breakdown of latency across the full STT → LLM → TTS pipeline.

## Purpose

`LatencyReport` lets you attribute latency to the right stage — for example, separating LLM time-to-first-token from TTS time, and isolating tool-call and thinking overhead. It is fully supported and sent automatically; no configuration flag is required to receive it.

## Fields

All fields are floats in seconds, and each is optional (omitted when not applicable to that turn), so log defensively rather than assuming every field is present on every report.

| Field                  | Type   | What It Measures                                                |
| ---------------------- | ------ | --------------------------------------------------------------- |
| `type`                 | string | Must be `"LatencyReport"`.                                      |
| `stt_latency`          | number | Speech-to-text: audio received to transcript produced.          |
| `ttt_token_latency`    | number | Time to first token of any type (text, tool call, or thinking). |
| `ttt_text_latency`     | number | Time to first text token from the LLM.                          |
| `ttt_tool_latency`     | number | Time to first tool-call token from the LLM.                     |
| `ttt_thinking_latency` | number | Time to first thinking token from the LLM.                      |
| `tts_latency`          | number | Text-to-speech: first text token to first audio byte.           |
| `total_latency`        | number | End-to-end: user utterance end to first audio byte.             |

## Example Payload

```json JSON
{
  "type": "LatencyReport",
  "stt_latency": 0.12,
  "ttt_token_latency": 0.34,
  "ttt_text_latency": 0.36,
  "ttt_tool_latency": 0.41,
  "ttt_thinking_latency": 0.29,
  "tts_latency": 0.18,
  "total_latency": 0.64
}
```

## Use Cases

Capture `LatencyReport` the same way as every other frame to chart and troubleshoot latency:

* Attribute end-to-end latency to the STT, LLM, or TTS stage.
* Separate LLM time-to-first-token from TTS time.
* Isolate tool-call and thinking overhead from text generation.

For an end-to-end logging pattern that persists every WebSocket frame, see [Session Observability](/docs/voice-agent-observability).
