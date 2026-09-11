---
title: "Langtrace"
source: https://docs.pinecone.io/integrations/langtrace
path: integrations/langtrace
---

Trace Pinecone API calls with Langtrace's OpenTelemetry SDK to debug RAG pipelines, monitor vector DB latency, and ship LLM observability.

[Langtrace AI](https://docs.langtrace.ai/) from Scale3 Labs is an open-source monitoring and evaluation platform for LLM-powered applications. It's built on [OpenTelemetry](https://opentelemetry.io/) (OTel) standards and supports native tracing for the most popular LLM vendors, vector databases, and frameworks, including LangChain and LlamaIndex.

Langtrace traces Pinecone natively, so its SDK generates OTel-standard traces with automatic instrumentation in two lines of code. You can send those traces to any observability tool that supports OTel, such as Datadog, Grafana Tempo, New Relic, or SigNoz. You can also view them in Langtrace's own client, which is optimized for LLM stacks.

Either way, you get high-cardinality tracing of your Pinecone API calls. That makes it easier to see what your database calls are doing and to troubleshoot your application during an incident.

<PrimarySecondaryCTA />
