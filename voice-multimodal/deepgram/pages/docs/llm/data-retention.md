---
title: "Data retention and MIP"
source: https://developers.deepgram.com/docs/llm/data-retention.md
path: docs/llm/data-retention
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Data retention and MIP

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

Think-Fast requests are always part of the Model Improvement Program (MIP): you cannot opt them out. phoneLLM mini requests are part of MIP unless you opt them out.

## Model Improvement Program

Unless a request is opted out, Deepgram stores the request and the model's response, including stream timing, in short-term storage and uses it for training under the [Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program).

| Model                       | `mip_opt_out: false` (default) | `mip_opt_out: true`                                |
| --------------------------- | ------------------------------ | -------------------------------------------------- |
| `think-fast`                | Supported                      | Not supported. The request is rejected with `400`. |
| `phonellm-mini-alpha-2-fp8` | Supported                      | Supported. Requires the MIP opt-out add-on.        |

> **Warning**
>
> **Think-Fast can only be used with the Model Improvement Program.** A Think-Fast request is rejected with `400` and this message when it opts out of MIP, or when your project requires MIP opt-out for all requests:
>
> `The think-fast LLM model does not yet support opting out of the Model Improvement Program (mip_opt_out).`
>
> In the Voice Agent API, a `Settings` message that selects `think-fast` and sets `mip_opt_out: true` at its top level, or comes from a project that requires opt-out, is rejected with `INVALID_SETTINGS` and the same message.

### Opt phoneLLM mini out of MIP

A phoneLLM mini request is opted out when either of these is true:

* The request sets `mip_opt_out` to `true`. This requires the MIP opt-out add-on on your project; without it, the request is rejected with `403`.
* Your project requires MIP opt-out for all requests.

```json
{
  "model": "phonellm-mini-alpha-2-fp8",
  "mip_opt_out": true,
  "messages": [{ "role": "user", "content": "Hi, can you check on my order?" }]
}
```

Deepgram reads `mip_opt_out` and does not forward it to the model service.

## Abuse monitoring

Deepgram reviews stored Early Access traffic for abuse of the models, using automated safety classifiers after the fact. Because every Think-Fast request is stored under MIP, every Think-Fast request is covered by abuse monitoring.

## Related resources

* [Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program)
* [Data Privacy Compliance](/trust-security/data-privacy-compliance)
