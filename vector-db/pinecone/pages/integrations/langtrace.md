---
title: "Langtrace"
source: https://docs.pinecone.io/integrations/langtrace
path: integrations/langtrace
---

Connect Pinecone and Langtrace to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

Scale3 Labs recently launched Langtrace AI, an open-source monitoring and evaluation platform for LLM-powered applications. Langtrace is built based on Open Telemetry(OTEL) standards and supports native tracing for the most popular LLM vendors, VectorDBs, and frameworks(like Langchain and LlamaIndex).

Langtrace AI supports tracing Pinecone natively, which means the Langtrace SDK can generate OTEL standard traces with automatic instrumentation in just 2 lines of code. These traces can be ingested by an observability tool that supports OTEL, such as Datadog, Grafana/Prometheus, SigNoz, Sentry, etc. Langtrace also has a visualization client that is optimized for visualizing the traces generated in an LLM stack.

By having a Pinecone integration, Pinecone users can get access to rich and high cardinal tracing for the Pinecone API calls using Langtrace, which they can ingest into their observability tool of choice. This helps customers gain insights into the DB calls and help with debugging and troubleshooting applications in case of incidents.

<PrimarySecondaryCTA />
