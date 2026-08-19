---
title: "Query tracing"
source: https://docs.pinecone.io/guides/nexus/query-tracing
path: guides/nexus/query-tracing
---

Trace any query to see the steps, retrieval code, tokens, and cost behind its answer.

Every query is recorded as a trace that shows how Pinecone Nexus reached an answer, from the steps the model ran down to the retrieval code it generated, along with the tokens, time, and cost each step took. Use it to understand a result or debug an unexpected one.

To open a trace, click **Show trace** after a query returns, or reopen a past query from its session in the **Sessions** list. A trace opens to the query text, the model that answered, and the views below.

## Summary bar

The summary bar reports the shape of the run at a glance.

* **Steps.** How many reasoning steps the model took, plus the final answer.
* **Tool calls.** How many times it called the retrieval SDK.
* **Tokens.** Input and output tokens for the whole query.
* **Latency.** Wall-clock time to produce the answer.
* **Cost.** Total cost, with a breakdown in **Cost detail**.

## Cost detail

**Cost detail** breaks the run down by tokens and cost.

* **Where the tokens went.** How the spend divides between the reasoning steps and the final synthesis, plus the total billed.
* **New input by step.** The fresh input tokens each step adds. Every step re-sends the whole conversation, so only the new tokens are fresh work. The carried remainder is re-read context that can be served from the prompt cache.
* **Output tokens by step.** The output tokens produced by each step and the answer.
* **Caching savings.** How much input was served from cache versus billed as fresh, with an effective cost estimate. Cached input bills far below fresh input, so a run that reuses more context costs less.

## Spans and inspector

The trace lists each span with its duration, from the model's own reasoning steps to the individual tool calls it made. Select any span to update the **inspector** with the detail for that span.

* **A reasoning step** shows its input and output tokens, its timing (split into decide time while the model reasons and execute time while the code runs), its cost, and the generated code the model wrote and ran.
* **A tool call** (for example, `query_db()`) shows its arguments (the query it ran), its result (such as the number of rows returned), and its timing.

This is the same agent loop described in [Queries](/guides/nexus/how-queries-work), made visible one span at a time.

## Final answer

The trace ends with the final answer produced for the query, the same grounded response the caller receives.
