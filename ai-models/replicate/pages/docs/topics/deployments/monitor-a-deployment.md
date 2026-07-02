---
title: "Monitor a deployment"
source: https://replicate.com/docs/topics/deployments/monitor-a-deployment.md
path: docs/topics/deployments/monitor-a-deployment
---

Deployments provide tools to help you track performance, diagnose issues, and monitor your model’s health.

[](#metrics-dashboard)Metrics dashboard
---------------------------------------

Each deployment provides a metrics dashboard to help you understand how your model is performing in production.

You can view up to 24 hours of historical metrics data, aggregated into 15-minute intervals.

### [](#available-metrics)Available metrics

The dashboard tracks the following metrics:

*   **Latency**: Track response times and identify performance bottlenecks
*   **Throughput**: Monitor requests per second and capacity utilization
*   **Error rates**: Identify and troubleshoot failed predictions
*   **Instance status**: See how many instances are starting, idle, or actively processing requests
*   **Queue depth**: Monitor pending predictions waiting for processing
*   **GPU memory usage**: Monitor how much GPU memory your deployment is using across all instances

The metrics graphs automatically refresh and provide interactive controls for zooming and filtering data by time range.

Access your deployment metrics by visiting [replicate.com/deployments](https://replicate.com/deployments) and selecting the deployment you want to monitor.

[](#gpu-memory-monitoring)GPU memory monitoring
-----------------------------------------------

GPU memory monitoring helps you optimize resource utilization and ensure your models are running efficiently. The GPU memory visualization shows:

*   **Total memory available**: The total GPU memory capacity allocated to your deployment across all instances.
*   **Memory usage patterns**: Both median and maximum GPU memory usage over configurable time periods (2 hours or 24 hours).
*   **Multi-instance aggregation**: Memory usage is aggregated across all running instances in your deployment, giving you a comprehensive view of resource utilization.

This monitoring helps you:

*   See if your model is using GPU memory efficiently
*   Decide if you need different hardware for better performance
*   Spot memory usage patterns and potential optimizations
*   Plan capacity for scaling your deployment

[](#setup-failure-notifications)Setup failure notifications
-----------------------------------------------------------

Info

This feature is only available for users with an enterprise contract. To learn more about our enterprise plan, reach out to [sales@replicate.com](mailto:sales@replicate.com).

You can choose to get notified via email when your deployment fails during the model’s [setup function](https://cog.run/python/#predictorsetup).

The alert includes:

*   The name of the deployment
*   URL of the version that failed setup
*   If relevant, any actions that we’ve automatically taken (like rolling back to a previous version)

To turn on setup failure alerts:

1.  Configure your email address:
    *   Go to your account settings at [replicate.com/account](https://replicate.com/account)
    *   Navigate to the **General** tab
    *   Set your preferred email address for notifications
2.  Turn on alerts for your deployment:
    *   Go to your deployment page at [replicate.com/deployments](https://replicate.com/deployments)
    *   Select the deployment you want to monitor
    *   Go to the **Settings** tab
    *   Scroll down to advanced settings and check the box to enable notifications for setup failure

If you use Slack, you can use Slack’s [send emails to Slack](https://slack.com/help/articles/206819278-Send-emails-to-Slack) feature to receive these notifications in a Slack channel.

[](#custom-setup-timeouts)Custom setup timeouts
-----------------------------------------------

Info

This feature is only available for users with an enterprise contract. To learn more about our enterprise plan, reach out to [sales@replicate.com](mailto:sales@replicate.com).

You can customize the timeout for your deployment’s model [setup function](https://cog.run/python/#predictorsetup). The setup timeout determines how long Replicate will wait for a model instance to complete setup before marking it as failed. The default setup timeout is 10 minutes.

To configure the setup timeout:

1.  Navigate to your deployment page at [replicate.com/deployments](https://replicate.com/deployments)
2.  Select the deployment you want to configure
3.  Go to the **Settings** tab
4.  Scroll to **Advanced settings** and pick a duration from 1 minute to 3 hours.

![Setup timeout configuration in deployment settings](/_content/assets/deployment-setup-timeout.FN-shQZL.png)

The default setup timeout is appropriate for most models, but you may need to increase it if your model:

*   Has a large model file that takes time to download
*   Performs complex initialization or preprocessing
*   Requires additional setup steps during instance startup
