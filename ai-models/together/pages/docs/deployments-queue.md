---
title: "Queue API"
source: https://docs.together.ai/docs/deployments-queue
path: docs/deployments-queue
---

Submit, monitor, and manage asynchronous jobs for your Dedicated Container deployments.

The Queue API provides asynchronous job processing for Dedicated Containers. Submit jobs to a managed queue, and workers automatically claim and process them. This model supports long-running inference, batch workloads, and explicit priority control.

<Tip>
  **New to Dedicated Containers?** Start with the [Overview](/docs/dedicated-container-inference) to understand the platform, or jump to the [Quickstart](/docs/containers-quickstart) to deploy your first container.
</Tip>

## Core Concepts

### Jobs

A **job** is a single unit of work submitted to your deployment. Jobs can run for seconds or hours, making them ideal for:

* Video generation
* Batch image processing
* Long-running inference tasks
* Any workload that doesn't fit the request-response pattern

### Job Lifecycle

| Status     | Description                                     |
| ---------- | ----------------------------------------------- |
| `pending`  | Job is queued, waiting for a worker to claim it |
| `running`  | Job has been claimed and is being processed     |
| `done`     | Job completed successfully                      |
| `failed`   | Job failed with an error                        |
| `canceled` | Job was canceled before processing started      |

### Priority

Jobs are processed in strict order of **priority first, then submission time**. Priority is an integer where higher values are processed first.

```python theme={null}
# High priority job (processed first)
client.beta.queue.submit(model="my-model", payload={...}, priority=10)

# Normal priority job
client.beta.queue.submit(model="my-model", payload={...}, priority=1)

# Low priority job (processed last)
client.beta.queue.submit(model="my-model", payload={...}, priority=0)
```

<Note>
  By default, priority is **not** considered for autoscaling metrics—the autoscaler scales based on total queue depth regardless of priority. Contact [support@together.ai](mailto:support@together.ai) for advanced scaling policies that account for priority tiers.
</Note>

### Job State with `info`

The `info` field provides persistent state that survives across the job lifecycle. You can:

1. **Set initial state** when submitting a job via the `info` parameter
2. **Update state** during processing using `emit()` in your Sprocket worker
3. **Preserve state** across retries—`info` accumulates rather than resets

This is useful for tracking progress, storing metadata, or passing context between retries.

<CodeGroup>
  ```python Submit with initial info theme={null}
  job = client.beta.queue.submit(
      model="my-model",
      payload={"prompt": "A cat playing piano"},
      info={"user_id": "user_123", "tier": "premium"},
  )
  ```

  ```python Update info during processing (in Sprocket) theme={null}
  from sprocket import emit


  def predict(self, args: dict) -> dict:
      emit({"progress": 0.5, "stage": "encoding"})
      # ... more processing
      emit({"progress": 1.0, "stage": "complete"})
      return {"output": result}
  ```
</CodeGroup>

For full endpoint documentation — request parameters, response schemas, and error codes — see the [Queue REST API Reference](/reference/queue-submit): [submit](/reference/queue-submit), [status](/reference/queue-status), [cancel](/reference/queue-cancel), [metrics](/reference/queue-metrics).

## Polling for Job Completion

For jobs that take time to complete, poll the status endpoint until the job reaches a terminal state (`done`, `failed`, or `canceled`).

<CodeGroup>
  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  # Submit job
  job = client.beta.queue.submit(
      model="my-deployment", payload={"prompt": "Generate a video of a sunset"}
  )

  print(f"Submitted job: {job.request_id}")

  # Poll for completion
  while True:
      status = client.beta.queue.retrieve(
          request_id=job.request_id, model="my-deployment"
      )

      if status.status == "done":
          print(f"Success! Result: {status.outputs}")
          break
      elif status.status == "failed":
          print(f"Failed: {status.error}")
          break
      elif status.status == "canceled":
          print("Job was canceled")
          break
      else:
          # Show progress if available
          if status.info and "progress" in status.info:
              print(f"Progress: {status.info['progress']:.0%}")
          time.sleep(2)  # Poll every 2 seconds
  ```

  ```shell Bash theme={null}
  #!/bin/bash
  REQUEST_ID="019ba379-92da-71e4-ac40-d98059fd67c7"
  MODEL="my-deployment"

  while true; do
    RESPONSE=$(curl -s "https://api.together.ai/v1/queue/status?request_id=$REQUEST_ID&model=$MODEL" \
      -H "Authorization: Bearer $TOGETHER_API_KEY")

    STATUS=$(echo $RESPONSE | jq -r '.status')

    case $STATUS in
      "done")
        echo "Success!"
        echo $RESPONSE | jq '.outputs'
        break
        ;;
      "failed")
        echo "Failed:"
        echo $RESPONSE | jq '.error'
        break
        ;;
      "canceled")
        echo "Cancelled"
        break
        ;;
      *)
        echo "Status: $STATUS"
        sleep 2
        ;;
    esac
  done
  ```
</CodeGroup>

***

## Best Practices

### Use Priority for Tiered Service

Implement different service tiers by assigning priority based on customer type:

```python theme={null}
def submit_job(user, payload):
    priority = 10 if user.tier == "premium" else 1
    return client.beta.queue.submit(
        model="my-deployment",
        payload=payload,
        priority=priority,
        info={"user_id": user.id, "tier": user.tier},
    )
```

### Track Progress for Long-Running Jobs

For jobs that take more than a few seconds, emit progress updates so clients can show status:

```python theme={null}
class VideoGenerator(Sprocket):
    def predict(self, args: dict) -> dict:
        total_frames = args.get("num_frames", 60)

        for i, frame in enumerate(self.generate_frames(args)):
            emit(
                {
                    "progress": (i + 1) / total_frames,
                    "current_frame": i + 1,
                    "total_frames": total_frames,
                }
            )

        return {"video": FileOutput("output.mp4")}
```

### Handle All Terminal States

Always check for `done`, `failed`, and `canceled` when polling:

```python theme={null}
terminal_states = {"done", "failed", "canceled"}

while status.status not in terminal_states:
    time.sleep(2)
    status = client.beta.queue.retrieve(...)
```

### Store Metadata in `info`

Use `info` to store job metadata that you'll need when the job completes:

```python theme={null}
job = client.beta.queue.submit(
    model="my-deployment",
    payload={"prompt": "..."},
    info={
        "user_id": "user_123",
        "callback_url": "https://myapp.com/webhook",
        "requested_at": datetime.now().isoformat(),
    },
)
```

***

## Error Codes

| Code  | Description                                                  |
| ----- | ------------------------------------------------------------ |
| `400` | Invalid request (missing required fields, malformed payload) |
| `401` | Unauthorized (invalid or missing API key)                    |
| `404` | Job or deployment not found                                  |
| `409` | Cannot cancel job (already running or completed)             |
| `500` | Internal server error                                        |

***

## Related Resources

* [Dedicated Containers Overview](/docs/dedicated-container-inference) – Architecture and concepts
* [Quickstart](/docs/containers-quickstart) – Deploy your first container
* [Sprocket SDK](/docs/deployments-sprocket) – Build queue-integrated workers
* [Jig CLI](/docs/deployments-jig) – Deploy and manage containers
