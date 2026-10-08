---
title: "Snowflake Openflow"
source: https://docs.pinecone.io/integrations/snowflake-openflow
path: integrations/snowflake-openflow
---

Use the Pinecone processors in Snowflake Openflow to upsert, query, and delete vectors in a Pinecone index as part of a data pipeline.

[Snowflake Openflow](https://docs.snowflake.com/en/user-guide/data-integration/openflow/about) is a data integration service built on Apache NiFi. Datavolo previously offered this integration. Snowflake acquired Datavolo in 2024.

Openflow includes processors that work with a Pinecone index:

* `UpsertPinecone` publishes vectors, including metadata and optionally text, to a Pinecone index.
* `QueryPinecone` queries Pinecone for vectors that are similar to an input vector, or retrieves a vector by ID.
* `DeletePinecone` deletes vectors from a Pinecone index.

<PrimarySecondaryCTA />
