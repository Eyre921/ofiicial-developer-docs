---
title: "Data regions"
source: https://langfuse.com/security/data-regions.md
path: security/data-regions
---

---
title: Data Regions & Availability
description: Details on Langfuse Cloud data regions, high availability, and the self-hosted option.
---

# Data Regions & Availability

Langfuse Cloud is designed for high availability and offers multiple data regions to meet your needs.

Our database and application run on AWS infrastructure, partly managed by Clickhouse.

## Langfuse Cloud Regions

All data, user accounts, and infrastructure are completely separated between the regions. You can have accounts in each regions.

| Region                                    | URL                                                                    | Location                     |
| ----------------------------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| **US**                                    | [`https://us.cloud.langfuse.com`](https://us.cloud.langfuse.com)       | Oregon (AWS `us-west-2`)     |
| **EU**                                    | [`https://cloud.langfuse.com`](https://cloud.langfuse.com)             | Ireland (AWS `eu-west-1`)    |
| **Japan**                                 | [`https://jp.cloud.langfuse.com`](https://jp.cloud.langfuse.com)       | Tokyo (AWS `ap-northeast-1`) |
| **HIPAA** ([learn more](/security/hipaa)) | [`https://hipaa.cloud.langfuse.com`](https://hipaa.cloud.langfuse.com) | Oregon (AWS `us-west-2`)     |

> Since all data and accounts are fully separated between regions, switching regions requires creating a new account and migrating your data. See the [data migration cookbook](/guides/cookbook/example_data_migration) for scripts to transfer traces, prompts, and datasets between projects.

## Connecting to a Region

To connect to a specific data region using the Langfuse SDKs, you need to set the base URL environment variable or pass it during initialization:

- **Python:** Set `LANGFUSE_BASE_URL` environment variable or use the `base_url` parameter.
- **JS/TS:** Set `LANGFUSE_BASE_URL` environment variable or use the `baseUrl` parameter.

Example base URLs:

- US: `https://us.cloud.langfuse.com`
- EU: `https://cloud.langfuse.com`
- Japan: `https://jp.cloud.langfuse.com`
- HIPAA: `https://hipaa.cloud.langfuse.com`

Refer to the [SDK documentation](/docs/sdk) for detailed configuration instructions.

## Choosing a Region

When selecting a data region, consider the following factors:

- **Compliance and data privacy requirements:** Choose the region that aligns with your organization's data residency needs (e.g., GDPR often favors the EU region).
- **Latency for Prompt Management:** If using Langfuse [Prompt Management](/docs/prompts), select the region closer to your application servers for lower latency when fetching prompts. This is hardly noticeable as the prompts are cached by the Langfuse SDK.
- **Latency for UI access:** Choose the region closer to your team's location for a faster experience when using the Langfuse web interface.

Less critical factor:

- **Tracing ingestion latency:** Trace data is sent asynchronously in batches, making ingestion latency less of a direct concern for application performance.

## Business Continuity & Availability

| Control                | Details                                                                                                                                                                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **High Availability**  | Multi‑AZ databases & load‑balanced stateless application layer on AWS.                                                                                                                                                                                                                             |
| **Recovery Precision** | RPO: 10 minutes (PITR for Postgres). RTO: 12 hours.                                                                                                                                                                                                                                                |
| **Backup Layers**      | Postgres: 7d retention. ClickHouse: 6-hourly backups (4d retention). S3: 7d versioning retention.                                                                                                                                                                                                  |
| **Durability**         | Encrypted backups stored across multiple availability zones within the primary region on AWS/ClickHouse Cloud; tested at least annually for restoration integrity. Postgres backups are additionally replicated to a secondary AWS region (see [Cross-Region Backup](#cross-region-backup) below). |
| **Status Page**        | [https://status.langfuse.com](https://status.langfuse.com) with historical uptime and incidents.                                                                                                                                                                                                   |

### Cross-Region Backup [#cross-region-backup]

To allow recovery from the permanent loss of an AWS region, a subset of data at rest is replicated to a secondary AWS region in the same legal jurisdiction.
This is a disaster-recovery control and does not provide active-active failover; on a full regional outage, Langfuse would rebuild the application stack in the secondary region and restore from the replicated backups.
The expected rebuild time is up to 12 hours.

| Data store                    | Primary region                                                           | Secondary region                                        | Mechanism                                                         | Retention             |
| ----------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------------------------------------- | --------------------- |
| **Postgres**                  | EU: `eu-west-1` <br/> US / HIPAA: `us-west-2` <br/> JP: `ap-northeast-1` | `eu-central-1` <br/> `us-east-2` <br/> `ap-northeast-3` | AWS Backup daily snapshot copy, re-encrypted with a dedicated CMK | 7 days in each region |
| **ClickHouse** (tracing data) | Same as the Cloud region above                                           | Not replicated                                          | —                                                                 | —                     |
| **S3 media bucket**           | Same as the Cloud region above                                           | Not replicated                                          | —                                                                 | —                     |

Postgres contains organization, project, user, API key, prompt, dataset, annotation, and score configuration data.
Replicating it cross-region allows projects, credentials, and prompt management to be restored without customer intervention following a regional outage.

ClickHouse stores historical traces, observations, and scores.
ClickHouse Cloud does not currently offer managed cross-region backup, and Langfuse does not maintain an out-of-region copy.
**On the permanent loss of the primary AWS region, historical tracing data is not recoverable from Langfuse, and a restored environment would begin ingesting fresh data.**
Active tracing ingestion resumes once the replacement environment is live.

S3 media buckets store uploaded media items referenced from traces. They are not replicated cross-region.
**On the permanent loss of the primary AWS region, uploaded media items are not recoverable**, even where the referencing trace survives.

All secondary regions are within the same legal jurisdiction as their primary region (EU ↔ EU, US ↔ US, Japan ↔ Japan), so cross-region replication does not change the data-residency or cross-border-transfer posture declared in the [DPA](/dpa) and [HIPAA region overview](/security/hipaa).

  **Protecting tracing data against a regional outage:** Since ClickHouse
  tracing data and S3 media buckets are not replicated cross-region, we
  recommend using the [Blob Storage
  integration](/docs/api-and-data-platform/features/export-to-blob-storage) to
  continuously export traces and observations into your own bucket. If that
  bucket resides outside of your Langfuse Cloud region, your tracing data is
  protected against a regional failure.

## Self-hosted Instances

Alternatively, you can self-host Langfuse for full control over your data and infrastructure. For installation and configuration, see: [Self-hosting guide](/self-hosting).

## Contact

For questions about data regions or availability, please [talk to us](/talk-to-us).

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/security/data-regions.md`.

### Querying these docs

If the answer is not on this page, query the documentation instead of guessing:

- **Semantic search** across all Langfuse docs, returning an answer with the relevant pages and excerpts. Ask a specific, self-contained question:

  ```bash
  curl -sG "https://langfuse.com/api/search-docs" --data-urlencode "query=How do I trace a LangGraph agent?"
  ```

- **Index of every page**: <https://langfuse.com/llms.txt>, with per-section indexes [llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), and [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt).

### Before writing Langfuse code

- **Install the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill).** It encodes Langfuse's own best practices for instrumentation, prompt management, and evaluation, and materially improves results.
- **Read [What does a good trace look like?](https://langfuse.com/docs/observability/best-practices.md)** before instrumenting an application.
- **Verify endpoints, parameters, and response fields** against the [API reference](https://api.reference.langfuse.com) instead of inferring them from code examples.
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx @langfuse/cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

