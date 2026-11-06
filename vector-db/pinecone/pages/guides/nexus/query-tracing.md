---
title: "Nexus query traces"
source: https://docs.pinecone.io/guides/nexus/query-tracing
path: guides/nexus/query-tracing
---

Learn what each part of a Pinecone Nexus query trace shows, from the summary bar and token detail to the reasoning steps and tool calls behind an answer.

Pinecone Nexus records a trace for every query. The trace shows each step the model ran, the retrieval code it generated, and the tokens and time each step took, so you can understand a result or debug an unexpected one.

## Open a trace

After a query returns, click **Show trace**. To trace an earlier query, open its session from the **Sessions** list and click **Show trace** on that query.

A trace opens with the query text and the model that answered, and it ends with the final answer the caller received.

## Summary bar

The summary bar at the top of the trace totals the run:

* **Steps:** The number of reasoning steps the model took, plus the final answer.
* **Tool calls:** The number of calls to the retrieval SDK.
* **Tokens:** Input and output tokens for the whole query.
* **Latency:** The time it took to produce the answer.

To see where the tokens went, click **Token detail**.

## Token detail

* **Where the tokens went:** How the tokens divide between the reasoning steps and the final synthesis, plus the total tokens billed.
* **New input by step:** The new input tokens each step adds. Each step resends the whole conversation, so only the new tokens are new work, and the prompt cache can serve the rest.
* **Output tokens by step:** The output tokens each step and the final answer produced.
* **Caching savings:** How much input the prompt cache served versus how much was billed as new input. The more context a run reuses, the more of its input the cache serves.

## Spans and inspector

The trace lists each span with its duration, from the model's reasoning steps to the tool calls they made. The spans follow the agent loop described in [Queries](/guides/nexus/queries). Select a span to show its details in the inspector:

* **Reasoning step:** Input and output tokens, timing split into decide time (the model reasoning) and execute time (the code running), and the code the model generated and ran.
* **Tool call:** Its arguments (such as the SQL a `query_db()` call ran), its result (such as the number of rows returned), and its timing.
