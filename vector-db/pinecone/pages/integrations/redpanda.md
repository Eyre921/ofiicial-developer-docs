---
title: "Redpanda"
source: https://docs.pinecone.io/integrations/redpanda
path: integrations/redpanda
---

Stream events into Pinecone with Redpanda Connect's declarative YAML pipelines for real-time vector ingestion, at-least-once delivery, and RAG ETL.

Redpanda Connect is a declarative data streaming service that handles data engineering tasks with chained, stateless processing steps. The Pinecone connector for Redpanda writes data from many existing data sources to Pinecone, configured in a few lines of YAML.

Redpanda Connect implements transaction-based resiliency with back pressure, so when connecting to at-least-once sources and sinks, it guarantees at-least-once delivery without persisting messages during transit.

Redpanda Connect comes with a wide range of connectors and is data agnostic, so you can add it to your existing infrastructure. Its functionality overlaps with integration frameworks, log aggregators, and ETL workflow engines, so you can use it to complement these tools or as a simpler alternative.

<PrimarySecondaryCTA />
