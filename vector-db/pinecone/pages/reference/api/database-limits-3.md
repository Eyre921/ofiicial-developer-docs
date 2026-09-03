---
title: "Pinecone Database limits overview"
source: https://docs.pinecone.io/reference/api/database-limits
path: reference/api/database-limits
---

Reference for Pinecone Database rate, object, operation, and identifier limits, plus known index and serverless limitations.

This page describes the limits and known limitations for Pinecone Database. Each topic has its own reference page:

* **[Rate limits](/reference/api/database-limits/rate-limits)**: request-per-second, monthly usage, and model throughput limits that vary by pricing plan, plus the `429` errors you get when you exceed them.
* **[Object limits](/reference/api/database-limits/object-limits)**: the number or size of projects, users, indexes, namespaces, storage, backups, and collections allowed by plan.
* **[Operation limits](/reference/api/database-limits/operation-limits)**: fixed batch-size limits for upsert, import, query, fetch, and delete, plus metadata filter limits.
* **[Identifier limits](/reference/api/database-limits/identifier-limits)**: maximum length and allowed characters for organization, project, index, namespace, and record identifiers.
* **[Known limitations](/reference/api/known-limitations)**: index and serverless caveats, such as upsert consistency and metadata rules.

<Note>
  If a limit is blocking you, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case. Many limits can be raised on request, and Support can often suggest a workaround for the ones that can't.
</Note>
