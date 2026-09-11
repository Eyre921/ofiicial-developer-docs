---
title: "Security"
source: https://langfuse.com/security.md
path: security
---

---
title: Overview
sidebarTitle: Overview
seoTitle: "Security & Compliance"
description: Overview of Langfuse's commitment to data privacy, security, and compliance, including links to detailed pages on specific measures and certifications.
---

# Security & Compliance Overview

**At Langfuse, we prioritize data privacy and security.** We understand that the data you entrust to us is a vital asset to your business, and we treat it with the utmost care.

We take active steps to demonstrate our commitment to data security and privacy such as annual SOC2 Type 2 and ISO27001 audits as well as External Penetration Tests. You can request access to the reports [here](/request-security-docs).

Langfuse is built with enterprise needs in mind, focusing on:

- **Security Measures:** Robust [Encryption](/security/encryption), access controls, and regular [Penetration Testing](/security/penetration-testing).
- **Privacy Measures:** Protecting user data according to regulations like [GDPR](/security/gdpr). We offer a [DPA](/dpa), provide a [HIPAA-ready region](/security/hipaa), and adhere to our [Privacy Policy](/privacy).
- **Transparency:** Open-source core and clear information on [software dependencies](/security/dependencies).
- **Reporting:** Clear channels for [responsible disclosure through Bugcrowd](/security/responsible-disclosure) and [Whistleblowing](/security/whistleblowing).

Langfuse is the most widely adopted LLM Engineering platform, used by **50,000+ companies**, with **34,464 GitHub stars**, **65M+ SDK installs per month**, and **38M+ Docker pulls**. Trusted by **21 of the Fortune 50** and **129 of the Fortune 500** companies.

## Langfuse Cloud security model

Langfuse Cloud is a fully managed, multi-tenant SaaS deployment. The security model combines three layers:

- **Security posture:** The production service is based on the same open-source Langfuse codebase, is covered by SOC 2 Type II and ISO 27001 audits, and undergoes annual third-party penetration tests. You can request the latest reports [here](/request-security-docs).
- **Tenant isolation:** All product data is scoped to a project. Every record is associated with a `projectId`, API keys are project-scoped, and authenticated requests are authorized through RBAC before queries are made. See the [Security FAQ](/security/security-faq) and [RBAC docs](/docs/administration/rbac).
- **Customer controls:** Teams can reduce what reaches Langfuse and how long it stays there with [masking](/docs/observability/features/masking), [data retention](/docs/administration/data-retention), [data deletion](/docs/administration/data-deletion), region selection, SSO/SCIM, and audit logs.

Langfuse Cloud runs on AWS and ClickHouse Cloud in isolated regional environments. Supporting services such as Postgres, ClickHouse, Redis, and S3 are covered by the same cloud security program: private network placement, least-privilege service access, encryption at rest and in transit, monitoring, and vendor/compliance review. If your requirements mandate infrastructure-level isolation in your own account or VPC, use [self-hosted Langfuse](/self-hosting) or contact us about Enterprise options.

## Compliance

We maintain internal policies in the [ClickHouse Trust Center](https://trust.clickhouse.com/) and adhere to several industry-standard compliance frameworks. Please check [Security FAQs](/security/security-faq) for more details.

- [SOC 2 Type II](/security/soc2)
- [ISO 27001](/security/iso27001)
- [HIPAA](/security/hipaa)
- [Hardening for Government](/self-hosting/configuration/hardening#hardening-for-government)

## Privacy

Langfuse is [GDPR](/security/gdpr) compliant, and offers data retention, data masking and data deletion capabilities to [manage the processing of personal data](/security/manage-personal-data). You can enter into a [DPA](/dpa) with Langfuse.

## Contact

- Use [Ask AI](/ask-ai) to get instant answers to your questions.
- For security inquiries: security@clickhouse.com
- For privacy inquiries: privacy@clickhouse.com
- For legal inquiries: legal@clickhouse.com

## General Information on Langfuse

### What is Langfuse?

Langfuse is an **open‑source AI engineering platform** that provides tracing, prompt management, evaluation, and metrics to help teams debug and continuously improve LLM‑based applications.

### What deployment models are available?

- **Langfuse Cloud** – fully‑managed SaaS (multi‑tenant) with US, EU, Japan, and HIPAA data regions
- **Self‑hosted OSS** – MIT‑licensed software that you can deploy on your own infrastructure
- **Self‑hosted Enterprise Edition** – commercial license with additional security/compliance features and vendor support.

### Which cloud provider and regions do you use?

Langfuse Cloud mainly runs on **AWS and ClickHouse Cloud**:

- **US & HIPAA region**: us-west-2 (Oregon)
- **EU region**: eu-west-1 (Ireland)
- **JP region**: ap-northeast-1 (Japan)

Self‑hosted customers can choose any region / provider. Langfuse Self-Hosted can be run fully offline/air-gapped.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/security.md`.

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
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx langfuse-cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

