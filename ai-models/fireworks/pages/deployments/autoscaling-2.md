---
title: "Autoscaling"
source: https://docs.fireworks.ai/deployments/autoscaling
path: deployments/autoscaling
---

Configure how your deployment scales based on traffic

Control how your deployment scales based on traffic and load.

## Configuration options

| Flag                     | Type      | Default       | Description                                            |
| ------------------------ | --------- | ------------- | ------------------------------------------------------ |
| `--min-replica-count`    | Integer   | 0             | Minimum number of replicas. Set to 0 for scale-to-zero |
| `--max-replica-count`    | Integer   | 1             | Maximum number of replicas                             |
| `--scale-up-window`      | Duration  | 30s           | Wait time before scaling up                            |
| `--scale-down-window`    | Duration  | 10m           | Wait time before scaling down                          |
| `--scale-to-zero-window` | Duration  | 1h            | Idle time before scaling to zero (min: 5m)             |
| `--load-targets`         | Key-value | `default=0.8` | Scaling thresholds. See options below                  |

**Load target options** (use as `--load-targets <key>=<value>[,<key>=<value>...]`):

* `default=<Fraction>` - General load target from 0 to 1
* `tokens_generated_per_second=<Integer>` - Desired tokens per second per replica
* `prompt_tokens_per_second=<Integer>` - Desired prompt tokens per second per replica
* `requests_per_second=<Number>` - Desired requests per second per replica
* `concurrent_requests=<Number>` - Desired concurrent requests per replica

When multiple targets are specified, the maximum replica count across all is used.

## Common patterns

<Tabs>
  <Tab title="Cost optimization">
    Scale to zero when idle to minimize costs:

    ```bash theme={null}
    firectl deployment create <MODEL_NAME> \
      --min-replica-count 0 \
      --max-replica-count 3 \
      --scale-to-zero-window 1h
    ```

    Best for: Development, testing, or intermittent production workloads.
  </Tab>

  <Tab title="Performance-focused">
    Keep replicas running for instant response:

    ```bash theme={null}
    firectl deployment create <MODEL_NAME> \
      --min-replica-count 2 \
      --max-replica-count 10 \
      --scale-up-window 15s \
      --load-targets concurrent_requests=5
    ```

    Best for: Low-latency requirements, avoiding cold starts, high-traffic applications.
  </Tab>

  <Tab title="Predictable traffic">
    Match known traffic patterns:

    ```bash theme={null}
    firectl deployment create <MODEL_NAME> \
      --min-replica-count 3 \
      --max-replica-count 5 \
      --scale-down-window 30m \
      --load-targets tokens_generated_per_second=150
    ```

    Best for: Steady workloads where you know typical load ranges.
  </Tab>
</Tabs>

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

<Warning>
  Requests to a scaled-to-zero deployment are **not queued**. Your application must implement retry logic to handle `503` responses while the deployment scales up.
</Warning>

### Handling scale-from-zero responses

Implement retry logic with exponential backoff to gracefully handle scale-up delays:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    import time
    import requests

    def query_deployment_with_retry(url, payload, max_retries=30, initial_delay=5):
        """Query a deployment with retry logic for scale-from-zero scenarios."""
        delay = initial_delay
        
        for attempt in range(max_retries):
            response = requests.post(url, json=payload, headers=headers)
            
            # Only retry if deployment is scaling up
            if response.status_code == 503:
                error_code = response.json().get("error", {}).get("code")
                if error_code == "DEPLOYMENT_SCALING_UP":
                    print(f"Deployment scaling up, retrying in {delay}s...")
                    time.sleep(delay)
                    delay = min(delay * 1.5, 60)  # Cap at 60 seconds
                    continue
                
            response.raise_for_status()
            return response.json()
        
        raise Exception("Deployment did not scale up in time")
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript theme={null}
    async function queryDeploymentWithRetry(url, payload, maxRetries = 30, initialDelay = 5000) {
      let delay = initialDelay;
      
      for (let attempt = 0; attempt < maxRetries; attempt++) {
        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', ...headers },
          body: JSON.stringify(payload)
        });
        
        // Only retry if deployment is scaling up
        if (response.status === 503) {
          const body = await response.json();
          if (body.error?.code === 'DEPLOYMENT_SCALING_UP') {
            console.log(`Deployment scaling up, retrying in ${delay/1000}s...`);
            await new Promise(resolve => setTimeout(resolve, delay));
            delay = Math.min(delay * 1.5, 60000); // Cap at 60 seconds
            continue;
          }
        }
        
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      }
      
      throw new Error('Deployment did not scale up in time');
    }
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    # Simple retry loop for scale-from-zero
    MAX_RETRIES=30
    RETRY_DELAY=5

    for i in $(seq 1 $MAX_RETRIES); do
      response=$(curl -s -w "\n%{http_code}" \
        https://api.fireworks.ai/inference/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $FIREWORKS_API_KEY" \
        -d '{"model": "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>", ...}')
      
      http_code=$(echo "$response" | tail -n1)
      body=$(echo "$response" | head -n -1)
      
      # Only retry if deployment is scaling up
      if [ "$http_code" -eq 503 ]; then
        error_code=$(echo "$body" | jq -r '.error.code // empty')
        if [ "$error_code" = "DEPLOYMENT_SCALING_UP" ]; then
          echo "Deployment scaling up, retrying in ${RETRY_DELAY}s..."
          sleep $RETRY_DELAY
          RETRY_DELAY=$((RETRY_DELAY * 2))
          continue
        fi

        echo "$body"
        exit 1
      fi
      
      # Check for success (2xx status codes)
      if [ "$http_code" -ge 200 ] && [ "$http_code" -lt 300 ]; then
        echo "$body"
        exit 0
      fi

      echo "$body"
      exit 1
    done

    echo "Deployment did not scale up in time"
    exit 1
    ```
  </Tab>
</Tabs>

<Tip>
  Cold start times vary depending on model size—larger models may take longer to download and initialize. If you need instant responses without cold starts, set `--min-replica-count 1` or higher to keep replicas always running.
</Tip>

<Note>
  Deployments with min replicas = 0 are auto-deleted after 7 days of no traffic. [Reserved capacity](/deployments/reservations) guarantees availability during scale-up.
</Note>
