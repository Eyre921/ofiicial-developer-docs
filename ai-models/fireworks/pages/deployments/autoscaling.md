---
title: "Autoscaling"
source: https://docs.fireworks.ai/deployments/autoscaling
path: deployments/autoscaling
---

Configure replica counts, scale-up/down windows, scale-to-zero, and load targets for on-demand Fireworks deployments using firectl flags.

Control how your deployment scales based on traffic and load.

## Configuration options

| Flag | Type | Default | Description |
| - | - | - | - |
| `--min-replica-count` | Integer | 0 | Minimum number of replicas. Set to 0 for scale-to-zero |
| `--max-replica-count` | Integer | 1 | Maximum number of replicas |
| `--scale-up-window` | Duration | 30s | How long a higher replica count must be recommended before it applies. See [How scaling decisions work](#how-scaling-decisions-work) |
| `--scale-down-window` | Duration | 10m | How long a lower replica count must be recommended before it applies |
| `--scale-to-zero-window` | Duration | 1h | Idle time before scaling to zero (min: 5m) |
| `--load-targets` | Key-value | `default=0.8` | Scaling thresholds. See options below |

**Load target options** (use as `--load-targets <key>=<value>[,<key>=<value>...]`):

* `default=<Fraction>` - General load target from 0 to 1
* `tokens_generated_per_second=<Integer>` - Desired tokens per second per replica
* `prompt_tokens_per_second=<Integer>` - Desired prompt tokens per second per replica
* `requests_per_second=<Number>` - Desired requests per second per replica
* `concurrent_requests=<Number>` - Desired concurrent requests per replica

When multiple targets are specified, the maximum replica count across all is used.

When you create a deployment, `default=0.8` is added if you don't set `default` yourself. `firectl deployment update --load-targets` replaces all existing load targets, so include `default` in the list if you want to keep it:

```bash theme={null}
firectl deployment update <DEPLOYMENT_ID> --load-targets default=0.8,concurrent_requests=10
```

The console sets one load target at a time, and saving a change there replaces all existing load targets. To combine targets, such as `default` and `concurrent_requests`, use `firectl`.

> [!NOTE]
>
> On deployments served by vLLM or SGLang, `concurrent_requests` counts the requests the engine is actively running. Requests queued inside the engine are not included.

## How scaling decisions work

The autoscaler regularly works out, for each load target, how many replicas would bring the load to that target, and uses the largest of those numbers, between your minimum and maximum replica counts.

**Scale-up window.** The autoscaler applies the lowest replica count recommended during the last `--scale-up-window`. A higher count takes effect only after it has been recommended for the whole window. New replicas then need time to start before they serve traffic, which depends on model size, so extra capacity arrives roughly one window plus the start-up time after load rises. A shorter window reacts faster; a longer one ignores brief spikes.

**Scale-down window.** The autoscaler applies the highest replica count recommended during the last `--scale-down-window`, so a lower count takes effect only after load has stayed lower for the whole window.

**How far one step can go.** `default` tracks how busy each replica is, using measures such as KV-cache usage, compute utilization, or the share of requests waiting, depending on the serving engine. These measures top out at 100% of a replica, so with only `default` set, one scaling step can raise the replica count to at most about `1 / target` times the replicas serving traffic: about 25% more (and at least one more replica) at the default `0.8`. Under a sudden traffic spike the deployment therefore grows in several steps. Per-replica targets such as `concurrent_requests` or `requests_per_second` are not limited to 100%, so a large backlog can add several replicas in one step.

To absorb sharp traffic increases, combine these with a `--min-replica-count` sized for your expected baseline traffic.

## Common patterns

> [tab] Cost optimization
>
> Scale to zero when idle to minimize costs:
>
> ```bash theme={null}
> firectl deployment create <MODEL_NAME> \
>   --deployment-shape default \
>   --min-replica-count 0 \
>   --max-replica-count 3 \
>   --scale-to-zero-window 1h
> ```
>
> Best for: Development, testing, or intermittent production workloads.

> [tab] Performance-focused
>
> Keep replicas running for instant response:
>
> ```bash theme={null}
> firectl deployment create <MODEL_NAME> \
>   --deployment-shape default \
>   --min-replica-count 2 \
>   --max-replica-count 10 \
>   --scale-up-window 15s \
>   --load-targets concurrent_requests=5
> ```
>
> Best for: Low-latency requirements, avoiding cold starts, high-traffic applications.

> [tab] Predictable traffic
>
> Match known traffic patterns:
>
> ```bash theme={null}
> firectl deployment create <MODEL_NAME> \
>   --deployment-shape default \
>   --min-replica-count 3 \
>   --max-replica-count 5 \
>   --scale-down-window 30m \
>   --load-targets tokens_generated_per_second=150
> ```
>
> Best for: Steady workloads where you know typical load ranges.

## Scaling from zero behavior

When a deployment is scaled to zero and receives a request, the system immediately returns a `503` error with the `DEPLOYMENT_SCALING_UP` error code while initiating the scale-up process:

```json theme={null}
{
  "error": {
    "message": "Deployment is currently scaled to zero and is scaling up. Please retry your request in a few minutes.",
    "code": "DEPLOYMENT_SCALING_UP",
    "type": "error"
  }
}
```

> [!WARNING]
>
> Requests to a scaled-to-zero deployment are **not queued**. Your application must implement retry logic to handle `503` responses while the deployment scales up.

### Handling scale-from-zero responses

Implement retry logic with exponential backoff to gracefully handle scale-up delays:

> [tab] Python
>
> ```python theme={null}
> import time
> import requests
>
> def query_deployment_with_retry(url, payload, max_retries=30, initial_delay=5):
>     """Query a deployment with retry logic for scale-from-zero scenarios."""
>     delay = initial_delay
>
>     for attempt in range(max_retries):
>         response = requests.post(url, json=payload, headers=headers)
>
>         # Only retry if deployment is scaling up
>         if response.status_code == 503:
>             error_code = response.json().get("error", {}).get("code")
>             if error_code == "DEPLOYMENT_SCALING_UP":
>                 print(f"Deployment scaling up, retrying in {delay}s...")
>                 time.sleep(delay)
>                 delay = min(delay * 1.5, 60)  # Cap at 60 seconds
>                 continue
>
>         response.raise_for_status()
>         return response.json()
>
>     raise Exception("Deployment did not scale up in time")
> ```

> [tab] JavaScript
>
> ```javascript theme={null}
> async function queryDeploymentWithRetry(url, payload, maxRetries = 30, initialDelay = 5000) {
>   let delay = initialDelay;
>
>   for (let attempt = 0; attempt < maxRetries; attempt++) {
>     const response = await fetch(url, {
>       method: 'POST',
>       headers: { 'Content-Type': 'application/json', ...headers },
>       body: JSON.stringify(payload)
>     });
>
>     // Only retry if deployment is scaling up
>     if (response.status === 503) {
>       const body = await response.json();
>       if (body.error?.code === 'DEPLOYMENT_SCALING_UP') {
>         console.log(`Deployment scaling up, retrying in ${delay/1000}s...`);
>         await new Promise(resolve => setTimeout(resolve, delay));
>         delay = Math.min(delay * 1.5, 60000); // Cap at 60 seconds
>         continue;
>       }
>     }
>
>     if (!response.ok) throw new Error(`HTTP ${response.status}`);
>     return response.json();
>   }
>
>   throw new Error('Deployment did not scale up in time');
> }
> ```

> [tab] curl
>
> ```bash theme={null}
> # Simple retry loop for scale-from-zero
> MAX_RETRIES=30
> RETRY_DELAY=5
>
> for i in $(seq 1 $MAX_RETRIES); do
>   response=$(curl -s -w "\n%{http_code}" \
>     https://api.fireworks.ai/inference/v1/chat/completions \
>     -H "Content-Type: application/json" \
>     -H "Authorization: Bearer $FIREWORKS_API_KEY" \
>     -d '{"model": "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>", ...}')
>
>   http_code=$(echo "$response" | tail -n1)
>   body=$(echo "$response" | head -n -1)
>
>   # Only retry if deployment is scaling up
>   if [ "$http_code" -eq 503 ]; then
>     error_code=$(echo "$body" | jq -r '.error.code // empty')
>     if [ "$error_code" = "DEPLOYMENT_SCALING_UP" ]; then
>       echo "Deployment scaling up, retrying in ${RETRY_DELAY}s..."
>       sleep $RETRY_DELAY
>       RETRY_DELAY=$((RETRY_DELAY * 2))
>       continue
>     fi
>
>     echo "$body"
>     exit 1
>   fi
>
>   # Check for success (2xx status codes)
>   if [ "$http_code" -ge 200 ] && [ "$http_code" -lt 300 ]; then
>     echo "$body"
>     exit 0
>   fi
>
>   echo "$body"
>   exit 1
> done
>
> echo "Deployment did not scale up in time"
> exit 1
> ```

> [!TIP]
>
> Cold start times vary depending on model size—larger models may take longer to download and initialize. If you need instant responses without cold starts, set `--min-replica-count 1` or higher to keep replicas always running.

> [!NOTE]
>
> Deployments with min replicas = 0 are auto-deleted after 7 days of no traffic. [Reserved capacity](/deployments/reservations) guarantees availability during scale-up.
