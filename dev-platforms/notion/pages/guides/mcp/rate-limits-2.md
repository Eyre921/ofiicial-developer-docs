---
title: "Notion MCP rate limits"
source: https://developers.notion.com/guides/mcp/rate-limits
path: guides/mcp/rate-limits
---

Understand Notion MCP request limits, handle rate-limit errors, and retry tool calls.

Notion MCP uses the standard [API request limits](/reference/request-limits). Every tool call counts toward them. These limits can change over time.

## What to do if you're rate-limited

If you encounter rate limit errors, ask your AI assistant to reduce parallel operations, or try again later.

Notion MCP retries a rate limit once when the wait is 2 seconds or less. Otherwise it returns the rate limit as a tool error right away instead of waiting it out. The error's `structuredContent.error` has `code: "rate_limited"`, the wait in seconds as `retry_after_seconds` when known, and the limit that was hit as `rate_limit_reason`. The text content includes the same `structuredContent` JSON for clients that read only text. See [Request limits](/reference/request-limits#rate-limit-responses).
