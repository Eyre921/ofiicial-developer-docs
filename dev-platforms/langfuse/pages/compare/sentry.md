---
title: "Sentry"
source: https://langfuse.com/compare/sentry.md
path: compare/sentry
---

---
title: Langfuse vs. Sentry for AI agents
shortTitle: Sentry
seoTitle: "Sentry AI Observability Alternative: Langfuse vs. Sentry"
description: Langfuse is the open-source AI engineering platform beside Sentry. October 2026 comparison of agent tracing, evaluation, retention, self-hosting, Seer, and when to run both.
tags: [comparison]
---

# Langfuse vs. Sentry for AI agents

This guide outlines the key differences between **[Langfuse](/)** and **[Sentry](https://sentry.io/product/tracing/ai-agent/)** for AI agent tracing and the quality workflow around it. All Sentry facts were checked against public Sentry pages in October 2026.

## TL;DR

- **Built for AI engineering, open-source core.** Langfuse's core tracing, evaluation, prompt management, and APIs are [MIT-licensed](#open-source-and-deployment) and available on Cloud or self-hosted, with Enterprise SSO in the free distribution; additional Enterprise features require a license. Sentry's source is Fair Source under the FSL, Apache 2.0 after two years, and Seer is unavailable on its self-hosted install.
- **The whole improvement loop in the product.** [Datasets, prompt experiments in the UI, application experiments through the SDK, annotation queues, LLM-as-a-judge, code evaluators, prompt labels, and CI gates](#improvement-loop) run inside Langfuse. Sentry documents exporting conversations to tools including Langfuse for evaluation; Seer focuses on investigating and fixing application code.
- **3 years of history through APIs and exports.** Langfuse Pro keeps raw traces for 3 years on ClickHouse, [open source since 2016](#storage), read through APIs, scheduled exports to your bucket on Pro with the Teams add-on, Enterprise, and self-hosted, and SQL when you self-host. Sentry retains full-fidelity spans for 30 days; Business and Enterprise add sampled retention up to 13 months.
- **Unlimited users, one meter, Seer optional.** Langfuse Pro is [$199 plus units](#pricing) with unlimited users and Halo on every Cloud plan. Sentry's $26 Team estimate is an application bill with 5 million spans; AI observability is on every plan, and Seer is an optional subscription at $40 per active contributor per month.
- **Most teams run both.** Sentry stays on errors, performance, and replay; Langfuse holds the agent workflow, [from the same OpenTelemetry instrumentation](#coexistence).

**Choose Langfuse** if you want a platform built for AI engineering rather than agent spans inside an error tracker: datasets, experiments, annotation queues, and prompt labels on the same production traces, an open-source core on Cloud or self-hosted including air-gapped, and 3 years of history on ClickHouse you can query and export. Proven at 21 of the Fortune 50.

**Choose Sentry agent tracing** if you are already running Sentry and the agent is one more span in an application you debug there. You accept 30 days of full-fidelity spans with sampled retention beyond that on Business and Enterprise, span quotas shared with the rest of the app, Seer as a separate per-contributor subscription that is absent from self-hosted, and an evaluation step that Sentry documents as an export.

---

## Open source and deployment [#open-source-and-deployment]

Langfuse's core tracing, evaluation, prompt management, and APIs are MIT-licensed and available on Cloud or self-hosted; additional Enterprise features require a license. [Self-hosting](/self-hosting) runs the UI, login, and data in your environment on every tier, including [air-gapped operation](/self-hosting/security/networking), and Enterprise SSO and organization-level RBAC ship in the [free distribution](/pricing-self-host). Langfuse Cloud is covered by [SOC 2 Type II and ISO 27001 audits, is GDPR compliant](/security), and signs a BAA from the Pro plan in the [HIPAA region](/security/hipaa). Langfuse is used by [21 of the Fortune 50 and 129 of the Fortune 500](/enterprise).

Sentry's [self-hosted docs](https://develop.sentry.dev/self-hosted/) publish the source under the Functional Source License, Apache 2.0 after two years, with a ban on offering it as a competing service. The install is Docker Compose with a 4-core, 16 GB minimum and community Discord in place of a support agreement. Seer is unavailable in self-hosted Sentry, which lists it with other AI and ML features as closed source; agent-tracing availability must be checked separately for the version you deploy. Air-gapped installation is described, with the note that Sentry provides no further help for it.

|                            | Langfuse                                                                                                                                                                            | Sentry                                                                                                                                                                        |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| License                    | **[MIT](https://github.com/langfuse/langfuse)** core: tracing, evaluation, prompts, APIs; Enterprise features licensed separately                                                   | FSL, Apache 2.0 after 2 years                                                                                                                                                 |
| GitHub stars               | [![Langfuse GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=for-the-badge&label=%20&labelColor=black&color=orange)](https://github.com/langfuse/langfuse) | [![Sentry GitHub stars](https://img.shields.io/github/stars/getsentry/sentry?style=for-the-badge&label=%20&labelColor=black&color=grey)](https://github.com/getsentry/sentry) |
| Self-hosting               | **[Every tier, including free](/pricing-self-host)**, evaluators and prompts included                                                                                               | Docker Compose, community-supported                                                                                                                                           |
| In-app AI agent on-prem    | [Halo](/docs/api-and-data-platform/features/halo), public beta on self-hosted                                                                                                       | Seer unavailable                                                                                                                                                              |
| Air-gapped operation       | Supported                                                                                                                                                                           | Described, not supported                                                                                                                                                      |
| Enterprise SSO             | **Included in free OSS**; Cloud via the [Teams add-on](/pricing)                                                                                                                    | SAML and SCIM on Business and Enterprise                                                                                                                                      |
| Published Cloud Enterprise | **[$2,499/month](/pricing)**                                                                                                                                                        | Custom                                                                                                                                                                        |

---

## Storage and retention [#storage]

[ClickHouse](https://clickhouse.com/) has been [open source since June 15, 2016](https://clickhouse.com/blog/open-source-10) (Apache 2.0) and is today the most popular open-source analytical database, with 2,000+ contributors. Langfuse Cloud and self-hosted run the same ClickHouse architecture, so you can move between them without locking into a closed store.

Both products store spans in ClickHouse. Langfuse works directly with ClickHouse's core team as [part of ClickHouse](/blog/joining-clickhouse). Every LLM call, tool execution, and agent step is written once to a wide, immutable observations table ([details](/blog/2026-03-10-simplify-langfuse-for-scale)), which is how Pro keeps 3 years of raw traces queryable. High-volume reads go through the [Observations](/docs/api-and-data-platform/features/public-api#v2) and [Metrics](/docs/metrics/features/metrics-api#v2) APIs, [scheduled exports](/docs/api-and-data-platform/features/export-to-blob-storage) (Pro with the Teams add-on, Enterprise, and self-hosted) land JSONL or Parquet in your own S3, GCS, or Azure bucket, and self-hosters query ClickHouse in SQL.

Sentry stores events in ClickHouse behind [Snuba](https://github.com/getsentry/snuba), its query service, and exposes traces and agent conversations through its API, CLI, and MCP server. Its [retention article](https://www.sentry.help/en/articles/17619175-how-does-trace-sampling-and-data-retention-affect-visibility-in-sentry-io-and-how-can-i-troubleshoot-related-issues) states that Sentry retains full-fidelity spans for 30 days; Business and Enterprise provide additional sampled retention up to 13 months, and legacy transaction-billing arrangements differ.

|                   | Langfuse                                                                                                                                                                                                            | Sentry                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Data store        | **ClickHouse**, [launched 2016 (OSS)](https://clickhouse.com/blog/open-source-10), Apache 2.0; same engine on Cloud and self-hosted                                                                                 | ClickHouse via Snuba, Sentry-operated on SaaS or in the self-hosted stack |
| Raw trace history | 30 days Hobby, 90 days Core, **3 years** Pro and Enterprise                                                                                                                                                         | 30 days full fidelity; sampled up to 13 months on Business and Enterprise |
| Getting data out  | SQL on ClickHouse when self-hosting; Observations and Metrics APIs; [scheduled export](/docs/api-and-data-platform/features/export-to-blob-storage) to your bucket (Pro with Teams add-on, Enterprise, self-hosted) | API, CLI JSON, and MCP for traces and conversations                       |

---

## Pricing [#pricing]

Sentry [prices](https://sentry.io/pricing/) an application-monitoring plan: Developer at $0, Team at $26/month, and Business at $80/month when billed annually with default prepaid data, which includes 5 million spans; errors, logs, replays, and other categories are metered on the same bill. Sentry AI observability is available across plans. [Seer](https://sentry.io/product/seer/) is an optional application-debugging subscription, priced separately at $40 per active contributor per month. Langfuse [Pro](/pricing) is $199/month with 100,000 units included, graduated usage rates after that, unlimited users, 3 years of data access, and Halo on every Cloud plan; scheduled bucket exports and Cloud SSO are the $300/month Teams add-on, and judge inference runs on your own model connection.

The two bills meter different platforms. The $26 estimate is application monitoring with a span allowance; Langfuse's bill starts when you ingest AI traces and scores into an engineering workspace. A team that keeps Sentry and adds Langfuse pays both.

|                 | Langfuse                                                                                    | Sentry                                                                    |
| --------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Entry           | Hobby free (50k units); Core $29; Pro $199                                                  | Developer free; Team $26; Business $80, annual                            |
| What is metered | Traces, observations, scores                                                                | Errors, spans, replays, logs, and other categories                        |
| Retention       | 30 / 90 days / **3 years** (Hobby / Core / Pro)                                             | 30 days full fidelity; sampled up to 13 months on Business and Enterprise |
| In-app AI agent | [Halo](/docs/api-and-data-platform/features/halo) on every Cloud plan, usage limits by plan | Seer, optional, $40 per active contributor/month                          |
| Seats           | Unlimited on Core and above                                                                 | One on Developer; unlimited on Team and Business                          |

See [Langfuse pricing](/pricing) or [talk to us](/talk-to-us) for a volume estimate.

---

## The improvement loop [#improvement-loop]

Langfuse runs the loop in one project. Add a production observation to a [dataset](/docs/evaluation/experiments/datasets), run a [prompt experiment](/docs/evaluation/experiments/experiments-via-ui) in the UI or a full-application experiment through the [SDK](/docs/evaluation/experiments/experiments-via-sdk), [compare the run to a baseline](/docs/evaluation/experiments/compare-experiments), and route outputs to [annotation queues](/docs/evaluation/evaluation-methods/annotation-queues). [Prompt labels](/docs/prompt-management/features/prompt-version-control) promote a version without a redeploy, and the version can carry [model and tool config](/docs/prompt-management/features/config) that your application reads at runtime. [LLM-as-a-judge](/docs/evaluation/evaluation-methods/llm-as-a-judge) and [code evaluators](/docs/evaluation/evaluation-methods/code-evaluators) score incoming observations and experiment runs, a [CI gate](/docs/evaluation/experiments/experiments-ci-cd) fails a build on the result, and [Halo](/docs/api-and-data-platform/features/halo) investigates traces and creates datasets, prompts, and dashboards on request; it is on every Cloud plan and in public beta for self-hosted.

Sentry treats that step as adjacent: its AI observability page says to export conversations with the CLI or MCP server and build datasets in Langfuse, Braintrust, promptfoo, or Phoenix. Seer investigates application errors, drafts a code fix, and reviews pull requests against production errors; it is a debugging agent, not a dataset runner for answer quality.

|                          | Langfuse                                                                                   | Sentry                                               |
| ------------------------ | ------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| After a bad answer       | Dataset, experiment, review, prompt label                                                  | Export the conversation to an eval tool              |
| Judges and code checks   | On observations and experiments inside Langfuse                                            | In the destination tool                              |
| Who runs the experiment  | Prompts and models in the UI; applications through the SDK, compared in Langfuse           | The destination tool                                 |
| Prompt release           | [Python and JS/TS](/docs/prompt-management/get-started), versioned config your app applies | No prompt registry on its AI observability pages     |
| Debugging a thrown error | Trace, log level, and the surrounding tool span                                            | Issue grouping, Seer, and the application trace      |
| CI                       | [GitHub Action](/docs/evaluation/experiments/experiments-ci-cd) on experiment results      | Seer reviews pull requests against production errors |

---

## Using Langfuse and Sentry together [#coexistence]

Leave error monitoring, performance, and session replay in Sentry; its `gen_ai` spans sit inside the application trace next to HTTP, database, and queue spans, and Conversations replays a session as a transcript. Send the agent workflow to Langfuse when the team needs to score it, review it, and change the prompt.

Instrument once with OpenTelemetry and fan out, or run the [Langfuse SDK](/docs/observability/sdk/overview) next to `sentry_sdk`; the [advanced SDK guide](/docs/observability/sdk/advanced-features#isolated-tracer-provider) shows an isolated `TracerProvider` if you want the two backends independent. Sentry's documented export of conversations into a Langfuse dataset covers history that already lives in Sentry.

---

## Which should you choose [#which-should-you-choose]

Choose **Langfuse** if you want **a platform built for AI engineering rather than an add-on to an error tracker**: free self-hosting with SSO and organization RBAC included, datasets, prompt experiments, annotation queues, and prompt labels in one UI with application experiments through the SDK, 3 years of raw history in ClickHouse you can query and export, and unit pricing with unlimited users.

Choose **Sentry agent tracing** if you are **already running Sentry** and the agent failure only has to sit next to the application's errors, traces, and replays.

Run **both** in the common case: Sentry for the application, Langfuse for the AI engineering loop. See [Using Langfuse and Sentry together](#coexistence).

---

## Why teams move away from Sentry agent tracing [#why-teams-move-away]

The same reasons recur in migration conversations.

- **The quality loop is an export.** Sentry's AI observability page sends conversations to Langfuse and other evaluation tools to become datasets. Langfuse runs that loop in one project: the dataset is scored by judges and code evaluators, compared to a baseline, reviewed in an annotation queue, and turned into a [prompt release](#improvement-loop) with a CI gate.
- **Full-fidelity history is 30 days.** Sentry retains full-fidelity spans for 30 days; Business and Enterprise add sampled retention up to 13 months, so a specific conversation from last quarter may not be there to replay. Langfuse Pro keeps **3 years** of the traces you would replay or add to a dataset, on [ClickHouse](#storage) you can query and export.
- **Seer is a separate per-contributor subscription and fixes code.** Sentry's Seer is optional at $40 per active contributor per month, absent from self-hosted, and built for application defects. Langfuse prices units with unlimited users, includes [Halo on every Cloud plan](#pricing), and treats answer quality, rubric review, and prompt versions as the core workflow.
- **Seer stops at the self-hosted boundary.** Sentry documents Seer and other AI and ML features as closed source and unavailable on the Docker Compose install. Langfuse runs evaluators, prompts, the CLI, and the MCP server in its [self-hosted distribution](#open-source-and-deployment), including air-gapped, with Halo in public beta there.

---

## Why teams choose Langfuse [#customers]

A pattern repeats across production adopters: start where governance requires, often self-hosted, then grow into the platform.

- **[Canva](/users/canva)** runs a multi-agent support system for a product with **250 million** monthly active users. LLM-as-a-judge evaluators score the systems across **15–20** metrics, and domain experts build evaluators without an engineering handoff. They self-hosted first, then moved to Cloud.
- **[SumUp](/users/sumup)** rolled AI support to **35+** markets and deflected almost **50%** of conversations, cutting external BPO cost by **30%**. They started self-hosted for the proof of concept, then moved to Langfuse Cloud.
- **[Merck](/users/merckgroup)** runs about **80** of 300+ GenAI use cases on Langfuse, with **200+** people building on it. They self-host for data sovereignty and provision projects via API.

---

## Switching from Sentry agent tracing [#switching-from-sentry]

Many teams do not switch; they add Langfuse and keep Sentry. When Langfuse becomes the system of record for new traces, history stays in Sentry for the plan's retention. Most teams see first traces in Langfuse the **same day**.

- **Instrumentation:** add the [Langfuse SDK](/docs/observability/sdk/overview) or point OpenTelemetry at the [OTLP endpoint](/integrations/native/opentelemetry). Leave the Sentry SDK in place for application errors.
- **Datasets:** export recorded conversations with [Sentry CLI JSON](https://sentry.io/cookbook/agent-conversations-to-evals/) (`sentry agent-conversation list --json`), map the inputs and expected outputs, and load them into a Langfuse [dataset](/docs/evaluation/experiments/datasets). Prefer the CLI for bulk payloads; Sentry notes that MCP responses may be truncated. Once traces land in Langfuse, add production observations from the UI.
- **Prompts and judges:** create them in [prompt management](/docs/prompt-management/get-started) and [evaluators](/docs/evaluation/overview).

[Talk to us](/talk-to-us) if you want help planning the split.

---

## Start free: Cloud or self-host [#get-started]

[Langfuse Cloud](https://cloud.langfuse.com) Hobby includes 50k units/month, no credit card. Or [self-host](/self-hosting) the MIT stack. The [example project](/docs/demo) is populated before you instrument anything.

- [Get started free](https://cloud.langfuse.com)
- [Talk to us](/talk-to-us)

---

## FAQ [#faq]

### Should I replace Sentry with Langfuse? [#should-i-replace-sentry-with-langfuse]

Usually no. Keep Sentry for errors, performance, and replay, and add Langfuse as the AI engineering platform: an open-source core for datasets, experiments, annotation queues, and prompt labels on the same production traces, with 3 years of history on Pro. Sentry already documents exporting conversations to Langfuse for evaluation. See [Using Langfuse and Sentry together](#coexistence).

### Does Sentry trace AI agents? [#does-sentry-trace-agents]

Yes. Agent tracing records model calls, tool executions, MCP calls, and handoffs inside the application trace, and Conversations replays the session. Sentry states it is available on every plan, including the free Developer plan, and Seer is a separate optional subscription. See [Using Langfuse and Sentry together](#coexistence).

### Is Sentry Seer an LLM evaluator? [#is-seer-an-llm-evaluator]

No. Seer is Sentry's debugging agent for application issues: it investigates errors, drafts fixes, and reviews pull requests, as an optional subscription at $40 per active contributor per month on paid plans, and it is not available on self-hosted Sentry. Dataset experiments, judges, and prompt management are the Langfuse side of this comparison. See [The improvement loop](#improvement-loop).

### Can I self-host Sentry's agent tracing and Seer? [#can-i-self-host-sentry-ai-features]

Sentry offers a self-hosted Docker Compose install under the Functional Source License. Its docs list Seer and other AI and ML features as closed source and unavailable there; check agent-tracing availability for the version you deploy. Langfuse self-hosts evaluators and prompts with the rest of its open-source core, with Halo in public beta on self-hosted. See [Open source and deployment](#open-source-and-deployment).

### How does Sentry pricing compare to Langfuse? [#how-does-sentry-pricing-compare]

They meter different platforms. Sentry's default annual Team price is $26/month with 5 million spans and the rest of the application quotas; AI observability is included across plans, and Seer is an optional $40 per active contributor per month. Langfuse Pro is $199/month plus units, with unlimited users and 3 years of retention; judge inference runs on your model connection, and scheduled exports are the Teams add-on. See [Pricing](#pricing).

### How do I send Sentry conversations to Langfuse? [#how-do-i-send-sentry-conversations-to-langfuse]

Export recorded conversations with the Sentry CLI as JSON, map the inputs and expected outputs, and load them into a Langfuse dataset; Sentry's cookbook recommends the CLI over MCP for bulk payloads because MCP responses may be truncated. New traces can go straight to Langfuse via the SDK or OpenTelemetry. See [Switching from Sentry agent tracing](#switching-from-sentry).

[Ask another question](/docs/ask-ai)

  This comparison is out of date? Please [raise a pull request](https://github.com/langfuse/langfuse-docs/blob/main/content/compare/sentry.mdx) with up-to-date information.

**Start with Langfuse** [Sign up](/cloud)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/compare/sentry.md`.

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

