---
title: "Datadog"
source: https://docs.pinecone.io/integrations/datadog
path: integrations/datadog
---

Monitor Pinecone with the Datadog integration to track request latency, index fullness, and usage trends, and alert on anomalies in vector workloads.

<Note>
  This feature is available on the [Builder, Standard, and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

Datadog is a monitoring and analytics tool that tracks performance metrics and monitors events for infrastructure and cloud services. You can use Datadog with Pinecone in the following ways:

* Track specific actions within Pinecone, such as request count, to find application requests with high latency or usage. Monitor trends over time to improve resource utilization and reduce spend.
* Get alerted automatically when index fullness reaches a certain threshold. You can also create your own monitors to alert on specific metrics and thresholds.
* Find and triage unexpected spikes in usage or latency by visualizing anomalies in Pinecone's Datadog dashboard. View metrics over time to understand trends and determine the severity of a spike.

<PrimarySecondaryCTA />

## Setup guide

Follow these steps to monitor a Pinecone project with Datadog:

1. Go to the [Pinecone integration](https://app.datadoghq.com/integrations/pinecone) tile in Datadog.
2. Go to the **Configure** tab.
3. Click **+ Add New**.
4. Enter a project name to identify your project in Datadog.
5. Don't select an environment. This is a legacy setting.
6. Enter an [API key](/guides/projects/understanding-projects#api-keys) for the Pinecone project you want to monitor.
7. Enter the [project ID](/guides/projects/understanding-projects#project-ids) of the Pinecone project you want to monitor.
8. Save the configuration.

On the **Monitoring Resources** tab, you'll find dashboards for the pod-based and serverless indexes in your project and recommendations for [configuring monitors](https://docs.datadoghq.com/monitors/configuration/?tab=thresholdalert) using [Pinecone's metrics](/guides/production/monitoring#available-metrics).
