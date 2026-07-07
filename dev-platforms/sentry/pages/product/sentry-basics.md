---
title: "Getting Started With Sentry"
source: https://docs.sentry.io/product/sentry-basics.md
path: product/sentry-basics
---

---
title: "Getting Started With Sentry"
description: "Set up Sentry and configure the key features that help you find and fix problems faster."
url: https://docs.sentry.io/product/sentry-basics/
---

# Getting Started With Sentry

Sentry captures errors, logs, traces, replays, profiles, and metrics from your application — and connects them all through distributed tracing. This page walks you through the steps to get the most out of Sentry **after you've [installed the SDK](https://docs.sentry.io/platforms.md)**.

**New to Sentry? → [Sign up here](https://sentry.io/signup/)** or [try the sandbox](https://sandbox.sentry.io/) to explore the product without installing anything.

## [Step 1: Connect Your Source Code](https://docs.sentry.io/product/sentry-basics.md#step-1-connect-your-source-code)

Connecting your source code repository is the single most impactful setup step. It unlocks:

* **[Suspect commits](https://docs.sentry.io/product/issues/suspect-commits.md)** — Sentry identifies the most likely commit that introduced an error
* **[Seer AI debugging](https://docs.sentry.io/product/ai-in-sentry/seer.md)** — root cause analysis, [Autofix](https://docs.sentry.io/product/ai-in-sentry/seer/autofix.md) (automatic PR generation), and [AI Code Review](https://docs.sentry.io/product/ai-in-sentry/seer/code-review.md)
* **Stack trace links** — click from a stack trace directly to the line in your repo
* **Readable stack traces** — upload [source maps](https://docs.sentry.io/platforms/javascript/sourcemaps.md) (JavaScript) or [debug symbols](https://docs.sentry.io/platforms/native/data-management/debug-files.md) (native) for de-minified/de-obfuscated stack traces

Set up your [GitHub](https://docs.sentry.io/integrations/source-code-mgmt/github.md), [GitLab](https://docs.sentry.io/integrations/source-code-mgmt/gitlab.md), or [Bitbucket](https://docs.sentry.io/integrations/source-code-mgmt/bitbucket.md) integration in **[Settings > Integrations](https://sentry.io/orgredirect/organizations/:orgslug/settings/integrations/)**.

## [Step 2: Set Up Alerts and Notifications](https://docs.sentry.io/product/sentry-basics.md#step-2-set-up-alerts-and-notifications)

Alerts make sure the right people know when things go wrong. Sentry supports:

* **[Alerts](https://docs.sentry.io/product/monitors-and-alerts/alerts.md)** — notify on new errors, regressions, error spikes, or when thresholds like error rate, latency and crash-free session rate are crossed
* **[Uptime monitors](https://docs.sentry.io/product/monitors-and-alerts/monitors/uptime-monitoring.md)** — watch your endpoints for downtime
* **[Cron monitors](https://docs.sentry.io/product/monitors-and-alerts/monitors/crons.md)** — track scheduled jobs for failures or missed runs

Route alerts to [Slack](https://docs.sentry.io/integrations/notification-incidents/slack.md), [Discord](https://docs.sentry.io/integrations/notification-incidents/discord.md), [PagerDuty](https://docs.sentry.io/integrations/notification-incidents/pagerduty.md), or your [issue tracker](https://docs.sentry.io/integrations/issue-tracking.md) (Jira, Linear, GitHub Issues). See [alert best practices](https://docs.sentry.io/product/monitors-and-alerts/alerts.md#alerts-best-practices) for tips on avoiding noise.

## [Step 3: Turn On More Features](https://docs.sentry.io/product/sentry-basics.md#step-3-turn-on-more-features)

After basic error monitoring, these features add the debugging context that will help you find and fix problems faster:

| Feature                                                                | What it adds                                                | Set up                                                                                                           |
| ---------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **[Tracing](https://docs.sentry.io/product/trace-explorer.md)**        | Follow requests across services, find slow queries and N+1s | Enable `tracesSampleRate` in SDK config                                                                          |
| **[Logs](https://docs.sentry.io/product/logs.md)**                     | Structured logs alongside errors and traces                 | Enable `enableLogs: true` in SDK config — [set up guide](https://docs.sentry.io/product/logs/getting-started.md) |
| **[Session Replay](https://docs.sentry.io/product/session-replay.md)** | Video-like recordings of user sessions (web and mobile)     | Enable replay in SDK config                                                                                      |
| **[Profiling](https://docs.sentry.io/product/profiling.md)**           | CPU profiles showing which functions are slow               | Enable profiling in SDK config                                                                                   |
| **[Application Metrics](https://docs.sentry.io/product/metrics.md)**   | Custom counters, gauges, distributions                      | Add metric calls to your code                                                                                    |
| **[User Feedback](https://docs.sentry.io/product/user-feedback.md)**   | Collect bug reports from users, linked to errors            | Add the feedback widget                                                                                          |

Check out Sentry's [cookbooks](https://sentry.io/cookbook/) to learn more about how others use Sentry, and how to go deeper with each of Sentry's tools.

## [Step 4: Explore Your Data](https://docs.sentry.io/product/sentry-basics.md#step-4-explore-your-data)

Once data is flowing, use these tools to understand your application's health:

* **[Dashboards](https://docs.sentry.io/product/dashboards.md)** — pre-built views for frontend, backend, mobile, and AI performance, plus custom dashboards
* **[Trace Explorer](https://docs.sentry.io/product/trace-explorer.md)** — search, filter, and aggregate span data to find performance bottlenecks
* **[Releases](https://docs.sentry.io/product/releases.md)** — track crash-free sessions, version adoption, and regressions by deploy

## [Learn More](https://docs.sentry.io/product/sentry-basics.md#learn-more)

### [Practical Guides](https://docs.sentry.io/product/sentry-basics.md#practical-guides)

Our **[Guides](https://docs.sentry.io/guides.md)** cover real-world patterns for each feature:

* [What to Prioritize](https://docs.sentry.io/guides/issues-errors.md) — error handling and triage strategies
* [What to Log](https://docs.sentry.io/guides/logs.md) — structured logging patterns
* [What to Track](https://docs.sentry.io/guides/metrics.md) — choosing the right metrics
* [Querying Traces](https://docs.sentry.io/guides/querying-traces.md) — finding slow pages and bottlenecks
* [Adding Custom Spans](https://docs.sentry.io/guides/custom-spans.md) — instrumenting your own code
* [Using Session Replay](https://docs.sentry.io/guides/session-replay.md) — debugging workflows with replays

### [Cookbook](https://docs.sentry.io/product/sentry-basics.md#cookbook)

The **[Sentry Cookbook](https://sentry.io/cookbook/)** has step-by-step recipes for common workflows, including debugging with MCP + Cursor, setting up AI observability, creating dashboards with AI agents, and more.

### [Interactive Resources](https://docs.sentry.io/product/sentry-basics.md#interactive-resources)

* **[Sandbox](https://sandbox.sentry.io/)** — explore Sentry with pre-populated sample data

### [Tutorials](https://docs.sentry.io/product/sentry-basics.md#tutorials)

Follow along with a sample app to set up error monitoring or distributed tracing end-to-end:

* #### [Performance Monitoring](https://docs.sentry.io/product/sentry-basics/performance-monitoring.md)

  Track application performance across your full stack with distributed tracing, automated issue detection, and pre-built dashboards.

* #### [User Feedback Basics](https://docs.sentry.io/product/sentry-basics/user-feedback-basics.md)

  Learn how to configure and deploy Sentry's User Feedback widget to capture qualitative insights from your users.

## Pages in this section

- [Distributed Tracing Tutorial](https://docs.sentry.io/product/sentry-basics/distributed-tracing.md)
- [Performance Monitoring](https://docs.sentry.io/product/sentry-basics/performance-monitoring.md)
- [User Feedback Basics](https://docs.sentry.io/product/sentry-basics/user-feedback-basics.md)
- [Frontend Error Monitoring Tutorial](https://docs.sentry.io/product/sentry-basics/integrate-frontend.md)
- [Backend Error Monitoring Tutorial](https://docs.sentry.io/product/sentry-basics/integrate-backend.md)

