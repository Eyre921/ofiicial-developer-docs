---
title: "Async Workloads Configuration"
source: https://docs.netlify.com/build/async-workloads/optional-configuration.md
path: build/async-workloads/optional-configuration
---

---
title: "Optional Configuration"
description: "How Async Workloads can be configured to meet the unique needs of websites."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

While the Async Workload extension is installed on the team level, there are a few site-level configurations that can be set to customize the behavior of Async Workloads.

## Modify your configuration
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

Alternatively, you can update the environment variables directly.

## Async Workloads API key

To ensure that only allowed clients can invoke workloads and related APIs, requests must provide an `Authorization` header with an API key that's known by Async Workloads.

When you install the Async Workloads extension, a new randomly generated API key is created on the team level. This key is used to authenticate requests to the Async Workload API. For teams on the Starter plan, you must create an API key on each of the sites that will use the Async Workloads extension.

This value is persisted under the `AWL_API_KEY` and `AWL_API_KEY_P{priority_integer}` convention environment variables.

### Create and rotate keys

For team-level API keys, navigate to the [Async Workloads extension details page](https://app.netlify.com/extensions/async-workloads). Select **Create a new API key** to input and save a new API key. For customers using Starter plans, this option is not available and the configurations must be managed on the site level.

For project scoped API keys, navigate to 
### NavigationPath Component:

Project configuration > Build & Deploy > Async Workloads
 in the Netlify UI. Select **Create a new API key** to input and save the new API key.

When you create a new API key, you must provide an **API key priority** and an **API key value**.

The **API key priority** is an integer that signals the priority of an API key - the higher the number, the higher the priority. Where the system automatically uses the API keys in making requests - like the router sending events to workloads - it will use the highest priority key available.

The **API key value** is the actual key that will be used for authentication.

Setting multiple keys allows teams to safely rotate keys and explicitly set priority for which keys to use internally. When rotating API keys, you can create a new key that has a higher priority than the existing keys. Once all clients are using the new keys, you can delete the older, lower priority keys. Redeploy the sites that Async Workloads runs on first, then any client-only sites.

To aid in the safe rotations of keys, if the system detects that a key being used is not the highest priority key, it will log a warning like `Lower priority key named "${keyName}" is being used for this request`. If these warnings are not present then there are no lower priority keys being used.

To delete API keys, delete the **API key value** field contents and save the changes. This will remove the API key from the site.

## Pending Processor Upper Limit

The pending processor is the system that picks up scheduled events and sends them to the Async Workloads router layer. To prevent your site from consuming a large amount of resources unexpectedly, Async Workloads will determine if the quantity of pending events is above a certain threshold limit. If it is, Async Workloads sees this as a potential infinite looping system. In that case, router layer will not be sent any more events from the pending processor until the number of pending events is below the limit. This limit can be configured if it's too low or too high for your sites needs. Async Workloads will still continue to allow events to be scheduled without data loss. Only the process of taking scheduled events and sending them to the router layer is disabled. The default is `2000`.

This value is persisted under the `AWL_PENDING_UPPER_LIMIT` environment variable.

## Serverless timeout limit

This is the max number of seconds Async Workloads should wait for timeout detection. This only applies to standard serverless functions as background functions use a 15 minute timeout. The [default deployment options](/build/functions/overview#default-deployment-options) for standard serverless functions includes a 60 second timeout. If deployment options are changed to have a higher or lower execution limit, or if timeout detection should be more aggressive for a site, this where that timeout limit can be set.

This value is persisted under the `AWL_SERVERLESS_TIMEOUT` environment variable.

## Workload chaining limit

Workload chains happen when one workload sends an event that triggers another workload. It's possible to have one workload invoke another workload which then re-invokes the original workload - causing an infinite loop of workload events. To avoid this from causing unexpected resource consumption, there is automatic chain limit detection. The default chain limit is 20. If it is necessary to have a larger limit, this limit can be set on this configuration.

This value is persisted under the `AWL_EVENT_CHAIN_LIMIT` environment variable.

## Scheduler polling interval

To run an async event queue system, there are processes that run in the background to ensure retries happen, delayed events are triggered after the delay, etc. This is achieved by running a serverless scheduler function on the site at appropriate intervals of time.

Adjustments to the polling interval of the scheduler will allow it to run more or less frequently. This only impacts the production scheduler.

The default value is `60` second intervals between each scheduler run. The minimum value is `10` seconds. For example, if you want to run it once every 5 minutes, you would set the value to `300`. The max value is `900` or 15 minutes. Values greater than `60` are rounded to the nearest minute.

### Which interval is best?

The more events that are expected to be delayed, errored, etc. the lower the interval should be to process them promptly. The recommendation is to start with the default and use the function logs and stored state, to determine if the interval should be changed to process delayed events more or less often.

### Local and branch scheduler

In production environments, the Async Workload scheduler runs continuously on an interval.

In non-production environments (dev, branch deploys, etc.), the scheduler runs only on "stateful" actions (for example, when processing or retrying events). This prevents unnecessary compute usage on environments that are not serving production traffic. Once triggered, the scheduler runs briefly and exits. This behavior cannot be disabled.

This value is persisted under the `AWL_SCHEDULER_INTERVAL` environment variable.

