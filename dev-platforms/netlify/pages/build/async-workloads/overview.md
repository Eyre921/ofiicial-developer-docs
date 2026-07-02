---
title: "Netlify Async Workloads Overview"
source: https://docs.netlify.com/build/async-workloads/overview.md
path: build/async-workloads/overview
---

---
title: "Async Workloads overview"
description: "Use Async Workloads to add serverless, durable compute and event-driven architecture to your site without managing all of the messy infrastructure."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Netlify Async Workloads is a powerful tool that enables developers to build resilient, scalable, and event-driven applications without the need to manage infrastructure and queues. With Async Workloads, complex workflows such as handling multi-step workflows, retries, and ensuring fault tolerance are simplified, allowing developers to focus on functionality rather than infrastructure management.

## Key features of Async Workloads:

- **Durable execution:** handle failures automatically, retrying workloads with default or custom limits and schedules if they fail due to issues like network errors, timeouts, or third-party service outages.
- **Event-based architecture:** workloads are triggered by specific events, decoupling the client from directly interacting with single entry points. This allows for more scalable, asynchronous processing of tasks.
- **Multi-step workflows:** Developers can break down workloads into discrete, retryable steps. If a step succeeds, it won't be repeated on a retry, making the process more efficient and resilient.
- **Scheduling and sleeping:** workloads can represent full workflows including intervals of time between processes. Easily schedule or pause a workflow for a set amount of time based on user conditions (like sending a follow-up email 7 days into a 10-day trial).
- **Simple developer experience:** developers can easily create event-driven workflows without managing any infrastructure. By using Netlify's existing serverless platform, Async Workloads eliminates the need to provision, scale, or maintain compute resources.

## Platform extension

Async Workloads is provided as a Netlify Extension so that it can be enabled on any site and plan level. This is an exemplary showcase of the power of Netlify's composable platform and extensibility. The extension uses the serverless resources on the site to do all of its internal work with controls to adjust the frequency of the background work it performs.

The system provisions serverless functions and blobs on the site to handle all internal processes. The usage of Async Workloads provisioned resources is billed as any other provisioned resources. So instead of buying, hosting, and managing a queueing system, Async Workloads uses access to the serverless functions and blobs on the site to do all of its internal work.

## Modify configuration
To update the Async Workloads configuration settings for your site:

For team-level configuration (not available for teams using the Starter plan):
1. In the Netlify UI, navigate to the [Async Workloads extension details page](https://app.netlify.com/extensions/async-workloads).
1. Update your configuration and then select **Save**.

For site-level configuration:
1. In the Netlify UI, navigate to 
### NavigationPath Component:

Project configuration > Build & Deploy > Async Workloads
 for the project you want to edit.
1. Update your configuration and then select **Save**.

Refer to [Async Workloads configuration settings](/build/async-workloads/optional-configuration) for more information.

## Uninstall the extension

As a Team Owner, to uninstall the Async Workloads extension:

1. In the Netlify UI, navigate to the 
### NavigationPath Component:

Extensions
 page for your team.
2. Search for `Async Workloads` and select it in the search results.
3. On the details page, navigate to the **Danger zone** section, and then select **Uninstall this extension**.

