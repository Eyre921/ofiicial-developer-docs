---
title: "Self-hosting"
source: https://langfuse.com/self-hosting.md
path: self-hosting
---

---
title: Self-host Langfuse (Open Source LLM Observability)
sidebarTitle: Overview
description: Self-host Langfuse - This guide shows you how to deploy open-source LLM observability with Docker, Kubernetes, or VMs on your own infrastructure.
label: "Version: v4"
---

# Self-host Langfuse

Langfuse is open source and can be self-hosted using Docker on your own infrastructure. Some add-on features require a [license key](/self-hosting/license-key).

When self-hosting Langfuse, you run the same infrastructure that powers Langfuse Cloud. Read ["Why Langfuse?"](/why) to learn more about why this is important to us.

## Deployment options [#deployment-options]

| Best for                | Deployment                                                                                                                                                                                                                                                                                          | Responsibility                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Fastest start           | [Langfuse Cloud](https://cloud.langfuse.com)                                                                                                                                                                                                                                                        | Fully managed by the Langfuse team                       |
| Local use and testing   | [Docker Compose](/self-hosting/deployment/docker-compose)                                                                                                                                                                                                                                           | Single VM without high availability, scaling, or backups |
| Production self-hosting | [Kubernetes (Helm)](/self-hosting/deployment/kubernetes-helm), [AWS](/self-hosting/deployment/aws), [Azure](/self-hosting/deployment/azure), [GCP](/self-hosting/deployment/gcp), [Render](/self-hosting/deployment/render) (community), or [Railway](/self-hosting/deployment/railway) (community) | Your infrastructure                                      |

Unless marked as community-supported, these deployment options are maintained and tested by the Langfuse team. Community-supported options are maintained in third-party repositories and supported on a best-effort basis. Report problems via [GitHub issues](/issues).

## Architecture [#architecture]

Langfuse only depends on open source components and can be deployed locally, on cloud infrastructure, or on-premises.

```mermaid
flowchart TB
    User["UI, API, SDKs"]
    subgraph vpc["VPC"]
        Web["Web Server<br/>(langfuse/langfuse)"]
        Worker["Async Worker<br/>(langfuse/worker)"]
        Postgres@{ img: "/images/logos/postgres_icon.svg", label: "Postgres - OLTP\n(Transactional Data)", pos: "b", w: 60, h: 60, constraint: "on" }
        Cache@{ img: "/images/logos/redis_icon.png", label: "Redis\n(Cache, Queue)", pos: "b", w: 60, h: 60, constraint: "on" }
        Clickhouse@{ img: "/images/logos/clickhouse_icon.svg", label: "Clickhouse - OLAP\n(Observability Data)", pos: "b", w: 60, h: 60, constraint: "on" }
        S3@{ img: "/images/logos/s3_icon.svg", label: "S3 / Blob Storage\n(Raw events, multi-modal attachments)", pos: "b", w: 60, h: 60, constraint: "on" }
    end
    LLM["LLM API/Gateway<br/>(optional; BYO; can be same VPC or VPC-peered)"]

    User --> Web
    Web --> S3
    Web --> Postgres
    Web --> Cache
    Web --> Clickhouse
    Web -..->|"optional for playground"| LLM

    Cache --> Worker
    Worker --> Clickhouse
    Worker --> Postgres
    Worker --> S3
    Worker -..->|"optional for evals"| LLM
```

<details>
<summary>View architecture components</summary>

Langfuse consists of two application containers, storage components, and an optional LLM API/Gateway.

- [**Application Containers**](/self-hosting/deployment/infrastructure/containers)
  - Langfuse Web: The main web application serving the Langfuse UI and APIs.
  - Langfuse Worker: A worker that asynchronously processes events.
- **Storage Components**:
  - [Postgres](/self-hosting/deployment/infrastructure/postgres): The main database for transactional workloads.
  - [Clickhouse](/self-hosting/deployment/infrastructure/clickhouse): High-performance OLAP database which stores traces, observations, and scores.
  - [Redis/Valkey cache](/self-hosting/deployment/infrastructure/cache): A fast in-memory data structure store. Used for queue and cache operations.
  - [S3/Blob Store](/self-hosting/deployment/infrastructure/blobstorage): Object storage to persist all incoming events, multi-modal inputs, and large exports.
- [**LLM API / Gateway**](/self-hosting/deployment/infrastructure/llm-api): Some features depend on an external LLM API or gateway.

Langfuse can be deployed within a VPC or on-premises in high-security environments.
Internet access is optional.
See [networking](/self-hosting/security/networking) documentation for more details.

</details>

## Optimized for performance, reliability, and uptime

Langfuse OSS and Enterprise use the same codebase as Langfuse Cloud. Langfuse processes **90B+ observations per month** and is trusted by **21 of the Fortune 50**. Its Docker images have been pulled **38M+ times**.

<details>
<summary>How Langfuse is optimized for scale and reliability</summary>

Some of the optimizations include:

- **Queued trace ingestion**: All traces are received in batches by the Langfuse Web container and immediately written to S3. Only a reference is persisted in Redis for queueing. Afterwards, the Langfuse Worker will pick up the traces from S3 and ingest them into Clickhouse. This ensures that high spikes in request load do not lead to timeouts or errors constrained by the database.
- **Caching of API keys**: API keys are cached in-memory in Redis. Thereby, the database is not hit on every API call and unauthorized requests can be rejected with very low resource usage.
- **Caching of prompts (SDKs and API)**: Even though prompts are cached client-side by the Langfuse SDKs and only revalidated in the background ([docs](/docs/prompts)), they need to be fetched from the Langfuse on first use. Thus, API response times are very important. Prompts are cached in a read-through cache in Redis. Thereby, hot prompts can be fetched from Langfuse without hitting a database.
- **Hyper-optimized ClickHouse schema**: Read-heavy analytical operations use a wide, mostly immutable observations table that avoids read-time joins and deduplication while taking advantage of ClickHouse's most performant access patterns. Read how we [simplified Langfuse for scale](/blog/2026-03-10-simplify-langfuse-for-scale).
- **Multi-modal traces in S3**: Multi-modal traces can include large videos or arbitrary files. To enable support for these, they are directly uploaded to S3/Blob Storage from the client SDKs. Learn more about [multi-modal traces](/docs/tracing-features/multi-modality).
- **Recoverability of events**: All incoming tracing and evaluation events are persisted in S3/Blob Storage first. Only after successful processing, the events are written to the database. This ensures that even if the database is temporarily unavailable, the events are not lost and can be processed later.
- **Background migrations**: Long-running migrations that are required by an upgrade but not blocking for regular operations are offloaded to a background job. This massively reduces the downtime during an upgrade. Learn more about [background migrations](/self-hosting/upgrade/background-migrations).

</details>

## Features

Langfuse supports many configuration options and self-hosted features.
For more details, please refer to the [configuration guide](/self-hosting/configuration).

- [Authentication & SSO](/self-hosting/security/authentication-and-sso)
- [Automated Access Provisioning](/self-hosting/administration/automated-access-provisioning)
- [Caching](/self-hosting/configuration/caching)
- [Code evaluators](/self-hosting/configuration/code-evaluators)
- [Langfuse Assistant](/self-hosting/configuration/langfuse-assistant)
- [Custom Base Path](/self-hosting/configuration/custom-base-path)
- [Encryption](/self-hosting/configuration/encryption)
- [Headless Initialization](/self-hosting/administration/headless-initialization)
- [Data Masking](/self-hosting/security/data-masking)
- [Networking](/self-hosting/security/networking)
- [Organization Creators (EE)](/self-hosting/administration/organization-creators)
- [Instance Management API (EE)](/self-hosting/administration/instance-management-api)
- [Health and Readiness Check](/self-hosting/configuration/health-readiness-endpoints)
- [Observability via OpenTelemetry](/self-hosting/configuration/observability)
- [Transactional Emails](/self-hosting/configuration/transactional-emails)
- [UI Customization (EE)](/self-hosting/administration/ui-customization)

## Subscribe to updates [#subscribe]

Release notes are published on [GitHub](https://github.com/langfuse/langfuse/releases). Langfuse uses tagged semver releases ([versioning policy](/self-hosting/upgrade/versioning)).

**[Langfuse OSS updates](/self-hosting/oss-newsletter)** — get an email when we ship important features and new releases for self-hosted (open source) Langfuse. Self-hosting updates only, no spam.

Subscribe to the Langfuse OSS newsletter at https://langfuse.com/self-hosting/oss-newsletter.

You can also watch the GitHub releases to get notified about new releases:

---

If you experience any issues when self-hosting Langfuse, please:

1. Check out [Troubleshooting & FAQ](/self-hosting/troubleshooting-and-faq) page.
2. Use [Ask AI](/docs/ask-ai) to get instant answers to your questions.
3. Ask the maintainers on [GitHub Discussions](/gh-support).
4. Create a bug report or feature request on [GitHub](/issues).

  Enterprise-grade support is available when self-hosting Langfuse. Learn more on
  our [pricing page](/pricing-self-host).

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/self-hosting.md`.

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

