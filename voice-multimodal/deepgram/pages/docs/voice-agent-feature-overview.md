---
title: "Feature Overview"
source: https://developers.deepgram.com/docs/voice-agent-feature-overview.md
path: docs/voice-agent-feature-overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Feature Overview

## Voice Selection

| Voice Selection                                              |
| ------------------------------------------------------------ |
| [Deepgram TTS Voice Models](/docs/tts-models)                |
| [Third Party TTS Voice Models](/docs/voice-agent-tts-models) |

## Supported LLM Models

| Models                                     |
| ------------------------------------------ |
| [LLM Models](/docs/voice-agent-llm-models) |

## Conversation Context

| Feature                                                   |
| --------------------------------------------------------- |
| [Agent Context](/docs/configure-voice-agent#agentcontext) |

## Inputs: Client Messages

| Feature                                                        |
| -------------------------------------------------------------- |
| [Settings](/docs/voice-agent-settings)                         |
| [Update Speak](/docs/voice-agent-update-speak)                 |
| [Update Think](/docs/voice-agent-update-think)                 |
| [Update Prompt](/docs/voice-agent-update-prompt)               |
| [Inject Agent Message](/docs/voice-agent-inject-agent-message) |
| [Inject User](/docs/voice-agent-inject-user-message)           |
| [Agent Keep Alive](/docs/agent-keep-alive)                     |

## Outputs: Server Events

| Feature                                                                                                  |
| -------------------------------------------------------------------------------------------------------- |
| [Welcome](/docs/voice-agent-welcome-message)                                                             |
| [Settings Applied](/docs/voice-agent-setting-applied-message)                                            |
| [Conversation Text](/docs/voice-agent-conversation-text)                                                 |
| [User Started Speaking](/docs/voice-agent-user-started-speaking)                                         |
| [Agent Thinking](/docs/voice-agent-agent-thinking)                                                       |
| [Acknowledgements](/docs/voice-agent-acknowledgements) (`PromptUpdated`, `SpeakUpdated`, `ThinkUpdated`) |
| [Agent Audio Done](/docs/voice-agent-agent-audio-done)                                                   |
| [Errors & Warnings](/docs/voice-agent-errors-warnings)                                                   |

## Input / Output Events

| Feature                                                            |
| ------------------------------------------------------------------ |
| [Function Call Request](/docs/voice-agent-function-call-request)   |
| [Function Call Response](/docs/voice-agent-function-call-response) |

## Session Length

Sessions close automatically after 2 hours. The server warns you 5 minutes ahead with `MAXIMUM_SESSION_LENGTH_APPROACHING` and closes the session with a `MAXIMUM_SESSION_LENGTH_REACHED` error. To keep a conversation going, start a new session and replay the prior turns in `agent.context`. See [Maximum session length](/docs/voice-agent-errors-warnings#maximum-session-length).

## Rate Limits

For information on Deepgram's Concurrency Rate Limits, refer to our [API Rate Limits Documentation](/reference/api-rate-limits).

## Deepgram Self-Hosted

Having challenges with performance and latency? Check out Deepgram's [Self-Hosted Solution](/docs/self-hosted-introduction) to get the benefits of running your own hosted instance of Deepgram.
